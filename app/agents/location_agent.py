"""Agent that decides which heritage site the visitor is near."""

from app.agents.sites import DEFAULT_SITE_ID, get_site
from app.camara.geofencing import subscribe_geofence
from app.camara.location import get_device_location, verify_location


def run_location_agent(site_id: str = DEFAULT_SITE_ID, language: str = "en") -> dict:
    """Use CAMARA location signals to choose the active landmark."""
    site = get_site(site_id)
    site_name = site["name_ar"] if language == "ar" else site["name_en"]

    location = get_device_location()
    verification = verify_location(
        site["lat"],
        site["lon"],
        site["radius_meters"],
    )
    geofence = subscribe_geofence(
        site_name,
        site["lat"],
        site["lon"],
        site["radius_meters"],
    )

    return {
        "site": site,
        "near_monument": site_name,
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
