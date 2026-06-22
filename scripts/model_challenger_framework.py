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
LEGACY_MODEL_VERSION = "market_intelligence_engine_v5"

MINIMUM_PROMOTION_GATES = {
    "3d": 20,
    "5d": 20,
    "10d": 30,
    "20d": 50,
    "60d": 50,
}

FORECAST_OUTCOME_PREFIXES = ("actual_return", "best_matching_scenario", "primary_hit", "path_error")
CHALLENGER_FORECAST_FIELDS = [
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
    "shadow_status",
    "blocked_reason",
    "actual_return_3d",
    "best_matching_scenario_3d",
    "primary_hit_3d",
    "path_error_3d",
    "actual_return_5d",
    "best_matching_scenario_5d",
    "primary_hit_5d",
    "path_error_5d",
    "actual_return_10d",
    "best_matching_scenario_10d",
    "primary_hit_10d",
    "path_error_10d",
    "actual_return_20d",
    "best_matching_scenario_20d",
    "primary_hit_20d",
    "path_error_20d",
    "actual_return_60d",
    "best_matching_scenario_60d",
    "primary_hit_60d",
    "path_error_60d",
    "status",
]

CHALLENGER_REGISTRY = [
    {
        "model_version": "challenger_v2_options_flow",
        "description": "Shadow-tests stricter scenario weighting from real volatility structure plus explicitly labeled flow proxy agreement.",
        "required_data_flags": ("options_structure_available", "flow_proxy_available"),
        "forbidden_without": "real volatility-structure data and explicitly labeled flow proxy inputs",
    },
    {
        "model_version": "challenger_v2_put_call",
        "description": "Adds real put/call pressure if a stable point-in-time source is available.",
        "required_data_flags": ("put_call_available",),
        "forbidden_without": "stable real put/call ratio data",
    },
    {
        "model_version": "challenger_v2_gamma_proxy",
        "description": "Adds defensible gamma exposure proxy only after the source and timestamp rules are validated.",
        "required_data_flags": ("gamma_available",),
        "forbidden_without": "reliable gamma exposure source or defensible proxy",
    },
    {
        "model_version": "challenger_v2_real_flow",
        "description": "Uses true fund-flow or positioning data instead of ETF-volume proxy-only evidence.",
        "required_data_flags": ("true_flow_available",),
        "forbidden_without": "true flow / positioning feed",
    },
    {
        "model_version": "challenger_v2_macro_event_risk",
        "description": "Adds higher-quality macro event risk features with release-time safety.",
        "required_data_flags": ("macro_event_quality_available",),
        "forbidden_without": "validated macro event quality data",
    },
    {
        "model_version": "challenger_v2_error_learning",
        "description": "Shadow-tests lessons learned from completed forecast deviations without rewriting baseline_v1.",
        "required_data_flags": ("forecast_deviation_evidence_available",),
        "forbidden_without": "at least 20 completed forecast deviation reviews and enough material deviations to avoid one-off hindsight fitting",
    },
    {
        "model_version": "challenger_v3_full_options_flow",
        "description": "Combines put/call, gamma proxy, true flow, and macro event risk after each component is validated.",
        "required_data_flags": (
            "put_call_available",
            "gamma_available",
            "true_flow_available",
            "macro_event_quality_available",
        ),
        "forbidden_without": "all component challengers passing their own shadow validation gates",
    },
]


def build_model_challenger_outputs(
    *,
    dashboard: dict[str, Any],
    records_path: Path | None = None,
    challenger_records_path: Path | None = None,
) -> dict[str, Any]:
    records_path = records_path or PROJECT_ROOT / "outputs" / "forecast_records.csv"
    challenger_records_path = challenger_records_path or PROJECT_ROOT / "outputs" / "model_challenger_forecasts.csv"
    baseline_records = _read_rows(records_path)
    challenger_records = _read_rows(challenger_records_path)
    data_flags = _data_availability_flags(dashboard)
    registry = [_registry_status(item, data_flags) for item in CHALLENGER_REGISTRY]
    leaderboard = _build_leaderboard(baseline_records, challenger_records, registry)
    promotion_status = _build_promotion_status(leaderboard, registry)
    standards = _validation_standards(leaderboard, promotion_status)
    leaderboard["validation_standards"] = standards
    promotion_status["validation_standards"] = standards
    return {
        "leaderboard": leaderboard,
        "promotion_status": promotion_status,
        "challenger_records": _public_records(challenger_records),
    }


