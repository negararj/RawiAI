"""CAMARA Geofencing wrappers."""

from datetime import datetime, timedelta, timezone

from app.config import (
    NOKIA_API_KEY,
    NOKIA_GEOFENCE_SINK_URL,
    NOKIA_TEST_PHONE_NUMBER,
    RAWIAI_USE_LIVE_APIS,
)
from app.camara.client import get_nokia_client
from app.camara.utils import api_error, to_dict


def subscribe_geofence(site_name: str, lat: float, lon: float, radius_meters: int) -> dict:
    """Subscribe to enter/exit events for a heritage site.

    CAMARA capability: Geofencing.
    """
    if (
        not RAWIAI_USE_LIVE_APIS
        or not NOKIA_API_KEY
        or not NOKIA_TEST_PHONE_NUMBER
        or not NOKIA_GEOFENCE_SINK_URL
    ):
        return {
            "subscription_id": "demo-geofence-subscription",
            "site_name": site_name,
            "lat": lat,
            "lon": lon,
            "radius_meters": radius_meters,
            "status": "DEMO_ACTIVE",
            "source": "demo-camara-geofencing",
            "message": (
                "Demo mode is using a simulated CAMARA geofence subscription. "
                "Set RAWIAI_USE_LIVE_APIS=true and add a public sink URL to call Nokia."
            ),
        }

    try:
        client = get_nokia_client()
        response = client.geofencing.create_subscription(
            protocol="HTTP",
            sink=NOKIA_GEOFENCE_SINK_URL,
            types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
            config={
                "subscription_detail": {
                    "device": {"phone_number": NOKIA_TEST_PHONE_NUMBER},
                    "area": {
                        "area_type": "CIRCLE",
                        "center": {
                            "latitude": lat,
                            "longitude": lon,
                        },
                        "radius": radius_meters,
                    },
                },
                "subscription_expire_time": datetime.now(timezone.utc) + timedelta(hours=2),
                "subscription_max_events": 10,
                "initial_event": True,
            },
            correlator="rawiai-geofence-subscription",
        )
    except Exception as exc:
        return {
            "subscription_id": None,
            "site_name": site_name,
            "lat": lat,
            "lon": lon,
            "radius_meters": radius_meters,
            **api_error("nokia-camara-geofencing", exc),
        }

    data = to_dict(response)

    return {
        "subscription_id": data.get("id"),
        "site_name": site_name,
        "lat": lat,
        "lon": lon,
        "radius_meters": radius_meters,
        "status": data.get("status"),
        "source": "nokia-camara-geofencing",
        "raw": data,
    }


def handle_geofence_event(event: dict) -> dict:
    """Normalize a CAMARA CloudEvent from the geofencing webhook."""
    return {
        "event_type": event.get("type", "unknown"),
        "site_name": event.get("site_name", "unknown"),
        "visitor_entered": event.get("event") == "ENTER",
    }
