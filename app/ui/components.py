"""Reusable, styled Reflex UI components for RawiAI."""

import reflex as rx

from app.agents.sites import DEMO_SITES
from app.ui.state import RawiState

_HAS_MULTIPLE_COUNTRIES = len({site["country_code"] for site in DEMO_SITES.values()}) > 1

# ---------------------------------------------------------------------------
# Design tokens
# ---------------------------------------------------------------------------

INK = "#2B1D14"
INK_SOFT = "#614D3C"
SAND = "#F7ECD8"
CARD = "#FFFBF2"
LINE = "#E4D2AC"
LINE_DEEP = "#D3C2AB"
RUST = "#AE5A2E"
RUST_DARK = "#7F3E1E"
RUST_TINT = "rgba(174, 90, 46, 0.11)"
TEAL = "#1F7A72"
TEAL_DEEP = "#0F4A45"
TEAL_SOFT = "rgba(31, 122, 114, 0.12)"
GOLD = "#C08A2E"
GOLD_SOFT = "#EADFC0"

# A per-landmark "sky wave" palette, inspired by editorial flat-illustration
# travel art (wavy horizontal sky bands over warm architecture).
SKY_BLUE = "#7FA6B8"
SKY_ROSE = "#E3A9A0"
SKY_PEACH = "#F5DCC0"
SKY_MINT = "#D8ECE6"

FONT_HEADING = "'Baloo 2', 'Lalezar', 'Tajawal', ui-rounded, sans-serif"
FONT_BODY = "'Inter', 'Tajawal', system-ui, sans-serif"
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

def card(*children, **style):
    merged = {**CARD_STYLE, **style}
    return rx.el.div(*children, style=merged)


# ---------------------------------------------------------------------------
# Localized UI strings
# ---------------------------------------------------------------------------

_STRINGS = {
    "tagline": ("App-Free Telecom-Native Storyteller", "راوي حضاري بلا تطبيقات، عبر شبكتك"),
    "network_ready": ("5G Active", "5G نشطة"),
    "hero_title": ("Let the network\ntell the story.", "دع الشبكة\nترِ الحكاية."),
    "identity": ("Identity", "الهوية"),
    "presence": ("Presence", "الحضور"),
    "network": ("Network", "الشبكة"),
    "qod": ("QoD", "جودة الخدمة"),
    "question_placeholder": ("Ask Rawi about this place...", "اسأل راوي عن هذا المكان..."),
    "begin_story": ("Begin the Story", "ابدأ الحكاية"),
    "listening": ("Listening to the network...", "يستمع إلى الشبكة..."),
    "voice_listening": ("Listening...", "أستمع..."),
    "voice_not_supported": (
        "Voice input isn't supported in this browser.",
        "الإدخال الصوتي غير مدعوم في هذا المتصفح.",
    ),
    "active_location": ("Active Location", "الموقع النشط"),
    "story": ("Story", "الحكاية"),
    "speak_story": ("Speak Story", "اروِ الحكاية"),
    "stop": ("Stop", "إيقاف"),
    "source": ("Source", "المصدر"),
    "route": ("Route", "المسار"),
    "heritage_trail_route": ("Heritage Trail Route", "مسار الرحلة التراثية"),
    "excellent_coverage": ("Excellent Coverage", "تغطية ممتازة"),
    "qod_line": ("Quality on Demand", "جودة الخدمة عند الطلب"),
    "qod_detail": (
        "Requested extra bandwidth priority so narration streams without buffering.",
        "تم طلب أولوية إضافية في النطاق الترددي ليصلك الصوت دون تقطّع.",
    ),
    "ai_systems_verified": ("All Systems Verified", "جميع الأنظمة موثّقة"),
    "verify_banner_sub": ("Presence verified via active telecom node", "تم التحقق من الحضور عبر شبكة اتصالات نشطة"),
    "active_verifications": ("Active Network Handshakes", "المصافحات الشبكية النشطة"),
    "verified_badge": ("Verified", "موثّق"),
    "error_badge": ("Error", "خطأ"),
    "sim_swap_no_swap": ("No recent SIM swap detected", "لم يتم اكتشاف تبديل شريحة مؤخرًا"),
    "sim_swap_swapped": ("Recent SIM swap detected", "تم اكتشاف تبديل شريحة مؤخرًا"),
    "sim_swap_unknown": ("SIM swap status unknown", "حالة تبديل الشريحة غير معروفة"),
    "what_is_camara_title": ("What is CAMARA?", "ما هو CAMARA؟"),
    "what_is_camara_body": (
        "CAMARA is an open standard, built with the GSMA and network operators, that lets apps like RawiAI ask "
        "the mobile network itself to confirm things like presence, identity, and connection quality — "
        "verified signals, not guesses.",
        "CAMARA معيار مفتوح، طُوّر بالتعاون مع GSMA ومشغلي الشبكات، يتيح لتطبيقات مثل راوي أن تسأل الشبكة "
        "نفسها للتحقق من أمور مثل الحضور والهوية وجودة الاتصال - إشارات موثّقة لا تخمينات.",
    ),
    "explore_cities": ("Explore Cities", "استكشف المدن"),
    "your_saved_stories": ("Your Saved Stories", "حكاياتك المحفوظة"),
    "stamps_collected": ("Stamps Collected", "الأختام المجمّعة"),
    "install_title": ("Install RawiAI", "ثبّت راوي"),
    "install_button": ("Install", "تثبيت"),
    "notify_me": ("Alert me on arrival", "نبّهني عند الوصول"),
    "watching": ("Watching for arrival...", "يراقب وصولك..."),
    "tab_explore": ("Explore", "استكشف"),
    "tab_browse": ("Browse", "تصفّح"),
    "tab_favorites": ("Favorites", "المفضلة"),
    "tab_camara": ("CAMARA", "CAMARA"),
    "tab_passport": ("Passport", "الجواز"),
    "no_camara_data": (
        "Run a story from the Explore tab to see its CAMARA verification trail here.",
        "ابدأ حكاية من تبويب استكشف لترى هنا مسار التحقق عبر CAMARA.",
    ),
    "select_country": ("Country", "الدولة"),
    "select_city": ("City", "المدينة"),
    "choose_city_hint": ("Choose a city to see its landmarks.", "اختر مدينة لعرض معالمها."),
    "view_landmark": ("View", "عرض"),
    "no_favorites_yet": (
        "No favorites yet. Browse landmarks and tap the heart to save one.",
        "لا توجد مفضلات بعد. تصفّح المعالم واضغط على القلب لحفظ أحدها.",
    ),
    "recommended_for_you": ("You might also like", "قد يعجبك أيضًا"),
    "passport_title": ("Heritage Passport", "جواز السفر"),
    "passport_hint": (
        "Your official verification of physical presence",
        "توثيقك الرسمي للحضور الفعلي",
    ),
    "locked_label": ("Locked", "مقفل"),
    "available_offline": ("Available offline", "متاح دون اتصال"),
    "read_offline": ("Read Offline", "اقرأ دون اتصال"),
    "offline_notice": (
        "Showing a story saved earlier on this device - no network needed.",
        "تعرض حكاية محفوظة مسبقًا على هذا الجهاز - لا حاجة إلى اتصال بالشبكة.",
    ),
}