def write_model_challenger_outputs(
    *,
    dashboard: dict[str, Any],
    public_dir: Path | None = None,
    outputs_dir: Path | None = None,
) -> dict[str, Any]:
    public_dir = public_dir or PROJECT_ROOT / "frontend" / "public"
    outputs_dir = outputs_dir or PROJECT_ROOT / "outputs"
    public_dir.mkdir(parents=True, exist_ok=True)
    outputs_dir.mkdir(parents=True, exist_ok=True)
    challenger_records_path = outputs_dir / "model_challenger_forecasts.csv"
    _ensure_challenger_csv(challenger_records_path)
    _append_ready_shadow_forecasts(
        dashboard=dashboard,
        records_path=outputs_dir / "forecast_records.csv",
        challenger_records_path=challenger_records_path,
    )
    payload = build_model_challenger_outputs(
        dashboard=dashboard,
        records_path=outputs_dir / "forecast_records.csv",
        challenger_records_path=challenger_records_path,
    )
    _write_json(public_dir / "model-leaderboard.json", payload["leaderboard"])
    _write_json(public_dir / "model-promotion-status.json", payload["promotion_status"])
    _write_json(
        public_dir / "model-challenger-forecasts.json",
        {
            "version": "model_challenger_forecasts_public_v1",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "records": payload["challenger_records"],
            "note": "Shadow forecasts are forecast-validation records, not execution records.",
        },
    )
    (outputs_dir / "model_leaderboard.md").write_text(
        render_model_leaderboard_markdown(payload["leaderboard"]),
        encoding="utf-8",
    )
    (outputs_dir / "model_promotion_rules.md").write_text(
        render_model_promotion_rules_markdown(payload["promotion_status"]),
        encoding="utf-8",
    )
    return payload


def render_model_leaderboard_markdown(leaderboard: dict[str, Any]) -> str:
    lines = [
        "# Model Leaderboard",
        "",
        f"Generated at: `{leaderboard.get('generated_at')}`",
        f"Active model: `{leaderboard.get('active_model_version')}`",
        "",
        "> This is forecast model validation, not execution guidance or portfolio accounting.",
        "",
        "## Baseline Freeze",
        "",
    ]
    freeze = leaderboard.get("baseline_freeze") or {}
    for key, value in freeze.items():
        lines.append(f"- {key}: `{value}`")
    standards = leaderboard.get("validation_standards") or {}
    lines.extend(["", "## Validation Standards", ""])
    for key in ("high_precision_standard", "stable_alpha_standard", "validated_forecasting_system_standard"):
        payload = standards.get(key) or {}
        lines.append(f"- {key}: `{payload.get('status')}`")
        for reason in payload.get("reasons") or []:
            lines.append(f"  - {reason}")
    lines.extend(["", "## Best Model By Horizon", ""])
    for horizon, payload in (leaderboard.get("best_model_by_horizon") or {}).items():
        lines.append(f"- {horizon}: `{payload}`")
    lines.extend(["", "## Models", ""])
    for model in leaderboard.get("models", []):
        lines.append(f"### {model.get('model_version')}")
        for key in (
            "role",
            "status",
            "total_forecasts",
            "pending_forecasts",
            "promotion_status",
            "reason",
        ):
            lines.append(f"- {key}: `{model.get(key)}`")
        lines.append("- horizon_metrics:")
        for horizon, metrics in (model.get("horizon_metrics") or {}).items():
            lines.append(f"  - {horizon}: `{metrics}`")
        lines.append("")
    lines.extend(["## Guardrails", ""])
    for guardrail in leaderboard.get("guardrails", []):
        lines.append(f"- {guardrail}")
    lines.append("")
    return "\n".join(lines)


def render_model_promotion_rules_markdown(status: dict[str, Any]) -> str:
    lines = [
        "# Model Promotion Rules",
        "",
        f"Generated at: `{status.get('generated_at')}`",
        "",
        "## Minimum Forward Sample Gates",
        "",
    ]
    for horizon, count in (status.get("minimum_sample_gates") or {}).items():
        lines.append(f"- {horizon}: `>= {count}` completed samples")
    lines.extend(
        [
            "",
            "## Required Majority Wins",
            "",
        ]
    )
    for metric in status.get("required_majority_win_metrics", []):
        lines.append(f"- {metric}")
    lines.extend(["", "## Current Promotion Status", ""])
    for model in status.get("models", []):
        lines.append(f"### {model.get('model_version')}")
        for key in ("status", "eligible", "reason", "wins_vs_baseline", "failed_gates"):
            lines.append(f"- {key}: `{model.get(key)}`")
        lines.append("")
    lines.extend(["## Validation Standards", ""])
    for key, payload in (status.get("validation_standards") or {}).items():
        if isinstance(payload, dict) and "status" in payload:
            lines.append(f"- {key}: `{payload.get('status')}`")
            for reason in payload.get("reasons") or []:
                lines.append(f"  - {reason}")
    lines.extend(["## Non-Negotiable Rules", ""])
    for rule in status.get("guardrails", []):
        lines.append(f"- {rule}")
    lines.append("")
    return "\n".join(lines)


