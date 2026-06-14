from __future__ import annotations

import copy
import json
import math
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BACKEND_ROOT = PROJECT_ROOT / "backend"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.services.analysis.historical_analogs import build_alpha_v1_analog_report
from app.services.data_providers.auto_download import DownloadedSeries
from app.services.data_providers.auto_download import refresh_market_data
from app.services.validation.forward_alpha_tracker import alpha_status_payload, report_payload
from scripts.market_intelligence_v2 import build_market_intelligence_v2
from scripts.market_intelligence_v3 import (
    V3_MARKET_SYMBOLS,
    build_market_intelligence_v3,
    render_high_confidence_signal_report_markdown,
)
from scripts.market_intelligence_v4 import (
    build_market_intelligence_v4,
    render_high_confidence_edge_report_markdown,
)
from scripts.providers.finnhub_provider import fetch_finnhub_bundle
from scripts.providers.fred_provider import DEFAULT_FRED_SERIES, fetch_fred_bundle
from scripts.providers.breadth_provider import fetch_breadth_bundle, render_breadth_status_markdown


SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
SYMBOL_NAMES = {
    "SPY": "S&P 500",
    "QQQ": "Nasdaq 100",
    "IWM": "Russell 2000",
    "DIA": "Dow Jones",
}
SUPPORT_SYMBOLS = ("^VIX", "HYG", "LQD", "TLT", "UUP", "^TNX")
HORIZONS = (3, 5, 10, 20, 60)
PAST_WINDOW = 90


