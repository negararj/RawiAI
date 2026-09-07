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

def desert_scene():
    """A camel ambling low along the bottom of the viewport - the only
    "foreground" background element; everything else in skyline_bar()
    blends in at low opacity instead."""
    return rx.el.div(
        style={
            "position": "fixed",
            "bottom": "8px",
            "left": "-15%",
            "width": "150px",
            "height": "86px",
            "background_image": "url('/illustrations/camel.png')",
            "background_repeat": "no-repeat",
            "background_size": "contain",
            "opacity": "0.85",
            "pointer_events": "none",
            "z_index": "0",
            "animation": "rawiWalk 40s linear infinite",
        }
    )


def skyline_bar():
    """A low-opacity skyline vignette along the bottom of the viewport,
    blended into the background rather than competing with foreground
    text: the skyline centered, the Burj Al Arab to its right, and the
    palm tree to its left."""
    return rx.el.div(
        rx.el.div(
            style={
                "position": "fixed",
                "bottom": "0",
                "left": "50%",
                "transform": "translateX(-50%)",
                "width": "210px",
                "height": "95px",
                "background_image": "url('/illustrations/skyline.png')",
                "background_repeat": "no-repeat",
                "background_position": "center bottom",
                "background_size": "contain",
                "opacity": "0.3",
                "pointer_events": "none",
                "z_index": "0",
            }
        ),
        rx.el.div(
            style={
                "position": "fixed",
                "bottom": "0",
                "right": "6%",
                "width": "46px",
                "height": "120px",
                "background_image": "url('/illustrations/burj-al-arab.png')",
                "background_repeat": "no-repeat",
                "background_position": "center bottom",
                "background_size": "contain",
                "opacity": "0.3",
                "pointer_events": "none",
                "z_index": "0",
            }
        ),
        rx.el.div(
            style={
                "position": "fixed",
                "bottom": "0",
                "left": "4%",
                "width": "80px",
                "height": "134px",
                "background_image": "url('/illustrations/palm.png')",
                "background_repeat": "no-repeat",
                "background_position": "center bottom",
                "background_size": "contain",
                "opacity": "0.3",
                "pointer_events": "none",
                "z_index": "0",
            }
        ),
    )


_GLOBAL_ANIMATIONS = """
<style>
/* English display headings, matching the pitch deck. Only in the font
   stack (see FONT_HEADING) - the browser falls back to Reem Kufi per
   glyph for any character Barabara doesn't cover, so Arabic headings are
   unaffected without any language-conditional logic. */
@font-face {
  font-family: 'Barabara';
  src: url('/fonts/BARABARA-final.otf') format('opentype');
  font-display: swap;
}
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
        desert_scene(),
        skyline_bar(),
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
