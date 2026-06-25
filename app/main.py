"""Composition root: build the app, wire everything together. No logic here.

Run with:  uvicorn app.main:app --reload
"""
import logging

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from .database import init_db
from .exceptions import AddressNotFound
from .router import router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Address Book")

#handle the exceptions
@app.exception_handler(AddressNotFound)
def address_not_found_handler(request:Request,exc:AddressNotFound):
    return JSONResponse(status_code=404,
                        content={"detail":str(exc)}
    )
@app.exception_handler(NoAddressFound)
def address_not_found_handler(request:Request,exc:NoAddressFound):
    return JSONResponse(status_code=200,
                        content={"Message": "No Nearby address found"})
# init the db
init_db()

# wiring: routes live in the router module
app.include_router(router)
