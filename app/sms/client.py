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
    TWILIO_API_KEY_SECRET,
    TWILIO_API_KEY_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_FROM_NUMBER,
)

TWILIO_API_BASE = "https://api.twilio.com/2010-04-01"


def _basic_auth() -> tuple[str, str] | None:
    """Prefer an API Key (SID starts with "SK") over the Account Auth
    Token when both are set - either works for Basic Auth, but the
    Account SID is required regardless since it's also part of the URL."""
    if TWILIO_API_KEY_SID and TWILIO_API_KEY_SECRET:
        return (TWILIO_API_KEY_SID, TWILIO_API_KEY_SECRET)
    if TWILIO_AUTH_TOKEN:
        return (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    return None


def send_arrival_sms(to_number: str, message: str) -> dict:
    """Send a real SMS via Twilio, or return a demo-mode stand-in."""
    auth = _basic_auth()
    if not RAWIAI_USE_SMS or not (TWILIO_ACCOUNT_SID and auth and TWILIO_FROM_NUMBER):
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
            auth=auth,
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
