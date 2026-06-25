"""Pydantic v2 schemas: the API contract (presentation layer).
"""


from pydantic import BaseModel, Field


class AddressCreate(BaseModel):
    """Input schema for creating a contact.


    """
    city: str
    latitude: float = Field(ge =-90,le=90)
    longitude: float= Field(ge =-180,le=180)



class AddressResponse(BaseModel):
    """Output schema returned to the client.
    """
    id:int
    city:str
    latitude:float
    longitude:float
    created_at: str
    updated_at:str

