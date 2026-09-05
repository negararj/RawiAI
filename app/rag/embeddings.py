"""Text embeddings for the RAG pipeline, backed by the Gemini embeddings API."""

from app.config import GEMINI_API_KEY, GEMINI_EMBEDDING_MODEL


def embed_text(text: str) -> list[float]:
    """Return an embedding vector for a piece of heritage narration or a query."""
    from google import genai

    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is missing. Add it to your .env file.")

    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.embed_content(
        model=GEMINI_EMBEDDING_MODEL,
        contents=text,
    )
    return list(response.embeddings[0].values)
