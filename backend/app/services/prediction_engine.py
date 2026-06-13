from __future__ import annotations

import hashlib
import math
from datetime import datetime, timedelta, timezone

from app.schemas.predictions import (
    FeatureSnapshot,
    HorizonForecast,
    LayeredModelOutputs,
    PredictionSnapshot,
    RiskSource,
    SimilarDay,
    TopReason,
)
from app.services.models.layers import (
    bottom_bounce_model,
    clamp01,
    long_term_vulnerability_model,
    medium_term_pullback_model,
    short_term_trigger_model,
)
from app.services.models.regime_models import predict_regime_ensemble
from app.services.signals.regime import MarketRegime, classify_rule_based_regime
from app.services.signals.risk_score import (
    ScoreInputs,
    bounce_quality_score,
    compute_core_scores,
    crisis_risk_score,
    pullback_risk_score,
)


SUPPORTED_SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
HORIZONS = ("1d", "3d", "5d", "10d", "20d", "60d")


def _seed(symbol: str) -> float:
    digest = hashlib.sha256(symbol.upper().encode("utf-8")).hexdigest()
    return int(digest[:8], 16) / 0xFFFFFFFF


def _wave(symbol: str, offset: float) -> float:
    return clamp01(0.5 + 0.35 * math.sin(_seed(symbol) * 7.0 + offset))


def latest_features(symbol: str) -> FeatureSnapshot:
    symbol = normalize_symbol(symbol)
    now = datetime.now(timezone.utc)
    values = {
        "valuation_overheat": _wave(symbol, 0.1),
        "momentum_extension": _wave(symbol, 0.7),
        "breadth_deterioration": _wave(symbol, 1.3),
        "vix_options_risk": _wave(symbol, 2.0),
        "positioning_crowding": _wave(symbol, 2.6),
        "rates_up": _wave(symbol, 3.2),
        "dollar_strength": _wave(symbol, 3.8),
        "earnings_downgrades": _wave(symbol, 4.4),
        "news_event_risk": _wave(symbol, 5.0),
        "credit_gdp_gap": _wave(symbol, 5.6),
        "credit_spreads": _wave(symbol, 6.2),
        "bank_stress": _wave(symbol, 6.8),
        "funding_market_stress": _wave(symbol, 7.4),
        "nonbank_leverage": _wave(symbol, 8.0),
        "dollar_liquidity": _wave(symbol, 8.6),
        "macro_recession_risk": _wave(symbol, 9.2),
        "policy_response_lag": _wave(symbol, 9.8),
        "real_estate_pressure": _wave(symbol, 10.4),
        "gamma_risk": _wave(symbol, 11.0),
        "zero_dte_risk": _wave(symbol, 11.6),
        "order_book_thinness": _wave(symbol, 12.2),
        "vol_term_structure_stress": _wave(symbol, 12.8),
        "premarket_strength": _wave(symbol, 13.4),
        "short_covering_pressure": _wave(symbol, 14.0),
        "drawdown_depth": _wave(symbol, 14.6),
        "panic_extreme": _wave(symbol, 15.2),
        "volume_expansion": _wave(symbol, 15.8),
        "breadth_repair": _wave(symbol, 16.4),
        "credit_spread_stabilization": _wave(symbol, 17.0),
        "vix_reversal": _wave(symbol, 17.6),
        "policy_liquidity_improvement": _wave(symbol, 18.2),
        "bad_news_resilience": _wave(symbol, 18.8),
    }
    regime = classify_rule_based_regime(
        trend_score=values["momentum_extension"] - values["breadth_deterioration"],
        breadth_score=values["breadth_repair"] - values["breadth_deterioration"],
        credit_stress=values["credit_spreads"],
        liquidity_stress=values["funding_market_stress"],
        volatility_stress=values["vix_options_risk"],
        bank_relative_strength=0.5 - values["bank_stress"],
    )
    return FeatureSnapshot(
        symbol=symbol,
        as_of=now,
        market_regime=regime.value,
        features=values,
        point_in_time_safe=True,
    )


