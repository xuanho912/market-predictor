from __future__ import annotations

import csv
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
HORIZONS = (3, 5, 10, 20, 60)
BASELINE_MODEL_VERSION = "baseline_v1"

FORECAST_FIELDS = [
    "forecast_id",
    "forecast_date",
    "model_version",
    "data_version",
    "symbol",
    "current_price",
    "primary_scenario",
    "primary_probability",
    "secondary_scenario",
    "secondary_probability",
    "risk_scenario",
    "risk_scenario_probability",
    "probability_gap",
    "close_call",
    "edge_status",
    "signal_confirmation_score",
    "model_confidence",
    "data_completeness",
    "strongest_predictor",
    "supporting_signals",
    "conflicting_signals",
    "missing_data",
    "invalidation_conditions",
    "forecast_horizons",
    "expected_return_by_horizon",
    "scenario_expected_return_by_horizon",
    "breadth_confirmation_score",
    "breadth_conflict_score",
    "options_confirmation_score",
    "options_conflict_score",
    "flow_confirmation_score",
    "flow_conflict_score",
]

OUTCOME_FIELDS = []
for horizon in HORIZONS:
    OUTCOME_FIELDS.extend(
        [
            f"actual_return_{horizon}d",
            f"best_matching_scenario_{horizon}d",
            f"primary_hit_{horizon}d",
            f"path_error_{horizon}d",
        ]
    )
OUTCOME_FIELDS.append("status")

CSV_FIELDS = FORECAST_FIELDS + OUTCOME_FIELDS


def update_forecast_accuracy_ledger(
    *,
    dashboard: dict[str, Any],
    price_history: dict[str, list[dict[str, Any]]],
    records_path: Path | None = None,
) -> dict[str, Any]:
    records_path = records_path or PROJECT_ROOT / "outputs" / "forecast_records.csv"
    records_path.parent.mkdir(parents=True, exist_ok=True)

    existing = _read_records(records_path)
    by_id = {row.get("forecast_id"): row for row in existing if row.get("forecast_id")}
    new_rows: list[dict[str, Any]] = []

    for symbol in SYMBOLS:
        record = _build_forecast_record(dashboard, symbol)
        if not record:
            continue
        forecast_id = record["forecast_id"]
        if forecast_id in by_id:
            preserved = {field: by_id[forecast_id].get(field, "") for field in CSV_FIELDS}
            new_rows.append(preserved)
        else:
            new_rows.append(record)

    merged_by_id = {row.get("forecast_id"): {field: row.get(field, "") for field in CSV_FIELDS} for row in existing if row.get("forecast_id")}
    for row in new_rows:
        merged_by_id.setdefault(row["forecast_id"], row)

    merged_rows = list(merged_by_id.values())
    for row in merged_rows:
        _backfill_outcomes(row, price_history)

    merged_rows.sort(key=lambda row: (str(row.get("forecast_date") or ""), str(row.get("symbol") or "")))
    _write_records(records_path, merged_rows)
    return {
        "version": "forecast_accuracy_ledger_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "active_model_version": BASELINE_MODEL_VERSION,
        "records_path": str(records_path),
        "total_records": len(merged_rows),
        "new_records_considered": len(new_rows),
        "pending_records": sum(1 for row in merged_rows if row.get("status") != "completed"),
        "completed_by_horizon": {
            f"{horizon}d": sum(1 for row in merged_rows if _float(row.get(f"actual_return_{horizon}d")) is not None)
            for horizon in HORIZONS
        },
        "immutability_note": "Forecast fields are write-once by forecast_id. Backfill may update only actual_return, best_matching_scenario, primary_hit, path_error and status fields.",
        "not_trading_note": "This is a forecast accuracy ledger, not a paper-trading, execution or PnL ledger.",
    }


def export_forecast_records_json(records_path: Path | None = None, *, limit: int = 1000) -> dict[str, Any]:
    records_path = records_path or PROJECT_ROOT / "outputs" / "forecast_records.csv"
    rows = _read_records(records_path)
    parsed = [_parse_public_row(row) for row in rows[-limit:]]
    return {
        "version": "forecast_records_public_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total_records": len(rows),
            "exported_records": len(parsed),
            "pending_records": sum(1 for row in rows if row.get("status") != "completed"),
            "model_versions": sorted({str(row.get("model_version") or "unknown") for row in rows}),
            "active_model_version": BASELINE_MODEL_VERSION,
            "completed_by_horizon": {
                f"{horizon}d": sum(1 for row in rows if _float(row.get(f"actual_return_{horizon}d")) is not None)
                for horizon in HORIZONS
            },
        },
        "records": parsed,
    }


