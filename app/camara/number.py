"""CAMARA Number Verification wrapper."""

from app.config import NOKIA_API_KEY, RAWIAI_USE_LIVE_APIS
from app.camara.client import get_nokia_client
from app.camara.utils import api_error, to_dict


def verify_number(phone_number: str) -> dict:
    """Verify the visitor phone number without an SMS code.

    CAMARA capability: Number Verification.
    """
    if not RAWIAI_USE_LIVE_APIS or not NOKIA_API_KEY:
        return {
            "phone_number": phone_number,
            "verified": True,
            "source": "demo-camara-number-verification",
            "message": (
                "Demo mode is using simulated CAMARA Number Verification. "
                "Set RAWIAI_USE_LIVE_APIS=true to call Nokia."
            ),
        }

    try:
        client = get_nokia_client()
        response = client.number_verification.verify_v2(
            request={"phone_number": phone_number},
            correlator="rawiai-number-check",
        )
    except Exception as exc:
        return {
            "phone_number": phone_number,
            "verified": False,
            **api_error("nokia-camara-number-verification", exc),
        }

    data = to_dict(response)

    return {
        "phone_number": phone_number,
        "verified": bool(data.get("devicePhoneNumberVerified", False)),
        "source": "nokia-camara-number-verification",
        "raw": data,
    }
