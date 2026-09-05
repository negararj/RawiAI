"""CAMARA Congestion Insights wrapper."""


def get_congestion(area_id: str) -> dict:
    """Check whether the network is congested near a route or site.

    CAMARA capability: Congestion / Connectivity Insights.
    """
    return {
        "area_id": area_id,
        "congestion_level": "low",
        "recommend_reroute": False,
        "source": "stub",
    }

