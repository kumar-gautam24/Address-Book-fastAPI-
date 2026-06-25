"""Repository layer: raw SQL only.

"""
import logging

from .database import get_connection

logger = logging.getLogger(__name__)


def create(data: dict) -> dict:
    logger.info("Inserting address: city=%s lat=%s lon=%s", data["city"], data["latitude"], data["longitude"])
    conn = get_connection()
    try:
        cur = conn.execute(
            "INSERT INTO address_book (city,latitude,longitude) VALUES (?,?,?) RETURNING *",
            (data["city"], data["latitude"], data["longitude"]),
        )
        row = cur.fetchone()
        conn.commit()
        logger.info("Inserted address id=%s", row["id"])
        return dict(row)
    finally:
        conn.close()


def get_all() -> list[dict]:
    logger.info("Fetching all addresses")
    conn = get_connection()
    try:
        cur = conn.execute("SELECT * FROM address_book")
        rows = cur.fetchall()
        logger.info("Fetched %s address(es)", len(rows))
        return [dict(row) for row in rows]
    finally:
        conn.close()


def get_by_id(address_id: int) -> dict | None:
    logger.info("Fetching address id=%s", address_id)
    conn = get_connection()
    try:
        cur = conn.execute(
            "SELECT * FROM address_book WHERE id = ?",
            (address_id,),
        )
        row = cur.fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def update_address(*, address_id: int, data: dict) -> dict | None:
    logger.info("Updating address id=%s", address_id)
    conn = get_connection()
    try:
        cur = conn.execute(
            "UPDATE address_book SET city=?, latitude=?, longitude=?, updated_at=CURRENT_TIMESTAMP WHERE id=? RETURNING *",
            (data["city"], data["latitude"], data["longitude"], address_id),
        )
        row = cur.fetchone()
        conn.commit()
        return dict(row) if row else None
    finally:
        conn.close()


def delete_address(address_id: int) -> bool:
    logger.info("Deleting address id=%s", address_id)
    conn = get_connection()
    try:
        cur = conn.execute(
            "DELETE FROM address_book WHERE id = ?",
            (address_id,),
        )
        conn.commit()
        return cur.rowcount == 1
    finally:
        conn.close()
