"""Simple orchestration skeleton for the three-agent demo flow."""

from app.agents.location_agent import run_location_agent
from app.agents.qa_agent import answer_question
from app.agents.route_agent import suggest_route
from app.audio.tts import text_to_speech


def run_demo_flow(question: str = "Tell me the story of this place.") -> dict:
    """Run the first end-to-end version of the RawiAI experience."""
    location_result = run_location_agent()
    qa_result = answer_question(question)
    route_result = suggest_route("al-hisn-fort")
    audio_result = text_to_speech(qa_result["answer"])

    return {
        "location": location_result,
        "qa": qa_result,
        "route": route_result,
        "audio": audio_result,
    }

