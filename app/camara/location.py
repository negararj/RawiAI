"""CAMARA Location Retrieval and Location Verification wrappers."""

from app.config import NOKIA_API_KEY, NOKIA_TEST_PHONE_NUMBER
from app.camara.client import get_nokia_client


def _to_dict(response) -> dict:
    """Convert a Nokia SDK response object into a normal Python dict."""
    if hasattr(response, "model_dump"):
        return response.model_dump(mode="json", by_alias=True)
    if hasattr(response, "dict"):
        return response.dict(by_alias=True)
    return dict(response)


def verify_location(lat: float, lon: float, radius_meters: int) -> dict:
    """Check whether the visitor is inside the heritage site area.

    CAMARA capability: Location Verification.
    """
    if not NOKIA_API_KEY or not NOKIA_TEST_PHONE_NUMBER:
        return {
            "verified": False,
            "verification_result": "UNKNOWN",
            "lat": lat,
            "lon": lon,
            "radius_meters": radius_meters,
            "source": "stub-missing-nokia-config",
            "message": (
                "Add NOKIA_API_KEY and NOKIA_TEST_PHONE_NUMBER to .env "
                "to call Nokia Location Verification."
            ),
        }

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

    data = _to_dict(response)
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
    return {
        "lat": 25.3573,
        "lon": 55.3820,
        "accuracy_meters": 100,
        "source": "stub",
    }
