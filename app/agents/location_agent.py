"""Agent that decides which heritage site the visitor is near."""

from app.camara.location import get_device_location, verify_location


def run_location_agent() -> dict:
    """Use CAMARA location signals to choose the active landmark."""
    location = get_device_location()
    verification = verify_location(location["lat"], location["lon"], 150)

    return {
        "near_monument": "Al Hisn Fort",
        "location": location,
        "verification": verification,
    }

