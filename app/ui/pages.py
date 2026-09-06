"""Main Reflex pages."""

import reflex as rx

from app.ui.components import (
    FONT_BODY,
    INK_SOFT,
    SAND,
    ask_card,
    brand_header,
    hero,
    install_card,
    network_card,
    route_card,
    site_card,
    story_card,
    t,
    timeline_card,
    trust_rail,
)
from app.ui.state import RawiState

# A faint eight-point-star lattice (rub el hizb motif), tiled behind the
# radial gradient - a quiet nod to Islamic geometric pattern work.
_PATTERN_SVG = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='48' height='48'>"
    "<g fill='none' stroke='%23C08A2E' stroke-width='1' opacity='0.14'>"
    "<rect x='12' y='12' width='24' height='24'/>"
    "<rect x='12' y='12' width='24' height='24' transform='rotate(45 24 24)'/>"
    "</g></svg>"
)

PAGE_STYLE = {
    "min_height": "100vh",
    "width": "100%",
    "display": "flex",
    "justify_content": "center",
    "background": (
        f"radial-gradient(circle at 15% 0%, #F3E3C9 0%, {SAND} 45%, #E7EFEB 100%), "
        f"url(\"{_PATTERN_SVG}\")"
    ),
    "background_repeat": "no-repeat, repeat",
    "background_size": "cover, 48px 48px",
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
                t("footer"),
                style={
                    "font_family": FONT_BODY,
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
