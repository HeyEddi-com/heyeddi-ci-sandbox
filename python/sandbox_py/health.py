"""Simple health check helpers for the sandbox API surface."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(frozen=True)
class HealthStatus:
    status: str
    checked_at: str
    version: str


def check_health(version: str = "0.1.0") -> HealthStatus:
    """Return an OK health payload with a UTC timestamp."""
    return HealthStatus(
        status="ok",
        checked_at=datetime.now(UTC).isoformat(),
        version=version,
    )
