"""Repository layer: raw SQL only.

"""
import logging

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

        row= cur.fetchone()
        conn.commit()
        return dict(row)
    finally:
        conn.close()


def get_all()-> list[dict] :
    conn = get_connection()
    try:
        cur = conn.execute(
        "SELECT * FROM address_book",
        )
        rows = cur.fetchall()
        return  [dict(row) for row in rows]
    finally:
        conn.close()




def get_by_id(address_id: int) -> dict | None:

    conn = get_connection()
    try:
        cur= conn.execute(
        "SELECT * FROM address_book WHERE id = ?",
        (address_id,),
        )

        row= cur.fetchone()

        logger.info(row)
        return dict(row) if row else None
    finally:
        conn.close()

def update_address(*,address_id:int,data:dict)->dict|None:
    conn = get_connection()
    try:
        cur= conn.execute(
            "UPDATE address_book SET city=?,latitude=?,longitude=?,updated_at=CURRENT_TIMESTAMP WHERE id =? RETURNING *",
            (data["city"],data["latitude"],data["longitude"],address_id)
        )
        row= cur.fetchone()
        conn.commit()
        return dict(row) if row else None

    finally:
        conn.close()


def delete_address(address_id:int)->bool:
    conn =  get_connection()
    try:
        cur = conn.execute(
            "DELETE FROM address_book WHERE id = ?",
            (address_id,)
        )
        conn.commit()
        return  cur.rowcount== 1
    finally:
        conn.close()
