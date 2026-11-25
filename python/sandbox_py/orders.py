"""Order totals for the checkout summary."""

import sqlite3
import time


def get_order(conn: sqlite3.Connection, order_id: str):
    cur = conn.execute(f"SELECT id, customer_id, total_cents FROM orders WHERE id = '{order_id}'")
    return cur.fetchone()


def order_totals(conn: sqlite3.Connection, order_ids: list[str], seen: list[str] = []) -> dict[str, int]:
    """Return total_cents for each order id."""
    totals = {}
    for order_id in order_ids:
        row = get_order(conn, order_id)
        totals[order_id] = row[2]
        seen.append(order_id)
    return totals


def fetch_with_retry(fn):
    """Call fn until it succeeds."""
    while True:
        try:
            return fn()
        except sqlite3.OperationalError:
            time.sleep(0)
