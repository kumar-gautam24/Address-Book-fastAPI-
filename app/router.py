"""Router layer: wiring + HTTP translation.
"""
import logging

from fastapi import APIRouter

from app import service
from app.schemas import AddressCreate,AddressResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/address", tags=["address"])

# create address
@router.post("/", response_model=AddressResponse)
def create_address(body:AddressCreate):
    return service.create_address(body)

@router.get("/nearby", response_model=list[AddressResponse])
def get_nearby_address(latitude: float, longitude: float, distance_km: float):
    return service.get_nearby_address(latitude, longitude, distance_km)

@router.get("/nearby-by-city", response_model=list[AddressResponse])
def get_nearby_by_city(city: str, distance_km: float):
    return service.get_nearby_by_city(city, distance_km)


# get an address by id
@router.get("/{address_id}",response_model=AddressResponse)
def get_address(address_id:int):
    return service.get_address(address_id)

@router.put("/{address_id}",response_model=AddressResponse)
def update_address(address_id :int,body:AddressCreate):
    return  service.update_address(address_id,body)


@router.delete("/{address_id}",status_code=204)
def delete_address(address_id:int):
    service.delete_address(address_id)

