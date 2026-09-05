"""ElevenLabs text-to-speech skeleton."""


def text_to_speech(text: str, voice: str = "default") -> dict:
    """Convert generated story text into audio."""
    return {
        "text": text,
        "voice": voice,
        "audio_url": None,
        "status": "stub",
    }

