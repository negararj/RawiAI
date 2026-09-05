"""Reflex state for the RawiAI demo app."""

import reflex as rx

from app.agents.graph import run_demo_flow


class RawiState(rx.State):
    """State shared by the mobile UI."""

    language: str = "en"
    question: str = "Tell me the story of this place."
    status: str = "Ready"
    answer: str = ""
    route: str = ""
    camara_status: str = ""
    qos_status: str = ""
    current_site: str = ""
    geofence_status: str = ""
    route_reason: str = ""
    story_source: str = ""
    camara_calls: str = ""
    flow_summary: str = ""
    timeline: str = ""

    def set_language(self, language: str):
        self.language = language

    def set_question(self, question: str):
        self.question = question

    def start_demo(self):
        self.status = "Checking location with CAMARA APIs..."
        result = run_demo_flow(self.question, language=self.language)
        self.current_site = result["location"]["near_monument"]
        self.answer = result["qa"]["answer"]
        self.route = result["route"]["route"]
        self.story_source = result["qa"]["source"]
        self.camara_calls = " -> ".join(result["camara_calls"])
        self.flow_summary = result["summary"]
        self.timeline = " | ".join(item["step"] for item in result["timeline"])
        self.camara_status = (
            f"Identity: {result['identity']['source']} | "
            f"Location: {result['location']['verification']['source']} | "
            f"Congestion: {result['route']['congestion']['source']}"
        )
        self.geofence_status = f"Geofence: {result['location']['geofence']['status']}"
        self.route_reason = result["route"]["reason"]
        self.qos_status = f"QoD: {result['qos']['status']}"
        self.status = "Story ready"