def t(key: str):
    en, ar = _STRINGS[key]
    return rx.cond(RawiState.is_ar, ar, en)


def t2(key: str):
    """Both languages together, e.g. 'Explore Cities · المدن' - for section
    titles where showing both reads as a feature, not clutter."""
    en, ar = _STRINGS[key]
    if en == ar:
        return en
    return f"{en} · {ar}"


# ---------------------------------------------------------------------------
# Header / hero
# ---------------------------------------------------------------------------


def network_status_pill():
    return rx.el.div(
        t("network_ready"),
        style={
            "font_family": FONT_BODY,
            "font_size": "11px",
            "font_weight": "700",
            "color": TEAL,
            "white_space": "nowrap",
            "text_transform": "uppercase",
            "padding": "4px 8px",
            "border_radius": "12px",
            "background": TEAL_SOFT,
            "border": f"1px solid {TEAL}",
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


def music_toggle_button():
    """Toggles the ambient background track (see the <audio> element in
    pages.py). Silently does nothing if no audio file has been provided
    yet at /audio/oud-ambient.mp3."""
    playing = RawiState.music_playing
    return rx.el.button(
        rx.image(src="/illustrations/oud.png", width="18px", height="18px", style={"object_fit": "contain"}),
        on_click=RawiState.toggle_music,
        title="Toggle background music",
        style={
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
            "width": "32px",
            "height": "32px",
            "border_radius": "999px",
            "border": f"1px solid {rx.cond(playing, RUST, LINE)}",
            "background": rx.cond(playing, SAND, "transparent"),
            "cursor": "pointer",
            "padding": "0",
            "opacity": rx.cond(playing, "1", "0.6"),
        },
    )


def brand_header():
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                "RawiAI",
                style={
                    "font_family": FONT_HEADING,
                    "font_size": "24px",
                    "font_weight": "800",
                    "color": INK,
                    "margin": "0",
                },
            ),
            rx.el.p(
                "راوي",
                dir="rtl",
                style={
                    "font_family": FONT_HEADING,
                    "font_size": "12px",
                    "font_weight": "700",
                    "color": RUST,
                    "margin": "0",
                    "text_transform": "uppercase",
                },
            ),
            style={"display": "flex", "flex_direction": "column", "gap": "2px"},
        ),
        rx.el.div(
            network_status_pill(),
            music_toggle_button(),
            language_toggle(),
            style={"display": "flex", "align_items": "center", "gap": "8px"},
        ),
        style={
            "display": "flex",
            "align_items": "center",
            "justify_content": "space-between",
            "width": "100%",
        },
    )


def hero():
    heading = _STRINGS["hero_title"][0].replace("\n", " ")
    heading_ar = _STRINGS["hero_title"][1].replace("\n", " ")
    return rx.el.div(
        rx.el.p(
            heading,
            dir="ltr",
            style={
                "font_family": FONT_HEADING,
                "font_size": "16px",
                "font_weight": "700",
                "color": RUST,
                "margin": "0",
                "text_align": "left",
            },
        ),
        rx.el.p(
            heading_ar,
            dir="rtl",
            style={
                "font_family": FONT_BODY,
                "font_size": "14px",
                "font_weight": "600",
                "color": INK,
                "margin": "0",
                "text_align": "right",
            },
        ),
        style={
            "display": "flex",
            "flex_direction": "column",
            "gap": "6px",
            "width": "100%",
            "background": CARD,
            "border": f"1px solid {LINE}",
            "border_radius": "16px",
            "padding": "18px",
            "box_sizing": "border-box",
        },
    )


# ---------------------------------------------------------------------------
# Tab navigation — Explore / Browse / Favorites
# ---------------------------------------------------------------------------


def tab_bar():
    def tab_button(key: str, icon: str, label_key: str):
        is_active = RawiState.active_tab == key
        return rx.el.button(
            rx.el.div(
                rx.icon(tag=icon, size=16, color=rx.cond(is_active, "white", INK_SOFT)),
                style={
                    "width": "30px",
                    "height": "30px",
                    "border_radius": "10px",
                    "display": "flex",
                    "align_items": "center",
                    "justify_content": "center",
                    "background": rx.cond(is_active, TEAL, "transparent"),
                    "transition": "all 0.15s ease",
                },
            ),
            rx.el.span(
                t(label_key),
                style={
                    "font_family": FONT_BODY,
                    "font_size": "10px",
                    "font_weight": "600",
                    "color": rx.cond(is_active, TEAL, INK_SOFT),
                },
            ),
            on_click=RawiState.set_active_tab(key),
            style={
                "display": "flex",
                "flex_direction": "column",
                "align_items": "center",
                "gap": "3px",
                "flex": "1",
                "padding": "4px 2px 0 2px",
                "border": "none",
                "cursor": "pointer",
                "background": "transparent",
            },
        )

    return rx.el.div(
        tab_button("explore", "compass", "tab_explore"),
        tab_button("browse", "map", "tab_browse"),
        tab_button("favorites", "heart", "tab_favorites"),
        tab_button("passport", "award", "tab_passport"),
        tab_button("camara", "shield-check", "tab_camara"),
        style={
            "display": "flex",
            "width": "100%",
            "border_top": f"1px solid {LINE}",
            "padding": "8px 4px 2px 4px",
        },
    )


def location_preview_card():
    """The mockup's persistent "Active Location" section - visible before
    the story even starts, using only real static content (the site's
    hand-drawn illustration, name, and a one-line teaser condensed from the
    site's actual narration text) plus honest status copy: the real CAMARA
    geofence result once the story has actually started, instead of a
    fabricated distance badge."""
    return rx.el.div(
        screen_title("active_location"),
        rx.el.div(
            rx.el.div(site_illustration(), style={"width": "100%", "height": "160px", "overflow": "hidden"}),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        RawiState.selected_site_name,
                        style={
                            "font_family": FONT_HEADING,
                            "font_size": "18px",
                            "font_weight": "700",
                            "color": INK,
                            "margin": "0",
                        },
                    ),
                    rx.cond(
                        RawiState.started,
                        rx.el.span(
                            t("verified_badge"),
                            style={
                                "font_family": FONT_BODY,
                                "font_size": "11px",
                                "font_weight": "700",
                                "color": TEAL,
                                "background": TEAL_SOFT,
                                "padding": "4px 8px",
                                "border_radius": "8px",
                                "white_space": "nowrap",
                            },
                        ),
                    ),
                    style={
                        "display": "flex",
                        "align_items": "center",
                        "justify_content": "space-between",
                        "gap": "8px",
                        "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
                    },
                ),
                rx.el.p(
                    RawiState.selected_site_teaser,
                    style={
                        "font_family": FONT_BODY,
                        "font_size": "13px",
                        "color": INK_SOFT,
                        "margin": "0",
                        "line_height": "1.4",
                        "text_align": RawiState.text_align,
                    },
                ),
                style={"padding": "16px", "display": "flex", "flex_direction": "column", "gap": "10px"},
            ),
            style={
                "background": CARD,
                "border": f"1px solid {LINE}",
                "border_radius": "16px",
                "overflow": "hidden",
                "width": "100%",
            },
        ),
        style={"display": "flex", "flex_direction": "column", "gap": "10px", "width": "100%"},
    )


