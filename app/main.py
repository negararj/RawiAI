"""Reflex app entry point."""

import reflex as rx

from app.ui.pages import index


app = rx.App()
app.add_page(index, route="/", title="RawiAI")

