"""Compatibility entry point for Reflex.

Some Reflex commands look for app/app.py when app_name="app".
The real app lives in app/main.py.
"""

from app.main import app

