"""Agent that answers visitor questions from heritage content."""

from functools import lru_cache

from app.agents.sites import DEFAULT_SITE_ID
from app.config import GEMINI_API_KEY, GEMINI_MODEL, RAWIAI_USE_GEMINI
from app.rag.retrieve import retrieve_facts


def _fallback_answer(facts: list[dict]) -> str:
    """Return a safe local answer when Gemini is unavailable."""
    if not facts:
        return "I do not have enough verified heritage information yet."

    return facts[0]["text"]


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


@lru_cache(maxsize=256)
def _generate_with_gemini(prompt: str) -> str:
    """Generate an answer using Gemini.

    Cached on the exact prompt: the demo mostly asks the same handful of
    questions per site/language, and Gemini's free tier caps at a small
    number of requests per day, so repeat demo runs would otherwise burn
    quota re-generating an answer that was already produced. A failed
    call raises and is never cached, so a transient rate limit still
    retries on the next attempt.
    """
    try:
        from google import genai
    except ImportError as exc:
        raise RuntimeError(
            "Install Gemini support first: python -m pip install google-genai"
        ) from exc

    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    text = getattr(response, "text", "") or ""
    return text.strip()


def answer_question(question: str, language: str = "en", site_id: str = DEFAULT_SITE_ID) -> dict:
    """Retrieve facts and generate an answer."""
    facts = retrieve_facts(question, language=language, site_id=site_id)
    prompt = _build_prompt(question, language, facts)

    if RAWIAI_USE_GEMINI and GEMINI_API_KEY:
        try:
            answer = _generate_with_gemini(prompt)
            source = f"gemini:{GEMINI_MODEL}"
        except Exception as exc:
            answer = _fallback_answer(facts)
            source = f"local-fallback-gemini-error:{exc.__class__.__name__}"
    else:
        answer = _fallback_answer(facts)
        source = "local-fallback"

    return {
        "question": question,
        "language": language,
        "facts": facts,
        "answer": answer,
        "source": source,
    }
