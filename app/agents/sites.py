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
    "teaser_en": "Step through the doors of a 19th-century fort that once watched over Sharjah's old city.",
    "teaser_ar": "ادخل من أبواب قلعة يعود تاريخها إلى القرن التاسع عشر، كانت تحرس مدينة الشارقة القديمة.",
    # Real IATA code for the site's city - used as the passport stamp code.
    "stamp_code": "SHJ",
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
    "teaser_en": "Once a watchtower guarding the island's only freshwater well, now the living memory of how Abu Dhabi began.",
    "teaser_ar": "كانت برجًا للمراقبة يحرس بئر المياه العذبة الوحيد في الجزيرة، واليوم هي الذاكرة الحية لبداية أبوظبي.",
    "stamp_code": "AUH",
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
    "teaser_en": "Wind towers, coral-and-gypsum walls, and lanes once home to Dubai Creek's pearl-trading merchants.",
    "teaser_ar": "أبراج الرياح وجدران المرجان والجص وأزقة كانت موطنًا لتجار اللؤلؤ على خور دبي.",
    "stamp_code": "DXB",
}


PETRA = {
    "id": "petra",
    "name_en": "Petra",
    "name_ar": "البتراء",
    "country_code": "JO",
    "country_en": "Jordan",
    "country_ar": "الأردن",
    "city_code": "wadi-musa",
    "city_en": "Wadi Musa",
    "city_ar": "وادي موسى",
    "lat": 30.3285,
    "lon": 35.4444,
    "radius_meters": 250,
    "tags": ["nabataean", "tombs", "unesco", "canyon"],
    "alt_name_en": "Petra - Quieter High Place Trail",
    "alt_name_ar": "البتراء - مسار المكان المرتفع الهادئ",
    "alt_lat": 30.3247,
    "alt_lon": 35.4472,
    "teaser_en": "A rose-red city carved into sandstone cliffs by the Nabataeans, reached through a narrow canyon.",
    "teaser_ar": "مدينة وردية اللون نحتها الأنباط في صخور رملية، يصل إليها الزائر عبر ممر صخري ضيق.",
    "stamp_code": "AQJ",
}

HEGRA = {
    "id": "hegra",
    "name_en": "Hegra",
    "name_ar": "الحِجر",
    "country_code": "SA",
    "country_en": "Saudi Arabia",
    "country_ar": "المملكة العربية السعودية",
    "city_code": "alula",
    "city_en": "AlUla",
    "city_ar": "العُلا",
    "lat": 26.7911,
    "lon": 37.9533,
    "radius_meters": 250,
    "tags": ["nabataean", "tombs", "unesco", "desert"],
    "alt_name_en": "Hegra - Quieter North Ridge Path",
    "alt_name_ar": "الحِجر - مسار التلال الشمالية الهادئ",
    "alt_lat": 26.7944,
    "alt_lon": 37.9567,
    "teaser_en": "Saudi Arabia's first UNESCO site: over 100 monumental Nabataean tombs carved into desert sandstone.",
    "teaser_ar": "أول موقع سعودي على قائمة اليونسكو للتراث العالمي: أكثر من مئة مقبرة نبطية منحوتة في صخور الصحراء.",
    "stamp_code": "ULH",
}

AL_ZUBARAH = {
    "id": "al-zubarah",
    "name_en": "Al Zubarah",
    "name_ar": "الزبارة",
    "country_code": "QA",
    "country_en": "Qatar",
    "country_ar": "قطر",
    "city_code": "al-shamal",
    "city_en": "Al Shamal",
    "city_ar": "الشمال",
    "lat": 25.9803,
    "lon": 51.0331,
    "radius_meters": 250,
    "tags": ["archaeological", "unesco", "coastal", "pearling"],
    "alt_name_en": "Al Zubarah - Quieter Seaward Wall",
    "alt_name_ar": "الزبارة - سور الجهة البحرية الهادئ",
    "alt_lat": 25.9831,
    "alt_lon": 51.0298,
    "teaser_en": "Qatar's only UNESCO site: a fortified 18th-century pearling and trading town, abandoned and remarkably preserved.",
    "teaser_ar": "الموقع القطري الوحيد على قائمة اليونسكو: مدينة محصّنة للغوص واللؤلؤ والتجارة من القرن الثامن عشر، هُجرت وحُفظت بشكل استثنائي.",
    "stamp_code": "DOH",
}


DEMO_SITES = {
    AL_HISN_FORT["id"]: AL_HISN_FORT,
    QASR_AL_HOSN["id"]: QASR_AL_HOSN,
    AL_FAHIDI["id"]: AL_FAHIDI,
    PETRA["id"]: PETRA,
    HEGRA["id"]: HEGRA,
    AL_ZUBARAH["id"]: AL_ZUBARAH,
}

DEFAULT_SITE_ID = AL_HISN_FORT["id"]


def get_site(site_id: str) -> dict:
    """Look up a demo site by id, falling back to the default site."""
    return DEMO_SITES.get(site_id, AL_HISN_FORT)
