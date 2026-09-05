"""Main Reflex pages."""

import reflex as rx

from app.ui.components import language_toggle, story_controls
from app.ui.state import RawiState


def index():
    return rx.container(
        rx.vstack(
            rx.heading("RawiAI", size="8"),
            rx.text("Network-aware heritage storytelling"),
            language_toggle(),
            story_controls(),
            rx.divider(),
            rx.text(RawiState.status),
            rx.heading("Answer", size="4"),
            rx.text(RawiState.answer),
            rx.heading("Route", size="4"),
            rx.text(RawiState.route),
            spacing="4",
            align="stretch",
        ),
        max_width="520px",
        padding="24px",
    )

