"""Reusable, styled Reflex UI components for RawiAI."""

import json

import reflex as rx

from app.agents.sites import AL_HISN_FORT, AL_HISN_FORT_ALT_ENTRANCE
from app.ui.state import RawiState

# ---------------------------------------------------------------------------
# Design tokens
# ---------------------------------------------------------------------------

INK = "#2B1D14"
INK_SOFT = "#7C6650"
SAND = "#F6EAD2"
CARD = "#FFFBF2"
LINE = "#E4D2AC"
RUST = "#AE5A2E"
RUST_DARK = "#7F3E1E"
TEAL = "#1F7A72"
TEAL_DEEP = "#0F4A45"
TEAL_SOFT = "#E1EFEC"
GOLD = "#C08A2E"
GOLD_SOFT = "#EADFC0"

FONT_HEADING = "'Reem Kufi', 'Tajawal', sans-serif"
FONT_BODY = "'Tajawal', 'Cairo', sans-serif"
FONT_STORY = "'Amiri', 'Tajawal', serif"

CARD_STYLE = {
    "background": CARD,
    "border": f"1px solid {LINE}",
    "border_radius": "18px",
    "padding": "18px 20px",
    "width": "100%",
    "box_shadow": "0 2px 12px rgba(43, 29, 20, 0.06)",
    "position": "relative",
}

# A thin repeating eight-point-star motif used as a hairline accent under
# card headers - a nod to Islamic geometric pattern work without needing an
# image asset.
_STAR_DIVIDER_SVG = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='24' height='8'>"
    "<path d='M0 4 L4 4 M8 1 L10 4 L8 7 M14 1 L16 4 L14 7 M20 4 L24 4' "
    "stroke='%23C08A2E' stroke-width='1' fill='none' opacity='0.55'/>"
    "</svg>"
)


def card(*children, **style):
    merged = {**CARD_STYLE, **style}
    return rx.el.div(*children, style=merged)


def star_divider():
    return rx.el.div(
        style={
            "width": "100%",
            "height": "8px",
            "background_image": f"url(\"{_STAR_DIVIDER_SVG}\")",
            "background_repeat": "repeat-x",
            "background_position": "center",
            "margin": "10px 0",
            "opacity": "0.8",
        }
    )


def eyebrow(text, color: str = RUST):
    return rx.el.p(
        text,
        style={
            "font_family": FONT_BODY,
            "font_size": "11px",
            "font_weight": "700",
            "letter_spacing": "1.5px",
            "text_transform": "uppercase",
            "color": color,
            "margin": "0",
        },
    )


# ---------------------------------------------------------------------------
# Localized UI strings
# ---------------------------------------------------------------------------

_STRINGS = {
    "tagline": ("App-Free Telecom-Native Storyteller", "راوي حضاري بلا تطبيقات، عبر شبكتك"),
    "hero_title": ("Let the network\ntell the story.", "دع الشبكة\nترِ الحكاية."),
    "hero_body": (
        "No app download. No rented headset. RawiAI verifies you're really "
        "at the site through Nokia CAMARA network APIs, then speaks its history aloud.",
        "بلا تحميل تطبيق، وبلا استئجار سماعات. راوي يتحقق من وجودك فعليًا عند الموقع "
        "عبر واجهات نوكيا CAMARA، ثم يروي لك قصته صوتيًا.",
    ),
    "identity": ("Identity", "الهوية"),
    "presence": ("Presence", "الحضور"),
    "network": ("Network", "الشبكة"),
    "qod": ("QoD", "جودة الخدمة"),
    "ask_rawi": ("Ask Rawi", "اسأل راوي"),
    "question_placeholder": ("Ask about this place...", "اسأل عن هذا المكان..."),
    "begin_story": ("Begin the Story", "ابدأ الحكاية"),
    "listening": ("Listening to the network...", "يستمع إلى الشبكة..."),
    "current_site": ("Current Site", "الموقع الحالي"),
    "story": ("Story", "الحكاية"),
    "speak_story": ("Speak Story", "اروِ الحكاية"),
    "stop": ("Stop", "إيقاف"),
    "source": ("Source", "المصدر"),
    "route": ("Route", "المسار"),
    "network_quality": ("Network Quality", "جودة الشبكة"),
    "qod_line": ("Quality on Demand", "جودة الخدمة عند الطلب"),
    "qod_detail": (
        "Requested extra bandwidth priority so narration streams without buffering.",
        "تم طلب أولوية إضافية في النطاق الترددي ليصلك الصوت دون تقطّع.",
    ),
    "camara_proof": ("CAMARA Proof", "إثبات CAMARA"),
    "camara_proof_body": (
        "We're not only using browser GPS — every step below is confirmed by a Nokia CAMARA network API call.",
        "نحن لا نعتمد على GPS المتصفح فقط - كل خطوة أدناه مؤكدة عبر استدعاء فعلي لواجهات نوكيا CAMARA.",
    ),
    "install_title": ("Install RawiAI", "ثبّت راوي"),
    "install_button": ("Install", "تثبيت"),
    "footer": (
        "DevNull · Immersive Tourism & Smart Cities · Nokia CAMARA Hackathon",
        "DevNull · السياحة الغامرة والمدن الذكية · هاكاثون نوكيا CAMARA",
    ),
}


