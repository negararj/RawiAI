"""Real SMS dispatch for the "network detects your entry" moment.

Uses Twilio's REST API directly over HTTP (no twilio SDK dependency) since
the whole call is one POST with basic auth and a form body. Requires a real
Twilio account - see .env.example for the variables needed. Follows the
same demo-safe pattern as app/camara/*: returns a clearly-labeled demo
response instead of sending anything when RAWIAI_USE_SMS is off or
credentials are missing, and never raises on failure.
"""

import httpx

from app.config import (
    RAWIAI_USE_SMS,
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_FROM_NUMBER,
)

TWILIO_API_BASE = "https://api.twilio.com/2010-04-01"


def send_arrival_sms(to_number: str, message: str) -> dict:
    """Send a real SMS via Twilio, or return a demo-mode stand-in."""
    if not RAWIAI_USE_SMS or not (TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN and TWILIO_FROM_NUMBER):
        return {
            "sent": False,
            "to": to_number,
            "message": message,
            "source": "demo-sms",
            "detail": (
                "Demo mode: no SMS sent. Set RAWIAI_USE_SMS=true and add Twilio "
                "credentials to .env to send a real message."
            ),
        }

    url = f"{TWILIO_API_BASE}/Accounts/{TWILIO_ACCOUNT_SID}/Messages.json"

    try:
        response = httpx.post(
            url,
            auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN),
            data={"To": to_number, "From": TWILIO_FROM_NUMBER, "Body": message},
            timeout=8,
        )
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        return {
            "sent": False,
            "to": to_number,
            "message": message,
            "source": "twilio-sms",
            "error_type": exc.__class__.__name__,
            "detail": str(exc),
        }

    return {
        "sent": True,
        "to": to_number,
        "message": message,
        "source": "twilio-sms",
        "sid": data.get("sid"),
        "status": data.get("status"),
    }
