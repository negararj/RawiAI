"""Check whether the CAMARA / Nokia wrappers are connected.

Run from the project root:

    python scripts/check_camara.py

For real Nokia calls, set this in .env first:

    RAWIAI_USE_LIVE_APIS=true
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.agents.sites import AL_HISN_FORT
from app.camara.congestion import get_congestion
from app.camara.geofencing import subscribe_geofence
from app.camara.location import get_device_location, verify_location
from app.camara.number import verify_number
from app.camara.qos import request_qos
from app.config import (
    NOKIA_API_KEY,
    NOKIA_GEOFENCE_SINK_URL,
    NOKIA_TEST_PHONE_NUMBER,
    RAWIAI_USE_LIVE_APIS,
)


def _print_result(name: str, result: dict):
    print(f"\n=== {name} ===")
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))


def main():
    print("RawiAI CAMARA health check")
    print(f"Live CAMARA mode: {RAWIAI_USE_LIVE_APIS}")
    print(f"Nokia API key present: {bool(NOKIA_API_KEY)}")
    print(f"Nokia test phone present: {bool(NOKIA_TEST_PHONE_NUMBER)}")
    print(f"Geofence sink URL present: {bool(NOKIA_GEOFENCE_SINK_URL)}")

    phone_number = NOKIA_TEST_PHONE_NUMBER or "+99999991000"
    site = AL_HISN_FORT

    _print_result("Number Verification", verify_number(phone_number))
    _print_result("Location Retrieval", get_device_location())
    _print_result(
        "Location Verification",
        verify_location(site["lat"], site["lon"], site["radius_meters"]),
    )
    _print_result(
        "Geofencing",
        subscribe_geofence(
            site["name"],
            site["lat"],
            site["lon"],
            site["radius_meters"],
        ),
    )
    _print_result("Congestion Insights", get_congestion(site["id"]))
    _print_result("Quality on Demand", request_qos("rawiai-health-check-session"))


if __name__ == "__main__":
    main()
