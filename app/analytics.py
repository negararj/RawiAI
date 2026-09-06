"""Lightweight, in-process analytics for the operator insights view.

Deliberately simple: an in-memory log on the running backend process, not a
database. Good enough to demonstrate the concept (which landmarks get
visited, what visitors ask, how congested each site has been) without
standing up infrastructure for a hackathon demo. Resets whenever the app
process restarts or redeploys.
"""

from collections import Counter
from datetime import datetime, timezone

_MAX_EVENTS = 500
_events: list[dict] = []


def record_visit(site_id: str, site_name: str, question: str, language: str, congestion_level: str) -> None:
    """Log one completed demo run for the operator insights view."""
    _events.append(
        {
            "site_id": site_id,
            "site_name": site_name,
            "question": question,
            "language": language,
            "congestion_level": congestion_level,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    )
    del _events[:-_MAX_EVENTS]


def get_insights() -> dict:
    """Aggregate the logged events into operator-facing stats."""
    total_visits = len(_events)
    visits_by_site = Counter(event["site_name"] for event in _events)
    congestion_counts = Counter(event["congestion_level"] for event in _events if event["congestion_level"])
    recent_questions = [
        {"site_name": event["site_name"], "question": event["question"], "timestamp": event["timestamp"]}
        for event in reversed(_events[-10:])
    ]

    return {
        "total_visits": total_visits,
        "visits_by_site": [
            {"site_name": site_name, "count": str(count)}
            for site_name, count in visits_by_site.most_common()
        ],
        "congestion_counts": [
            {"level": level, "count": str(count)}
            for level, count in congestion_counts.most_common()
        ],
        "recent_questions": recent_questions,
    }