def main() -> int:
    public_dir = PROJECT_ROOT / "frontend" / "public"
    public_dir.mkdir(parents=True, exist_ok=True)

    alpha_status = alpha_status_payload()
    alpha_report = report_payload()
    analogs = {symbol: build_alpha_v1_analog_report(symbol, top_k=20) for symbol in SYMBOLS}
    market_symbols = tuple(dict.fromkeys(SYMBOLS + SUPPORT_SYMBOLS + V3_MARKET_SYMBOLS))
    downloaded = refresh_market_data(symbols=market_symbols, lookback_days=520)
    series_by_symbol = {series.symbol: series for series in downloaded}
    finnhub_bundle = fetch_finnhub_bundle(symbols=SYMBOLS, lookback_days=520)
    fred_bundle = fetch_fred_bundle(lookback_days=1800)
    _print_fred_diagnostics(fred_bundle)
    breadth_bundle = fetch_breadth_bundle(series_by_symbol=series_by_symbol, lookback_days=420)
    _print_breadth_diagnostics(breadth_bundle)
    price_history = _load_price_history(series_by_symbol)

    market_overview = _build_market_overview(alpha_status, analogs, price_history)
    simulated_paths = _build_simulated_paths(alpha_status, analogs, price_history, market_overview)
    baseline_overview = copy.deepcopy(market_overview)
    baseline_paths = copy.deepcopy(simulated_paths)
    no_fred_bundle = _empty_fred_bundle()
    baseline_v2 = build_market_intelligence_v2(
        series_by_symbol=series_by_symbol,
        overview=baseline_overview,
        simulated_paths=baseline_paths,
        analogs=analogs,
    )
    baseline_v3 = build_market_intelligence_v3(
        series_by_symbol=series_by_symbol,
        overview=baseline_overview,
        simulated_paths=baseline_paths,
        analogs=analogs,
        prior_intelligence=baseline_v2,
        finnhub_bundle=finnhub_bundle,
        fred_bundle=no_fred_bundle,
        breadth_bundle=breadth_bundle,
    )
    baseline_v4 = build_market_intelligence_v4(
        series_by_symbol=series_by_symbol,
        overview=baseline_overview,
        simulated_paths=baseline_paths,
        analogs=analogs,
        prior_intelligence=baseline_v3,
        finnhub_bundle=finnhub_bundle,
        fred_bundle=no_fred_bundle,
    )
    intelligence_v2 = build_market_intelligence_v2(
        series_by_symbol=series_by_symbol,
        overview=market_overview,
        simulated_paths=simulated_paths,
        analogs=analogs,
    )
    intelligence_v3 = build_market_intelligence_v3(
        series_by_symbol=series_by_symbol,
        overview=market_overview,
        simulated_paths=simulated_paths,
        analogs=analogs,
        prior_intelligence=intelligence_v2,
        finnhub_bundle=finnhub_bundle,
        fred_bundle=fred_bundle,
        breadth_bundle=breadth_bundle,
    )
    intelligence_v4 = build_market_intelligence_v4(
        series_by_symbol=series_by_symbol,
        overview=market_overview,
        simulated_paths=simulated_paths,
        analogs=analogs,
        prior_intelligence=intelligence_v3,
        finnhub_bundle=finnhub_bundle,
        fred_bundle=fred_bundle,
    )
    fred_effect_summary = _fred_effect_summary(baseline_v4, intelligence_v4, baseline_paths, simulated_paths)
    intelligence_v4["fred_effect_summary"] = fred_effect_summary
    intelligence_v4["data_quality_report"]["summary"]["fred_effect_summary"] = fred_effect_summary
    dashboard = {
        "generated_by": "scripts/export_static_alpha_v1.py",
        "source": "github_actions_forward_tracker_outputs",
        "as_of": _latest_as_of(alpha_status, analogs),
        "status_note": "Alpha v1 remains a research candidate. Simulated paths are probabilistic scenarios, not guaranteed forecasts.",
        "overview": market_overview,
        "simulated_paths": simulated_paths,
        "market_intelligence_v2": intelligence_v2,
        "market_intelligence_v3": intelligence_v3,
        "market_intelligence_v4": intelligence_v4,
        "data_quality_report": intelligence_v4["data_quality_report"],
        "breadth_status": breadth_bundle,
        "feature_snapshot_v2": intelligence_v2["feature_snapshot_v2"],
        "feature_snapshot_v3": intelligence_v3["feature_snapshot_v3"],
        "model_confidence_by_symbol": intelligence_v4["model_confidence_by_symbol"],
        "high_confidence_signal_report": intelligence_v3["high_confidence_signal_report"],
        "high_confidence_edge_report": intelligence_v4["high_confidence_edge_report"],
        "alpha_status": alpha_status,
        "forward_report": alpha_report,
        "analogs": analogs,
    }

    _write_json(public_dir / "alpha-v1-status.json", {
        "generated_by": "scripts/export_static_alpha_v1.py",
        "source": "github_actions_forward_tracker_outputs",
        "alpha_status": alpha_status,
        "forward_report": alpha_report,
    })
    _write_json(public_dir / "alpha-v1-analogs.json", {
        "generated_by": "scripts/export_static_alpha_v1.py",
        "source": "github_actions_forward_tracker_outputs",
        "analogs": analogs,
    })
    _write_json(public_dir / "data_quality_report.json", intelligence_v4["data_quality_report"])
    _write_json(public_dir / "breadth-status.json", breadth_bundle)
    _write_json(public_dir / "high-confidence-signal-report.json", intelligence_v3["high_confidence_signal_report"])
    _write_json(public_dir / "high-confidence-edge-report.json", intelligence_v4["high_confidence_edge_report"])
    _write_json(public_dir / "market-overview.json", market_overview)
    _write_json(public_dir / "simulated-paths.json", simulated_paths)
    _write_json(public_dir / "prediction-dashboard.json", dashboard)
    _write_report(PROJECT_ROOT / "outputs" / "high_confidence_signal_report.md", intelligence_v3["high_confidence_signal_report"])
    _write_edge_report(PROJECT_ROOT / "outputs" / "high_confidence_edge_report.md", intelligence_v4["high_confidence_edge_report"])
    _write_fred_status_report(PROJECT_ROOT / "outputs" / "fred_data_status.md", fred_bundle, fred_effect_summary, intelligence_v4)
    _write_breadth_status_report(PROJECT_ROOT / "outputs" / "breadth_data_status.md", breadth_bundle)

    print("wrote frontend/public/alpha-v1-status.json")
    print("wrote frontend/public/alpha-v1-analogs.json")
    print("wrote frontend/public/data_quality_report.json")
    print("wrote frontend/public/breadth-status.json")
    print("wrote frontend/public/high-confidence-signal-report.json")
    print("wrote frontend/public/high-confidence-edge-report.json")
    print("wrote frontend/public/market-overview.json")
    print("wrote frontend/public/simulated-paths.json")
    print("wrote frontend/public/prediction-dashboard.json")
    print("wrote outputs/high_confidence_signal_report.md")
    print("wrote outputs/high_confidence_edge_report.md")
    print("wrote outputs/fred_data_status.md")
    print("wrote outputs/breadth_data_status.md")
    return 0


