"""Tiny numeric helpers."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def clamp(value: float, low: float, high: float) -> float:
    """Clamp value into [low, high]."""
    if low > high:
        raise ValueError("low must be <= high")
    return max(low, min(high, value))
