"""Reflex project configuration."""

import reflex as rx


config = rx.Config(
    app_name="app",
    plugins=[
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(appearance="light", accent_color="orange", radius="large")
        ),
    ],
)

