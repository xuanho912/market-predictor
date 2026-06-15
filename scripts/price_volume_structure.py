from __future__ import annotations

import json
import math
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BACKEND_ROOT = PROJECT_ROOT / "backend"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.services.data_providers.auto_download import DownloadedSeries, refresh_market_data


SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
VERSION = "price_volume_structure_v1"


def build_price_volume_structure(
    series_by_symbol: dict[str, DownloadedSeries],
    symbols: tuple[str, ...] = SYMBOLS,
) -> dict[str, Any]:
    payload = {
        "version": VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "disclaimer": "K线和成交量结构只用于预测确认，不是交易信号、买卖建议或仓位建议。",
        "symbols": {},
        "summary": {},
    }
    for symbol in symbols:
        payload["symbols"][symbol] = _symbol_structure(symbol, series_by_symbol.get(symbol))

    scores = [
        _num(item.get("price_structure_score"))
        for item in payload["symbols"].values()
        if _num(item.get("price_structure_score")) is not None
    ]
    volume_scores = [
        _num(item.get("volume_confirmation_score"))
        for item in payload["symbols"].values()
        if _num(item.get("volume_confirmation_score")) is not None
    ]
    payload["summary"] = {
        "average_price_structure_score": _round(_mean(scores)),
        "average_volume_confirmation_score": _round(_mean(volume_scores)),
        "symbols_with_bullish_reversal_candle": [
            symbol for symbol, item in payload["symbols"].items() if item.get("candle", {}).get("bullish_reversal_candle")
        ],
        "symbols_with_breakdown_risk": [
            symbol for symbol, item in payload["symbols"].items() if _num(item.get("breakdown_risk_score"), 0) >= 60
        ],
    }
    return payload


def render_price_volume_structure_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Price / Volume Structure",
        "",
        "This report is a forecast-confirmation layer only. It is not a trading system and does not provide buy/sell/entry/exit/PnL guidance.",
        "",
        f"- version: {payload.get('version')}",
        f"- generated_at: {payload.get('generated_at')}",
        "",
        "| Symbol | Candle | Price structure | Volume confirmation | Reversal | Breakdown risk | Breakout confirmation |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for symbol, item in sorted((payload.get("symbols") or {}).items()):
        candle = (item.get("candle") or {}).get("latest_candle_type", "unknown")
        lines.append(
            f"| {symbol} | {candle} | {_fmt_score(item.get('price_structure_score'))} | "
            f"{_fmt_score(item.get('volume_confirmation_score'))} | {_fmt_score(item.get('reversal_candle_score'))} | "
            f"{_fmt_score(item.get('breakdown_risk_score'))} | {_fmt_score(item.get('breakout_confirmation_score'))} |"
        )
    lines.append("")
    return "\n".join(lines)


