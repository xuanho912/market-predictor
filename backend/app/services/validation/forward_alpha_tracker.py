from __future__ import annotations

import csv
import math
import os
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable


BACKEND_ROOT = Path(__file__).resolve().parents[3]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

SIGNAL_NAME = "bounce_probability_top_decile_v1"
SIGNAL_VERSION = "alpha_v1"
FROZEN_ON = "2026-06-13"
FROZEN_BOUNCE_THRESHOLD = 0.32534311
ALPHA_STATUS = "RESEARCH ALPHA CANDIDATE"
SUPPORTED_SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
FORWARD_HORIZONS = (3, 5, 10, 20, 60)
VALIDATION_PERIOD = "forward_only"
RISK_NOTE = "Research alpha candidate only. Forecast validation only; not an execution recommendation."

CSV_FIELDS = [
    "signal_date",
    "symbol",
    "bounce_probability",
    "threshold_used",
    "regime",
    "close_price",
    "forward_return_3d",
    "forward_return_5d",
    "forward_return_10d",
    "forward_return_20d",
    "forward_return_60d",
    "max_adverse_excursion",
    "max_favorable_excursion",
    "signal_status",
    "validation_period",
]

CHECK_FIELDS = [
    "check_date",
    "symbol",
    "bounce_probability",
    "threshold_used",
    "distance_to_threshold",
    "live_signal",
    "regime",
    "close_price",
    "data_source_status",
    "signal_blocked_reason",
    "validation_period",
]


@dataclass(frozen=True)
class ForwardAlphaSignal:
    signal_date: str
    symbol: str
    bounce_probability: float
    threshold_used: float
    regime: str
    close_price: float | None

    def to_row(self) -> dict[str, str]:
        row = {field: "" for field in CSV_FIELDS}
        row.update(
            {
                "signal_date": self.signal_date,
                "symbol": self.symbol,
                "bounce_probability": f"{self.bounce_probability:.8f}",
                "threshold_used": f"{self.threshold_used:.8f}",
                "regime": self.regime,
                "close_price": "" if self.close_price is None else f"{self.close_price:.8f}",
                "signal_status": "pending",
                "validation_period": VALIDATION_PERIOD,
            }
        )
        return row


def default_outputs_dir() -> Path:
    configured = os.getenv("ALPHA_OUTPUT_DIR")
    if configured:
        return Path(configured)
    return Path(__file__).resolve().parents[4] / "outputs"


def default_signals_path() -> Path:
    return default_outputs_dir() / "forward_alpha_v1_signals.csv"


def default_checks_path() -> Path:
    return default_outputs_dir() / "forward_alpha_v1_daily_checks.csv"


def default_report_path() -> Path:
    return default_outputs_dir() / "forward_alpha_v1_report.md"


def ensure_signal_file(path: Path | None = None) -> Path:
    signals_path = path or default_signals_path()
    signals_path.parent.mkdir(parents=True, exist_ok=True)
    if not signals_path.exists():
        with signals_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
            writer.writeheader()
    return signals_path


def ensure_check_file(path: Path | None = None) -> Path:
    checks_path = path or default_checks_path()
    checks_path.parent.mkdir(parents=True, exist_ok=True)
    if not checks_path.exists():
        with checks_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=CHECK_FIELDS)
            writer.writeheader()
    return checks_path


def load_signal_rows(path: Path | None = None) -> list[dict[str, str]]:
    signals_path = ensure_signal_file(path)
    with signals_path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def save_signal_rows(rows: list[dict[str, str]], path: Path | None = None) -> None:
    signals_path = ensure_signal_file(path)
    with signals_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in CSV_FIELDS})


def load_check_rows(path: Path | None = None) -> list[dict[str, str]]:
    checks_path = ensure_check_file(path)
    with checks_path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def save_check_rows(rows: list[dict[str, str]], path: Path | None = None) -> None:
    checks_path = ensure_check_file(path)
    with checks_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CHECK_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in CHECK_FIELDS})


def read_value(prediction: Any, name: str, default: Any = None) -> Any:
    if isinstance(prediction, dict):
        return prediction.get(name, default)
    return getattr(prediction, name, default)


