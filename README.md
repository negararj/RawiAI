# RawiAI

RawiAI is a Nokia Hackathon demo for network-aware heritage storytelling.

The app uses Nokia Network as Code / CAMARA APIs as the main technical layer:

- Location Verification
- Location Retrieval
- Geofencing
- Number Verification
- Congestion Insights
- Quality on Demand

## 1. Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Copy the environment file:

```bash
copy .env.example .env
```

Add your real Nokia and Gemini keys to `.env`.

## 2. Run Qdrant

```bash
docker compose up qdrant
```

## 3. Run the app

```bash
reflex run
```

## 4. Team responsibilities

Track 1 owns `app/camara/`.

Track 2 owns `app/agents/` and `app/rag/`.

Track 3 owns `app/ui/` and `public/`.

Track 4 owns integration, `.env.example`, deployment, and `docker-compose.yml`.

Track 5 owns `app/content/`, the demo script, and the pitch.

## 5. Important rule

Start with stubs, then replace one stub at a time with the real API call.

Do not connect everything at once. Test each CAMARA function alone first.