# ---------------------------------------------------------------------------
# Trust rail — the four CAMARA signals checked before the story begins
# ---------------------------------------------------------------------------


def trust_chip(label, active):
    return rx.el.div(
        rx.el.span(label, style={"font_family": FONT_BODY, "font_size": "11px", "font_weight": "700"}),
        rx.cond(active, rx.icon(tag="check", size=11, color="white")),
        style={
            "display": "flex",
            "align_items": "center",
            "gap": "4px",
            "padding": "6px 10px",
            "border_radius": "10px",
            "background": rx.cond(active, TEAL, LINE),
            "color": rx.cond(active, "white", INK_SOFT),
            "transition": "all 0.2s ease",
            "flex": "1",
            "justify_content": "center",
        },
    )


def trust_rail():
    return rx.el.div(
        trust_chip(t("identity"), RawiState.step_identity),
        trust_chip(t("presence"), RawiState.step_presence),
        trust_chip(t("network"), RawiState.step_network),
        trust_chip(t("qod"), RawiState.step_qos),
        style={"display": "flex", "gap": "6px", "width": "100%", "flex_wrap": "wrap"},
    )


# ---------------------------------------------------------------------------
# Arrival alert — client-side geolocation watch that pops a native
# notification when the visitor's phone GPS enters the site radius. This is
# the on-device complement to the network-side CAMARA geofencing: CAMARA
# proves presence to the backend, this gives the visitor an immediate nudge.
# ---------------------------------------------------------------------------

# Reads the target site's lat/lon/radius/name from the hidden elements
# below at the moment the watch starts, rather than baking one site's
# coordinates in at compile time - so switching landmarks in Browse
# automatically re-targets the arrival alert too.
_ARRIVAL_WATCH_SCRIPT = """
(function() {
  function haversineMeters(lat1, lon1, lat2, lon2) {
    var R = 6371000;
    var toRad = function(d) { return (d * Math.PI) / 180; };
    var dLat = toRad(lat2 - lat1);
    var dLon = toRad(lon2 - lon1);
    var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
      Math.sin(dLon / 2) * Math.sin(dLon / 2);
    return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  }

  function readTarget() {
    var byId = function(id, fallback) {
      var el = document.getElementById(id);
      return el ? el.innerText : fallback;
    };
    return {
      lat: parseFloat(byId("rawi-site-lat", "0")),
      lon: parseFloat(byId("rawi-site-lon", "0")),
      radius: parseFloat(byId("rawi-site-radius", "150")),
      name: byId("rawi-site-name", "this site"),
    };
  }

  function notifyArrival(name) {
    var title = "Rawi AI";
    var body = "You've arrived at " + name + " — tap to hear its story.";
    if (window.Notification && Notification.permission === "granted") {
      var n = new Notification(title, { body: body, icon: "/rawiai-icon.svg" });
      n.onclick = function() {
        window.focus();
        n.close();
      };
    } else {
      alert(title + ": " + body);
    }
  }

  window.rawiStopArrivalWatch = function() {
    if (window.__rawiWatchId != null && navigator.geolocation) {
      navigator.geolocation.clearWatch(window.__rawiWatchId);
      window.__rawiWatchId = null;
    }
  };

  window.rawiStartArrivalWatch = function() {
    if (!("geolocation" in navigator)) {
      alert("Geolocation is not available on this device or browser.");
      return;
    }

    var begin = function() {
      var target = readTarget();
      window.__rawiArrivalFired = false;
      window.__rawiWatchId = navigator.geolocation.watchPosition(
        function(pos) {
          var distance = haversineMeters(
            pos.coords.latitude,
            pos.coords.longitude,
            target.lat,
            target.lon
          );
          if (distance <= target.radius && !window.__rawiArrivalFired) {
            window.__rawiArrivalFired = true;
            notifyArrival(target.name);
          }
        },
        function(err) {
          console.log("RawiAI geolocation error:", err);
        },
        { enableHighAccuracy: true, maximumAge: 5000, timeout: 15000 }
      );
    };

    if (window.Notification && Notification.permission !== "granted" && Notification.permission !== "denied") {
      Notification.requestPermission().then(begin);
    } else {
      begin();
    }
  };
})();
"""


def arrival_watch_script():
    return rx.script(_ARRIVAL_WATCH_SCRIPT)


def arrival_alert_button():
    active = RawiState.arrival_watch_enabled
    return rx.el.div(
        rx.el.button(
            rx.icon(tag=rx.cond(active, "bell-ring", "bell"), size=14, color=rx.cond(active, "white", TEAL)),
            rx.el.span(
                rx.cond(active, t("watching"), t("notify_me")),
                style={"font_family": FONT_BODY, "font_size": "12px", "font_weight": "600"},
            ),
            on_click=RawiState.toggle_arrival_watch,
            style={
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
                "gap": "6px",
                "width": "100%",
                "padding": "10px",
                "border_radius": "12px",
                "border": f"1px solid {rx.cond(active, TEAL, LINE)}",
                "background": rx.cond(active, TEAL, SAND),
                "color": rx.cond(active, "white", TEAL),
                "cursor": "pointer",
                "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
            },
        ),
        # Hidden bridge elements: the arrival-watch script reads these at
        # click-time so it always targets whichever landmark is selected.
        rx.el.span(RawiState.selected_site_lat, id="rawi-site-lat", style={"display": "none"}),
        rx.el.span(RawiState.selected_site_lon, id="rawi-site-lon", style={"display": "none"}),
        rx.el.span(RawiState.selected_site_radius, id="rawi-site-radius", style={"display": "none"}),
        rx.el.span(RawiState.selected_site_name, id="rawi-site-name", style={"display": "none"}),
        style={"width": "100%", "margin_top": "10px"},
    )


# ---------------------------------------------------------------------------
# Voice input - speak the question instead of typing it
# ---------------------------------------------------------------------------


