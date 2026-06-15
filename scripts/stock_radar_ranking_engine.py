from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
STOCK_MODEL_VERSION = "stock_baseline_v1"
RADAR_VERSION = "next_day_stock_radar_v1"


def build_top_stock_candidates(
    stock_dashboard: dict[str, Any],
    *,
    records_path: Path | None = None,
    write_ledger: bool = True,
    top_n: int = 20,
) -> dict[str, Any]:
    symbols = stock_dashboard.get("symbols") or {}
    candidates = [_candidate_from_symbol(symbol, payload) for symbol, payload in symbols.items()]
    candidates = [candidate for candidate in candidates if candidate.get("data_status") == "available"]
    candidates.sort(key=lambda item: (_float(item.get("final_radar_score")) or 0.0), reverse=True)
    for index, candidate in enumerate(candidates, start=1):
        candidate["rank"] = index
        candidate["whether_top10_candidate"] = index <= 10
    top_candidates = candidates[:top_n]
    if write_ledger:
        update_stock_forecast_records_with_radar(top_candidates, records_path=records_path)
    payload = {
        "version": RADAR_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "as_of": stock_dashboard.get("as_of"),
        "model_version": stock_dashboard.get("model_version") or STOCK_MODEL_VERSION,
        "universe_size": len(candidates),
        "top_n": top_n,
        "command_center": _command_center(top_candidates, stock_dashboard),
        "top_candidates": top_candidates,
        "notes": [
            "This radar ranks next-day high-elasticity forecast candidates, not trade recommendations.",
            "Missing company news, earnings, options or real flow lowers confidence and is not filled synthetically.",
            "Candidates are evaluated after the market dashboard context; the market remains the first layer.",
        ],
    }
    return payload


def build_stock_radar_validation_scorecard(records_path: Path | None = None) -> dict[str, Any]:
    records_path = records_path or PROJECT_ROOT / "outputs" / "stock_forecast_records.csv"
    records = _read_records(records_path)
    completed = [record for record in records if _actual_next_day_return(record) is not None]
    top10 = [record for record in completed if _truthy(record.get("whether_top10_candidate"))]
    non_top10 = [record for record in completed if not _truthy(record.get("whether_top10_candidate"))]
    high_score = _top_percentile(completed, "final_radar_score", 0.2)
    low_score = _bottom_percentile(completed, "final_radar_score", 0.2)
    high_confluence = _top_percentile(completed, "confluence_score", 0.2)
    low_confluence = _bottom_percentile(completed, "confluence_score", 0.2)
    catalyst_candidates = [record for record in completed if (_float(record.get("catalyst_score")) or 0) >= 50]
    high_risk = [record for record in completed if (_float(record.get("risk_score")) or 0) >= 65]
    scorecard = {
        "version": "stock_radar_validation_scorecard_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "validation_type": "forward_validation",
        "total_records": len(records),
        "completed_next_day_samples": len(completed),
        "pending_records": len(records) - len(completed),
        "evidence_level": _evidence_level(len(completed)),
        "validation_status": "not_yet_validated" if len(completed) < 20 else "early_evidence",
        "top10_vs_watchlist": {
            "top10": _performance(top10),
            "non_top10": _performance(non_top10),
            "answer": _comparison_answer(top10, non_top10, "avg_abs_next_day_return"),
            "question": "Top 10 candidates 是否比普通 watchlist 股票波动更大？",
        },
        "final_radar_score_effectiveness": {
            "high_score_top20pct": _performance(high_score),
            "low_score_bottom20pct": _performance(low_score),
            "answer": _comparison_answer(high_score, low_score, "avg_abs_next_day_return"),
            "question": "high final_radar_score 是否真的对应更大次日 range？",
        },
        "confluence_effectiveness": {
            "high_confluence_top20pct": _performance(high_confluence),
            "low_confluence_bottom20pct": _performance(low_confluence),
            "answer": _comparison_answer(high_confluence, low_confluence, "primary_hit_rate"),
            "question": "high confluence 是否真的更准？",
        },
        "catalyst_effectiveness": {
            "catalyst_candidates": _performance(catalyst_candidates),
            "all_completed": _performance(completed),
            "answer": _comparison_answer(catalyst_candidates, completed, "avg_abs_next_day_return"),
            "question": "catalyst candidates 是否真的波动更大？",
        },
        "risk_score_effectiveness": {
            "high_risk": _performance(high_risk),
            "all_completed": _performance(completed),
            "answer": _comparison_answer(high_risk, completed, "failure_rate"),
            "question": "risk_score 高的股票是否真的更容易失败？",
        },
        "not_validated_warning": (
            "not_enough_forward_samples"
            if len(completed) < 20
            else "early evidence only; do not treat the radar as validated alpha"
        ),
    }
    return scorecard


