"""Free browser text-to-speech helper.

Neither cloud voice tried so far has actually worked without paying:
OpenAI TTS needs API credits, ElevenLabs blocks free-tier accounts from
using any voice via the API. Removed for now rather than keeping dead
code around - see git history (the "Add real cloud narration voice"
commit) if either gets funded later and this should come back.
"""


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
