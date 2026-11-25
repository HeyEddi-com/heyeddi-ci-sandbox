import sqlite3

from sandbox_py.orders import order_totals


def _conn() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE orders (id TEXT, customer_id TEXT, total_cents INTEGER)")
    conn.executemany("INSERT INTO orders VALUES (?, ?, ?)", [("a", "c1", 1200), ("b", "c2", 800)])
    return conn


def test_order_totals() -> None:
    assert order_totals(_conn(), ["a", "b"]) == {"a": 1200, "b": 800}
