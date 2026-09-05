"""Retrieve relevant heritage facts for the Q&A agent."""

import re
from pathlib import Path

from app.config import RAWIAI_USE_QDRANT


def _clean_markdown(text: str) -> str:
    """Remove draft comments and simple markdown formatting for narration."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"^\s*#\s+", "", text, flags=re.MULTILINE)
    text = text.replace("**", "")
    return text.strip()


def _local_fallback(query: str, language: str) -> list[dict]:
    """Read heritage narration straight from markdown, no vector search needed."""
    file_name = "al_hisn_fort_ar.md" if language == "ar" else "al_hisn_fort_en.md"
    content_path = Path("app/content") / file_name
    text = _clean_markdown(content_path.read_text(encoding="utf-8"))

    return [
        {
            "site": "Al Hisn Fort",
            "language": language,
            "text": text,
            "query": query,
            "source": "local-markdown",
        }
    ]


def _search_qdrant(query: str, language: str, limit: int = 3) -> list[dict]:
    """Search Qdrant for the narration chunks closest to the visitor's question."""
    from qdrant_client.models import FieldCondition, Filter, MatchValue

    from app.rag.embeddings import embed_text
    from app.rag.qdrant import COLLECTION_NAME, get_qdrant_client

    client = get_qdrant_client()
    vector = embed_text(query)
    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        query_filter=Filter(
            must=[FieldCondition(key="language", match=MatchValue(value=language))]
        ),
        limit=limit,
    )

    facts = [
        {
            "site": point.payload.get("site", "Al Hisn Fort"),
            "language": language,
            "text": point.payload.get("text", ""),
            "query": query,
            "source": "qdrant",
        }
        for point in response.points
        if point.payload and point.payload.get("text")
    ]
    return facts


def retrieve_facts(query: str, language: str = "en") -> list[dict]:
    """Return grounded heritage facts for the Q&A agent.

    Tries Qdrant vector search first when RAWIAI_USE_QDRANT is enabled. Falls
    back to reading the markdown source directly if Qdrant is unreachable or
    has not been ingested yet, so the demo never goes silent.
    """
    if RAWIAI_USE_QDRANT:
        try:
            facts = _search_qdrant(query, language=language)
            if facts:
                return facts
        except Exception:
            pass

    return _local_fallback(query, language)
