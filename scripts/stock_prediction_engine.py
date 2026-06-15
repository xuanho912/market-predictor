from __future__ import annotations

import csv
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
HORIZONS = (1, 3, 5, 10, 20, 60)
STOCK_MODEL_VERSION = "stock_baseline_v1"


def build_stock_prediction_dashboard(
    *,
    stock_data_bundle: dict[str, Any],
    market_dashboard: dict[str, Any],
    write_ledger: bool = True,
) -> dict[str, Any]:
    support_rows = {
        symbol: payload.get("rows") or []
        for symbol, payload in (stock_data_bundle.get("support_symbols") or {}).items()
    }
    symbols: dict[str, Any] = {}
    for symbol, payload in (stock_data_bundle.get("symbols") or {}).items():
        rows = payload.get("rows") or []
        if payload.get("status") != "available" or not rows:
            symbols[symbol] = _missing_symbol_payload(symbol, payload, market_dashboard)
            continue
        benchmark = payload.get("benchmark") or "QQQ"
        sector_etf = payload.get("sector_etf")
        features = _stock_features(rows, support_rows.get("SPY", []), support_rows.get("QQQ", []), support_rows.get(benchmark, []), support_rows.get(sector_etf, []))
        market_context = _market_context_for_stock(symbol, benchmark, market_dashboard)
        scenarios = _scenario_ranking(features, market_context, payload)
        price_levels = _price_levels(rows, scenarios, features)
        symbols[symbol] = {
            "symbol": symbol,
            "model_version": STOCK_MODEL_VERSION,
            "as_of": rows[-1]["date"],
            "current_price": rows[-1]["close"],
            "benchmark": benchmark,
            "sector_etf": sector_etf,
            "data_status": payload.get("status"),
            "market_context_for_stock": market_context,
            "features": features,
            "scenario_ranking": scenarios,
            "forecast_price_levels": price_levels,
            "supporting_signals": scenarios.get("supporting_signals", []),
            "conflicting_signals": scenarios.get("conflicting_signals", []),
            "missing_data": _missing_data(payload),
            "validation_status": "not_yet_validated",
            "not_trading_advice": True,
        }

    if write_ledger:
        _update_stock_forecast_records(symbols)
    return {
        "version": "stock_prediction_dashboard_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "model_version": STOCK_MODEL_VERSION,
        "watchlist": stock_data_bundle.get("watchlist") or [],
        "summary": _summary(symbols, stock_data_bundle),
        "market_context_source": {
            "market_as_of": market_dashboard.get("as_of"),
            "active_market_model": "baseline_v1",
            "alpha_v1_threshold_unchanged": 0.32534311,
            "note": "Stock module consumes market context but does not modify baseline_v1 or Alpha v1.",
        },
        "symbols": symbols,
        "data_provider": {
            "provider": stock_data_bundle.get("provider"),
            "version": stock_data_bundle.get("version"),
            "summary": stock_data_bundle.get("summary"),
        },
        "guardrails": [
            "This is a probabilistic stock forecast module, not a trading system.",
            "Missing fundamentals, earnings, company news and single-stock options are labeled missing, not inferred.",
            "Stock forecasts are separate from the SPY/QQQ/IWM/DIA baseline_v1 market model.",
        ],
    }


