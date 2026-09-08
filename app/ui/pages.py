"""Main Reflex pages."""

import reflex as rx

from app.ui.components import (
    FONT_BODY,
    FONT_HEADING,
    INK,
    INK_SOFT,
    LINE,
    RUST,
    RUST_DARK,
    SAND,
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
    location_preview_card,
    network_card,
    offline_notice,
    route_card,
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



_GLOBAL_ANIMATIONS = """
<style>
@keyframes rawiSplashOut {
  0%, 75% { opacity: 1; }
  100% { opacity: 0; visibility: hidden; pointer-events: none; }
}
@keyframes rawiPulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.04); }
}
@keyframes pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(174, 90, 46, 0.5); }
  50% { box-shadow: 0 0 0 8px rgba(174, 90, 46, 0); }
}
</style>
"""


def splash_screen():
    """A brief map-and-journey themed splash shown while the app boots,
    fading out on its own via a fixed-duration CSS animation - no need to
    hook into the backend connection lifecycle."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(tag="compass", size=24, color=TEAL_DEEP),
                style={
                    "width": "52px",
                    "height": "52px",
                    "border_radius": "999px",
                    "background": "white",
                    "display": "flex",
                    "align_items": "center",
                    "justify_content": "center",
                    "box_shadow": "0 4px 14px rgba(15, 74, 69, 0.2)",
                    "margin_bottom": "18px",
                },
            ),
            rx.el.div(
                rx.el.h1(
                    "RawiAI",
                    style={
                        "font_family": FONT_HEADING,
                        "font_size": "26px",
                        "font_weight": "700",
                        "color": INK,
                        "margin": "0",
                        "letter_spacing": "0.5px",
                    },
                ),
                rx.el.p("راوي", style={"font_family": FONT_HEADING, "font_size": "15px", "color": TEAL_DEEP, "margin": "2px 0 10px 0"}),
                rx.el.p(
                    "HERITAGE STORIES UNLEASHED",
                    style={
                        "font_family": FONT_BODY,
                        "font_size": "10px",
                        "font_weight": "700",
                        "letter_spacing": "1.5px",
                        "text_transform": "uppercase",
                        "color": RUST,
                        "margin": "0",
                    },
                ),
                style={
                    "background": TEAL_SOFT,
                    "padding": "22px 36px",
                    "border_radius": "18px",
                    "transform": "rotate(-2deg)",
                    "box_shadow": "0 10px 30px rgba(15, 74, 69, 0.25)",
                    "border": f"2px dashed {LINE}",
                    "text_align": "center",
                },
            ),
            rx.el.h2(
                "Let the network\ntell the story.",
                style={
                    "font_family": FONT_HEADING,
                    "font_size": "19px",
                    "font_weight": "700",
                    "color": INK,
                    "line_height": "1.3",
                    "white_space": "pre-line",
                    "text_align": "center",
                    "margin": "22px 0 4px 0",
                },
            ),
            rx.el.p(
                "يروي لك الحكاية دون أي تحميل",
                style={"font_family": FONT_HEADING, "font_size": "13px", "color": INK_SOFT, "margin": "0 0 20px 0", "text_align": "center"},
            ),
            rx.el.button(
                "Begin Your Journey · ابدأ الرحلة",
                on_click=rx.call_script(
                    "var el = document.getElementById('rawi-splash'); if (el) { el.style.animation = 'none'; el.style.display = 'none'; }"
                ),
                style={
                    "font_family": FONT_BODY,
                    "padding": "13px 30px",
                    "border": "none",
                    "border_radius": "999px",
                    "background": f"linear-gradient(135deg, {RUST}, {RUST_DARK})",
                    "color": "white",
                    "font_size": "13px",
                    "font_weight": "700",
                    "cursor": "pointer",
                    "box_shadow": "0 8px 18px rgba(174, 90, 46, 0.35)",
                },
            ),
            style={
                "display": "flex",
                "flex_direction": "column",
                "align_items": "center",
                "position": "relative",
                "z_index": "1",
                "padding": "0 24px",
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
            "background": f"{SAND} url(\"{_PATTERN_SVG}\")",
            "background_size": "84px 84px",
            "animation": "rawiSplashOut 0.6s ease 1.4s forwards",
        },
    )

PAGE_STYLE = {
    "min_height": "100vh",
    "width": "100%",
    "display": "flex",
    "justify_content": "center",
    "background": f"{SAND} url(\"{_PATTERN_SVG}\")",
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
        trust_rail(),
        arrival_alert_button(),
        ask_card(),
        location_preview_card(),
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
        rx.html(_GLOBAL_ANIMATIONS),
        splash_screen(),
        # Ambient background track, toggled by music_toggle_button() in the
        # header. Not autoplaying (browsers block that without a user
        # gesture anyway) - starts/stops only when tapped. preload="none"
        # because the current track is ~25MB; nothing downloads until the
        # visitor actually taps the music button.
        rx.el.audio(src="/audio/music.m4a", id="rawi-bgm", loop=True, preload="none", style={"display": "none"}),
        style=PAGE_STYLE,
    )
