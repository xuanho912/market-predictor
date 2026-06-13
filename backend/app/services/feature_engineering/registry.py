from __future__ import annotations

from dataclasses import dataclass


FEATURE_GROUPS = (
    "price",
    "volatility",
    "credit",
    "rates",
    "liquidity",
    "macro",
    "earnings",
    "positioning",
    "breadth",
    "news_text",
    "onchain_crypto",
    "alternative_data",
)

FEATURE_TRANSFORMS = (
    "level",
    "change",
    "acceleration",
    "percentile",
    "cross_signal",
    "divergence",
)


@dataclass(frozen=True)
class FeatureSpec:
    name: str
    group: str
    source: str
    frequency: str
    transform: str
    lag_policy: str
    missing_value_policy: str

    def __post_init__(self) -> None:
        if self.group not in FEATURE_GROUPS:
            raise ValueError(f"Unknown feature group: {self.group}")
        if self.transform not in FEATURE_TRANSFORMS:
            raise ValueError(f"Unknown feature transform: {self.transform}")
        if not self.name.startswith(f"{self.group}__"):
            raise ValueError("Feature names must start with '<group>__'.")
