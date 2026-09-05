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

    def set_language(self, language: str):
        self.language = language

    def set_question(self, question: str):
        self.question = question

    def start_demo(self):
        self.status = "Checking location with CAMARA APIs..."
        result = run_demo_flow(self.question)
        self.answer = result["qa"]["answer"]
        self.route = result["route"]["route"]
        self.status = "Story ready"

