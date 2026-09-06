"""Reflex state for the RawiAI demo app."""

import asyncio

import reflex as rx

from app.agents.graph import run_demo_flow


class RawiState(rx.State):
    """State shared by the mobile UI."""

    language: str = "en"
    question: str = "Tell me the story of this place."
    status: str = "Tap Begin and let the network find you."

    started: bool = False
    is_loading: bool = False

    # Trust-layer chips (CAMARA signals), revealed in sequence for the demo.
    step_identity: bool = False
    step_presence: bool = False
    step_network: bool = False
    step_qos: bool = False

    answer: str = ""
    route: str = ""
    route_reason: str = ""
    congestion_level: str = ""
    qos_status: str = ""
    current_site: str = ""
    geofence_status: str = ""
    story_source: str = ""
    flow_summary: str = ""
    pwa_status: str = "Installable on supported mobile browsers"

    camara_calls: list[str] = []
    timeline: list[dict[str, str]] = []

    def set_language(self, language: str):
        self.language = language

    def set_question(self, question: str):
        self.question = question

    @rx.var
    def is_ar(self) -> bool:
        return self.language == "ar"

    @rx.var
    def dir(self) -> str:
        return "rtl" if self.language == "ar" else "ltr"

    @rx.var
    def text_align(self) -> str:
        return "right" if self.language == "ar" else "left"

    async def start_demo(self):
        """Run the demo flow and reveal each CAMARA-verified step in order."""
        self.started = True
        self.is_loading = True
        self.step_identity = False
        self.step_presence = False
        self.step_network = False
        self.step_qos = False
        self.status = "Sensing your presence on the network..."
        yield
        await asyncio.sleep(0.35)

        result = run_demo_flow(self.question, language=self.language)

        self.camara_calls = result["camara_calls"]
        self.timeline = [
            {
                "step": item["step"],
                "detail": item["detail"],
                "source": item["source"],
            }
            for item in result["timeline"]
        ]
        self.flow_summary = result["summary"]

        self.step_identity = True
        self.status = f"Identity confirmed via {result['identity']['source']}"
        yield
        await asyncio.sleep(0.35)

        self.current_site = result["location"]["near_monument"]
        self.geofence_status = f"Geofence: {result['location']['geofence']['status']}"
        self.step_presence = True
        self.status = f"Presence verified near {self.current_site}"
        yield
        await asyncio.sleep(0.35)

        self.congestion_level = result["route"]["congestion"]["congestion_level"]
        self.route = result["route"]["route"]
        self.route_reason = result["route"]["reason"]
        self.step_network = True
        self.status = "Network context confirmed"
        yield
        await asyncio.sleep(0.3)

        self.answer = result["qa"]["answer"]
        self.story_source = result["qa"]["source"]
        self.status = "The storyteller is speaking..."
        yield
        await asyncio.sleep(0.3)

        self.qos_status = result["qos"]["status"]
        self.step_qos = True
        self.status = "Your heritage story is live"
        self.is_loading = False