def build_forecast_accuracy_scorecard(records_path: Path | None = None) -> dict[str, Any]:
    records_path = records_path or PROJECT_ROOT / "outputs" / "forecast_records.csv"
    rows = _read_records(records_path)
    by_horizon = {f"{horizon}d": _horizon_scorecard(rows, horizon) for horizon in HORIZONS}
    completed_counts = [by_horizon[f"{horizon}d"]["completed_count"] for horizon in HORIZONS]
    strongest_completed_count = max(completed_counts) if completed_counts else 0
    current_evidence_level = _sample_gate(strongest_completed_count)
    return {
        "version": "forecast_accuracy_scorecard_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sample_counts": {
            "total_forecasts": len(rows),
            "pending_forecasts": sum(1 for row in rows if row.get("status") != "completed"),
            **{f"completed_{horizon}d": by_horizon[f"{horizon}d"]["completed_count"] for horizon in HORIZONS},
        },
        "current_evidence_level": current_evidence_level,
        "validation_warning": (
            "当前预测准确度仍未被前向样本验证，不能称为 high precision / stable alpha / validated forecasting system。"
            if current_evidence_level == "insufficient_samples"
            else "Forward validation evidence is accumulating; do not promote models without horizon-specific proof."
        ),
        "primary_scenario_accuracy": by_horizon,
        "by_scenario": _bucket_scorecards(rows, "primary_scenario"),
        "by_edge_status": _bucket_scorecards(rows, "edge_status"),
        "confidence_validation": {
            "signal_confirmation_top_10": _bucket_scorecards(_top_fraction(rows, "signal_confirmation_score", 0.10), "all"),
            "confidence_top_10": _bucket_scorecards(_top_fraction(rows, "model_confidence", 0.10), "all"),
            "high_data_completeness": _bucket_scorecards([row for row in rows if (_float(row.get("data_completeness")) or 0.0) >= 85.0], "all"),
            "low_data_completeness": _bucket_scorecards([row for row in rows if (_float(row.get("data_completeness")) or 0.0) < 85.0], "all"),
            "breadth_confirmed": _bucket_scorecards([row for row in rows if (_float(row.get("breadth_confirmation_score")) or 0.0) >= 55.0], "all"),
            "breadth_conflicted": _bucket_scorecards([row for row in rows if (_float(row.get("breadth_conflict_score")) or 0.0) >= 55.0], "all"),
            "options_confirmed": _bucket_scorecards([row for row in rows if (_float(row.get("options_confirmation_score")) or 0.0) >= 55.0], "all"),
            "options_conflicted": _bucket_scorecards([row for row in rows if (_float(row.get("options_conflict_score")) or 0.0) >= 55.0], "all"),
            "flow_confirmed": _bucket_scorecards([row for row in rows if (_float(row.get("flow_confirmation_score")) or 0.0) >= 58.0], "all"),
            "flow_conflicted": _bucket_scorecards([row for row in rows if (_float(row.get("flow_conflict_score")) or 0.0) >= 55.0], "all"),
        },
        "core_questions": {
            "edge_vs_no_edge": _edge_comparison(rows),
            "high_confidence_better": _high_confidence_comparison(rows),
            "primary_beats_secondary": _primary_secondary_overall(rows),
        },
        "sample_gate_rules": {
            "sample_lt_20": "insufficient_samples",
            "sample_20_50": "early_evidence",
            "sample_50_100": "moderate_evidence",
            "sample_gt_100": "stronger_evidence",
        },
        "guardrails": [
            "This scorecard validates probabilistic forecast paths, not trades.",
            "Forecast records are immutable except for future-outcome backfill fields.",
            "Different horizons are scored separately.",
            "If high-confidence buckets do not beat ordinary buckets, model confidence must remain capped.",
        ],
    }