def _print_fred_diagnostics(bundle: dict[str, Any]) -> None:
    print(f"FRED_API_KEY_PRESENT={str(bool(os.getenv('FRED_API_KEY', '').strip())).lower()}")
    print(f"FRED_PROVIDER_AVAILABLE={str(bool(bundle.get('available'))).lower()}")
    print(f"FRED_PROVIDER_FALLBACK_USED={str(bool(bundle.get('fallback_used'))).lower()}")
    print(f"FRED_PROVIDER_RATE_LIMITED={str(bool(bundle.get('rate_limited'))).lower()}")
    for name in sorted((bundle.get("series") or {}).keys()):
        payload = bundle["series"][name]
        success = bool(payload.get("real_data"))
        print(
            "FRED_SERIES "
            f"name={name} "
            f"series_id={payload.get('series_id')} "
            f"success={str(success).lower()} "
            f"latest_date={payload.get('latest_date') or 'NA'} "
            f"latest_value={payload.get('latest_value') if payload.get('latest_value') is not None else 'NA'} "
            f"source={payload.get('source') or 'NA'} "
            f"stale={str(bool(payload.get('stale_data'))).lower()} "
            f"error_type={payload.get('error_type') or 'NA'} "
            f"error_reason={payload.get('error_reason') or 'NA'}"
        )


def _print_breadth_diagnostics(bundle: dict[str, Any]) -> None:
    summary = bundle.get("summary") or {}
    print(f"BREADTH_PROVIDER_AVAILABLE={str(bool(summary.get('provider_available'))).lower()}")
    print(f"BREADTH_TRUE_AVAILABLE={str(bool(summary.get('true_breadth_available'))).lower()}")
    print(f"BREADTH_AVERAGE_QUALITY={summary.get('average_breadth_quality_score')}")
    print(f"BREADTH_STALE_DATA={str(bool(summary.get('stale_data'))).lower()}")
    for symbol, payload in sorted((bundle.get("universes") or {}).items()):
        scores = payload.get("scores") or {}
        print(
            "BREADTH_UNIVERSE "
            f"symbol={symbol} "
            f"status={payload.get('status') or 'missing'} "
            f"true_breadth={str(bool(payload.get('is_true_breadth'))).lower()} "
            f"proxy={str(bool(payload.get('is_proxy'))).lower()} "
            f"latest_date={payload.get('latest_date') or 'NA'} "
            f"used={payload.get('constituents_used') if payload.get('constituents_used') is not None else 'NA'} "
            f"expected={payload.get('constituents_expected') if payload.get('constituents_expected') is not None else 'NA'} "
            f"coverage={payload.get('coverage_ratio') if payload.get('coverage_ratio') is not None else 'NA'} "
            f"stale_constituents={str(bool(payload.get('stale_constituents'))).lower()} "
            f"stale_price_data={str(bool(payload.get('stale_price_data'))).lower()} "
            f"improvement={scores.get('breadth_improvement_score') if scores.get('breadth_improvement_score') is not None else 'NA'} "
            f"conflict={scores.get('breadth_conflict_score') if scores.get('breadth_conflict_score') is not None else 'NA'} "
            f"quality={scores.get('breadth_quality_score') if scores.get('breadth_quality_score') is not None else 'NA'}"
        )


def _empty_fred_bundle() -> dict[str, Any]:
    return {
        "provider": "fred",
        "configured": bool(os.getenv("FRED_API_KEY", "").strip()),
        "api_key_present": bool(os.getenv("FRED_API_KEY", "").strip()),
        "available": False,
        "missing": True,
        "rate_limited": False,
        "fallback_used": False,
        "cache_used": False,
        "successful_series": [],
        "failed_series": list(DEFAULT_FRED_SERIES.keys()),
        "series": {
            name: {
                "name": name,
                "series_id": series_id,
                "rows": [],
                "row_count": 0,
                "latest_date": None,
                "latest_value": None,
                "source": "disabled_baseline",
                "status": "missing",
                "real_data": False,
                "fallback_used": False,
                "stale_data": True,
                "missing_data": True,
                "error_reason": "baseline_without_fred",
            }
            for name, series_id in DEFAULT_FRED_SERIES.items()
        },
        "derived": {},
    }


