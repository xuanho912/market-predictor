from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
HORIZONS = (3, 5, 10, 20, 60)
SCENARIO_PATHS = ("expected_path", "bounce_path", "bearish_path", "analog_average_path")
SCENARIO_LABELS = {
    "expected_path": "base_path",
    "bounce_path": "bounce_path",
    "bearish_path": "failed_bounce_path",
    "analog_average_path": "analog_average_path",
}


def build_historical_replay_benchmark(dashboard: dict[str, Any]) -> dict[str, Any]:
    rows = _replay_rows(dashboard)
    primary_secondary = {f"{horizon}d": _primary_secondary_metrics(rows, horizon) for horizon in HORIZONS}
    scenario_type = {SCENARIO_LABELS[scenario]: _scenario_metrics(rows, scenario) for scenario in SCENARIO_PATHS}
    edge_status = _bucket_metrics(rows, "edge_status")
    signal_confirmation = {
        "top_10": _bucket_summary(_top_fraction(rows, "signal_confirmation_score", 0.10)),
        "top_20": _bucket_summary(_top_fraction(rows, "signal_confirmation_score", 0.20)),
        "bottom_20": _bucket_summary(_bottom_fraction(rows, "signal_confirmation_score", 0.20)),
        "effectiveness_question": _compare_high_low(rows, "signal_confirmation_score"),
    }
    data_effectiveness = _data_effectiveness(rows)
    report = {
        "version": "historical_replay_benchmark_v1",
        "validation_type": "historical_replay",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "prediction-dashboard historical analog replay rows",
        "as_of": dashboard.get("as_of"),
        "sample_size": len(rows),
        "symbols": list(SYMBOLS),
        "horizons": [f"{horizon}d" for horizon in HORIZONS],
        "status": "research_evaluation_only_not_forward_validation",
        "primary_vs_secondary": primary_secondary,
        "scenario_type_performance": scenario_type,
        "edge_status_performance": edge_status,
        "signal_confirmation_effectiveness": signal_confirmation,
        "data_completeness_effectiveness": data_effectiveness,
        "by_symbol": _bucket_metrics(rows, "symbol"),
        "by_regime": _bucket_metrics(rows, "regime"),
        "core_questions": _core_questions(primary_secondary, edge_status, signal_confirmation, data_effectiveness),
        "guardrails": [
            "Historical replay is research evaluation only and cannot replace daily forward validation.",
            "Historical replay results must not be described as confirmed alpha.",
            "Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.",
            "No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.",
            "Alpha v1 threshold remains frozen at 0.32534311.",
        ],
    }
    return report


