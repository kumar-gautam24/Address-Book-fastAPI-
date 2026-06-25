"""Repository layer: raw SQL only.

"""
import logging
from typing import Optional

from .database import get_connection

logger = logging.getLogger(__name__)


def create(data: dict) -> dict:
    """Insert a contact and return the created row as a dict (incl. new id).
    """

    conn= get_connection()
    try:

        cur= conn.execute(
        "INSERT INTO address_book (city,latitude,longitude) VALUES (?,?,?) RETURNING *",
        (data["city"],data["latitude"],data["longitude"]),
        )
        conn.commit()
        row= cur.fetchone()
        return dict(row)
    finally:
        conn.close()


def get_by_id(address_id: int) -> dict | None:

    conn = get_connection()
    try:
        cur= conn.execute(
        "SELECT * FROM address_book WHERE id = ?",
        (address_id,),
        )
        conn.commit()
        row= cur.fetchone()
        return dict(row) if row else None
    finally:
        conn.close()