def render_forecast_accuracy_scorecard_markdown(scorecard: dict[str, Any]) -> str:
    lines = [
        "# Forecast Accuracy Scorecard",
        "",
        f"Generated at: `{scorecard.get('generated_at')}`",
        "",
        "## Sample Counts",
        "",
    ]
    for key, value in (scorecard.get("sample_counts") or {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            f"- current_evidence_level: `{scorecard.get('current_evidence_level')}`",
            f"- validation_warning: {scorecard.get('validation_warning')}",
        ]
    )
    lines.extend(["", "## Primary Scenario Accuracy", ""])
    for horizon, payload in (scorecard.get("primary_scenario_accuracy") or {}).items():
        lines.append(f"### {horizon}")
        for key in (
            "completed_count",
            "sample_gate",
            "primary_scenario_hit_rate",
            "primary_path_mean_absolute_error",
            "primary_path_median_absolute_error",
            "secondary_scenario_hit_rate",
            "primary_vs_secondary_accuracy_spread",
            "primary_closer_than_secondary_rate",
            "close_call_primary_closer_rate",
        ):
            lines.append(f"- {key}: `{payload.get(key)}`")
        lines.append("")
    lines.extend(["## Core Questions", ""])
    for key, value in (scorecard.get("core_questions") or {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- This validates forecast accuracy, not paper trading, PnL or execution.",
            "- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.",
            "",
        ]
    )
    return "\n".join(lines)


def _build_forecast_record(dashboard: dict[str, Any], symbol: str) -> dict[str, Any] | None:
    overview_symbol = (((dashboard.get("overview") or {}).get("symbols") or {}).get(symbol)) or {}
    simulated_symbol = (((dashboard.get("simulated_paths") or {}).get("symbols") or {}).get(symbol)) or {}
    if not overview_symbol or not simulated_symbol:
        return None
    ranking = simulated_symbol.get("scenario_ranking") or {}
    primary = ranking.get("primary") or {}
    secondary = ranking.get("secondary") or {}
    risk_scenario = ranking.get("risk_scenario")
    all_scenarios = ranking.get("all_scenarios") or []
    risk_payload = next((item for item in all_scenarios if item.get("scenario") == risk_scenario), {})
    confidence = simulated_symbol.get("model_confidence") or {}
    edge = simulated_symbol.get("market_edge_status") or {}
    confirmation = simulated_symbol.get("signal_confirmation") or {}
    predictors = simulated_symbol.get("predictors_v4") or simulated_symbol.get("predictors") or {}
    features = simulated_symbol.get("feature_snapshot_v3") or {}
    breadth = features.get("breadth") or {}
    vol = features.get("volatility_options") or {}
    flow = features.get("flow_positioning_proxy") or {}
    data_quality = dashboard.get("data_quality_report") or {}
    summary = data_quality.get("summary") or {}
    forecast_date = str(simulated_symbol.get("as_of") or overview_symbol.get("as_of") or dashboard.get("as_of") or "")[:10]
    model_version = BASELINE_MODEL_VERSION
    data_version = f"{summary.get('latest_date') or forecast_date}|completeness={summary.get('data_completeness_score')}"
    forecast_id = _forecast_id(forecast_date, model_version, symbol)
    expected_by_horizon = _expected_return_by_horizon(simulated_symbol)
    scenario_returns = _scenario_expected_returns(simulated_symbol)
    row = {
        "forecast_id": forecast_id,
        "forecast_date": forecast_date,
        "model_version": model_version,
        "data_version": data_version,
        "symbol": symbol,
        "current_price": _fmt_float(overview_symbol.get("current_price") or simulated_symbol.get("current_price")),
        "primary_scenario": primary.get("scenario") or ranking.get("primary_scenario"),
        "primary_probability": _fmt_float(primary.get("probability") or ranking.get("scenario_probability")),
        "secondary_scenario": secondary.get("scenario") or ranking.get("secondary_scenario"),
        "secondary_probability": _fmt_float(secondary.get("probability")),
        "risk_scenario": risk_scenario,
        "risk_scenario_probability": _fmt_float(risk_payload.get("probability")),
        "probability_gap": _fmt_float(ranking.get("probability_gap") or ranking.get("primary_secondary_gap")),
        "close_call": str(bool(ranking.get("close_call"))).lower(),
        "edge_status": edge.get("market_edge_status") or "NO_EDGE",
        "signal_confirmation_score": _fmt_float(confirmation.get("confirmation_score") or confirmation.get("signal_confirmation_score")),
        "model_confidence": _fmt_float(confidence.get("confidence_score")),
        "data_completeness": _fmt_float(summary.get("data_completeness_score")),
        "strongest_predictor": _strongest_predictor_name(predictors),
        "supporting_signals": _json([item.get("name") for item in confirmation.get("supporting_evidence", []) if item.get("name")]),
        "conflicting_signals": _json([item.get("name") for item in confirmation.get("conflicting_evidence", []) if item.get("name")]),
        "missing_data": _json(summary.get("missing_key_sources") or []),
        "invalidation_conditions": _json(simulated_symbol.get("risk_invalidation_conditions") or ranking.get("switching_conditions") or []),
        "forecast_horizons": _json([f"{horizon}d" for horizon in HORIZONS]),
        "expected_return_by_horizon": _json(expected_by_horizon),
        "scenario_expected_return_by_horizon": _json(scenario_returns),
        "breadth_confirmation_score": _fmt_float(_score100(breadth.get("breadth_confirmation_score"), breadth.get("breadth_improvement_score"))),
        "breadth_conflict_score": _fmt_float(_score100(breadth.get("breadth_conflict_score"), breadth.get("breadth_deterioration_score"))),
        "options_confirmation_score": _fmt_float(max(_score100(vol.get("volatility_reversal_score")), _score100(vol.get("panic_release_score")))),
        "options_conflict_score": _fmt_float(max(_score100(vol.get("option_stress_score")), _score100(vol.get("tail_risk_score")), _score100(vol.get("failed_bounce_options_risk")))),
        "flow_confirmation_score": _fmt_float(_score100(flow.get("flow_confirmation_score"))),
        "flow_conflict_score": _fmt_float(_score100(flow.get("flow_conflict_score"), flow.get("risk_off_rotation_score"))),
        "status": "pending",
    }
    for horizon in HORIZONS:
        row[f"actual_return_{horizon}d"] = ""
        row[f"best_matching_scenario_{horizon}d"] = ""
        row[f"primary_hit_{horizon}d"] = ""
    return {field: row.get(field, "") for field in CSV_FIELDS}


