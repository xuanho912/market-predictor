from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
HORIZONS = (1, 3, 5, 10, 20, 60)


def build_forecast_deviation_review(
    *,
    records_path: Path | None = None,
    news_event_bundle: dict[str, Any] | None = None,
    data_quality_report: dict[str, Any] | None = None,
    data_freshness_status: dict[str, Any] | None = None,
    max_items: int = 60,
) -> dict[str, Any]:
    records_path = records_path or PROJECT_ROOT / "outputs" / "forecast_records.csv"
    records = _read_records(records_path)
    deviations: list[dict[str, Any]] = []
    for record in records:
        for horizon in HORIZONS:
            item = _deviation_item(
                record,
                horizon,
                news_event_bundle or {},
                data_quality_report or {},
                data_freshness_status or {},
            )
            if item:
                deviations.append(item)

    deviations.sort(
        key=lambda item: (
            str(item.get("forecast_date") or ""),
            _horizon_days(str(item.get("horizon") or "")),
            float(item.get("absolute_error") or 0.0),
        ),
        reverse=True,
    )
    material = [item for item in deviations if item.get("material_deviation")]
    driver_counts: Counter[str] = Counter()
    for item in material:
        for driver in item.get("likely_error_drivers") or []:
            driver_counts[str(driver)] += 1

    summary = {
        "total_forecast_records": len(records),
        "completed_outcomes_reviewed": len(deviations),
        "material_deviation_count": len(material),
        "latest_forecast_date": max((str(item.get("forecast_date") or "") for item in records), default=None),
        "latest_reviewed_forecast_date": max((str(item.get("forecast_date") or "") for item in deviations), default=None),
        "latest_market_date": (data_freshness_status or {}).get("latest_market_date"),
        "data_freshness_status": (data_freshness_status or {}).get("data_freshness_status"),
        "largest_absolute_error": max((float(item.get("absolute_error") or 0.0) for item in deviations), default=None),
        "dominant_error_theme": driver_counts.most_common(1)[0][0] if driver_counts else "not_enough_completed_outcomes",
        "evidence_level": _evidence_level(len(deviations)),
        "validation_status": "not_yet_validated" if len(deviations) < 20 else "early_evidence",
        "update_blockers": _update_blockers(records, deviations, data_freshness_status or {}),
    }
    return {
        "version": "forecast_deviation_review_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "validation_type": "forecast_validation",
        "summary": summary,
        "latest_deviations": deviations[:max_items],
        "driver_counts": dict(driver_counts.most_common()),
        "review_questions": [
            "预测方向是否错了，还是方向对但幅度低估/高估？",
            "主路径是否输给了第二路径或风险路径？",
            "偏差是否来自新闻/事件驱动、波动率修复、信用、宽度、资金流、价格结构或数据缺失？",
            "高置信样本是否真的比普通样本偏差更小？",
        ],
        "guardrails": [
            "This is forecast error attribution, not a trading or PnL report.",
            "Attribution is diagnostic and probabilistic; it is not proof of causality.",
            "Forecast fields are not rewritten. Only completed outcome fields are reviewed.",
            "Alpha v1 threshold remains frozen at 0.32534311.",
        ],
    }


