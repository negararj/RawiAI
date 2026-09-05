"""Reusable, styled Reflex UI components for RawiAI."""

import reflex as rx

from app.ui.state import RawiState

# ---------------------------------------------------------------------------
# Design tokens
# ---------------------------------------------------------------------------

INK = "#2D1F17"
INK_SOFT = "#7A6A5C"
SAND = "#FBF3E4"
CARD = "#FFFCF6"
LINE = "#EDE0CC"
RUST = "#B85C2E"
RUST_DARK = "#8F4620"
TEAL = "#2F9C93"
TEAL_SOFT = "#E4F4F1"
GOLD = "#D9A441"

CARD_STYLE = {
    "background": CARD,
    "border": f"1px solid {LINE}",
    "border_radius": "20px",
    "padding": "18px 20px",
    "width": "100%",
    "box_shadow": "0 2px 10px rgba(45, 31, 23, 0.05)",
}


def card(*children, **style):
    merged = {**CARD_STYLE, **style}
    return rx.el.div(*children, style=merged)


def eyebrow(text: str, color: str = RUST):
    return rx.el.p(
        text.upper(),
        style={
            "font_size": "11px",
            "font_weight": "700",
            "letter_spacing": "1.5px",
            "color": color,
            "margin": "0",
        },
    )


# ---------------------------------------------------------------------------
# Header / hero
# ---------------------------------------------------------------------------


def lantern_mark():
    return rx.el.div(
        "🏮",
        style={
            "font_size": "20px",
            "width": "38px",
            "height": "38px",
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
            "background": TEAL_SOFT,
            "border_radius": "12px",
        },
    )


def language_toggle():
    def option(label: str, code: str):
        is_active = RawiState.language == code
        return rx.el.button(
            label,
            on_click=RawiState.set_language(code),
            style={
                "padding": "6px 14px",
                "font_size": "13px",
                "font_weight": "600",
                "border_radius": "999px",
                "border": "none",
                "cursor": "pointer",
                "background": rx.cond(is_active, RUST, "transparent"),
                "color": rx.cond(is_active, "white", INK_SOFT),
                "transition": "all 0.15s ease",
            },
        )

    return rx.el.div(
        option("EN", "en"),
        option("عربي", "ar"),
        style={
            "display": "flex",
            "gap": "2px",
            "background": SAND,
            "border": f"1px solid {LINE}",
            "border_radius": "999px",
            "padding": "3px",
        },
    )


def brand_header():
    return rx.el.div(
        rx.el.div(
            lantern_mark(),
            rx.el.div(
                rx.el.p(
                    "RAWI AI",
                    style={
                        "font_size": "16px",
                        "font_weight": "800",
                        "color": INK,
                        "margin": "0",
                        "letter_spacing": "0.5px",
                    },
                ),
                rx.el.p(
                    "راوي",
                    style={"font_size": "12px", "color": INK_SOFT, "margin": "0"},
                ),
                style={"display": "flex", "flex_direction": "column", "gap": "1px"},
            ),
            style={"display": "flex", "align_items": "center", "gap": "10px"},
        ),
        language_toggle(),
        style={
            "display": "flex",
            "align_items": "center",
            "justify_content": "space-between",
            "width": "100%",
        },
    )


def hero():
    return rx.el.div(
        eyebrow("App-Free Telecom-Native Storyteller", color=TEAL),
        rx.el.h1(
            "Let the network\ntell the story.",
            style={
                "font_size": "30px",
                "font_weight": "800",
                "color": INK,
                "line_height": "1.2",
                "margin": "6px 0 4px 0",
                "white_space": "pre-line",
            },
        ),
        rx.el.p(
            "No app download. No rented headset. RawiAI verifies you're really "
            "at the site through Nokia CAMARA network APIs, then speaks its history aloud.",
            style={
                "font_size": "14px",
                "color": INK_SOFT,
                "line_height": "1.55",
                "margin": "0",
            },
        ),
        style={"display": "flex", "flex_direction": "column", "gap": "2px", "width": "100%"},
    )


# ---------------------------------------------------------------------------
# Trust rail — the four CAMARA signals checked before the story begins
# ---------------------------------------------------------------------------


def trust_chip(icon: str, label: str, active):
    return rx.el.div(
        rx.icon(
            tag=icon,
            size=15,
            color=rx.cond(active, "white", INK_SOFT),
        ),
        rx.el.span(label, style={"font_size": "11px", "font_weight": "600"}),
        style={
            "display": "flex",
            "align_items": "center",
            "gap": "6px",
            "padding": "8px 10px",
            "border_radius": "12px",
            "background": rx.cond(active, TEAL, SAND),
            "color": rx.cond(active, "white", INK_SOFT),
            "border": f"1px solid {rx.cond(active, TEAL, LINE)}",
            "transition": "all 0.2s ease",
            "flex": "1",
            "justify_content": "center",
        },
    )


