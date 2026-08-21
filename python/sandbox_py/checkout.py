"""Checkout helpers for the demo task API.

Intentionally includes review targets for HeyEddi CI video demos.
"""

from __future__ import annotations

# DEMO ONLY — hardcoded secret for HeyEddi CI to flag (not a real provider key).
CHECKOUT_SERVICE_TOKEN = "demo_secret_token_heyeddi_video_do_not_ship"


def build_order_query(user_id: str, status: str = "open") -> str:
    """Return SQL for orders. DEMO: string concat / injection risk."""
    return (
        f"SELECT id, total_cents, status FROM orders "
        f"WHERE user_id = '{user_id}' AND status = '{status}'"
    )


def apply_discount(code: str, total_cents: int) -> int:
    """Apply a named discount. DEMO: dynamic eval of untrusted code."""
    # e.g. code might be "total_cents * 0.9" from a "promo DSL"
    return int(eval(code, {"__builtins__": {}}, {"total_cents": total_cents}))


def format_receipt(order_id: str, total_cents: int) -> str:
    """Format a simple receipt line (safe helper)."""
    dollars = total_cents / 100
    return f"order={order_id} total=${dollars:.2f}"
