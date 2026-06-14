from __future__ import annotations

import math
from datetime import datetime
from typing import Any


PRICE_LEVEL_HORIZONS = (1, 3, 5, 10, 20, 60)
PATH_KEYS = {
    "expected_path": "综合期望路径",
    "bounce_path": "反抽情景",
    "bearish_path": "风险路径",
    "analog_average_path": "历史均值情景",
}


def build_forecast_price_levels(
    *,
    price_history: dict[str, list[dict[str, Any]]],
    simulated_paths: dict[str, Any],
) -> dict[str, Any]:
    """Derive scenario price levels from existing paths and point-in-time price structure."""

    symbols: dict[str, Any] = {}
    for symbol, path_payload in (simulated_paths.get("symbols") or {}).items():
        rows = price_history.get(symbol, [])
        symbols[symbol] = _build_symbol_price_levels(symbol, rows, path_payload)

    return {
        "version": "forecast_price_levels_v1",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "as_of": simulated_paths.get("as_of"),
        "validation_type": "forecast_scenario_levels",
        "disclaimer": (
            "Forecast price levels are probabilistic scenario points derived from simulated paths, "
            "recent price structure and volatility bands. They are not execution instructions, "
            "risk-control rules, or guaranteed target prices."
        ),
        "symbols": symbols,
    }


