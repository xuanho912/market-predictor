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
    raw_records = _read_records(records_path)
    records = _dedupe_records_for_validation(raw_records)
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

    learning_summary = _model_learning_summary(material, driver_counts)
    summary = {
        "total_forecast_records": len(records),
        "raw_forecast_rows": len(raw_records),
        "deduped_legacy_rows": max(0, len(raw_records) - len(records)),
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
        "correction_policy": "past_forecasts_are_not_rewritten_only_actuals_and_error_fields_are_backfilled",
        "model_learning_status": learning_summary["status"],
    }
    return {
        "version": "forecast_deviation_review_v2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "validation_type": "forecast_validation",
        "summary": summary,
        "latest_deviations": deviations[:max_items],
        "driver_counts": dict(driver_counts.most_common()),
        "model_learning_summary": learning_summary,
        "model_upgrade_plan": _model_upgrade_plan(driver_counts, len(deviations), len(material)),
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
            "Baseline v1 is not changed by this review. Lessons must enter a challenger first.",
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
                f"- secondary_scenario: `{item.get('secondary_scenario')}`",
                f"- risk_scenario: `{item.get('risk_scenario')}`",
                f"- expected_return: `{item.get('expected_return')}`",
                f"- actual_return: `{item.get('actual_return')}`",
                f"- forecast_error: `{item.get('forecast_error')}`",
                f"- severity: `{item.get('severity')}`",
                f"- primary_hit: `{item.get('primary_hit')}`",
                f"- best_matching_scenario: `{item.get('best_matching_scenario')}`",
                f"- likely_error_drivers: `{', '.join(item.get('likely_error_drivers') or [])}`",
                f"- underweighted_factors: `{', '.join(item.get('underweighted_factors') or [])}`",
                f"- overweighted_factors: `{', '.join(item.get('overweighted_factors') or [])}`",
                f"- diagnostic_note: {item.get('diagnostic_note')}",
                "",
            ]
        )

    lines.extend(["", "## Model Learning Summary", ""])
    learning = payload.get("model_learning_summary") or {}
    for key, value in learning.items():
        if key == "lessons":
            continue
        lines.append(f"- {key}: `{value}`")
    lessons = learning.get("lessons") or []
    if lessons:
        lines.extend(["", "### Lessons", ""])
        for item in lessons:
            lines.append(
                f"- `{item.get('driver')}` count `{item.get('count')}`: {item.get('lesson')} "
                f"Action: {item.get('future_model_action')}"
            )

    lines.extend(["", "## Model Upgrade Plan", ""])
    for item in payload.get("model_upgrade_plan") or []:
        lines.append(f"- {item}")

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
    scenario_returns_all = _loads_dict(record.get("scenario_expected_return_by_horizon"))
    scenario_returns, expected_source = _scenario_returns_for_horizon(scenario_returns_all, horizon)
    expected = _float(expected_returns.get(key))
    primary = str(record.get("primary_scenario") or "")
    primary_expected = _float(scenario_returns.get(primary))
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
        "expected_return_source": expected_source if primary_expected is not None else "expected_return_by_horizon",
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
        "underweighted_factors": _underweighted_factors(record, error, threshold, drivers),
        "overweighted_factors": _overweighted_factors(record, error, threshold, drivers),
        "supporting_signals_at_forecast": _loads_list(record.get("supporting_signals")),
        "conflicting_signals_at_forecast": _loads_list(record.get("conflicting_signals")),
        "missing_data_at_forecast": _loads_list(record.get("missing_data")),
        "diagnostic_note": _diagnostic_note(record, drivers, material),
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


def _underweighted_factors(record: dict[str, Any], error: float, threshold: float, drivers: list[str]) -> list[str]:
    if abs(error) < threshold:
        return []
    if error > 0:
        allowed = {
            "news_event_driver_underweighted",
            "volatility_repair_underweighted",
            "breadth_follow_through_underweighted",
            "risk_on_flow_underweighted",
        }
        return [item for item in drivers if item.endswith("underweighted") or item in allowed]
    return [item for item in drivers if item.endswith("underweighted")]


def _overweighted_factors(record: dict[str, Any], error: float, threshold: float, drivers: list[str]) -> list[str]:
    if abs(error) < threshold:
        return []
    out: list[str] = []
    if error > 0 and "risk_off_news_overweighted_or_resolved" in drivers:
        out.append("risk_off_news_or_macro_risk")
    if error < 0 and record.get("primary_scenario") in {"bounce_path", "analog_average_path"}:
        out.append("bounce_repair_assumption")
    return out


