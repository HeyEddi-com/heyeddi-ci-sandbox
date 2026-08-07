"""HeyEddi CI sandbox Python package."""

__version__ = "0.1.0"


def greet(name: str = "world") -> str:
    """Return a friendly greeting."""
    return f"hello, {name}"

from .health import HealthStatus, check_health

__all__ = ["greet", "HealthStatus", "check_health"]
