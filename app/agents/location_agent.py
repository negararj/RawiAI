"""Agent that decides which heritage site the visitor is near."""

from app.camara.location import get_device_location, verify_location


AL_HISN_FORT = {
    "name": "Al Hisn Fort",
    "lat": 25.3573,
    "lon": 55.3820,
    "radius_meters": 150,
}


def run_location_agent() -> dict:
    """Use CAMARA location signals to choose the active landmark."""
    location = get_device_location()
    verification = verify_location(
        AL_HISN_FORT["lat"],
        AL_HISN_FORT["lon"],
        AL_HISN_FORT["radius_meters"],
    )

    return {
        "near_monument": AL_HISN_FORT["name"],
        "location": location,
        "verification": verification,
    }
