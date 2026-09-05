"""Main Reflex pages."""

import reflex as rx

from app.ui.components import language_toggle, section, story_controls
from app.ui.state import RawiState


def index():
    return rx.container(
        rx.vstack(
            rx.vstack(
                rx.text("Nokia CAMARA demo", color="#7a4b2a", weight="bold"),
                rx.heading("RawiAI", size="9", color="#2d1f17"),
                rx.text(
                    "Network-aware heritage storytelling for MENA sites.",
                    color="#5f4a3e",
                ),
                spacing="2",
                align="start",
                width="100%",
            ),
            rx.hstack(
                language_toggle(),
                rx.spacer(),
                rx.badge(RawiState.status, color_scheme="orange", size="2"),
                width="100%",
                align="center",
            ),
            section(
                "Ask Rawi",
                story_controls(),
            ),
            rx.text(RawiState.language, id="rawi-language", display="none"),
            section(
                "Current Site",
                rx.text(RawiState.current_site, color="#3b2a20", weight="bold"),
                rx.text(RawiState.flow_summary, color="#6b5a50"),
            ),
            section(
                "CAMARA Proof",
                rx.text(RawiState.camara_calls, color="#3b2a20"),
                rx.text(RawiState.camara_status, color="#6b5a50"),
                rx.text(RawiState.geofence_status, color="#6b5a50"),
            ),
            section(
                "Story",
                rx.text(RawiState.story_source, color="#7a4b2a"),
                rx.text(
                    RawiState.answer,
                    id="rawi-answer",
                    color="#2d1f17",
                    line_height="1.7",
                ),
                rx.button(
                    "Speak Story",
                    on_click=rx.call_script(
                        """
const text = document.getElementById("rawi-answer")?.innerText || "";
const language = document.getElementById("rawi-language")?.innerText || "en";
if (text.trim()) {
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = language === "ar" ? "ar-SA" : "en-US";
  window.speechSynthesis.speak(utterance);
}
"""
                    ),
                    variant="outline",
                    color_scheme="orange",
                ),
            ),
            section(
                "Route",
                rx.text(RawiState.route, color="#2d1f17", weight="bold"),
                rx.text(RawiState.route_reason, color="#6b5a50"),
            ),
            section(
                "Network Quality",
                rx.text(RawiState.qos_status, color="#2d1f17", weight="bold"),
                rx.text(RawiState.timeline, color="#6b5a50"),
            ),
            spacing="5",
            align="stretch",
        ),
        max_width="680px",
        min_height="100vh",
        padding="24px",
        background="#fff8ee",
    )
