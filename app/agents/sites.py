"""Heritage site catalog used by the agents and the Browse tab."""


AL_HISN_FORT = {
    "id": "al-hisn-fort",
    "name_en": "Al Hisn Fort",
    "name_ar": "قلعة الحصن",
    "country_code": "AE",
    "country_en": "United Arab Emirates",
    "country_ar": "الإمارات العربية المتحدة",
    "city_code": "sharjah",
    "city_en": "Sharjah",
    "city_ar": "الشارقة",
    "lat": 25.3573,
    "lon": 55.3820,
    "radius_meters": 150,
    "tags": ["fort", "museum", "old-city"],
    # Illustrative "quieter path" waypoint used to demo the congestion
    # reroute feature and the live map - not a claim about a specific
    # real gate.
    "alt_name_en": "Al Hisn Fort - Quieter East Path",
    "alt_name_ar": "قلعة الحصن - المسار الشرقي الهادئ",
    "alt_lat": 25.3578,
    "alt_lon": 55.3835,
}

QASR_AL_HOSN = {
    "id": "qasr-al-hosn",
    "name_en": "Qasr Al Hosn",
    "name_ar": "قصر الحصن",
    "country_code": "AE",
    "country_en": "United Arab Emirates",
    "country_ar": "الإمارات العربية المتحدة",
    "city_code": "abu-dhabi",
    "city_en": "Abu Dhabi",
    "city_ar": "أبوظبي",
    "lat": 24.4764,
    "lon": 54.3705,
    "radius_meters": 150,
    "tags": ["fort", "palace", "old-city"],
    "alt_name_en": "Qasr Al Hosn - Quieter Garden Path",
    "alt_name_ar": "قصر الحصن - مسار الحديقة الهادئ",
    "alt_lat": 24.4778,
    "alt_lon": 54.3718,
}

AL_FAHIDI = {
    "id": "al-fahidi",
    "name_en": "Al Fahidi Historical Neighbourhood",
    "name_ar": "حي الفهيدي التاريخي",
    "country_code": "AE",
    "country_en": "United Arab Emirates",
    "country_ar": "الإمارات العربية المتحدة",
    "city_code": "dubai",
    "city_en": "Dubai",
    "city_ar": "دبي",
    "lat": 25.2637,
    "lon": 55.2972,
    "radius_meters": 200,
    "tags": ["old-city", "heritage-district", "wind-towers"],
    "alt_name_en": "Al Fahidi - Quieter Creekside Path",
    "alt_name_ar": "الفهيدي - مسار الخور الهادئ",
    "alt_lat": 25.2651,
    "alt_lon": 55.2989,
}


DEMO_SITES = {
    AL_HISN_FORT["id"]: AL_HISN_FORT,
    QASR_AL_HOSN["id"]: QASR_AL_HOSN,
    AL_FAHIDI["id"]: AL_FAHIDI,
}

DEFAULT_SITE_ID = AL_HISN_FORT["id"]


def get_site(site_id: str) -> dict:
    """Look up a demo site by id, falling back to the default site."""
    return DEMO_SITES.get(site_id, AL_HISN_FORT)