def _build_leaderboard(
    baseline_records: list[dict[str, Any]],
    challenger_records: list[dict[str, Any]],
    registry: list[dict[str, Any]],
) -> dict[str, Any]:
    all_records = baseline_records + challenger_records
    versions = sorted({row.get("model_version") for row in all_records if row.get("model_version")})
    if BASELINE_MODEL_VERSION not in versions:
        versions.insert(0, BASELINE_MODEL_VERSION)
    models = []
    for version in versions:
        rows = [row for row in all_records if row.get("model_version") == version]
        role = "active_baseline" if version == BASELINE_MODEL_VERSION else "legacy_pre_baseline" if version == LEGACY_MODEL_VERSION else "shadow_challenger"
        models.append(_model_card(version, role, rows))
    for item in registry:
        if item["model_version"] not in versions:
            models.append(_registered_challenger_card(item))
    return {
        "version": "model_leaderboard_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "active_model_version": BASELINE_MODEL_VERSION,
        "best_model_by_horizon": _best_model_by_horizon(models),
        "baseline_freeze": {
            "model_version": BASELINE_MODEL_VERSION,
            "frozen_components": [
                "scenario ranking",
                "signal confirmation",
                "historical analog engine",
                "FRED rates/credit",
                "breadth/internal resonance",
                "VIX term / VVIX / SKEW",
                "flow / positioning proxy",
                "forecast accuracy ledger",
                "historical replay benchmark",
            ],
            "alpha_v1_threshold": 0.32534311,
            "past_forecast_policy": "Past rows are immutable. Pre-freeze rows keep their original model_version.",
        },
        "models": models,
        "registered_challengers": registry,
        "guardrails": _guardrails(),
    }


def _build_promotion_status(leaderboard: dict[str, Any], registry: list[dict[str, Any]]) -> dict[str, Any]:
    baseline = next((m for m in leaderboard.get("models", []) if m.get("model_version") == BASELINE_MODEL_VERSION), {})
    models = []
    for item in registry:
        card = next((m for m in leaderboard.get("models", []) if m.get("model_version") == item["model_version"]), {})
        status = _promotion_decision(card, baseline, item)
        models.append(status)
    return {
        "version": "model_promotion_status_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "active_model_version": BASELINE_MODEL_VERSION,
        "minimum_sample_gates": MINIMUM_PROMOTION_GATES,
        "required_majority_win_metrics": [
            "primary scenario hit rate",
            "primary vs secondary accuracy spread",
            "mean absolute path error",
            "median absolute path error",
            "high confidence accuracy",
            "signal confirmation top 10% performance",
            "edge status performance",
            "calibration quality",
            "max adverse path control",
        ],
        "models": models,
        "guardrails": _guardrails()
        + [
            "If a challenger only wins one horizon while degrading others, it cannot be promoted.",
            "Historical replay can create research priority, not active-model promotion.",
            "Only forward validation can promote a challenger to active_model.",
        ],
    }


