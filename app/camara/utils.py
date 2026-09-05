"""Shared helpers for CAMARA wrapper modules."""


def to_dict(response) -> dict:
    """Convert a Nokia SDK response object into a normal Python dict."""
    if response is None:
        return {}
    if hasattr(response, "model_dump"):
        return response.model_dump(mode="json", by_alias=True)
    if hasattr(response, "dict"):
        return response.dict(by_alias=True)
    return dict(response)


def to_dict_list(response_items) -> list[dict]:
    """Convert a list of Nokia SDK response objects into normal dicts."""
    return [to_dict(item) for item in response_items or []]


def api_error(source: str, exc: Exception) -> dict:
    """Return a safe, user-readable CAMARA error response."""
    return {
        "source": source,
        "status": "error",
        "error_type": exc.__class__.__name__,
        "message": str(exc),
    }
