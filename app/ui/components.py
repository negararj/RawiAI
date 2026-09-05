"""Reusable Reflex UI components."""

import reflex as rx

from app.ui.state import RawiState


def section(title: str, *children):
    return rx.vstack(
        rx.heading(title, size="4", color="#2d1f17"),
        *children,
        spacing="2",
        align="stretch",
        width="100%",
        padding_y="8px",
    )


def language_toggle():
    return rx.hstack(
        rx.button(
            "English",
            on_click=RawiState.set_language("en"),
            variant="soft",
            color_scheme="orange",
        ),
        rx.button(
            "Arabic",
            on_click=RawiState.set_language("ar"),
            variant="soft",
            color_scheme="orange",
        ),
        spacing="2",
    )


def story_controls():
    return rx.vstack(
        rx.input(
            value=RawiState.question,
            on_change=RawiState.set_question,
            placeholder="Ask about this place",
            size="3",
        ),
        rx.button(
            "Start Heritage Story",
            on_click=RawiState.start_demo,
            size="3",
            color_scheme="orange",
            width="100%",
        ),
        spacing="3",
        width="100%",
    )
