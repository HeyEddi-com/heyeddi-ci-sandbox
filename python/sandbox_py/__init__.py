"""HeyEddi CI sandbox Python package."""

__version__ = "0.1.0"


def greet_user(name: str = "world") -> str:
    """Return a friendly greeting.

    Renamed from ``greet`` on purpose: callers outside this diff still import
    ``greet`` so related-context discovery must surface them.
    """
    return f"hello, {name}"
