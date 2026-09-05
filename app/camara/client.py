"""Nokia Network as Code client setup."""

from app.config import NOKIA_API_KEY, NOKIA_RAPIDAPI_HOST


def get_nokia_client():
    """Create the Nokia Network as Code SDK client.

    Keep this function as the single place where credentials are used.
    """
    try:
        from network_as_code import NetworkAsCodeApi
    except ImportError as exc:
        raise RuntimeError(
            "Install the Nokia SDK first: pip install network_as_code"
        ) from exc

    if not NOKIA_API_KEY:
        raise RuntimeError("NOKIA_API_KEY is missing. Add it to your .env file.")

    return NetworkAsCodeApi(
        rapidapi_host=NOKIA_RAPIDAPI_HOST,
        api_key=NOKIA_API_KEY,
    )