def t(key: str):
    en, ar = _STRINGS[key]
    return rx.cond(RawiState.is_ar, ar, en)


# ---------------------------------------------------------------------------
# Header / hero
# ---------------------------------------------------------------------------


def lantern_mark():
    """A small hand-drawn Arabian fanous (lantern), matching the pitch deck's
    teal-and-gold lantern motif, instead of a generic emoji."""
    return rx.el.div(
        rx.el.svg(
            rx.el.path(d="M9 3h6v3H9z", fill=GOLD),
            rx.el.path(d="M7 6h10l-1.5 3h-7z", fill=TEAL),
            rx.el.rect(x="7.5", y="9", width="9", height="9", rx="1.5", fill=TEAL),
            rx.el.path(d="M8 9.5 L16 9.5", stroke=GOLD_SOFT, stroke_width="0.6"),
            rx.el.path(d="M8 13 L16 13", stroke=GOLD_SOFT, stroke_width="0.6"),
            rx.el.path(d="M8 16.5 L16 16.5", stroke=GOLD_SOFT, stroke_width="0.6"),
            rx.el.path(d="M9 18h6l-1.5 2.5h-3z", fill=GOLD),
            rx.el.circle(cx="12", cy="21.5", r="1", fill=GOLD),
            view_box="0 0 24 24",
            width="22",
            height="22",
            fill="none",
        ),
        style={
            "width": "38px",
            "height": "38px",
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
            "background": TEAL_SOFT,
            "border_radius": "12px",
            "border": f"1px solid {LINE}",
            "flex_shrink": "0",
        },
    )


def language_toggle():
    def option(label: str, code: str):
        is_active = RawiState.language == code
        return rx.el.button(
            label,
            on_click=RawiState.set_language(code),
            style={
                "font_family": FONT_BODY,
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
                        "font_family": FONT_HEADING,
                        "font_size": "17px",
                        "font_weight": "700",
                        "color": INK,
                        "margin": "0",
                        "letter_spacing": "0.5px",
                    },
                ),
                rx.el.p(
                    "راوي",
                    style={
                        "font_family": FONT_HEADING,
                        "font_size": "13px",
                        "color": TEAL_DEEP,
                        "margin": "0",
                    },
                ),
                style={"display": "flex", "flex_direction": "column", "gap": "1px"},
            ),
            style={
                "display": "flex",
                "align_items": "center",
                "gap": "10px",
                "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
            },
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
        eyebrow(t("tagline"), color=TEAL),
        rx.el.h1(
            t("hero_title"),
            style={
                "font_family": FONT_HEADING,
                "font_size": "28px",
                "font_weight": "700",
                "color": INK,
                "line_height": "1.3",
                "margin": "8px 0 6px 0",
                "white_space": "pre-line",
                "text_align": RawiState.text_align,
            },
        ),
        rx.el.p(
            t("hero_body"),
            style={
                "font_family": FONT_BODY,
                "font_size": "14px",
                "color": INK_SOFT,
                "line_height": "1.6",
                "margin": "0",
                "text_align": RawiState.text_align,
            },
        ),
        star_divider(),
        style={"display": "flex", "flex_direction": "column", "gap": "2px", "width": "100%"},
    )


