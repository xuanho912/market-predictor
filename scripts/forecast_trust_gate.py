from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
CORE_HORIZONS = ("1d", "3d", "5d", "10d", "20d", "60d")


def build_forecast_trust_gate(
    *,
    dashboard: dict[str, Any],
    data_freshness_status: dict[str, Any] | None = None,
    forecast_scorecard: dict[str, Any] | None = None,
    forecast_deviation_review: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a conservative readiness gate for relying on the forecast terminal.

    This does not change any forecast. It only states whether the current
    forecasts are ready to be treated as a dependable forecasting tool.
    """

    freshness = data_freshness_status or dashboard.get("data_freshness_status") or {}
    scorecard = forecast_scorecard or dashboard.get("forecast_accuracy_scorecard") or {}
    deviation = forecast_deviation_review or dashboard.get("forecast_deviation_review") or {}
    data_quality = dashboard.get("data_quality_report") or {}
    data_summary = data_quality.get("summary") or {}

    blockers: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    passes: list[str] = []

    freshness_status = str(freshness.get("data_freshness_status") or "unknown")
    if freshness_status in {"fresh", "market_closed"}:
        passes.append("data_is_current_or_market_closed")
    elif freshness_status == "market_open_unconfirmed":
        warnings.append(
            {
                "code": "market_open_unconfirmed",
                "severity": "medium",
                "message": "Current data is an intraday or unconfirmed snapshot; do not freeze it as a validated daily forecast.",
            }
        )
    else:
        blockers.append(
            {
                "code": "stale_or_failed_data",
                "severity": "critical",
                "message": freshness.get("warning_message")
                or "Data is stale or provider failed, so the current forecast cannot be treated as today's forecast.",
            }
        )

    completeness = _float(data_summary.get("data_completeness_score"))
    if completeness is not None and completeness >= 85:
        passes.append("data_completeness_85_plus")
    else:
        blockers.append(
            {
                "code": "data_completeness_below_gate",
                "severity": "high",
                "message": f"Data completeness is {completeness if completeness is not None else 'missing'}, below the 85/100 reliance gate.",
            }
        )

    counts = scorecard.get("sample_counts") or {}
    completed = {h: int(_float(counts.get(f"completed_{h}")) or 0) for h in CORE_HORIZONS}
    sample_gate = _sample_gate(completed)
    if sample_gate["passed"]:
        passes.append("forward_sample_gate_passed")
    else:
        blockers.append(
            {
                "code": "insufficient_forward_samples",
                "severity": "critical",
                "message": sample_gate["message"],
                "completed_by_horizon": completed,
            }
        )

    path_edge = _path_edge_quality(scorecard)
    if path_edge["passed"]:
        passes.append("primary_beats_secondary_with_enough_samples")
    else:
        blockers.append(
            {
                "code": "primary_path_not_validated",
                "severity": "high",
                "message": path_edge["message"],
                "details": path_edge,
            }
        )

    high_confidence = _high_confidence_quality(scorecard)
    if high_confidence["passed"]:
        passes.append("high_confidence_bucket_validated")
    else:
        warnings.append(
            {
                "code": "high_confidence_not_validated",
                "severity": "medium",
                "message": high_confidence["message"],
                "details": high_confidence,
            }
        )

    deviation_summary = deviation.get("summary") or {}
    deviation_gate = _deviation_quality(deviation_summary)
    if deviation_gate["passed"]:
        passes.append("deviation_rate_under_control")
    else:
        warnings.append(
            {
                "code": "deviation_learning_needed",
                "severity": "medium",
                "message": deviation_gate["message"],
                "details": deviation_gate,
            }
        )

    trust_score = _trust_score(
        freshness_status=freshness_status,
        completeness=completeness,
        sample_gate=sample_gate,
        path_edge=path_edge,
        high_confidence=high_confidence,
        deviation_gate=deviation_gate,
        blocker_count=len(blockers),
    )
    status = _trust_status(blockers, warnings, trust_score, sample_gate, path_edge)
    symbol_readiness = _symbol_readiness(dashboard, status)

    return {
        "version": "forecast_trust_gate_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "validation_type": "forecast_reliability_gate",
        "status": status,
        "trust_score": trust_score,
        "would_rely_for_real_money": status in {"CONDITIONAL_DECISION_SUPPORT", "VALIDATED_FORECAST_TOOL"},
        "use_boundary": _use_boundary(status),
        "data_freshness_status": freshness_status,
        "latest_market_date": freshness.get("latest_market_date"),
        "expected_latest_trading_date": freshness.get("expected_latest_trading_date"),
        "data_completeness_score": completeness,
        "forward_completed_samples": completed,
        "passes": passes,
        "blockers": blockers,
        "warnings": warnings,
        "symbol_readiness": symbol_readiness,
        "minimum_reliance_rules": [
            "Fresh or market-closed current data is mandatory.",
            "At least 20 completed 1d, 20 completed 3d, 20 completed 5d, 30 completed 10d and 50 completed 20d forecasts are required before treating the terminal as dependable.",
            "Primary scenario must beat secondary scenario on completed samples, not just look plausible.",
            "High-confidence forecasts must outperform ordinary forecasts before confidence can be trusted.",
            "Material deviation themes must be reviewed and routed into a challenger, not silently baked into baseline_v1.",
        ],
        "next_actions": _next_actions(status, blockers, warnings),
        "guardrails": [
            "This gate does not modify Alpha v1 threshold, baseline_v1 or historical forecast records.",
            "This is forecast reliability assessment, not trading advice.",
            "A blocked gate means the dashboard can still be used for research, but not as a dependable forecast tool.",
        ],
    }


def render_forecast_trust_gate_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Forecast Trust Gate",
        "",
        f"Generated at: `{payload.get('generated_at')}`",
        "",
        "This report answers whether the current Market Prediction Dashboard is dependable as a forecasting tool. It is not trading advice.",
        "",
        "## Current Status",
        "",
        f"- status: `{payload.get('status')}`",
        f"- trust_score: `{payload.get('trust_score')}`",
        f"- would_rely_for_real_money: `{payload.get('would_rely_for_real_money')}`",
        f"- use_boundary: {payload.get('use_boundary')}",
        f"- latest_market_date: `{payload.get('latest_market_date')}`",
        f"- expected_latest_trading_date: `{payload.get('expected_latest_trading_date')}`",
        f"- data_completeness_score: `{payload.get('data_completeness_score')}`",
        "",
        "## Forward Samples",
        "",
    ]
    for horizon, count in (payload.get("forward_completed_samples") or {}).items():
        lines.append(f"- {horizon}: `{count}`")

    lines.extend(["", "## Blockers", ""])
    blockers = payload.get("blockers") or []
    if not blockers:
        lines.append("- None.")
    for item in blockers:
        lines.append(f"- `{item.get('code')}` ({item.get('severity')}): {item.get('message')}")

    lines.extend(["", "## Warnings", ""])
    warnings = payload.get("warnings") or []
    if not warnings:
        lines.append("- None.")
    for item in warnings:
        lines.append(f"- `{item.get('code')}` ({item.get('severity')}): {item.get('message')}")

    lines.extend(["", "## Symbol Readiness", ""])
    for symbol, item in (payload.get("symbol_readiness") or {}).items():
        lines.append(
            f"- {symbol}: `{item.get('readiness')}` | primary `{item.get('primary_scenario')}` "
            f"{item.get('primary_probability')} | reason: {item.get('reason')}"
        )

    lines.extend(["", "## Next Actions", ""])
    for item in payload.get("next_actions") or []:
        lines.append(f"- {item}")

    lines.extend(["", "## Guardrails", ""])
    for item in payload.get("guardrails") or []:
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def write_forecast_trust_gate_outputs(
    payload: dict[str, Any],
    *,
    public_dir: Path | None = None,
    outputs_dir: Path | None = None,
) -> None:
    public_dir = public_dir or PROJECT_ROOT / "frontend" / "public"
    outputs_dir = outputs_dir or PROJECT_ROOT / "outputs"
    public_dir.mkdir(parents=True, exist_ok=True)
    outputs_dir.mkdir(parents=True, exist_ok=True)
    (public_dir / "forecast-trust-gate.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (outputs_dir / "forecast_trust_gate.md").write_text(
        render_forecast_trust_gate_markdown(payload),
        encoding="utf-8",
    )


def _sample_gate(completed: dict[str, int]) -> dict[str, Any]:
    required = {"1d": 20, "3d": 20, "5d": 20, "10d": 30, "20d": 50}
    missing = {h: max(0, req - int(completed.get(h, 0))) for h, req in required.items()}
    missing = {h: gap for h, gap in missing.items() if gap > 0}
    if not missing:
        return {"passed": True, "required": required, "missing": {}, "message": "Forward sample gate passed."}
    return {
        "passed": False,
        "required": required,
        "missing": missing,
        "message": "Forward validation samples are not enough to rely on the model as a high-confidence forecasting system.",
    }


def _path_edge_quality(scorecard: dict[str, Any]) -> dict[str, Any]:
    by_horizon = scorecard.get("primary_scenario_accuracy") or {}
    details: dict[str, Any] = {}
    checked = 0
    passed = 0
    for horizon in ("1d", "3d", "5d", "10d", "20d"):
        item = by_horizon.get(horizon) or {}
        count = int(_float(item.get("completed_count")) or 0)
        closer = _float(item.get("primary_closer_than_secondary_rate"))
        spread = _float(item.get("primary_vs_secondary_accuracy_spread"))
        details[horizon] = {"completed_count": count, "primary_closer_rate": closer, "primary_vs_secondary_spread": spread}
        if count >= 20:
            checked += 1
            if closer is not None and closer >= 0.55 and (spread is None or spread >= 0.05):
                passed += 1
    if checked >= 2 and passed >= max(1, checked // 2 + checked % 2):
        return {"passed": True, "checked_horizons": checked, "passed_horizons": passed, "details": details, "message": "Primary path has forward evidence against secondary path."}
    return {
        "passed": False,
        "checked_horizons": checked,
        "passed_horizons": passed,
        "details": details,
        "message": "Primary-vs-secondary path advantage is not yet proven on enough forward samples.",
    }


def _high_confidence_quality(scorecard: dict[str, Any]) -> dict[str, Any]:
    question = ((scorecard.get("core_questions") or {}).get("high_confidence_better") or "")
    passed = "early_advantage" in str(question) or "validated" in str(question)
    return {
        "passed": passed,
        "core_question": question or "missing",
        "message": "High-confidence bucket has evidence." if passed else "High-confidence forecasts have not proven they are more accurate than ordinary forecasts.",
    }


def _deviation_quality(summary: dict[str, Any]) -> dict[str, Any]:
    reviewed = int(_float(summary.get("completed_outcomes_reviewed")) or 0)
    material = int(_float(summary.get("material_deviation_count")) or 0)
    if reviewed < 20:
        return {
            "passed": False,
            "reviewed": reviewed,
            "material": material,
            "material_rate": None,
            "message": "Deviation sample is still too small to know whether errors are under control.",
        }
    rate = material / reviewed if reviewed else 1.0
    return {
        "passed": rate <= 0.25,
        "reviewed": reviewed,
        "material": material,
        "material_rate": round(rate, 4),
        "message": "Deviation rate is under control." if rate <= 0.25 else "Material deviation rate is too high; confidence must remain capped.",
    }


def _trust_score(
    *,
    freshness_status: str,
    completeness: float | None,
    sample_gate: dict[str, Any],
    path_edge: dict[str, Any],
    high_confidence: dict[str, Any],
    deviation_gate: dict[str, Any],
    blocker_count: int,
) -> int:
    score = 0
    if freshness_status in {"fresh", "market_closed"}:
        score += 20
    elif freshness_status == "market_open_unconfirmed":
        score += 8
    if completeness is not None:
        score += min(20, max(0, int((completeness - 65) / 20 * 20)))
    if sample_gate.get("passed"):
        score += 25
    else:
        completed = sample_gate.get("required") or {}
        missing = sample_gate.get("missing") or {}
        if completed:
            missing_total = sum(float(v) for v in missing.values())
            required_total = sum(float(v) for v in completed.values())
            score += max(0, int(25 * (1 - missing_total / required_total)))
    if path_edge.get("passed"):
        score += 15
    if high_confidence.get("passed"):
        score += 10
    if deviation_gate.get("passed"):
        score += 10
    score -= blocker_count * 8
    return max(0, min(100, int(round(score))))


def _trust_status(
    blockers: list[dict[str, Any]],
    warnings: list[dict[str, Any]],
    trust_score: int,
    sample_gate: dict[str, Any],
    path_edge: dict[str, Any],
) -> str:
    blocker_codes = {str(item.get("code")) for item in blockers}
    if "stale_or_failed_data" in blocker_codes:
        return "BLOCKED_STALE_DATA"
    if not sample_gate.get("passed"):
        return "RESEARCH_ONLY_FORWARD_VALIDATION_NEEDED"
    if not path_edge.get("passed"):
        return "RESEARCH_ONLY_PATH_EDGE_UNPROVEN"
    if trust_score >= 80 and not warnings:
        return "VALIDATED_FORECAST_TOOL"
    if trust_score >= 70:
        return "CONDITIONAL_DECISION_SUPPORT"
    return "RESEARCH_ONLY"


def _use_boundary(status: str) -> str:
    if status == "BLOCKED_STALE_DATA":
        return "Do not use the displayed forecast as today's forecast until data freshness is restored."
    if status.startswith("RESEARCH_ONLY"):
        return "Use as a research radar and scenario explainer only; do not treat it as a dependable forecasting edge."
    if status == "CONDITIONAL_DECISION_SUPPORT":
        return "Can support discretionary market review, but only with external confirmation and strict awareness that this is not a trading signal."
    return "Forecast tool has passed the configured reliability gates, but it still remains probabilistic and not guaranteed."


def _symbol_readiness(dashboard: dict[str, Any], global_status: str) -> dict[str, Any]:
    symbols = ((dashboard.get("simulated_paths") or {}).get("symbols") or {})
    result: dict[str, Any] = {}
    for symbol in SYMBOLS:
        item = symbols.get(symbol) or {}
        ranking = item.get("scenario_ranking") or {}
        primary = ranking.get("primary") or {}
        secondary = ranking.get("secondary") or {}
        confluence = item.get("confluence") or {}
        edge = (item.get("market_edge_status") or {}).get("market_edge_status") or "NO_EDGE"
        confidence = _float((item.get("model_confidence") or {}).get("confidence_score"))
        gap = _float(ranking.get("probability_gap"))
        confluence_score = _float(confluence.get("confluence_score"))
        readiness = "blocked_by_global_gate"
        reason = "Global trust gate is not ready."
        if global_status in {"CONDITIONAL_DECISION_SUPPORT", "VALIDATED_FORECAST_TOOL"}:
            if edge in {"STRONG_EDGE", "MODERATE_EDGE"} and confidence is not None and confidence >= 65 and gap is not None and gap >= 0.08:
                readiness = "usable_forecast_context"
                reason = "Edge, confidence and scenario gap pass symbol-level readiness checks."
            else:
                readiness = "watch_only"
                reason = "Symbol-level edge, confidence or scenario gap is not strong enough."
        result[symbol] = {
            "readiness": readiness,
            "reason": reason,
            "edge_status": edge,
            "confidence_score": confidence,
            "confluence_score": confluence_score,
            "primary_scenario": primary.get("scenario"),
            "primary_probability": primary.get("probability"),
            "secondary_scenario": secondary.get("scenario"),
            "secondary_probability": secondary.get("probability"),
            "probability_gap": gap,
        }
    return result


def _next_actions(status: str, blockers: list[dict[str, Any]], warnings: list[dict[str, Any]]) -> list[str]:
    actions: list[str] = []
    codes = {str(item.get("code")) for item in blockers + warnings}
    if "stale_or_failed_data" in codes:
        actions.append("Restore latest market data and rerun GitHub Actions before reading the dashboard as today's forecast.")
    if "insufficient_forward_samples" in codes:
        actions.append("Keep accumulating immutable forward forecasts until minimum sample gates are met.")
    if "primary_path_not_validated" in codes:
        actions.append("Do not promote any model until primary-vs-secondary path accuracy is proven by forward samples.")
    if "high_confidence_not_validated" in codes:
        actions.append("Keep confidence capped until high-confidence buckets outperform ordinary samples.")
    if "deviation_learning_needed" in codes:
        actions.append("Route repeated deviation themes into a challenger model rather than editing baseline_v1.")
    if not actions:
        actions.append("Continue daily forward validation and keep challenger models shadow-only until promotion gates are met.")
    return actions


def _float(value: Any) -> float | None:
    try:
        if value in (None, ""):
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    public_dir = PROJECT_ROOT / "frontend" / "public"
    outputs_dir = PROJECT_ROOT / "outputs"
    dashboard = _load_json(public_dir / "prediction-dashboard.json")
    freshness = _load_json(public_dir / "data-freshness-status.json")
    scorecard = _load_json(public_dir / "forecast-accuracy-scorecard.json")
    deviation = _load_json(public_dir / "forecast-deviation-review.json")
    payload = build_forecast_trust_gate(
        dashboard=dashboard,
        data_freshness_status=freshness,
        forecast_scorecard=scorecard,
        forecast_deviation_review=deviation,
    )
    write_forecast_trust_gate_outputs(payload, public_dir=public_dir, outputs_dir=outputs_dir)
    if dashboard:
        dashboard["forecast_trust_gate"] = payload
        (public_dir / "prediction-dashboard.json").write_text(
            json.dumps(dashboard, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print("wrote frontend/public/forecast-trust-gate.json")
    print("wrote outputs/forecast_trust_gate.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