def render_forecast_price_levels_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Forecast Price Levels",
        "",
        f"Generated at: `{payload.get('generated_at')}`",
        "",
        "These are probability-path scenario levels, not execution instructions, risk-control rules, or guaranteed targets.",
        "",
    ]
    for symbol, data in (payload.get("symbols") or {}).items():
        lines.extend(
            [
                f"## {symbol}",
                "",
                f"- current price: `{_fmt(data.get('current_price'))}`",
                f"- primary confirmation: `{_fmt(_level_price(data, 'primary_confirmation_level'))}`",
                f"- primary invalidation: `{_fmt(_level_price(data, 'primary_invalidation_level'))}`",
                f"- risk activation: `{_fmt(_level_price(data, 'risk_scenario_activation_level'))}`",
                f"- trend repair confirmation: `{_fmt(_level_price(data, 'trend_reversal_confirmation_level'))}`",
                "",
                "| Horizon | Expected | Primary | Secondary | Risk | Upper | Lower |",
                "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for horizon, row in (data.get("forecast_price_table") or {}).items():
            lines.append(
                " | ".join(
                    [
                        f"| {horizon}",
                        _fmt(row.get("expected_price")),
                        _fmt(row.get("primary_scenario_price")),
                        _fmt(row.get("secondary_scenario_price")),
                        _fmt(row.get("risk_scenario_price")),
                        _fmt(row.get("upper_confidence_price")),
                        f"{_fmt(row.get('lower_confidence_price'))} |",
                    ]
                )
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def _build_symbol_price_levels(symbol: str, rows: list[dict[str, Any]], path_payload: dict[str, Any]) -> dict[str, Any]:
    current_price = _float_or_none(path_payload.get("current_price")) or _last_price(rows)
    structure = _price_structure(rows, current_price)
    price_table = _price_table(path_payload, current_price)
    triggers = _path_trigger_levels(path_payload, price_table, structure, current_price)
    summary = _summary(symbol, path_payload, triggers, current_price)
    return {
        "symbol": symbol,
        "name": path_payload.get("name"),
        "current_price": current_price,
        "source_note": "Derived from existing simulated paths, recent price structure and realized-volatility bands.",
        "not_trading_advice": True,
        "forecast_price_table": price_table,
        "path_trigger_levels": triggers,
        "price_structure": structure,
        "summary": summary,
    }


def _price_table(path_payload: dict[str, Any], current_price: float | None) -> dict[str, Any]:
    paths = path_payload.get("paths") or {}
    ranking = path_payload.get("scenario_ranking") or {}
    split_index = int(paths.get("split_index") or 0)
    primary = ((ranking.get("primary") or {}).get("scenario")) or "expected_path"
    secondary = ((ranking.get("secondary") or {}).get("scenario")) or "analog_average_path"
    risk = (ranking.get("risk_scenario") or ((ranking.get("tertiary") or {}).get("scenario")) or "bearish_path")
    primary_prob = _float_or_none((ranking.get("primary") or {}).get("probability"))
    confidence = ranking.get("path_reliability") or (ranking.get("primary") or {}).get("confidence") or "medium"

    table: dict[str, Any] = {}
    for horizon in PRICE_LEVEL_HORIZONS:
        index = split_index + horizon
        expected = _path_value(paths, "expected_path", index)
        primary_price = _path_value(paths, primary, index)
        secondary_price = _path_value(paths, secondary, index)
        risk_price = _path_value(paths, risk, index)
        upper = _path_value(paths, "confidence_band_upper", index)
        lower = _path_value(paths, "confidence_band_lower", index)
        analog = _path_value(paths, "analog_average_path", index)
        table[f"{horizon}d"] = {
            "horizon": f"{horizon}d",
            "expected_price": _round_price(expected),
            "expected_return": _round_return(_return_from(current_price, expected)),
            "primary_scenario": primary,
            "primary_scenario_label": PATH_KEYS.get(primary, primary),
            "primary_scenario_price": _round_price(primary_price),
            "secondary_scenario": secondary,
            "secondary_scenario_label": PATH_KEYS.get(secondary, secondary),
            "secondary_scenario_price": _round_price(secondary_price),
            "risk_scenario": risk,
            "risk_scenario_label": PATH_KEYS.get(risk, risk),
            "risk_scenario_price": _round_price(risk_price),
            "upper_confidence_price": _round_price(upper),
            "lower_confidence_price": _round_price(lower),
            "analog_average_price": _round_price(analog),
            "probability_of_reaching_primary_price": _round_return(primary_prob),
            "confidence_level": confidence,
            "source": "simulated_path",
            "not_guaranteed_forecast": True,
        }
    return table


def _path_trigger_levels(
    path_payload: dict[str, Any],
    price_table: dict[str, Any],
    structure: dict[str, Any],
    current_price: float | None,
) -> dict[str, Any]:
    ranking = path_payload.get("scenario_ranking") or {}
    primary = ((ranking.get("primary") or {}).get("scenario")) or "expected_path"
    primary_prob = _float_or_none((ranking.get("primary") or {}).get("probability")) or 0.0
    secondary_prob = _float_or_none((ranking.get("secondary") or {}).get("probability")) or 0.0
    risk_prob = _float_or_none((ranking.get("tertiary") or {}).get("probability")) or 0.0
    probability_gap = _float_or_none(ranking.get("primary_secondary_gap")) or max(primary_prob - secondary_prob, 0.0)
    atr = _float_or_none(structure.get("atr_proxy_14d")) or 0.0

    row3 = price_table.get("3d") or {}
    row5 = price_table.get("5d") or {}
    row10 = price_table.get("10d") or {}
    row20 = price_table.get("20d") or {}
    row60 = price_table.get("60d") or {}

    primary_5d = _float_or_none(row5.get("primary_scenario_price"))
    primary_20d = _float_or_none(row20.get("primary_scenario_price"))
    bounce_5d = _path_horizon_price(path_payload, "bounce_path", 5)
    bounce_20d = _path_horizon_price(path_payload, "bounce_path", 20)
    bounce_60d = _path_horizon_price(path_payload, "bounce_path", 60)
    risk_5d = _float_or_none(row5.get("risk_scenario_price"))
    risk_10d = _float_or_none(row10.get("risk_scenario_price"))
    lower_3d = _float_or_none(row3.get("lower_confidence_price"))
    lower_20d = _float_or_none(row20.get("lower_confidence_price"))

    recent_high_5d = _float_or_none(structure.get("high_5d"))
    recent_high_20d = _float_or_none(structure.get("high_20d"))
    recent_low_5d = _float_or_none(structure.get("low_5d"))
    recent_low_10d = _float_or_none(structure.get("low_10d"))
    recent_low_20d = _float_or_none(structure.get("low_20d"))
    ma20 = _float_or_none(structure.get("ma_20d"))
    ma50 = _float_or_none(structure.get("ma_50d"))
    upper_20d = _float_or_none(row20.get("upper_confidence_price"))

    primary_confirmation = _max_available(
        primary_5d,
        recent_high_5d,
        _add(current_price, atr * 0.35),
    )
    primary_invalidation = _min_available(
        recent_low_10d,
        lower_3d,
        _subtract(current_price, atr * 0.60),
    )
    risk_activation = _min_available(
        risk_10d,
        recent_low_20d,
        lower_20d,
        _subtract(current_price, atr),
    )
    trend_confirmation = _max_available(
        primary_20d,
        recent_high_20d,
        ma20,
        ma50,
    )

    conservative_bounce = _max_available(bounce_5d, primary_5d, recent_high_5d)
    base_bounce = _max_available(bounce_20d, primary_20d, recent_high_20d)
    extended_bounce = _max_available(bounce_60d, upper_20d)
    first_warning = _min_available(recent_low_5d, lower_3d, _subtract(current_price, atr * 0.45))
    critical_warning = _min_available(recent_low_20d, risk_10d, lower_20d, _subtract(current_price, atr * 1.1))

    return {
        "current_price": _round_price(current_price),
        "primary_scenario": primary,
        "primary_probability": _round_return(primary_prob),
        "secondary_probability": _round_return(secondary_prob),
        "risk_probability": _round_return(risk_prob),
        "probability_gap": _round_return(probability_gap),
        "primary_confirmation_level": _level(
            primary_confirmation,
            current_price,
            "confluence" if _near(primary_confirmation, primary_5d) and _near(primary_confirmation, recent_high_5d) else "simulated_path",
            "若价格突破或收在该价位上方，说明主路径正在兑现；这不是操作建议。",
            ["primary_path_5d", "recent_5d_high", "realized_volatility_band"],
        ),
        "primary_invalidation_level": _level(
            primary_invalidation,
            current_price,
            "confluence" if _near(primary_invalidation, recent_low_10d) and _near(primary_invalidation, lower_3d) else "price_structure",
            "若价格跌破或收在该价位下方，主路径可信度下降，风险路径权重上升。",
            ["recent_10d_low", "lower_confidence_band_3d", "realized_volatility_band"],
        ),
        "risk_scenario_activation_level": _level(
            risk_activation,
            current_price,
            "confluence" if _near(risk_activation, risk_10d) and _near(risk_activation, recent_low_20d) else "simulated_path",
            "若价格跌破该价位，失败反抽 / 下跌延续路径开始接管。",
            ["risk_path_10d", "recent_20d_low", "lower_confidence_band_20d"],
        ),
        "trend_reversal_confirmation_level": _level(
            trend_confirmation,
            current_price,
            "confluence" if _near(trend_confirmation, primary_20d) and (_near(trend_confirmation, recent_high_20d) or _near(trend_confirmation, ma50)) else "price_structure",
            "若价格突破该价位，趋势修复概率上升；仍需后续前向验证。",
            ["primary_path_20d", "recent_20d_high", "20d_or_50d_moving_average"],
        ),
        "bounce_target_zone": {
            "conservative_bounce_target": _level(
                conservative_bounce,
                current_price,
                "confluence" if _near(conservative_bounce, bounce_5d) and _near(conservative_bounce, recent_high_5d) else "simulated_path",
                "保守反抽情景点位，来自短期反抽路径和近期压力区。",
                ["bounce_path_5d", "recent_5d_high"],
            ),
            "base_bounce_target": _level(
                base_bounce,
                current_price,
                "simulated_path",
                "基础反抽情景点位，主要来自 20d 反抽路径。",
                ["bounce_path_20d", "primary_path_20d", "recent_20d_high"],
            ),
            "extended_bounce_target": _level(
                extended_bounce,
                current_price,
                "volatility_band" if _near(extended_bounce, upper_20d) else "simulated_path",
                "扩展反抽情景点位，来自 60d 反抽路径或上方置信带。",
                ["bounce_path_60d", "upper_confidence_band_20d"],
            ),
        },
        "failed_bounce_warning_zone": {
            "first_warning_level": _level(
                first_warning,
                current_price,
                "price_structure",
                "第一警戒区：跌破后说明反抽质量变差。",
                ["recent_5d_low", "lower_confidence_band_3d"],
            ),
            "critical_warning_level": _level(
                critical_warning,
                current_price,
                "confluence" if _near(critical_warning, recent_low_20d) and _near(critical_warning, risk_10d) else "simulated_path",
                "关键警戒区：跌破后风险路径权重显著上升。",
                ["recent_20d_low", "risk_path_10d", "lower_confidence_band_20d"],
            ),
        },
        "calculation_note": "Levels are derived from simulated paths, recent price structure, realized-volatility bands and scenario probabilities. They are not trading instructions.",
    }


def _summary(symbol: str, path_payload: dict[str, Any], triggers: dict[str, Any], current_price: float | None) -> dict[str, Any]:
    primary = (path_payload.get("scenario_ranking") or {}).get("primary") or {}
    secondary = (path_payload.get("scenario_ranking") or {}).get("secondary") or {}
    return {
        "plain_language": (
            f"{symbol} 当前主路径是 {primary.get('label') or primary.get('scenario') or 'data_missing'}，"
            f"第二路径是 {secondary.get('label') or secondary.get('scenario') or 'data_missing'}。"
            "价格点位只是路径验证条件，不是操作建议。"
        ),
        "primary_confirmation_distance": _level_distance(triggers.get("primary_confirmation_level"), current_price),
        "primary_invalidation_distance": _level_distance(triggers.get("primary_invalidation_level"), current_price),
        "risk_activation_distance": _level_distance(triggers.get("risk_scenario_activation_level"), current_price),
    }


def _price_structure(rows: list[dict[str, Any]], current_price: float | None) -> dict[str, Any]:
    closes = [_float_or_none(row.get("close")) for row in rows]
    closes = [value for value in closes if value is not None]
    if not closes:
        return {
            "status": "data_missing",
            "source": "price_structure",
        }
    returns = [
        (closes[index] / closes[index - 1] - 1.0)
        for index in range(1, len(closes))
        if closes[index - 1] and closes[index]
    ]
    vol20 = _std(returns[-20:]) if returns else None
    atr_proxy = _mean_abs(returns[-14:]) * (current_price or closes[-1]) if returns else None
    return {
        "status": "available",
        "source": "price_structure",
        "latest_date": rows[-1].get("date") if rows else None,
        "high_5d": _round_price(_max_available(*closes[-5:])),
        "low_5d": _round_price(_min_available(*closes[-5:])),
        "high_10d": _round_price(_max_available(*closes[-10:])),
        "low_10d": _round_price(_min_available(*closes[-10:])),
        "high_20d": _round_price(_max_available(*closes[-20:])),
        "low_20d": _round_price(_min_available(*closes[-20:])),
        "ma_20d": _round_price(_mean(closes[-20:]) if len(closes) >= 20 else None),
        "ma_50d": _round_price(_mean(closes[-50:]) if len(closes) >= 50 else None),
        "ma_200d": _round_price(_mean(closes[-200:]) if len(closes) >= 200 else None),
        "realized_volatility_20d": _round_return(vol20 * math.sqrt(252) if vol20 is not None else None),
        "atr_proxy_14d": _round_price(atr_proxy),
        "data_points": len(closes),
        "ma_200d_status": "available" if len(closes) >= 200 else "data_missing",
    }


def _path_horizon_price(path_payload: dict[str, Any], path_key: str, horizon: int) -> float | None:
    paths = path_payload.get("paths") or {}
    split_index = int(paths.get("split_index") or 0)
    return _path_value(paths, path_key, split_index + horizon)


def _path_value(paths: dict[str, Any], key: str, index: int) -> float | None:
    values = paths.get(key)
    if not isinstance(values, list) or index < 0 or index >= len(values):
        return None
    return _float_or_none(values[index])


def _level(price: float | None, current_price: float | None, source: str, condition: str, inputs: list[str]) -> dict[str, Any]:
    return {
        "price": _round_price(price),
        "source": source if price is not None else "data_missing",
        "distance_from_current": _round_price(None if price is None or current_price is None else price - current_price),
        "distance_percent": _round_return(None if price is None or current_price in (None, 0) else price / current_price - 1.0),
        "condition": condition,
        "inputs": inputs,
        "not_trading_advice": True,
    }


def _level_distance(level: Any, current_price: float | None) -> dict[str, Any]:
    if not isinstance(level, dict):
        return {"price": None, "distance_from_current": None, "distance_percent": None}
    return {
        "price": level.get("price"),
        "distance_from_current": level.get("distance_from_current"),
        "distance_percent": level.get("distance_percent"),
    }


def _level_price(data: dict[str, Any], key: str) -> float | None:
    level = data.get("path_trigger_levels", {}).get(key)
    return _float_or_none(level.get("price")) if isinstance(level, dict) else None


def _last_price(rows: list[dict[str, Any]]) -> float | None:
    for row in reversed(rows):
        parsed = _float_or_none(row.get("close"))
        if parsed is not None:
            return parsed
    return None


def _return_from(current_price: float | None, future_price: float | None) -> float | None:
    if current_price in (None, 0) or future_price is None:
        return None
    return future_price / current_price - 1.0


def _float_or_none(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _round_price(value: float | None) -> float | None:
    return round(value, 2) if value is not None and math.isfinite(value) else None


def _round_return(value: float | None) -> float | None:
    return round(value, 4) if value is not None and math.isfinite(value) else None


def _fmt(value: Any) -> str:
    parsed = _float_or_none(value)
    return "data_missing" if parsed is None else f"{parsed:.2f}"


def _add(value: float | None, delta: float | None) -> float | None:
    if value is None or delta is None:
        return None
    return value + delta


def _subtract(value: float | None, delta: float | None) -> float | None:
    if value is None or delta is None:
        return None
    return value - delta


def _max_available(*values: float | None) -> float | None:
    clean = [value for value in values if value is not None and math.isfinite(value)]
    return max(clean) if clean else None


def _min_available(*values: float | None) -> float | None:
    clean = [value for value in values if value is not None and math.isfinite(value)]
    return min(clean) if clean else None


def _near(left: float | None, right: float | None, tolerance: float = 0.006) -> bool:
    if left is None or right is None or right == 0:
        return False
    return abs(left / right - 1.0) <= tolerance


def _mean(values: list[float | None]) -> float | None:
    clean = [value for value in values if value is not None and math.isfinite(value)]
    return sum(clean) / len(clean) if clean else None


def _mean_abs(values: list[float]) -> float:
    clean = [value for value in values if math.isfinite(value)]
    return sum(abs(value) for value in clean) / len(clean) if clean else 0.0


def _std(values: list[float]) -> float | None:
    clean = [value for value in values if math.isfinite(value)]
    if len(clean) < 2:
        return None
    mean = sum(clean) / len(clean)
    variance = sum((value - mean) ** 2 for value in clean) / (len(clean) - 1)
    return math.sqrt(variance)