# ---------------------------------------------------------------------------
# Trust rail — the four CAMARA signals checked before the story begins
# ---------------------------------------------------------------------------


def trust_chip(icon: str, label, active):
    return rx.el.div(
        rx.icon(
            tag=icon,
            size=15,
            color=rx.cond(active, "white", INK_SOFT),
        ),
        rx.el.span(label, style={"font_family": FONT_BODY, "font_size": "11px", "font_weight": "600"}),
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
        trust_chip("shield-check", t("identity"), RawiState.step_identity),
        trust_chip("map-pin", t("presence"), RawiState.step_presence),
        trust_chip("radio-tower", t("network"), RawiState.step_network),
        trust_chip("gauge", t("qod"), RawiState.step_qos),
        style={"display": "flex", "gap": "8px", "width": "100%"},
    )


# ---------------------------------------------------------------------------
# Ask card
# ---------------------------------------------------------------------------


def ask_card():
    return card(
        rx.el.p(
            t("ask_rawi"),
            style={
                "font_family": FONT_HEADING,
                "font_size": "14px",
                "font_weight": "700",
                "color": INK,
                "margin": "0 0 10px 0",
                "text_align": RawiState.text_align,
            },
        ),
        rx.el.input(
            value=RawiState.question,
            on_change=RawiState.set_question,
            placeholder=t("question_placeholder"),
            dir=RawiState.dir,
            style={
                "font_family": FONT_BODY,
                "width": "100%",
                "padding": "12px 14px",
                "border_radius": "12px",
                "border": f"1px solid {LINE}",
                "background": SAND,
                "font_size": "14px",
                "color": INK,
                "outline": "none",
                "box_sizing": "border-box",
                "text_align": RawiState.text_align,
            },
        ),
        rx.el.button(
            rx.cond(RawiState.is_loading, t("listening"), t("begin_story")),
            on_click=RawiState.start_demo,
            disabled=RawiState.is_loading,
            style={
                "font_family": FONT_BODY,
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
                "box_shadow": "0 8px 18px rgba(174, 90, 46, 0.35)",
            },
        ),
        rx.el.div(
            rx.icon(tag="sparkles", size=13, color=TEAL),
            rx.el.p(
                RawiState.status,
                style={"font_family": FONT_BODY, "font_size": "12px", "color": INK_SOFT, "margin": "0"},
            ),
            style={
                "display": "flex",
                "align_items": "center",
                "gap": "6px",
                "margin_top": "10px",
                "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
            },
        ),
    )


# ---------------------------------------------------------------------------
# Result cards (shown after the demo starts)
# ---------------------------------------------------------------------------


def section_label(icon: str, text, color: str = RUST):
    return rx.el.div(
        rx.icon(tag=icon, size=14, color=color),
        rx.el.span(
            text,
            style={
                "font_family": FONT_BODY,
                "font_size": "11px",
                "font_weight": "700",
                "letter_spacing": "0.8px",
                "text_transform": "uppercase",
                "color": color,
            },
        ),
        style={
            "display": "flex",
            "align_items": "center",
            "gap": "6px",
            "margin_bottom": "8px",
            "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
        },
    )


def site_card():
    return card(
        section_label("map-pin", t("current_site"), TEAL),
        rx.el.p(
            RawiState.current_site,
            style={
                "font_family": FONT_HEADING,
                "font_size": "18px",
                "font_weight": "700",
                "color": INK,
                "margin": "0",
                "text_align": RawiState.text_align,
            },
        ),
        rx.el.p(
            RawiState.geofence_status,
            style={
                "font_family": FONT_BODY,
                "font_size": "12px",
                "color": INK_SOFT,
                "margin": "4px 0 0 0",
                "text_align": RawiState.text_align,
            },
        ),
    )


