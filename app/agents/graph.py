"""LangGraph-based orchestration for the RawiAI agent.

Per the hackathon's AI Resource & Tooling Guide: "Treat each CAMARA API as
a tool the agent decides when to call, not a button the user presses. That
is what makes a solution 'agentic'."

Identity and presence verification stay deterministic preconditions - you
cannot tell a site's story without first confirming which site it is and
that the visitor is really there, so there is no real decision to make
there. The genuinely agentic step is what happens with the live Congestion
Insights signal: whether to suggest an alternate route and whether to
request Quality on Demand are decided by an LLM call (decide_network_action
below) reasoning over the actual signal value and the visitor's question,
not a hardcoded threshold. Its stated reasoning is carried into the
timeline so it's visible in the CAMARA Proof tab, per the guide's tip to
"show the agent's reasoning trace on screen during the demo."

A rule-based fallback (_fallback_decision) only kicks in if Gemini is
unavailable or its output can't be parsed - the guide's own advice to
"have a clear fallback when a model is rate-limited."
"""

import json
import operator
import re
from datetime import datetime, timezone
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph

from app.agents.location_agent import run_location_agent
from app.agents.qa_agent import answer_question
from app.agents.sites import DEFAULT_SITE_ID
from app.analytics import record_visit
from app.audio.tts import text_to_speech
from app.camara.congestion import get_congestion
from app.camara.number import verify_number
from app.camara.qos import request_qos
from app.camara.sim_swap import check_sim_swap
from app.config import GEMINI_API_KEY, GEMINI_MODEL, NOKIA_TEST_PHONE_NUMBER, RAWIAI_USE_GEMINI


class AgentState(TypedDict, total=False):
    question: str
    language: str
    site_id: str
    identity_result: dict
    sim_swap_result: dict
    location_result: dict
    congestion: dict
    should_reroute: bool
    should_request_qos: bool
    decision_reasoning: str
    route: dict
    qos_result: dict
    qa_result: dict
    timeline: Annotated[list[dict], operator.add]
    camara_calls: Annotated[list[str], operator.add]


def _node_verify_identity(state: AgentState) -> dict:
    phone_number = NOKIA_TEST_PHONE_NUMBER or "+99999991000"
    identity_result = verify_number(phone_number)
    sim_swap_result = check_sim_swap(phone_number)
    return {
        "identity_result": identity_result,
        "sim_swap_result": sim_swap_result,
        "camara_calls": ["Number Verification", "SIM Swap"],
        "timeline": [
            {
                "step": "Identity",
                "detail": "Verify the visitor phone/session context.",
                "source": identity_result["source"],
            },
            {
                "step": "SIM Swap",
                "detail": (
                    "No recent SIM swap detected."
                    if sim_swap_result.get("swapped") is False
                    else "Recent SIM swap detected - treat session with extra caution."
                    if sim_swap_result.get("swapped")
                    else "SIM swap status unknown."
                ),
                "source": sim_swap_result["source"],
            },
        ],
    }


def _node_verify_presence(state: AgentState) -> dict:
    location_result = run_location_agent(site_id=state["site_id"], language=state["language"])
    return {
        "location_result": location_result,
        "camara_calls": list(location_result["camara_calls"]),
        "timeline": [
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
        ],
    }


def _node_sense_network(state: AgentState) -> dict:
    site_id = state["location_result"]["site"]["id"]
    congestion = get_congestion(site_id)
    return {"congestion": congestion, "camara_calls": ["Congestion Insights"]}


def _fallback_decision(congestion: dict) -> dict:
    """Rule-based stand-in used only when Gemini is unavailable/unparsable."""
    busy = congestion.get("congestion_level") in {"Medium", "High"}
    level = congestion.get("congestion_level", "Unknown")
    return {
        "should_reroute": busy,
        "should_request_qos": busy,
        "reasoning": (
            f"Fallback rule (Gemini unavailable): congestion is {level}, so "
            f"{'reroute and prioritize bandwidth' if busy else 'no action is needed'}."
        ),
    }


def _ask_gemini_for_decision(prompt: str) -> dict:
    from google import genai

    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(model=GEMINI_MODEL, contents=prompt)
    text = (getattr(response, "text", "") or "").strip()
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in the agent's response")
    data = json.loads(match.group(0))
    return {
        "should_reroute": bool(data["should_reroute"]),
        "should_request_qos": bool(data["should_request_qos"]),
        "reasoning": str(data.get("reasoning", "")).strip() or "No reasoning given.",
    }