def render_top_stock_candidates_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Next-Day Stock Radar v1",
        "",
        f"Generated at: `{payload.get('generated_at')}`",
        f"As of: `{payload.get('as_of')}`",
        "",
        "This report ranks next-day high-elasticity stock forecast candidates. It is not a trading report and does not contain buy/sell instructions.",
        "",
        "## Command Center",
        "",
    ]
    command = payload.get("command_center") or {}
    for key in (
        "radar_status",
        "top_candidate",
        "top3_candidates",
        "market_context_note",
        "data_freshness_note",
        "validation_status",
        "risk_note",
    ):
        lines.append(f"- {key}: `{command.get(key)}`")
    lines.extend(["", "## Top Candidates", "", "| Rank | Ticker | Type | Radar | Elasticity | Confluence | Catalyst | Risk | Range | Trigger | Invalidation | Reason |", "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- |"])
    for item in payload.get("top_candidates") or []:
        rng = item.get("expected_next_day_range") or {}
        lines.append(
            "| {rank} | {ticker} | {candidate_type} | {final_radar_score} | {elasticity_score} | "
            "{confluence_score} | {catalyst_score} | {risk_score} | {low}-{high} | {trigger} | {invalid} | {reason} |".format(
                rank=item.get("rank"),
                ticker=item.get("ticker"),
                candidate_type=item.get("candidate_type"),
                final_radar_score=item.get("final_radar_score"),
                elasticity_score=item.get("elasticity_score"),
                confluence_score=item.get("confluence_score"),
                catalyst_score=item.get("catalyst_score"),
                risk_score=item.get("risk_score"),
                low=rng.get("low"),
                high=rng.get("high"),
                trigger=item.get("upside_trigger_level"),
                invalid=item.get("invalidation_level"),
                reason=str(item.get("one_line_reason") or "").replace("|", "/"),
            )
        )
    lines.extend(["", "Validation status: `not_yet_validated` until enough forward samples complete.", ""])
    return "\n".join(lines)


def render_stock_radar_validation_scorecard(payload: dict[str, Any]) -> str:
    lines = [
        "# Stock Radar Validation Scorecard",
        "",
        f"Generated at: `{payload.get('generated_at')}`",
        "",
        f"- total_records: `{payload.get('total_records')}`",
        f"- completed_next_day_samples: `{payload.get('completed_next_day_samples')}`",
        f"- pending_records: `{payload.get('pending_records')}`",
        f"- evidence_level: `{payload.get('evidence_level')}`",
        f"- validation_status: `{payload.get('validation_status')}`",
        f"- warning: `{payload.get('not_validated_warning')}`",
        "",
        "## Questions",
        "",
    ]
    for section in (
        "top10_vs_watchlist",
        "final_radar_score_effectiveness",
        "confluence_effectiveness",
        "catalyst_effectiveness",
        "risk_score_effectiveness",
    ):
        block = payload.get(section) or {}
        lines.append(f"- {block.get('question')}: `{block.get('answer')}`")
    lines.extend(["", "This scorecard validates forecasts only. It is not a trading, PnL or paper trading report.", ""])
    return "\n".join(lines)