def trust_rail():
    return rx.el.div(
        trust_chip("shield-check", "Identity", RawiState.step_identity),
        trust_chip("map-pin", "Presence", RawiState.step_presence),
        trust_chip("radio-tower", "Network", RawiState.step_network),
        trust_chip("gauge", "QoD", RawiState.step_qos),
        style={"display": "flex", "gap": "8px", "width": "100%"},
    )


# ---------------------------------------------------------------------------
# Ask card
# ---------------------------------------------------------------------------


def ask_card():
    return card(
        rx.el.p(
            "Ask Rawi",
            style={"font_size": "13px", "font_weight": "700", "color": INK, "margin": "0 0 10px 0"},
        ),
        rx.el.input(
            value=RawiState.question,
            on_change=RawiState.set_question,
            placeholder="Ask about this place...",
            style={
                "width": "100%",
                "padding": "12px 14px",
                "border_radius": "12px",
                "border": f"1px solid {LINE}",
                "background": SAND,
                "font_size": "14px",
                "color": INK,
                "outline": "none",
                "box_sizing": "border-box",
            },
        ),
        rx.el.button(
            rx.cond(RawiState.is_loading, "Listening to the network...", "Begin the Story"),
            on_click=RawiState.start_demo,
            disabled=RawiState.is_loading,
            style={
                "width": "100%",
                "margin_top": "12px",
                "padding": "13px",
                "border": "none",
                "border_radius": "14px",
                "background": f"linear-gradient(135deg, {RUST}, {RUST_DARK})",
                "color": "white",
                "font_size": "14px",
                "font_weight": "700",
                "cursor": rx.cond(RawiState.is_loading, "default", "pointer"),
                "opacity": rx.cond(RawiState.is_loading, "0.75", "1"),
                "box_shadow": f"0 8px 18px rgba(184, 92, 46, 0.35)",
            },
        ),
        rx.el.div(
            rx.icon(tag="sparkles", size=13, color=TEAL),
            rx.el.p(RawiState.status, style={"font_size": "12px", "color": INK_SOFT, "margin": "0"}),
            style={"display": "flex", "align_items": "center", "gap": "6px", "margin_top": "10px"},
        ),
    )


# ---------------------------------------------------------------------------
# Result cards (shown after the demo starts)
# ---------------------------------------------------------------------------


def section_label(icon: str, text: str, color: str = RUST):
    return rx.el.div(
        rx.icon(tag=icon, size=14, color=color),
        rx.el.span(
            text.upper(),
            style={"font_size": "11px", "font_weight": "700", "letter_spacing": "0.8px", "color": color},
        ),
        style={"display": "flex", "align_items": "center", "gap": "6px", "margin_bottom": "8px"},
    )


def site_card():
    return card(
        section_label("map-pin", "Current Site", TEAL),
        rx.el.p(
            RawiState.current_site,
            style={"font_size": "18px", "font_weight": "800", "color": INK, "margin": "0"},
        ),
        rx.el.p(
            RawiState.geofence_status,
            style={"font_size": "12px", "color": INK_SOFT, "margin": "4px 0 0 0"},
        ),
    )


def story_card():
    return card(
        section_label("volume-2", "Story", RUST),
        rx.el.p(
            RawiState.answer,
            id="rawi-answer",
            style={
                "font_size": "15px",
                "color": INK,
                "line_height": "1.75",
                "margin": "0",
                "text_align": RawiState.text_align,
                "white_space": "pre-line",
            },
        ),
        rx.el.p(RawiState.language, id="rawi-language", style={"display": "none"}),
        rx.el.div(
            rx.el.button(
                rx.icon(tag="volume-2", size=14, color="white"),
                rx.el.span("Speak Story", style={"font_size": "13px", "font_weight": "600", "color": "white"}),
                on_click=rx.call_script(
                    """
const text = document.getElementById("rawi-answer")?.innerText || "";
const language = document.getElementById("rawi-language")?.innerText || "en";
if (text.trim()) {
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = language === "ar" ? "ar-SA" : "en-US";
  window.speechSynthesis.speak(utterance);
}
"""
                ),
                style={
                    "display": "flex",
                    "align_items": "center",
                    "gap": "6px",
                    "padding": "9px 14px",
                    "border_radius": "999px",
                    "border": "none",
                    "background": RUST,
                    "cursor": "pointer",
                },
            ),
            rx.el.button(
                rx.icon(tag="square", size=14, color=RUST),
                rx.el.span("Stop", style={"font_size": "13px", "font_weight": "600", "color": RUST}),
                on_click=rx.call_script("window.speechSynthesis.cancel();"),
                style={
                    "display": "flex",
                    "align_items": "center",
                    "gap": "6px",
                    "padding": "9px 14px",
                    "border_radius": "999px",
                    "border": f"1px solid {RUST}",
                    "background": "transparent",
                    "cursor": "pointer",
                },
            ),
            style={"display": "flex", "gap": "10px", "margin_top": "14px"},
        ),
        rx.el.p(
            f"Source: {RawiState.story_source}",
            style={"font_size": "11px", "color": INK_SOFT, "margin_top": "10px"},
        ),
    )


