from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class Driver(BaseModel):
    name: str
    group: str
    contribution: float


class HorizonForecast(BaseModel):
    horizon: str
    up_probability: float = Field(ge=0.0, le=1.0)
    down_probability: float = Field(ge=0.0, le=1.0)
    sideways_probability: float = Field(ge=0.0, le=1.0)
    expected_return: float
    max_upside_p50: float
    max_downside_p50: float
    confidence: float = Field(ge=0.0, le=1.0)


class TopReason(BaseModel):
    title: str
    layer: str
    direction: str
    evidence: str
    contribution: float


class SimilarDay(BaseModel):
    date: str
    similarity: float = Field(ge=0.0, le=1.0)
    regime: str
    forward_20d_return: float
    max_drawdown_20d: float


class RiskSource(BaseModel):
    source: str
    score: float = Field(ge=0.0, le=100.0)
    contribution: float
    evidence: str


class LongTermVulnerabilityOutput(BaseModel):
    financial_system_vulnerability_score: float = Field(ge=0.0, le=100.0)
    crisis_probability_12m: float = Field(ge=0.0, le=1.0)
    most_vulnerable_sectors: list[str]


class MediumTermPullbackOutput(BaseModel):
    max_drawdown_probability_20d: float = Field(ge=0.0, le=1.0)
    max_drawdown_probability_60d: float = Field(ge=0.0, le=1.0)
    expected_drawdown: float
    risk_source_breakdown: list[RiskSource]


class ShortTermTriggerOutput(BaseModel):
    sharp_drop_probability: float = Field(ge=0.0, le=1.0)
    sharp_rebound_probability: float = Field(ge=0.0, le=1.0)
    intraday_range: tuple[float, float]
    key_trigger_levels: list[float]


class BottomBounceOutput(BaseModel):
    bounce_probability_10d: float = Field(ge=0.0, le=1.0)
    bounce_probability_20d: float = Field(ge=0.0, le=1.0)
    is_dead_cat_bounce: bool
    may_form_medium_term_bottom: bool


class LayeredModelOutputs(BaseModel):
    long_term_vulnerability: LongTermVulnerabilityOutput
    medium_term_pullback: MediumTermPullbackOutput
    short_term_trigger: ShortTermTriggerOutput
    bottom_bounce: BottomBounceOutput


class PredictionSnapshot(BaseModel):
    forecast_timestamp: datetime
    symbol: str
    market_regime: str
    model_version: str
    feature_snapshot_version: str
    horizons: list[HorizonForecast]
    pullback_risk_score: float = Field(ge=0.0, le=100.0)
    crisis_risk_score: float = Field(ge=0.0, le=100.0)
    bounce_probability: float = Field(ge=0.0, le=1.0)
    bounce_quality_score: float = Field(ge=0.0, le=100.0)
    downside_continuation_probability: float = Field(ge=0.0, le=1.0)
    trend_reversal_probability: float = Field(ge=0.0, le=1.0)
    dead_cat_bounce_risk: float = Field(ge=0.0, le=1.0)
    top_reasons: list[TopReason]
    historical_similar_days: list[SimilarDay]
    risk_source_breakdown: list[RiskSource]
    model_layers: LayeredModelOutputs


class FeatureSnapshot(BaseModel):
    symbol: str
    as_of: datetime
    market_regime: str
    features: dict[str, float]
    point_in_time_safe: bool


class BacktestSummary(BaseModel):
    symbol: str
    validation_method: str
    point_in_time_data: bool
    macro_release_aligned: bool
    random_split_used: bool
    calibration_metrics: dict[str, float]
    classification_metrics: dict[str, float]
    regime_metrics: dict[str, dict[str, float]]
    cost_assumptions: dict[str, float | str]
    imbalance_policy: str
