"""Composition root: build the app, wire everything together. No logic here.

Run with:  uvicorn app.main:app --reload
"""
import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .database import init_db
from .exceptions import AddressNotFound
from .router import router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Address Book")

#handle the exceptions
@app.exception_handler(AddressNotFound)
def address_not_found_handler(_request: Request, exc: AddressNotFound):
    return JSONResponse(status_code=404,
                        content={"detail":str(exc)}
    )
# init the db
init_db()

# wiring: routes live in the router module
app.include_router(router)