def _decide_network_action(state: AgentState) -> dict:
    """The agentic decision point: an LLM reasons over the live Congestion
    Insights reading (and the visitor's question) to decide - not a fixed
    threshold - whether the reroute and QoD tools are worth calling."""
    congestion = state["congestion"]
    prompt = f"""
You are the network-decision agent inside a heritage-site tour guide app.
You have one real-time signal from Nokia CAMARA Congestion Insights:

Congestion level near the site: {congestion.get("congestion_level", "Unknown")}
Visitor's question: {state["question"]}

Decide two independent actions:
1. should_reroute: suggest a quieter alternate path. Only worth it if
   congestion is meaningfully degrading the visit.
2. should_request_qos: request Quality-on-Demand network prioritization.
   Only worth it if congestion could make the spoken narration choppy.

Respond with ONLY a JSON object, no markdown, no other text:
{{"should_reroute": true or false, "should_request_qos": true or false, "reasoning": "one short sentence"}}
""".strip()

    decision = _fallback_decision(congestion)
    source = "local-fallback-decision"
    if RAWIAI_USE_GEMINI and GEMINI_API_KEY:
        try:
            decision = _ask_gemini_for_decision(prompt)
            source = f"gemini:{GEMINI_MODEL}"
        except Exception as exc:
            decision = _fallback_decision(congestion)
            source = f"local-fallback-decision-error:{exc.__class__.__name__}"

    reasoning = decision["reasoning"]
    return {
        "should_reroute": decision["should_reroute"],
        "should_request_qos": decision["should_request_qos"],
        "decision_reasoning": reasoning,
        # Sensible "no action" defaults; suggest_route/request_qos overwrite
        # these in a later step if the agent decided to actually invoke them.
        "route": {
            "route": "Continue on the main heritage route.",
            "reason": f"Agent decision: {reasoning}",
            "congestion": congestion,
        },
        "qos_result": {
            "session_id": "rawiai-story-session",
            "qos_requested": False,
            "status": "NOT_REQUESTED",
            "source": "agent-decision-skipped",
        },
        "timeline": [{"step": "Agent Decision", "detail": reasoning, "source": source}],
    }


def _route_after_decision(state: AgentState) -> list[str]:
    branches = []
    if state["should_reroute"]:
        branches.append("suggest_route")
    if state["should_request_qos"]:
        branches.append("request_qos")
    if not branches:
        branches.append("skip_network_action")
    return branches


def _node_skip_network_action(state: AgentState) -> dict:
    return {}


def _node_suggest_route(state: AgentState) -> dict:
    return {
        "route": {
            "route": "Use the quieter heritage path through the east entrance.",
            "reason": f"Agent decision: {state['decision_reasoning']}",
            "congestion": state["congestion"],
        }
    }


def _node_request_qos(state: AgentState) -> dict:
    qos_result = request_qos("rawiai-story-session")
    return {
        "qos_result": qos_result,
        "camara_calls": ["Quality on Demand"],
        "timeline": [
            {
                "step": "QoD",
                "detail": f"Agent-requested: {state['decision_reasoning']}",
                "source": qos_result["source"],
            }
        ],
    }


def _node_generate_story(state: AgentState) -> dict:
    qa_result = answer_question(state["question"], language=state["language"], site_id=state["site_id"])
    return {
        "qa_result": qa_result,
        "timeline": [
            {
                "step": "Story",
                "detail": "Generate or retrieve the heritage narration.",
                "source": qa_result["source"],
            }
        ],
    }


def _build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("verify_identity", _node_verify_identity)
    graph.add_node("verify_presence", _node_verify_presence)
    graph.add_node("sense_network", _node_sense_network)
    graph.add_node("decide_network_action", _decide_network_action)
    graph.add_node("suggest_route", _node_suggest_route)
    graph.add_node("request_qos", _node_request_qos)
    graph.add_node("skip_network_action", _node_skip_network_action)
    graph.add_node("generate_story", _node_generate_story)

    graph.add_edge(START, "verify_identity")
    graph.add_edge("verify_identity", "verify_presence")
    graph.add_edge("verify_presence", "sense_network")
    graph.add_edge("sense_network", "decide_network_action")
    graph.add_conditional_edges("decide_network_action", _route_after_decision)
    graph.add_edge("suggest_route", "generate_story")
    graph.add_edge("request_qos", "generate_story")
    graph.add_edge("skip_network_action", "generate_story")
    graph.add_edge("generate_story", END)

    return graph.compile()


_COMPILED_GRAPH = _build_graph()


def run_demo_flow(
    question: str = "Tell me the story of this place.",
    language: str = "en",
    site_id: str = DEFAULT_SITE_ID,
) -> dict:
    """Run the RawiAI agent graph and reshape its final state into the
    flat dict shape the UI state layer expects."""
    started_at = datetime.now(timezone.utc).isoformat()

    final_state = _COMPILED_GRAPH.invoke(
        {
            "question": question,
            "language": language,
            "site_id": site_id,
            "timeline": [],
            "camara_calls": [],
        }
    )

    identity_result = final_state["identity_result"]
    location_result = final_state["location_result"]
    qa_result = final_state["qa_result"]
    route = final_state["route"]
    qos_result = final_state["qos_result"]

    audio_result = text_to_speech(qa_result["answer"], language=language)

    record_visit(
        site_id=site_id,
        site_name=location_result["near_monument"],
        question=question,
        language=language,
        congestion_level=final_state["congestion"]["congestion_level"],
    )

    return {
        "identity": identity_result,
        "sim_swap": final_state["sim_swap_result"],
        "language": language,
        "question": question,
        "location": location_result,
        "qa": qa_result,
        "route": {
            "area_id": site_id,
            "congestion": final_state["congestion"],
            "route": route["route"],
            "reason": route["reason"],
            "camara_calls": ["Congestion Insights"],
        },
        "audio": audio_result,
        "qos": qos_result,
        "camara_calls": final_state["camara_calls"],
        "timeline": final_state["timeline"],
        "started_at": started_at,
        "summary": (
            f"RawiAI found {location_result['near_monument']}, prepared a "
            f"{language} story, and had its agent decide "
            f"{'to reroute' if final_state['should_reroute'] else 'no reroute was needed'} "
            f"and {'request' if final_state['should_request_qos'] else 'skip'} QoD."
        ),
    }