def _fred_effect_summary(
    without_fred: dict[str, Any],
    with_fred: dict[str, Any],
    paths_without_fred: dict[str, Any],
    paths_with_fred: dict[str, Any],
) -> dict[str, Any]:
    before_quality = without_fred.get("data_quality_report", {}).get("summary", {})
    after_quality = with_fred.get("data_quality_report", {}).get("summary", {})
    symbols: dict[str, Any] = {}
    for symbol in SYMBOLS:
        before_edge = without_fred.get("edge_status_by_symbol", {}).get(symbol, {})
        after_edge = with_fred.get("edge_status_by_symbol", {}).get(symbol, {})
        before_predictors = without_fred.get("predictor_outputs_by_symbol", {}).get(symbol, {})
        after_predictors = with_fred.get("predictor_outputs_by_symbol", {}).get(symbol, {})
        before_rank = paths_without_fred.get("symbols", {}).get(symbol, {}).get("scenario_ranking", {})
        after_rank = paths_with_fred.get("symbols", {}).get(symbol, {}).get("scenario_ranking", {})
        before_risk = float((before_predictors.get("risk_expansion_predictor") or {}).get("probability") or 0.0)
        after_risk = float((after_predictors.get("risk_expansion_predictor") or {}).get("probability") or 0.0)
        before_downside = float((before_predictors.get("downside_continuation_predictor") or {}).get("probability") or 0.0)
        after_downside = float((after_predictors.get("downside_continuation_predictor") or {}).get("probability") or 0.0)
        symbols[symbol] = {
            "edge_status_without_fred": before_edge.get("market_edge_status"),
            "edge_status_with_fred": after_edge.get("market_edge_status"),
            "edge_status_changed": before_edge.get("market_edge_status") != after_edge.get("market_edge_status"),
            "primary_scenario_without_fred": before_rank.get("primary_scenario"),
            "primary_scenario_with_fred": after_rank.get("primary_scenario"),
            "primary_scenario_changed": before_rank.get("primary_scenario") != after_rank.get("primary_scenario"),
            "risk_expansion_without_fred": round(before_risk, 4),
            "risk_expansion_with_fred": round(after_risk, 4),
            "risk_expansion_delta": round(after_risk - before_risk, 4),
            "failed_bounce_without_fred": round(before_downside, 4),
            "failed_bounce_with_fred": round(after_downside, 4),
            "failed_bounce_delta": round(after_downside - before_downside, 4),
        }
    return {
        "data_completeness_without_fred": before_quality.get("data_completeness_score"),
        "data_completeness_with_fred": after_quality.get("data_completeness_score"),
        "data_completeness_delta": (after_quality.get("data_completeness_score") or 0) - (before_quality.get("data_completeness_score") or 0),
        "target_85_met_with_fred": bool(after_quality.get("v4_target_met")),
        "symbols": symbols,
        "note": "This compares the current run against the same run with FRED disabled. It does not change Alpha v1.",
    }