def normalize_symbol(symbol: str) -> str:
    normalized = symbol.upper().strip()
    if normalized not in SUPPORTED_SYMBOLS:
        raise ValueError(f"Unsupported symbol: {symbol}. Supported: {', '.join(SUPPORTED_SYMBOLS)}")
    return normalized


def _horizon_forecasts(features: dict[str, float], pullback_score: float, crisis_score: float, regime: MarketRegime) -> list[HorizonForecast]:
    forecasts: list[HorizonForecast] = []
    for index, horizon in enumerate(HORIZONS, start=1):
        horizon_scale = index / len(HORIZONS)
        regime_prediction = predict_regime_ensemble(features, regime.value, horizon_scale=horizon_scale)
        down = clamp01(
            0.50 * regime_prediction.down_probability
            + 0.50 * (0.15 + pullback_score / 180.0 * horizon_scale + crisis_score / 260.0 * horizon_scale)
        )
        up = clamp01(
            0.55 * regime_prediction.up_probability
            + 0.45 * (0.62 - down * 0.45 + features["breadth_repair"] * 0.12 + features["policy_liquidity_improvement"] * 0.08)
        )
        if regime in {MarketRegime.CRISIS_MODE, MarketRegime.CREDIT_STRESS, MarketRegime.LIQUIDITY_CRUNCH}:
            up = clamp01(up - 0.12 * horizon_scale)
            down = clamp01(down + 0.12 * horizon_scale)
        sideways = max(0.0, 1.0 - up - down)
        total = up + down + sideways
        up, down, sideways = up / total, down / total, sideways / total
        expected_return = round((up - down) * 0.012 * index, 4)
        forecasts.append(
            HorizonForecast(
                horizon=horizon,
                up_probability=round(up, 4),
                down_probability=round(down, 4),
                sideways_probability=round(sideways, 4),
                expected_return=expected_return,
                max_upside_p50=round(abs(expected_return) + 0.008 * index, 4),
                max_downside_p50=round(-(abs(expected_return) + 0.010 * index + down * 0.025), 4),
                confidence=round(clamp01(0.45 + abs(up - down) * 0.55), 4),
            )
        )
    return forecasts


def _top_reasons(features: dict[str, float]) -> list[TopReason]:
    reason_specs = [
        ("Credit spreads", "confirmation", "bearish", "credit spreads and high-yield stress are elevated", features["credit_spreads"]),
        ("Market breadth", "confirmation", "bearish", "breadth deterioration weakens trend quality", features["breadth_deterioration"]),
        ("Positioning", "amplifier", "bearish", "crowded positioning can amplify de-risking", features["positioning_crowding"]),
        ("Credit stabilization", "confirmation", "bounce", "credit spread stabilization improves bounce quality", features["credit_spread_stabilization"]),
        ("Bad-news resilience", "trigger", "bullish", "price resilience to negative news supports bottoming probability", features["bad_news_resilience"]),
    ]
    return [
        TopReason(title=title, layer=layer, direction=direction, evidence=evidence, contribution=round(contribution, 3))
        for title, layer, direction, evidence, contribution in sorted(reason_specs, key=lambda item: item[4], reverse=True)[:4]
    ]


def _similar_days(symbol: str, regime: str) -> list[SimilarDay]:
    base = datetime.now(timezone.utc).date()
    return [
        SimilarDay(
            date=(base - timedelta(days=365 * (i + 1) - int(_seed(symbol) * 20))).isoformat(),
            similarity=round(0.86 - i * 0.07, 3),
            regime=regime,
            forward_20d_return=round(0.015 - i * 0.011 + _seed(symbol) * 0.01, 4),
            max_drawdown_20d=round(-0.025 - i * 0.012 - _seed(symbol) * 0.01, 4),
        )
        for i in range(5)
    ]