def update_stock_forecast_records_with_radar(
    top_candidates: list[dict[str, Any]],
    *,
    records_path: Path | None = None,
) -> None:
    records_path = records_path or PROJECT_ROOT / "outputs" / "stock_forecast_records.csv"
    rows = _read_records(records_path)
    if not rows:
        return
    candidate_by_id = {
        _forecast_id(str(item.get("forecast_date") or item.get("as_of") or ""), str(item.get("model_version") or STOCK_MODEL_VERSION), str(item.get("ticker") or "")): item
        for item in top_candidates
    }
    extra_fields = [
        "top_rank",
        "candidate_type",
        "radar_level",
        "final_radar_score",
        "elasticity_score",
        "catalyst_score",
        "risk_score",
        "expected_next_day_range",
        "actual_next_day_return",
        "actual_next_day_high_low_range",
        "whether_top10_candidate",
    ]
    fieldnames = list(rows[0].keys())
    for field in extra_fields:
        if field not in fieldnames:
            fieldnames.append(field)
    for row in rows:
        candidate = candidate_by_id.get(str(row.get("forecast_id") or ""))
        if not candidate:
            row.setdefault("whether_top10_candidate", "false")
            continue
        row["top_rank"] = candidate.get("rank")
        row["candidate_type"] = candidate.get("candidate_type")
        row["radar_level"] = candidate.get("radar_level")
        row["final_radar_score"] = candidate.get("final_radar_score")
        row["elasticity_score"] = candidate.get("elasticity_score")
        row["catalyst_score"] = candidate.get("catalyst_score")
        row["risk_score"] = candidate.get("risk_score")
        row["expected_next_day_range"] = json.dumps(candidate.get("expected_next_day_range"), sort_keys=True)
        row["whether_top10_candidate"] = "true" if candidate.get("whether_top10_candidate") else "false"
        row.setdefault("actual_next_day_return", "")
        row.setdefault("actual_next_day_high_low_range", "")
    records_path.parent.mkdir(parents=True, exist_ok=True)
    with records_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _candidate_from_symbol(symbol: str, payload: dict[str, Any]) -> dict[str, Any]:
    features = payload.get("features") or {}
    trend = features.get("price_trend") or {}
    volume = features.get("volume") or {}
    rel = features.get("relative_strength") or {}
    volatility = features.get("volatility") or {}
    ranking = payload.get("scenario_ranking") or {}
    primary = ranking.get("primary") or {}
    secondary = ranking.get("secondary") or {}
    risk = ranking.get("risk") or {}
    confluence = payload.get("stock_confluence") or {}
    modules = confluence.get("module_scores") or {}
    levels = ((payload.get("forecast_price_levels") or {}).get("trigger_levels") or {})
    price_table = ((payload.get("forecast_price_levels") or {}).get("forecast_price_table") or {})
    one_day = price_table.get("1d") or {}
    data_quality = payload.get("data_quality") or {}
    volume_z = _float(volume.get("volume_z_score")) or 0.0
    volume_vs_20d = _float(volume.get("volume_vs_20d_average")) or 0.0
    atr_pct = _float(volatility.get("atr_pct")) or 0.0
    realized_vol = _float(volatility.get("realized_volatility_20d")) or 0.0
    price_range = _float(volatility.get("price_range_20d")) or 0.0
    gap = abs(_float(trend.get("gap_up_down")) or 0.0)
    rs_score = _float(rel.get("relative_strength_trend")) or 50.0
    confluence_score = _float(confluence.get("stock_confluence_score")) or 0.0
    news_status = str(data_quality.get("company_news") or "missing")
    earnings_status = str(data_quality.get("earnings") or "missing")
    primary_probability = _float(primary.get("probability")) or 0.0
    failed_probability = _scenario_probability(ranking, "stock_failed_bounce")
    downside_probability = _scenario_probability(ranking, "stock_downside_continuation")
    event_probability = _scenario_probability(ranking, "stock_event_risk")

    elasticity_score = _clamp(atr_pct * 900 + realized_vol * 25 + price_range * 120 + abs(volume_z) * 8 + gap * 450, 0, 100)
    volume_anomaly_score = _clamp(45 + volume_z * 14 + volume_vs_20d * 22, 0, 100)
    relative_strength_score = _clamp(rs_score + (_float(rel.get("stock_vs_benchmark_20d")) or 0) * 180, 0, 100)
    squeeze_proxy_score = _clamp(elasticity_score * 0.35 + volume_anomaly_score * 0.30 + max(55 - rs_score, 0) * 0.55 + abs(_float(trend.get("drawdown_20d")) or 0) * 90, 0, 100)
    catalyst_score = _catalyst_score(news_status, earnings_status, event_probability, data_quality)
    market_context = str((payload.get("market_context_for_stock") or {}).get("context") or "neutral")
    sector_context = str((modules.get("sector_context") or {}).get("status") or "missing")
    market_score = _market_context_score(market_context)
    sector_score = _sector_context_score(sector_context)
    risk_score = _risk_score(market_context, failed_probability, downside_probability, elasticity_score, data_quality)
    final_score = (
        elasticity_score * 0.26
        + volume_anomaly_score * 0.17
        + relative_strength_score * 0.15
        + catalyst_score * 0.11
        + confluence_score * 0.15
        + squeeze_proxy_score * 0.06
        + market_score * 0.05
        + sector_score * 0.05
    )
    missing_count = len(data_quality.get("missing_fields") or [])
    final_score -= min(missing_count * 1.0, 8)
    if _float(payload.get("current_price")) is not None and _float(payload.get("current_price")) < 2:
        final_score -= 15
    final_score = _clamp(final_score, 0, 100)
    candidate_type = _candidate_type(primary, final_score, elasticity_score, catalyst_score, squeeze_proxy_score, risk_score, trend, volume)
    expected_range = {
        "low": _round_price(one_day.get("lower_confidence_price")),
        "mid": _round_price(one_day.get("expected_price")),
        "high": _round_price(one_day.get("upper_confidence_price")),
        "range_pct": _round(_safe_div((_float(one_day.get("upper_confidence_price")) or 0) - (_float(one_day.get("lower_confidence_price")) or 0), _float(payload.get("current_price")) or 0)),
    }
    upside_trigger = _level_price(levels, "breakout_level") or _level_price(levels, "primary_confirmation_level")
    invalidation = _level_price(levels, "primary_invalidation_level") or _level_price(levels, "breakdown_level")
    downside_risk = _level_price(levels, "risk_scenario_activation_level") or _level_price(levels, "breakdown_level")
    support = list(confluence.get("supporting_evidence") or [])
    conflict = list(confluence.get("conflicting_evidence") or [])
    return {
        "rank": None,
        "ticker": symbol,
        "company_name": payload.get("company_name") or symbol,
        "logo": payload.get("logo"),
        "last_close": payload.get("current_price"),
        "forecast_date": payload.get("as_of"),
        "as_of": payload.get("as_of"),
        "model_version": payload.get("model_version") or STOCK_MODEL_VERSION,
        "data_status": payload.get("data_status"),
        "candidate_type": candidate_type,
        "radar_level": _radar_level(final_score, risk_score),
        "final_radar_score": round(final_score, 2),
        "elasticity_score": round(elasticity_score, 2),
        "next_day_move_probability": _round(_clamp((elasticity_score * 0.55 + volume_anomaly_score * 0.25 + catalyst_score * 0.20) / 100, 0, 1)),
        "confluence_score": round(confluence_score, 2),
        "catalyst_score": round(catalyst_score, 2),
        "volume_anomaly_score": round(volume_anomaly_score, 2),
        "relative_strength_score": round(relative_strength_score, 2),
        "squeeze_proxy_score": round(squeeze_proxy_score, 2),
        "risk_score": round(risk_score, 2),
        "market_context": market_context,
        "sector_context": sector_context,
        "primary_scenario": primary.get("scenario"),
        "primary_probability": primary_probability,
        "secondary_scenario": secondary.get("scenario"),
        "risk_scenario": risk.get("scenario"),
        "expected_next_day_range": expected_range,
        "expected_next_day_low": expected_range["low"],
        "expected_next_day_mid": expected_range["mid"],
        "expected_next_day_high": expected_range["high"],
        "upside_trigger_level": upside_trigger,
        "downside_risk_level": downside_risk,
        "invalidation_level": invalidation,
        "one_line_reason": _one_line_reason(candidate_type, elasticity_score, volume_anomaly_score, relative_strength_score, catalyst_score, market_context, sector_context),
        "main_supporting_evidence": support[:4],
        "main_conflicting_evidence": conflict[:4],
        "validation_status": "not_yet_validated",
        "data_quality": data_quality.get("score"),
        "data_missing": data_quality.get("missing_fields") or [],
        "news_fields": {
            "company_news": news_status,
            "earnings": earnings_status,
            "catalyst_note": "real company news/earnings unavailable; catalyst score capped" if catalyst_score <= 40 else "catalyst data present or event risk proxy elevated",
        },
        "volume_fields": {
            "volume_z_score": _round(volume_z),
            "relative_volume_5d": None,
            "relative_volume_20d": _round(volume_vs_20d),
            "abnormal_volume_flag": bool(volume_z >= 1.5 or volume_vs_20d >= 0.5),
        },
        "relative_strength_fields": {
            "stock_vs_SPY_20d": rel.get("stock_vs_spy_20d"),
            "stock_vs_QQQ_20d": rel.get("stock_vs_qqq_20d"),
            "stock_vs_benchmark_20d": rel.get("stock_vs_benchmark_20d"),
            "stock_vs_sector_20d": rel.get("stock_vs_sector_20d"),
            "relative_strength_rank": round(relative_strength_score, 2),
        },
    }


