# RawiAI Build Steps

This guide explains exactly what to build, in what order, and where each piece goes.

The goal is not to finish everything at once. The goal is to make the app work in small layers:

1. First with fake/stub data.
2. Then with Nokia CAMARA sandbox APIs.
3. Then with AI story generation.
4. Then with free browser voice output.
5. Then with polish for the demo.

## Step 1: Open The Project

Open this folder in VS Code:

```text
C:\Users\negar\Desktop\RawiAI
```

This is the project root.

## Step 2: Create The Python Environment

In the VS Code terminal, run:

```bash
python -m venv .venv
```

Then activate it:

```bash
.\.venv\Scripts\Activate.ps1
```

If activation fails because of PowerShell permissions, run:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then try activation again:

```bash
.\.venv\Scripts\Activate.ps1
```

## Step 3: Install Packages

Run:

```bash
pip install -r requirements.txt
```

This installs:

- Reflex for the web app.
- Nokia Network as Code SDK for CAMARA APIs.
- Qdrant client for the vector database.
- LangGraph for agents.
- Gemini for story generation.
- Browser text-to-speech for free voice.
- Pytest for tests.

## Step 4: Create Your Secret Keys File

Copy the example file:

```bash
copy .env.example .env
```

Open `.env`.

Put your real keys there:

```env
NOKIA_API_KEY=your_nokia_key_here
NOKIA_RAPIDAPI_HOST=network-as-code.nokia.rapidapi.com

GEMINI_API_KEY=your_gemini_key_here

QDRANT_URL=http://localhost:6333
```

Important: never upload `.env` to GitHub.

## Step 5: Understand The App Flow

The demo should work like this:

```text
Visitor opens RawiAI
-> CAMARA checks location / network context
-> Location Agent chooses the monument
-> Q&A Agent retrieves heritage facts
-> Gemini writes the answer or story
-> Browser text-to-speech speaks the answer
-> Route Agent checks congestion
-> CAMARA QoD is requested for smooth playback
```

## Step 6: Start With CAMARA Stubs

Open:

```text
app/camara/location.py
```

You will see:

```python
def verify_location(lat: float, lon: float, radius_meters: int) -> dict:
```

For now, this returns fake data.

This is good. Do not connect the real API yet.

First, make sure the whole app works with fake data.

## Step 7: Run The Current Tests

Run:

```bash
pytest
```

Expected result:

```text
3 tests passed
```

If tests pass, your skeleton is healthy.

## Step 8: Run The Reflex App

Run:

```bash
reflex run
```

Open the local URL Reflex gives you, usually:

```text
http://localhost:3000
```

You should see:

```text
RawiAI
Network-aware heritage storytelling
English / Arabic buttons
Question input
Start Heritage Story button
Status
Answer
Route
```

Click:

```text
Start Heritage Story
```

The app should show a placeholder answer and route.

## Step 9: Add Real Heritage Content

Open:

```text
app/content/al_hisn_fort_en.md
```

Replace the placeholder with a real English story.

Use this structure:

```markdown
# Al Hisn Fort

Al Hisn Fort is one of Sharjah's most important historic buildings...

It was used for...

One interesting detail is...

As you continue walking, notice...
```

Then open:

```text
app/content/al_hisn_fort_ar.md
```

Add the Arabic version.

Use simple, clear Arabic. It does not need to be academic.

## Step 10: Replace Retrieval Stub

Open:

```text
app/rag/retrieve.py
```

Right now, it returns this:

```python
"Placeholder fact. Replace with Qdrant search result."
```

For the first working version, replace it with content from the markdown files.

Simple version:

```python
from pathlib import Path


def retrieve_facts(query: str, language: str = "en") -> list[dict]:
    file_name = "al_hisn_fort_ar.md" if language == "ar" else "al_hisn_fort_en.md"
    content_path = Path("app/content") / file_name
    text = content_path.read_text(encoding="utf-8")

    return [
        {
            "site": "Al Hisn Fort",
            "language": language,
            "text": text,
            "query": query,
        }
    ]
```

Do this before Qdrant. It is easier and helps the demo work faster.

## Step 11: Connect Gemini

Open:

```text
app/agents/qa_agent.py
```

Find:

```python
"answer": "This is a placeholder answer. Connect Gemini here.",
```

Replace the placeholder with a Gemini call.

The Q&A Agent should receive:

```text
visitor question
language
retrieved facts
current site name
```

The answer should be:

```text
short
warm
spoken like a tour guide
grounded in the facts
```

Do not let Gemini invent historical facts. Tell it to only use the retrieved content.

## Step 12: Connect Free Browser Voice

Open:

```text
app/audio/tts.py
```

Find:

```python
def text_to_speech(text: str) -> dict:
```

We are not using ElevenLabs for the free hackathon version.

The app uses the browser's built-in Web Speech API instead.

The function should return:

```python
{
    "provider": "browser-speech-synthesis",
    "status": "ready"
}
```

The actual speaking happens in:

```text
app/ui/pages.py
```

The `Speak Story` button reads the answer text from the page and speaks it aloud.

## Step 13: CAMARA API Order

Do CAMARA in this order.

Do not start with all six APIs.

### 13.1 Location Verification

Open:

```text
app/camara/location.py
```

Replace:

```python
verify_location()
```

with the real Nokia Location Verification API.

Purpose:

```text
Prove the visitor is really near the heritage site.
```

Judges should hear:

