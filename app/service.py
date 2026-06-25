"""Service layer: business rules.
"""
import logging
from pickle import EMPTY_DICT

from . import repository
from .exceptions import AddressNotFound, NoAddressFound
from .schemas import AddressCreate

logger = logging.getLogger(__name__)


def create_address(payload:AddressCreate)->dict:
    data = payload.model_dump()
    return repository.create(data)


def get_address(address_id: int)->dict:
    address= repository.get_by_id(address_id)
    if address is None:
        raise  AddressNotFound(address_id)
    else :
        return address


def update_address(address_id:int,payload:AddressCreate)->dict:
    data = payload.model_dump()
    address= repository.update_address(address_id=address_id,data=data)
    if address is None:
        raise AddressNotFound(address_id)
    else:
        return  address


def delete_address(address_id:int)->bool:
    deleted= repository.delete_address(address_id)
    if not deleted:
        raise AddressNotFound(address_id)
    return  deleted


def get_nearby_address(latitude:float,longitude:float)-> list[dict]:
    addresses= repository.get_all()
    if not addresses :
        raise NoAddressFound()
    else:
        return addresses