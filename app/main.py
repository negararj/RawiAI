"""Reflex app entry point."""

import reflex as rx

from app.ui.pages import index


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Cairo:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap",
        "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css",
    ],
    style={"font_family": "'Cairo', sans-serif"},
)
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