def normalize_signal_date(value: Any) -> str:
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    return str(value)[:10]


def signal_from_prediction(
    prediction: Any,
    *,
    close_price: float | None = None,
    signal_date: str | None = None,
    threshold: float = FROZEN_BOUNCE_THRESHOLD,
) -> ForwardAlphaSignal | None:
    symbol = str(read_value(prediction, "symbol", "")).upper()
    if symbol not in SUPPORTED_SYMBOLS:
        return None

    bounce_probability = float(read_value(prediction, "bounce_probability", 0.0))
    if bounce_probability < threshold:
        return None

    signal_date = signal_date or normalize_signal_date(
        read_value(prediction, "forecast_timestamp", read_value(prediction, "timestamp", ""))
    )
    regime = str(read_value(prediction, "market_regime", read_value(prediction, "regime", "unknown")))
    return ForwardAlphaSignal(
        signal_date=signal_date,
        symbol=symbol,
        bounce_probability=bounce_probability,
        threshold_used=threshold,
        regime=regime,
        close_price=close_price,
    )


def append_latest_predictions(
    predictions: Iterable[Any],
    *,
    close_prices: dict[tuple[str, str], float] | None = None,
    signal_dates: dict[str, str] | None = None,
    path: Path | None = None,
    threshold: float = FROZEN_BOUNCE_THRESHOLD,
) -> list[ForwardAlphaSignal]:
    rows = load_signal_rows(path)
    seen = {(row["signal_date"], row["symbol"]) for row in rows}
    appended: list[ForwardAlphaSignal] = []

    for prediction in predictions:
        symbol = str(read_value(prediction, "symbol", "")).upper()
        signal_date = normalize_signal_date(
            read_value(prediction, "forecast_timestamp", read_value(prediction, "timestamp", ""))
        )
        if signal_dates and symbol in signal_dates:
            signal_date = signal_dates[symbol]
        close_price = close_prices.get((signal_date, symbol)) if close_prices else None
        signal = signal_from_prediction(
            prediction,
            close_price=close_price,
            signal_date=signal_date,
            threshold=threshold,
        )
        if signal is None or (signal.signal_date, signal.symbol) in seen:
            continue
        rows.append(signal.to_row())
        seen.add((signal.signal_date, signal.symbol))
        appended.append(signal)

    save_signal_rows(rows, path)
    return appended


def record_daily_checks(
    predictions: Iterable[Any],
    *,
    close_prices: dict[tuple[str, str], float] | None = None,
    signal_dates: dict[str, str] | None = None,
    path: Path | None = None,
    threshold: float = FROZEN_BOUNCE_THRESHOLD,
    allow_signal: bool = True,
    data_source_status: str = "live_yfinance",
    signal_blocked_reason: str = "",
) -> list[dict[str, str]]:
    rows = load_check_rows(path)
    by_key = {(row["check_date"], row["symbol"]): row for row in rows}
    for prediction in predictions:
        symbol = str(read_value(prediction, "symbol", "")).upper()
        if symbol not in SUPPORTED_SYMBOLS:
            continue
        check_date = normalize_signal_date(
            read_value(prediction, "forecast_timestamp", read_value(prediction, "timestamp", ""))
        )
        if signal_dates and symbol in signal_dates:
            check_date = signal_dates[symbol]
        close_price = close_prices.get((check_date, symbol)) if close_prices else None
        bounce_probability = float(read_value(prediction, "bounce_probability", 0.0))
        regime = str(read_value(prediction, "market_regime", read_value(prediction, "regime", "unknown")))
        by_key[(check_date, symbol)] = {
            "check_date": check_date,
            "symbol": symbol,
            "bounce_probability": f"{bounce_probability:.8f}",
            "threshold_used": f"{threshold:.8f}",
            "distance_to_threshold": f"{threshold - bounce_probability:.8f}",
            "live_signal": str(allow_signal and bounce_probability >= threshold).lower(),
            "regime": regime,
            "close_price": "" if close_price is None else f"{close_price:.8f}",
            "data_source_status": data_source_status,
            "signal_blocked_reason": signal_blocked_reason,
            "validation_period": VALIDATION_PERIOD,
        }
    updated = [by_key[key] for key in sorted(by_key)]
    save_check_rows(updated, path)
    return updated


