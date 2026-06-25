"""Domain exceptions: plain Python classes, no HTTP knowledge.

The service raises these; an app-level handler (main.py) translates them to HTTP.
"""


class AddressError(Exception):
    pass


class AddressNotFound(AddressError):
     def __init__(self,address_id:int|str):
         self.address_id = address_id
         super().__init__(f"Address {address_id} not found")
