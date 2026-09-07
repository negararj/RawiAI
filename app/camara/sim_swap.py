"""CAMARA SIM Swap wrapper."""

from app.camara.client import get_nokia_client
from app.camara.utils import api_error, to_dict
from app.config import NOKIA_API_KEY, RAWIAI_USE_LIVE_APIS


def check_sim_swap(phone_number: str, max_age_hours: int = 240) -> dict:
    """Check whether the visitor's SIM has swapped recently - a fraud/
    identity-trust signal alongside Number Verification.

    CAMARA capability: SIM Swap.
    """
    if not RAWIAI_USE_LIVE_APIS or not NOKIA_API_KEY:
        return {
            "phone_number": phone_number,
            "swapped": False,
            "source": "demo-camara-sim-swap",
            "message": (
                "Demo mode is using simulated CAMARA SIM Swap. "
                "Set RAWIAI_USE_LIVE_APIS=true to call Nokia."
            ),
        }

    try:
        client = get_nokia_client()
        response = client.sim_swap.check(
            phone_number=phone_number,
            max_age=max_age_hours,
            correlator="rawiai-sim-swap-check",
        )
    except Exception as exc:
        return {
            "phone_number": phone_number,
            "swapped": None,
            **api_error("nokia-camara-sim-swap", exc),
        }

    data = to_dict(response)

    return {
        "phone_number": phone_number,
        "swapped": bool(data.get("swapped", False)),
        "source": "nokia-camara-sim-swap",
        "raw": data,
    }
