"""Reusable Reflex UI components."""

import reflex as rx

from app.ui.state import RawiState


def language_toggle():
    return rx.hstack(
        rx.button("English", on_click=RawiState.set_language("en")),
        rx.button("Arabic", on_click=RawiState.set_language("ar")),
        spacing="2",
    )


def story_controls():
    return rx.vstack(
        rx.input(
            value=RawiState.question,
            on_change=RawiState.set_question,
            placeholder="Ask about this place",
        ),
        rx.button("Start Heritage Story", on_click=RawiState.start_demo),
        spacing="3",
        width="100%",
    )
