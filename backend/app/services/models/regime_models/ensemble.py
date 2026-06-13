from __future__ import annotations

from dataclasses import dataclass

from app.services.models.regime_models.base import RegimeProbability, RuleRegimeModel
from app.services.models.regime_models.bear_model import bear_model
from app.services.models.regime_models.bull_model import bull_model
from app.services.models.regime_models.high_vol_model import high_vol_model
from app.services.models.regime_models.panic_model import panic_model
from app.services.models.regime_models.recovery_model import recovery_model


REGIME_MODEL_MAP: dict[str, RuleRegimeModel] = {
    "bull_market": bull_model,
    "bull_trend": bull_model,
    "bear_market": bear_model,
    "bear_trend": bear_model,
    "panic": panic_model,
    "crisis": panic_model,
    "crisis_mode": panic_model,
    "recovery": recovery_model,
    "bottoming": recovery_model,
    "oversold_bounce": recovery_model,
    "high_volatility": high_vol_model,
    "liquidity_crunch": high_vol_model,
    "credit_stress": high_vol_model,
}


@dataclass(frozen=True)
class RegimeEnsemblePrediction:
    selected_model: str
    up_probability: float
    down_probability: float
    sideways_probability: float


def predict_regime_ensemble(features: dict[str, float], regime: str, horizon_scale: float = 1.0) -> RegimeEnsemblePrediction:
    model = REGIME_MODEL_MAP.get(regime, bear_model if features.get("credit_spreads", 0.0) > 0.65 else bull_model)
    selected = model.predict(features, horizon_scale=horizon_scale)
    fallback = _blend_fallback(features, horizon_scale)
    up = 0.70 * selected.up_probability + 0.30 * fallback.up_probability
    down = 0.70 * selected.down_probability + 0.30 * fallback.down_probability
    sideways = max(0.0, 1.0 - up - down)
    total = up + down + sideways
    return RegimeEnsemblePrediction(
        selected_model=model.name,
        up_probability=up / total,
        down_probability=down / total,
        sideways_probability=sideways / total,
    )


def _blend_fallback(features: dict[str, float], horizon_scale: float) -> RegimeProbability:
    up = max(0.0, min(1.0, 0.42 + features.get("breadth_repair", 0.5) * 0.15 - features.get("credit_spreads", 0.5) * 0.08))
    down = max(
        0.0,
        min(
            1.0,
            0.25
            + features.get("credit_spreads", 0.5) * 0.18
            + features.get("vix_options_risk", 0.5) * 0.10 * horizon_scale
            + features.get("breadth_deterioration", 0.5) * 0.10,
        ),
    )
    sideways = max(0.0, 1.0 - up - down)
    total = up + down + sideways
    return RegimeProbability(up_probability=up / total, down_probability=down / total, sideways_probability=sideways / total)
