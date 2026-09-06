"""Load heritage content into Qdrant.

Run this once (after `docker compose up qdrant`) whenever the content
markdown files change:

    python -m app.rag.ingest
"""

import re
import uuid
from pathlib import Path

from qdrant_client.models import PointStruct

from app.agents.sites import DEMO_SITES
from app.rag.embeddings import embed_text
from app.rag.qdrant import COLLECTION_NAME, ensure_collection, get_qdrant_client

CONTENT_DIR = Path("app/content")


def _clean_markdown(text: str) -> str:
    """Remove draft comments and simple markdown formatting for narration."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"^\s*#\s+.*$", "", text, flags=re.MULTILINE)
    text = text.replace("**", "")
    return text.strip()


def _chunk(text: str) -> list[str]:
    """Split narration into paragraph-sized retrieval chunks."""
    return [paragraph.strip() for paragraph in text.split("\n\n") if paragraph.strip()]


def ingest_content() -> dict:
    """Embed each heritage-content paragraph, for every demo site, into Qdrant."""
    points: list[PointStruct] = []

    for site in DEMO_SITES.values():
        slug = site["id"].replace("-", "_")
        sources = [
            ("en", site["name_en"], CONTENT_DIR / f"{slug}_en.md"),
            ("ar", site["name_ar"], CONTENT_DIR / f"{slug}_ar.md"),
        ]

        for language, site_name, path in sources:
            chunks = _chunk(_clean_markdown(path.read_text(encoding="utf-8")))
            for index, chunk in enumerate(chunks):
                vector = embed_text(chunk)
                points.append(
                    PointStruct(
                        id=str(uuid.uuid4()),
                        vector=vector,
                        payload={
                            "site_id": site["id"],
                            "site": site_name,
                            "language": language,
                            "text": chunk,
                            "chunk_index": index,
                        },
                    )
                )

    if not points:
        return {"collection": COLLECTION_NAME, "status": "empty", "chunks": 0}

    client = get_qdrant_client()
    ensure_collection(client, vector_size=len(points[0].vector))
    client.upsert(collection_name=COLLECTION_NAME, points=points)

    return {"collection": COLLECTION_NAME, "status": "ok", "chunks": len(points)}


if __name__ == "__main__":
    print(ingest_content())