def _backfill_outcomes(row: dict[str, Any], price_history: dict[str, list[dict[str, Any]]]) -> None:
    symbol = row.get("symbol")
    forecast_date = str(row.get("forecast_date") or "")[:10]
    rows = price_history.get(str(symbol), [])
    by_date = {str(item.get("date"))[:10]: index for index, item in enumerate(rows)}
    if forecast_date not in by_date:
        row["status"] = row.get("status") or "pending"
        return
    start_index = by_date[forecast_date]
    start_price = _float(rows[start_index].get("close"))
    if start_price is None or start_price == 0:
        return
    scenario_returns = _loads_dict(row.get("scenario_expected_return_by_horizon"))
    completed = 0
    for horizon in HORIZONS:
        key = f"{horizon}d"
        if start_index + horizon >= len(rows):
            continue
        end_price = _float(rows[start_index + horizon].get("close"))
        if end_price is None:
            continue
        actual = end_price / start_price - 1.0
        row[f"actual_return_{key}"] = _fmt_float(actual)
        best = _best_matching_scenario(actual, scenario_returns.get(key) or {})
        row[f"best_matching_scenario_{key}"] = best or ""
        row[f"primary_hit_{key}"] = str(best == row.get("primary_scenario")).lower() if best else ""
        primary_expected = _float((scenario_returns.get(key) or {}).get(row.get("primary_scenario")))
        row[f"path_error_{key}"] = _fmt_float(abs(actual - primary_expected)) if primary_expected is not None else ""
        completed += 1
    row["status"] = "completed" if completed == len(HORIZONS) else "partially_completed" if completed else "pending"


