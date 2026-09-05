"""Qdrant connection helpers."""

from qdrant_client import QdrantClient

from app.config import QDRANT_URL


COLLECTION_NAME = "heritage_content"


def get_qdrant_client() -> QdrantClient:
    """Create a Qdrant client."""
    return QdrantClient(url=QDRANT_URL)