def voice_input_button():
    active = RawiState.is_listening
    return rx.el.button(
        rx.icon(tag="mic", size=18, color="white"),
        on_click=RawiState.start_voice_input,
        disabled=active,
        style={
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
            "width": "42px",
            "height": "42px",
            "flex_shrink": "0",
            "border": "none",
            "border_radius": "14px",
            "background": RUST,
            "cursor": "pointer",
            "animation": rx.cond(active, "pulse 1.2s ease-in-out infinite", "none"),
        },
    )


# ---------------------------------------------------------------------------
# Ask card
# ---------------------------------------------------------------------------


def ask_card():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(tag="search", size=15, color=INK_SOFT, style={"flex_shrink": "0"}),
                rx.el.input(
                    value=RawiState.question,
                    on_change=RawiState.set_question,
                    placeholder=t("question_placeholder"),
                    dir=RawiState.dir,
                    style={
                        "font_family": FONT_BODY,
                        "flex": "1",
                        "min_width": "0",
                        "border": "none",
                        "background": "transparent",
                        "font_size": "14px",
                        "color": INK,
                        "outline": "none",
                        "text_align": RawiState.text_align,
                    },
                ),
                rx.el.span(RawiState.language, id="rawi-language", style={"display": "none"}),
                style={
                    "display": "flex",
                    "align_items": "center",
                    "gap": "10px",
                    "flex": "1",
                    "min_width": "0",
                    "padding": "12px",
                    "border_radius": "14px",
                    "border": f"1px solid {LINE}",
                    "background": CARD,
                    "box_sizing": "border-box",
                    "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
                },
            ),
            voice_input_button(),
            style={
                "display": "flex",
                "align_items": "center",
                "gap": "8px",
                "width": "100%",
                "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
            },
        ),
        rx.el.button(
            rx.cond(RawiState.is_loading, t("listening"), t2("begin_story")),
            on_click=RawiState.start_demo,
            disabled=RawiState.is_loading,
            style={
                "font_family": FONT_BODY,
                "width": "100%",
                "padding": "16px",
                "border": "none",
                "border_radius": "14px",
                "background": RUST,
                "color": "white",
                "font_size": "16px",
                "font_weight": "700",
                "cursor": rx.cond(RawiState.is_loading, "default", "pointer"),
                "opacity": rx.cond(RawiState.is_loading, "0.75", "1"),
                "box_shadow": "0 4px 4px rgba(174, 90, 46, 0.2)",
                "animation": rx.cond(
                    RawiState.is_loading | RawiState.started,
                    "none",
                    "rawiPulse 2.5s ease-in-out infinite",
                ),
            },
        ),
        rx.cond(
            RawiState.started,
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
                    "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
                },
            ),
        ),
        style={"display": "flex", "flex_direction": "column", "gap": "10px", "width": "100%"},
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


def offline_notice():
    return rx.el.div(
        rx.icon(tag="download", size=14, color=TEAL_DEEP),
        rx.el.span(
            t("offline_notice"),
            style={"font_family": FONT_BODY, "font_size": "12px", "font_weight": "600", "color": TEAL_DEEP},
        ),
        style={
            "display": "flex",
            "align_items": "center",
            "gap": "8px",
            "padding": "10px 14px",
            "border_radius": "12px",
            "background": TEAL_SOFT,
            "border": f"1px solid {LINE}",
            "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
        },
    )




# ---------------------------------------------------------------------------
# Landmark illustrations - flat-style banner art per site, in the same
# geometric language as the lantern mark and skyline bar. Reuses the
# already-verified dome path from the skyline (translate/scale only, no new
# arc math) to stay low-risk.
# ---------------------------------------------------------------------------

_ILLUSTRATION_VIEWBOX = "0 0 320 150"
_DOME_PATH = "M12 48 L12 30 A23 23 0 0 1 58 30 L58 48 Z"


def _wave(y: int, amplitude: int, color: str, opacity: float = 0.85, width: int = 9):
    """A thick, rounded wavy stroke spanning the canvas width - a smooth
    continuous S-curve built from one quadratic segment (Q) plus repeated
    smooth continuations (T), the standard reliable SVG sine-wave recipe."""
    d = f"M-20 {y} Q20 {y - amplitude} 60 {y} T140 {y} T220 {y} T300 {y} T380 {y}"
    return rx.el.path(d=d, stroke=color, stroke_width=str(width), fill="none", opacity=str(opacity), stroke_linecap="round")


def _illustration_frame(sky_bg: str, waves: list, *children):
    return rx.el.svg(
        rx.el.rect(x="0", y="0", width="320", height="150", fill=sky_bg),
        *waves,
        rx.el.line(x1="0", y1="130", x2="320", y2="130", stroke=LINE, stroke_width="2"),
        *children,
        view_box=_ILLUSTRATION_VIEWBOX,
        width="100%",
        height="150",
        style={"display": "block"},
    )


def al_hisn_fort_illustration():
    merlon_x = [112, 132, 152, 172, 192]
    merlons = [
        rx.el.rect(x=str(x), y="40", width="12", height="10", fill=RUST)
        for x in merlon_x
    ]
    return _illustration_frame(
        SKY_MINT,
        [_wave(18, 6, SKY_BLUE), _wave(30, 5, SKY_ROSE, opacity=0.7), _wave(42, 4, SKY_BLUE, opacity=0.5)],
        rx.el.rect(x="40", y="90", width="60", height="40", fill=RUST_DARK, opacity="0.75"),
        rx.el.rect(x="220", y="90", width="60", height="40", fill=RUST_DARK, opacity="0.75"),
        rx.el.rect(x="110", y="50", width="100", height="80", fill=RUST),
        *merlons,
        rx.el.rect(x="150", y="100", width="20", height="30", fill=INK),
        rx.el.line(x1="160", y1="40", x2="160", y2="15", stroke=INK, stroke_width="2"),
        rx.el.polygon(points="160,15 178,22 160,29", fill=GOLD),
        rx.el.line(x1="30", y1="130", x2="30", y2="95", stroke=INK, stroke_width="4"),
        rx.el.line(x1="30", y1="95", x2="15", y2="80", stroke=INK, stroke_width="3"),
        rx.el.line(x1="30", y1="95", x2="22", y2="78", stroke=INK, stroke_width="3"),
        rx.el.line(x1="30", y1="95", x2="38", y2="78", stroke=INK, stroke_width="3"),
        rx.el.line(x1="30", y1="95", x2="45", y2="80", stroke=INK, stroke_width="3"),
    )