def _horizon_scorecard(rows: list[dict[str, Any]], horizon: int) -> dict[str, Any]:
    key = f"{horizon}d"
    completed = [row for row in rows if _float(row.get(f"actual_return_{key}")) is not None]
    primary_errors: list[float] = []
    secondary_errors: list[float] = []
    primary_hits = secondary_hits = primary_closer = close_total = close_primary_closer = 0
    for row in completed:
        actual = _float(row.get(f"actual_return_{key}"))
        scenario_returns = _loads_dict(row.get("scenario_expected_return_by_horizon")).get(key) or {}
        primary_expected = _float(scenario_returns.get(row.get("primary_scenario")))
        secondary_expected = _float(scenario_returns.get(row.get("secondary_scenario")))
        if actual is None:
            continue
        if primary_expected is not None:
            primary_errors.append(abs(actual - primary_expected))
        if secondary_expected is not None:
            secondary_errors.append(abs(actual - secondary_expected))
        if str(row.get(f"primary_hit_{key}")).lower() == "true":
            primary_hits += 1
        if row.get(f"best_matching_scenario_{key}") == row.get("secondary_scenario"):
            secondary_hits += 1
        if primary_expected is not None and secondary_expected is not None:
            if abs(actual - primary_expected) < abs(actual - secondary_expected):
                primary_closer += 1
                if str(row.get("close_call")).lower() == "true":
                    close_primary_closer += 1
            if str(row.get("close_call")).lower() == "true":
                close_total += 1
    count = len(completed)
    return {
        "completed_count": count,
        "sample_gate": _sample_gate(count),
        "primary_scenario_hit_rate": _rate(primary_hits, count),
        "primary_path_mean_absolute_error": _mean(primary_errors),
        "primary_path_median_absolute_error": _median(primary_errors),
        "secondary_scenario_hit_rate": _rate(secondary_hits, count),
        "primary_vs_secondary_accuracy_spread": _rate(primary_hits - secondary_hits, count),
        "primary_closer_than_secondary_rate": _rate(primary_closer, len(secondary_errors)),
        "close_call_sample_count": close_total,
        "close_call_primary_closer_rate": _rate(close_primary_closer, close_total),
    }


def _bucket_scorecards(rows: list[dict[str, Any]], field: str) -> dict[str, Any]:
    buckets: dict[str, list[dict[str, Any]]] = {}
    if field == "all":
        buckets["all"] = rows
    else:
        for row in rows:
            buckets.setdefault(str(row.get(field) or "unknown"), []).append(row)
    return {name: {f"{horizon}d": _horizon_scorecard(items, horizon) for horizon in HORIZONS} for name, items in buckets.items()}


def _edge_comparison(rows: list[dict[str, Any]]) -> str:
    strong = [row for row in rows if row.get("edge_status") in {"MODERATE_EDGE", "STRONG_EDGE"}]
    no_edge = [row for row in rows if row.get("edge_status") == "NO_EDGE"]
    strong_20 = _horizon_scorecard(strong, 20)
    no_20 = _horizon_scorecard(no_edge, 20)
    if strong_20["completed_count"] < 20:
        return "insufficient_samples_for_edge_validation"
    if no_20["completed_count"] and (strong_20.get("primary_scenario_hit_rate") or 0) <= (no_20.get("primary_scenario_hit_rate") or 0):
        return "moderate_or_strong_edge_not_better_than_no_edge_keep_confidence_capped"
    return "moderate_or_strong_edge_has_early_advantage_but_requires_more_samples"


def _high_confidence_comparison(rows: list[dict[str, Any]]) -> str:
    top = _top_fraction(rows, "model_confidence", 0.10)
    top_20 = _horizon_scorecard(top, 20)
    all_20 = _horizon_scorecard(rows, 20)
    if top_20["completed_count"] < 20:
        return "insufficient_samples_for_high_confidence_validation"
    if (top_20.get("primary_scenario_hit_rate") or 0) <= (all_20.get("primary_scenario_hit_rate") or 0):
        return "high_confidence_not_better_than_all_samples_keep_confidence_capped"
    return "high_confidence_bucket_has_early_advantage_but_not_validated"


def _primary_secondary_overall(rows: list[dict[str, Any]]) -> str:
    values = [_horizon_scorecard(rows, horizon).get("primary_closer_than_secondary_rate") for horizon in HORIZONS]
    clean = [value for value in values if value is not None]
    if not clean:
        return "insufficient_samples"
    return "primary_path_more_accurate_than_secondary" if sum(clean) / len(clean) > 0.5 else "primary_path_not_better_than_secondary"


def _read_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return [{field: row.get(field, "") for field in CSV_FIELDS} for row in csv.DictReader(handle)]


def _write_records(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in CSV_FIELDS} for row in rows)


