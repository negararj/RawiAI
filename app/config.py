"""Shared configuration loaded from environment variables."""

import os

from dotenv import load_dotenv


load_dotenv()


RAWIAI_USE_LIVE_APIS = os.getenv("RAWIAI_USE_LIVE_APIS", "false").lower() == "true"
RAWIAI_USE_GEMINI = os.getenv("RAWIAI_USE_GEMINI", "false").lower() == "true"

NOKIA_API_KEY = os.getenv("NOKIA_API_KEY", "")
NOKIA_RAPIDAPI_HOST = os.getenv(
    "NOKIA_RAPIDAPI_HOST",
    "network-as-code.nokia.rapidapi.com",
)
NOKIA_TEST_PHONE_NUMBER = os.getenv("NOKIA_TEST_PHONE_NUMBER", "")
NOKIA_GEOFENCE_SINK_URL = os.getenv("NOKIA_GEOFENCE_SINK_URL", "")
RAWIAI_APPLICATION_SERVER_IPV4 = os.getenv("RAWIAI_APPLICATION_SERVER_IPV4", "8.8.8.8")
NOKIA_QOS_PROFILE = os.getenv("NOKIA_QOS_PROFILE", "DOWNLINK_M_UPLINK_L")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
GEMINI_EMBEDDING_MODEL = os.getenv("GEMINI_EMBEDDING_MODEL", "gemini-embedding-001")

RAWIAI_USE_QDRANT = os.getenv("RAWIAI_USE_QDRANT", "false").lower() == "true"
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")

# Real SMS-triggered entry: when a CAMARA geofencing "area-entered" event
# arrives at /geofence, send the visitor a link via Twilio. Off by default -
# needs a real Twilio account (or another provider swapped into
# app/sms/client.py) to actually send anything.
RAWIAI_USE_SMS = os.getenv("RAWIAI_USE_SMS", "false").lower() == "true"
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER", "")
RAWIAI_APP_URL = os.getenv("RAWIAI_APP_URL", "")
