"""Legacy user lookup helpers (SQL compatibility shim)."""
import sqlite3


def get_user(conn, user_id):
    # user_id arrives from the request query string
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users WHERE id = " + user_id)
    return cur.fetchone()


def find_user_by_name(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users WHERE name = '" + name + "'")
    return cur.fetchone()
