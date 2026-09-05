"""Qdrant connection helpers."""

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from app.config import QDRANT_URL


COLLECTION_NAME = "heritage_content"


def get_qdrant_client() -> QdrantClient:
    """Create a Qdrant client."""
    return QdrantClient(url=QDRANT_URL)


def ensure_collection(client: QdrantClient, vector_size: int) -> None:
    """Create the heritage content collection if it does not exist yet."""
    if client.collection_exists(COLLECTION_NAME):
        return

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
    )