def _validation_standards(leaderboard: dict[str, Any], promotion_status: dict[str, Any]) -> dict[str, Any]:
    baseline = next((model for model in leaderboard.get("models", []) if model.get("model_version") == BASELINE_MODEL_VERSION), {})
    horizon_metrics = baseline.get("horizon_metrics") or {}
    completed = {horizon: int((horizon_metrics.get(horizon) or {}).get("completed_count") or 0) for horizon in MINIMUM_PROMOTION_GATES}
    max_completed = max(completed.values(), default=0)
    min_completed = min(completed.values(), default=0)
    has_promotion_candidate = any(model.get("status") == "promotion_candidate" for model in promotion_status.get("models", []))

    high_precision_reasons: list[str] = []
    if min_completed < 20:
        high_precision_reasons.append("forward completed samples are below the minimum validation gate")
    if not _moderate_strong_edge_validated(baseline):
        high_precision_reasons.append("MODERATE_EDGE / STRONG_EDGE samples are not yet proven better than NO_EDGE")
    if not _horizon_advantage_validated(baseline):
        high_precision_reasons.append("5d / 20d primary-path advantage is not yet forward validated")

    stable_alpha_reasons: list[str] = []
    if max_completed < 50:
        stable_alpha_reasons.append("forward-only samples are too small for stable alpha")
    stable_alpha_reasons.append("Alpha v1 remains RESEARCH ALPHA CANDIDATE and cannot be upgraded by historical replay")

    validated_reasons: list[str] = []
    if min_completed < 20:
        validated_reasons.append("forecast accuracy ledger has insufficient completed forward samples")
    if not has_promotion_candidate:
        validated_reasons.append("no challenger has qualified for promotion against baseline_v1")

    return {
        "high_precision_standard": {
            "status": "met" if not high_precision_reasons else "not_yet_validated",
            "reasons": high_precision_reasons,
            "definition_doc": "docs/forecast_accuracy_definition.md",
        },
        "stable_alpha_standard": {
            "status": "met" if not stable_alpha_reasons else "not_yet_validated",
            "alpha_v1_status": "RESEARCH ALPHA CANDIDATE",
            "reasons": stable_alpha_reasons,
            "definition_doc": "docs/stable_alpha_definition.md",
        },
        "validated_forecasting_system_standard": {
            "status": "met" if not validated_reasons else "not_yet_validated",
            "reasons": validated_reasons,
            "requires_forward_validation": True,
        },
        "forward_completed_samples_by_horizon": completed,
        "summary": "Current system is an auditable baseline and challenger framework, not yet a high-precision or stable-alpha system.",
    }


