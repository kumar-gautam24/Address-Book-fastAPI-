"""Database layer: connection management + schema initialization.

Knows nothing about HTTP, Pydantic, or business rules. Pure sqlite3.
"""
import logging
import sqlite3

logger = logging.getLogger(__name__)

DB_PATH = "database.db"


def get_connection() -> sqlite3.Connection:
    """Open a NEW sqlite3 connection with dict-like rows.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    logger.debug("Opened sqlite connection to %s", DB_PATH)
    return conn


def init_db() -> None:
    """Create the  table if it does not exist (idempotent)
    """
    conn = get_connection()
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS address_book (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT ,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()
        logger.info("Database initialized (contacts table ready)")
    finally:
        conn.close()
