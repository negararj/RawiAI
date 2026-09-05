"""CAMARA Number Verification wrapper."""


def verify_number(phone_number: str) -> dict:
    """Verify the visitor phone number without an SMS code.

    CAMARA capability: Number Verification.
    """
    return {
        "phone_number": phone_number,
        "verified": False,
        "source": "stub",
    }