def _write_fred_status_report(path: Path, bundle: dict[str, Any], effect_summary: dict[str, Any], intelligence_v4: dict[str, Any]) -> None:
    quality = intelligence_v4.get("data_quality_report", {}).get("summary", {})
    lines = [
        "# FRED Data Status",
        "",
        f"Generated at: `{datetime.utcnow().isoformat()}Z`",
        "",
        "## Provider",
        "",
        f"- FRED_API_KEY present: `{bool(os.getenv('FRED_API_KEY', '').strip())}`",
        f"- provider available: `{bool(bundle.get('available'))}`",
        f"- fallback used: `{bool(bundle.get('fallback_used'))}`",
        f"- rate limited: `{bool(bundle.get('rate_limited'))}`",
        f"- successful series: `{', '.join(bundle.get('successful_series') or []) or 'none'}`",
        f"- failed series: `{', '.join(bundle.get('failed_series') or []) or 'none'}`",
        "",
        "## Series",
        "",
        "| name | series_id | success | latest_date | latest_value | source | stale | error |",
        "|---|---|---:|---|---:|---|---:|---|",
    ]
    for name in sorted((bundle.get("series") or {}).keys()):
        payload = bundle["series"][name]
        error = payload.get("error_reason") or payload.get("error_type") or ""
        lines.append(
            "| "
            + " | ".join(
                [
                    str(name),
                    str(payload.get("series_id") or ""),
                    str(bool(payload.get("real_data"))),
                    str(payload.get("latest_date") or ""),
                    str(payload.get("latest_value") if payload.get("latest_value") is not None else ""),
                    str(payload.get("source") or ""),
                    str(bool(payload.get("stale_data"))),
                    str(error),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Data Completeness Effect",
            "",
            f"- without FRED: `{effect_summary.get('data_completeness_without_fred')}`",
            f"- with current FRED status: `{effect_summary.get('data_completeness_with_fred')}`",
            f"- delta: `{effect_summary.get('data_completeness_delta')}`",
            f"- target 85 met: `{effect_summary.get('target_85_met_with_fred')}`",
            f"- current report score: `{quality.get('data_completeness_score')}`",
            "",
            "## Risk Expansion / Failed Bounce Effect",
            "",
            "| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |",
            "|---|---|---|---|---|---:|---:|",
        ]
    )
    for symbol in SYMBOLS:
        row = effect_summary.get("symbols", {}).get(symbol, {})
        lines.append(
            "| "
            + " | ".join(
                [
                    symbol,
                    str(row.get("edge_status_without_fred")),
                    str(row.get("edge_status_with_fred")),
                    str(row.get("primary_scenario_without_fred")),
                    str(row.get("primary_scenario_with_fred")),
                    str(row.get("risk_expansion_delta")),
                    str(row.get("failed_bounce_delta")),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Warning",
            "",
            "If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_breadth_status_report(path: Path, bundle: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_breadth_status_markdown(bundle), encoding="utf-8")


def _load_price_history(series_by_symbol: dict[str, DownloadedSeries] | None = None) -> dict[str, list[dict[str, Any]]]:
    downloaded = (
        [series_by_symbol[symbol] for symbol in SYMBOLS if symbol in series_by_symbol]
        if series_by_symbol is not None
        else refresh_market_data(symbols=SYMBOLS, lookback_days=220)
    )
    history: dict[str, list[dict[str, Any]]] = {}
    for series in downloaded:
        clean_rows = [
            {
                "date": str(row["date"]),
                "close": float(row["close"]),
                "source": series.source,
            }
            for row in series.rows
            if row.get("date") and float(row.get("close") or 0.0) > 0
        ]
        history[series.symbol] = clean_rows[-PAST_WINDOW:]
    return history


def _build_market_overview(
    alpha_status: dict[str, Any],
    analogs: dict[str, dict[str, Any]],
    price_history: dict[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    symbols: dict[str, Any] = {}
    latest_bounce = alpha_status.get("latest_bounce_probability_by_symbol", {})
    distance = alpha_status.get("distance_to_threshold_by_symbol", {})
    live_symbols = {item.get("symbol") for item in alpha_status.get("live_signals", [])}
    for symbol in SYMBOLS:
        analog = analogs.get(symbol, {})
        distribution = analog.get("historical_distribution", {})
        bounce_probability = _float_or_none(latest_bounce.get(symbol))
        if bounce_probability is None:
            bounce_probability = _float_or_none(analog.get("current_bounce_probability")) or 0.0
        live_signal = symbol in live_symbols or bool(analog.get("current_alpha_v1_triggered"))
        historical_support = analog.get("interpretation", {}).get("historical_support", "neutral")
        downside = _downside_continuation_probability(distribution)
        reversal = _trend_reversal_probability(distribution)
        current_price = _current_price(symbol, alpha_status, price_history)
        state = _market_state(live_signal, bounce_probability, historical_support, downside, analog.get("current_regime"))
        symbols[symbol] = {
            "symbol": symbol,
            "name": SYMBOL_NAMES[symbol],
            "current_price": current_price,
            "market_state": state,
            "bounce_probability": bounce_probability,
            "downside_continuation_probability": downside,
            "trend_reversal_probability": reversal,
            "historical_support": historical_support,
            "live_signal": live_signal,
            "distance_to_threshold": _float_or_none(distance.get(symbol)),
            "as_of": analog.get("as_of") or alpha_status.get("latest_checked_date"),
            "data_source_status": alpha_status.get("data_source_status") or analog.get("data_source_status"),
        }
    strongest = max(symbols.values(), key=lambda item: item["bounce_probability"])
    return {
        "as_of": alpha_status.get("latest_checked_date") or _latest_as_of(alpha_status, analogs),
        "symbols": symbols,
        "strongest_symbol": strongest["symbol"],
        "dashboard_status": "forward_only_observation",
        "status_note": "Alpha v1 is still a research candidate. No auto-trading is enabled.",
    }


def _build_simulated_paths(
    alpha_status: dict[str, Any],
    analogs: dict[str, dict[str, Any]],
    price_history: dict[str, list[dict[str, Any]]],
    overview: dict[str, Any],
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "as_of": overview.get("as_of"),
        "disclaimer": "Simulated future paths are probabilistic scenarios based on current signals and historical analogs, not guaranteed forecasts.",
        "symbols": {},
    }
    for symbol in SYMBOLS:
        rows = price_history.get(symbol, [])
        if not rows:
            continue
        current_price = overview["symbols"][symbol]["current_price"] or rows[-1]["close"]
        cases = analogs.get(symbol, {}).get("top_similar_cases", [])
        horizon_returns = _scenario_returns(cases)
        past_dates = [row["date"] for row in rows]
        past_prices = [row["close"] for row in rows]
        future_dates = _future_business_dates(rows[-1]["date"], max(HORIZONS))
        chart_dates = past_dates + future_dates[1:]

        analog_average = _path_from_horizon_returns(current_price, horizon_returns["average"])
        bounce_path = _path_from_horizon_returns(current_price, horizon_returns["best_quartile"])
        bearish_path = _path_from_horizon_returns(current_price, horizon_returns["worst_quartile"])
        expected_path = _expected_path(current_price, horizon_returns, overview["symbols"][symbol])
        confidence_upper = [max(values) for values in zip(bounce_path, analog_average, expected_path)]
        confidence_lower = [min(values) for values in zip(bearish_path, analog_average, expected_path)]

        payload["symbols"][symbol] = {
            "symbol": symbol,
            "name": SYMBOL_NAMES[symbol],
            "current_price": current_price,
            "market_state": overview["symbols"][symbol]["market_state"],
            "live_signal": overview["symbols"][symbol]["live_signal"],
            "bounce_probability": overview["symbols"][symbol]["bounce_probability"],
            "downside_continuation_probability": overview["symbols"][symbol]["downside_continuation_probability"],
            "trend_reversal_probability": overview["symbols"][symbol]["trend_reversal_probability"],
            "historical_support": overview["symbols"][symbol]["historical_support"],
            "paths": {
                "dates": chart_dates,
                "split_index": len(past_dates) - 1,
                "historical_price": past_prices + [None for _ in future_dates[1:]],
                "expected_path": [None for _ in past_dates[:-1]] + expected_path,
                "bounce_path": [None for _ in past_dates[:-1]] + bounce_path,
                "bearish_path": [None for _ in past_dates[:-1]] + bearish_path,
                "analog_average_path": [None for _ in past_dates[:-1]] + analog_average,
                "confidence_band_upper": [None for _ in past_dates[:-1]] + confidence_upper,
                "confidence_band_lower": [None for _ in past_dates[:-1]] + confidence_lower,
            },
            "horizon_summary": _horizon_summary(horizon_returns, overview["symbols"][symbol]),
            "scenario_cards": _scenario_cards(horizon_returns, overview["symbols"][symbol]),
            "risk_invalidation_conditions": _risk_invalidation_conditions(overview["symbols"][symbol]),
        }
    return payload


def _scenario_returns(cases: list[dict[str, Any]]) -> dict[str, dict[int, float]]:
    if not cases:
        return {
            "average": {horizon: 0.0 for horizon in HORIZONS},
            "best_quartile": {horizon: 0.0 for horizon in HORIZONS},
            "worst_quartile": {horizon: 0.0 for horizon in HORIZONS},
        }
    sorted_cases = sorted(cases, key=lambda case: _float_or_none(case.get("forward_return_20d")) or 0.0)
    quartile = max(1, math.ceil(len(sorted_cases) * 0.25))
    worst = sorted_cases[:quartile]
    best = sorted_cases[-quartile:]
    return {
        "average": {h: _mean([_float_or_none(case.get(f"forward_return_{h}d")) for case in cases]) for h in HORIZONS},
        "best_quartile": {h: _mean([_float_or_none(case.get(f"forward_return_{h}d")) for case in best]) for h in HORIZONS},
        "worst_quartile": {h: _mean([_float_or_none(case.get(f"forward_return_{h}d")) for case in worst]) for h in HORIZONS},
    }


def _path_from_horizon_returns(current_price: float, returns_by_horizon: dict[int, float]) -> list[float]:
    points = {0: 0.0, **returns_by_horizon}
    values: list[float] = []
    sorted_horizons = sorted(points)
    for day in range(0, max(HORIZONS) + 1):
        lower = max(h for h in sorted_horizons if h <= day)
        upper = min(h for h in sorted_horizons if h >= day)
        if lower == upper:
            value = points[lower]
        else:
            weight = (day - lower) / (upper - lower)
            value = points[lower] + (points[upper] - points[lower]) * weight
        values.append(round(current_price * (1 + value), 4))
    return values


def _expected_path(current_price: float, scenario_returns: dict[str, dict[int, float]], overview: dict[str, Any]) -> list[float]:
    bounce_weight = 0.25 + (0.25 if overview["live_signal"] else 0.0) + overview["bounce_probability"] * 0.25
    bearish_weight = 0.20 + overview["downside_continuation_probability"] * 0.30
    if overview["historical_support"] == "supportive":
        bounce_weight += 0.10
    if overview["market_state"] in {"risk_off", "panic"}:
        bearish_weight += 0.15
    base_weight = max(0.10, 1.0 - bounce_weight - bearish_weight)
    total = bounce_weight + bearish_weight + base_weight
    bounce_weight, bearish_weight, base_weight = bounce_weight / total, bearish_weight / total, base_weight / total
    blended = {
        horizon: (
            scenario_returns["best_quartile"][horizon] * bounce_weight
            + scenario_returns["worst_quartile"][horizon] * bearish_weight
            + scenario_returns["average"][horizon] * base_weight
        )
        for horizon in HORIZONS
    }
    return _path_from_horizon_returns(current_price, blended)


def _horizon_summary(scenario_returns: dict[str, dict[int, float]], overview: dict[str, Any]) -> dict[str, Any]:
    summary: dict[str, Any] = {}
    for horizon in HORIZONS:
        expected = scenario_returns["average"][horizon]
        up_probability = _clip(0.45 + overview["bounce_probability"] * 0.35 + max(expected, 0) * 3.0, 0.0, 0.95)
        down_probability = _clip(0.35 + overview["downside_continuation_probability"] * 0.35 + max(-expected, 0) * 3.0, 0.0, 0.95)
        total = up_probability + down_probability
        if total > 1:
            up_probability, down_probability = up_probability / total, down_probability / total
        summary[f"{horizon}d"] = {
            "expected_return": expected,
            "up_probability": up_probability,
            "down_probability": down_probability,
            "risk_note": _risk_note_for_horizon(horizon, overview),
        }
    return summary


def _scenario_cards(scenario_returns: dict[str, dict[int, float]], overview: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "name": "Base case",
            "name_cn": "基准情景",
            "summary_cn": "按最相似历史样本的平均路径推演。",
            "return_20d": scenario_returns["average"][20],
            "probability_weight": _clip(0.45 - overview["downside_continuation_probability"] * 0.15, 0.15, 0.65),
        },
        {
            "name": "Bounce case",
            "name_cn": "反弹情景",
            "summary_cn": "如果 Alpha v1 信号继续有效，路径更接近历史上较好的反抽样本。",
            "return_20d": scenario_returns["best_quartile"][20],
            "probability_weight": _clip(overview["bounce_probability"], 0.05, 0.80),
        },
        {
            "name": "Bearish case",
            "name_cn": "失败反弹情景",
            "summary_cn": "如果波动和信用代理恶化，路径更接近历史上较差的一组样本。",
            "return_20d": scenario_returns["worst_quartile"][20],
            "probability_weight": _clip(overview["downside_continuation_probability"], 0.05, 0.80),
        },
        {
            "name": "Historical analog case",
            "name_cn": "历史相似情景",
            "summary_cn": "只看最相似历史样本后的实际表现，不做确定性预测。",
            "return_20d": scenario_returns["average"][20],
            "probability_weight": 0.50 if overview["historical_support"] == "supportive" else 0.35,
        },
    ]


def _risk_invalidation_conditions(overview: dict[str, Any]) -> list[str]:
    conditions = [
        "VIX 重新快速上升，说明波动压力没有解除。",
        "HYG 明显走弱或信用代理指标恶化。",
        "价格跌破最近低点，反弹候选失效。",
        "历史相似情景支持度从 supportive 转为 weak_or_conflicting。",
    ]
    if overview["market_state"] in {"risk_off", "panic"}:
        conditions.insert(0, "市场状态仍处于 risk_off / panic，反弹更容易失败。")
    return conditions


def _market_state(
    live_signal: bool,
    bounce_probability: float,
    historical_support: str,
    downside_probability: float,
    regime: str | None,
) -> str:
    if regime in {"crisis", "panic", "crisis_mode"}:
        return "panic"
    if downside_probability >= 0.65:
        return "risk_off"
    if live_signal and bounce_probability >= 0.50:
        return "oversold_bounce"
    if live_signal or historical_support == "supportive":
        return "recovery"
    if bounce_probability < 0.25 and historical_support != "supportive":
        return "no_edge"
    return "sideways"


def _downside_continuation_probability(distribution: dict[str, Any]) -> float:
    avg_20d = _float_or_none(distribution.get("avg_return_20d")) or 0.0
    hit_20d = _float_or_none(distribution.get("hit_rate_20d"))
    worst_20d = _float_or_none(distribution.get("worst_case_20d")) or 0.0
    base = 0.45
    base += _clip(-avg_20d * 4.0, 0.0, 0.25)
    base += _clip(-worst_20d * 1.5, 0.0, 0.20)
    if hit_20d is not None:
        base += _clip((0.50 - hit_20d) * 0.50, -0.15, 0.20)
    return _clip(base, 0.05, 0.95)


def _trend_reversal_probability(distribution: dict[str, Any]) -> float:
    avg_20d = _float_or_none(distribution.get("avg_return_20d")) or 0.0
    avg_60d = _float_or_none(distribution.get("avg_return_60d")) or 0.0
    hit_20d = _float_or_none(distribution.get("hit_rate_20d")) or 0.5
    return _clip(0.30 + avg_20d * 3.0 + avg_60d * 1.5 + (hit_20d - 0.50) * 0.35, 0.05, 0.90)


def _current_price(symbol: str, alpha_status: dict[str, Any], price_history: dict[str, list[dict[str, Any]]]) -> float | None:
    for signal in alpha_status.get("live_signals", []):
        if signal.get("symbol") == symbol and signal.get("close_price") is not None:
            return float(signal["close_price"])
    rows = price_history.get(symbol, [])
    return float(rows[-1]["close"]) if rows else None


def _future_business_dates(start_date: str, days: int) -> list[str]:
    current = datetime.fromisoformat(start_date).date()
    dates: list[str] = []
    while len(dates) < days + 1:
        if len(dates) == 0:
            dates.append(current.isoformat())
        current += timedelta(days=1)
        if current.weekday() < 5:
            dates.append(current.isoformat())
    return dates[: days + 1]


def _latest_as_of(alpha_status: dict[str, Any], analogs: dict[str, dict[str, Any]]) -> str | None:
    return alpha_status.get("latest_checked_date") or max((analog.get("as_of") for analog in analogs.values() if analog.get("as_of")), default=None)


def _mean(values: list[float | None]) -> float:
    clean = [value for value in values if value is not None and math.isfinite(value)]
    return sum(clean) / len(clean) if clean else 0.0


def _float_or_none(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _clip(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))


def _risk_note_for_horizon(horizon: int, overview: dict[str, Any]) -> str:
    if overview["market_state"] in {"risk_off", "panic"}:
        return f"{horizon}日路径受风险偏好和波动压力影响较大。"
    if overview["live_signal"]:
        return f"{horizon}日路径偏向反弹观察，但仍需等待未来真实结果验证。"
    return f"{horizon}日没有强信号，按历史相似情景做中性观察。"


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_high_confidence_signal_report_markdown(payload), encoding="utf-8")


def _write_edge_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_high_confidence_edge_report_markdown(payload), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