def _diagnostic_note(record: dict[str, Any], drivers: list[str], material: bool) -> str:
    if not material:
        return "实际结果与预测路径偏差不大，暂不做强归因。"
    if "news_event_driver_underweighted" in drivers:
        return "实际走势强于预测，复盘优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落或期货风险偏好改善。"
    if "news_event_risk_underweighted" in drivers:
        return "实际走势弱于预测，复盘优先检查是否低估了新闻/事件风险或利空价格确认。"
    if "risk_off_news_overweighted_or_resolved" in drivers:
        return "实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。"
    if "volatility_repair_underweighted" in drivers:
        return "实际走势强于预测，可能低估了波动率回落和恐慌释放后的修复力度。"
    if "breadth_conflict_underweighted" in drivers:
        return "实际走势弱于预测，可能低估了市场内部参与不足对主路径的拖累。"
    return "出现实质偏差，需要检查当时支持/冲突证据的权重是否合理。"


def _model_learning_summary(material: list[dict[str, Any]], driver_counts: Counter[str]) -> dict[str, Any]:
    lessons = []
    for driver, count in driver_counts.most_common():
        lessons.append(
            {
                "driver": driver,
                "count": count,
                "lesson": _driver_lesson(driver),
                "future_model_action": _driver_action(driver),
                "baseline_change_allowed": False,
            }
        )
    if not lessons:
        lessons.append(
            {
                "driver": "not_enough_completed_outcomes",
                "count": 0,
                "lesson": "还没有足够到期样本，不能根据主观感觉修改模型。",
                "future_model_action": "继续回填实际结果；至少 20 个完成样本后再评估权重调整。",
                "baseline_change_allowed": False,
            }
        )
    status = "lessons_ready_for_shadow_challenger" if len(material) >= 20 else "insufficient_forward_evidence"
    return {
        "status": status,
        "material_deviation_samples": len(material),
        "minimum_samples_before_weight_change": 20,
        "recommended_challenger": "challenger_v2_error_learning",
        "baseline_v1_policy": "frozen_do_not_rewrite",
        "lessons": lessons,
    }


def _model_upgrade_plan(driver_counts: Counter[str], completed_count: int, material_count: int) -> list[str]:
    plan = [
        "不改写旧预测；只允许回填 actual_return、best_matching_scenario、primary_hit、path_error。",
        "baseline_v1 保持冻结；经验先进入 challenger_v2_error_learning 的 shadow 评估。",
    ]
    if completed_count < 20:
        plan.append("完成样本少于 20，暂不允许基于偏差调整主模型权重。")
    if material_count == 0:
        plan.append("当前没有足够实质偏差样本；继续积累前向验证。")
    if driver_counts.get("news_event_driver_underweighted"):
        plan.append("在 challenger 中提高“重大新闻 + 价格反应确认”的短周期权重。")
    if driver_counts.get("risk_off_news_overweighted_or_resolved"):
        plan.append("在 challenger 中要求 risk-off 新闻必须得到价格确认，否则降低风险路径权重。")
    if driver_counts.get("volatility_repair_underweighted"):
        plan.append("在 challenger 中提高 VIX/VVIX/SKEW 修复对 1d/3d/5d 反抽路径的影响。")
    if driver_counts.get("breadth_conflict_underweighted"):
        plan.append("在 challenger 中提高 breadth 冲突对失败反抽风险的惩罚。")
    if driver_counts.get("risk_on_flow_underweighted"):
        plan.append("在 challenger 中提高 risk-on flow proxy 与成交量确认的共振权重。")
    return plan


