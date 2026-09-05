"""Retrieve relevant heritage facts for the Q&A agent."""

from pathlib import Path
import re


def _clean_markdown(text: str) -> str:
    """Remove draft comments and simple markdown formatting for narration."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"^\s*#\s+", "", text, flags=re.MULTILINE)
    text = text.replace("**", "")
    return text.strip()


def retrieve_facts(query: str, language: str = "en") -> list[dict]:
    file_name = "al_hisn_fort_ar.md" if language == "ar" else "al_hisn_fort_en.md"
    content_path = Path("app/content") / file_name
    text = _clean_markdown(content_path.read_text(encoding="utf-8"))

    return [
        {
            "site": "Al Hisn Fort",
            "language": language,
            "text": text,
            "query": query,
        }
    ]
