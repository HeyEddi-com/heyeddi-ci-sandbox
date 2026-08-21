"""HeyEddi CI sandbox Python package."""

__version__ = "0.1.0"


def greet(name: str = "world") -> str:
    """Return a friendly greeting."""
    return f"hello, {name}"

from sandbox_py.checkout import (  # noqa: E402
    apply_discount,
    build_order_query,
    format_receipt,
)
