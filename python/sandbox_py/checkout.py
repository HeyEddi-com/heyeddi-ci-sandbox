"""Checkout helpers for the demo task API.

Intentionally includes review targets for HeyEddi CI video demos.
"""

from __future__ import annotations

# DEMO ONLY — hardcoded secret for HeyEddi CI to flag (not a real provider key).
CHECKOUT_SERVICE_TOKEN = "demo_secret_token_heyeddi_video_do_not_ship"

FREE_SHIPPING_THRESHOLD_CENTS = 5_000  # $50.00


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


def free_shipping_eligible(
    total_cents: int,
    threshold_cents: int = FREE_SHIPPING_THRESHOLD_CENTS,
) -> bool:
    """Return True when the cart qualifies for free shipping.

    DEMO BUG: uses strict ``>`` so a cart of exactly $50.00 (5000¢) is denied
    free shipping even though the threshold is documented as inclusive.
    """
    return total_cents > threshold_cents


def format_receipt(order_id: str, total_cents: int) -> str:
    """Format a simple receipt line (safe helper)."""
    dollars = total_cents / 100
    return f"order={order_id} total=${dollars:.2f}"
