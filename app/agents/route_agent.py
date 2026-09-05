"""Agent that changes the route when congestion is detected."""

from app.camara.congestion import get_congestion


def suggest_route(area_id: str) -> dict:
    """Use CAMARA congestion insights to decide whether to reroute."""
    congestion = get_congestion(area_id)

    if congestion["recommend_reroute"]:
        route = "Use the quieter heritage path through the east entrance."
        reason = (
            "CAMARA Congestion Insights reports enough congestion that "
            "the Route Agent should suggest a calmer path."
        )
    else:
        route = "Continue on the main heritage route."
        reason = (
            "CAMARA Congestion Insights does not show enough congestion "
            "to change the visitor route."
        )

    return {
        "area_id": area_id,
        "congestion": congestion,
        "route": route,
        "reason": reason,
        "camara_calls": ["Congestion Insights"],
    }