def update_completed_signals(
    price_history: dict[str, dict[str, float]],
    *,
    path: Path | None = None,
) -> list[dict[str, str]]:
    rows = load_signal_rows(path)
    changed = False
    for row in rows:
        if row.get("signal_status") == "completed":
            continue
        symbol = row["symbol"]
        history = price_history.get(symbol, {})
        ordered_dates = sorted(history)
        if row["signal_date"] not in history:
            continue
        start_index = ordered_dates.index(row["signal_date"])
        if start_index + max(FORWARD_HORIZONS) >= len(ordered_dates):
            continue
        start_price = _row_float(row, "close_price") or history[row["signal_date"]]
        future_prices = [
            history[ordered_dates[index]]
            for index in range(start_index + 1, start_index + max(FORWARD_HORIZONS) + 1)
        ]
        for horizon in FORWARD_HORIZONS:
            end_price = history[ordered_dates[start_index + horizon]]
            row[f"forward_return_{horizon}d"] = f"{end_price / start_price - 1.0:.8f}"
        path_returns = [price / start_price - 1.0 for price in future_prices]
        row["max_adverse_excursion"] = f"{min(path_returns):.8f}"
        row["max_favorable_excursion"] = f"{max(path_returns):.8f}"
        row["signal_status"] = "completed"
        row["validation_period"] = VALIDATION_PERIOD
        changed = True
    if changed:
        save_signal_rows(rows, path)
    return rows


def forward_performance(path: Path | None = None) -> dict[str, Any]:
    rows = load_signal_rows(path)
    completed = [row for row in rows if row.get("signal_status") == "completed"]
    pending = [row for row in rows if row.get("signal_status") != "completed"]
    by_horizon = {
        f"{horizon}d": _return_metrics([_row_float(row, f"forward_return_{horizon}d") for row in completed])
        for horizon in FORWARD_HORIZONS
    }
    return {
        "signal_name": SIGNAL_NAME,
        "signal_version": SIGNAL_VERSION,
        "frozen_on": FROZEN_ON,
        "threshold_used": FROZEN_BOUNCE_THRESHOLD,
        "alpha_status": ALPHA_STATUS,
        "signal_count": len(rows),
        "completed_count": len(completed),
        "pending_count": len(pending),
        "by_horizon": by_horizon,
        "by_symbol": _group_metrics(completed, "symbol"),
        "by_regime": _group_metrics(completed, "regime"),
        "by_month": _month_metrics(completed),
    }


def alpha_status_payload() -> dict[str, Any]:
    signal_rows = load_signal_rows()
    check_rows = load_check_rows()
    pending = [row for row in signal_rows if row.get("signal_status") == "pending"]
    latest_date = max((row["check_date"] for row in check_rows), default=None)
    latest_checks = [row for row in check_rows if row.get("check_date") == latest_date] if latest_date else []
    latest_by_symbol = {row["symbol"]: _safe_float(row.get("bounce_probability")) for row in latest_checks}
    distance_by_symbol = {row["symbol"]: _safe_float(row.get("distance_to_threshold")) for row in latest_checks}
    data_source_status = latest_checks[0].get("data_source_status") if latest_checks else None
    signal_blocked_reason = latest_checks[0].get("signal_blocked_reason") if latest_checks else None
    live_signal = bool(pending)
    return {
        "signal_name": SIGNAL_NAME,
        "signal_version": SIGNAL_VERSION,
        "status": ALPHA_STATUS,
        "live_signal": live_signal,
        "forecast_signal": live_signal,
        "threshold": FROZEN_BOUNCE_THRESHOLD,
        "latest_checked_date": latest_date,
        "latest_bounce_probability_by_symbol": latest_by_symbol,
        "distance_to_threshold_by_symbol": distance_by_symbol,
        "expected_validation_horizons": [f"{horizon}d" for horizon in FORWARD_HORIZONS],
        "risk_note": RISK_NOTE,
        "data_source_status": data_source_status,
        "signal_blocked_reason": signal_blocked_reason,
        "live_signals": [_public_signal(row) for row in pending],
        "forecast_signals": [_public_signal(row) for row in pending],
        "no_signal": None if live_signal else "no forecast signal",
        "validation_period": VALIDATION_PERIOD,
    }


