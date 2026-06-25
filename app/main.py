"""Composition root: build the app, wire everything together. No logic here.

Run with:  uvicorn app.main:app --reload
"""
import logging

from fastapi import FastAPI

from .database import init_db
from .router import router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Address Book")

# Simple: create the table once, when the app starts up.
# (Later refactor: move this into a lifespan handler. Trade-off: this runs at
#  import time, which is fine for a small app but surprising in tests.)
init_db()

# wiring: routes live in the router module
app.include_router(router)