def qasr_al_hosn_illustration():
    def dome_group(translate_x, translate_y, scale):
        return rx.el.g(
            rx.el.path(d=_DOME_PATH, fill=RUST),
            rx.el.rect(x="32", y="2", width="6", height="8", fill=RUST),
            rx.el.circle(cx="35", cy="2", r="2", fill=RUST),
            transform=f"translate({translate_x},{translate_y}) scale({scale})",
        )

    return _illustration_frame(
        SKY_PEACH,
        [_wave(16, 5, GOLD, opacity=0.6), _wave(26, 6, SKY_ROSE), _wave(38, 4, GOLD, opacity=0.45)],
        rx.el.rect(x="60", y="90", width="35", height="40", fill=RUST_DARK, opacity="0.75"),
        rx.el.rect(x="225", y="90", width="35", height="40", fill=RUST_DARK, opacity="0.75"),
        rx.el.rect(x="100", y="70", width="120", height="60", fill=RUST),
        dome_group(42.5, 42, 1),
        dome_group(207.5, 42, 1),
        dome_group(90, 10, 2),
    )


def al_fahidi_illustration():
    return _illustration_frame(
        SKY_MINT,
        [_wave(16, 5, TEAL, opacity=0.55), _wave(28, 6, SKY_BLUE), _wave(40, 4, TEAL, opacity=0.4)],
        rx.el.rect(x="60", y="90", width="70", height="40", fill=RUST_DARK, opacity="0.75"),
        rx.el.rect(x="85", y="30", width="20", height="60", fill=RUST_DARK),
        rx.el.line(x1="90", y1="35", x2="90", y2="85", stroke=GOLD_SOFT, stroke_width="2"),
        rx.el.line(x1="97", y1="35", x2="97", y2="85", stroke=GOLD_SOFT, stroke_width="2"),
        rx.el.line(x1="104", y1="35", x2="104", y2="85", stroke=GOLD_SOFT, stroke_width="2"),
        rx.el.rect(x="180", y="95", width="65", height="35", fill=RUST_DARK, opacity="0.75"),
        rx.el.rect(x="200", y="35", width="18", height="60", fill=RUST_DARK),
        rx.el.line(x1="204", y1="40", x2="204", y2="90", stroke=GOLD_SOFT, stroke_width="2"),
        rx.el.line(x1="210", y1="40", x2="210", y2="90", stroke=GOLD_SOFT, stroke_width="2"),
        rx.el.line(x1="216", y1="40", x2="216", y2="90", stroke=GOLD_SOFT, stroke_width="2"),
    )


def petra_illustration():
    return _illustration_frame(
        SKY_ROSE,
        [_wave(16, 5, GOLD, opacity=0.5), _wave(28, 6, SKY_PEACH, opacity=0.6), _wave(40, 4, GOLD, opacity=0.35)],
        rx.el.polygon(points="0,130 0,20 45,50 45,130", fill=RUST_DARK, opacity="0.85"),
        rx.el.polygon(points="320,130 320,20 275,50 275,130", fill=RUST_DARK, opacity="0.85"),
        rx.el.rect(x="130", y="70", width="60", height="60", fill=RUST),
        rx.el.rect(x="140", y="55", width="8", height="15", fill=RUST),
        rx.el.rect(x="172", y="55", width="8", height="15", fill=RUST),
        rx.el.polygon(points="130,55 190,55 160,35", fill=RUST),
        rx.el.circle(cx="160", cy="28", r="6", fill=GOLD),
        rx.el.rect(x="152", y="100", width="16", height="30", fill=INK),
    )


def hegra_illustration():
    return _illustration_frame(
        SKY_PEACH,
        [_wave(16, 5, GOLD, opacity=0.55), _wave(28, 6, SKY_ROSE, opacity=0.5), _wave(40, 4, GOLD, opacity=0.35)],
        rx.el.path(d="M0 130 Q40 105 90 130 T180 130 T270 130 T320 130 Z", fill=SKY_ROSE, opacity="0.5"),
        rx.el.rect(x="115", y="60", width="90", height="70", fill=RUST),
        rx.el.rect(x="120", y="50", width="14", height="10", fill=RUST),
        rx.el.rect(x="139", y="44", width="14", height="16", fill=RUST),
        rx.el.rect(x="167", y="44", width="14", height="16", fill=RUST),
        rx.el.rect(x="186", y="50", width="14", height="10", fill=RUST),
        rx.el.rect(x="152", y="100", width="20", height="30", fill=INK),
    )


def al_zubarah_illustration():
    return _illustration_frame(
        SKY_BLUE,
        [_wave(16, 5, SKY_MINT, opacity=0.6), _wave(28, 6, GOLD, opacity=0.3), _wave(40, 4, SKY_MINT, opacity=0.4)],
        rx.el.rect(x="30", y="95", width="50", height="35", fill=RUST_DARK, opacity="0.8"),
        rx.el.rect(x="90", y="100", width="60", height="30", fill=RUST_DARK, opacity="0.75"),
        rx.el.rect(x="230", y="98", width="55", height="32", fill=RUST_DARK, opacity="0.75"),
        rx.el.rect(x="0", y="112", width="320", height="8", fill=RUST_DARK, opacity="0.6"),
        rx.el.rect(x="150", y="60", width="26", height="60", fill=RUST),
        rx.el.rect(x="150", y="52", width="6", height="8", fill=RUST),
        rx.el.rect(x="162", y="52", width="6", height="8", fill=RUST),
        rx.el.rect(x="170", y="52", width="6", height="8", fill=RUST),
        rx.el.line(x1="250", y1="90", x2="250", y2="120", stroke=INK, stroke_width="2"),
        rx.el.polygon(points="250,90 250,118 274,118", fill=INK, opacity="0.6"),
    )


def site_illustration():
    return landmark_thumbnail(RawiState.selected_site_id)


def landmark_thumbnail(site_id):
    """Same illustration set as site_illustration(), but keyed off any
    site_id Var (e.g. a landmark_card row) rather than the globally
    selected site - used for Browse/Favorites photo-style cards."""
    return rx.match(
        site_id,
        ("qasr-al-hosn", qasr_al_hosn_illustration()),
        ("al-fahidi", al_fahidi_illustration()),
        ("petra", petra_illustration()),
        ("hegra", hegra_illustration()),
        ("al-zubarah", al_zubarah_illustration()),
        al_hisn_fort_illustration(),
    )


# ---------------------------------------------------------------------------
# Story pagination - "visual book" pages with a dot indicator
# ---------------------------------------------------------------------------


def story_page_dot(index):
    is_active = index == RawiState.story_page_index
    return rx.el.div(
        style={
            "width": rx.cond(is_active, "18px", "6px"),
            "height": "6px",
            "border_radius": "999px",
            "background": rx.cond(is_active, RUST, LINE),
            "transition": "all 0.2s ease",
        }
    )