def _parse_public_row(row: dict[str, Any]) -> dict[str, Any]:
    payload = dict(row)
    for key in ("supporting_signals", "conflicting_signals", "missing_data", "invalidation_conditions", "forecast_horizons", "expected_return_by_horizon", "scenario_expected_return_by_horizon"):
        payload[key] = _loads(payload.get(key))
    for key, value in list(payload.items()):
        parsed = _float(value)
        if parsed is not None:
            payload[key] = parsed
        elif str(value).lower() in {"true", "false"}:
            payload[key] = str(value).lower() == "true"
    return payload


def _expected_return_by_horizon(simulated_symbol: dict[str, Any]) -> dict[str, float | None]:
    summary = simulated_symbol.get("horizon_summary") or simulated_symbol.get("prediction_horizons") or {}
    return {f"{horizon}d": _float((summary.get(f"{horizon}d") or {}).get("expected_return")) for horizon in HORIZONS}


def _scenario_expected_returns(simulated_symbol: dict[str, Any]) -> dict[str, dict[str, float | None]]:
    paths = simulated_symbol.get("paths") or {}
    split = int(paths.get("split_index") or 0)
    current = _value_at(paths.get("expected_path"), split) or _float(simulated_symbol.get("current_price")) or 0.0
    mapping = {
        "expected_path": paths.get("expected_path"),
        "bounce_path": paths.get("bounce_path"),
        "bearish_path": paths.get("bearish_path"),
        "analog_average_path": paths.get("analog_average_path"),
    }
    result: dict[str, dict[str, float | None]] = {}
    for horizon in HORIZONS:
        row: dict[str, float | None] = {}
        for scenario, values in mapping.items():
            future = _value_at(values, split + horizon)
            row[scenario] = (future / current - 1.0) if future is not None and current else None
        result[f"{horizon}d"] = row
    return result


def _best_matching_scenario(actual: float, scenario_returns: dict[str, Any]) -> str | None:
    distances = []
    for scenario, value in scenario_returns.items():
        parsed = _float(value)
        if parsed is not None:
            distances.append((abs(actual - parsed), scenario))
    return min(distances)[1] if distances else None


def _top_fraction(rows: list[dict[str, Any]], key: str, fraction: float) -> list[dict[str, Any]]:
    if not rows:
        return []
    count = max(1, math.ceil(len(rows) * fraction))
    return sorted(rows, key=lambda row: _float(row.get(key)) or 0.0, reverse=True)[:count]


def _forecast_id(forecast_date: str, model_version: str, symbol: str) -> str:
    return hashlib.sha256(f"{forecast_date}|{model_version}|{symbol}".encode("utf-8")).hexdigest()[:18]


def _strongest_predictor_name(predictors: dict[str, Any]) -> str:
    if not predictors:
        return ""
    return max(predictors.items(), key=lambda item: _float((item[1] or {}).get("probability")) or 0.0)[0]


def _score100(value: Any, fallback: Any = None) -> float:
    parsed = _float(value)
    if parsed is None:
        parsed = _float(fallback)
    if parsed is None:
        return 0.0
    if parsed <= 1.0:
        parsed *= 100.0
    return max(0.0, min(100.0, parsed))


def _value_at(values: Any, index: int) -> float | None:
    if not isinstance(values, list) or index < 0 or index >= len(values):
        return None
    return _float(values[index])


def _loads(value: Any) -> Any:
    if value in {None, ""}:
        return None
    try:
        return json.loads(str(value))
    except json.JSONDecodeError:
        return value


def _loads_dict(value: Any) -> dict[str, Any]:
    parsed = _loads(value)
    return parsed if isinstance(parsed, dict) else {}


def _json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def _fmt_float(value: Any) -> str:
    parsed = _float(value)
    return "" if parsed is None else f"{parsed:.10g}"


def _float(value: Any) -> float | None:
    try:
        if value in {None, ""}:
            return None
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _mean(values: list[float]) -> float | None:
    return round(sum(values) / len(values), 6) if values else None


def _median(values: list[float]) -> float | None:
    if not values:
        return None
    values = sorted(values)
    mid = len(values) // 2
    if len(values) % 2:
        return round(values[mid], 6)
    return round((values[mid - 1] + values[mid]) / 2.0, 6)


def _rate(numerator: int | float, denominator: int) -> float | None:
    return round(float(numerator) / denominator, 4) if denominator else None


def _sample_gate(count: int) -> str:
    if count < 20:
        return "insufficient_samples"
    if count <= 50:
        return "early_evidence"
    if count <= 100:
        return "moderate_evidence"
    return "stronger_evidence"
