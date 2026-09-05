"""CAMARA Geofencing wrappers."""


def subscribe_geofence(site_name: str, lat: float, lon: float, radius_meters: int) -> dict:
    """Subscribe to enter/exit events for a heritage site.

    CAMARA capability: Geofencing.
    """
    return {
        "subscription_id": "demo-geofence-subscription",
        "site_name": site_name,
        "lat": lat,
        "lon": lon,
        "radius_meters": radius_meters,
        "status": "stub",
    }


def handle_geofence_event(event: dict) -> dict:
    """Normalize a CAMARA CloudEvent from the geofencing webhook."""
    return {
        "event_type": event.get("type", "unknown"),
        "site_name": event.get("site_name", "unknown"),
        "visitor_entered": event.get("event") == "ENTER",
    }