def _symbol_structure(symbol: str, series: DownloadedSeries | None) -> dict[str, Any]:
    rows = _rows(series)
    if len(rows) < 30:
        return {
            "symbol": symbol,
            "status": "missing",
            "latest_date": None,
            "data_quality": 0,
            "warning": "Not enough price/volume rows for structure analysis.",
        }

    latest = rows[-1]
    prev = rows[-2]
    close = latest["close"]
    open_ = latest["open"]
    high = latest["high"]
    low = latest["low"]
    volume = latest["volume"]
    range_ = max(high - low, 0.0)
    body = abs(close - open_)
    upper_wick = max(high - max(open_, close), 0.0)
    lower_wick = max(min(open_, close) - low, 0.0)
    close_position = (close - low) / range_ if range_ > 0 else 0.5
    candle_type = "bullish" if close > open_ else "bearish" if close < open_ else "doji"

    ma5 = _sma(rows, 5)
    ma20 = _sma(rows, 20)
    ma50 = _sma(rows, 50)
    ma200 = _sma(rows, 200)
    atr14 = _atr(rows, 14)
    recent_high_5 = _max_high(rows, 5, exclude_latest=True)
    recent_low_5 = _min_low(rows, 5, exclude_latest=True)
    recent_high_10 = _max_high(rows, 10, exclude_latest=True)
    recent_low_10 = _min_low(rows, 10, exclude_latest=True)
    recent_high_20 = _max_high(rows, 20, exclude_latest=True)
    recent_low_20 = _min_low(rows, 20, exclude_latest=True)
    volume_avg20 = _mean([row["volume"] for row in rows[-21:-1] if row["volume"] > 0])
    volume_std20 = _std([row["volume"] for row in rows[-21:-1] if row["volume"] > 0])
    volume_z = (volume - volume_avg20) / volume_std20 if volume_std20 and volume_avg20 else None
    relative_volume20 = volume / volume_avg20 if volume_avg20 else None
    up_volumes = [row["volume"] for row in rows[-20:] if row["close"] >= row["open"] and row["volume"] > 0]
    down_volumes = [row["volume"] for row in rows[-20:] if row["close"] < row["open"] and row["volume"] > 0]
    up_day_volume = _mean(up_volumes)
    down_day_volume = _mean(down_volumes)
    signed_volume = sum((1 if row["close"] >= row["open"] else -1) * row["volume"] for row in rows[-20:])
    total_volume = sum(row["volume"] for row in rows[-20:] if row["volume"] > 0)
    accumulation_distribution_proxy = signed_volume / total_volume if total_volume else None

    long_lower_wick = range_ > 0 and lower_wick / range_ >= 0.35 and lower_wick >= body * 1.5
    long_upper_wick = range_ > 0 and upper_wick / range_ >= 0.35 and upper_wick >= body * 1.5
    bullish_reversal = bool(long_lower_wick and close_position >= 0.58 and close >= open_)
    bearish_reversal = bool(long_upper_wick and close_position <= 0.42 and close <= open_)
    gap_up = prev["close"] > 0 and open_ >= prev["close"] * 1.004
    gap_down = prev["close"] > 0 and open_ <= prev["close"] * 0.996
    high_close = close_position >= 0.72
    low_close = close_position <= 0.28
    failed_breakout = bool(recent_high_20 and high > recent_high_20 and close < recent_high_20)
    reclaim_candle = bool(ma20 and prev["close"] < ma20 and close > ma20 and high_close)
    failed_breakdown_reclaim = bool(recent_low_10 and low < recent_low_10 and close > recent_low_10 and close_position >= 0.55)

    volume_expansion = bool(relative_volume20 is not None and relative_volume20 >= 1.2)
    volume_contraction = bool(relative_volume20 is not None and relative_volume20 <= 0.8)
    panic_volume_proxy = bool(volume_expansion and close < open_ and close_position <= 0.35)
    accumulation_proxy = bool(accumulation_distribution_proxy is not None and accumulation_distribution_proxy > 0.12)
    distribution_proxy = bool(accumulation_distribution_proxy is not None and accumulation_distribution_proxy < -0.12)

    above5 = _above(close, ma5)
    above20 = _above(close, ma20)
    above50 = _above(close, ma50)
    above200 = _above(close, ma200)
    distance_swing_high = _distance(close, recent_high_20)
    distance_swing_low = _distance(close, recent_low_20)

    price_structure_score = _clamp_score(
        42
        + (8 if above5 else -4)
        + (10 if above20 else -6)
        + (8 if above50 else -5)
        + (6 if above200 else -4)
        + (8 if high_close else 0)
        + (8 if reclaim_candle else 0)
        + (6 if failed_breakdown_reclaim else 0)
        - (10 if low_close else 0)
        - (10 if failed_breakout else 0)
    )
    volume_confirmation_score = _clamp_score(
        45
        + (10 if volume_expansion and close >= open_ else 0)
        + (8 if accumulation_proxy else 0)
        + (6 if up_day_volume and down_day_volume and up_day_volume > down_day_volume else 0)
        - (8 if distribution_proxy else 0)
        - (10 if panic_volume_proxy else 0)
        - (4 if volume_contraction else 0)
    )
    reversal_candle_score = _clamp_score(
        25
        + (25 if bullish_reversal else 0)
        + (15 if failed_breakdown_reclaim else 0)
        + (10 if long_lower_wick else 0)
        + (8 if high_close else 0)
        - (12 if bearish_reversal else 0)
    )
    breakdown_risk_score = _clamp_score(
        28
        + (16 if low_close else 0)
        + (14 if failed_breakout else 0)
        + (10 if close < (recent_low_5 or -math.inf) else 0)
        + (8 if not above20 else 0)
        + (8 if distribution_proxy else 0)
        + (8 if panic_volume_proxy else 0)
        - (10 if bullish_reversal else 0)
    )
    breakout_confirmation_score = _clamp_score(
        30
        + (18 if recent_high_20 and close > recent_high_20 else 0)
        + (12 if high_close else 0)
        + (12 if volume_expansion and close >= open_ else 0)
        + (8 if above20 else 0)
        + (8 if above50 else 0)
        - (10 if failed_breakout else 0)
    )

    return {
        "symbol": symbol,
        "status": "available",
        "latest_date": str(latest["date"]),
        "current_price": _round(close),
        "data_quality": _data_quality(rows),
        "candle": {
            "latest_candle_type": candle_type,
            "long_lower_wick": long_lower_wick,
            "long_upper_wick": long_upper_wick,
            "bullish_reversal_candle": bullish_reversal,
            "bearish_reversal_candle": bearish_reversal,
            "gap_up": gap_up,
            "gap_down": gap_down,
            "low_close": low_close,
            "high_close": high_close,
            "failed_breakout": failed_breakout,
            "reclaim_candle": reclaim_candle,
            "failed_breakdown_reclaim": failed_breakdown_reclaim,
            "close_position_in_range": _round(close_position),
        },
        "volume": {
            "volume": _round(volume, 0),
            "volume_z_score": _round(volume_z),
            "volume_vs_20d_average": _round(relative_volume20),
            "volume_expansion": volume_expansion,
            "volume_contraction": volume_contraction,
            "up_day_volume": _round(up_day_volume, 0),
            "down_day_volume": _round(down_day_volume, 0),
            "panic_volume_proxy": panic_volume_proxy,
            "accumulation_distribution_proxy": _round(accumulation_distribution_proxy),
            "accumulation_proxy": accumulation_proxy,
            "distribution_proxy": distribution_proxy,
        },
        "technical_structure": {
            "above_5d_ma": above5,
            "above_20d_ma": above20,
            "above_50d_ma": above50,
            "above_200d_ma": above200,
            "ma5": _round(ma5),
            "ma20": _round(ma20),
            "ma50": _round(ma50),
            "ma200": _round(ma200),
            "distance_to_recent_swing_high": _round(distance_swing_high),
            "distance_to_recent_swing_low": _round(distance_swing_low),
            "recent_breakout_level": _round(recent_high_20),
            "recent_breakdown_level": _round(recent_low_20),
            "recent_high_5d": _round(recent_high_5),
            "recent_low_5d": _round(recent_low_5),
            "recent_high_10d": _round(recent_high_10),
            "recent_low_10d": _round(recent_low_10),
            "recent_high_20d": _round(recent_high_20),
            "recent_low_20d": _round(recent_low_20),
            "atr_14": _round(atr14),
            "atr_pct": _round(atr14 / close if atr14 and close else None),
        },
        "price_structure_score": price_structure_score,
        "volume_confirmation_score": volume_confirmation_score,
        "reversal_candle_score": reversal_candle_score,
        "breakdown_risk_score": breakdown_risk_score,
        "breakout_confirmation_score": breakout_confirmation_score,
        "interpretation": _interpret(symbol, price_structure_score, volume_confirmation_score, reversal_candle_score, breakdown_risk_score),
    }