def _driver_lesson(driver: str) -> str:
    lessons = {
        "model_underestimated_upside_or_repair": "模型低估了修复/反抽强度，需要检查事件催化、波动率修复和价格确认。",
        "model_underestimated_downside_or_failed_bounce": "模型低估了下跌延续或反抽失败风险，需要检查信用、宽度、波动率和新闻风险。",
        "news_event_driver_underweighted": "重大新闻如果被价格确认，短周期影响可能大于历史相似样本。",
        "news_event_risk_underweighted": "风险新闻如果被价格确认，应提高风险路径权重。",
        "risk_off_news_overweighted_or_resolved": "risk-off 新闻若快速缓和或未被价格确认，不能继续压低主路径。",
        "volatility_repair_underweighted": "波动率结构修复会放大短线反抽，需要进入 1d/3d/5d 权重。",
        "breadth_follow_through_underweighted": "宽度改善后的持续承接可能被低估。",
        "breadth_conflict_underweighted": "指数上涨但内部参与不足时，失败反抽风险可能被低估。",
        "risk_on_flow_underweighted": "risk-on flow 与成交量确认同向时，短线弹性可能被低估。",
        "risk_off_flow_underweighted": "risk-off flow 与价格走弱同向时，下跌延续风险可能被低估。",
        "news_data_gap_limited_attribution": "新闻数据缺口会限制归因质量，需要标记而不是事后编故事。",
        "stale_data_risk": "数据过期时不应输出今日判断。",
    }
    return lessons.get(driver, "该偏差主题需要继续积累样本后再判断是否稳定。")