def render_stock_prediction_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Stock Prediction Report",
        "",
        f"Generated at: `{payload.get('generated_at')}`",
        f"Model version: `{payload.get('model_version')}`",
        "",
        "This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce buy/sell instructions.",
        "",
        "## Summary",
        "",
    ]
    for key, value in (payload.get("summary") or {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## Symbols", ""])
    for symbol, data in (payload.get("symbols") or {}).items():
        ranking = data.get("scenario_ranking") or {}
        primary = ranking.get("primary") or {}
        secondary = ranking.get("secondary") or {}
        risk = ranking.get("risk") or {}
        lines.extend(
            [
                f"### {symbol}",
                "",
                f"- status: `{data.get('data_status')}`",
                f"- current_price: `{_fmt(data.get('current_price'))}`",
                f"- market_context: `{(data.get('market_context_for_stock') or {}).get('context')}`",
                f"- primary: `{primary.get('scenario')}` / `{_pct(primary.get('probability'))}`",
                f"- secondary: `{secondary.get('scenario')}` / `{_pct(secondary.get('probability'))}`",
                f"- risk: `{risk.get('scenario')}` / `{_pct(risk.get('probability'))}`",
                f"- validation_status: `{data.get('validation_status')}`",
                "",
            ]
        )
        levels = ((data.get("forecast_price_levels") or {}).get("trigger_levels") or {})
        lines.extend(
            [
                f"- primary_confirmation_level: `{_fmt((levels.get('primary_confirmation_level') or {}).get('price'))}`",
                f"- primary_invalidation_level: `{_fmt((levels.get('primary_invalidation_level') or {}).get('price'))}`",
                f"- risk_scenario_activation_level: `{_fmt((levels.get('risk_scenario_activation_level') or {}).get('price'))}`",
                "",
            ]
        )
    return "\n".join(lines)


def _missing_symbol_payload(symbol: str, payload: dict[str, Any], market_dashboard: dict[str, Any]) -> dict[str, Any]:
    benchmark = payload.get("benchmark") or "QQQ"
    return {
        "symbol": symbol,
        "model_version": STOCK_MODEL_VERSION,
        "as_of": None,
        "current_price": None,
        "benchmark": benchmark,
        "sector_etf": payload.get("sector_etf"),
        "data_status": payload.get("status"),
        "market_context_for_stock": _market_context_for_stock(symbol, benchmark, market_dashboard),
        "features": {},
        "scenario_ranking": {
            "primary": {"scenario": "stock_data_missing", "probability": None, "label": "数据缺失"},
            "secondary": {"scenario": "stock_data_missing", "probability": None, "label": "数据缺失"},
            "risk": {"scenario": "stock_data_missing", "probability": None, "label": "数据缺失"},
            "close_call": True,
            "ranking_note": "Stock forecast blocked because real point-in-time price data is missing.",
        },
        "forecast_price_levels": {},
        "supporting_signals": [],
        "conflicting_signals": ["真实个股价格数据缺失，不能生成 live stock forecast。"],
        "missing_data": _missing_data(payload),
        "validation_status": "not_yet_validated",
        "not_trading_advice": True,
    }


def _stock_features(
    rows: list[dict[str, Any]],
    spy_rows: list[dict[str, Any]],
    qqq_rows: list[dict[str, Any]],
    benchmark_rows: list[dict[str, Any]],
    sector_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    close = _last_close(rows)
    returns = {f"{h}d": _return(rows, h) for h in HORIZONS}
    ma = {f"ma_{n}d": _sma(rows, n) for n in (5, 20, 50, 200)}
    distances = {f"distance_to_{n}d_ma": _distance(close, ma[f"ma_{n}d"]) for n in (5, 20, 50, 200)}
    drawdown_20 = _drawdown(rows, 20)
    drawdown_60 = _drawdown(rows, 60)
    atr = _atr(rows, 14)
    realized_vol = _realized_vol(rows, 20)
    volume_z = _volume_z_score(rows, 20)
    stock_20 = _return(rows, 20) or 0.0
    stock_60 = _return(rows, 60) or 0.0
    benchmark_20 = _return(benchmark_rows, 20)
    benchmark_60 = _return(benchmark_rows, 60)
    sector_20 = _return(sector_rows, 20)
    latest = rows[-1]
    prev = rows[-2] if len(rows) >= 2 else latest
    open_price = _float(latest.get("open")) or close
    prev_close = _float(prev.get("close")) or close
    gap = _safe_div(open_price - prev_close, prev_close)
    recent_high = _max_close(rows, 20)
    recent_low = _min_close(rows, 20)
    trend_slope = _safe_div(close - (_sma(rows[:-20], 20) or close), close) if len(rows) > 40 else stock_20
    up_volume, down_volume = _up_down_volume(rows, 20)
    volume_confirmation = _clamp(50 + (volume_z or 0) * 8 + (10 if stock_20 > 0 else -6), 0, 100)
    relative_strength_trend = _clamp(50 + ((stock_20 - (benchmark_20 or 0)) * 180) + ((stock_60 - (benchmark_60 or 0)) * 90), 0, 100)
    return {
        "price_trend": {
            "close": close,
            "returns": returns,
            "drawdown_20d": drawdown_20,
            "drawdown_60d": drawdown_60,
            **distances,
            "trend_slope": _round(trend_slope),
            "recent_swing_high": recent_high,
            "recent_swing_low": recent_low,
            "gap_up_down": _round(gap),
        },
        "volume": {
            "volume_z_score": _round(volume_z),
            "volume_vs_20d_average": _round(_safe_div(_float(latest.get("volume")), _avg_volume(rows, 20))),
            "up_volume_down_volume_proxy": _round(_safe_div(up_volume, down_volume)),
            "accumulation_distribution_proxy": _round(_safe_div(up_volume - down_volume, up_volume + down_volume)),
            "panic_volume_proxy": bool((volume_z or 0) >= 2.0 and (returns.get("1d") or 0) < 0),
            "volume_confirmation_score": round(volume_confirmation, 2),
        },
        "relative_strength": {
            "stock_vs_spy_20d": _round(stock_20 - (_return(spy_rows, 20) or 0)),
            "stock_vs_qqq_20d": _round(stock_20 - (_return(qqq_rows, 20) or 0)),
            "stock_vs_benchmark_20d": _round(stock_20 - (benchmark_20 or 0)),
            "stock_vs_benchmark_60d": _round(stock_60 - (benchmark_60 or 0)),
            "stock_vs_sector_20d": _round(stock_20 - (sector_20 or 0)) if sector_rows else None,
            "relative_strength_trend": round(relative_strength_trend, 2),
        },
        "volatility": {
            "realized_volatility_20d": _round(realized_vol),
            "atr_14d": _round(atr),
            "atr_pct": _round(_safe_div(atr, close)),
            "price_range_20d": _round(_safe_div(recent_high - recent_low, close) if close else None),
            "implied_volatility": None,
            "option_stress": "missing",
        },
        "news_event": {
            "company_news": "missing",
            "earnings_date": None,
            "earnings_risk_flag": "missing",
            "analyst_rating_news": "missing",
            "news_sentiment": "missing",
            "news_risk_score": None,
        },
        "fundamentals_valuation": {
            "revenue_growth": None,
            "earnings_growth": None,
            "forward_pe": None,
            "profitability": None,
            "debt_risk": None,
            "cash_flow_quality": None,
            "valuation_percentile": None,
            "status": "missing",
        },
    }


def _market_context_for_stock(symbol: str, benchmark: str, market_dashboard: dict[str, Any]) -> dict[str, Any]:
    symbols = ((market_dashboard.get("simulated_paths") or {}).get("symbols") or {})
    overview = ((market_dashboard.get("overview") or {}).get("symbols") or {})
    market_symbol = symbols.get(benchmark) or symbols.get("QQQ") or symbols.get("SPY") or {}
    overview_symbol = overview.get(benchmark) or overview.get("QQQ") or overview.get("SPY") or {}
    ranking = market_symbol.get("scenario_ranking") or {}
    primary = ranking.get("primary") or {}
    alerts = market_symbol.get("market_alerts") or {}
    edge = (market_symbol.get("market_edge_status") or {}).get("market_edge_status") or "NO_EDGE"
    primary_scenario = primary.get("scenario")
    primary_probability = _float(primary.get("probability")) or 0.0
    risk_alert = str((alerts.get("strongest_alert") or {}).get("alert_type") or "")
    risk_level = str((alerts.get("strongest_alert") or {}).get("alert_level") or "NO_ALERT")
    if "risk" in risk_alert.lower() or risk_level in {"WARNING", "HIGH_CONVICTION", "EXTREME"}:
        context = "risk_off_pressure"
    elif primary_scenario == "bounce_path" and edge in {"MODERATE_EDGE", "STRONG_EDGE"}:
        context = "market_tailwind"
    elif primary_scenario in {"bearish_path", "failed_bounce_path"}:
        context = "market_headwind"
    elif primary_probability >= 0.35:
        context = "supportive"
    else:
        context = "neutral"
    return {
        "symbol": symbol,
        "benchmark": benchmark,
        "context": context,
        "benchmark_primary_scenario": primary_scenario,
        "benchmark_primary_probability": _round(primary_probability),
        "benchmark_edge_status": edge,
        "benchmark_market_state": overview_symbol.get("market_state"),
        "risk_alert_type": risk_alert or "NO_ALERT",
        "risk_alert_level": risk_level,
        "note": "Market context is an input to stock forecast probabilities; it does not modify the market baseline model.",
    }


def _scenario_ranking(features: dict[str, Any], market_context: dict[str, Any], data_payload: dict[str, Any]) -> dict[str, Any]:
    trend = features.get("price_trend") or {}
    volume = features.get("volume") or {}
    rel = features.get("relative_strength") or {}
    vol = features.get("volatility") or {}
    ret20 = _float((trend.get("returns") or {}).get("20d")) or 0.0
    ret5 = _float((trend.get("returns") or {}).get("5d")) or 0.0
    dd20 = _float(trend.get("drawdown_20d")) or 0.0
    dist20 = _float(trend.get("distance_to_20d_ma")) or 0.0
    dist50 = _float(trend.get("distance_to_50d_ma")) or 0.0
    rel_score = _float(rel.get("relative_strength_trend")) or 50.0
    volume_score = _float(volume.get("volume_confirmation_score")) or 50.0
    atr_pct = _float(vol.get("atr_pct")) or 0.03
    context = market_context.get("context")

    bounce = 0.18 + min(abs(dd20), 0.25) * 0.85 + (0.08 if context in {"market_tailwind", "supportive"} else 0.0)
    trend_repair = 0.16 + max(ret20, 0.0) * 0.55 + max(rel_score - 50, 0) / 250
    downside = 0.16 + max(-ret20, 0.0) * 0.75 + max(-dist50, 0.0) * 0.55
    failed_bounce = 0.14 + max(-ret5, 0.0) * 0.80 + (0.08 if context in {"risk_off_pressure", "market_headwind"} else 0.0)
    sideways = 0.18 + max(0.0, 0.04 - abs(ret20)) * 1.2
    event_risk = 0.10 + min(atr_pct, 0.10) * 1.1

    if volume_score >= 62 and ret5 > 0:
        bounce += 0.05
        trend_repair += 0.04
    if rel_score < 42:
        downside += 0.05
        failed_bounce += 0.04
    if data_payload.get("data_categories", {}).get("company_news") == "missing":
        event_risk += 0.03

    raw = {
        "stock_bounce": max(bounce, 0.01),
        "stock_trend_repair": max(trend_repair, 0.01),
        "stock_downside_continuation": max(downside, 0.01),
        "stock_failed_bounce": max(failed_bounce, 0.01),
        "stock_sideways": max(sideways, 0.01),
        "stock_event_risk": max(event_risk, 0.01),
    }
    total = sum(raw.values())
    normalized = {key: value / total for key, value in raw.items()}
    ordered = sorted(normalized.items(), key=lambda item: item[1], reverse=True)
    supporting = _supporting_signals(features, market_context)
    conflicting = _conflicting_signals(features, market_context)
    probability_gap = ordered[0][1] - ordered[1][1]
    return {
        "primary": _scenario_item(ordered[0], features, market_context),
        "secondary": _scenario_item(ordered[1], features, market_context),
        "risk": _scenario_item(next((item for item in ordered if item[0] in {"stock_failed_bounce", "stock_downside_continuation", "stock_event_risk"}), ordered[2]), features, market_context),
        "all_scenarios": [_scenario_item(item, features, market_context) for item in ordered],
        "probability_gap": _round(probability_gap),
        "close_call": probability_gap < 0.08,
        "supporting_signals": supporting,
        "conflicting_signals": conflicting,
        "ranking_note": "Stock scenario probabilities combine market context, price structure, volume, relative strength and volatility. They are not validated alpha and not trading advice.",
    }


def _scenario_item(item: tuple[str, float], features: dict[str, Any], market_context: dict[str, Any]) -> dict[str, Any]:
    scenario, probability = item
    labels = {
        "stock_bounce": "个股反抽",
        "stock_trend_repair": "个股趋势修复",
        "stock_downside_continuation": "个股下跌延续",
        "stock_failed_bounce": "个股失败反抽",
        "stock_sideways": "个股震荡",
        "stock_event_risk": "个股事件风险",
    }
    return {
        "scenario": scenario,
        "label": labels.get(scenario, scenario),
        "probability": _round(probability),
        "reason": _scenario_reason(scenario, features, market_context),
        "confidence": "low" if _missing_event_or_fundamental(features) else "medium",
    }


def _price_levels(rows: list[dict[str, Any]], scenarios: dict[str, Any], features: dict[str, Any]) -> dict[str, Any]:
    current = _last_close(rows)
    vol = features.get("volatility") or {}
    trend = features.get("price_trend") or {}
    atr_pct = _float(vol.get("atr_pct")) or 0.03
    ranking = scenarios.get("all_scenarios") or []
    scenario_prices = {item["scenario"]: _scenario_horizon_returns(item["scenario"], atr_pct) for item in ranking}
    primary = (scenarios.get("primary") or {}).get("scenario") or "stock_sideways"
    secondary = (scenarios.get("secondary") or {}).get("scenario") or "stock_sideways"
    risk = (scenarios.get("risk") or {}).get("scenario") or "stock_downside_continuation"
    primary_prob = _float((scenarios.get("primary") or {}).get("probability")) or 0.0
    rows_by_horizon: dict[str, Any] = {}
    for horizon in HORIZONS:
        expected_return = sum((_float(item.get("probability")) or 0) * scenario_prices[item["scenario"]][horizon] for item in ranking if item["scenario"] in scenario_prices)
        upper = expected_return + atr_pct * math.sqrt(horizon / 5) * 1.1
        lower = expected_return - atr_pct * math.sqrt(horizon / 5) * 1.1
        rows_by_horizon[f"{horizon}d"] = {
            "expected_price": _price(current, expected_return),
            "expected_return": _round(expected_return),
            "primary_scenario_price": _price(current, scenario_prices.get(primary, {}).get(horizon, expected_return)),
            "secondary_scenario_price": _price(current, scenario_prices.get(secondary, {}).get(horizon, expected_return)),
            "risk_scenario_price": _price(current, scenario_prices.get(risk, {}).get(horizon, expected_return)),
            "upper_confidence_price": _price(current, upper),
            "lower_confidence_price": _price(current, lower),
            "probability_of_reaching_primary_price": _round(primary_prob),
            "confidence_level": (scenarios.get("primary") or {}).get("confidence") or "low",
        }
    recent_high = _float(trend.get("recent_swing_high")) or current
    recent_low = _float(trend.get("recent_swing_low")) or current
    atr = (_float(vol.get("atr_14d")) or current * atr_pct)
    confirmation = max(recent_high, current + atr * 0.45)
    invalidation = min(recent_low, current - atr * 0.65)
    risk_activation = min(invalidation, current - atr * 1.1)
    trend_repair = max(recent_high, _float(rows_by_horizon.get("20d", {}).get("primary_scenario_price")) or current)
    return {
        "forecast_price_table": rows_by_horizon,
        "trigger_levels": {
            "primary_confirmation_level": _level(confirmation, current, "站上该价位说明个股主路径正在兑现", "price_structure + scenario_path"),
            "primary_invalidation_level": _level(invalidation, current, "跌破该价位说明个股主路径失效概率上升", "recent_low + volatility_band"),
            "risk_scenario_activation_level": _level(risk_activation, current, "跌破该价位说明个股风险路径权重上升", "volatility_band"),
            "trend_repair_confirmation_level": _level(trend_repair, current, "突破该价位说明个股趋势修复概率提高", "recent_high + scenario_path"),
        },
        "disclaimer": "Price levels are probabilistic scenario references, not target prices or execution instructions.",
    }


def _scenario_horizon_returns(scenario: str, atr_pct: float) -> dict[int, float]:
    scale = max(atr_pct, 0.015)
    base = {
        "stock_bounce": {1: 0.18, 3: 0.45, 5: 0.68, 10: 0.95, 20: 1.25, 60: 1.55},
        "stock_trend_repair": {1: 0.10, 3: 0.28, 5: 0.45, 10: 0.78, 20: 1.20, 60: 1.85},
        "stock_downside_continuation": {1: -0.20, 3: -0.48, 5: -0.72, 10: -1.05, 20: -1.38, 60: -1.70},
        "stock_failed_bounce": {1: -0.08, 3: -0.28, 5: -0.52, 10: -0.90, 20: -1.05, 60: -1.15},
        "stock_sideways": {1: 0.02, 3: 0.04, 5: 0.05, 10: 0.06, 20: 0.07, 60: 0.08},
        "stock_event_risk": {1: -0.12, 3: -0.30, 5: -0.40, 10: -0.50, 20: -0.55, 60: -0.45},
    }
    return {h: multiplier * scale for h, multiplier in base.get(scenario, base["stock_sideways"]).items()}


def _supporting_signals(features: dict[str, Any], market_context: dict[str, Any]) -> list[str]:
    items: list[str] = []
    if market_context.get("context") in {"market_tailwind", "supportive"}:
        items.append("大盘背景支持个股风险偏好。")
    if (_float(((features.get("relative_strength") or {}).get("relative_strength_trend"))) or 0) >= 60:
        items.append("个股相对强弱优于基准。")
    if (_float(((features.get("volume") or {}).get("volume_confirmation_score"))) or 0) >= 60:
        items.append("成交量结构支持当前路径。")
    if (_float(((features.get("price_trend") or {}).get("distance_to_20d_ma"))) or 0) > 0:
        items.append("价格站在 20d 均线上方。")
    return items or ["当前没有足够强的多源支持证据。"]


def _conflicting_signals(features: dict[str, Any], market_context: dict[str, Any]) -> list[str]:
    items: list[str] = []
    if market_context.get("context") in {"risk_off_pressure", "market_headwind"}:
        items.append("大盘背景对个股路径形成压力。")
    if (_float(((features.get("relative_strength") or {}).get("relative_strength_trend"))) or 50) < 45:
        items.append("个股相对强弱弱于基准。")
    if (_float(((features.get("price_trend") or {}).get("distance_to_50d_ma"))) or 0) < 0:
        items.append("价格仍在 50d 均线下方。")
    if _missing_event_or_fundamental(features):
        items.append("财报、估值、公司新闻或个股期权数据缺失，个股置信度受限。")
    return items


def _scenario_reason(scenario: str, features: dict[str, Any], market_context: dict[str, Any]) -> str:
    context = market_context.get("context")
    if scenario == "stock_bounce":
        return f"结合回撤、成交量和大盘背景，短中期反抽权重较高；当前市场背景为 {context}。"
    if scenario == "stock_trend_repair":
        return "相对强弱和中期趋势修复信号较强时，该路径上升。"
    if scenario == "stock_downside_continuation":
        return "价格低于关键均线、相对弱势或大盘 risk-off 时，下跌延续权重上升。"
    if scenario == "stock_failed_bounce":
        return "反抽缺乏成交量/相对强弱确认或大盘风险上升时，失败反抽权重上升。"
    if scenario == "stock_event_risk":
        return "个股新闻、财报、估值或期权数据缺失时，事件风险保持为独立风险路径。"
    return "信号分歧较大时，震荡路径权重上升。"


def _missing_data(payload: dict[str, Any]) -> list[str]:
    categories = payload.get("data_categories") or {}
    missing = [key for key, value in categories.items() if value == "missing"]
    if payload.get("synthetic_blocked"):
        missing.append("synthetic_blocked")
    return missing


def _missing_event_or_fundamental(features: dict[str, Any]) -> bool:
    return (features.get("news_event") or {}).get("company_news") == "missing" or (features.get("fundamentals_valuation") or {}).get("status") == "missing"


def _summary(symbols: dict[str, Any], stock_data_bundle: dict[str, Any]) -> dict[str, Any]:
    available = [symbol for symbol, payload in symbols.items() if payload.get("data_status") == "available"]
    strongest = None
    if available:
        strongest = max(
            available,
            key=lambda symbol: _float(((symbols[symbol].get("scenario_ranking") or {}).get("primary") or {}).get("probability")) or 0.0,
        )
    return {
        "supported_symbols": len(available),
        "watchlist_size": len(symbols),
        "strongest_stock_symbol": strongest,
        "stock_data_quality_score": (stock_data_bundle.get("summary") or {}).get("data_quality_score"),
        "validation_status": "not_yet_validated",
        "missing_high_value_data": ["fundamentals", "earnings", "company_news", "single_stock_options"],
    }


def _update_stock_forecast_records(symbols: dict[str, Any], path: Path | None = None) -> None:
    path = path or PROJECT_ROOT / "outputs" / "stock_forecast_records.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "forecast_id",
        "forecast_date",
        "model_version",
        "symbol",
        "current_price",
        "primary_scenario",
        "primary_probability",
        "secondary_scenario",
        "secondary_probability",
        "risk_scenario",
        "risk_probability",
        "market_context",
        "validation_status",
        "status",
    ]
    existing: dict[str, dict[str, Any]] = {}
    if path.exists():
        with path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                if row.get("forecast_id"):
                    existing[row["forecast_id"]] = row
    for symbol, payload in symbols.items():
        if payload.get("data_status") != "available" or not payload.get("as_of"):
            continue
        ranking = payload.get("scenario_ranking") or {}
        primary = ranking.get("primary") or {}
        secondary = ranking.get("secondary") or {}
        risk = ranking.get("risk") or {}
        forecast_id = _forecast_id(payload["as_of"], STOCK_MODEL_VERSION, symbol)
        existing.setdefault(
            forecast_id,
            {
                "forecast_id": forecast_id,
                "forecast_date": payload.get("as_of"),
                "model_version": STOCK_MODEL_VERSION,
                "symbol": symbol,
                "current_price": payload.get("current_price"),
                "primary_scenario": primary.get("scenario"),
                "primary_probability": primary.get("probability"),
                "secondary_scenario": secondary.get("scenario"),
                "secondary_probability": secondary.get("probability"),
                "risk_scenario": risk.get("scenario"),
                "risk_probability": risk.get("probability"),
                "market_context": (payload.get("market_context_for_stock") or {}).get("context"),
                "validation_status": "not_yet_validated",
                "status": "pending",
            },
        )
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in sorted(existing.values(), key=lambda item: (str(item.get("forecast_date")), str(item.get("symbol")))):
            writer.writerow({field: row.get(field, "") for field in fields})


def _forecast_id(forecast_date: str, model_version: str, symbol: str) -> str:
    return hashlib.sha256(f"{forecast_date}|{model_version}|{symbol}".encode("utf-8")).hexdigest()[:20]


def _last_close(rows: list[dict[str, Any]]) -> float:
    return float(rows[-1]["close"]) if rows else 0.0


def _return(rows: list[dict[str, Any]], horizon: int) -> float | None:
    if len(rows) <= horizon:
        return None
    end = _float(rows[-1].get("close"))
    start = _float(rows[-1 - horizon].get("close"))
    return _safe_div(end - start, start)


def _drawdown(rows: list[dict[str, Any]], window: int) -> float | None:
    if not rows:
        return None
    sample = rows[-window:]
    peak = max((_float(row.get("close")) or 0.0) for row in sample)
    close = _last_close(rows)
    return _safe_div(close - peak, peak)


def _sma(rows: list[dict[str, Any]], window: int) -> float | None:
    if len(rows) < window:
        return None
    values = [_float(row.get("close")) for row in rows[-window:]]
    values = [value for value in values if value is not None]
    return sum(values) / len(values) if values else None


def _distance(close: float, ma: float | None) -> float | None:
    return _round(_safe_div(close - ma, ma)) if ma else None


def _atr(rows: list[dict[str, Any]], window: int) -> float | None:
    if len(rows) < 2:
        return None
    ranges = []
    for index in range(max(1, len(rows) - window), len(rows)):
        row = rows[index]
        prev_close = _float(rows[index - 1].get("close")) or _float(row.get("close")) or 0.0
        high = _float(row.get("high")) or prev_close
        low = _float(row.get("low")) or prev_close
        ranges.append(max(high - low, abs(high - prev_close), abs(low - prev_close)))
    return sum(ranges) / len(ranges) if ranges else None


def _realized_vol(rows: list[dict[str, Any]], window: int) -> float | None:
    if len(rows) <= window:
        return None
    returns = [_return(rows[: index + 1], 1) for index in range(len(rows) - window, len(rows))]
    clean = [value for value in returns if value is not None]
    if len(clean) < 2:
        return None
    mean = sum(clean) / len(clean)
    variance = sum((value - mean) ** 2 for value in clean) / (len(clean) - 1)
    return math.sqrt(variance) * math.sqrt(252)


def _volume_z_score(rows: list[dict[str, Any]], window: int) -> float | None:
    if len(rows) < window + 1:
        return None
    values = [_float(row.get("volume")) for row in rows[-window - 1 : -1]]
    values = [value for value in values if value is not None]
    latest = _float(rows[-1].get("volume"))
    if latest is None or len(values) < 5:
        return None
    mean = sum(values) / len(values)
    std = math.sqrt(sum((value - mean) ** 2 for value in values) / len(values))
    return _safe_div(latest - mean, std) if std else 0.0


def _avg_volume(rows: list[dict[str, Any]], window: int) -> float | None:
    values = [_float(row.get("volume")) for row in rows[-window:]]
    values = [value for value in values if value is not None]
    return sum(values) / len(values) if values else None


def _up_down_volume(rows: list[dict[str, Any]], window: int) -> tuple[float, float]:
    up = 0.0
    down = 0.0
    for index in range(max(1, len(rows) - window), len(rows)):
        volume = _float(rows[index].get("volume")) or 0.0
        close = _float(rows[index].get("close")) or 0.0
        prev = _float(rows[index - 1].get("close")) or close
        if close >= prev:
            up += volume
        else:
            down += volume
    return up, down


def _max_close(rows: list[dict[str, Any]], window: int) -> float:
    sample = rows[-window:] if rows else []
    return max((_float(row.get("high")) or _float(row.get("close")) or 0.0) for row in sample) if sample else 0.0


def _min_close(rows: list[dict[str, Any]], window: int) -> float:
    sample = rows[-window:] if rows else []
    return min((_float(row.get("low")) or _float(row.get("close")) or 0.0) for row in sample) if sample else 0.0


def _level(price: float, current: float, meaning: str, source: str) -> dict[str, Any]:
    return {
        "price": _round_price(price),
        "meaning": meaning,
        "source": source,
        "distance_pct": _round(_safe_div(price - current, current)),
        "confidence": "low",
        "not_trading_instruction": True,
    }


def _price(current: float, expected_return: float | None) -> float | None:
    if expected_return is None:
        return None
    return _round_price(current * (1 + expected_return))


def _safe_div(num: float | None, den: float | None) -> float | None:
    if num is None or den in (None, 0):
        return None
    return num / den


def _float(value: Any) -> float | None:
    try:
        if value is None:
            return None
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if number == number else None


def _round(value: float | None, digits: int = 4) -> float | None:
    return round(value, digits) if value is not None and value == value else None


def _round_price(value: float | None) -> float | None:
    return round(value, 2) if value is not None and value == value else None


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _fmt(value: Any) -> str:
    number = _float(value)
    return "missing" if number is None else f"{number:.2f}"


def _pct(value: Any) -> str:
    number = _float(value)
    return "missing" if number is None else f"{number * 100:.1f}%"
