"""Service layer: business rules.

Decides what 'missing' means (raises domain errors), maps repo dicts ->
ContactResponse. No SQL, no HTTP here.
"""
import logging

from . import repository
from .exceptions import ContactNotFound

logger = logging.getLogger(__name__)


def create_contact(payload):
    """Create a contact.

    TODO (you implement):
      - decide what `payload` is (ContactCreate) and turn it into a dict for the repo
      - row = repository.create(...)
      - return ContactResponse(**row)
    """
    raise NotImplementedError


def get_contact(contact_id: int):
    """Fetch one contact by id.

    TODO (you implement):
      - row = repository.get_by_id(contact_id)
      - if row is None: raise ContactNotFound(contact_id)   # the business decision
      - return ContactResponse(**row)
    """
    raise NotImplementedError
