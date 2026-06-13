from __future__ import annotations

from app.schemas.predictions import (
    BottomBounceOutput,
    LongTermVulnerabilityOutput,
    MediumTermPullbackOutput,
    RiskSource,
    ShortTermTriggerOutput,
)
from app.services.signals.risk_score import bounce_quality_score, crisis_risk_score, pullback_risk_score


def clamp01(value: float) -> float:
    return min(max(value, 0.0), 1.0)


def long_term_vulnerability_model(features: dict[str, float]) -> LongTermVulnerabilityOutput:
    values = {
        "credit_gdp_gap": features["credit_gdp_gap"],
        "credit_spreads": features["credit_spreads"],
        "bank_stress": features["bank_stress"],
        "funding_market_stress": features["funding_market_stress"],
        "nonbank_leverage": features["nonbank_leverage"],
        "dollar_liquidity": features["dollar_liquidity"],
        "macro_recession_risk": features["macro_recession_risk"],
        "policy_response_lag": features["policy_response_lag"],
    }
    score = crisis_risk_score(values)
    sectors = sorted(
        [
            ("banks", features["bank_stress"]),
            ("commercial_real_estate", features["real_estate_pressure"]),
            ("leveraged_credit", features["credit_spreads"]),
            ("nonbank_financials", features["nonbank_leverage"]),
        ],
        key=lambda item: item[1],
        reverse=True,
    )
    return LongTermVulnerabilityOutput(
        financial_system_vulnerability_score=score,
        crisis_probability_12m=clamp01(score / 120.0 + features["macro_recession_risk"] * 0.15),
        most_vulnerable_sectors=[name for name, _ in sectors[:3]],
    )


def medium_term_pullback_model(features: dict[str, float]) -> MediumTermPullbackOutput:
    values = {
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
    score = pullback_risk_score(values)
    breakdown = [
        RiskSource(source=name, score=round(value * 100, 1), contribution=round(value, 3), evidence=f"{name} normalized risk input")
        for name, value in sorted(values.items(), key=lambda item: item[1], reverse=True)[:5]
    ]
    return MediumTermPullbackOutput(
        max_drawdown_probability_20d=clamp01(score / 130.0),
        max_drawdown_probability_60d=clamp01(score / 115.0),
        expected_drawdown=round(-0.03 - score / 1000.0, 4),
        risk_source_breakdown=breakdown,
    )


def short_term_trigger_model(features: dict[str, float], last_price: float) -> ShortTermTriggerOutput:
    sharp_drop = clamp01(
        0.25 * features["gamma_risk"]
        + 0.20 * features["zero_dte_risk"]
        + 0.20 * features["order_book_thinness"]
        + 0.20 * features["news_event_risk"]
        + 0.15 * features["vol_term_structure_stress"]
    )
    sharp_rebound = clamp01(
        0.30 * features["short_covering_pressure"]
        + 0.25 * features["panic_extreme"]
        + 0.20 * features["vix_reversal"]
        + 0.15 * features["breadth_repair"]
        + 0.10 * features["premarket_strength"]
    )
    intraday_width = 0.012 + 0.035 * max(sharp_drop, sharp_rebound)
    return ShortTermTriggerOutput(
        sharp_drop_probability=sharp_drop,
        sharp_rebound_probability=sharp_rebound,
        intraday_range=(round(last_price * (1 - intraday_width), 2), round(last_price * (1 + intraday_width), 2)),
        key_trigger_levels=[
            round(last_price * (1 - intraday_width * 0.65), 2),
            round(last_price, 2),
            round(last_price * (1 + intraday_width * 0.65), 2),
        ],
    )


def bottom_bounce_model(features: dict[str, float]) -> BottomBounceOutput:
    quality_inputs = {
        "drawdown_depth": features["drawdown_depth"],
        "panic_extreme": features["panic_extreme"],
        "volume_expansion": features["volume_expansion"],
        "breadth_repair": features["breadth_repair"],
        "credit_spread_stabilization": features["credit_spread_stabilization"],
        "vix_reversal": features["vix_reversal"],
        "policy_liquidity_improvement": features["policy_liquidity_improvement"],
        "bad_news_resilience": features["bad_news_resilience"],
    }
    quality = bounce_quality_score(quality_inputs)
    dead_cat_risk = clamp01(
        0.30 * (1 - features["breadth_repair"])
        + 0.25 * (1 - features["credit_spread_stabilization"])
        + 0.20 * (1 - features["volume_expansion"])
        + 0.15 * features["earnings_downgrades"]
        + 0.10 * (1 - features["vix_reversal"])
    )
    return BottomBounceOutput(
        bounce_probability_10d=clamp01(quality / 120.0 + features["short_covering_pressure"] * 0.10),
        bounce_probability_20d=clamp01(quality / 110.0 + features["policy_liquidity_improvement"] * 0.10),
        is_dead_cat_bounce=dead_cat_risk >= 0.55,
        may_form_medium_term_bottom=quality >= 65 and dead_cat_risk < 0.45,
    )
