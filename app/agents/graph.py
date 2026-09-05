"""Simple orchestration skeleton for the three-agent demo flow."""

from app.agents.location_agent import run_location_agent
from app.agents.qa_agent import answer_question
from app.agents.route_agent import suggest_route
from app.audio.tts import text_to_speech
from app.camara.number import verify_number
from app.camara.qos import request_qos
from app.config import NOKIA_TEST_PHONE_NUMBER


def run_demo_flow(
    question: str = "Tell me the story of this place.",
    language: str = "en",
) -> dict:
    """Run the first end-to-end version of the RawiAI experience."""
    identity_result = verify_number(NOKIA_TEST_PHONE_NUMBER or "+99999991000")
    location_result = run_location_agent()
    qa_result = answer_question(question, language=language)
    route_result = suggest_route(location_result["site"]["id"])
    audio_result = text_to_speech(qa_result["answer"])
    qos_result = request_qos("rawiai-story-session")

    return {
        "identity": identity_result,
        "language": language,
        "location": location_result,
        "qa": qa_result,
        "route": route_result,
        "audio": audio_result,
        "qos": qos_result,
        "camara_calls": [
            "Number Verification",
            *location_result["camara_calls"],
            *route_result["camara_calls"],
            "Quality on Demand",
        ],
    }