def story_pager():
    return rx.el.div(
        rx.el.button(
            rx.icon(tag="chevron-left", size=16, color=rx.cond(RawiState.story_page_index == 0, LINE, RUST)),
            on_click=RawiState.prev_story_page,
            disabled=RawiState.story_page_index == 0,
            style={"border": "none", "background": "transparent", "cursor": "pointer", "padding": "4px"},
        ),
        rx.el.div(
            rx.foreach(RawiState.story_page_dots, story_page_dot),
            style={"display": "flex", "align_items": "center", "gap": "5px"},
        ),
        rx.el.button(
            rx.icon(
                tag="chevron-right",
                size=16,
                color=rx.cond(RawiState.story_page_index >= RawiState.story_page_count - 1, LINE, RUST),
            ),
            on_click=RawiState.next_story_page,
            disabled=RawiState.story_page_index >= RawiState.story_page_count - 1,
            style={"border": "none", "background": "transparent", "cursor": "pointer", "padding": "4px"},
        ),
        style={
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
            "gap": "10px",
            "margin_top": "12px",
            "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
        },
    )


def story_card():
    return card(
        section_label("volume-2", t("story"), RUST),
        rx.el.p(
            RawiState.current_story_page,
            style={
                "font_family": FONT_STORY,
                "font_size": "16px",
                "color": INK,
                "line_height": "1.85",
                "margin": "0",
                "text_align": RawiState.text_align,
                "white_space": "pre-line",
                "min_height": "90px",
            },
        ),
        rx.cond(RawiState.story_page_count > 1, story_pager()),
        rx.el.p(RawiState.answer, id="rawi-answer", style={"display": "none"}),
        rx.el.audio(src=RawiState.audio_data_url, id="rawi-tts-audio", style={"display": "none"}),
        rx.el.div(
            rx.el.button(
                rx.icon(tag="volume-2", size=14, color="white"),
                rx.el.span(
                    t("speak_story"),
                    style={"font_family": FONT_BODY, "font_size": "13px", "font_weight": "600", "color": "white"},
                ),
                on_click=rx.call_script(
                    """
const audioEl = document.getElementById("rawi-tts-audio");
if (audioEl && audioEl.getAttribute("src")) {
  audioEl.currentTime = 0;
  audioEl.play();
} else {
  const text = document.getElementById("rawi-answer")?.innerText || "";
  const language = document.getElementById("rawi-language")?.innerText || "en";
  if (text.trim()) {
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = language === "ar" ? "ar-SA" : "en-US";
    window.speechSynthesis.speak(utterance);
  }
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
                on_click=rx.call_script(
                    """
window.speechSynthesis.cancel();
const audioEl = document.getElementById("rawi-tts-audio");
if (audioEl) audioEl.pause();
"""
                ),
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


# Reads the main/alt points from the hidden bridge elements below at mount
# time, so the same script works for whichever landmark is selected. Uses
# el._leaflet_id (set internally by Leaflet) rather than a global flag to
# decide whether to init, since the container div remounts fresh - with a
# new key() - each time the selected site changes.
_ROUTE_MAP_SCRIPT = """
(function() {
  function readPoint(latId, lonId, nameId) {
    var byId = function(id) {
      var el = document.getElementById(id);
      return el ? el.innerText : "";
    };
    return {
      lat: parseFloat(byId(latId)),
      lon: parseFloat(byId(lonId)),
      name: byId(nameId),
    };
  }

  function initMap() {
    var el = document.getElementById("rawi-route-map");
    if (!el || typeof L === "undefined" || el._leaflet_id) return;

    var main = readPoint("rawi-site-lat", "rawi-site-lon", "rawi-site-name");
    var alt = readPoint("rawi-alt-lat", "rawi-alt-lon", "rawi-alt-name");
    var mainPos = [main.lat, main.lon];
    var altPos = [alt.lat, alt.lon];

    var map = L.map(el, { zoomControl: false }).setView(mainPos, 16);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19 }).addTo(map);

    L.marker(mainPos).addTo(map).bindPopup(main.name);
    L.marker(altPos).addTo(map).bindPopup(alt.name);
    map.fitBounds(L.latLngBounds([mainPos, altPos]), { padding: [24, 24] });

    fetch("https://router.project-osrm.org/route/v1/foot/" + mainPos[1] + "," + mainPos[0] + ";" + altPos[1] + "," + altPos[0] + "?overview=full&geometries=geojson")
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
    """A small live OpenStreetMap showing the main entrance, a quieter
    alternate path, and a walking route between them (via OSRM) - for
    whichever landmark is currently selected."""
    script = _ROUTE_MAP_SCRIPT.replace("__ROUTE_COLOR__", RUST)

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
        rx.el.span(RawiState.selected_alt_lat, id="rawi-alt-lat", style={"display": "none"}),
        rx.el.span(RawiState.selected_alt_lon, id="rawi-alt-lon", style={"display": "none"}),
        rx.el.span(RawiState.selected_alt_name, id="rawi-alt-name", style={"display": "none"}),
        rx.script(script),
        # Force a full remount when the selected landmark changes, so the
        # map re-reads fresh coordinates instead of keeping the old view.
        key=RawiState.selected_site_id,
        style={"width": "100%"},
    )


def route_card():
    return card(
        rx.el.div(
            section_label("route", t("heritage_trail_route"), TEAL),
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
        section_label("wifi", t("excellent_coverage"), RUST),
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


def verified_badge(verified):
    return rx.el.span(
        rx.cond(verified, t("verified_badge"), t("error_badge")),
        style={
            "font_family": FONT_BODY,
            "font_size": "11px",
            "font_weight": "600",
            "color": rx.cond(verified, TEAL, RUST),
            "background": rx.cond(verified, TEAL_SOFT, RUST_TINT),
            "padding": "4px 8px",
            "border_radius": "6px",
            "flex_shrink": "0",
            "white_space": "nowrap",
        },
    )


def timeline_card():
    def row(item):
        verified = item["verified"] == "true"
        return rx.el.div(
            rx.el.div(
                rx.el.div(style={"width": "12px", "height": "12px", "border_radius": "50%", "background": RUST, "flex_shrink": "0"}),
                rx.cond(
                    item["is_last"] != "true",
                    rx.el.div(style={"width": "2px", "flex": "1", "background": LINE, "min_height": "70px"}),
                ),
                style={"width": "24px", "flex_shrink": "0", "display": "flex", "flex_direction": "column", "align_items": "center"},
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(item["step"], style={"font_family": FONT_HEADING, "font_weight": "700", "font_size": "15px", "color": INK, "margin": "0"}),
                    verified_badge(verified),
                    style={
                        "display": "flex",
                        "align_items": "center",
                        "justify_content": "space-between",
                        "gap": "8px",
                        "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
                    },
                ),
                rx.el.p(item["api_label"], style={"font_family": FONT_BODY, "font_weight": "700", "font_size": "11px", "color": GOLD, "margin": "0"}),
                rx.el.p(item["detail"], style={"font_family": FONT_BODY, "font_size": "13px", "color": INK_SOFT, "line_height": "1.4", "margin": "0"}),
                style={
                    "flex": "1",
                    "min_width": "0",
                    "padding_bottom": "20px",
                    "display": "flex",
                    "flex_direction": "column",
                    "gap": "4px",
                    "text_align": RawiState.text_align,
                },
            ),
            style={"display": "flex", "gap": "12px", "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row")},
        )

    return rx.el.div(
        screen_title("active_verifications"),
        rx.el.div(rx.foreach(RawiState.timeline, row), style={"width": "100%"}),
        style={"display": "flex", "flex_direction": "column", "gap": "8px", "width": "100%"},
    )


def what_is_camara_card():
    return rx.el.div(
        rx.el.div(
            rx.icon(tag="circle-alert", size=18, color=RUST),
            rx.el.p(
                t("what_is_camara_title"),
                style={"font_family": FONT_HEADING, "font_size": "15px", "font_weight": "700", "color": INK, "margin": "0"},
            ),
            style={
                "display": "flex",
                "align_items": "center",
                "gap": "8px",
                "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
            },
        ),
        rx.el.p(
            t("what_is_camara_body"),
            style={
                "font_family": FONT_BODY,
                "font_size": "13px",
                "color": INK_SOFT,
                "margin": "0",
                "line_height": "1.4",
                "text_align": RawiState.text_align,
            },
        ),
        style={
            "display": "flex",
            "flex_direction": "column",
            "gap": "10px",
            "width": "100%",
            "background": CARD,
            "border": f"1px solid {LINE}",
            "border_radius": "16px",
            "padding": "16px",
            "box_sizing": "border-box",
        },
    )


def all_systems_banner():
    return rx.el.div(
        rx.el.div(
            rx.icon(tag="shield-check", size=20, color=TEAL),
            style={
                "width": "44px",
                "height": "44px",
                "border_radius": "22px",
                "background": "white",
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
                "flex_shrink": "0",
            },
        ),
        rx.el.div(
            rx.el.p(
                t("ai_systems_verified"),
                style={"font_family": FONT_HEADING, "font_size": "16px", "font_weight": "700", "color": "white", "margin": "0"},
            ),
            rx.el.p(
                t("verify_banner_sub"),
                style={"font_family": FONT_BODY, "font_size": "12px", "color": "white", "opacity": "0.8", "margin": "0"},
            ),
            style={"display": "flex", "flex_direction": "column", "gap": "2px", "min_width": "0"},
        ),
        style={
            "display": "flex",
            "align_items": "center",
            "gap": "12px",
            "width": "100%",
            "padding": "16px",
            "border_radius": "16px",
            "background": TEAL,
            "box_sizing": "border-box",
            "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
        },
    )


def camara_tab():
    return rx.el.div(
        all_systems_banner(),
        rx.cond(
            RawiState.timeline.length() > 0,
            timeline_card(),
            rx.el.p(
                t("no_camara_data"),
                style={
                    "font_family": FONT_BODY,
                    "font_size": "13px",
                    "color": INK_SOFT,
                    "text_align": "center",
                    "padding": "24px 8px",
                },
            ),
        ),
        what_is_camara_card(),
        style={"display": "flex", "flex_direction": "column", "gap": "16px", "width": "100%"},
    )


# ---------------------------------------------------------------------------
# Browse tab — country -> city -> landmark
# ---------------------------------------------------------------------------


def pill_row(items, selected_code, on_select):
    def pill(item):
        is_active = selected_code == item["code"]
        return rx.el.button(
            item["label"],
            on_click=on_select(item["code"]),
            style={
                "font_family": FONT_BODY,
                "padding": "8px 16px",
                "font_size": "13px",
                "font_weight": "600",
                "border_radius": "999px",
                "border": f"1px solid {rx.cond(is_active, TEAL, LINE)}",
                "cursor": "pointer",
                "background": rx.cond(is_active, TEAL, "white"),
                "color": rx.cond(is_active, "white", INK),
            },
        )

    return rx.el.div(
        rx.foreach(items, pill),
        style={"display": "flex", "flex_wrap": "wrap", "gap": "8px"},
    )


def favorite_heart_button(site_id, is_favorite):
    active = is_favorite == "true"
    return rx.el.button(
        rx.icon(tag="heart", size=16, color=rx.cond(active, RUST, INK_SOFT)),
        on_click=RawiState.toggle_favorite(site_id),
        style={
            "border": "none",
            "background": "transparent",
            "cursor": "pointer",
            "padding": "4px",
            "flex_shrink": "0",
        },
    )


def landmark_card(item):
    is_offline = item["has_offline"] == "true"
    return card(
        rx.el.div(
            landmark_thumbnail(item["id"]),
            style={"border_radius": "12px", "overflow": "hidden", "margin_bottom": "12px", "border": f"1px solid {LINE}"},
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    item["name"],
                    style={"font_family": FONT_HEADING, "font_size": "15px", "font_weight": "700", "color": INK, "margin": "0"},
                ),
                rx.el.p(
                    item["city"],
                    style={"font_family": FONT_BODY, "font_size": "12px", "color": INK_SOFT, "margin": "2px 0 0 0"},
                ),
                rx.cond(
                    is_offline,
                    rx.el.div(
                        rx.icon(tag="download", size=11, color=TEAL),
                        rx.el.span(
                            t("available_offline"),
                            style={"font_family": FONT_BODY, "font_size": "10px", "font_weight": "700", "color": TEAL},
                        ),
                        style={"display": "flex", "align_items": "center", "gap": "4px", "margin_top": "4px"},
                    ),
                ),
                style={"text_align": RawiState.text_align},
            ),
            favorite_heart_button(item["id"], item["is_favorite"]),
            style={
                "display": "flex",
                "align_items": "center",
                "justify_content": "space-between",
                "flex_direction": rx.cond(RawiState.is_ar, "row-reverse", "row"),
            },
        ),
        rx.el.div(
            rx.el.button(
                t("view_landmark"),
                on_click=RawiState.select_landmark(item["id"]),
                style={
                    "font_family": FONT_BODY,
                    "flex": "1",
                    "padding": "9px",
                    "border": "none",
                    "border_radius": "12px",
                    "background": SAND,
                    "color": RUST_DARK,
                    "font_size": "13px",
                    "font_weight": "700",
                    "cursor": "pointer",
                },
            ),
            rx.cond(
                is_offline,
                rx.el.button(
                    t("read_offline"),
                    on_click=RawiState.view_offline(item["id"]),
                    style={
                        "font_family": FONT_BODY,
                        "flex": "1",
                        "padding": "9px",
                        "border": f"1px solid {TEAL}",
                        "border_radius": "12px",
                        "background": "transparent",
                        "color": TEAL,
                        "font_size": "13px",
                        "font_weight": "700",
                        "cursor": "pointer",
                    },
                ),
            ),
            style={"display": "flex", "gap": "8px", "margin_top": "10px"},
        ),
    )


def screen_title(key: str):
    """A bilingual screen heading, e.g. 'Explore Cities · المدن' - shown
    above a tab's content regardless of the active language toggle."""
    return rx.el.h2(
        t2(key),
        style={
            "font_family": FONT_HEADING,
            "font_size": "20px",
            "font_weight": "700",
            "color": INK,
            "margin": "0",
            "text_align": RawiState.text_align,
        },
    )


def browse_breadcrumb():
    return rx.cond(
        RawiState.selected_country_code != "",
        rx.el.div(
            rx.el.span(RawiState.selected_country_label, style={"font_family": FONT_BODY, "font_size": "12px", "color": INK_SOFT}),
            rx.icon(tag="chevron-right", size=12, color=INK_SOFT),
            rx.el.span(t("select_city"), style={"font_family": FONT_BODY, "font_size": "12px", "color": INK_SOFT, "font_weight": "700"}),
            style={"display": "flex", "align_items": "center", "gap": "4px"},
        ),
    )


def browse_tab():
    children = [browse_breadcrumb(), screen_title("explore_cities")]
    if _HAS_MULTIPLE_COUNTRIES:
        children.append(
            card(
                section_label("map-pin", t("select_country"), TEAL),
                pill_row(RawiState.available_countries, RawiState.selected_country_code, RawiState.set_selected_country),
            )
        )
    children.append(
        card(
            section_label("map-pin", t("select_city"), TEAL),
            pill_row(RawiState.available_cities, RawiState.selected_city_code, RawiState.set_selected_city),
        )
    )
    children.append(
        rx.cond(
            RawiState.selected_city_code == "",
            rx.el.p(
                t("choose_city_hint"),
                style={"font_family": FONT_BODY, "font_size": "13px", "color": INK_SOFT, "text_align": "center", "padding": "8px"},
            ),
            rx.el.div(
                rx.foreach(RawiState.browse_landmarks, landmark_card),
                style={"display": "flex", "flex_direction": "column", "gap": "12px"},
            ),
        )
    )
    return rx.el.div(*children, style={"display": "flex", "flex_direction": "column", "gap": "16px", "width": "100%"})


# ---------------------------------------------------------------------------
# Favorites tab — saved landmarks + tag-based recommendations
# ---------------------------------------------------------------------------


def passport_badge(item):
    stamped = item["stamped"] == "true"
    return rx.el.div(
        rx.el.div(
            rx.cond(
                stamped,
                rx.el.span(item["code"], style={"font_family": FONT_HEADING, "font_size": "14px", "font_weight": "800", "color": TEAL}),
                rx.icon(tag="lock", size=16, color=INK_SOFT),
            ),
            style={
                "width": "56px",
                "height": "56px",
                "border_radius": "999px",
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
                "border": f"{rx.cond(stamped, '2px', '1px')} dashed {rx.cond(stamped, TEAL, '#AFA595')}",
                "flex_shrink": "0",
            },
        ),
        rx.el.p(
            item["name"],
            style={"font_family": FONT_HEADING, "font_size": "13px", "font_weight": "700", "color": INK, "text_align": "center", "margin": "0"},
        ),
        rx.cond(
            stamped,
            rx.el.p(item["date"], style={"font_family": FONT_BODY, "font_size": "10px", "color": RUST, "margin": "0"}),
            rx.el.p(t("locked_label"), style={"font_family": FONT_BODY, "font_size": "10px", "color": INK, "opacity": "0.7", "margin": "0"}),
        ),
        style={
            "display": "flex",
            "flex_direction": "column",
            "align_items": "center",
            "gap": "8px",
            "padding": "12px",
            "border_radius": "20px",
            "border": rx.cond(stamped, f"2px solid {GOLD}", f"1.5px dashed {LINE_DEEP}"),
            "background": rx.cond(stamped, "white", LINE),
            "box_shadow": rx.cond(stamped, "0 4px 4px rgba(192, 138, 46, 0.11)", "none"),
            "opacity": rx.cond(stamped, "1", "0.6"),
            "text_align": "center",
        },
    )


def passport_progress_row():
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                t("stamps_collected"),
                style={"font_family": FONT_BODY, "font_size": "13px", "font_weight": "600", "color": INK},
            ),
            rx.el.span(
                RawiState.passport_count_label,
                style={"font_family": FONT_BODY, "font_size": "13px", "font_weight": "700", "color": TEAL},
            ),
            style={"display": "flex", "align_items": "center", "justify_content": "space-between"},
        ),
        rx.el.div(
            rx.el.div(
                style={
                    "height": "100%",
                    "width": RawiState.passport_progress_pct,
                    "background": TEAL,
                    "border_radius": "5px",
                    "transition": "width 0.3s ease",
                },
            ),
            style={"width": "100%", "height": "10px", "background": LINE, "border_radius": "5px", "overflow": "hidden"},
        ),
        style={"display": "flex", "flex_direction": "column", "gap": "6px", "width": "100%"},
    )


