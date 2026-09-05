"""Agent that changes the route when congestion is detected."""

from app.camara.congestion import get_congestion


def suggest_route(area_id: str) -> dict:
    """Use CAMARA congestion insights to decide whether to reroute."""
    congestion = get_congestion(area_id)

    if congestion["recommend_reroute"]:
        route = "Use the quieter heritage path through the east entrance."
    else:
        route = "Continue on the main heritage route."

    return {
        "congestion": congestion,
        "route": route,
    }