```text
We are not only using browser GPS. We verify presence through CAMARA network APIs.
```

### 13.2 Location Retrieval

Still in:

```text
app/camara/location.py
```

Replace:

```python
get_device_location()
```

Purpose:

```text
Get approximate network-based visitor location.
```

### 13.3 Geofencing

Open:

```text
app/camara/geofencing.py
```

Replace:

```python
subscribe_geofence()
```

Purpose:

```text
When a visitor enters the site, the network can trigger the welcome experience.
```

Open:

```text
app/webhooks/geofence_events.py
```

This is where geofence events are received.

For demo day, if a public webhook is hard, simulate the event with a button.

Say clearly:

```text
The event format follows CAMARA geofencing CloudEvents; the demo uses simulator mode.
```

### 13.4 Congestion Insights

Open:

```text
app/camara/congestion.py
```

Replace:

```python
get_congestion()
```

Purpose:

```text
Detect whether an area is crowded or the network is busy.
```

Then open:

```text
app/agents/route_agent.py
```

Use the congestion result to decide:

```text
normal route
or quieter alternate route
```

### 13.5 Quality on Demand

Open:

```text
app/camara/qos.py
```

Replace:

```python
request_qos()
```

Purpose:

```text
Request better network quality for the audio storytelling session.
```

Use this right before or during audio playback.

### 13.6 Number Verification

Open:

```text
app/camara/number.py
```

Replace:

```python
verify_number()
```

Purpose:

```text
Passwordless visitor identity.
```

This is useful, but less important than location, geofencing, congestion, and QoD.

## Step 14: Connect CAMARA To The Agents

Open:

```text
app/agents/location_agent.py
```

This file already calls:

```python
get_device_location()
verify_location()
```

After you replace the stubs, this agent automatically starts using real CAMARA results.

Open:

```text
app/agents/route_agent.py
```

This file already calls:

```python
get_congestion()
```

After you replace the stub, rerouting becomes CAMARA-powered.

## Step 15: Connect Everything In The Main Flow

Open:

```text
app/agents/graph.py
```

This is the full demo pipeline:

```python
location_result = run_location_agent()
qa_result = answer_question(question)
route_result = suggest_route("al-hisn-fort")
audio_result = text_to_speech(qa_result["answer"])
```

This file is where you control the order of the demo.

For the hackathon, keep the order simple and easy to explain.

## Step 16: Improve The UI

Open:

```text
app/ui/pages.py
```

This controls what the visitor sees.

Add these visible sections:

```text
1. Welcome message
2. CAMARA status
3. Current landmark
4. Play story button
5. Ask a question box
6. Route suggestion
7. Network/QoD status
```

Open:

```text
app/ui/state.py
```

This controls what happens when buttons are clicked.

The most important function is:

```python
def start_demo(self):
```

This function should:

```text
check location
generate story
prepare browser voice
show route
show QoD status
```

## Step 17: Add PWA Install Support

Files already exist:

```text
public/manifest.json
public/service-worker.js
```

Later, connect them to Reflex so the app can be installed on a phone.

For demo day, the most important thing is:

```text
Judges open one web link.
No app store.
No big download.
```

## Step 18: Add Qdrant Later

Do not start with Qdrant first.

Once the story works from markdown files, then use Qdrant.

Open:

```text
docker-compose.yml
```

Run:

```bash
docker compose up qdrant
```

Then open:

```text
app/rag/ingest.py
```

This file should:

```text
read markdown files
split content into chunks
create embeddings
store chunks in Qdrant
```

Then open:

```text
app/rag/retrieve.py
```

This file should:

```text
search Qdrant
return the most relevant heritage facts
```

## Step 19: What Each Person Should Do

### Sarah: CAMARA APIs

Work in:

```text
app/camara/
app/webhooks/
```

Start with:

```text
location.py
geofencing.py
congestion.py
qos.py
```

### Negar: AI Agents

Work in:

```text
app/agents/
app/rag/
```

Start with:

```text
qa_agent.py
graph.py
retrieve.py
```

### Botheina: Frontend / PWA

Work in:

```text
app/ui/
public/
```

Start with:

```text
pages.py
state.py
components.py
manifest.json
```

### Yasmeen: Architecture / Integration

Work in:

```text
README.md
BUILD_STEPS.md
docker-compose.yml
.env.example
```

Also make sure all parts connect.

### Sadaf: Content / Pitch

Work in:

```text
app/content/
```

Start with:

```text
al_hisn_fort_en.md
al_hisn_fort_ar.md
demo_questions.md
```

Also own the Amina demo story.

## Step 20: Demo Checklist

Before judging, make sure this works:

```text
Open web link
Click Start Heritage Story
Show CAMARA location status
Show landmark name
Generate story
Click Speak Story
Ask one question
Show congestion route change
Show QoD status
```

Also record a backup video.

Network demos can fail during judging, even when the code is good.

## Step 21: What To Say About CAMARA

Use this simple explanation:

```text
RawiAI uses Nokia Network as Code CAMARA APIs as the trust and network intelligence layer.

Location Verification confirms that the visitor is really near the monument.
Geofencing lets the network trigger the welcome moment.
Congestion Insights helps the Route Agent avoid crowded or degraded areas.
Quality on Demand supports smoother audio storytelling.
Number Verification can make sign-in passwordless.

The AI is not guessing context. It receives verified network context from CAMARA, then creates the right story for the right place.
```
