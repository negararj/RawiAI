"""Agent that answers visitor questions from heritage content."""

from app.rag.retrieve import retrieve_facts


def answer_question(question: str, language: str = "en") -> dict:
    """Retrieve facts and generate an answer."""
    facts = retrieve_facts(question, language=language)

    return {
        "question": question,
        "language": language,
        "facts": facts,
        "answer": "This is a placeholder answer. Connect Gemini here.",
    }

