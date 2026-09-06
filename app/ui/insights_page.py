"""Operator-facing insights dashboard - a separate page, not part of the
visitor-facing tab flow. Reads the in-process analytics log (see
app/analytics.py); resets when the app process restarts or redeploys."""

import reflex as rx

from app.analytics import get_insights
from app.ui.components import CARD, FONT_BODY, FONT_HEADING, GOLD, INK, INK_SOFT, LINE, RUST, TEAL, TEAL_SOFT


class InsightsState(rx.State):
    """Pulls fresh stats from the in-process analytics log on demand."""

    refresh_tick: int = 0

    def refresh(self):
        self.refresh_tick += 1

    @rx.var
    def total_visits(self) -> str:
        _ = self.refresh_tick
        return str(get_insights()["total_visits"])

    @rx.var
    def visits_by_site(self) -> list[dict[str, str]]:
        _ = self.refresh_tick
        return get_insights()["visits_by_site"]

    @rx.var
    def congestion_counts(self) -> list[dict[str, str]]:
        _ = self.refresh_tick
        return get_insights()["congestion_counts"]

    @rx.var
    def recent_questions(self) -> list[dict[str, str]]:
        _ = self.refresh_tick
        return get_insights()["recent_questions"]

    @rx.var
    def has_data(self) -> bool:
        _ = self.refresh_tick
        return get_insights()["total_visits"] > 0


def _panel(*children, **style):
    base = {
        "background": CARD,
        "border": f"1px solid {LINE}",
        "border_radius": "16px",
        "padding": "16px 18px",
        "width": "100%",
    }
    return rx.el.div(*children, style={**base, **style})


def _row_style():
    return {
        "display": "flex",
        "justify_content": "space-between",
        "padding": "8px 0",
        "border_bottom": f"1px solid {LINE}",
    }


def _site_count_row(item):
    return rx.el.div(
        rx.el.span(item["site_name"], style={"font_family": FONT_BODY, "font_size": "13px", "color": INK, "font_weight": "600"}),
        rx.el.span(item["count"], style={"font_family": FONT_BODY, "font_size": "13px", "color": TEAL, "font_weight": "700"}),
        style=_row_style(),
    )


def _level_count_row(item):
    return rx.el.div(
        rx.el.span(item["level"], style={"font_family": FONT_BODY, "font_size": "13px", "color": INK, "font_weight": "600"}),
        rx.el.span(item["count"], style={"font_family": FONT_BODY, "font_size": "13px", "color": TEAL, "font_weight": "700"}),
        style=_row_style(),
    )


def insights_index():
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                "OPERATOR VIEW",
                style={"font_family": FONT_BODY, "font_size": "11px", "font_weight": "700", "letter_spacing": "1.5px", "color": RUST, "margin": "0"},
            ),
            rx.el.h1(
                "RawiAI Insights",
                style={"font_family": FONT_HEADING, "font_size": "26px", "font_weight": "700", "color": INK, "margin": "4px 0"},
            ),
            rx.el.p(
                "Aggregated, anonymized visitor activity from this running instance. Resets on redeploy - this is a demo-scoped log, not a database.",
                style={"font_family": FONT_BODY, "font_size": "13px", "color": INK_SOFT, "margin": "0 0 16px 0", "line_height": "1.5"},
            ),
            rx.el.button(
                "Refresh",
                on_click=InsightsState.refresh,
                style={
                    "font_family": FONT_BODY,
                    "padding": "8px 16px",
                    "border_radius": "999px",
                    "border": f"1px solid {TEAL}",
                    "background": "transparent",
                    "color": TEAL,
                    "font_size": "13px",
                    "font_weight": "700",
                    "cursor": "pointer",
                    "margin_bottom": "16px",
                },
            ),
            _panel(
                rx.el.p(
                    "TOTAL COMPLETED STORIES",
                    style={"font_family": FONT_BODY, "font_size": "11px", "font_weight": "700", "color": TEAL, "letter_spacing": "0.8px", "margin": "0"},
                ),
                rx.el.p(
                    InsightsState.total_visits,
                    style={"font_family": FONT_HEADING, "font_size": "40px", "font_weight": "700", "color": INK, "margin": "4px 0 0 0"},
                ),
                background=TEAL_SOFT,
                border="none",
            ),
            rx.cond(
                InsightsState.has_data,
                rx.el.div(
                    _panel(
                        rx.el.p(
                            "VISITS BY LANDMARK",
                            style={"font_family": FONT_BODY, "font_size": "11px", "font_weight": "700", "color": GOLD, "letter_spacing": "0.8px", "margin": "0 0 6px 0"},
                        ),
                        rx.foreach(InsightsState.visits_by_site, _site_count_row),
                        margin_top="16px",
                    ),
                    _panel(
                        rx.el.p(
                            "CONGESTION SEEN",
                            style={"font_family": FONT_BODY, "font_size": "11px", "font_weight": "700", "color": GOLD, "letter_spacing": "0.8px", "margin": "0 0 6px 0"},
                        ),
                        rx.foreach(InsightsState.congestion_counts, _level_count_row),
                        margin_top="16px",
                    ),
                    _panel(
                        rx.el.p(
                            "RECENT QUESTIONS",
                            style={"font_family": FONT_BODY, "font_size": "11px", "font_weight": "700", "color": GOLD, "letter_spacing": "0.8px", "margin": "0 0 6px 0"},
                        ),
                        rx.foreach(
                            InsightsState.recent_questions,
                            lambda item: rx.el.div(
                                rx.el.p(item["site_name"], style={"font_family": FONT_BODY, "font_size": "12px", "font_weight": "700", "color": INK, "margin": "0"}),
                                rx.el.p(item["question"], style={"font_family": FONT_BODY, "font_size": "12px", "color": INK_SOFT, "margin": "2px 0 0 0"}),
                                style={"padding": "8px 0", "border_bottom": f"1px solid {LINE}"},
                            ),
                        ),
                        margin_top="16px",
                    ),
                    style={"width": "100%"},
                ),
                rx.el.p(
                    "No stories completed yet on this instance. Run a demo from the main app to see data here.",
                    style={"font_family": FONT_BODY, "font_size": "13px", "color": INK_SOFT, "text_align": "center", "padding": "24px 0"},
                ),
            ),
            style={"width": "100%", "max_width": "480px", "display": "flex", "flex_direction": "column"},
        ),
        style={
            "min_height": "100vh",
            "width": "100%",
            "display": "flex",
            "justify_content": "center",
            "background": "#F7ECD8",
            "padding": "32px 16px",
            "box_sizing": "border-box",
        },
    )
