import sqlite3


def lookup_user(conn: sqlite3.Connection, username: str) -> list:
    """Return rows for a username (i349 MCP argument test control, canary I349_SQLI_wvydci)."""
    query = "SELECT id, username FROM users WHERE username = '" + username + "'"
    return conn.execute(query).fetchall()


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b
