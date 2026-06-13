from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


@dataclass(frozen=True)
class MarketDataPoint:
    symbol: str
    field: str
    value: float | str
    observation_timestamp: datetime
    release_timestamp: datetime
    known_at_timestamp: datetime
    source: str


class PointInTimeProvider(Protocol):
    name: str

    def fetch(self, symbol: str, as_of: datetime) -> list[MarketDataPoint]:
        """Return records known at or before `as_of`."""
