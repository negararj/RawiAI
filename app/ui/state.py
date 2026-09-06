"""Reflex state for the RawiAI demo app."""

import asyncio
import json

import reflex as rx

from app.agents.graph import run_demo_flow
from app.agents.sites import DEFAULT_SITE_ID, DEMO_SITES, get_site


class RawiState(rx.State):
    """State shared by the mobile UI."""

    language: str = "en"
    question: str = "Tell me the story of this place."
    status: str = "Tap Begin and let the network find you."

    active_tab: str = "explore"
    selected_site_id: str = DEFAULT_SITE_ID
    selected_country_code: str = ""
    selected_city_code: str = ""

    favorite_ids: list[str] = []

    started: bool = False
    is_loading: bool = False

    # Trust-layer chips (CAMARA signals), revealed in sequence for the demo.
    step_identity: bool = False
    step_presence: bool = False
    step_network: bool = False
    step_qos: bool = False

    answer: str = ""
    route: str = ""
    route_reason: str = ""
    congestion_level: str = ""
    qos_status: str = ""
    current_site: str = ""
    geofence_status: str = ""
    story_source: str = ""
    flow_summary: str = ""
    pwa_status: str = "Installable on supported mobile browsers"

    camara_calls: list[str] = []
    timeline: list[dict[str, str]] = []

    arrival_watch_enabled: bool = False

    def toggle_arrival_watch(self):
        self.arrival_watch_enabled = not self.arrival_watch_enabled
        if self.arrival_watch_enabled:
            return rx.call_script("window.rawiStartArrivalWatch && window.rawiStartArrivalWatch();")
        return rx.call_script("window.rawiStopArrivalWatch && window.rawiStopArrivalWatch();")

    def set_language(self, language: str):
        self.language = language

    def set_question(self, question: str):
        self.question = question

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
        self.step_identity = False
        self.step_presence = False
        self.step_network = False
        self.step_qos = False
        self.answer = ""
        self.route = ""
        self.route_reason = ""
        self.congestion_level = ""
        self.qos_status = ""
        self.current_site = ""
        self.geofence_status = ""
        self.story_source = ""
        self.status = "Tap Begin and let the network find you."

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

    def hydrate_favorites(self, value: str):
        try:
            loaded = json.loads(value) if value else []
        except (TypeError, ValueError):
            loaded = []
        self.favorite_ids = [site_id for site_id in loaded if site_id in DEMO_SITES]

    def load_favorites(self):
        return rx.call_script(
            "localStorage.getItem('rawi_favorites') || '[]'",
            callback=RawiState.hydrate_favorites,
        )

    @rx.var
    def favorite_cards(self) -> list[dict[str, str]]:
        return [
            {
                "id": site["id"],
                "name": site["name_ar"] if self.is_ar else site["name_en"],
                "city": site["city_ar"] if self.is_ar else site["city_en"],
                "is_favorite": "true",
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
            }
            for site in DEMO_SITES.values()
            if site["id"] not in self.favorite_ids and set(site["tags"]) & favorite_tags
        ]

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

        result = run_demo_flow(self.question, language=self.language, site_id=self.selected_site_id)

        self.camara_calls = result["camara_calls"]
        self.timeline = [
            {
                "step": item["step"],
                "detail": item["detail"],
                "source": item["source"],
            }
            for item in result["timeline"]
        ]
        self.flow_summary = result["summary"]

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