def _command_center(candidates: list[dict[str, Any]], stock_dashboard: dict[str, Any]) -> dict[str, Any]:
    top = candidates[0] if candidates else {}
    top3 = [item.get("ticker") for item in candidates[:3]]
    high_count = sum(1 for item in candidates if item.get("radar_level") in {"HIGH_ELASTICITY", "HIGH_RISK_HIGH_VOLATILITY"})
    market_contexts = [str(item.get("market_context")) for item in candidates[:10]]
    risk_off_count = sum(1 for item in market_contexts if item in {"risk_off_pressure", "market_headwind"})
    if high_count >= 3:
        status = "HIGH_ELASTICITY_WATCH"
    elif candidates and (_float(top.get("final_radar_score")) or 0) >= 55:
        status = "MODERATE_OPPORTUNITY"
    else:
        status = "NO_STRONG_RADAR_EDGE"
    return {
        "radar_status": status,
        "top_candidate": top.get("ticker"),
        "top3_candidates": top3,
        "top10_count": min(len(candidates), 10),
        "market_context_note": "market risk pressure is high for many candidates" if risk_off_count >= 4 else "market context is mixed or supportive for selected candidates",
        "data_freshness_note": f"as_of={stock_dashboard.get('as_of')}",
        "validation_status": "not_yet_validated",
        "risk_note": "High elasticity means larger forecast movement potential, not a buy/sell recommendation.",
    }