def congestion_badge():
    is_high = RawiState.congestion_level == "High"
    is_medium = RawiState.congestion_level == "Medium"
    color = rx.cond(is_high, "#C24E3A", rx.cond(is_medium, GOLD, TEAL))
    return rx.el.span(
        RawiState.congestion_level,
        style={
            "font_size": "11px",
            "font_weight": "700",
            "padding": "3px 10px",
            "border_radius": "999px",
            "background": color,
            "color": "white",
        },
    )


def route_card():
    return card(
        rx.el.div(
            section_label("route", "Route", TEAL),
            congestion_badge(),
            style={"display": "flex", "align_items": "center", "justify_content": "space-between"},
        ),
        rx.el.p(
            RawiState.route,
            style={"font_size": "15px", "font_weight": "700", "color": INK, "margin": "0"},
        ),
        rx.el.p(
            RawiState.route_reason,
            style={"font_size": "12px", "color": INK_SOFT, "margin": "6px 0 0 0", "line-height": "1.5"},
        ),
    )


def network_card():
    return card(
        section_label("gauge", "Network Quality", RUST),
        rx.el.p(
            f"Quality on Demand: {RawiState.qos_status}",
            style={"font_size": "15px", "font_weight": "700", "color": INK, "margin": "0"},
        ),
        rx.el.p(
            "Requested extra bandwidth priority so narration streams without buffering.",
            style={"font_size": "12px", "color": INK_SOFT, "margin": "6px 0 0 0", "line-height": "1.5"},
        ),
    )


def timeline_card():
    def row(item):
        return rx.el.div(
            rx.el.div(style={
                "width": "6px", "height": "6px", "border_radius": "999px",
                "background": TEAL, "margin_top": "6px", "flex_shrink": "0",
            }),
            rx.el.div(
                rx.el.p(item["step"], style={"font_size": "13px", "font_weight": "700", "color": INK, "margin": "0"}),
                rx.el.p(item["detail"], style={"font_size": "12px", "color": INK_SOFT, "margin": "2px 0 0 0"}),
                rx.el.p(
                    item["source"],
                    style={"font_size": "10px", "color": TEAL, "margin": "3px 0 0 0", "font_family": "monospace"},
                ),
            ),
            style={"display": "flex", "gap": "10px", "padding": "8px 0", "border_bottom": f"1px solid {LINE}"},
        )

    return card(
        section_label("shield-check", "CAMARA Proof", TEAL),
        rx.el.p(
            "We're not only using browser GPS — every step below is confirmed by a Nokia CAMARA network API call.",
            style={"font_size": "12px", "color": INK_SOFT, "margin": "0 0 6px 0", "line-height": "1.5"},
        ),
        rx.el.div(rx.foreach(RawiState.timeline, row), style={"width": "100%"}),
    )


# ---------------------------------------------------------------------------
# Install / footer
# ---------------------------------------------------------------------------


def install_card():
    return card(
        rx.el.div(
            rx.icon(tag="download", size=18, color=RUST),
            rx.el.div(
                rx.el.p(
                    "Install RawiAI",
                    style={"font_size": "13px", "font_weight": "700", "color": INK, "margin": "0"},
                ),
                rx.el.p(
                    RawiState.pwa_status,
                    style={"font_size": "11px", "color": INK_SOFT, "margin": "2px 0 0 0"},
                ),
            ),
            style={"display": "flex", "align_items": "center", "gap": "10px", "flex": "1"},
        ),
        rx.el.button(
            "Install",
            on_click=rx.call_script(
                """
if (window.rawiInstallPrompt) {
  window.rawiInstallPrompt.prompt();
  window.rawiInstallPrompt.userChoice.finally(() => {
    window.rawiInstallPrompt = null;
  });
} else {
  alert("Install is available from your browser menu on supported devices.");
}
"""
            ),
            style={
                "padding": "9px 16px",
                "border_radius": "999px",
                "border": "none",
                "background": SAND,
                "color": RUST_DARK,
                "font_size": "12px",
                "font_weight": "700",
                "cursor": "pointer",
                "flex_shrink": "0",
            },
        ),
        style={**CARD_STYLE, "display": "flex", "align_items": "center", "justify_content": "space-between", "background": TEAL_SOFT, "border": "none"},
    )
