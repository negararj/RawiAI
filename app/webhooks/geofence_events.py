"""Geofencing webhook receiver skeleton.

In Reflex/FastAPI integration, connect this handler to a public HTTPS route.
"""

from app.camara.geofencing import handle_geofence_event


def receive_geofence_event(cloudevent: dict) -> dict:
    """Process a CAMARA geofencing CloudEvent."""
    normalized = handle_geofence_event(cloudevent)

    return {
        "received": True,
        "normalized": normalized,
    }

