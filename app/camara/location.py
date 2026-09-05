"""CAMARA Location Retrieval and Location Verification wrappers."""


def verify_location(lat: float, lon: float, radius_meters: int) -> dict:
    """Check whether the visitor is inside the heritage site area.

    CAMARA capability: Location Verification.
    """
    return {
        "verified": False,
        "lat": lat,
        "lon": lon,
        "radius_meters": radius_meters,
        "source": "stub",
    }


def get_device_location() -> dict:
    """Get the visitor device location from the network.

    CAMARA capability: Location Retrieval.
    """
    return {
        "lat": 25.3573,
        "lon": 55.3820,
        "accuracy_meters": 100,
        "source": "stub",
    }

