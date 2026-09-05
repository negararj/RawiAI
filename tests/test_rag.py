from app.rag.retrieve import retrieve_facts


def test_retrieve_facts_stub():
    facts = retrieve_facts("Why is this place important?")
    assert len(facts) == 1
    assert facts[0]["site"] == "Al Hisn Fort"

