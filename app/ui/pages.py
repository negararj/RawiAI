"""Main Reflex pages."""

import reflex as rx

from app.ui.components import (
    FONT_BODY,
    FONT_HEADING,
    INK,
    INK_SOFT,
    SKY_MINT,
    TEAL_DEEP,
    TEAL_SOFT,
    arrival_alert_button,
    arrival_watch_script,
    ask_card,
    brand_header,
    browse_tab,
    camara_tab,
    favorites_tab,
    passport_tab,
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
    "<g fill='none' stroke='%23C08A2E' stroke-width='1.5' opacity='0.11'>"
    "<circle cx='0' cy='0' r='42'/>"
    "<circle cx='84' cy='0' r='42'/>"
    "<circle cx='0' cy='84' r='42'/>"
    "<circle cx='84' cy='84' r='42'/>"
    "<circle cx='42' cy='42' r='42'/>"
    "</g></svg>"
)

# A simple side-profile camel silhouette - ellipses and lines only, so
# there's no arc-radius geometry to get wrong. The "walking" comes entirely
# from animating this static pose across the screen, not from leg motion.
_CAMEL_SVG = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 140 80'>"
    "<g fill='none' stroke='%23B8763F' stroke-width='4' stroke-linecap='round'>"
    "<line x1='40' y1='58' x2='40' y2='70'/>"
    "<line x1='52' y1='60' x2='52' y2='70'/>"
    "<line x1='85' y1='60' x2='85' y2='70'/>"
    "<line x1='97' y1='58' x2='97' y2='70'/>"
    "</g>"
    "<ellipse cx='65' cy='48' rx='32' ry='16' fill='%23B8763F'/>"
    "<circle cx='52' cy='28' r='14' fill='%23B8763F'/>"
    "<line x1='90' y1='42' x2='112' y2='15' stroke='%23B8763F' stroke-width='12' stroke-linecap='round'/>"
    "<ellipse cx='118' cy='10' rx='9' ry='6' fill='%23B8763F'/>"
    "<line x1='35' y1='45' x2='25' y2='58' stroke='%23B8763F' stroke-width='3' stroke-linecap='round'/>"
    "</svg>"
)

# A palm tree - trunk plus radiating fronds, swayed as one rigid shape
# (matches how a real palm sways as a whole, and avoids animating a single
# sub-part of a background-image, which CSS can't do anyway).
_PALM_SVG = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 100'>"
    "<line x1='30' y1='95' x2='34' y2='30' stroke='%232B1D14' stroke-width='6' stroke-linecap='round'/>"
    "<g stroke='%233C8C5C' stroke-width='5' stroke-linecap='round'>"
    "<line x1='34' y1='30' x2='10' y2='15'/>"
    "<line x1='34' y1='30' x2='20' y2='8'/>"
    "<line x1='34' y1='30' x2='34' y2='4'/>"
    "<line x1='34' y1='30' x2='48' y2='9'/>"
    "<line x1='34' y1='30' x2='56' y2='20'/>"
    "</g>"
    "</svg>"
)


def desert_scene():
    """A camel ambling across the bottom of the viewport and a palm tree
    swaying nearby - the page-background flourish, replacing the lanterns."""
    return rx.el.div(
        rx.el.div(
            style={
                "position": "fixed",
                "bottom": "34px",
                "left": "-15%",
                "width": "90px",
                "height": "51px",
                "background_image": f"url(\"{_CAMEL_SVG}\")",
                "background_repeat": "no-repeat",
                "background_size": "contain",
                "opacity": "0.5",
                "pointer_events": "none",
                "z_index": "0",
                "animation": "rawiWalk 40s linear infinite",
            }
        ),
        rx.el.div(
            style={
                "position": "fixed",
                "bottom": "30px",
                "right": "6%",
                "width": "70px",
                "height": "117px",
                "background_image": f"url(\"{_PALM_SVG}\")",
                "background_repeat": "no-repeat",
                "background_size": "contain",
                "opacity": "0.45",
                "pointer_events": "none",
                "z_index": "0",
                "animation": "rawiSway 6s ease-in-out infinite",
                "transform_origin": "bottom center",
            }
        ),
    )


