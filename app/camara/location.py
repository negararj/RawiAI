"""CAMARA Location Retrieval and Location Verification wrappers."""

from app.config import NOKIA_API_KEY, NOKIA_TEST_PHONE_NUMBER, RAWIAI_USE_LIVE_APIS
from app.camara.client import get_nokia_client
from app.camara.utils import api_error, to_dict


def verify_location(lat: float, lon: float, radius_meters: int) -> dict:
    """Check whether the visitor is inside the heritage site area.

    CAMARA capability: Location Verification.
    """
    if not RAWIAI_USE_LIVE_APIS or not NOKIA_API_KEY or not NOKIA_TEST_PHONE_NUMBER:
        return {
            "verified": True,
            "verification_result": "DEMO_TRUE",
            "lat": lat,
            "lon": lon,
            "radius_meters": radius_meters,
            "source": "demo-camara-location-verification",
            "message": (
                "Demo mode is using simulated CAMARA Location Verification. "
                "Set RAWIAI_USE_LIVE_APIS=true to call Nokia."
            ),
        }

    try:
        client = get_nokia_client()
        response = client.location.verify_v1(
            device={"phone_number": NOKIA_TEST_PHONE_NUMBER},
            area={
                "area_type": "CIRCLE",
                "center": {
                    "latitude": lat,
                    "longitude": lon,
                },
                "radius": radius_meters,
            },
            max_age=60,
            correlator="rawiai-location-check",
        )
    except Exception as exc:
        error = api_error("nokia-camara-location-verification", exc)
        return {
            "verified": False,
            "verification_result": "ERROR",
            "lat": lat,
            "lon": lon,
            "radius_meters": radius_meters,
            **error,
        }

    data = to_dict(response)
    verification_result = data.get("verificationResult", "UNKNOWN")

    return {
        "verified": verification_result == "TRUE",
        "verification_result": verification_result,
        "match_rate": data.get("matchRate"),
        "last_location_time": data.get("lastLocationTime"),
        "lat": lat,
        "lon": lon,
        "radius_meters": radius_meters,
        "source": "nokia-camara-location-verification",
        "raw": data,
    }


def get_device_location() -> dict:
    """Get the visitor device location from the network.

    CAMARA capability: Location Retrieval.
    """
    if not RAWIAI_USE_LIVE_APIS or not NOKIA_API_KEY or not NOKIA_TEST_PHONE_NUMBER:
        return {
            "lat": 25.3573,
            "lon": 55.3820,
            "accuracy_meters": 100,
            "source": "demo-camara-location-retrieval",
            "message": (
                "Demo mode is using simulated CAMARA Location Retrieval. "
                "Set RAWIAI_USE_LIVE_APIS=true to call Nokia."
            ),
        }

    try:
        client = get_nokia_client()
        response = client.location.retrieve(
            device={"phone_number": NOKIA_TEST_PHONE_NUMBER},
            max_age=60,
        )
    except Exception as exc:
        return {
            "area": {},
            "source": "nokia-camara-location-retrieval",
            **api_error("nokia-camara-location-retrieval", exc),
        }

    data = to_dict(response)

    return {
        "area": data.get("area", {}),
        "last_location_time": data.get("lastLocationTime"),
        "source": "nokia-camara-location-retrieval",
        "raw": data,
    }
