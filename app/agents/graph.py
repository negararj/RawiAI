"""Simple orchestration skeleton for the three-agent demo flow."""

from datetime import datetime, timezone

from app.agents.location_agent import run_location_agent
from app.agents.qa_agent import answer_question
from app.agents.route_agent import suggest_route
from app.agents.sites import DEFAULT_SITE_ID
from app.audio.tts import text_to_speech
from app.camara.number import verify_number
from app.camara.qos import request_qos
from app.config import NOKIA_TEST_PHONE_NUMBER


def run_demo_flow(
    question: str = "Tell me the story of this place.",
    language: str = "en",
    site_id: str = DEFAULT_SITE_ID,
) -> dict:
    """Run the first end-to-end version of the RawiAI experience."""
    started_at = datetime.now(timezone.utc).isoformat()

    identity_result = verify_number(NOKIA_TEST_PHONE_NUMBER or "+99999991000")
    location_result = run_location_agent(site_id=site_id, language=language)
    qa_result = answer_question(question, language=language, site_id=site_id)
    route_result = suggest_route(location_result["site"]["id"])
    audio_result = text_to_speech(qa_result["answer"])
    qos_result = request_qos("rawiai-story-session")

    camara_calls = [
        "Number Verification",
        *location_result["camara_calls"],
        *route_result["camara_calls"],
        "Quality on Demand",
    ]

    timeline = [
        {
            "step": "Identity",
            "detail": "Verify the visitor phone/session context.",
            "source": identity_result["source"],
        },
        {
            "step": "Presence",
            "detail": f"Detect and verify presence near {location_result['near_monument']}.",
            "source": location_result["verification"]["source"],
        },
        {
            "step": "Geofence",
            "detail": "Prepare the network-triggered welcome moment.",
            "source": location_result["geofence"]["source"],
        },
        {
            "step": "Story",
            "detail": "Generate or retrieve the heritage narration.",
            "source": qa_result["source"],
        },
        {
            "step": "Route",
            "detail": route_result["reason"],
            "source": route_result["congestion"]["source"],
        },
        {
            "step": "QoD",
            "detail": "Request network quality for smooth story playback.",
            "source": qos_result["source"],
        },
    ]

    return {
        "identity": identity_result,
        "language": language,
        "question": question,
        "location": location_result,
        "qa": qa_result,
        "route": route_result,
        "audio": audio_result,
        "qos": qos_result,
        "camara_calls": camara_calls,
        "timeline": timeline,
        "started_at": started_at,
        "summary": (
            f"RawiAI found {location_result['near_monument']}, prepared a "
            f"{language} story, checked congestion, and requested QoD."
        ),
    }