def _catalyst_score(news_status: str, earnings_status: str, event_probability: float, data_quality: dict[str, Any]) -> float:
    if news_status == "available" or earnings_status == "available":
        return _clamp(55 + event_probability * 60, 0, 100)
    if news_status in {"stale_cache", "partial"} or earnings_status in {"partial", "proxy"}:
        return _clamp(42 + event_probability * 45, 0, 70)
    return _clamp(22 + event_probability * 35 - len(data_quality.get("missing_fields") or []) * 0.8, 0, 40)


def _risk_score(market_context: str, failed_probability: float, downside_probability: float, elasticity_score: float, data_quality: dict[str, Any]) -> float:
    risk = failed_probability * 50 + downside_probability * 42 + elasticity_score * 0.22
    if market_context in {"risk_off_pressure", "market_headwind"}:
        risk += 14
    risk += min(len(data_quality.get("missing_fields") or []) * 1.2, 10)
    return _clamp(risk, 0, 100)


def _candidate_type(
    primary: dict[str, Any],
    final_score: float,
    elasticity_score: float,
    catalyst_score: float,
    squeeze_proxy_score: float,
    risk_score: float,
    trend: dict[str, Any],
    volume: dict[str, Any],
) -> str:
    scenario = str(primary.get("scenario") or "")
    if final_score < 32:
        return "no_edge"
    if scenario == "stock_downside_continuation":
        return "downside_continuation"
    if scenario == "stock_failed_bounce":
        return "failed_bounce_risk"
    if catalyst_score >= 55:
        return "event_driven_move"
    if squeeze_proxy_score >= 68:
        return "short_squeeze_proxy"
    if abs(_float(trend.get("gap_up_down")) or 0) >= 0.025 and (_float(volume.get("volume_z_score")) or 0) >= 1:
        return "gap_continuation"
    if scenario == "stock_bounce":
        return "oversold_bounce"
    if scenario == "stock_trend_repair":
        return "upside_momentum"
    if elasticity_score >= 65 or risk_score >= 70:
        return "high_volatility_watch"
    return "no_edge"


def _one_line_reason(
    candidate_type: str,
    elasticity_score: float,
    volume_score: float,
    rs_score: float,
    catalyst_score: float,
    market_context: str,
    sector_context: str,
) -> str:
    parts = [f"弹性 {elasticity_score:.0f}", f"成交量 {volume_score:.0f}", f"相对强弱 {rs_score:.0f}"]
    if catalyst_score >= 50:
        parts.append(f"催化 {catalyst_score:.0f}")
    else:
        parts.append("新闻/财报催化不足")
    parts.append(f"大盘 {market_context}")
    parts.append(f"板块 {sector_context}")
    return f"{candidate_type}: " + " / ".join(parts)


def _market_context_score(context: str) -> float:
    return {
        "market_tailwind": 76,
        "supportive": 68,
        "neutral": 52,
        "market_headwind": 34,
        "risk_off_pressure": 26,
    }.get(context, 45)


def _sector_context_score(status: str) -> float:
    return {
        "supportive": 72,
        "neutral": 52,
        "proxy": 45,
        "missing": 35,
        "conflicting": 28,
    }.get(status, 45)


