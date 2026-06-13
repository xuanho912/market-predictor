from __future__ import annotations

from dataclasses import dataclass


RETURN_HORIZONS = (1, 3, 5, 10, 20, 60)
MANDATORY_LABELS = (
    *(f"future_return_{h}d" for h in RETURN_HORIZONS),
    "trend_label",
    "pullback_5d",
    "pullback_20d",
    "pullback_60d",
    "downside_continuation_10d",
    "downside_continuation_20d",
    "bounce_5d",
    "bounce_10d",
    "bounce_20d",
    "trend_reversal_20d",
    "trend_reversal_60d",
    "crash_risk_60d",
    "crash_risk_120d",
    "systemic_crisis_180d",
)


@dataclass(frozen=True)
class LabelSpec:
    name: str
    horizon_days: int
    threshold: float | None
    version: str
    description: str

    def __post_init__(self) -> None:
        if self.name not in MANDATORY_LABELS:
            raise ValueError(f"Label is not in mandatory market-prediction set: {self.name}")


def future_return(current_close: float, future_close: float) -> float:
    if current_close <= 0:
        raise ValueError("current_close must be positive")
    return future_close / current_close - 1.0


def drawdown(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    peak = values[0]
    max_drawdown = 0.0
    for value in values:
        peak = max(peak, value)
        max_drawdown = min(max_drawdown, value / peak - 1.0)
    return max_drawdown