def passport_strip():
    return rx.el.div(
        rx.foreach(RawiState.passport_cards, passport_badge),
        style={"display": "grid", "grid_template_columns": "1fr 1fr", "gap": "12px", "width": "100%"},
    )


def passport_tab():
    return rx.el.div(
        rx.el.div(
            screen_title("passport_title"),
            rx.el.p(
                t("passport_hint"),
                style={"font_family": FONT_BODY, "font_size": "12px", "color": INK_SOFT, "margin": "0", "text_align": "center"},
            ),
            style={
                "width": "100%",
                "padding": "16px",
                "border_radius": "16px",
                "border": f"2px dashed {GOLD}",
                "background": CARD,
                "box_sizing": "border-box",
                "display": "flex",
                "flex_direction": "column",
                "align_items": "center",
                "gap": "8px",
                "text_align": "center",
            },
        ),
        passport_progress_row(),
        passport_strip(),
        style={"display": "flex", "flex_direction": "column", "gap": "16px", "width": "100%"},
    )


def favorites_tab():
    return rx.el.div(
        screen_title("your_saved_stories"),
        rx.cond(
            RawiState.favorite_cards.length() == 0,
            rx.el.p(
                t("no_favorites_yet"),
                style={"font_family": FONT_BODY, "font_size": "13px", "color": INK_SOFT, "text_align": "center", "padding": "8px"},
            ),
            rx.el.div(
                rx.foreach(RawiState.favorite_cards, landmark_card),
                style={"display": "flex", "flex_direction": "column", "gap": "12px"},
            ),
        ),
        rx.cond(
            RawiState.recommended_cards.length() > 0,
            rx.el.div(
                section_label("sparkles", t("recommended_for_you"), GOLD),
                rx.el.div(
                    rx.foreach(RawiState.recommended_cards, landmark_card),
                    style={"display": "flex", "flex_direction": "column", "gap": "12px"},
                ),
                style={"margin_top": "6px"},
            ),
        ),
        style={"display": "flex", "flex_direction": "column", "gap": "16px", "width": "100%"},
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