def latest_alpha_payload() -> dict[str, Any]:
    return alpha_status_payload()


def signal_rows_payload() -> dict[str, Any]:
    rows = load_signal_rows()
    return {
        "signal_name": SIGNAL_NAME,
        "status": ALPHA_STATUS,
        "threshold": FROZEN_BOUNCE_THRESHOLD,
        "signals": [_public_signal(row) for row in rows],
    }


def report_payload() -> dict[str, Any]:
    report_path = default_report_path()
    report_text = report_path.read_text(encoding="utf-8") if report_path.exists() else ""
    return {
        "signal_name": SIGNAL_NAME,
        "status": ALPHA_STATUS,
        "threshold": FROZEN_BOUNCE_THRESHOLD,
        "performance": forward_performance(),
        "report_markdown": report_text,
    }


def run_daily_forward_observation() -> dict[str, Any]:
    from app.db.storage import save_prediction
    from app.services.data_providers.auto_download import is_real_market_data, refresh_market_data
    from app.services.prediction_engine import SUPPORTED_SYMBOLS as ENGINE_SYMBOLS
    from app.services.prediction_engine import build_prediction

    symbols = tuple(ENGINE_SYMBOLS)
    downloaded = refresh_market_data(symbols=symbols + ("^VIX", "^TNX", "HYG", "LQD"))
    source_by_symbol = {series.symbol: series.source for series in downloaded}
    real_by_symbol = {series.symbol: is_real_market_data(series) for series in downloaded}
    live_data_ready = all(real_by_symbol.get(symbol, False) for symbol in symbols)
    data_source_status = "real_market_data" if live_data_ready else "synthetic_fallback_no_signal"
    signal_blocked_reason = "" if live_data_ready else "real market data unavailable; synthetic fallback cannot create alpha_v1 signals"
    price_history = {
        series.symbol: {
            str(row["date"]): float(row["close"])
            for row in series.rows
            if series.symbol in symbols and "date" in row and "close" in row
        }
        for series in downloaded
        if series.symbol in symbols
    }
    signal_dates = {symbol: max(history) for symbol, history in price_history.items() if history}
    close_prices = {
        (latest_date, symbol): price_history[symbol][latest_date]
        for symbol, latest_date in signal_dates.items()
    }

    predictions = [build_prediction(symbol) for symbol in symbols]
    for prediction in predictions:
        save_prediction(prediction)

    checks = record_daily_checks(
        predictions,
        close_prices=close_prices,
        signal_dates=signal_dates,
        allow_signal=live_data_ready,
        data_source_status=data_source_status,
        signal_blocked_reason=signal_blocked_reason,
    )
    appended = []
    if live_data_ready:
        appended = append_latest_predictions(predictions, close_prices=close_prices, signal_dates=signal_dates)
        update_completed_signals(price_history)
    write_forward_report()
    return {
        "status": ALPHA_STATUS,
        "signal_name": SIGNAL_NAME,
        "threshold": FROZEN_BOUNCE_THRESHOLD,
        "checked_symbols": list(symbols),
        "latest_checked_date": max(signal_dates.values()) if signal_dates else None,
        "new_signal_count": len(appended),
        "new_signals": [signal.to_row() for signal in appended],
        "live_signal": bool(appended) or alpha_status_payload()["live_signal"],
        "forecast_signal": bool(appended) or alpha_status_payload()["live_signal"],
        "daily_check_count": len(checks),
        "data_source_status": data_source_status,
        "data_sources": {symbol: source_by_symbol.get(symbol, "missing") for symbol in symbols},
        "signal_blocked_reason": signal_blocked_reason,
        "validation_period": VALIDATION_PERIOD,
    }


