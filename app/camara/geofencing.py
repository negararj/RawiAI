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


def subscribe_geofence(site_name: str, lat: float, lon: float, radius_meters: int, site_id: str = "") -> dict:
    """Subscribe to enter/exit events for a heritage site.

    CAMARA capability: Geofencing.

    The correlator is site-specific (rawiai-geofence-<site_id>) so the
    webhook receiving the resulting CloudEvent can tell which landmark it's
    for, since the event payload itself doesn't otherwise carry that.
    """
    correlator = f"rawiai-geofence-{site_id}" if site_id else "rawiai-geofence-subscription"

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
            correlator=correlator,
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
    """Normalize a CAMARA geofencing CloudEvent from the webhook.

    Defensive about the exact shape: real CAMARA geofencing CloudEvents
    nest most fields under "data", but this also accepts the simulator's
    flatter shape (a plain {"type", "event", "site_name", ...} dict) used
    by the demo-mode "Simulate Entry" button, since no real Nokia event has
    been captured yet to confirm the exact production payload.
    """
    data = event.get("data") if isinstance(event.get("data"), dict) else event

    event_type = event.get("type", "unknown")
    visitor_entered = event.get("event") == "ENTER" or "area-entered" in str(event_type)

    device = data.get("device") if isinstance(data.get("device"), dict) else {}
    phone_number = device.get("phoneNumber") or data.get("phone_number") or ""

    correlator = data.get("correlator") or event.get("correlator") or ""
    site_id = correlator.removeprefix("rawiai-geofence-") if correlator.startswith("rawiai-geofence-") else ""

    site_name = event.get("site_name", "")
    if not site_name and site_id:
        from app.agents.sites import DEMO_SITES

        site = DEMO_SITES.get(site_id)
        site_name = site["name_en"] if site else "unknown"

    return {
        "event_type": event_type,
        "site_id": site_id,
        "site_name": site_name or "unknown",
        "phone_number": phone_number,
        "visitor_entered": visitor_entered,
    }
