"""Text-to-speech: a real cloud voice when configured, the browser's free
built-in voice otherwise. Tries OpenAI TTS first, then ElevenLabs, then
falls back to the browser - each is a paid service with its own quota, so
any error (rate limit, wrong plan, network) silently drops to the next
option rather than breaking the story.
"""

import base64

import httpx

from app.config import (
    ELEVENLABS_API_KEY,
    ELEVENLABS_VOICE_ID,
    OPENAI_API_KEY,
    OPENAI_TTS_MODEL,
    OPENAI_TTS_VOICE,
    RAWIAI_USE_ELEVENLABS,
    RAWIAI_USE_OPENAI_TTS,
)

OPENAI_API_BASE = "https://api.openai.com/v1"
ELEVENLABS_API_BASE = "https://api.elevenlabs.io/v1"


def _browser_voice(text: str, status: str = "ready") -> dict:
    return {
        "text": text,
        "audio_data_url": "",
        "provider": "browser-speech-synthesis",
        "status": status,
    }


def _audio_data_url(audio_bytes: bytes, provider: str, text: str) -> dict:
    audio_b64 = base64.b64encode(audio_bytes).decode("ascii")
    return {
        "text": text,
        "audio_data_url": f"data:audio/mpeg;base64,{audio_b64}",
        "provider": provider,
        "status": "ready",
    }


def _try_openai(text: str) -> dict | None:
    if not RAWIAI_USE_OPENAI_TTS or not OPENAI_API_KEY:
        return None
    try:
        response = httpx.post(
            f"{OPENAI_API_BASE}/audio/speech",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
            json={"model": OPENAI_TTS_MODEL, "voice": OPENAI_TTS_VOICE, "input": text},
            timeout=30,
        )
        response.raise_for_status()
    except Exception:
        return None
    return _audio_data_url(response.content, "openai-tts", text)


def _try_elevenlabs(text: str) -> dict | None:
    if not RAWIAI_USE_ELEVENLABS or not ELEVENLABS_API_KEY:
        return None
    try:
        response = httpx.post(
            f"{ELEVENLABS_API_BASE}/text-to-speech/{ELEVENLABS_VOICE_ID}",
            headers={
                "xi-api-key": ELEVENLABS_API_KEY,
                "Content-Type": "application/json",
                "Accept": "audio/mpeg",
            },
            json={
                "text": text,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
            },
            timeout=30,
        )
        response.raise_for_status()
    except Exception:
        return None
    return _audio_data_url(response.content, "elevenlabs", text)


def text_to_speech(text: str) -> dict:
    """Tell the UI how to speak the story: real cloud audio if a provider
    is configured and succeeds, otherwise the browser's Web Speech API,
    which needs no paid provider or API key at all.
    """
    if not text.strip():
        return _browser_voice(text)

    result = _try_openai(text)
    if result:
        return result

    result = _try_elevenlabs(text)
    if result:
        return result

    return _browser_voice(text, status="cloud-tts-unavailable")
