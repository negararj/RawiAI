from app.agents.graph import run_demo_flow


def test_demo_flow_stub(monkeypatch):
    monkeypatch.setattr("app.agents.qa_agent.RAWIAI_USE_GEMINI", False)
    monkeypatch.setattr("app.agents.qa_agent.GEMINI_API_KEY", "")
    monkeypatch.setattr("app.agents.graph.RAWIAI_USE_GEMINI", False)
    monkeypatch.setattr("app.agents.graph.GEMINI_API_KEY", "")
    monkeypatch.setattr("app.camara.location.NOKIA_API_KEY", "")
    monkeypatch.setattr("app.camara.location.NOKIA_TEST_PHONE_NUMBER", "")
    monkeypatch.setattr("app.camara.congestion.NOKIA_API_KEY", "")
    monkeypatch.setattr("app.camara.congestion.NOKIA_TEST_PHONE_NUMBER", "")
    monkeypatch.setattr("app.camara.number.NOKIA_API_KEY", "")
    monkeypatch.setattr("app.camara.sim_swap.NOKIA_API_KEY", "")
    monkeypatch.setattr("app.camara.qos.NOKIA_API_KEY", "")
    monkeypatch.setattr("app.camara.qos.NOKIA_TEST_PHONE_NUMBER", "")

    result = run_demo_flow()
    assert "identity" in result
    assert result["language"] == "en"
    assert "location" in result
    assert "qa" in result
    assert "route" in result
    assert "audio" in result
    assert "qos" in result
    assert "timeline" in result
    assert result["summary"].startswith("RawiAI found")
    assert "Geofencing" in result["camara_calls"]
    assert "SIM Swap" in result["camara_calls"]
    assert "sim_swap" in result
    assert result["location"]["near_monument"] == "Al Hisn Fort"

    steps = [item["step"] for item in result["timeline"]]
    assert "Agent Decision" in steps
    decision_step = next(item for item in result["timeline"] if item["step"] == "Agent Decision")
    assert decision_step["source"] == "local-fallback-decision"
