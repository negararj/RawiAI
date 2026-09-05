"""Main Reflex pages."""

import reflex as rx

from app.ui.components import (
    ask_card,
    brand_header,
    hero,
    install_card,
    network_card,
    route_card,
    site_card,
    story_card,
    timeline_card,
    trust_rail,
    SAND,
    INK_SOFT,
)
from app.ui.state import RawiState

PAGE_STYLE = {
    "min_height": "100vh",
    "width": "100%",
    "display": "flex",
    "justify_content": "center",
    "background": f"radial-gradient(circle at 15% 0%, #F3E3C9 0%, {SAND} 45%, #EAF3F1 100%)",
    "padding": "32px 16px",
    "box_sizing": "border-box",
}

SHELL_STYLE = {
    "width": "100%",
    "max_width": "440px",
    "display": "flex",
    "flex_direction": "column",
    "gap": "16px",
}


def index():
    return rx.el.div(
        rx.el.div(
            brand_header(),
            hero(),
            trust_rail(),
            ask_card(),
            rx.cond(
                RawiState.started,
                rx.el.div(
                    site_card(),
                    story_card(),
                    route_card(),
                    network_card(),
                    timeline_card(),
                    style={"display": "flex", "flex_direction": "column", "gap": "16px"},
                ),
            ),
            install_card(),
            rx.el.p(
                "DevNull · Immersive Tourism & Smart Cities · Nokia CAMARA Hackathon",
                style={
                    "font_size": "11px",
                    "color": INK_SOFT,
                    "text_align": "center",
                    "margin": "4px 0 0 0",
                },
            ),
            style=SHELL_STYLE,
            custom_attrs={"dir": RawiState.dir},
        ),
        rx.script(
            """
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("/service-worker.js");
  });
}

window.addEventListener("beforeinstallprompt", (event) => {
  event.preventDefault();
  window.rawiInstallPrompt = event;
});
"""
        ),
        style=PAGE_STYLE,
    )
