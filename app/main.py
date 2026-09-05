"""Reflex app entry point."""

import reflex as rx

from app.ui.pages import index


app = rx.App()
app.add_page(
    index,
    route="/",
    title="RawiAI",
    description="Network-aware heritage storytelling powered by CAMARA APIs.",
    meta=[
        rx.el.link(rel="manifest", href="/manifest.webmanifest"),
        {"name": "theme-color", "content": "#9b4f24"},
        {"name": "apple-mobile-web-app-capable", "content": "yes"},
        {"name": "apple-mobile-web-app-title", "content": "RawiAI"},
    ],
)
