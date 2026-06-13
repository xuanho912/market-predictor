from __future__ import annotations

from dataclasses import dataclass


RISK_LAYERS = ("vulnerability", "trigger", "amplifier", "confirmation")


@dataclass(frozen=True)
class Reason:
    layer: str
    feature_name: str
    direction: str
    text: str

    def __post_init__(self) -> None:
        if self.layer not in RISK_LAYERS:
            raise ValueError(f"Unknown risk layer: {self.layer}")
        if self.direction not in {"bullish", "bearish", "bounce", "crisis"}:
            raise ValueError(f"Unknown explanation direction: {self.direction}")
