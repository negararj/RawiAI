from app.agents.graph import run_demo_flow


def test_demo_flow_stub():
    result = run_demo_flow()
    assert "location" in result
    assert "qa" in result
    assert "route" in result
    assert "audio" in result

