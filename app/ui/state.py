"""Reflex state for the RawiAI demo app."""

import asyncio
import json
from datetime import date

import reflex as rx

from app.agents.graph import run_demo_flow
from app.agents.sites import DEFAULT_SITE_ID, DEMO_SITES, get_site

# Resolves to the transcript (or "" on any failure/no-support), so
# rx.call_script's Promise-awaiting behavior hands the callback a plain
# string either way.
_VOICE_INPUT_SCRIPT = """
(function() {
  var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    return Promise.resolve("");
  }
  return new Promise(function(resolve) {
    var langEl = document.getElementById("rawi-language");
    var lang = (langEl && langEl.innerText === "ar") ? "ar-SA" : "en-US";
    var recognition = new SpeechRecognition();
    recognition.lang = lang;
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;
    var done = false;
    var finish = function(value) {
      if (done) return;
      done = true;
      resolve(value);
    };
    recognition.onresult = function(event) {
      finish(event.results[0][0].transcript);
    };
    recognition.onerror = function() {
      finish("");
    };
    recognition.onend = function() {
      finish("");
    };
    try {
      recognition.start();
    } catch (e) {
      finish("");
    }
  });
})()
"""


def _describe_source(source: str) -> tuple[str, bool]:
    """(subtitle, verified) for a timeline row, derived from its real
    source tag - never invents an API name for a non-CAMARA step."""
    if "-camara-" in source:
        api_name = source.split("-camara-", 1)[1].replace("-", " ").title()
        return f"CAMARA {api_name}", "error" not in source
    if source.startswith("gemini:"):
        return "Gemini AI", True
    if "fallback" in source:
        return "Local Fallback Logic", "error" not in source
    if "offline" in source or "cache" in source:
        return "Offline Cache", True
    return source, "error" not in source


