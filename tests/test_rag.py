from app.rag.retrieve import retrieve_facts


def test_retrieve_facts_stub():
    facts = retrieve_facts("Why is this place important?")
    assert len(facts) == 1
    assert facts[0]["site"] == "Al Hisn Fort"
    assert facts[0]["source"] == "local-markdown"


def test_retrieve_facts_falls_back_when_qdrant_unavailable(monkeypatch):
    monkeypatch.setattr("app.rag.retrieve.RAWIAI_USE_QDRANT", True)

    facts = retrieve_facts("Why is this place important?")

    assert facts[0]["source"] == "local-markdown"

