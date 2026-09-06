"""Geofencing webhook receiver.

Registered as a real POST route on the backend in app/main.py.
"""

from app.camara.geofencing import handle_geofence_event
from app.config import NOKIA_TEST_PHONE_NUMBER, RAWIAI_APP_URL
from app.sms.client import send_arrival_sms


def receive_geofence_event(cloudevent: dict) -> dict:
    """Process a CAMARA geofencing CloudEvent and, on a real entry, text the
    visitor a link straight to their story - the "Amina gets an SMS the
    moment she enters" moment from the pitch deck, made real rather than
    just narrated."""
    normalized = handle_geofence_event(cloudevent)

    sms_result = None
    if normalized["visitor_entered"]:
        phone_number = normalized["phone_number"] or NOKIA_TEST_PHONE_NUMBER
        link = RAWIAI_APP_URL or "https://rawiai-silver-apple.reflex.run"
        message = f"Welcome to {normalized['site_name']}! Tap to hear its story: {link}"
        sms_result = send_arrival_sms(phone_number, message) if phone_number else None

    return {
        "received": True,
        "normalized": normalized,
        "sms": sms_result,
    }
