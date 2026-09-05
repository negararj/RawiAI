"""CAMARA Congestion Insights wrapper."""

from app.config import NOKIA_API_KEY, NOKIA_TEST_PHONE_NUMBER, RAWIAI_USE_LIVE_APIS
from app.camara.client import get_nokia_client
from app.camara.utils import api_error, to_dict_list


CONGESTION_SCORE = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
}


def get_congestion(area_id: str) -> dict:
    """Check whether the network is congested near a route or site.

    CAMARA capability: Congestion / Connectivity Insights.
    """
    if not RAWIAI_USE_LIVE_APIS or not NOKIA_API_KEY or not NOKIA_TEST_PHONE_NUMBER:
        return {
            "area_id": area_id,
            "congestion_level": "Medium",
            "recommend_reroute": True,
            "source": "demo-camara-congestion-insights",
            "message": (
                "Demo mode is using simulated CAMARA Congestion Insights. "
                "Set RAWIAI_USE_LIVE_APIS=true to call Nokia."
            ),
        }

    try:
        client = get_nokia_client()
        response = client.congestion_insights.query(
            device={"phone_number": NOKIA_TEST_PHONE_NUMBER},
        )
    except Exception as exc:
        return {
            "area_id": area_id,
            "congestion_level": "Unknown",
            "recommend_reroute": False,
            **api_error("nokia-camara-congestion-insights", exc),
        }

    items = to_dict_list(response)
    levels = [item.get("congestionLevel") for item in items]
    highest_level = max(levels, key=lambda level: CONGESTION_SCORE.get(level, 0), default="Unknown")

    return {
        "area_id": area_id,
        "congestion_level": highest_level,
        "recommend_reroute": highest_level in {"Medium", "High"},
        "source": "nokia-camara-congestion-insights",
        "raw": items,
    }
