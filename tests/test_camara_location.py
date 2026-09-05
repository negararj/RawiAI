from app.camara.location import get_device_location, verify_location


def test_get_device_location_stub(monkeypatch):
    monkeypatch.setattr("app.camara.location.NOKIA_API_KEY", "")
    monkeypatch.setattr("app.camara.location.NOKIA_TEST_PHONE_NUMBER", "")

    result = get_device_location()
    assert result["source"] == "demo-camara-location-retrieval"


def test_verify_location_stub(monkeypatch):
    monkeypatch.setattr("app.camara.location.NOKIA_API_KEY", "")
    monkeypatch.setattr("app.camara.location.NOKIA_TEST_PHONE_NUMBER", "")

    result = verify_location(25.3573, 55.3820, 150)
    assert result["source"] == "demo-camara-location-verification"