def write_forward_report(path: Path | None = None) -> Path:
    report_path = path or default_report_path()
    performance = forward_performance()
    status = alpha_status_payload()
    signal_rows = load_signal_rows()
    completed = [row for row in signal_rows if row.get("signal_status") == "completed"]
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Forward Alpha v1 Report",
        "",
        f"Signal: `{SIGNAL_NAME}`",
        f"Frozen on: {FROZEN_ON}",
        f"Threshold used: `{FROZEN_BOUNCE_THRESHOLD:.8f}`",
        f"Validation period: `{VALIDATION_PERIOD}`",
        "",
        f"## FORWARD ALPHA STATUS: {ALPHA_STATUS}",
        "",
        "Alpha v1 remains a frozen research candidate until enough post-freeze observations mature.",
        "",
        "## Summary",
        "",
        f"- signal count: {performance['signal_count']}",
        f"- pending signals: {performance['pending_count']}",
        f"- completed signals: {performance['completed_count']}",
        f"- forecast signal: {str(status['live_signal']).lower()}",
        f"- latest checked date: {status['latest_checked_date'] or 'n/a'}",
        f"- data source status: {status.get('data_source_status') or 'n/a'}",
        f"- signal blocked reason: {status.get('signal_blocked_reason') or 'n/a'}",
        "",
        "## Latest Check",
        "",
        _render_latest_check_table(status),
        "",
        "## Average Return By Horizon",
        "",
        _render_horizon_table(performance["by_horizon"]),
        "",
        "## Max Adverse / Favorable Excursion",
        "",
        _render_excursion_summary(completed),
        "",
        "## Performance By Symbol",
        "",
        _render_group_summary(performance["by_symbol"]),
        "",
        "## Performance By Regime",
        "",
        _render_group_summary(performance["by_regime"]),
        "",
        "## Performance By Year/Month",
        "",
        _render_month_summary(performance["by_month"]),
        "",
        "## Historical Alpha Character Check",
        "",
        "Forward validation has not confirmed alpha v1. Treat it only as a bounce scenario input until completed forward observations are sufficient and stable.",
    ]
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def _public_signal(row: dict[str, str]) -> dict[str, Any]:
    return {
        "symbol": row.get("symbol"),
        "signal_date": row.get("signal_date"),
        "bounce_probability": _safe_float(row.get("bounce_probability")),
        "threshold_used": _safe_float(row.get("threshold_used")),
        "regime": row.get("regime"),
        "close_price": _safe_float(row.get("close_price")),
        "expected_validation_horizons": [f"{horizon}d" for horizon in FORWARD_HORIZONS],
        "signal_status": row.get("signal_status"),
        "validation_period": row.get("validation_period", VALIDATION_PERIOD),
        "risk_note": RISK_NOTE,
    }


def _safe_float(value: str | None) -> float | None:
    if value in (None, ""):
        return None
    return float(value)


def _row_float(row: dict[str, str], field: str) -> float | None:
    value = row.get(field, "")
    if value == "":
        return None
    return float(value)


def _return_metrics(values: list[float | None]) -> dict[str, float | int | None]:
    clean = [value for value in values if value is not None and math.isfinite(value)]
    if not clean:
        return {"count": 0, "average_return": None, "median_return": None, "hit_rate": None, "t_stat": None}
    ordered = sorted(clean)
    mid = len(ordered) // 2
    median = ordered[mid] if len(ordered) % 2 else (ordered[mid - 1] + ordered[mid]) / 2.0
    avg = sum(clean) / len(clean)
    variance = sum((value - avg) ** 2 for value in clean) / (len(clean) - 1) if len(clean) > 1 else 0.0
    stdev = math.sqrt(variance)
    t_stat = avg / (stdev / math.sqrt(len(clean))) if len(clean) > 1 and stdev > 0 else None
    return {
        "count": len(clean),
        "average_return": avg,
        "median_return": median,
        "hit_rate": sum(1 for value in clean if value > 0) / len(clean),
        "t_stat": t_stat,
    }


def _group_metrics(rows: list[dict[str, str]], field: str) -> dict[str, Any]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row.get(field, "unknown"), []).append(row)
    return {
        key: {
            f"{horizon}d": _return_metrics([_row_float(row, f"forward_return_{horizon}d") for row in values])
            for horizon in FORWARD_HORIZONS
        }
        for key, values in sorted(grouped.items())
    }


def _month_metrics(rows: list[dict[str, str]]) -> dict[str, Any]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["signal_date"][:7], []).append(row)
    return {
        month: {
            "signal_count": len(values),
            "forward_return_20d": _return_metrics([_row_float(row, "forward_return_20d") for row in values]),
        }
        for month, values in sorted(grouped.items())
    }


