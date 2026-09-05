"""Agent that answers visitor questions from heritage content."""

from app.config import GEMINI_API_KEY
from app.rag.retrieve import retrieve_facts


def _build_prompt(question: str, language: str, facts: list[dict]) -> str:
    """Create a grounded prompt for the story guide."""
    facts_text = "\n\n".join(fact["text"] for fact in facts)
    site_name = facts[0]["site"] if facts else "the heritage site"

    return f"""
You are RawiAI, a warm heritage tour guide.

Visitor language: {language}
Current site: {site_name}
Visitor question: {question}

Use ONLY the heritage facts below.
If the facts do not contain the answer, say that you do not have enough verified information.
Do not invent dates, names, events, or historical details.

Style:
- short
- warm
- spoken like a tour guide
- easy to understand
- grounded in the facts

Heritage facts:
{facts_text}
""".strip()


def _generate_with_gemini(prompt: str) -> str:
    """Generate an answer using Gemini."""
    try:
        import google.generativeai as genai
    except ImportError as exc:
        raise RuntimeError(
            "Install Gemini support first: python -m pip install google-generativeai"
        ) from exc

    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text.strip()


def answer_question(question: str, language: str = "en") -> dict:
    """Retrieve facts and generate an answer."""
    facts = retrieve_facts(question, language=language)
    prompt = _build_prompt(question, language, facts)

    if GEMINI_API_KEY:
        answer = _generate_with_gemini(prompt)
        source = "gemini"
    else:
        answer = (
            "Gemini is not connected yet. Add GEMINI_API_KEY to your .env file. "
            f"For now, here are the verified notes I found: {facts[0]['text']}"
        )
        source = "local-fallback"

    return {
        "question": question,
        "language": language,
        "facts": facts,
        "answer": answer,
        "source": source,
    }
