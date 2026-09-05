"""CAMARA Quality on Demand wrapper."""


def request_qos(session_id: str) -> dict:
    """Request better network quality for a visitor session.

    CAMARA capability: Quality on Demand.
    """
    return {
        "session_id": session_id,
        "qos_requested": False,
        "status": "stub",
    }