def story_card():
    return card(
        section_label("volume-2", t("story"), RUST),
        rx.el.p(
            RawiState.answer,
            id="rawi-answer",
            style={
                "font_family": FONT_STORY,
                "font_size": "16px",
                "color": INK,
                "line_height": "1.85",
                "margin": "0",
                "text_align": RawiState.text_align,
                "white_space": "pre-line",
            },
        ),
        rx.el.p(RawiState.language, id="rawi-language", style={"display": "none"}),
        rx.el.div(
            rx.el.button(
                rx.icon(tag="volume-2", size=14, color="white"),
                rx.el.span(
                    t("speak_story"),
                    style={"font_family": FONT_BODY, "font_size": "13px", "font_weight": "600", "color": "white"},
                ),
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
                rx.el.span(
                    t("stop"),
                    style={"font_family": FONT_BODY, "font_size": "13px", "font_weight": "600", "color": RUST},
                ),
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
            style={
                "display": "flex",
                "gap": "10px",
                "margin_top": "14px",
                "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
            },
        ),
        rx.el.p(
            rx.cond(RawiState.is_ar, f"{_STRINGS['source'][1]}: {RawiState.story_source}", f"Source: {RawiState.story_source}"),
            style={
                "font_family": FONT_BODY,
                "font_size": "11px",
                "color": INK_SOFT,
                "margin_top": "10px",
                "text_align": RawiState.text_align,
            },
        ),
    )


def congestion_badge():
    is_high = RawiState.congestion_level == "High"
    is_medium = RawiState.congestion_level == "Medium"
    color = rx.cond(is_high, "#B24A32", rx.cond(is_medium, GOLD, TEAL))
    return rx.el.span(
        RawiState.congestion_level,
        style={
            "font_family": FONT_BODY,
            "font_size": "11px",
            "font_weight": "700",
            "padding": "3px 10px",
            "border_radius": "999px",
            "background": color,
            "color": "white",
        },
    )


_ROUTE_MAP_SCRIPT_TEMPLATE = """
(function() {
  function initMap() {
    if (window.__rawiMapInited) return;
    var el = document.getElementById("rawi-route-map");
    if (!el || typeof L === "undefined") return;
    window.__rawiMapInited = true;

    var main = [__MAIN_LAT__, __MAIN_LON__];
    var alt = [__ALT_LAT__, __ALT_LON__];

    var map = L.map(el, { zoomControl: false }).setView(main, 17);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19 }).addTo(map);

    L.marker(main).addTo(map).bindPopup(__MAIN_LABEL__);
    L.marker(alt).addTo(map).bindPopup(__ALT_LABEL__);
    map.fitBounds(L.latLngBounds([main, alt]), { padding: [24, 24] });

    fetch("https://router.project-osrm.org/route/v1/foot/" + main[1] + "," + main[0] + ";" + alt[1] + "," + alt[0] + "?overview=full&geometries=geojson")
      .then(function(r) { return r.json(); })
      .then(function(data) {
        if (data.routes && data.routes[0]) {
          var coords = data.routes[0].geometry.coordinates.map(function(c) { return [c[1], c[0]]; });
          L.polyline(coords, { color: "__ROUTE_COLOR__", weight: 4, opacity: 0.85 }).addTo(map);
        }
      })
      .catch(function() {});
  }

  if (typeof L !== "undefined") {
    initMap();
    return;
  }
  if (!window.__rawiLeafletLoading) {
    window.__rawiLeafletLoading = true;
    var script = document.createElement("script");
    script.src = "https://unpkg.com/leaflet@1.9.4/dist/leaflet.js";
    script.onload = initMap;
    document.head.appendChild(script);
  } else {
    var tries = 0;
    var interval = setInterval(function() {
      tries += 1;
      if (typeof L !== "undefined") {
        clearInterval(interval);
        initMap();
      } else if (tries > 40) {
        clearInterval(interval);
      }
    }, 250);
  }
})();
"""


def route_map():
    """A small live OpenStreetMap showing the main entrance, the quieter
    alternate entrance, and a walking route between them (via OSRM)."""
    script = (
        _ROUTE_MAP_SCRIPT_TEMPLATE.replace("__MAIN_LAT__", str(AL_HISN_FORT["lat"]))
        .replace("__MAIN_LON__", str(AL_HISN_FORT["lon"]))
        .replace("__ALT_LAT__", str(AL_HISN_FORT_ALT_ENTRANCE["lat"]))
        .replace("__ALT_LON__", str(AL_HISN_FORT_ALT_ENTRANCE["lon"]))
        .replace("__MAIN_LABEL__", json.dumps(AL_HISN_FORT["name"]))
        .replace("__ALT_LABEL__", json.dumps(AL_HISN_FORT_ALT_ENTRANCE["name"]))
        .replace("__ROUTE_COLOR__", RUST)
    )

    return rx.el.div(
        rx.el.div(
            id="rawi-route-map",
            style={
                "width": "100%",
                "height": "180px",
                "border_radius": "14px",
                "overflow": "hidden",
                "margin_top": "12px",
                "background": SAND,
                "border": f"1px solid {LINE}",
            },
        ),
        rx.script(script),
        style={"width": "100%"},
    )


def route_card():
    return card(
        rx.el.div(
            section_label("route", t("route"), TEAL),
            congestion_badge(),
            style={"display": "flex", "align_items": "center", "justify_content": "space-between"},
        ),
        rx.el.p(
            RawiState.route,
            style={
                "font_family": FONT_BODY,
                "font_size": "15px",
                "font_weight": "700",
                "color": INK,
                "margin": "0",
                "text_align": RawiState.text_align,
            },
        ),
        rx.el.p(
            RawiState.route_reason,
            style={
                "font_family": FONT_BODY,
                "font_size": "12px",
                "color": INK_SOFT,
                "margin": "6px 0 0 0",
                "line_height": "1.5",
                "text_align": RawiState.text_align,
            },
        ),
        route_map(),
    )


def network_card():
    return card(
        section_label("gauge", t("network_quality"), RUST),
        rx.el.p(
            rx.cond(
                RawiState.is_ar,
                f"{_STRINGS['qod_line'][1]}: {RawiState.qos_status}",
                f"{_STRINGS['qod_line'][0]}: {RawiState.qos_status}",
            ),
            style={
                "font_family": FONT_BODY,
                "font_size": "15px",
                "font_weight": "700",
                "color": INK,
                "margin": "0",
                "text_align": RawiState.text_align,
            },
        ),
        rx.el.p(
            t("qod_detail"),
            style={
                "font_family": FONT_BODY,
                "font_size": "12px",
                "color": INK_SOFT,
                "margin": "6px 0 0 0",
                "line_height": "1.5",
                "text_align": RawiState.text_align,
            },
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
                rx.el.p(item["step"], style={"font_family": FONT_BODY, "font_size": "13px", "font_weight": "700", "color": INK, "margin": "0"}),
                rx.el.p(item["detail"], style={"font_family": FONT_BODY, "font_size": "12px", "color": INK_SOFT, "margin": "2px 0 0 0"}),
                rx.el.p(
                    item["source"],
                    style={"font_size": "10px", "color": TEAL, "margin": "3px 0 0 0", "font_family": "monospace"},
                ),
                style={"text_align": RawiState.text_align},
            ),
            style={
                "display": "flex",
                "gap": "10px",
                "padding": "8px 0",
                "border_bottom": f"1px solid {LINE}",
                "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
            },
        )

    return card(
        section_label("shield-check", t("camara_proof"), TEAL),
        rx.el.p(
            t("camara_proof_body"),
            style={
                "font_family": FONT_BODY,
                "font_size": "12px",
                "color": INK_SOFT,
                "margin": "0 0 6px 0",
                "line_height": "1.5",
                "text_align": RawiState.text_align,
            },
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
                    t("install_title"),
                    style={"font_family": FONT_BODY, "font_size": "13px", "font_weight": "700", "color": INK, "margin": "0"},
                ),
                rx.el.p(
                    RawiState.pwa_status,
                    style={"font_family": FONT_BODY, "font_size": "11px", "color": INK_SOFT, "margin": "2px 0 0 0"},
                ),
                style={"text_align": RawiState.text_align},
            ),
            style={
                "display": "flex",
                "align_items": "center",
                "gap": "10px",
                "flex": "1",
                "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
            },
        ),
        rx.el.button(
            t("install_button"),
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
                "font_family": FONT_BODY,
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
        style={
            **CARD_STYLE,
            "display": "flex",
            "align_items": "center",
            "justify_content": "space-between",
            "background": TEAL_SOFT,
            "border": f"1px solid {LINE}",
        },
    )