def render_historical_replay_benchmark_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Historical Replay Benchmark",
        "",
        f"Generated at: `{report.get('generated_at')}`",
        f"Validation type: `{report.get('validation_type')}`",
        f"Status: `{report.get('status')}`",
        f"Sample size: `{report.get('sample_size')}`",
        "",
        "> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.",
        "",
        "## Core Questions",
        "",
    ]
    for key, value in (report.get("core_questions") or {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## Primary vs Secondary Scenario", ""])
    for horizon, payload in (report.get("primary_vs_secondary") or {}).items():
        lines.append(f"### {horizon}")
        for key in (
            "sample_size",
            "primary_hit_rate",
            "secondary_hit_rate",
            "primary_vs_secondary_accuracy_spread",
            "primary_closer_than_secondary_rate",
            "primary_mean_absolute_error",
            "secondary_mean_absolute_error",
            "primary_error_advantage",
            "close_call_sample_size",
            "close_call_primary_closer_rate",
        ):
            lines.append(f"- {key}: `{payload.get(key)}`")
        lines.append("")
    lines.extend(["## Scenario Type Performance", ""])
    for scenario, payload in (report.get("scenario_type_performance") or {}).items():
        lines.append(f"### {scenario}")
        lines.extend(_summary_lines(payload))
        lines.append("")
    lines.extend(["## Edge Status Performance", ""])
    for bucket, payload in (report.get("edge_status_performance") or {}).items():
        lines.append(f"### {bucket}")
        lines.extend(_summary_lines(payload))
        lines.append("")
    lines.extend(["## Signal Confirmation Effectiveness", ""])
    signal = report.get("signal_confirmation_effectiveness") or {}
    for bucket in ("top_10", "top_20", "bottom_20"):
        lines.append(f"### {bucket}")
        lines.extend(_summary_lines(signal.get(bucket) or {}))
        lines.append("")
    lines.append(f"- effectiveness_question: `{signal.get('effectiveness_question')}`")
    lines.extend(["", "## Data Completeness / Evidence Buckets", ""])
    data = report.get("data_completeness_effectiveness") or {}
    for bucket, payload in data.items():
        if not isinstance(payload, dict):
            lines.append(f"- {bucket}: `{payload}`")
            continue
        lines.append(f"### {bucket}")
        lines.extend(_summary_lines(payload))
        lines.append("")
    lines.extend(["## Guardrails", ""])
    lines.extend(f"- {item}" for item in report.get("guardrails", []))
    lines.append("")
    return "\n".join(lines)


def write_historical_replay_benchmark(
    dashboard: dict[str, Any],
    *,
    json_path: Path | None = None,
    markdown_path: Path | None = None,
) -> dict[str, Any]:
    json_path = json_path or PROJECT_ROOT / "frontend" / "public" / "historical-replay-benchmark.json"
    markdown_path = markdown_path or PROJECT_ROOT / "outputs" / "historical_replay_benchmark.md"
    report = build_historical_replay_benchmark(dashboard)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    markdown_path.write_text(render_historical_replay_benchmark_markdown(report), encoding="utf-8")
    return report


def _replay_rows(dashboard: dict[str, Any]) -> list[dict[str, Any]]:
    data_quality_summary = ((dashboard.get("data_quality_report") or {}).get("summary") or {})
    simulated_symbols = ((dashboard.get("simulated_paths") or {}).get("symbols") or {})
    analogs = dashboard.get("analogs") or {}
    rows: list[dict[str, Any]] = []
    for symbol in SYMBOLS:
        symbol_state = simulated_symbols.get(symbol) or {}
        analog = analogs.get(symbol) or {}
        if not symbol_state or not analog:
            continue
        scenario_returns = _scenario_expected_returns(symbol_state)
        ranking = symbol_state.get("scenario_ranking") or {}
        features = symbol_state.get("feature_snapshot_v3") or {}
        breadth = features.get("breadth") or {}
        options = features.get("volatility_options") or {}
        flow = features.get("flow_positioning_proxy") or {}
        confirmation = symbol_state.get("signal_confirmation") or symbol_state.get("signal_agreement") or {}
        confidence = symbol_state.get("model_confidence") or {}
        edge = symbol_state.get("market_edge_status") or {}
        predictors = symbol_state.get("predictors_v4") or symbol_state.get("predictors") or {}
        primary = ranking.get("primary") or {}
        secondary = ranking.get("secondary") or {}
        risk_scenario = ranking.get("risk_scenario")
        for case in analog.get("top_similar_cases", []):
            row = {
                "symbol": symbol,
                "date": case.get("date"),
                "regime": case.get("regime") or "unknown",
                "similarity_score": _float(case.get("similarity_score")),
                "primary_scenario": primary.get("scenario") or ranking.get("primary_scenario"),
                "primary_probability": _float(primary.get("probability") or ranking.get("scenario_probability")),
                "secondary_scenario": secondary.get("scenario") or ranking.get("secondary_scenario"),
                "secondary_probability": _float(secondary.get("probability")),
                "risk_scenario": risk_scenario,
                "probability_gap": _float(ranking.get("probability_gap") or ranking.get("primary_secondary_gap")),
                "close_call": bool(ranking.get("close_call")),
                "edge_status": edge.get("market_edge_status") or "NO_EDGE",
                "signal_confirmation_score": _score100(confirmation.get("confirmation_score") or confirmation.get("signal_agreement_score")),
                "model_confidence": _score100(confidence.get("confidence_score")),
                "data_completeness": _score100(data_quality_summary.get("data_completeness_score")),
                "strongest_predictor": _strongest_predictor_name(predictors),
                "fred_available": bool(data_quality_summary.get("fred_available")),
                "finnhub_available": bool(data_quality_summary.get("finnhub_available")),
                "breadth_confirmation_score": _score100(breadth.get("breadth_confirmation_score"), breadth.get("breadth_improvement_score")),
                "breadth_conflict_score": _score100(breadth.get("breadth_conflict_score"), breadth.get("breadth_deterioration_score")),
                "true_breadth": bool(breadth.get("is_true_breadth")),
                "options_confirmation_score": max(_score100(options.get("volatility_reversal_score")), _score100(options.get("panic_release_score"))),
                "options_conflict_score": max(
                    _score100(options.get("option_stress_score")),
                    _score100(options.get("tail_risk_score")),
                    _score100(options.get("failed_bounce_options_risk")),
                ),
                "flow_confirmation_score": _score100(flow.get("flow_confirmation_score")),
                "flow_conflict_score": _score100(flow.get("flow_conflict_score"), flow.get("risk_off_rotation_score")),
                "flow_quality_score": _score100(flow.get("flow_quality_score")),
                "true_flow_available": bool(flow.get("true_flow_available")),
                "max_adverse_excursion": _float(case.get("max_adverse_excursion")),
                "max_favorable_excursion": _float(case.get("max_favorable_excursion")),
            }
            for horizon in HORIZONS:
                row[f"forward_return_{horizon}d"] = _float(case.get(f"forward_return_{horizon}d"))
                row[f"scenario_expected_returns_{horizon}d"] = scenario_returns.get(f"{horizon}d", {})
            rows.append(row)
    return rows


def _primary_secondary_metrics(rows: list[dict[str, Any]], horizon: int) -> dict[str, Any]:
    key = f"{horizon}d"
    usable = [row for row in rows if _float(row.get(f"forward_return_{key}")) is not None]
    primary_errors: list[float] = []
    secondary_errors: list[float] = []
    primary_hits = secondary_hits = primary_closer = secondary_closer = ties = 0
    close_rows = close_primary_closer = 0
    actual_returns: list[float] = []
    for row in usable:
        actual = _float(row.get(f"forward_return_{key}"))
        if actual is None:
            continue
        actual_returns.append(actual)
        primary = str(row.get("primary_scenario") or "")
        secondary = str(row.get("secondary_scenario") or "")
        scenario_returns = row.get(f"scenario_expected_returns_{key}") or {}
        primary_expected = _float(scenario_returns.get(primary))
        secondary_expected = _float(scenario_returns.get(secondary))
        primary_hit = _scenario_direction_hit(primary, actual)
        secondary_hit = _scenario_direction_hit(secondary, actual)
        if primary_hit is not None:
            primary_hits += int(primary_hit)
        if secondary_hit is not None:
            secondary_hits += int(secondary_hit)
        if primary_expected is not None and secondary_expected is not None:
            p_error = abs(actual - primary_expected)
            s_error = abs(actual - secondary_expected)
            primary_errors.append(p_error)
            secondary_errors.append(s_error)
            if p_error < s_error:
                primary_closer += 1
                if row.get("close_call"):
                    close_primary_closer += 1
            elif s_error < p_error:
                secondary_closer += 1
            else:
                ties += 1
            if row.get("close_call"):
                close_rows += 1
    count = len(actual_returns)
    return {
        "sample_size": count,
        "sample_gate": _sample_gate(count),
        "primary_hit_rate": _rate(primary_hits, count),
        "secondary_hit_rate": _rate(secondary_hits, count),
        "primary_vs_secondary_accuracy_spread": _rate(primary_hits - secondary_hits, count),
        "primary_closer_than_secondary_rate": _rate(primary_closer, len(primary_errors)),
        "secondary_closer_than_primary_rate": _rate(secondary_closer, len(primary_errors)),
        "tie_rate": _rate(ties, len(primary_errors)),
        "primary_mean_absolute_error": _mean(primary_errors),
        "secondary_mean_absolute_error": _mean(secondary_errors),
        "primary_error_advantage": _round((_mean(secondary_errors) or 0.0) - (_mean(primary_errors) or 0.0)) if primary_errors and secondary_errors else None,
        "average_forward_return": _mean(actual_returns),
        "median_forward_return": _median(actual_returns),
        "max_adverse_path": _min(actual_returns),
        "max_favorable_path": _max(actual_returns),
        "close_call_sample_size": close_rows,
        "close_call_primary_closer_rate": _rate(close_primary_closer, close_rows),
    }


def _scenario_metrics(rows: list[dict[str, Any]], scenario: str) -> dict[str, Any]:
    by_horizon: dict[str, Any] = {}
    as_primary = [row for row in rows if row.get("primary_scenario") == scenario]
    for horizon in HORIZONS:
        key = f"{horizon}d"
        actuals: list[float] = []
        errors: list[float] = []
        direction_hits = 0
        direction_total = 0
        for row in rows:
            actual = _float(row.get(f"forward_return_{key}"))
            expected = _float((row.get(f"scenario_expected_returns_{key}") or {}).get(scenario))
            if actual is None:
                continue
            actuals.append(actual)
            hit = _scenario_direction_hit(scenario, actual)
            if hit is not None:
                direction_total += 1
                direction_hits += int(hit)
            if expected is not None:
                errors.append(abs(actual - expected))
        primary_actuals = [_float(row.get(f"forward_return_{key}")) for row in as_primary]
        primary_actuals = [value for value in primary_actuals if value is not None]
        by_horizon[key] = {
            "sample_size": len(actuals),
            "direction_hit_rate": _rate(direction_hits, direction_total),
            "path_mean_absolute_error": _mean(errors),
            "average_forward_return": _mean(actuals),
            "median_forward_return": _median(actuals),
            "max_adverse_path": _min(actuals),
            "max_favorable_path": _max(actuals),
            "as_primary_sample_size": len(primary_actuals),
            "as_primary_avg_return": _mean(primary_actuals),
            "as_primary_hit_rate": _rate(sum(1 for value in primary_actuals if value > 0), len(primary_actuals)),
        }
    return {
        "sample_size": len(rows),
        "as_primary_sample_size": len(as_primary),
        "by_horizon": by_horizon,
    }


def _bucket_metrics(rows: list[dict[str, Any]], field: str) -> dict[str, Any]:
    buckets: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        buckets.setdefault(str(row.get(field) or "unknown"), []).append(row)
    return {name: _bucket_summary(items) for name, items in sorted(buckets.items())}


def _bucket_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "sample_size": len(rows),
        "by_horizon": {f"{horizon}d": _primary_secondary_metrics(rows, horizon) for horizon in HORIZONS},
    }


def _data_effectiveness(rows: list[dict[str, Any]]) -> dict[str, Any]:
    high_completeness = [row for row in rows if (_float(row.get("data_completeness")) or 0.0) >= 85.0]
    low_completeness = [row for row in rows if (_float(row.get("data_completeness")) or 0.0) < 85.0]
    fred_available = [row for row in rows if row.get("fred_available")]
    fred_missing = [row for row in rows if not row.get("fred_available")]
    breadth_confirmed = [row for row in rows if (_float(row.get("breadth_confirmation_score")) or 0.0) >= 55.0]
    breadth_conflicted = [row for row in rows if (_float(row.get("breadth_conflict_score")) or 0.0) >= 55.0]
    options_confirmed = [row for row in rows if (_float(row.get("options_confirmation_score")) or 0.0) >= 55.0]
    options_conflicted = [row for row in rows if (_float(row.get("options_conflict_score")) or 0.0) >= 55.0]
    flow_confirmed = [row for row in rows if (_float(row.get("flow_confirmation_score")) or 0.0) >= 58.0 and (_float(row.get("flow_quality_score")) or 0.0) >= 45.0]
    flow_conflicted = [row for row in rows if (_float(row.get("flow_conflict_score")) or 0.0) >= 55.0]
    return {
        "high_data_completeness": _bucket_summary(high_completeness),
        "low_data_completeness": _bucket_summary(low_completeness),
        "fred_available": _bucket_summary(fred_available),
        "fred_missing": _bucket_summary(fred_missing),
        "breadth_confirmed": _bucket_summary(breadth_confirmed),
        "breadth_conflicted": _bucket_summary(breadth_conflicted),
        "options_confirmed": _bucket_summary(options_confirmed),
        "options_conflicted": _bucket_summary(options_conflicted),
        "flow_confirmed": _bucket_summary(flow_confirmed),
        "flow_conflicted": _bucket_summary(flow_conflicted),
        "data_enhancement_question": _data_enhancement_question(high_completeness, low_completeness, breadth_confirmed, breadth_conflicted, options_confirmed, options_conflicted, flow_confirmed, flow_conflicted),
    }


def _core_questions(
    primary_secondary: dict[str, Any],
    edge_status: dict[str, Any],
    signal_confirmation: dict[str, Any],
    data_effectiveness: dict[str, Any],
) -> dict[str, Any]:
    p20 = primary_secondary.get("20d") or {}
    primary_better = _is_positive(p20.get("primary_error_advantage")) and (_float(p20.get("primary_closer_than_secondary_rate")) or 0.0) > 0.50
    moderate = edge_status.get("MODERATE_EDGE") or {}
    strong = edge_status.get("STRONG_EDGE") or {}
    no_edge = edge_status.get("NO_EDGE") or {}
    edge_answer = _compare_bucket_20d([moderate, strong], [no_edge])
    return {
        "primary_scenario_beats_secondary": "yes_historical_replay" if primary_better else "not_proven_or_mixed",
        "moderate_or_strong_edge_beats_no_edge": edge_answer,
        "signal_confirmation_high_samples_more_accurate": signal_confirmation.get("effectiveness_question"),
        "data_enhancement_improves_prediction_quality": data_effectiveness.get("data_enhancement_question"),
        "forward_validation_required": "yes_daily_forward_validation_remains_decisive",
    }


def _compare_high_low(rows: list[dict[str, Any]], key: str) -> str:
    top = _top_fraction(rows, key, 0.20)
    bottom = _bottom_fraction(rows, key, 0.20)
    top20 = _primary_secondary_metrics(top, 20)
    bottom20 = _primary_secondary_metrics(bottom, 20)
    if not top or not bottom:
        return "insufficient_samples"
    top_error = _float(top20.get("primary_mean_absolute_error"))
    bottom_error = _float(bottom20.get("primary_mean_absolute_error"))
    top_closer = _float(top20.get("primary_closer_than_secondary_rate")) or 0.0
    bottom_closer = _float(bottom20.get("primary_closer_than_secondary_rate")) or 0.0
    if top_error is not None and bottom_error is not None and top_error < bottom_error and top_closer >= bottom_closer:
        return "historical_replay_supportive_but_not_forward_validated"
    return "historical_replay_mixed_or_not_better_keep_confidence_capped"


def _data_enhancement_question(*buckets: list[dict[str, Any]]) -> str:
    compared = [bucket for bucket in buckets if bucket]
    if len(compared) < 2:
        return "insufficient_contrast_in_current_historical_replay"
    return "historical_replay_available_compare_bucket_metrics_but_forward_validation_required"


def _compare_bucket_20d(left_buckets: list[dict[str, Any]], right_buckets: list[dict[str, Any]]) -> str:
    left_rows = sum(int(((bucket.get("by_horizon") or {}).get("20d") or {}).get("sample_size") or 0) for bucket in left_buckets)
    right_rows = sum(int(((bucket.get("by_horizon") or {}).get("20d") or {}).get("sample_size") or 0) for bucket in right_buckets)
    if not left_rows or not right_rows:
        return "insufficient_comparison_samples"
    left_error = _mean([_float(((bucket.get("by_horizon") or {}).get("20d") or {}).get("primary_mean_absolute_error")) or 0.0 for bucket in left_buckets if ((bucket.get("by_horizon") or {}).get("20d") or {}).get("sample_size")])
    right_error = _mean([_float(((bucket.get("by_horizon") or {}).get("20d") or {}).get("primary_mean_absolute_error")) or 0.0 for bucket in right_buckets if ((bucket.get("by_horizon") or {}).get("20d") or {}).get("sample_size")])
    if left_error is not None and right_error is not None and left_error < right_error:
        return "historical_replay_supportive_but_forward_validation_required"
    return "historical_replay_not_better_or_mixed"


def _scenario_expected_returns(symbol_state: dict[str, Any]) -> dict[str, dict[str, float | None]]:
    paths = symbol_state.get("paths") or {}
    split_index = int(paths.get("split_index") or 0)
    current = _value_at(paths.get("expected_path"), split_index) or _float(symbol_state.get("current_price")) or 0.0
    result: dict[str, dict[str, float | None]] = {}
    for horizon in HORIZONS:
        row: dict[str, float | None] = {}
        for scenario in SCENARIO_PATHS:
            future = _value_at(paths.get(scenario), split_index + horizon)
            row[scenario] = (future / current - 1.0) if future is not None and current else None
        result[f"{horizon}d"] = row
    return result


def _strongest_predictor_name(predictors: dict[str, Any]) -> str:
    if not predictors:
        return ""
    return max(predictors.items(), key=lambda item: _float((item[1] or {}).get("probability")) or 0.0)[0]


def _scenario_direction_hit(scenario: str, actual: float) -> bool | None:
    direction = _scenario_direction(scenario)
    if direction == 0:
        return None
    return (actual > 0 and direction > 0) or (actual < 0 and direction < 0)


def _scenario_direction(scenario: str) -> int:
    if scenario in {"expected_path", "bounce_path", "analog_average_path"}:
        return 1
    if scenario == "bearish_path":
        return -1
    return 0


def _top_fraction(rows: list[dict[str, Any]], key: str, fraction: float) -> list[dict[str, Any]]:
    if not rows:
        return []
    count = max(1, math.ceil(len(rows) * fraction))
    return sorted(rows, key=lambda row: _float(row.get(key)) or 0.0, reverse=True)[:count]


def _bottom_fraction(rows: list[dict[str, Any]], key: str, fraction: float) -> list[dict[str, Any]]:
    if not rows:
        return []
    count = max(1, math.ceil(len(rows) * fraction))
    return sorted(rows, key=lambda row: _float(row.get(key)) or 0.0)[:count]


def _summary_lines(payload: dict[str, Any]) -> list[str]:
    lines = [f"- sample_size: `{payload.get('sample_size', 0)}`"]
    for horizon, row in (payload.get("by_horizon") or {}).items():
        if "path_mean_absolute_error" in row or "direction_hit_rate" in row:
            lines.append(
                f"- {horizon}: sample `{row.get('sample_size', 0)}`, direction_hit `{row.get('direction_hit_rate')}`, path_mae `{row.get('path_mean_absolute_error')}`, as_primary `{row.get('as_primary_sample_size')}`, as_primary_hit `{row.get('as_primary_hit_rate')}`, avg `{row.get('average_forward_return')}`, median `{row.get('median_forward_return')}`"
            )
        else:
            lines.append(
                f"- {horizon}: sample `{row.get('sample_size', 0)}`, primary_hit `{row.get('primary_hit_rate')}`, primary_closer `{row.get('primary_closer_than_secondary_rate')}`, primary_mae `{row.get('primary_mean_absolute_error')}`, avg `{row.get('average_forward_return')}`, median `{row.get('median_forward_return')}`"
            )
    return lines


def _value_at(values: Any, index: int) -> float | None:
    if not isinstance(values, list) or index < 0 or index >= len(values):
        return None
    return _float(values[index])


def _score100(value: Any, fallback: Any = None) -> float:
    parsed = _float(value)
    if parsed is None:
        parsed = _float(fallback)
    if parsed is None:
        return 0.0
    if parsed <= 1.0:
        parsed *= 100.0
    return _round(max(0.0, min(100.0, parsed))) or 0.0


def _float(value: Any) -> float | None:
    try:
        if value in {None, ""}:
            return None
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _mean(values: list[float]) -> float | None:
    values = [value for value in values if value is not None and math.isfinite(value)]
    return _round(sum(values) / len(values)) if values else None


def _median(values: list[float]) -> float | None:
    values = sorted(value for value in values if value is not None and math.isfinite(value))
    if not values:
        return None
    mid = len(values) // 2
    if len(values) % 2:
        return _round(values[mid])
    return _round((values[mid - 1] + values[mid]) / 2.0)


def _min(values: list[float]) -> float | None:
    return _round(min(values)) if values else None


def _max(values: list[float]) -> float | None:
    return _round(max(values)) if values else None


def _rate(numerator: int | float, denominator: int) -> float | None:
    return _round(float(numerator) / denominator, 4) if denominator else None


def _round(value: float | None, digits: int = 6) -> float | None:
    return round(value, digits) if value is not None and math.isfinite(value) else None


def _sample_gate(count: int) -> str:
    if count < 20:
        return "insufficient_samples"
    if count <= 50:
        return "early_evidence"
    if count <= 100:
        return "moderate_evidence"
    return "stronger_evidence"


def _is_positive(value: Any) -> bool:
    parsed = _float(value)
    return parsed is not None and parsed > 0


def main() -> int:
    dashboard_path = PROJECT_ROOT / "frontend" / "public" / "prediction-dashboard.json"
    if not dashboard_path.exists():
        raise SystemExit(f"Missing dashboard file: {dashboard_path}")
    dashboard = json.loads(dashboard_path.read_text(encoding="utf-8"))
    report = write_historical_replay_benchmark(dashboard)
    print(f"wrote frontend/public/historical-replay-benchmark.json sample_size={report.get('sample_size')}")
    print("wrote outputs/historical_replay_benchmark.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