def _interpret(symbol: str, price_score: int, volume_score: int, reversal_score: int, breakdown_score: int) -> str:
    if breakdown_score >= 65:
        return f"{symbol} K线/成交量结构偏风险，需要观察是否跌破关键失效位。"
    if price_score >= 65 and volume_score >= 55:
        return f"{symbol} 价格结构和成交量对当前主路径有一定确认。"
    if reversal_score >= 60:
        return f"{symbol} 出现反转/回收类K线结构，但仍需要后续价格确认。"
    return f"{symbol} 价格和成交量确认度一般，不能单独支持强判断。"


def _rows(series: DownloadedSeries | None) -> list[dict[str, Any]]:
    if not series:
        return []
    rows: list[dict[str, Any]] = []
    for row in series.rows:
        payload = row if isinstance(row, dict) else vars(row)
        try:
            close = float(payload.get("close") or payload.get("Close"))
        except (TypeError, ValueError):
            continue
        if not math.isfinite(close) or close <= 0:
            continue
        def field(name: str, fallback: float = close) -> float:
            try:
                value = float(payload.get(name) or payload.get(name.title()) or fallback)
            except (TypeError, ValueError):
                value = fallback
            return value if math.isfinite(value) else fallback
        rows.append(
            {
                "date": str(payload.get("date") or payload.get("Date") or ""),
                "open": field("open"),
                "high": max(field("high"), close),
                "low": min(field("low"), close),
                "close": close,
                "volume": max(field("volume", 0.0), 0.0),
            }
        )
    return rows


