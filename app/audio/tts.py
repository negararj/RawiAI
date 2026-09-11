"""Text-to-speech: a real FreeTTS voice when configured, the browser's
free built-in voice otherwise. FreeTTS is a real paid-company-run service
(Outline Technologies LLC) with a free tier - 5,000 characters per
generation, 15,000 per month - so any error (quota exceeded, network)
silently falls back to the browser voice rather than breaking the story.
"""

import httpx

from app.config import FREETTS_API_KEY, FREETTS_VOICE_AR, FREETTS_VOICE_EN, RAWIAI_USE_FREETTS

FREETTS_API_BASE = "https://freetts.org/api"


def _browser_voice(text: str, status: str = "ready") -> dict:
    return {
        "text": text,
        "audio_url": "",
        "provider": "browser-speech-synthesis",
        "status": status,
    }


def _try_freetts(text: str, language: str) -> dict | None:
    if not RAWIAI_USE_FREETTS or not FREETTS_API_KEY:
        return None

    voice = FREETTS_VOICE_AR if language == "ar" else FREETTS_VOICE_EN
    try:
        response = httpx.post(
            f"{FREETTS_API_BASE}/v1/tts",
            headers={"x-api-key": FREETTS_API_KEY},
            json={"text": text, "voice": voice, "rate": "+0%", "pitch": "+0Hz"},
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
    except Exception:
        return None

    audio_url = data.get("audio_url")
    if not audio_url:
        return None

    return {
        "text": text,
        "audio_url": audio_url,
        "provider": "freetts",
        "status": "ready",
    }


def text_to_speech(text: str, language: str = "en") -> dict:
    """Tell the UI how to speak the story: a real FreeTTS-hosted audio
    file if configured and it succeeds, otherwise the browser's Web
    Speech API, which needs no paid provider or API key at all.
    """
    if not text.strip():
        return _browser_voice(text)

    result = _try_freetts(text, language)
    if result:
        return result

    return _browser_voice(text, status="cloud-tts-unavailable")
