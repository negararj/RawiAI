"""Agent that decides which heritage site the visitor is near."""

from app.agents.sites import AL_HISN_FORT
from app.camara.geofencing import subscribe_geofence
from app.camara.location import get_device_location, verify_location


def run_location_agent() -> dict:
    """Use CAMARA location signals to choose the active landmark."""
    site = AL_HISN_FORT

    location = get_device_location()
    verification = verify_location(
        site["lat"],
        site["lon"],
        site["radius_meters"],
    )
    geofence = subscribe_geofence(
        site["name"],
        site["lat"],
        site["lon"],
        site["radius_meters"],
    )

    return {
        "site": site,
        "near_monument": site["name"],
        "visitor_is_near_site": verification["verified"],
        "location": location,
        "verification": verification,
        "geofence": geofence,
        "camara_calls": [
            "Location Retrieval",
            "Location Verification",
            "Geofencing",
        ],
    }