def _fmt_pct(value: Any) -> str:
    if value is None:
        return "n/a"
    return f"{float(value) * 100:.3f}%"


def _fmt_num(value: Any) -> str:
    if value is None:
        return "n/a"
    return f"{float(value):.3f}"


def _markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return "n/a"
    header = rows[0]
    return "\n".join(
        ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
        + ["| " + " | ".join(row) + " |" for row in rows[1:]]
    )


def _render_latest_check_table(status: dict[str, Any]) -> str:
    rows = [["Symbol", "Bounce probability", "Distance to threshold"]]
    latest = status["latest_bounce_probability_by_symbol"]
    distance = status["distance_to_threshold_by_symbol"]
    if not latest:
        return "No daily check has been recorded yet."
    for symbol in SUPPORTED_SYMBOLS:
        rows.append([symbol, _fmt_pct(latest.get(symbol)), _fmt_pct(distance.get(symbol))])
    return _markdown_table(rows)


def _render_horizon_table(by_horizon: dict[str, Any]) -> str:
    rows = [["Horizon", "Count", "Average", "Median", "Hit rate", "t-stat"]]
    for horizon in [f"{value}d" for value in FORWARD_HORIZONS]:
        metrics = by_horizon.get(horizon, {})
        rows.append(
            [
                horizon,
                str(metrics.get("count", 0)),
                _fmt_pct(metrics.get("average_return")),
                _fmt_pct(metrics.get("median_return")),
                _fmt_pct(metrics.get("hit_rate")),
                _fmt_num(metrics.get("t_stat")),
            ]
        )
    return _markdown_table(rows)


def _render_excursion_summary(rows: list[dict[str, str]]) -> str:
    adverse = [_row_float(row, "max_adverse_excursion") for row in rows]
    favorable = [_row_float(row, "max_favorable_excursion") for row in rows]
    adverse_clean = [value for value in adverse if value is not None]
    favorable_clean = [value for value in favorable if value is not None]
    if not adverse_clean or not favorable_clean:
        return "- max adverse excursion: n/a\n- max favorable excursion: n/a"
    return "\n".join(
        [
            f"- max adverse excursion: {_fmt_pct(min(adverse_clean))}",
            f"- max favorable excursion: {_fmt_pct(max(favorable_clean))}",
        ]
    )


def _render_group_summary(groups: dict[str, Any]) -> str:
    if not groups:
        return "n/a"
    rows = [["Group", "3d avg", "5d avg", "10d avg", "20d avg", "60d avg"]]
    for name, metrics in groups.items():
        rows.append(
            [
                name,
                _fmt_pct(metrics.get("3d", {}).get("average_return")),
                _fmt_pct(metrics.get("5d", {}).get("average_return")),
                _fmt_pct(metrics.get("10d", {}).get("average_return")),
                _fmt_pct(metrics.get("20d", {}).get("average_return")),
                _fmt_pct(metrics.get("60d", {}).get("average_return")),
            ]
        )
    return _markdown_table(rows)


def _render_month_summary(months: dict[str, Any]) -> str:
    if not months:
        return "n/a"
    rows = [["Month", "Signals", "20d avg"]]
    for month, metrics in months.items():
        rows.append(
            [
                month,
                str(metrics.get("signal_count", 0)),
                _fmt_pct(metrics.get("forward_return_20d", {}).get("average_return")),
            ]
        )
    return _markdown_table(rows)


def main() -> int:
    result = run_daily_forward_observation()
    print(f"signal_name={result['signal_name']}")
    print(f"status={result['status']}")
    print(f"threshold={result['threshold']:.8f}")
    print(f"latest_checked_date={result['latest_checked_date']}")
    print(f"new_signal_count={result['new_signal_count']}")
    print(f"forecast_signal={str(result['live_signal']).lower()}")
    print(f"data_source_status={result['data_source_status']}")
    if result["signal_blocked_reason"]:
        print(f"signal_blocked_reason={result['signal_blocked_reason']}")
    print(f"validation_period={result['validation_period']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