def render_forecast_deviation_review_markdown(payload: dict[str, Any]) -> str:
    summary = payload.get("summary") or {}
    lines = [
        "# Forecast Deviation Review",
        "",
        f"Generated at: `{payload.get('generated_at')}`",
        "",
        "This report reviews forecast-vs-actual deviations after horizons complete. It is not a trading, PnL or execution report.",
        "",
        "## Summary",
        "",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## Latest Material Deviations", ""])
    material = [item for item in (payload.get("latest_deviations") or []) if item.get("material_deviation")]
    if not material:
        lines.append("- No material completed deviations yet. Forward samples are still accumulating.")
    for item in material[:20]:
        lines.extend(
            [
                f"### {item.get('symbol')} {item.get('horizon')} from {item.get('forecast_date')}",
                "",
                f"- primary_scenario: `{item.get('primary_scenario')}`",
                f"- expected_return: `{item.get('expected_return')}`",
                f"- actual_return: `{item.get('actual_return')}`",
                f"- forecast_error: `{item.get('forecast_error')}`",
                f"- severity: `{item.get('severity')}`",
                f"- primary_hit: `{item.get('primary_hit')}`",
                f"- likely_error_drivers: `{', '.join(item.get('likely_error_drivers') or [])}`",
                f"- diagnostic_note: {item.get('diagnostic_note')}",
                "",
            ]
        )
    lines.extend(["", "## Guardrails", ""])
    for item in payload.get("guardrails") or []:
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def write_forecast_deviation_review_outputs(
    payload: dict[str, Any],
    *,
    public_dir: Path | None = None,
    outputs_dir: Path | None = None,
) -> None:
    public_dir = public_dir or PROJECT_ROOT / "frontend" / "public"
    outputs_dir = outputs_dir or PROJECT_ROOT / "outputs"
    public_dir.mkdir(parents=True, exist_ok=True)
    outputs_dir.mkdir(parents=True, exist_ok=True)
    (public_dir / "forecast-deviation-review.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (outputs_dir / "forecast_deviation_review.md").write_text(
        render_forecast_deviation_review_markdown(payload),
        encoding="utf-8",
    )


def _deviation_item(
    record: dict[str, Any],
    horizon: int,
    news_event_bundle: dict[str, Any],
    data_quality_report: dict[str, Any],
    data_freshness_status: dict[str, Any],
) -> dict[str, Any] | None:
    key = f"{horizon}d"
    actual = _float(record.get(f"actual_return_{key}"))
    if actual is None:
        return None
    expected_returns = _loads_dict(record.get("expected_return_by_horizon"))
    scenario_returns = _loads_dict(record.get("scenario_expected_return_by_horizon"))
    expected = _float(expected_returns.get(key))
    primary = str(record.get("primary_scenario") or "")
    primary_expected = _float((scenario_returns.get(key) or {}).get(primary))
    expected = primary_expected if primary_expected is not None else expected
    if expected is None:
        return None
    error = actual - expected
    abs_error = abs(error)
    threshold = _material_threshold(horizon)
    material = abs_error >= threshold
    drivers = _likely_error_drivers(
        record,
        actual,
        expected,
        error,
        threshold,
        news_event_bundle,
        data_quality_report,
        data_freshness_status,
    )
    return {
        "forecast_id": record.get("forecast_id"),
        "forecast_date": record.get("forecast_date"),
        "symbol": record.get("symbol"),
        "horizon": key,
        "model_version": record.get("model_version"),
        "primary_scenario": primary,
        "secondary_scenario": record.get("secondary_scenario"),
        "risk_scenario": record.get("risk_scenario"),
        "expected_return": _round(expected),
        "actual_return": _round(actual),
        "forecast_error": _round(error),
        "absolute_error": _round(abs_error),
        "error_direction": _error_direction(actual, expected, error, threshold),
        "severity": _severity(abs_error, threshold),
        "material_deviation": material,
        "primary_hit": _bool_or_none(record.get(f"primary_hit_{key}")),
        "best_matching_scenario": record.get(f"best_matching_scenario_{key}"),
        "path_error": _float(record.get(f"path_error_{key}")),
        "likely_error_drivers": drivers,
        "underweighted_factors": _underweighted_factors(record, actual, error, threshold, drivers),
        "overweighted_factors": _overweighted_factors(record, actual, error, threshold, drivers),
        "supporting_signals_at_forecast": _loads_list(record.get("supporting_signals")),
        "conflicting_signals_at_forecast": _loads_list(record.get("conflicting_signals")),
        "missing_data_at_forecast": _loads_list(record.get("missing_data")),
        "diagnostic_note": _diagnostic_note(record, actual, expected, drivers, material),
        "not_causal_proof": True,
    }


def _likely_error_drivers(
    record: dict[str, Any],
    actual: float,
    expected: float,
    error: float,
    threshold: float,
    news_event_bundle: dict[str, Any],
    data_quality_report: dict[str, Any],
    data_freshness_status: dict[str, Any],
) -> list[str]:
    drivers: list[str] = []
    supporting = set(_loads_list(record.get("supporting_signals")))
    conflicting = set(_loads_list(record.get("conflicting_signals")))
    missing = set(_loads_list(record.get("missing_data")))
    if abs(error) < threshold:
        return ["normal_forecast_noise"]
    if error > 0:
        drivers.append("model_underestimated_upside_or_repair")
        if _news_supports_risk_on(news_event_bundle) or "news_event_supports_bounce" in supporting:
            drivers.append("news_event_driver_underweighted")
        if "risk_off_news_event" in conflicting and actual > 0:
            drivers.append("risk_off_news_overweighted_or_resolved")
        if (_float(record.get("options_confirmation_score")) or 0) >= 75:
            drivers.append("volatility_repair_underweighted")
        if (_float(record.get("breadth_confirmation_score")) or 0) >= 70:
            drivers.append("breadth_follow_through_underweighted")
        if (_float(record.get("flow_confirmation_score")) or 0) >= 65:
            drivers.append("risk_on_flow_underweighted")
    else:
        drivers.append("model_underestimated_downside_or_failed_bounce")
        if "risk_off_news_event" in conflicting or _news_supports_risk_off(news_event_bundle):
            drivers.append("news_event_risk_underweighted")
        if (_float(record.get("options_conflict_score")) or 0) >= 55:
            drivers.append("volatility_or_tail_risk_underweighted")
        if (_float(record.get("breadth_conflict_score")) or 0) >= 55:
            drivers.append("breadth_conflict_underweighted")
        if (_float(record.get("flow_conflict_score")) or 0) >= 55:
            drivers.append("risk_off_flow_underweighted")
    if any("news" in item.lower() or "finnhub_news" in item.lower() for item in missing):
        drivers.append("news_data_gap_limited_attribution")
    freshness_status = str(data_freshness_status.get("data_freshness_status") or "")
    if (data_quality_report.get("summary") or {}).get("data_freshness_status") == "stale" or freshness_status == "stale":
        drivers.append("stale_data_risk")
    if freshness_status == "market_open_unconfirmed":
        drivers.append("intraday_snapshot_risk")
    return list(dict.fromkeys(drivers))


def _underweighted_factors(record: dict[str, Any], actual: float, error: float, threshold: float, drivers: list[str]) -> list[str]:
    if abs(error) < threshold:
        return []
    if error > 0:
        return [item for item in drivers if item.endswith("underweighted") or item in {"news_event_driver_underweighted", "volatility_repair_underweighted", "breadth_follow_through_underweighted", "risk_on_flow_underweighted"}]
    return [item for item in drivers if item.endswith("underweighted")]


def _overweighted_factors(record: dict[str, Any], actual: float, error: float, threshold: float, drivers: list[str]) -> list[str]:
    if abs(error) < threshold:
        return []
    out: list[str] = []
    if error > 0 and "risk_off_news_overweighted_or_resolved" in drivers:
        out.append("risk_off_news_or_macro_risk")
    if error < 0 and record.get("primary_scenario") in {"bounce_path", "analog_average_path"}:
        out.append("bounce_repair_assumption")
    return out


def _diagnostic_note(record: dict[str, Any], actual: float, expected: float, drivers: list[str], material: bool) -> str:
    if not material:
        return "实际结果与预测路径偏差不大，暂不做强归因。"
    if "news_event_driver_underweighted" in drivers:
        return "实际走势强于预测，复盘优先检查是否低估了新闻/事件催化，例如地缘缓和、油价回落或期货风险偏好改善。"
    if "news_event_risk_underweighted" in drivers:
        return "实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。"
    if "volatility_repair_underweighted" in drivers:
        return "实际走势强于预测，可能低估了波动率回落和恐慌释放后的修复力度。"
    if "breadth_conflict_underweighted" in drivers:
        return "实际走势弱于预测，可能低估了市场内部参与不足对主路径的拖累。"
    return "出现实质偏差，需要检查当时支持/冲突证据的权重是否合理。"


def _news_supports_risk_on(news_event_bundle: dict[str, Any]) -> bool:
    narrative = news_event_bundle.get("market_narrative") or {}
    direction = str(narrative.get("narrative_direction") or news_event_bundle.get("news_direction") or "")
    effect = news_event_bundle.get("prediction_logic_effect") or {}
    return "bounce" in direction or "risk_on" in direction or str(effect.get("direction")) in {"supports_bounce", "supports_trend_reversal"}


def _news_supports_risk_off(news_event_bundle: dict[str, Any]) -> bool:
    narrative = news_event_bundle.get("market_narrative") or {}
    direction = str(narrative.get("narrative_direction") or news_event_bundle.get("news_direction") or "")
    effect = news_event_bundle.get("prediction_logic_effect") or {}
    return "risk_expansion" in direction or "downside" in direction or "risk_off" in direction or str(effect.get("direction")) == "supports_risk_expansion"


def _update_blockers(
    records: list[dict[str, Any]],
    deviations: list[dict[str, Any]],
    data_freshness_status: dict[str, Any],
) -> list[dict[str, Any]]:
    blockers: list[dict[str, Any]] = []
    freshness_status = str(data_freshness_status.get("data_freshness_status") or "")
    if freshness_status in {"stale", "provider_failed", "market_open_unconfirmed"}:
        blockers.append(
            {
                "reason": freshness_status,
                "detail": data_freshness_status.get("warning_message")
                or "Data freshness gate blocked current-day forecast validation.",
            }
        )

    latest_forecast_date = max((str(row.get("forecast_date") or "")[:10] for row in records), default="")
    latest_market_date = str(data_freshness_status.get("latest_market_date") or "")[:10]
    if latest_forecast_date and latest_market_date and latest_market_date <= latest_forecast_date:
        blockers.append(
            {
                "reason": "no_future_market_close_yet",
                "detail": (
                    f"Latest market date {latest_market_date} is not after latest forecast date "
                    f"{latest_forecast_date}, so no completed 1d/3d/5d outcome can be scored yet."
                ),
            }
        )

    if records and "actual_return_1d" not in records[0]:
        blockers.append(
            {
                "reason": "legacy_records_missing_1d_fields",
                "detail": "Older forecast_records.csv was created before 1d outcome fields were added; the next valid export will migrate the ledger columns.",
            }
        )

    completed_actual_fields = [
        (row.get("forecast_date"), row.get("symbol"), f"{horizon}d")
        for row in records
        for horizon in HORIZONS
        if _float(row.get(f"actual_return_{horizon}d")) is not None
    ]
    if completed_actual_fields and not deviations:
        blockers.append(
            {
                "reason": "completed_actuals_without_comparable_expected_path",
                "detail": (
                    "Some actual returns have been backfilled, but the matching historical forecast record "
                    "does not contain an expected path for that horizon, so success/failure cannot be scored without rewriting old forecast fields."
                ),
            }
        )

    if not deviations and not blockers:
        blockers.append(
            {
                "reason": "waiting_for_completed_horizons",
                "detail": "Forecasts exist, but no configured horizon has a completed future close and actual_return backfill yet.",
            }
        )
    return blockers


def _read_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _loads_dict(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    if not value:
        return {}
    try:
        parsed = json.loads(str(value))
    except Exception:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def _loads_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    if not value:
        return []
    try:
        parsed = json.loads(str(value))
    except Exception:
        return []
    return [str(item) for item in parsed] if isinstance(parsed, list) else []


def _float(value: Any) -> float | None:
    try:
        if value in (None, ""):
            return None
        return float(value)
    except Exception:
        return None


def _bool_or_none(value: Any) -> bool | None:
    if value in (None, ""):
        return None
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"true", "1", "yes"}:
        return True
    if text in {"false", "0", "no"}:
        return False
    return None


def _round(value: float | None) -> float | None:
    return round(value, 6) if value is not None else None


def _material_threshold(horizon: int) -> float:
    return {
        1: 0.008,
        3: 0.012,
        5: 0.016,
        10: 0.025,
        20: 0.04,
        60: 0.07,
    }.get(horizon, 0.02)


def _severity(abs_error: float, threshold: float) -> str:
    if abs_error < threshold:
        return "normal"
    if abs_error < threshold * 1.75:
        return "moderate"
    if abs_error < threshold * 3:
        return "large"
    return "extreme"


def _error_direction(actual: float, expected: float, error: float, threshold: float) -> str:
    if abs(error) < threshold:
        return "within_expected_noise"
    if error > 0:
        return "actual_stronger_than_forecast"
    return "actual_weaker_than_forecast"


def _horizon_days(value: str) -> int:
    try:
        return int(value.replace("d", ""))
    except Exception:
        return 0


def _evidence_level(count: int) -> str:
    if count < 20:
        return "insufficient_samples"
    if count < 50:
        return "early_evidence"
    if count < 100:
        return "moderate_evidence"
    return "stronger_evidence"


if __name__ == "__main__":
    news_path = PROJECT_ROOT / "frontend" / "public" / "news-event-status.json"
    quality_path = PROJECT_ROOT / "frontend" / "public" / "data_quality_report.json"
    freshness_path = PROJECT_ROOT / "frontend" / "public" / "data-freshness-status.json"
    news = _loads_dict(news_path.read_text(encoding="utf-8")) if news_path.exists() else {}
    quality = _loads_dict(quality_path.read_text(encoding="utf-8")) if quality_path.exists() else {}
    freshness = _loads_dict(freshness_path.read_text(encoding="utf-8")) if freshness_path.exists() else {}
    review = build_forecast_deviation_review(
        news_event_bundle=news,
        data_quality_report=quality,
        data_freshness_status=freshness,
    )
    write_forecast_deviation_review_outputs(review)
    print("wrote frontend/public/forecast-deviation-review.json")
    print("wrote outputs/forecast_deviation_review.md")
