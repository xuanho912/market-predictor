from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RegimeProbability:
    up_probability: float
    down_probability: float
    sideways_probability: float


class RuleRegimeModel:
    def __init__(self, name: str, up_bias: float, down_bias: float, volatility_sensitivity: float) -> None:
        self.name = name
        self.up_bias = up_bias
        self.down_bias = down_bias
        self.volatility_sensitivity = volatility_sensitivity

    def predict(self, features: dict[str, float], horizon_scale: float = 1.0) -> RegimeProbability:
        breadth = features.get("breadth_repair", 0.5) - features.get("breadth_deterioration", 0.5)
        credit = features.get("credit_spreads", 0.5)
        volatility = features.get("vix_options_risk", features.get("volatility", 0.5))
        up = _clamp(0.34 + self.up_bias + breadth * 0.22 - credit * 0.10)
        down = _clamp(0.28 + self.down_bias + credit * 0.20 + volatility * self.volatility_sensitivity * horizon_scale)
        sideways = max(0.0, 1.0 - up - down)
        total = up + down + sideways
        return RegimeProbability(up_probability=up / total, down_probability=down / total, sideways_probability=sideways / total)


def _clamp(value: float) -> float:
    return min(max(value, 0.0), 1.0)