def _sma(rows: list[dict[str, Any]], window: int) -> float | None:
    if len(rows) < window:
        return None
    return _mean([row["close"] for row in rows[-window:]])


def _atr(rows: list[dict[str, Any]], window: int) -> float | None:
    if len(rows) < window + 1:
        return None
    ranges: list[float] = []
    for index in range(len(rows) - window, len(rows)):
        row = rows[index]
        prev_close = rows[index - 1]["close"]
        ranges.append(max(row["high"] - row["low"], abs(row["high"] - prev_close), abs(row["low"] - prev_close)))
    return _mean(ranges)


def _max_high(rows: list[dict[str, Any]], window: int, exclude_latest: bool = False) -> float | None:
    selected = rows[-window - 1 : -1] if exclude_latest else rows[-window:]
    return max((row["high"] for row in selected), default=None)


def _min_low(rows: list[dict[str, Any]], window: int, exclude_latest: bool = False) -> float | None:
    selected = rows[-window - 1 : -1] if exclude_latest else rows[-window:]
    return min((row["low"] for row in selected), default=None)


def _above(price: float, level: float | None) -> bool:
    return bool(level is not None and price > level)


def _distance(price: float, level: float | None) -> float | None:
    if level is None or level == 0:
        return None
    return price / level - 1.0


def _mean(values: list[float | None]) -> float | None:
    clean = [float(value) for value in values if value is not None and math.isfinite(float(value))]
    return sum(clean) / len(clean) if clean else None


def _std(values: list[float]) -> float | None:
    mean = _mean(values)
    if mean is None or len(values) < 2:
        return None
    variance = sum((value - mean) ** 2 for value in values) / (len(values) - 1)
    return math.sqrt(variance) if variance > 0 else None


def _num(value: Any, default: float | None = None) -> float | None:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return default
    return parsed if math.isfinite(parsed) else default


def _round(value: Any, digits: int = 4) -> float | None:
    parsed = _num(value)
    return round(parsed, digits) if parsed is not None else None


def _clamp_score(value: float) -> int:
    return int(round(max(0.0, min(100.0, value))))


def _data_quality(rows: list[dict[str, Any]]) -> int:
    length_score = min(100, len(rows) / 220 * 100)
    volume_available = sum(1 for row in rows[-60:] if row.get("volume", 0) > 0) / max(1, min(60, len(rows))) * 100
    return _clamp_score(length_score * 0.55 + volume_available * 0.45)


def _fmt_score(value: Any) -> str:
    parsed = _num(value)
    return "NA" if parsed is None else f"{parsed:.0f}/100"


def main() -> int:
    series = refresh_market_data(symbols=SYMBOLS, lookback_days=320)
    payload = build_price_volume_structure({item.symbol: item for item in series})
    public_path = PROJECT_ROOT / "frontend" / "public" / "price-volume-structure.json"
    output_path = PROJECT_ROOT / "outputs" / "price_volume_structure.md"
    public_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    public_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    output_path.write_text(render_price_volume_structure_markdown(payload), encoding="utf-8")
    print("wrote frontend/public/price-volume-structure.json")
    print("wrote outputs/price_volume_structure.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
