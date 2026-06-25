"""Domain exceptions: plain Python classes, no HTTP knowledge.

The service raises these; an app-level handler (main.py) translates them to HTTP.
"""


class ContactError(Exception):
    """Base class for all domain errors in this app."""
    pass


class ContactNotFound(ContactError):
    """Raised by the service when a requested contact does not exist.

    TODO (you implement):
      - store the missing id so the handler can build a useful message
    """
    pass
