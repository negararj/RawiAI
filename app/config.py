"""Shared configuration loaded from environment variables."""

import os

from dotenv import load_dotenv


load_dotenv()


NOKIA_API_KEY = os.getenv("NOKIA_API_KEY", "")
NOKIA_RAPIDAPI_HOST = os.getenv(
    "NOKIA_RAPIDAPI_HOST",
    "network-as-code.nokia.rapidapi.com",
)
NOKIA_TEST_PHONE_NUMBER = os.getenv("NOKIA_TEST_PHONE_NUMBER", "")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