def _radar_level(final_score: float, risk_score: float) -> str:
    if final_score >= 72 and risk_score >= 70:
        return "HIGH_RISK_HIGH_VOLATILITY"
    if final_score >= 68:
        return "HIGH_ELASTICITY"
    if final_score >= 52:
        return "MODERATE_OPPORTUNITY"
    if final_score >= 35:
        return "WATCH"
    return "NO_EDGE"


def _performance(records: list[dict[str, Any]]) -> dict[str, Any]:
    returns = [_actual_next_day_return(record) for record in records]
    returns = [value for value in returns if value is not None]
    ranges = [_actual_next_day_range(record) for record in records]
    ranges = [value for value in ranges if value is not None]
    primary_hits = [_bool(record.get("primary_hit")) for record in records]
    range_hits = [_bool(record.get("range_hit")) for record in records]
    return {
        "sample_size": len(records),
        "completed_return_samples": len(returns),
        "avg_next_day_return": _mean(returns),
        "avg_abs_next_day_return": _mean([abs(value) for value in returns]),
        "avg_next_day_high_low_range": _mean(ranges),
        "primary_hit_rate": _rate(primary_hits),
        "range_hit_rate": _rate(range_hits),
        "failure_rate": _rate([None if value is None else value < 0 for value in returns]),
    }


def _comparison_answer(group_a: list[dict[str, Any]], group_b: list[dict[str, Any]], metric: str) -> str:
    if len(group_a) < 5 or len(group_b) < 5:
        return "not_enough_forward_samples"
    a = _performance(group_a).get(metric)
    b = _performance(group_b).get(metric)
    if a is None or b is None:
        return "not_enough_forward_samples"
    if a > b:
        return "yes_preliminary"
    if a < b:
        return "no_preliminary"
    return "mixed"


def _top_percentile(records: list[dict[str, Any]], field: str, pct: float) -> list[dict[str, Any]]:
    valid = [record for record in records if _float(record.get(field)) is not None]
    valid.sort(key=lambda item: _float(item.get(field)) or 0.0, reverse=True)
    if not valid:
        return []
    return valid[: max(1, int(len(valid) * pct))]


def _bottom_percentile(records: list[dict[str, Any]], field: str, pct: float) -> list[dict[str, Any]]:
    valid = [record for record in records if _float(record.get(field)) is not None]
    valid.sort(key=lambda item: _float(item.get(field)) or 0.0)
    if not valid:
        return []
    return valid[: max(1, int(len(valid) * pct))]


def _actual_next_day_return(record: dict[str, Any]) -> float | None:
    return _float(record.get("actual_next_day_return") or record.get("actual_1d_return") or record.get("actual_return_1d"))


def _actual_next_day_range(record: dict[str, Any]) -> float | None:
    value = _float(record.get("actual_next_day_high_low_range"))
    return value


def _scenario_probability(ranking: dict[str, Any], scenario: str) -> float:
    for item in ranking.get("all_scenarios") or []:
        if item.get("scenario") == scenario:
            return _float(item.get("probability")) or 0.0
    return 0.0


def _level_price(levels: dict[str, Any], key: str) -> float | None:
    return _round_price((levels.get(key) or {}).get("price"))


def _read_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _forecast_id(forecast_date: str, model_version: str, symbol: str) -> str:
    return hashlib.sha256(f"{forecast_date}|{model_version}|{symbol}".encode("utf-8")).hexdigest()[:20]


def _evidence_level(samples: int) -> str:
    if samples < 20:
        return "insufficient_samples"
    if samples < 50:
        return "early_evidence"
    if samples < 100:
        return "moderate_evidence"
    return "stronger_evidence"


def _mean(values: list[float]) -> float | None:
    if not values:
        return None
    return round(sum(values) / len(values), 6)


def _rate(values: list[bool | None]) -> float | None:
    valid = [value for value in values if value is not None]
    if not valid:
        return None
    return round(sum(1 for value in valid if value) / len(valid), 4)


def _truthy(value: Any) -> bool:
    return value in (True, "true", "True", "1", 1)


def _bool(value: Any) -> bool | None:
    if value in (True, "true", "True", "1", 1):
        return True
    if value in (False, "false", "False", "0", 0):
        return False
    return None


def _float(value: Any) -> float | None:
    try:
        if value in (None, ""):
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def _safe_div(numerator: float, denominator: float) -> float | None:
    if not denominator:
        return None
    return numerator / denominator


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _round(value: Any, digits: int = 4) -> float | None:
    number = _float(value)
    if number is None:
        return None
    return round(number, digits)


def _round_price(value: Any) -> float | None:
    number = _float(value)
    if number is None:
        return None
    return round(number, 2)
