"""Retrieve relevant heritage facts for the Q&A agent."""


def retrieve_facts(query: str, language: str = "en") -> list[dict]:
    """Return relevant facts for a visitor question."""
    return [
        {
            "site": "Al Hisn Fort",
            "language": language,
            "text": "Placeholder fact. Replace with Qdrant search result.",
            "query": query,
        }
    ]

