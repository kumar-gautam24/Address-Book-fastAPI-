"""Service layer: business rules.
"""
import logging
import math

from . import repository
from .exceptions import AddressNotFound
from .schemas import AddressCreate

logger = logging.getLogger(__name__)


def create_address(payload: AddressCreate) -> dict:
    data = payload.model_dump()
    address = repository.create(data)
    logger.info("Created address id=%s city=%s", address["id"], address["city"])
    return address


def get_address(address_id: int) -> dict:
    logger.info("Fetching address id=%s", address_id)
    address = repository.get_by_id(address_id)
    if address is None:
        logger.warning("Address id=%s not found", address_id)
        raise AddressNotFound(address_id)
    return address


def update_address(address_id: int, payload: AddressCreate) -> dict:
    logger.info("Updating address id=%s", address_id)
    data = payload.model_dump()
    address = repository.update_address(address_id=address_id, data=data)
    if address is None:
        logger.warning("Address id=%s not found for update", address_id)
        raise AddressNotFound(address_id)
    logger.info("Updated address id=%s", address_id)
    return address


def delete_address(address_id: int) -> None:
    logger.info("Deleting address id=%s", address_id)
    deleted = repository.delete_address(address_id)
    if not deleted:
        logger.warning("Address id=%s not found for deletion", address_id)
        raise AddressNotFound(address_id)
    logger.info("Deleted address id=%s", address_id)


def _haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Return the great-circle distance in km between two lat/lon points."""
    R = 6371  # Earth radius in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return R * 2 * math.asin(math.sqrt(a))


def get_nearby_address(latitude: float, longitude: float, distance_km: float) -> list[dict]:
    logger.info("Searching addresses within %.2fkm of (%.4f, %.4f)", distance_km, latitude, longitude)
    addresses = repository.get_all()
    results = [
        a for a in addresses
        if _haversine_km(latitude, longitude, a["latitude"], a["longitude"]) <= distance_km
    ]
    logger.info("Found %s address(es) within %.2fkm", len(results), distance_km)
    return results