class RawiState(rx.State):
    """State shared by the mobile UI."""

    language: str = "en"
    question: str = ""
    status: str = "Tap Begin and let the network find you."

    active_tab: str = "explore"
    selected_site_id: str = DEFAULT_SITE_ID
    selected_country_code: str = get_site(DEFAULT_SITE_ID)["country_code"]
    selected_city_code: str = ""

    favorite_ids: list[str] = []
    cached_stories: dict[str, str] = {}
    stamped_ids: list[str] = []
    stamped_dates: dict[str, str] = {}
    is_offline_view: bool = False

    started: bool = False
    is_loading: bool = False
    is_listening: bool = False

    # Trust-layer chips (CAMARA signals), revealed in sequence for the demo.
    step_identity: bool = False
    step_presence: bool = False
    step_network: bool = False
    step_qos: bool = False

    answer: str = ""
    story_page_index: int = 0
    route: str = ""
    route_reason: str = ""
    congestion_level: str = ""
    qos_status: str = ""
    current_site: str = ""
    geofence_status: str = ""
    sim_swap_status: str = ""
    story_source: str = ""
    flow_summary: str = ""
    pwa_status: str = "Installable on supported mobile browsers"

    camara_calls: list[str] = []
    timeline: list[dict[str, str]] = []

    arrival_watch_enabled: bool = False
    music_playing: bool = False

    def toggle_music(self):
        self.music_playing = not self.music_playing
        script = (
            "var el = document.getElementById('rawi-bgm'); "
            "if (el) { " + ("el.play().catch(function(){});" if self.music_playing else "el.pause();") + " }"
        )
        return rx.call_script(script)

    def toggle_arrival_watch(self):
        self.arrival_watch_enabled = not self.arrival_watch_enabled
        if self.arrival_watch_enabled:
            return rx.call_script("window.rawiStartArrivalWatch && window.rawiStartArrivalWatch();")
        return rx.call_script("window.rawiStopArrivalWatch && window.rawiStopArrivalWatch();")

    def set_language(self, language: str):
        self.language = language

    def set_question(self, question: str):
        self.question = question

    def start_voice_input(self):
        self.is_listening = True
        return rx.call_script(_VOICE_INPUT_SCRIPT, callback=RawiState.finish_voice_input)

    def finish_voice_input(self, transcript: str):
        self.is_listening = False
        if transcript:
            self.question = transcript

    @rx.var
    def is_ar(self) -> bool:
        return self.language == "ar"

    @rx.var
    def dir(self) -> str:
        return "rtl" if self.language == "ar" else "ltr"

    @rx.var
    def text_align(self) -> str:
        return "right" if self.language == "ar" else "left"

    @rx.var
    def selected_site_name(self) -> str:
        site = get_site(self.selected_site_id)
        return site["name_ar"] if self.is_ar else site["name_en"]

    @rx.var
    def selected_site_lat(self) -> str:
        return str(get_site(self.selected_site_id)["lat"])

    @rx.var
    def selected_site_lon(self) -> str:
        return str(get_site(self.selected_site_id)["lon"])

    @rx.var
    def selected_site_radius(self) -> str:
        return str(get_site(self.selected_site_id)["radius_meters"])

    @rx.var
    def selected_alt_lat(self) -> str:
        return str(get_site(self.selected_site_id)["alt_lat"])

    @rx.var
    def selected_alt_lon(self) -> str:
        return str(get_site(self.selected_site_id)["alt_lon"])

    @rx.var
    def selected_alt_name(self) -> str:
        site = get_site(self.selected_site_id)
        return site["alt_name_ar"] if self.is_ar else site["alt_name_en"]

    @rx.var
    def selected_site_teaser(self) -> str:
        site = get_site(self.selected_site_id)
        return site["teaser_ar"] if self.is_ar else site["teaser_en"]


    # -----------------------------------------------------------------
    # Browse tab: country -> city -> landmark
    # -----------------------------------------------------------------

    @rx.var
    def available_countries(self) -> list[dict[str, str]]:
        seen: dict[str, str] = {}
        for site in DEMO_SITES.values():
            seen[site["country_code"]] = site["country_ar"] if self.is_ar else site["country_en"]
        return [{"code": code, "label": label} for code, label in seen.items()]

    @rx.var
    def selected_country_label(self) -> str:
        for country in self.available_countries:
            if country["code"] == self.selected_country_code:
                return country["label"]
        return ""

    @rx.var
    def available_cities(self) -> list[dict[str, str]]:
        if not self.selected_country_code:
            return []
        seen: dict[str, str] = {}
        for site in DEMO_SITES.values():
            if site["country_code"] != self.selected_country_code:
                continue
            seen[site["city_code"]] = site["city_ar"] if self.is_ar else site["city_en"]
        return [{"code": code, "label": label} for code, label in seen.items()]

    @rx.var
    def browse_landmarks(self) -> list[dict[str, str]]:
        results = []
        for site in DEMO_SITES.values():
            if self.selected_country_code and site["country_code"] != self.selected_country_code:
                continue
            if self.selected_city_code and site["city_code"] != self.selected_city_code:
                continue
            results.append(
                {
                    "id": site["id"],
                    "name": site["name_ar"] if self.is_ar else site["name_en"],
                    "city": site["city_ar"] if self.is_ar else site["city_en"],
                    "is_favorite": "true" if site["id"] in self.favorite_ids else "false",
                    "has_offline": "true" if self._cache_story_key(site["id"]) in self.cached_stories else "false",
                }
            )
        return results

    def set_selected_country(self, code: str):
        self.selected_country_code = code
        self.selected_city_code = ""

    def set_selected_city(self, code: str):
        self.selected_city_code = code

    def set_active_tab(self, tab: str):
        self.active_tab = tab

    def _reset_explore(self):
        self.started = False
        self.is_loading = False
        self.is_offline_view = False
        self.step_identity = False
        self.step_presence = False
        self.step_network = False
        self.step_qos = False
        self.answer = ""
        self.story_page_index = 0
        self.route = ""
        self.route_reason = ""
        self.congestion_level = ""
        self.qos_status = ""
        self.current_site = ""
        self.geofence_status = ""
        self.sim_swap_status = ""
        self.story_source = ""
        self.status = "Tap Begin and let the network find you."

    @rx.var
    def story_pages(self) -> list[str]:
        text = self.answer.strip()
        if not text:
            return []

        # Prefer blank-line paragraph breaks. Gemini doesn't always use them
        # (seen with some Arabic responses that come back as one block with
        # single newlines instead), so fall back to single newlines, and
        # only treat it as one page if there's truly no break at all.
        pages = [p.strip() for p in text.split("\n\n") if p.strip()]
        if len(pages) > 1:
            return pages

        pages = [p.strip() for p in text.split("\n") if p.strip()]
        if len(pages) > 1:
            return pages

        return [text]

    @rx.var
    def story_page_count(self) -> int:
        return len(self.story_pages)

    @rx.var
    def story_page_dots(self) -> list[int]:
        return list(range(len(self.story_pages)))

    @rx.var
    def current_story_page(self) -> str:
        pages = self.story_pages
        if not pages:
            return ""
        index = min(self.story_page_index, len(pages) - 1)
        return pages[index]

    def next_story_page(self):
        if self.story_page_index < len(self.story_pages) - 1:
            self.story_page_index += 1

    def prev_story_page(self):
        if self.story_page_index > 0:
            self.story_page_index -= 1

    def select_landmark(self, site_id: str):
        """Chosen from the Browse tab - switch the active landmark and jump to Explore."""
        self.selected_site_id = site_id
        self.active_tab = "explore"
        self._reset_explore()

    # -----------------------------------------------------------------
    # Favorites + simple tag-based recommendations
    # -----------------------------------------------------------------

    def toggle_favorite(self, site_id: str):
        if site_id in self.favorite_ids:
            self.favorite_ids = [f for f in self.favorite_ids if f != site_id]
        else:
            self.favorite_ids = [*self.favorite_ids, site_id]
        return rx.call_script(
            f"localStorage.setItem('rawi_favorites', {json.dumps(json.dumps(self.favorite_ids))});"
        )

    def hydrate_local_data(self, value: str):
        """Restore favorites, offline-cached stories, and passport stamps saved on this device."""
        try:
            data = json.loads(value) if value else {}
        except (TypeError, ValueError):
            data = {}

        favorites = data.get("favorites") or []
        self.favorite_ids = [site_id for site_id in favorites if site_id in DEMO_SITES]

        stories = data.get("stories") or {}
        self.cached_stories = {k: v for k, v in stories.items() if isinstance(v, str)}

        stamps = data.get("stamps") or []
        self.stamped_ids = [site_id for site_id in stamps if site_id in DEMO_SITES]

        stamp_dates = data.get("stamp_dates") or {}
        self.stamped_dates = {
            site_id: value for site_id, value in stamp_dates.items() if site_id in DEMO_SITES and isinstance(value, str)
        }

    def load_local_data(self):
        return rx.call_script(
            """
JSON.stringify({
  favorites: JSON.parse(localStorage.getItem('rawi_favorites') || '[]'),
  stories: JSON.parse(localStorage.getItem('rawi_offline_stories') || '{}'),
  stamps: JSON.parse(localStorage.getItem('rawi_stamps') || '[]'),
  stamp_dates: JSON.parse(localStorage.getItem('rawi_stamp_dates') || '{}')
})
""",
            callback=RawiState.hydrate_local_data,
        )

    def _persist_stamps(self):
        return rx.call_script(
            f"localStorage.setItem('rawi_stamps', {json.dumps(json.dumps(self.stamped_ids))});"
            f"localStorage.setItem('rawi_stamp_dates', {json.dumps(json.dumps(self.stamped_dates))});"
        )

    @rx.var
    def passport_cards(self) -> list[dict[str, str]]:
        return [
            {
                "id": site["id"],
                "name": site["name_ar"] if self.is_ar else site["name_en"],
                "code": site["stamp_code"],
                "date": self.stamped_dates.get(site["id"], ""),
                "stamped": "true" if site["id"] in self.stamped_ids else "false",
            }
            for site in DEMO_SITES.values()
        ]

    @rx.var
    def passport_count_label(self) -> str:
        count, total = len(self.stamped_ids), len(DEMO_SITES)
        if self.is_ar:
            return f"{count} من {total} مواقع تمت زيارتها"
        return f"{count} of {total} sites visited"

    @rx.var
    def passport_progress_pct(self) -> str:
        total = len(DEMO_SITES)
        if total == 0:
            return "0%"
        return f"{(len(self.stamped_ids) / total) * 100:.0f}%"

    def _cache_story_key(self, site_id: str | None = None, language: str | None = None) -> str:
        return f"{site_id or self.selected_site_id}:{language or self.language}"

    def _persist_story_cache(self):
        return rx.call_script(
            f"localStorage.setItem('rawi_offline_stories', {json.dumps(json.dumps(self.cached_stories))});"
        )

    @rx.var
    def favorite_cards(self) -> list[dict[str, str]]:
        return [
            {
                "id": site["id"],
                "name": site["name_ar"] if self.is_ar else site["name_en"],
                "city": site["city_ar"] if self.is_ar else site["city_en"],
                "is_favorite": "true",
                "has_offline": "true" if self._cache_story_key(site["id"]) in self.cached_stories else "false",
            }
            for site in DEMO_SITES.values()
            if site["id"] in self.favorite_ids
        ]

    @rx.var
    def recommended_cards(self) -> list[dict[str, str]]:
        favorite_tags: set[str] = set()
        for site in DEMO_SITES.values():
            if site["id"] in self.favorite_ids:
                favorite_tags.update(site["tags"])

        if not favorite_tags:
            return []

        return [
            {
                "id": site["id"],
                "name": site["name_ar"] if self.is_ar else site["name_en"],
                "city": site["city_ar"] if self.is_ar else site["city_en"],
                "is_favorite": "false",
                "has_offline": "false",
            }
            for site in DEMO_SITES.values()
            if site["id"] not in self.favorite_ids and set(site["tags"]) & favorite_tags
        ]

    def view_offline(self, site_id: str):
        """Replay a previously cached story with no network round trip at all."""
        key = self._cache_story_key(site_id)
        cached_answer = self.cached_stories.get(key)
        if cached_answer is None:
            return

        self.selected_site_id = site_id
        self.active_tab = "explore"
        self._reset_explore()

        site = get_site(site_id)
        self.is_offline_view = True
        self.started = True
        self.current_site = site["name_ar"] if self.is_ar else site["name_en"]
        self.answer = cached_answer
        self.story_source = "offline-cache"
        self.status = "Showing a story saved earlier on this device."

    # -----------------------------------------------------------------
    # Explore tab: the CAMARA + Gemini demo flow
    # -----------------------------------------------------------------

    async def start_demo(self):
        """Run the demo flow and reveal each CAMARA-verified step in order."""
        self._reset_explore()
        self.started = True
        self.is_loading = True
        self.status = "Sensing your presence on the network..."
        yield
        await asyncio.sleep(0.35)

        effective_question = self.question.strip() or "Tell me the story of this place."
        try:
            result = run_demo_flow(effective_question, language=self.language, site_id=self.selected_site_id)
        except Exception:
            # A live Nokia/Gemini/audio call failed in a way none of their
            # own try/excepts caught. Show a plain retry message instead of
            # letting it surface as the generic "contact the administrator"
            # error toast, and leave the story empty rather than half-built.
            self.is_loading = False
            self.status = "Something interrupted the network check - please tap Begin the Story again."
            yield
            return

        self.camara_calls = result["camara_calls"]
        _raw_timeline = result["timeline"]
        self.timeline = [
            {
                "step": item["step"],
                "detail": item["detail"],
                "source": item["source"],
                "api_label": _describe_source(item["source"])[0],
                "verified": "true" if _describe_source(item["source"])[1] else "false",
                "is_last": "true" if idx == len(_raw_timeline) - 1 else "false",
            }
            for idx, item in enumerate(_raw_timeline)
        ]
        self.flow_summary = result["summary"]

        _swapped = result["sim_swap"].get("swapped")
        self.sim_swap_status = "no_swap" if _swapped is False else "swapped" if _swapped else "unknown"
        self.step_identity = True
        self.status = f"Identity confirmed via {result['identity']['source']}"
        yield
        await asyncio.sleep(0.35)

        self.current_site = result["location"]["near_monument"]
        self.geofence_status = f"Geofence: {result['location']['geofence']['status']}"
        self.step_presence = True
        self.status = f"Presence verified near {self.current_site}"
        yield
        await asyncio.sleep(0.35)

        self.congestion_level = result["route"]["congestion"]["congestion_level"]
        self.route = result["route"]["route"]
        self.route_reason = result["route"]["reason"]
        self.step_network = True
        self.status = "Network context confirmed"
        yield
        await asyncio.sleep(0.3)

        self.answer = result["qa"]["answer"]
        self.story_source = result["qa"]["source"]
        self.status = "The storyteller is speaking..."
        yield
        await asyncio.sleep(0.3)

        self.qos_status = result["qos"]["status"]
        self.step_qos = True
        self.status = "Your heritage story is live"
        self.is_loading = False

        # Cache the finished story so it can be replayed offline later,
        # from the Favorites tab, with no network round trip at all.
        if self.answer:
            self.cached_stories = {
                **self.cached_stories,
                self._cache_story_key(): self.answer,
            }
            yield self._persist_story_cache()

        # Stamp the passport for this landmark on a real, completed visit.
        if self.answer and self.selected_site_id not in self.stamped_ids:
            self.stamped_ids = [*self.stamped_ids, self.selected_site_id]
            self.stamped_dates = {**self.stamped_dates, self.selected_site_id: date.today().strftime("%b %d, %Y")}
            yield self._persist_stamps()