def build_prediction(symbol: str) -> PredictionSnapshot:
    feature_snapshot = latest_features(symbol)
    features = feature_snapshot.features
    regime = MarketRegime(feature_snapshot.market_regime)
    pullback_inputs = {
        "valuation_overheat": features["valuation_overheat"],
        "momentum_extension": features["momentum_extension"],
        "breadth_deterioration": features["breadth_deterioration"],
        "vix_options_risk": features["vix_options_risk"],
        "positioning_crowding": features["positioning_crowding"],
        "rates_up": features["rates_up"],
        "dollar_strength": features["dollar_strength"],
        "earnings_downgrades": features["earnings_downgrades"],
        "news_event_risk": features["news_event_risk"],
    }
    crisis_inputs = {
        "credit_gdp_gap": features["credit_gdp_gap"],
        "credit_spreads": features["credit_spreads"],
        "bank_stress": features["bank_stress"],
        "funding_market_stress": features["funding_market_stress"],
        "nonbank_leverage": features["nonbank_leverage"],
        "dollar_liquidity": features["dollar_liquidity"],
        "macro_recession_risk": features["macro_recession_risk"],
        "policy_response_lag": features["policy_response_lag"],
    }
    bounce_inputs = {
        "drawdown_depth": features["drawdown_depth"],
        "panic_extreme": features["panic_extreme"],
        "volume_expansion": features["volume_expansion"],
        "breadth_repair": features["breadth_repair"],
        "credit_spread_stabilization": features["credit_spread_stabilization"],
        "vix_reversal": features["vix_reversal"],
        "policy_liquidity_improvement": features["policy_liquidity_improvement"],
        "bad_news_resilience": features["bad_news_resilience"],
    }
    scores = compute_core_scores(ScoreInputs(pullback=pullback_inputs, crisis=crisis_inputs, bounce_quality=bounce_inputs))
    long_term = long_term_vulnerability_model(features)
    medium_term = medium_term_pullback_model(features)
    short_term = short_term_trigger_model(features, last_price=430.0 + _seed(feature_snapshot.symbol) * 120.0)
    bottom_bounce = bottom_bounce_model(features)
    risk_breakdown = [
        RiskSource(source=name, score=round(value * 100.0, 1), contribution=round(value, 3), evidence=f"{name} normalized contribution")
        for name, value in sorted({**pullback_inputs, **crisis_inputs}.items(), key=lambda item: item[1], reverse=True)[:8]
    ]
    dead_cat_risk = 1.0 if bottom_bounce.is_dead_cat_bounce else clamp01(1 - scores["bounce_quality_score"] / 100.0)
    return PredictionSnapshot(
        forecast_timestamp=feature_snapshot.as_of,
        symbol=feature_snapshot.symbol,
        market_regime=feature_snapshot.market_regime,
        model_version="rules-mvp-v1",
        feature_snapshot_version="deterministic-point-in-time-demo-v1",
        horizons=_horizon_forecasts(features, scores["pullback_risk_score"], scores["crisis_risk_score"], regime),
        pullback_risk_score=scores["pullback_risk_score"],
        crisis_risk_score=scores["crisis_risk_score"],
        bounce_probability=bottom_bounce.bounce_probability_20d,
        bounce_quality_score=scores["bounce_quality_score"],
        downside_continuation_probability=medium_term.max_drawdown_probability_20d,
        trend_reversal_probability=clamp01(0.25 + features["breadth_repair"] * 0.30 + features["credit_spread_stabilization"] * 0.20),
        dead_cat_bounce_risk=dead_cat_risk,
        top_reasons=_top_reasons(features),
        historical_similar_days=_similar_days(feature_snapshot.symbol, feature_snapshot.market_regime),
        risk_source_breakdown=risk_breakdown,
        model_layers=LayeredModelOutputs(
            long_term_vulnerability=long_term,
            medium_term_pullback=medium_term,
            short_term_trigger=short_term,
            bottom_bounce=bottom_bounce,
        ),
    )
