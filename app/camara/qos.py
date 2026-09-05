"""CAMARA Quality on Demand wrapper."""

from app.config import (
    NOKIA_API_KEY,
    NOKIA_QOS_PROFILE,
    NOKIA_TEST_PHONE_NUMBER,
    RAWIAI_USE_LIVE_APIS,
    RAWIAI_APPLICATION_SERVER_IPV4,
)
from app.camara.client import get_nokia_client
from app.camara.utils import api_error, to_dict


def request_qos(session_id: str) -> dict:
    """Request better network quality for a visitor session.

    CAMARA capability: Quality on Demand.
    """
    if not RAWIAI_USE_LIVE_APIS or not NOKIA_API_KEY or not NOKIA_TEST_PHONE_NUMBER:
        return {
            "session_id": session_id,
            "qos_requested": True,
            "status": "DEMO_REQUESTED",
            "source": "demo-camara-quality-on-demand",
            "message": (
                "Demo mode is using simulated CAMARA Quality on Demand. "
                "Set RAWIAI_USE_LIVE_APIS=true to call Nokia."
            ),
        }

    try:
        client = get_nokia_client()
        response = client.qod.create_session_v1(
            device={"phone_number": NOKIA_TEST_PHONE_NUMBER},
            application_server={"ipv4address": RAWIAI_APPLICATION_SERVER_IPV4},
            qos_profile=NOKIA_QOS_PROFILE,
            duration=300,
        )
    except Exception as exc:
        return {
            "session_id": session_id,
            "qos_requested": False,
            **api_error("nokia-camara-quality-on-demand", exc),
        }

    data = to_dict(response)
    qos_status = data.get("qosStatus", "UNKNOWN")

    return {
        "session_id": data.get("sessionId", session_id),
        "qos_requested": qos_status in {"REQUESTED", "AVAILABLE"},
        "status": qos_status,
        "qos_profile": data.get("qosProfile"),
        "expires_at": data.get("expiresAt"),
        "source": "nokia-camara-quality-on-demand",
        "raw": data,
    }