def _driver_action(driver: str) -> str:
    actions = {
        "news_event_driver_underweighted": "shadow-test event_reaction_overlay：新闻方向必须与 SPY/QQQ、VIX、HYG/LQD 价格反应一致。",
        "news_event_risk_underweighted": "shadow-test risk_event_confirmation：risk-off 新闻得到价格确认才提高风险路径。",
        "risk_off_news_overweighted_or_resolved": "shadow-test news_decay：未被价格确认或快速缓和的 risk-off 新闻权重衰减。",
        "volatility_repair_underweighted": "shadow-test vol_repair_boost：VIX term 修复提高短周期 bounce 权重。",
        "breadth_follow_through_underweighted": "shadow-test breadth_follow_through：宽度改善持续两日以上才提高中期修复权重。",
        "breadth_conflict_underweighted": "shadow-test breadth_conflict_penalty：宽度冲突提高 failed_bounce 风险。",
        "risk_on_flow_underweighted": "shadow-test flow_confirmation_boost：risk-on flow 与成交量共振提高短线弹性。",
        "risk_off_flow_underweighted": "shadow-test flow_conflict_penalty：risk-off flow 提高 downside continuation。",
    }
    return actions.get(driver, "keep_observing_until_forward_sample_gate")


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
        (row, horizon)
        for row in records
        for horizon in HORIZONS
        if _float(row.get(f"actual_return_{horizon}d")) is not None
    ]
    not_comparable = [
        (row.get("forecast_date"), row.get("symbol"), f"{horizon}d")
        for row, horizon in completed_actual_fields
        if not _has_comparable_expected_path(row, horizon)
    ]
    if completed_actual_fields and not deviations and not_comparable:
        blockers.append(
            {
                "reason": "completed_actuals_without_comparable_expected_path",
                "detail": (
                    "Some actual returns have been backfilled, but the matching historical forecast record "
                    "does not contain a stored or safely derived expected path for that horizon, so success/failure cannot be scored without rewriting old forecast fields."
                ),
                "examples": not_comparable[:8],
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


def _dedupe_records_for_validation(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str], dict[str, Any]] = {}
    for row in rows:
        key = (
            str(row.get("forecast_date") or ""),
            str(row.get("model_version") or ""),
            str(row.get("symbol") or ""),
        )
        current = grouped.get(key)
        if current is None or _completed_field_count(row) > _completed_field_count(current):
            grouped[key] = row
    return [grouped[key] for key in sorted(grouped)]


def _completed_field_count(row: dict[str, Any]) -> int:
    return sum(1 for horizon in HORIZONS if _float(row.get(f"actual_return_{horizon}d")) is not None)


def _scenario_returns_for_horizon(scenario_returns: dict[str, Any], horizon: int) -> tuple[dict[str, Any], str]:
    key = f"{horizon}d"
    direct = scenario_returns.get(key)
    if isinstance(direct, dict) and direct:
        return direct, "stored_scenario_path"

    available: list[tuple[int, dict[str, Any]]] = []
    for raw_key, value in scenario_returns.items():
        if not isinstance(value, dict):
            continue
        try:
            days = int(str(raw_key).replace("d", ""))
        except ValueError:
            continue
        if days > 0:
            available.append((days, value))
    if not available:
        return {}, "missing_expected_path"

    nearest_days, nearest_values = min(available, key=lambda item: abs(item[0] - horizon))
    scale = horizon / nearest_days
    derived = {
        scenario: (_float(value) * scale if _float(value) is not None else None)
        for scenario, value in nearest_values.items()
    }
    return derived, f"derived_from_{nearest_days}d_path"


def _has_comparable_expected_path(row: dict[str, Any], horizon: int) -> bool:
    scenario_returns, _ = _scenario_returns_for_horizon(
        _loads_dict(row.get("scenario_expected_return_by_horizon")),
        horizon,
    )
    primary = str(row.get("primary_scenario") or "")
    if primary and _float(scenario_returns.get(primary)) is not None:
        return True
    expected = _loads_dict(row.get("expected_return_by_horizon")).get(f"{horizon}d")
    return _float(expected) is not None


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


_build_forecast_deviation_review_impl = build_forecast_deviation_review


def build_forecast_deviation_review(*args: Any, **kwargs: Any) -> dict[str, Any]:
    payload = _build_forecast_deviation_review_impl(*args, **kwargs)
    payload["review_questions"] = [
        "预测方向错了，还是方向对但幅度低估/高估？",
        "主路径是否输给了第二路径或风险路径？",
        "偏差是否来自新闻/事件、波动率修复、信用、宽度、资金流、价格结构或数据缺口？",
        "高置信样本是否真的比普通样本偏差更小？",
    ]
    return payload


def _diagnostic_note(record: dict[str, Any], drivers: list[str], material: bool) -> str:
    if not material:
        return "实际结果与预测路径偏差不大，暂不做强归因。"
    if "news_event_driver_underweighted" in drivers:
        return "实际走势强于预测，优先检查是否低估了新闻/事件催化，例如地缘风险缓和、油价回落、政策或期货风险偏好改善。"
    if "news_event_risk_underweighted" in drivers:
        return "实际走势弱于预测，优先检查是否低估了新闻/事件风险，或利空是否得到了价格确认。"
    if "risk_off_news_overweighted_or_resolved" in drivers:
        return "实际走势强于预测，说明 risk-off 新闻可能未被价格确认、已被市场消化，或风险快速缓和。"
    if "volatility_repair_underweighted" in drivers:
        return "实际走势强于预测，可能低估了波动率回落和恐慌释放后的修复力度。"
    if "breadth_conflict_underweighted" in drivers:
        return "实际走势弱于预测，可能低估了市场内部参与不足对主路径的拖累。"
    if "risk_off_flow_underweighted" in drivers:
        return "实际走势弱于预测，可能低估了风险偏好资金流转弱对下跌延续路径的影响。"
    if "risk_on_flow_underweighted" in drivers:
        return "实际走势强于预测，可能低估了风险偏好资金流与成交量共振的短线弹性。"
    return "出现实质偏差，需要复盘当时支持/冲突证据的权重是否合理；该归因是诊断，不是因果证明。"


def _model_learning_summary(material: list[dict[str, Any]], driver_counts: Counter[str]) -> dict[str, Any]:
    lessons = []
    for driver, count in driver_counts.most_common():
        lessons.append(
            {
                "driver": driver,
                "count": count,
                "lesson": _driver_lesson(driver),
                "future_model_action": _driver_action(driver),
                "baseline_change_allowed": False,
            }
        )
    if not lessons:
        lessons.append(
            {
                "driver": "not_enough_completed_outcomes",
                "count": 0,
                "lesson": "还没有足够到期样本，不能根据主观感觉修改模型。",
                "future_model_action": "继续回填实际结果；至少 20 个完成样本后再评估 challenger 权重调整。",
                "baseline_change_allowed": False,
            }
        )
    status = "lessons_ready_for_shadow_challenger" if len(material) >= 20 else "insufficient_forward_evidence"
    return {
        "status": status,
        "material_deviation_samples": len(material),
        "minimum_samples_before_weight_change": 20,
        "recommended_challenger": "challenger_v2_error_learning",
        "baseline_v1_policy": "frozen_do_not_rewrite",
        "lessons": lessons,
    }


def _model_upgrade_plan(driver_counts: Counter[str], completed_count: int, material_count: int) -> list[str]:
    plan = [
        "不改写旧预测；只允许回填 actual_return、best_matching_scenario、primary_hit、path_error。",
        "baseline_v1 保持冻结；经验先进入 challenger_v2_error_learning 的 shadow 评估。",
    ]
    if completed_count < 20:
        plan.append("完成样本少于 20，暂不允许基于偏差调整主模型权重。")
    if material_count == 0:
        plan.append("当前没有足够实质偏差样本；继续积累前向验证。")
    if driver_counts.get("news_event_driver_underweighted"):
        plan.append("在 challenger 中提高“重大新闻 + 价格反应确认”的短周期权重。")
    if driver_counts.get("risk_off_news_overweighted_or_resolved"):
        plan.append("在 challenger 中要求 risk-off 新闻必须得到价格确认，否则降低风险路径权重。")
    if driver_counts.get("volatility_repair_underweighted"):
        plan.append("在 challenger 中提高 VIX/VVIX/SKEW 修复对 1d/3d/5d 反抽路径的影响。")
    if driver_counts.get("breadth_conflict_underweighted"):
        plan.append("在 challenger 中提高 breadth 冲突对失败反抽风险的惩罚。")
    if driver_counts.get("risk_on_flow_underweighted"):
        plan.append("在 challenger 中提高 risk-on flow proxy 与成交量确认的共振权重。")
    return plan


def _driver_lesson(driver: str) -> str:
    lessons = {
        "model_underestimated_upside_or_repair": "模型低估了修复/反抽强度，需要检查事件催化、波动率修复和价格确认。",
        "model_underestimated_downside_or_failed_bounce": "模型低估了下跌延续或反抽失败风险，需要检查信用、宽度、波动率和新闻风险。",
        "news_event_driver_underweighted": "重大新闻如果被价格确认，短周期影响可能大于历史相似样本。",
        "news_event_risk_underweighted": "风险新闻如果被价格确认，应提高风险路径权重。",
        "risk_off_news_overweighted_or_resolved": "risk-off 新闻若快速缓和或未被价格确认，不应继续压低主路径。",
        "volatility_repair_underweighted": "波动率结构修复会放大短线反抽，需要进入 1d/3d/5d 权重验证。",
        "volatility_or_tail_risk_underweighted": "尾部风险或波动率重新上升时，失败反抽/风险扩散可能被低估。",
        "breadth_follow_through_underweighted": "宽度改善后的持续承接可能被低估。",
        "breadth_conflict_underweighted": "指数上涨但内部参与不足时，失败反抽风险可能被低估。",
        "risk_on_flow_underweighted": "risk-on flow 与成交量确认同向时，短线弹性可能被低估。",
        "risk_off_flow_underweighted": "risk-off flow 与价格走弱同向时，下跌延续风险可能被低估。",
        "news_data_gap_limited_attribution": "新闻数据缺口会限制归因质量，需要标记而不是事后编故事。",
        "stale_data_risk": "数据过期时不应输出今日判断。",
        "intraday_snapshot_risk": "盘中快照未确认时，不应冻结为正式收盘预测。",
    }
    return lessons.get(driver, "该偏差主题需要继续积累样本后再判断是否稳定。")


def _driver_action(driver: str) -> str:
    actions = {
        "news_event_driver_underweighted": "shadow-test event_reaction_overlay：新闻方向必须与 SPY/QQQ、VIX、HYG/LQD 价格反应一致。",
        "news_event_risk_underweighted": "shadow-test risk_event_confirmation：risk-off 新闻得到价格确认才提高风险路径。",
        "risk_off_news_overweighted_or_resolved": "shadow-test news_decay：未被价格确认或快速缓和的 risk-off 新闻权重衰减。",
        "volatility_repair_underweighted": "shadow-test vol_repair_boost：VIX term 修复提高短周期 bounce 权重。",
        "volatility_or_tail_risk_underweighted": "shadow-test tail_risk_penalty：VVIX/SKEW/VIX term 恶化时提高风险路径。",
        "breadth_follow_through_underweighted": "shadow-test breadth_follow_through：宽度改善持续两日以上才提高中期修复权重。",
        "breadth_conflict_underweighted": "shadow-test breadth_conflict_penalty：宽度冲突提高 failed_bounce 风险。",
        "risk_on_flow_underweighted": "shadow-test flow_confirmation_boost：risk-on flow 与成交量共振提高短线弹性。",
        "risk_off_flow_underweighted": "shadow-test flow_conflict_penalty：risk-off flow 提高 downside continuation。",
    }
    return actions.get(driver, "keep_observing_until_forward_sample_gate")


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
