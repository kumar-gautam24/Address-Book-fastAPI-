"""Router layer: wiring + HTTP translation.

Sync handlers (so blocking sqlite3 runs in the threadpool). No SQL, no business
rules. Simple version: catch the domain error here with try/except and raise
HTTPException. (Later refactor: move that to a global exception handler.)
"""
import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/contacts", tags=["contacts"])


# TODO (you implement):
#   POST "" -> create a contact
#       - def (SYNC), body: ContactCreate, response_model=ContactResponse, 201
#       - return service.create_contact(payload)
#
#   GET "/{contact_id}" -> fetch one
#       - def (SYNC)
#       - try:
#             return service.get_contact(contact_id)
#         except ContactNotFound:
#             raise HTTPException(status_code=404, detail=...)
