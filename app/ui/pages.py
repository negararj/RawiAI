"""Main Reflex pages."""

import reflex as rx

from app.ui.components import (
    FONT_BODY,
    FONT_HEADING,
    GOLD,
    INK,
    INK_SOFT,
    LINE,
    RUST,
    RUST_DARK,
    SAND,
    TEAL,
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

# The exact background dot-grid from the Figma export's `.screen::before`
# rule: a radial-gradient ring repeated on a 56px tile, ink-tinted at 6%
# opacity, blended with multiply.
_PATTERN_BACKGROUND = (
    "radial-gradient(circle at center, transparent 0px 9px, "
    "rgba(43, 29, 20, 0.06) 9.5px 10.5px, transparent 11px)"
)

# The three decorative line-art motifs from the Figma export's <symbol>
# defs (d-tree-palm, d-ring-crosshair, d-ring-wide) - reproduced with the
# exact path data so the background matches pixel-for-pixel.
_DECO_TREE_PATH = (
    "M33.3 46.7H20L16.7 40.8 13.3 46.7H6.7C6.7 30.6 14.9 17.5 25 17.5S43.3 30.6 43.3 46.7"
    "C45 58.3 53.3 96.3 46.7 128.3H33.3C36.1 116.7 38.3 105 36.7 90.4"
    "M43.3 41.7C46.7 37.3 50.8 35 55 35c10.1 0 18.3 13.1 18.3 29.2H63.3l-3.3-5.8-3.3 5.8H46.7"
    "M19.6 56.6C12.5 69.2 12 88.6 18.5 100l14.1-24.8 11.8-20.6C37.9 43.2 26.8 44.1 19.6 56.6z"
)
_DECO_RING_CROSSHAIR_PATH = (
    "M75 37.5L45 62.5M45 37.5L75 62.5"
    "M110 50c0 23-22.4 41.7-50 41.7S10 73 10 50 32.4 8.3 60 8.3 110 27 110 50z"
)
_DECO_RING_WIDE_PATH = (
    "M150 22.5L90 37.5M90 22.5l60 15"
    "M220 30c0 13.8-44.8 25-100 25S20 43.8 20 30 64.8 5 120 5s100 11.2 100 25z"
)


def _deco_svg(path: str, view_box: str, color: str, style: dict):
    return rx.el.svg(
        rx.el.path(d=path, stroke=color, stroke_width="2", fill="none", stroke_linecap="round"),
        view_box=view_box,
        style={"position": "fixed", "pointer_events": "none", "z_index": "0", **style},
    )


def screen_decorations():
    """The Figma export's three background motifs (palm tree, gold
    crosshair-ring, rust wide-ring), positioned exactly as specified."""
    return rx.el.div(
        _deco_svg(_DECO_TREE_PATH, "0 0 80 140", TEAL, {"width": "80px", "height": "140px", "left": "-10px", "bottom": "80px"}),
        _deco_svg(_DECO_RING_CROSSHAIR_PATH, "0 0 120 100", GOLD, {"width": "120px", "height": "100px", "right": "-20px", "bottom": "120px"}),
        _deco_svg(_DECO_RING_WIDE_PATH, "0 0 240 60", RUST, {"width": "240px", "height": "60px", "left": "0", "bottom": "140px"}),
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
                "background_image": "url('/illustrations/palm.png')",
                "background_repeat": "no-repeat",
                "background_size": "contain",
                "opacity": "0.9",
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
                "background_image": "url('/illustrations/camel.png')",
                "background_repeat": "no-repeat",
                "background_size": "contain",
                "opacity": "0.9",
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
                    "UAE STORIES UNLEASHED",
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
            "background": f"{SAND} {_PATTERN_BACKGROUND}",
            "background_size": "56px 56px",
            "animation": "rawiSplashOut 0.6s ease 1.4s forwards",
        },
    )

PAGE_STYLE = {
    "min_height": "100vh",
    "width": "100%",
    "display": "flex",
    "justify_content": "center",
    "background": f"{SAND} {_PATTERN_BACKGROUND}",
    "background_repeat": "repeat",
    "background_size": "56px 56px",
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
        screen_decorations(),
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
