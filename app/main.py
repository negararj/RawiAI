"""Reflex app entry point."""

import logging

import reflex as rx
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.ui.insights_page import insights_index
from app.ui.pages import index
from app.webhooks.geofence_events import receive_geofence_event

logger = logging.getLogger(__name__)


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?"
        "family=Baloo+2:wght@500;600;700;800"
        "&family=Lalezar"
        "&family=Reem+Kufi:wght@400..700"
        "&family=Tajawal:wght@400;500;700;800"
        "&family=Inter:wght@400;500;600;700"
        "&family=Amiri:ital,wght@0,400;0,700;1,400"
        "&display=swap",
        "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css",
    ],
    style={"font_family": "'Tajawal', sans-serif"},
)
async def _geofence_webhook(request: Request) -> JSONResponse:
    """Receive CAMARA geofencing CloudEvents from Nokia's network.

    Registered directly on the Starlette ASGI app since Reflex's App does
    not expose a public API for adding custom HTTP routes.
    """
    payload = await request.json()
    result = receive_geofence_event(payload)
    logger.info("Received CAMARA geofence event: %s", result)
    return JSONResponse(result)


@app.register_lifespan_task
async def _register_custom_routes():
    if app._api is not None:
        app._api.add_route("/geofence", _geofence_webhook, methods=["POST"])


app.add_page(
    index,
    route="/",
    title="RawiAI",
    description="Network-aware heritage storytelling powered by CAMARA APIs.",
    meta=[
        rx.el.link(rel="manifest", href="/manifest.webmanifest"),
        {"name": "theme-color", "content": "#9b4f24"},
        {"name": "apple-mobile-web-app-capable", "content": "yes"},
        {"name": "apple-mobile-web-app-title", "content": "RawiAI"},
    ],
)
app.add_page(
    insights_index,
    route="/insights",
    title="RawiAI Insights",
    description="Operator-facing view of aggregated, anonymized visitor activity.",
)