_GLOBAL_ANIMATIONS = """
<style>
@keyframes rawiSway {
  0%, 100% { transform: rotate(-3deg); }
  50% { transform: rotate(3deg); }
}
@keyframes rawiSplashOut {
  0%, 75% { opacity: 1; }
  100% { opacity: 0; visibility: hidden; pointer-events: none; }
}
@keyframes rawiPulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.04); }
}
@keyframes rawiWalk {
  0% { left: -15%; }
  100% { left: 115%; }
}
</style>
"""


def splash_screen():
    """A brief map-and-journey themed splash shown while the app boots,
    fading out on its own via a fixed-duration CSS animation - no need to
    hook into the backend connection lifecycle."""
    return rx.el.div(
        rx.icon(
            tag="compass",
            size=30,
            color=TEAL_DEEP,
            style={"position": "absolute", "top": "10%", "right": "12%", "opacity": "0.8"},
        ),
        rx.el.div(
            style={
                "position": "absolute",
                "bottom": "18%",
                "right": "8%",
                "width": "60px",
                "height": "100px",
                "background_image": f"url(\"{_PALM_SVG}\")",
                "background_repeat": "no-repeat",
                "background_size": "contain",
                "opacity": "0.75",
                "animation": "rawiSway 6s ease-in-out infinite",
                "transform_origin": "bottom center",
            }
        ),
        rx.el.div(
            style={
                "position": "fixed",
                "bottom": "12%",
                "width": "100px",
                "height": "57px",
                "background_image": f"url(\"{_CAMEL_SVG}\")",
                "background_repeat": "no-repeat",
                "background_size": "contain",
                "opacity": "0.75",
                "animation": "rawiWalk 14s linear infinite",
            }
        ),
        rx.el.svg(
            rx.el.path(
                d="M20 20 Q40 40 20 60 Q0 80 30 90",
                stroke=INK,
                stroke_width="2",
                fill="none",
                stroke_dasharray="4,5",
            ),
            rx.el.line(x1="26", y1="86", x2="34", y2="94", stroke=INK, stroke_width="2"),
            rx.el.line(x1="34", y1="86", x2="26", y2="94", stroke=INK, stroke_width="2"),
            view_box="0 0 100 100",
            width="70",
            height="70",
            style={"position": "absolute", "top": "14%", "left": "10%", "opacity": "0.7"},
        ),
        rx.el.div(
            rx.el.p("راوي", style={"font_family": FONT_HEADING, "font_size": "16px", "color": TEAL_DEEP, "margin": "0"}),
            rx.el.h1(
                "RAWI AI",
                style={
                    "font_family": FONT_HEADING,
                    "font_size": "32px",
                    "font_weight": "700",
                    "color": INK,
                    "margin": "4px 0 0 0",
                    "letter_spacing": "1px",
                },
            ),
            style={
                "background": TEAL_SOFT,
                "padding": "28px 40px",
                "border_radius": "18px",
                "transform": "rotate(-2deg)",
                "box_shadow": "0 10px 30px rgba(15, 74, 69, 0.25)",
                "text_align": "center",
            },
        ),
        id="rawi-splash",
        style={
            "position": "fixed",
            "inset": "0",
            "z_index": "9999",
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
            "background": f"{SKY_MINT} url(\"{_PATTERN_SVG}\")",
            "background_size": "84px 84px",
            "animation": "rawiSplashOut 0.6s ease 1.4s forwards",
        },
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
            rx.cond(RawiState.active_tab == "passport", passport_tab()),
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
        desert_scene(),
        skyline_bar(),
        rx.html(_GLOBAL_ANIMATIONS),
        splash_screen(),
        style=PAGE_STYLE,
    )