def _best_model_by_horizon(models: list[dict[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for horizon in MINIMUM_PROMOTION_GATES:
        candidates: list[dict[str, Any]] = []
        for model in models:
            metrics = ((model.get("horizon_metrics") or {}).get(horizon) or {})
            completed = int(metrics.get("completed_count") or 0)
            mae = _float(metrics.get("primary_mean_absolute_error"))
            hit = _float(metrics.get("primary_hit_rate"))
            if completed and mae is not None:
                candidates.append(
                    {
                        "model_version": model.get("model_version"),
                        "completed_count": completed,
                        "primary_hit_rate": hit,
                        "primary_mean_absolute_error": mae,
                    }
                )
        candidates.sort(key=lambda item: (item["primary_mean_absolute_error"], -(item["primary_hit_rate"] or 0.0)))
        result[horizon] = candidates[0] if candidates else {
            "model_version": None,
            "completed_count": 0,
            "status": "insufficient_forward_samples",
        }
    return result


def _moderate_strong_edge_validated(model: dict[str, Any]) -> bool:
    return int(model.get("completed_forecasts") or 0) >= 20 and model.get("promotion_status") == "active_model"


def _horizon_advantage_validated(model: dict[str, Any]) -> bool:
    metrics = model.get("horizon_metrics") or {}
    for horizon in ("5d", "20d"):
        row = metrics.get(horizon) or {}
        if int(row.get("completed_count") or 0) < MINIMUM_PROMOTION_GATES[horizon]:
            return False
        if (_float(row.get("primary_vs_secondary_accuracy_spread")) or 0.0) <= 0:
            return False
    return True


def _model_card(version: str, role: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    horizon_metrics = {f"{horizon}d": _horizon_metrics(rows, horizon) for horizon in HORIZONS}
    completed = sum(1 for row in rows if row.get("status") == "completed")
    pending = sum(1 for row in rows if row.get("status") != "completed")
    gates_met = _gates_met(horizon_metrics)
    promotion_status = (
        "active_model" if role == "active_baseline"
        else "historical_only_not_validated" if role == "legacy_pre_baseline"
        else "insufficient_forward_evidence" if not gates_met
        else "shadow_evaluation_ready"
    )
    reason = (
        "Frozen current production model. Not a claim of high precision or stable alpha."
        if role == "active_baseline"
        else "Pre-baseline records are preserved for audit only and cannot be renamed."
        if role == "legacy_pre_baseline"
        else "Forward samples have not met promotion gates."
    )
    return {
        "model_version": version,
        "role": role,
        "status": "tracking" if rows else "no_records_yet",
        "total_forecasts": len(rows),
        "pending_forecasts": pending,
        "completed_forecasts": completed,
        "horizon_metrics": horizon_metrics,
        "promotion_status": promotion_status,
        "reason": reason,
    }


def _registered_challenger_card(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "model_version": item["model_version"],
        "role": "registered_shadow_challenger",
        "status": item["status"],
        "total_forecasts": 0,
        "pending_forecasts": 0,
        "completed_forecasts": 0,
        "horizon_metrics": {f"{horizon}d": _empty_horizon_metrics() for horizon in HORIZONS},
        "promotion_status": "blocked_missing_required_data" if item["missing_required_data"] else "ready_for_shadow_implementation",
        "reason": item["blocked_reason"] or "Required data is available, but challenger logic must be explicitly versioned before producing forecasts.",
    }


def _promotion_decision(card: dict[str, Any], baseline: dict[str, Any], registry_item: dict[str, Any]) -> dict[str, Any]:
    if registry_item.get("missing_required_data"):
        return {
            "model_version": registry_item["model_version"],
            "status": "blocked_missing_required_data",
            "eligible": False,
            "reason": registry_item["blocked_reason"],
            "wins_vs_baseline": 0,
            "failed_gates": list(registry_item["missing_required_data"]),
        }
    if not card or card.get("total_forecasts", 0) == 0:
        return {
            "model_version": registry_item["model_version"],
            "status": "insufficient_forward_evidence",
            "eligible": False,
            "reason": "No shadow forecasts have matured.",
            "wins_vs_baseline": 0,
            "failed_gates": list(MINIMUM_PROMOTION_GATES),
        }
    failed_gates = [
        horizon
        for horizon, minimum in MINIMUM_PROMOTION_GATES.items()
        if ((card.get("horizon_metrics") or {}).get(horizon) or {}).get("completed_count", 0) < minimum
    ]
    if failed_gates:
        return {
            "model_version": registry_item["model_version"],
            "status": "insufficient_forward_evidence",
            "eligible": False,
            "reason": "Forward validation sample gates are not met.",
            "wins_vs_baseline": 0,
            "failed_gates": failed_gates,
        }
    wins = _wins_vs_baseline(card, baseline)
    status = "promotion_candidate" if wins >= 5 else "keep_shadow"
    return {
        "model_version": registry_item["model_version"],
        "status": status,
        "eligible": status == "promotion_candidate",
        "reason": "Majority forward metrics beat baseline." if status == "promotion_candidate" else "Forward metrics do not beat baseline by majority.",
        "wins_vs_baseline": wins,
        "failed_gates": [],
    }


def _registry_status(item: dict[str, Any], flags: dict[str, bool]) -> dict[str, Any]:
    missing = [flag for flag in item["required_data_flags"] if not flags.get(flag, False)]
    return {
        **item,
        "status": "blocked_missing_required_data" if missing else "ready_for_shadow_implementation",
        "missing_required_data": missing,
        "blocked_reason": f"Missing {', '.join(missing)}; cannot generate this shadow forecast without {item['forbidden_without']}." if missing else "",
    }


def _data_availability_flags(dashboard: dict[str, Any]) -> dict[str, bool]:
    options = ((dashboard.get("options_status") or {}).get("summary") or {})
    flow = ((dashboard.get("flow_positioning_status") or dashboard.get("flow_status") or {}).get("summary") or {})
    data_quality = ((dashboard.get("data_quality_report") or {}).get("summary") or {})
    deviation_review = dashboard.get("forecast_deviation_review") or _load_latest_deviation_review()
    deviation_summary = ((deviation_review or {}).get("summary") or {})
    finnhub_available = bool(data_quality.get("finnhub_available"))
    options_structure_available = bool(
        options.get("options_available")
        and options.get("vix_term_available")
        and (options.get("vvix_available") or options.get("skew_available"))
    )
    completed_deviation_reviews = int(_float(deviation_summary.get("completed_outcomes_reviewed")) or 0)
    material_deviation_count = int(_float(deviation_summary.get("material_deviation_count")) or 0)
    return {
        "options_structure_available": options_structure_available,
        "flow_proxy_available": bool(flow.get("flow_available")) and bool(flow.get("flow_proxy_only")),
        "put_call_available": bool(options.get("put_call_available")),
        "gamma_available": bool(options.get("gamma_available")),
        "true_flow_available": bool(flow.get("true_flow_available")),
        "macro_event_quality_available": finnhub_available and bool(data_quality.get("macro_event_quality_available")),
        "forecast_deviation_evidence_available": completed_deviation_reviews >= 20 and material_deviation_count >= 3,
    }


def _load_latest_deviation_review() -> dict[str, Any]:
    path = PROJECT_ROOT / "frontend" / "public" / "forecast-deviation-review.json"
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _append_ready_shadow_forecasts(
    *,
    dashboard: dict[str, Any],
    records_path: Path,
    challenger_records_path: Path,
) -> None:
    baseline_rows = [row for row in _read_rows(records_path) if row.get("model_version") == BASELINE_MODEL_VERSION]
    if not baseline_rows:
        return
    data_flags = _data_availability_flags(dashboard)
    registry = [_registry_status(item, data_flags) for item in CHALLENGER_REGISTRY]
    ready = [item for item in registry if item.get("status") == "ready_for_shadow_implementation"]
    if not ready:
        return
    latest_date = max(str(row.get("forecast_date") or "") for row in baseline_rows)
    current_baseline_rows = [row for row in baseline_rows if str(row.get("forecast_date") or "") == latest_date]
    existing = _read_rows(challenger_records_path)
    existing_ids = {row.get("forecast_id") for row in existing if row.get("forecast_id")}
    additions: list[dict[str, Any]] = []
    for registry_item in ready:
        for baseline_row in current_baseline_rows:
            shadow = _build_shadow_forecast_from_baseline(baseline_row, registry_item, dashboard)
            if shadow and shadow["forecast_id"] not in existing_ids:
                additions.append(shadow)
                existing_ids.add(shadow["forecast_id"])
    if not additions:
        return
    with challenger_records_path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CHALLENGER_FORECAST_FIELDS, lineterminator="\n")
        writer.writerows(additions)


def _build_shadow_forecast_from_baseline(
    baseline_row: dict[str, Any],
    registry_item: dict[str, Any],
    dashboard: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    if registry_item.get("model_version") == "challenger_v2_error_learning":
        return _build_error_learning_shadow_forecast(baseline_row, registry_item, dashboard or {})
    if registry_item.get("model_version") != "challenger_v2_options_flow":
        return None
    forecast_date = str(baseline_row.get("forecast_date") or "")
    symbol = str(baseline_row.get("symbol") or "")
    if not forecast_date or not symbol:
        return None
    primary_probability = _float(baseline_row.get("primary_probability")) or 0.0
    secondary_probability = _float(baseline_row.get("secondary_probability")) or 0.0
    risk_probability = _float(baseline_row.get("risk_scenario_probability")) or 0.0
    option_support = (_float(baseline_row.get("options_confirmation_score")) or 0.0) / 100.0
    option_conflict = (_float(baseline_row.get("options_conflict_score")) or 0.0) / 100.0
    flow_support = (_float(baseline_row.get("flow_confirmation_score")) or 0.0) / 100.0
    flow_conflict = (_float(baseline_row.get("flow_conflict_score")) or 0.0) / 100.0
    support = (option_support + flow_support) / 2.0
    conflict = (option_conflict + flow_conflict) / 2.0
    tilt = max(-0.04, min(0.04, (support - conflict) * 0.05))
    if baseline_row.get("primary_scenario") != "bounce_path":
        tilt *= 0.5
    primary_probability = max(0.01, min(0.95, primary_probability + tilt))
    secondary_probability = max(0.01, min(0.95, secondary_probability - tilt * 0.55))
    risk_probability = max(0.01, min(0.95, risk_probability - tilt * 0.45))
    row = {field: baseline_row.get(field, "") for field in CHALLENGER_FORECAST_FIELDS}
    model_version = registry_item["model_version"]
    row.update(
        {
            "forecast_id": _forecast_id(forecast_date, model_version, symbol),
            "model_version": model_version,
            "primary_probability": _fmt_float(primary_probability),
            "secondary_probability": _fmt_float(secondary_probability),
            "risk_scenario_probability": _fmt_float(risk_probability),
            "probability_gap": _fmt_float(primary_probability - secondary_probability),
            "close_call": str(abs(primary_probability - secondary_probability) < 0.08).lower(),
            "shadow_status": "pending_forward_validation",
            "blocked_reason": "",
            "supporting_signals": _json_append(baseline_row.get("supporting_signals"), "options_flow_shadow_confirmation"),
            "conflicting_signals": _json_append(baseline_row.get("conflicting_signals"), "options_flow_shadow_conflicts_if_vol_or_flow_reverses"),
            "status": "pending",
        }
    )
    for horizon in HORIZONS:
        key = f"{horizon}d"
        row[f"actual_return_{key}"] = ""
        row[f"best_matching_scenario_{key}"] = ""
        row[f"primary_hit_{key}"] = ""
        row[f"path_error_{key}"] = ""
    return {field: row.get(field, "") for field in CHALLENGER_FORECAST_FIELDS}


def _build_error_learning_shadow_forecast(
    baseline_row: dict[str, Any],
    registry_item: dict[str, Any],
    dashboard: dict[str, Any],
) -> dict[str, Any] | None:
    forecast_date = str(baseline_row.get("forecast_date") or "")
    symbol = str(baseline_row.get("symbol") or "")
    if not forecast_date or not symbol:
        return None
    review = dashboard.get("forecast_deviation_review") or {}
    driver_counts = review.get("driver_counts") or {}
    if not isinstance(driver_counts, dict):
        driver_counts = {}
    primary_probability = _float(baseline_row.get("primary_probability")) or 0.0
    secondary_probability = _float(baseline_row.get("secondary_probability")) or 0.0
    risk_probability = _float(baseline_row.get("risk_scenario_probability")) or 0.0
    primary_scenario = str(baseline_row.get("primary_scenario") or "")
    upside_pressure = sum(
        int(driver_counts.get(key) or 0)
        for key in (
            "news_event_driver_underweighted",
            "risk_off_news_overweighted_or_resolved",
            "volatility_repair_underweighted",
            "breadth_follow_through_underweighted",
            "risk_on_flow_underweighted",
        )
    )
    downside_pressure = sum(
        int(driver_counts.get(key) or 0)
        for key in (
            "news_event_risk_underweighted",
            "volatility_or_tail_risk_underweighted",
            "breadth_conflict_underweighted",
            "risk_off_flow_underweighted",
            "model_underestimated_downside_or_failed_bounce",
        )
    )
    net = max(-1.0, min(1.0, (upside_pressure - downside_pressure) / max(1, upside_pressure + downside_pressure)))
    tilt = max(-0.05, min(0.05, net * 0.035))
    if primary_scenario not in {"bounce_path", "analog_average_path", "expected_path"}:
        tilt *= -0.5
    primary_probability = max(0.01, min(0.95, primary_probability + tilt))
    secondary_probability = max(0.01, min(0.95, secondary_probability - tilt * 0.5))
    risk_probability = max(0.01, min(0.95, risk_probability - tilt * 0.5))
    row = {field: baseline_row.get(field, "") for field in CHALLENGER_FORECAST_FIELDS}
    model_version = registry_item["model_version"]
    row.update(
        {
            "forecast_id": _forecast_id(forecast_date, model_version, symbol),
            "model_version": model_version,
            "primary_probability": _fmt_float(primary_probability),
            "secondary_probability": _fmt_float(secondary_probability),
            "risk_scenario_probability": _fmt_float(risk_probability),
            "probability_gap": _fmt_float(primary_probability - secondary_probability),
            "close_call": str(abs(primary_probability - secondary_probability) < 0.08).lower(),
            "shadow_status": "pending_forward_validation",
            "blocked_reason": "",
            "supporting_signals": _json_append(baseline_row.get("supporting_signals"), "error_learning_shadow_adjustment"),
            "conflicting_signals": _json_append(baseline_row.get("conflicting_signals"), "error_learning_requires_forward_validation"),
            "status": "pending",
        }
    )
    for horizon in HORIZONS:
        key = f"{horizon}d"
        row[f"actual_return_{key}"] = ""
        row[f"best_matching_scenario_{key}"] = ""
        row[f"primary_hit_{key}"] = ""
        row[f"path_error_{key}"] = ""
    return {field: row.get(field, "") for field in CHALLENGER_FORECAST_FIELDS}


def _horizon_metrics(rows: list[dict[str, Any]], horizon: int) -> dict[str, Any]:
    key = f"{horizon}d"
    completed = [row for row in rows if _float(row.get(f"actual_return_{key}")) is not None]
    primary_hits = secondary_hits = primary_closer = 0
    primary_errors: list[float] = []
    secondary_errors: list[float] = []
    for row in completed:
        actual = _float(row.get(f"actual_return_{key}"))
        scenario_returns = _loads_dict(row.get("scenario_expected_return_by_horizon")).get(key) or {}
        primary_expected = _float(scenario_returns.get(row.get("primary_scenario")))
        secondary_expected = _float(scenario_returns.get(row.get("secondary_scenario")))
        if actual is None:
            continue
        if str(row.get(f"primary_hit_{key}")).lower() == "true":
            primary_hits += 1
        if row.get(f"best_matching_scenario_{key}") == row.get("secondary_scenario"):
            secondary_hits += 1
        if primary_expected is not None:
            primary_errors.append(abs(actual - primary_expected))
        if secondary_expected is not None:
            secondary_errors.append(abs(actual - secondary_expected))
        if primary_expected is not None and secondary_expected is not None and abs(actual - primary_expected) < abs(actual - secondary_expected):
            primary_closer += 1
    count = len(completed)
    return {
        "completed_count": count,
        "sample_gate": _sample_gate(count),
        "primary_hit_rate": _rate(primary_hits, count),
        "secondary_hit_rate": _rate(secondary_hits, count),
        "primary_vs_secondary_accuracy_spread": _rate(primary_hits - secondary_hits, count),
        "primary_closer_than_secondary_rate": _rate(primary_closer, len(secondary_errors)),
        "primary_mean_absolute_error": _mean(primary_errors),
        "primary_median_absolute_error": _median(primary_errors),
        "secondary_mean_absolute_error": _mean(secondary_errors),
    }


def _empty_horizon_metrics() -> dict[str, Any]:
    return {
        "completed_count": 0,
        "sample_gate": "insufficient_samples",
        "primary_hit_rate": None,
        "secondary_hit_rate": None,
        "primary_vs_secondary_accuracy_spread": None,
        "primary_closer_than_secondary_rate": None,
        "primary_mean_absolute_error": None,
        "primary_median_absolute_error": None,
        "secondary_mean_absolute_error": None,
    }


def _gates_met(horizon_metrics: dict[str, Any]) -> bool:
    return all((horizon_metrics.get(horizon) or {}).get("completed_count", 0) >= minimum for horizon, minimum in MINIMUM_PROMOTION_GATES.items())


def _wins_vs_baseline(card: dict[str, Any], baseline: dict[str, Any]) -> int:
    wins = 0
    for horizon in MINIMUM_PROMOTION_GATES:
        model_row = (card.get("horizon_metrics") or {}).get(horizon) or {}
        base_row = (baseline.get("horizon_metrics") or {}).get(horizon) or {}
        if _greater(model_row.get("primary_hit_rate"), base_row.get("primary_hit_rate")):
            wins += 1
        if _greater(model_row.get("primary_vs_secondary_accuracy_spread"), base_row.get("primary_vs_secondary_accuracy_spread")):
            wins += 1
        if _lower(model_row.get("primary_mean_absolute_error"), base_row.get("primary_mean_absolute_error")):
            wins += 1
    return wins


def _read_rows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _ensure_challenger_csv(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        with path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames == CHALLENGER_FORECAST_FIELDS:
                return
            rows = [{field: row.get(field, "") for field in CHALLENGER_FORECAST_FIELDS} for row in reader]
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=CHALLENGER_FORECAST_FIELDS, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        csv.DictWriter(handle, fieldnames=CHALLENGER_FORECAST_FIELDS, lineterminator="\n").writeheader()


def _public_records(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for row in rows[-1000:]:
        item = dict(row)
        for key, value in list(item.items()):
            parsed = _float(value)
            if parsed is not None:
                item[key] = parsed
            elif str(value).lower() in {"true", "false"}:
                item[key] = str(value).lower() == "true"
            elif key in {"supporting_signals", "conflicting_signals", "missing_data", "invalidation_conditions", "forecast_horizons", "expected_return_by_horizon", "scenario_expected_return_by_horizon"}:
                item[key] = _loads(value)
        result.append(item)
    return result


def _guardrails() -> list[str]:
    return [
        "Alpha v1 threshold remains frozen at 0.32534311.",
        "Baseline v1 records are immutable except realized-outcome backfills.",
        "Challengers must run as shadow forecasts before replacing baseline.",
        "Historical replay cannot promote a model without forward validation.",
        "This system validates market probability paths, not execution guidance or portfolio accounting.",
    ]


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


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def _forecast_id(forecast_date: str, model_version: str, symbol: str) -> str:
    return hashlib.sha256(f"{forecast_date}|{model_version}|{symbol}".encode("utf-8")).hexdigest()[:18]


def _json_append(value: Any, item: str) -> str:
    parsed = _loads(value)
    items = parsed if isinstance(parsed, list) else []
    if item not in items:
        items.append(item)
    return json.dumps(items, ensure_ascii=False, sort_keys=True)


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


def _greater(left: Any, right: Any) -> bool:
    left_value = _float(left)
    right_value = _float(right)
    return left_value is not None and right_value is not None and left_value > right_value


def _lower(left: Any, right: Any) -> bool:
    left_value = _float(left)
    right_value = _float(right)
    return left_value is not None and right_value is not None and left_value < right_value


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


def main() -> int:
    dashboard_path = PROJECT_ROOT / "frontend" / "public" / "prediction-dashboard.json"
    dashboard = json.loads(dashboard_path.read_text(encoding="utf-8")) if dashboard_path.exists() else {}
    payload = write_model_challenger_outputs(dashboard=dashboard)
    print(f"wrote frontend/public/model-leaderboard.json models={len(payload['leaderboard'].get('models', []))}")
    print("wrote frontend/public/model-promotion-status.json")
    print("wrote outputs/model_leaderboard.md")
    print("wrote outputs/model_promotion_rules.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
