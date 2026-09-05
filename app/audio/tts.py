"""Free browser text-to-speech helper."""


def text_to_speech(text: str) -> dict:
    """Tell the UI that the story can be spoken by the browser.

    The actual voice runs in the visitor's browser with Web Speech API, so no
    paid text-to-speech provider or API key is required.
    """
    return {
        "text": text,
        "audio_url": None,
        "provider": "browser-speech-synthesis",
        "status": "ready",
    }
