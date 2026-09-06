"""Main Reflex pages."""

import reflex as rx

from app.ui.components import (
    FONT_BODY,
    INK_SOFT,
    arrival_alert_button,
    arrival_watch_script,
    ask_card,
    brand_header,
    browse_tab,
    camara_tab,
    favorites_tab,
    hero,
    install_card,
    network_card,
    offline_notice,
    route_card,
    selected_site_chip,
    site_card,
    story_card,
    t,
    tab_bar,
    trust_rail,
)
from app.ui.state import RawiState

# An interlocking-circles lattice - the classic Islamic geometric motif seen
# on the pitch deck's backgrounds. Circles centered at each tile corner
# (radius = half the tile size) plus one centered in the tile connect
# seamlessly with their neighbors when repeated, weaving into a continuous
# mesh rather than a grid of separate rings.
_PATTERN_SVG = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='84' height='84'>"
    "<g fill='none' stroke='%23C08A2E' stroke-width='1.5' opacity='0.22'>"
    "<circle cx='0' cy='0' r='42'/>"
    "<circle cx='84' cy='0' r='42'/>"
    "<circle cx='0' cy='84' r='42'/>"
    "<circle cx='84' cy='84' r='42'/>"
    "<circle cx='42' cy='42' r='42'/>"
    "</g></svg>"
)

# A hanging fanous (lantern) for the page corners - same shapes as the
# header's lantern_mark, shifted down to make room for a chain and a small
# crescent moon finial above, matching the deck's title-slide artwork.
_BACKGROUND_LANTERN_SVG = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 32'>"
    "<line x1='12' y1='0' x2='12' y2='6' stroke='%23C08A2E' stroke-width='1' stroke-dasharray='1,2'/>"
    "<circle cx='12' cy='7' r='2' fill='%23C08A2E'/>"
    "<path d='M9 11h6v3H9z' fill='%23C08A2E'/>"
    "<path d='M7 14h10l-1.5 3h-7z' fill='%231F7A72'/>"
    "<rect x='7.5' y='17' width='9' height='9' rx='1.5' fill='%231F7A72'/>"
    "<path d='M8 17.5 L16 17.5' stroke='%23EADFC0' stroke-width='0.6'/>"
    "<path d='M8 21 L16 21' stroke='%23EADFC0' stroke-width='0.6'/>"
    "<path d='M8 24.5 L16 24.5' stroke='%23EADFC0' stroke-width='0.6'/>"
    "<path d='M9 26h6l-1.5 2.5h-3z' fill='%23C08A2E'/>"
    "<circle cx='12' cy='29.5' r='1' fill='%23C08A2E'/>"
    "</svg>"
)


def background_lanterns():
    """Large decorative lanterns hanging from the top corners, behind the
    card - purely a page-background flourish, matching the deck's title
    slide. Hidden behind the (opaque) card on narrow phones; visible in the
    margins on wider screens."""
    def lantern(side):
        style = {
            "position": "fixed",
            "top": "0",
            "width": "110px",
            "height": "147px",
            "background_image": f"url(\"{_BACKGROUND_LANTERN_SVG}\")",
            "background_repeat": "no-repeat",
            "background_size": "contain",
            "opacity": "0.6",
            "pointer_events": "none",
            "z_index": "0",
        }
        style[side] = "4%"
        return rx.el.div(style=style)

    return rx.el.div(
        lantern("left"),
        lantern("right"),
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
    "background": f"#F7ECD8 url(\"{_PATTERN_SVG}\")",
    "background_repeat": "repeat",
    "background_size": "84px 84px",
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


def explore_tab():
    return rx.el.div(
        hero(),
        selected_site_chip(),
        trust_rail(),
        arrival_alert_button(),
        ask_card(),
        rx.cond(
            RawiState.started,
            rx.cond(
                RawiState.is_offline_view,
                rx.el.div(
                    offline_notice(),
                    story_card(),
                    style={"display": "flex", "flex_direction": "column", "gap": "16px"},
                ),
                rx.el.div(
                    site_card(),
                    story_card(),
                    route_card(),
                    network_card(),
                    style={"display": "flex", "flex_direction": "column", "gap": "16px"},
                ),
            ),
        ),
        style={"display": "flex", "flex_direction": "column", "gap": "16px", "width": "100%"},
    )


def index():
    return rx.el.div(
        rx.el.div(
            brand_header(),
            tab_bar(),
            rx.cond(RawiState.active_tab == "explore", explore_tab()),
            rx.cond(RawiState.active_tab == "browse", browse_tab()),
            rx.cond(RawiState.active_tab == "favorites", favorites_tab()),
            rx.cond(RawiState.active_tab == "camara", camara_tab()),
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
            on_mount=RawiState.load_local_data,
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
        background_lanterns(),
        skyline_bar(),
        style=PAGE_STYLE,
    )
