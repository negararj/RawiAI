"""Main Reflex pages."""

import reflex as rx

from app.ui.components import (
    FONT_BODY,
    INK_SOFT,
    SAND,
    arrival_alert_button,
    arrival_watch_script,
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

# A fort-wall battlement silhouette, tiled along the bottom of the viewport -
# echoes the fortress/skyline artwork on the pitch deck's title slide.
_BATTLEMENT_SVG = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='20' height='24'>"
    "<path d='M0 24 L0 8 L4 8 L4 3 L8 3 L8 8 L12 8 L12 3 L16 3 L16 8 L20 8 L20 24 Z' "
    "fill='%23AE5A2E' opacity='0.5'/></svg>"
)

# A single dome + minaret silhouette, centered above the battlements - the
# same skyline motif as the deck's title-slide illustration. The dome arc
# radius equals half its base width, so it forms an exact semicircle
# springing from y=30 up to a peak at y=7 - kept clear of the canvas edge.
_DOME_SVG = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='70' height='50'>"
    "<path d='M12 48 L12 30 A23 23 0 0 1 58 30 L58 48 Z' fill='%23AE5A2E' opacity='0.4'/>"
    "<rect x='32' y='2' width='6' height='8' fill='%23AE5A2E' opacity='0.4'/>"
    "<circle cx='35' cy='2' r='2' fill='%23AE5A2E' opacity='0.4'/></svg>"
)


def skyline_bar():
    """A fixed heritage skyline (fort battlements + a dome) along the
    bottom of the viewport, drawn from the pitch deck's title-slide art."""
    return rx.el.div(
        style={
            "position": "fixed",
            "bottom": "0",
            "left": "0",
            "width": "100%",
            "height": "40px",
            "background_image": f"url(\"{_DOME_SVG}\"), url(\"{_BATTLEMENT_SVG}\")",
            "background_repeat": "no-repeat, repeat-x",
            "background_position": "center bottom, bottom",
            "background_size": "56px 40px, 40px 24px",
            "pointer_events": "none",
            "z_index": "0",
        }
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
    "position": "relative",
    "z_index": "1",
    "padding_bottom": "24px",
}


def index():
    return rx.el.div(
        rx.el.div(
            brand_header(),
            hero(),
            trust_rail(),
            arrival_alert_button(),
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
        arrival_watch_script(),
        skyline_bar(),
        style=PAGE_STYLE,
    )
