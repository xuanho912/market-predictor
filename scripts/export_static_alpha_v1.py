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
from scripts.forecast_accuracy_ledger import (
    build_forecast_accuracy_scorecard,
    export_forecast_records_json,
    render_forecast_accuracy_scorecard_markdown,
    update_forecast_accuracy_ledger,
)
from scripts.historical_replay_benchmark import (
    render_historical_replay_benchmark_markdown,
    build_historical_replay_benchmark,
)
from scripts.model_challenger_framework import write_model_challenger_outputs
from scripts.forecast_price_levels import build_forecast_price_levels, render_forecast_price_levels_markdown
from scripts.price_volume_structure import build_price_volume_structure, render_price_volume_structure_markdown
from scripts.confluence_engine import (
    attach_confluence_to_symbols,
    build_confluence_score,
    render_confluence_score_markdown,
)
from scripts.market_alert_engine import (
    attach_alerts_to_symbols,
    build_market_alerts,
    render_market_alerts_markdown,
)
from scripts.providers.finnhub_provider import fetch_finnhub_bundle
from scripts.providers.fred_provider import DEFAULT_FRED_SERIES, fetch_fred_bundle
from scripts.providers.breadth_provider import fetch_breadth_bundle, render_breadth_status_markdown
from scripts.providers.flow_positioning_provider import (
    fetch_flow_positioning_bundle,
    render_flow_positioning_status_markdown,
)
from scripts.providers.options_provider import fetch_options_bundle, render_options_status_markdown
from scripts.providers.news_event_provider import (
    NEWS_EVENT_MARKET_SYMBOLS,
    fetch_news_event_bundle,
    render_news_event_status_markdown,
)


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
    event_refresh = _event_refresh_enabled()
    validation_type = "event_refresh" if event_refresh else "daily"

    alpha_status = alpha_status_payload()
    alpha_report = report_payload()
    analogs = {symbol: build_alpha_v1_analog_report(symbol, top_k=20) for symbol in SYMBOLS}
    market_symbols = tuple(dict.fromkeys(SYMBOLS + SUPPORT_SYMBOLS + V3_MARKET_SYMBOLS + NEWS_EVENT_MARKET_SYMBOLS))
    downloaded = refresh_market_data(symbols=market_symbols, lookback_days=520)
    series_by_symbol = {series.symbol: series for series in downloaded}
    finnhub_bundle = fetch_finnhub_bundle(symbols=SYMBOLS, lookback_days=520)
    fred_bundle = fetch_fred_bundle(lookback_days=1800)
    _print_fred_diagnostics(fred_bundle)
    breadth_bundle = fetch_breadth_bundle(series_by_symbol=series_by_symbol, lookback_days=420)
    _print_breadth_diagnostics(breadth_bundle)
    options_bundle = fetch_options_bundle(series_by_symbol=series_by_symbol)
    _print_options_diagnostics(options_bundle)
    flow_bundle = fetch_flow_positioning_bundle(series_by_symbol=series_by_symbol)
    _print_flow_diagnostics(flow_bundle)
    price_history = _load_price_history(series_by_symbol, window=PAST_WINDOW)
    price_structure_history = _load_price_history(series_by_symbol, window=260)

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
        options_bundle=options_bundle,
        flow_bundle=flow_bundle,
    )
    baseline_v4 = build_market_intelligence_v4(
        series_by_symbol=series_by_symbol,
        overview=baseline_overview,
        simulated_paths=baseline_paths,
        analogs=analogs,
        prior_intelligence=baseline_v3,
        finnhub_bundle=finnhub_bundle,
        fred_bundle=no_fred_bundle,
        options_bundle=options_bundle,
    )
    no_breadth_overview = copy.deepcopy(market_overview)
    no_breadth_paths = copy.deepcopy(simulated_paths)
    no_breadth_v2 = build_market_intelligence_v2(
        series_by_symbol=series_by_symbol,
        overview=no_breadth_overview,
        simulated_paths=no_breadth_paths,
        analogs=analogs,
    )
    no_breadth_v3 = build_market_intelligence_v3(
        series_by_symbol=series_by_symbol,
        overview=no_breadth_overview,
        simulated_paths=no_breadth_paths,
        analogs=analogs,
        prior_intelligence=no_breadth_v2,
        finnhub_bundle=finnhub_bundle,
        fred_bundle=fred_bundle,
        breadth_bundle=None,
        options_bundle=options_bundle,
        flow_bundle=flow_bundle,
    )
    no_breadth_v4 = build_market_intelligence_v4(
        series_by_symbol=series_by_symbol,
        overview=no_breadth_overview,
        simulated_paths=no_breadth_paths,
        analogs=analogs,
        prior_intelligence=no_breadth_v3,
        finnhub_bundle=finnhub_bundle,
        fred_bundle=fred_bundle,
        options_bundle=options_bundle,
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
        options_bundle=options_bundle,
        flow_bundle=flow_bundle,
    )
    intelligence_v4 = build_market_intelligence_v4(
        series_by_symbol=series_by_symbol,
        overview=market_overview,
        simulated_paths=simulated_paths,
        analogs=analogs,
        prior_intelligence=intelligence_v3,
        finnhub_bundle=finnhub_bundle,
        fred_bundle=fred_bundle,
        options_bundle=options_bundle,
    )
    news_event_bundle = fetch_news_event_bundle(
        finnhub_bundle=finnhub_bundle,
        series_by_symbol=series_by_symbol,
        simulated_paths=simulated_paths,
        validation_type=validation_type,
    )
    _print_news_event_diagnostics(news_event_bundle)
    fred_effect_summary = _fred_effect_summary(baseline_v4, intelligence_v4, baseline_paths, simulated_paths)
    breadth_impact_report = _breadth_impact_report(no_breadth_v4, intelligence_v4, no_breadth_paths, simulated_paths)
    intelligence_v4["fred_effect_summary"] = fred_effect_summary
    intelligence_v4["breadth_impact_report"] = breadth_impact_report
    intelligence_v4["news_event_intelligence"] = news_event_bundle
    intelligence_v4["data_quality_report"]["summary"]["fred_effect_summary"] = fred_effect_summary
    intelligence_v4["data_quality_report"]["summary"]["breadth_impact_summary"] = breadth_impact_report["summary"]
    _apply_news_event_quality(intelligence_v4["data_quality_report"], news_event_bundle)
    news_event_effect_summary = _apply_news_event_overlay(
        market_overview=market_overview,
        simulated_paths=simulated_paths,
        intelligence_v4=intelligence_v4,
        news_event_bundle=news_event_bundle,
        validation_type=validation_type,
    )
    news_event_bundle["prediction_logic_effect"] = news_event_effect_summary
    intelligence_v4["news_event_prediction_effect"] = news_event_effect_summary
    _attach_news_event_intelligence(market_overview, simulated_paths, news_event_bundle)
    forecast_price_levels = build_forecast_price_levels(
        price_history=price_structure_history,
        simulated_paths=simulated_paths,
    )
    forecast_price_levels["validation_type"] = validation_type
    _attach_forecast_price_levels(market_overview, simulated_paths, forecast_price_levels)
    price_volume_structure = build_price_volume_structure(series_by_symbol=series_by_symbol)
    confluence_score = build_confluence_score(
        market_overview=market_overview,
        simulated_paths=simulated_paths,
        intelligence_v4=intelligence_v4,
        forecast_price_levels=forecast_price_levels,
        price_volume_structure=price_volume_structure,
        breadth_bundle=breadth_bundle,
        options_bundle=options_bundle,
        flow_bundle=flow_bundle,
        news_event_bundle=news_event_bundle,
    )
    attach_confluence_to_symbols(market_overview, simulated_paths, confluence_score)
    market_alerts = build_market_alerts(
        market_overview=market_overview,
        simulated_paths=simulated_paths,
        forecast_price_levels=forecast_price_levels,
        price_volume_structure=price_volume_structure,
        confluence_score=confluence_score,
        news_event_bundle=news_event_bundle,
    )
    attach_alerts_to_symbols(market_overview, simulated_paths, market_alerts)
    dashboard = {
        "generated_by": "scripts/export_static_alpha_v1.py",
        "source": "github_actions_forward_tracker_outputs",
        "validation_type": validation_type,
        "event_refresh": event_refresh,
        "as_of": _latest_as_of(alpha_status, analogs),
        "status_note": "Alpha v1 remains a research candidate. Simulated paths are probabilistic scenarios, not guaranteed forecasts.",
        "overview": market_overview,
        "simulated_paths": simulated_paths,
        "market_intelligence_v2": intelligence_v2,
        "market_intelligence_v3": intelligence_v3,
        "market_intelligence_v4": intelligence_v4,
        "data_quality_report": intelligence_v4["data_quality_report"],
        "breadth_status": breadth_bundle,
        "options_status": options_bundle,
        "flow_status": flow_bundle,
        "flow_positioning_status": flow_bundle,
        "news_event_status": news_event_bundle,
        "breadth_impact_report": breadth_impact_report,
        "forecast_price_levels": forecast_price_levels,
        "price_volume_structure": price_volume_structure,
        "confluence_score": confluence_score,
        "market_alerts": market_alerts,
        "feature_snapshot_v2": intelligence_v2["feature_snapshot_v2"],
        "feature_snapshot_v3": intelligence_v3["feature_snapshot_v3"],
        "model_confidence_by_symbol": intelligence_v4["model_confidence_by_symbol"],
        "high_confidence_signal_report": intelligence_v3["high_confidence_signal_report"],
        "high_confidence_edge_report": intelligence_v4["high_confidence_edge_report"],
        "alpha_status": alpha_status,
        "forward_report": alpha_report,
        "analogs": analogs,
    }
    ledger_summary = (
        _event_refresh_ledger_summary()
        if event_refresh
        else update_forecast_accuracy_ledger(dashboard=dashboard, price_history=price_history)
    )
    forecast_records = export_forecast_records_json()
    forecast_scorecard = build_forecast_accuracy_scorecard()
    historical_replay_benchmark = build_historical_replay_benchmark(dashboard)
    model_governance = write_model_challenger_outputs(dashboard=dashboard, public_dir=public_dir, outputs_dir=PROJECT_ROOT / "outputs")
    dashboard["forecast_ledger_summary"] = ledger_summary
    dashboard["forecast_records"] = forecast_records
    dashboard["forecast_accuracy_scorecard"] = forecast_scorecard
    dashboard["historical_replay_benchmark"] = historical_replay_benchmark
    dashboard["model_leaderboard"] = model_governance["leaderboard"]
    dashboard["model_promotion_status"] = model_governance["promotion_status"]

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
    _write_json(public_dir / "options-status.json", options_bundle)
    _write_json(public_dir / "flow-status.json", flow_bundle)
    _write_json(public_dir / "flow-positioning-status.json", flow_bundle)
    _write_json(public_dir / "news-event-status.json", news_event_bundle)
    _write_json(public_dir / "breadth-impact-report.json", breadth_impact_report)
    _write_json(public_dir / "forecast-price-levels.json", forecast_price_levels)
    _write_json(public_dir / "price-volume-structure.json", price_volume_structure)
    _write_json(public_dir / "confluence-score.json", confluence_score)
    _write_json(public_dir / "market-alerts.json", market_alerts)
    _write_json(public_dir / "high-confidence-signal-report.json", intelligence_v3["high_confidence_signal_report"])
    _write_json(public_dir / "high-confidence-edge-report.json", intelligence_v4["high_confidence_edge_report"])
    _write_json(public_dir / "forecast-records.json", forecast_records)
    _write_json(public_dir / "forecast-accuracy-scorecard.json", forecast_scorecard)
    _write_json(public_dir / "historical-replay-benchmark.json", historical_replay_benchmark)
    _write_json(public_dir / "model-leaderboard.json", model_governance["leaderboard"])
    _write_json(public_dir / "model-promotion-status.json", model_governance["promotion_status"])
    _write_json(public_dir / "market-overview.json", market_overview)
    _write_json(public_dir / "simulated-paths.json", simulated_paths)
    _write_json(public_dir / "prediction-dashboard.json", dashboard)
    _write_report(PROJECT_ROOT / "outputs" / "high_confidence_signal_report.md", intelligence_v3["high_confidence_signal_report"])
    _write_edge_report(PROJECT_ROOT / "outputs" / "high_confidence_edge_report.md", intelligence_v4["high_confidence_edge_report"])
    _write_fred_status_report(PROJECT_ROOT / "outputs" / "fred_data_status.md", fred_bundle, fred_effect_summary, intelligence_v4)
    _write_breadth_status_report(PROJECT_ROOT / "outputs" / "breadth_data_status.md", breadth_bundle)
    _write_options_status_report(PROJECT_ROOT / "outputs" / "options_data_status.md", options_bundle)
    _write_flow_status_report(PROJECT_ROOT / "outputs" / "flow_data_status.md", flow_bundle)
    _write_flow_status_report(PROJECT_ROOT / "outputs" / "flow_positioning_status.md", flow_bundle)
    _write_news_event_status_report(PROJECT_ROOT / "outputs" / "news_event_status.md", news_event_bundle)
    _write_breadth_impact_status_report(PROJECT_ROOT / "outputs" / "breadth_impact_report.md", breadth_impact_report)
    _write_forecast_price_levels_report(PROJECT_ROOT / "outputs" / "forecast_price_levels.md", forecast_price_levels)
    _write_price_volume_structure_report(PROJECT_ROOT / "outputs" / "price_volume_structure.md", price_volume_structure)
    _write_confluence_score_report(PROJECT_ROOT / "outputs" / "confluence_score.md", confluence_score)
    _write_market_alerts_report(PROJECT_ROOT / "outputs" / "market_alerts.md", market_alerts)
    _write_forecast_accuracy_scorecard_report(PROJECT_ROOT / "outputs" / "forecast_accuracy_scorecard.md", forecast_scorecard)
    _write_historical_replay_benchmark_report(PROJECT_ROOT / "outputs" / "historical_replay_benchmark.md", historical_replay_benchmark)

    print("wrote frontend/public/alpha-v1-status.json")
    print("wrote frontend/public/alpha-v1-analogs.json")
    print("wrote frontend/public/data_quality_report.json")
    print("wrote frontend/public/breadth-status.json")
    print("wrote frontend/public/options-status.json")
    print("wrote frontend/public/flow-status.json")
    print("wrote frontend/public/flow-positioning-status.json")
    print("wrote frontend/public/news-event-status.json")
    print("wrote frontend/public/breadth-impact-report.json")
    print("wrote frontend/public/forecast-price-levels.json")
    print("wrote frontend/public/price-volume-structure.json")
    print("wrote frontend/public/confluence-score.json")
    print("wrote frontend/public/market-alerts.json")
    print("wrote frontend/public/high-confidence-signal-report.json")
    print("wrote frontend/public/high-confidence-edge-report.json")
    print("wrote frontend/public/forecast-records.json")
    print("wrote frontend/public/forecast-accuracy-scorecard.json")
    print("wrote frontend/public/historical-replay-benchmark.json")
    print("wrote frontend/public/model-leaderboard.json")
    print("wrote frontend/public/model-promotion-status.json")
    print("wrote frontend/public/market-overview.json")
    print("wrote frontend/public/simulated-paths.json")
    print("wrote frontend/public/prediction-dashboard.json")
    print("wrote outputs/high_confidence_signal_report.md")
    print("wrote outputs/high_confidence_edge_report.md")
    print("wrote outputs/fred_data_status.md")
    print("wrote outputs/breadth_data_status.md")
    print("wrote outputs/options_data_status.md")
    print("wrote outputs/flow_data_status.md")
    print("wrote outputs/flow_positioning_status.md")
    print("wrote outputs/news_event_status.md")
    print("wrote outputs/breadth_impact_report.md")
    print("wrote outputs/forecast_price_levels.md")
    print("wrote outputs/price_volume_structure.md")
    print("wrote outputs/confluence_score.md")
    print("wrote outputs/market_alerts.md")
    print("wrote outputs/forecast_accuracy_scorecard.md")
    print("wrote outputs/historical_replay_benchmark.md")
    print("wrote outputs/model_leaderboard.md")
    print("wrote outputs/model_promotion_rules.md")
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


def _print_options_diagnostics(bundle: dict[str, Any]) -> None:
    summary = bundle.get("summary") or {}
    market = bundle.get("market") or {}
    print(f"OPTIONS_AVAILABLE={str(bool(summary.get('options_available'))).lower()}")
    print(f"OPTIONS_PARTIAL={str(bool(summary.get('options_partial'))).lower()}")
    print(f"OPTIONS_MISSING={str(bool(summary.get('options_missing'))).lower()}")
    print(f"VIX_TERM_AVAILABLE={str(bool(summary.get('vix_term_available'))).lower()}")
    print(f"VVIX_AVAILABLE={str(bool(summary.get('vvix_available'))).lower()}")
    print(f"SKEW_AVAILABLE={str(bool(summary.get('skew_available'))).lower()}")
    print(f"PUT_CALL_AVAILABLE={str(bool(summary.get('put_call_available'))).lower()}")
    print(f"GAMMA_AVAILABLE={str(bool(summary.get('gamma_available'))).lower()}")
    print(f"OPTIONS_QUALITY_SCORE={summary.get('options_quality_score')}")
    print(f"VIX_TERM_STATE={market.get('term_structure_state') or 'missing'}")
    print(f"OPTION_STRESS_SCORE={market.get('option_stress_score') if market.get('option_stress_score') is not None else 'NA'}")
    for symbol, payload in sorted((bundle.get("sources") or {}).items()):
        print(
            "OPTIONS_SOURCE "
            f"symbol={symbol} "
            f"status={payload.get('status') or 'missing'} "
            f"latest_date={payload.get('latest_date') or 'NA'} "
            f"latest_value={payload.get('latest_value') if payload.get('latest_value') is not None else 'NA'} "
            f"source={payload.get('source') or 'NA'} "
            f"real_data={str(bool(payload.get('real_data'))).lower()} "
            f"stale={str(bool(payload.get('stale_data'))).lower()}"
        )


def _print_flow_diagnostics(bundle: dict[str, Any]) -> None:
    summary = bundle.get("summary") or {}
    print(f"FLOW_AVAILABLE={str(bool(summary.get('flow_available'))).lower()}")
    print(f"FLOW_PROXY_ONLY={str(bool(summary.get('flow_proxy_only'))).lower()}")
    print(f"TRUE_FLOW_AVAILABLE={str(bool(summary.get('true_flow_available'))).lower()}")
    print(f"FLOW_AVERAGE_QUALITY={summary.get('average_flow_quality_score')}")
    print(f"FLOW_CONFIRMATION_SCORE={summary.get('overall_flow_confirmation_score')}")
    print(f"FLOW_CONFLICT_SCORE={summary.get('overall_flow_conflict_score')}")
    for symbol, payload in sorted((bundle.get("symbols") or {}).items()):
        scores = payload.get("scores") or {}
        print(
            "FLOW_PROXY "
            f"symbol={symbol} "
            f"status={payload.get('status') or 'missing'} "
            f"latest_date={payload.get('latest_date') or 'NA'} "
            f"quality={scores.get('flow_quality_score') if scores.get('flow_quality_score') is not None else 'NA'} "
            f"confirmation={scores.get('flow_confirmation_score') if scores.get('flow_confirmation_score') is not None else 'NA'} "
            f"conflict={scores.get('flow_conflict_score') if scores.get('flow_conflict_score') is not None else 'NA'} "
            f"true_flow={str(bool(payload.get('true_flow_available'))).lower()}"
        )


def _print_news_event_diagnostics(bundle: dict[str, Any]) -> None:
    narrative = bundle.get("market_narrative") or {}
    reaction = bundle.get("price_reaction_confirmation") or {}
    print(f"NEWS_EVENT_STATUS={bundle.get('status') or 'missing'}")
    print(f"NEWS_EVENT_VALIDATION_TYPE={bundle.get('validation_type') or 'daily'}")
    print(f"NEWS_EVENT_PROVIDER_FAILED={str(bool(bundle.get('provider_failed'))).lower()}")
    print(f"NEWS_EVENT_MAJOR_COUNT={bundle.get('major_event_count') if bundle.get('major_event_count') is not None else 'NA'}")
    print(f"NEWS_EVENT_RISK_LEVEL={bundle.get('event_risk_level') or 'NA'}")
    print(f"NEWS_EVENT_NARRATIVE={narrative.get('market_narrative') or 'no_clear_narrative'}")
    print(f"NEWS_EVENT_DIRECTION={narrative.get('narrative_direction') or 'mixed'}")
    print(f"NEWS_EVENT_PRICE_CONFIRMED={str(bool(reaction.get('price_reaction_confirmed'))).lower()}")
    print(f"NEWS_EVENT_CONFIRMATION_SCORE={reaction.get('confirmation_score') if reaction.get('confirmation_score') is not None else 'NA'}")
    calendar = bundle.get("economic_calendar_risk") or {}
    print(f"NEWS_EVENT_MACRO_RISK_FLAG={str(bool(calendar.get('macro_event_risk_flag'))).lower()}")
    print(f"NEWS_EVENT_MACRO_RISK_SCORE={calendar.get('macro_event_risk_score') if calendar.get('macro_event_risk_score') is not None else 'NA'}")


def _event_refresh_enabled() -> bool:
    return os.getenv("EVENT_REFRESH", "").strip().lower() in {"1", "true", "yes", "y"}


def _event_refresh_ledger_summary() -> dict[str, Any]:
    return {
        "version": "forecast_accuracy_ledger_v1",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "active_model_version": "baseline_v1",
        "event_refresh_mode": True,
        "ledger_append_skipped": True,
        "validation_type": "event_refresh",
        "immutability_note": "Manual event refresh updates the current dashboard only. It does not rewrite or append baseline_v1 forecast records.",
        "not_trading_note": "This is a forecast refresh, not a trading signal or execution workflow.",
    }


def _apply_news_event_overlay(
    *,
    market_overview: dict[str, Any],
    simulated_paths: dict[str, Any],
    intelligence_v4: dict[str, Any],
    news_event_bundle: dict[str, Any],
    validation_type: str,
) -> dict[str, Any]:
    narrative = news_event_bundle.get("market_narrative") or {}
    reaction = news_event_bundle.get("price_reaction_confirmation") or {}
    calendar = news_event_bundle.get("economic_calendar_risk") or {}
    direction = str(narrative.get("narrative_direction") or "mixed")
    strength = _clip((_float_or_none(narrative.get("narrative_strength")) or 0.0) / 100.0, 0.0, 1.0)
    reaction_score = _clip((_float_or_none(reaction.get("confirmation_score")) or 0.0) / 100.0, 0.0, 1.0)
    major_count = int(news_event_bundle.get("major_event_count") or 0)
    price_confirmed = bool(reaction.get("price_reaction_confirmed"))
    macro_score = _clip((_float_or_none(calendar.get("macro_event_risk_score")) or 0.0) / 100.0, 0.0, 1.0)
    macro_risk = bool(calendar.get("macro_event_risk_flag"))
    event_risk_level = str(news_event_bundle.get("event_risk_level") or "low")
    impacts = news_event_bundle.get("symbol_impacts") or {}
    summary: dict[str, Any] = {
        "version": "news_event_overlay_v1",
        "validation_type": validation_type,
        "applied": False,
        "major_event_count": major_count,
        "direction": direction,
        "price_reaction_confirmed": price_confirmed,
        "macro_event_risk_flag": macro_risk,
        "event_risk_level": event_risk_level,
        "not_a_trading_signal": True,
        "symbols": {},
    }
    if major_count == 0 and not macro_risk:
        summary["reason"] = "no_major_event_or_macro_risk"
        return summary

    for symbol in SYMBOLS:
        overview_symbol = (market_overview.get("symbols") or {}).get(symbol)
        simulated_symbol = (simulated_paths.get("symbols") or {}).get(symbol)
        if not isinstance(overview_symbol, dict) or not isinstance(simulated_symbol, dict):
            continue
        impact = impacts.get(symbol, {})
        symbol_effect = _apply_news_event_overlay_to_symbol(
            symbol=symbol,
            overview_symbol=overview_symbol,
            simulated_symbol=simulated_symbol,
            intelligence_v4=intelligence_v4,
            impact=impact,
            direction=direction,
            strength=strength,
            reaction_score=reaction_score,
            price_confirmed=price_confirmed,
            macro_score=macro_score,
            macro_risk=macro_risk,
            event_risk_level=event_risk_level,
            major_count=major_count,
            validation_type=validation_type,
        )
        summary["symbols"][symbol] = symbol_effect
        summary["applied"] = bool(summary["applied"] or symbol_effect.get("overlay_applied"))
    return summary


def _apply_news_event_overlay_to_symbol(
    *,
    symbol: str,
    overview_symbol: dict[str, Any],
    simulated_symbol: dict[str, Any],
    intelligence_v4: dict[str, Any],
    impact: dict[str, Any],
    direction: str,
    strength: float,
    reaction_score: float,
    price_confirmed: bool,
    macro_score: float,
    macro_risk: bool,
    event_risk_level: str,
    major_count: int,
    validation_type: str,
) -> dict[str, Any]:
    before_ranking = copy.deepcopy(simulated_symbol.get("scenario_ranking") or {})
    before_primary = (before_ranking.get("primary") or {}).get("scenario")
    before_primary_prob = _float_or_none((before_ranking.get("primary") or {}).get("probability"))
    confirmation_delta = 0.0
    predictor_deltas = {
        "bounce_predictor": 0.0,
        "downside_continuation_predictor": 0.0,
        "trend_reversal_predictor": 0.0,
        "risk_expansion_predictor": 0.0,
    }
    weight_deltas = {
        "base_path_weight": 0.0,
        "bounce_path_weight": 0.0,
        "bearish_path_weight": 0.0,
        "analog_path_weight": 0.0,
    }
    overlay_applied = major_count > 0 or macro_risk
    reason_parts: list[str] = []
    if major_count > 0 and direction in {"supports_bounce", "supports_trend_reversal"}:
        if price_confirmed:
            magnitude = min(0.055, 0.015 + 0.045 * strength * max(reaction_score, 0.35))
            weight_deltas["bounce_path_weight"] += magnitude
            weight_deltas["bearish_path_weight"] -= magnitude * 0.35
            confirmation_delta += min(6.0, 2.0 + 5.0 * strength * reaction_score)
            predictor_deltas["bounce_predictor"] += min(0.04, 0.015 + magnitude * 0.45)
            predictor_deltas["trend_reversal_predictor"] += min(0.02, magnitude * 0.30)
            predictor_deltas["risk_expansion_predictor"] -= min(0.025, magnitude * 0.35)
            reason_parts.append("risk-on news with price confirmation raised bounce path weight")
        else:
            magnitude = min(0.035, 0.012 + 0.025 * strength)
            weight_deltas["base_path_weight"] += magnitude
            weight_deltas["bearish_path_weight"] += magnitude * 0.35
            confirmation_delta -= min(2.0, 0.5 + 2.0 * strength)
            predictor_deltas["downside_continuation_predictor"] += min(0.015, magnitude * 0.25)
            reason_parts.append("risk-on news is not confirmed by price, so base/risk paths gained weight")
    elif major_count > 0 and direction in {"supports_downside", "supports_risk_expansion"}:
        magnitude = min(0.060, 0.016 + 0.050 * strength * (reaction_score if price_confirmed else 0.45))
        weight_deltas["bearish_path_weight"] += magnitude
        weight_deltas["bounce_path_weight"] -= magnitude * 0.35
        weight_deltas["base_path_weight"] += 0.010 if not price_confirmed else 0.0
        confirmation_delta -= min(8.0, 2.0 + 6.0 * strength * (reaction_score if price_confirmed else 0.50))
        predictor_deltas["downside_continuation_predictor"] += min(0.04, magnitude * 0.55)
        predictor_deltas["risk_expansion_predictor"] += min(0.05, magnitude * 0.65)
        predictor_deltas["bounce_predictor"] -= min(0.025, magnitude * 0.30)
        reason_parts.append("risk-off news raised failed-bounce / risk-expansion path weight")
    elif major_count > 0:
        magnitude = min(0.030, 0.010 + 0.020 * strength)
        weight_deltas["base_path_weight"] += magnitude
        confirmation_delta -= 1.0 if strength >= 0.35 else 0.0
        reason_parts.append("mixed news increased base path uncertainty")
    if macro_risk:
        macro_delta = min(0.035, 0.010 + 0.030 * macro_score)
        weight_deltas["base_path_weight"] += macro_delta
        confirmation_delta -= min(4.0, 1.0 + 4.0 * macro_score)
        reason_parts.append("near-term macro calendar risk capped conviction")

    _update_signal_confirmation_for_news(
        simulated_symbol=simulated_symbol,
        overview_symbol=overview_symbol,
        intelligence_v4=intelligence_v4,
        symbol=symbol,
        delta=confirmation_delta,
        direction=direction,
        price_confirmed=price_confirmed,
        macro_risk=macro_risk,
        reason_parts=reason_parts,
    )
    _update_predictors_for_news(simulated_symbol, overview_symbol, intelligence_v4, symbol, predictor_deltas, reason_parts)
    new_weights = _adjust_path_weights_for_news(simulated_symbol, weight_deltas, direction, price_confirmed, macro_risk, reason_parts)
    for target in (simulated_symbol, overview_symbol):
        target["path_weight_model"] = copy.deepcopy(new_weights)
        target["base_path_weight"] = new_weights["base_path_weight"]
        target["bounce_path_weight"] = new_weights["bounce_path_weight"]
        target["bearish_path_weight"] = new_weights["bearish_path_weight"]
        target["analog_path_weight"] = new_weights["analog_path_weight"]
        target["scenario_ranking"] = _scenario_ranking_from_adjusted_weights(symbol, new_weights, simulated_symbol.get("scenario_ranking") or {}, reason_parts)
    simulated_symbol["scenario_weights"] = {
        "base_scenario": new_weights["base_path_weight"],
        "bounce_scenario": new_weights["bounce_path_weight"],
        "bearish_scenario": new_weights["bearish_path_weight"],
        "historical_analog_average": new_weights["analog_path_weight"],
    }
    _update_scenario_cards_for_news(simulated_symbol, new_weights)
    path_overlay = _apply_news_event_path_shock(
        simulated_symbol=simulated_symbol,
        direction=direction,
        strength=strength,
        reaction_score=reaction_score,
        price_confirmed=price_confirmed,
        major_count=major_count,
        validation_type=validation_type,
    )
    if event_risk_level == "high" and direction in {"supports_downside", "supports_risk_expansion"} and price_confirmed:
        _apply_news_event_risk_warning(simulated_symbol, overview_symbol, intelligence_v4, symbol)

    after_ranking = simulated_symbol.get("scenario_ranking") or {}
    after_primary = (after_ranking.get("primary") or {}).get("scenario")
    after_primary_prob = _float_or_none((after_ranking.get("primary") or {}).get("probability"))
    effect = {
        "overlay_applied": overlay_applied,
        "validation_type": validation_type,
        "before_primary_scenario": before_primary,
        "after_primary_scenario": after_primary,
        "primary_scenario_changed": before_primary != after_primary,
        "before_primary_probability": before_primary_prob,
        "after_primary_probability": after_primary_prob,
        "primary_probability_delta": _round_return((after_primary_prob or 0.0) - (before_primary_prob or 0.0)),
        "confirmation_delta": round(confirmation_delta, 2),
        "predictor_deltas": {key: round(value, 4) for key, value in predictor_deltas.items()},
        "path_weight_deltas": {key: round(value, 4) for key, value in weight_deltas.items()},
        "path_overlay": path_overlay,
        "reason": "; ".join(reason_parts) if reason_parts else "no material news/event effect",
        "impact": impact.get("impact"),
        "not_a_trading_signal": True,
    }
    patch = simulated_symbol.setdefault("news_event_intelligence", {})
    patch["prediction_logic_effect"] = effect
    patch["validation_type"] = validation_type
    overview_patch = overview_symbol.setdefault("news_event_intelligence", {})
    overview_patch["prediction_logic_effect"] = effect
    overview_patch["validation_type"] = validation_type
    return effect


def _update_signal_confirmation_for_news(
    *,
    simulated_symbol: dict[str, Any],
    overview_symbol: dict[str, Any],
    intelligence_v4: dict[str, Any],
    symbol: str,
    delta: float,
    direction: str,
    price_confirmed: bool,
    macro_risk: bool,
    reason_parts: list[str],
) -> None:
    confirmation = copy.deepcopy(simulated_symbol.get("signal_confirmation") or {})
    if not confirmation:
        confirmation = copy.deepcopy((intelligence_v4.get("signal_confirmation_by_symbol") or {}).get(symbol) or {})
    if not confirmation:
        return
    before = _float_or_none(confirmation.get("confirmation_score")) or _float_or_none(confirmation.get("signal_confirmation_score")) or 0.0
    after = _clip(before + delta, 0.0, 100.0)
    confirmation["confirmation_score"] = round(after, 2)
    confirmation["signal_confirmation_score"] = round(after, 2)
    confirmation["confirmation_level"] = "strong" if after >= 70 else "mixed" if after >= 45 else "weak"
    if direction in {"supports_bounce", "supports_trend_reversal"} and price_confirmed:
        confirmation.setdefault("supporting_evidence", []).append(
            {"name": "news_event_price_confirmed", "score": round(after, 2), "detail": "重大 risk-on 新闻已被价格反应初步确认。"}
        )
    elif direction in {"supports_downside", "supports_risk_expansion"}:
        confirmation.setdefault("conflicting_evidence", []).append(
            {"name": "risk_off_news_event", "score": round(100 - after, 2), "detail": "重大 risk-off 新闻提高风险路径权重。"}
        )
    elif direction in {"supports_bounce", "supports_trend_reversal"} and not price_confirmed:
        confirmation.setdefault("conflicting_evidence", []).append(
            {"name": "news_not_confirmed_by_price", "score": round(100 - after, 2), "detail": "新闻文字利多，但指数/VIX/信用代理没有充分确认。"}
        )
    if macro_risk:
        confirmation.setdefault("conflicting_evidence", []).append(
            {"name": "macro_event_calendar_risk", "score": round(100 - after, 2), "detail": "临近重要宏观事件，短线路径置信度需要打折。"}
        )
    for target in (simulated_symbol, overview_symbol):
        target["signal_confirmation"] = copy.deepcopy(confirmation)
        target["signal_confirmation_score"] = round(after, 2)
    (intelligence_v4.setdefault("signal_confirmation_by_symbol", {}))[symbol] = copy.deepcopy(confirmation)
    reason_parts.append(f"signal confirmation adjusted {delta:+.2f} points")


def _update_predictors_for_news(
    simulated_symbol: dict[str, Any],
    overview_symbol: dict[str, Any],
    intelligence_v4: dict[str, Any],
    symbol: str,
    deltas: dict[str, float],
    reason_parts: list[str],
) -> None:
    predictors = copy.deepcopy(simulated_symbol.get("predictors_v4") or {})
    if not predictors:
        predictors = copy.deepcopy((intelligence_v4.get("predictor_outputs_by_symbol") or {}).get(symbol) or {})
    if not predictors:
        return
    for predictor_name, delta in deltas.items():
        if predictor_name not in predictors or abs(delta) < 0.0001:
            continue
        payload = predictors[predictor_name]
        before = _float_or_none(payload.get("probability")) or 0.0
        after = _clip(before + delta, 0.0, 0.95)
        payload["probability"] = round(after, 4)
        for probability_key in (
            "bounce_probability",
            "downside_continuation_probability",
            "trend_reversal_probability",
            "risk_expansion_probability",
        ):
            if probability_key in payload:
                payload[probability_key] = round(after, 4)
        drivers_key = "main_drivers" if "main_drivers" in payload else "key_drivers"
        payload.setdefault(drivers_key, [])
        payload[drivers_key] = list(payload[drivers_key]) + [f"news_event_overlay:{delta:+.3f}"]
    for target in (simulated_symbol, overview_symbol):
        target["predictors_v4"] = copy.deepcopy(predictors)
        target["predictors"] = copy.deepcopy(predictors)
    (intelligence_v4.setdefault("predictor_outputs_by_symbol", {}))[symbol] = copy.deepcopy(predictors)
    if any(abs(value) >= 0.0001 for value in deltas.values()):
        reason_parts.append("independent predictors adjusted by news/event overlay")


def _adjust_path_weights_for_news(
    simulated_symbol: dict[str, Any],
    deltas: dict[str, float],
    direction: str,
    price_confirmed: bool,
    macro_risk: bool,
    reason_parts: list[str],
) -> dict[str, Any]:
    weights = copy.deepcopy(simulated_symbol.get("path_weight_model") or {})
    if not weights:
        weights = {
            "base_path_weight": _float_or_none(simulated_symbol.get("base_path_weight")) or 0.25,
            "bounce_path_weight": _float_or_none(simulated_symbol.get("bounce_path_weight")) or 0.25,
            "bearish_path_weight": _float_or_none(simulated_symbol.get("bearish_path_weight")) or 0.25,
            "analog_path_weight": _float_or_none(simulated_symbol.get("analog_path_weight")) or 0.25,
        }
    raw = {
        key: max((_float_or_none(weights.get(key)) or 0.0) + deltas.get(key, 0.0), 0.001)
        for key in ("base_path_weight", "bounce_path_weight", "bearish_path_weight", "analog_path_weight")
    }
    total = sum(raw.values()) or 1.0
    for key, value in raw.items():
        weights[key] = round(value / total, 4)
    factors = dict(weights.get("weight_factors") or {})
    factors.update(
        {
            "news_event_direction": direction,
            "news_event_price_confirmed": 1.0 if price_confirmed else 0.0,
            "news_event_macro_risk": 1.0 if macro_risk else 0.0,
        }
    )
    weights["weight_factors"] = factors
    notes = list(weights.get("weight_source_notes") or [])
    notes.append("News/Event overlay can move a small amount of weight between bounce, base and risk paths when a major event is detected.")
    weights["weight_source_notes"] = notes
    weights["news_event_overlay_applied"] = True
    weights["news_event_overlay_note"] = "; ".join(reason_parts) if reason_parts else "no material event adjustment"
    weights["low_confidence_simulation"] = bool(weights.get("low_confidence_simulation")) or (macro_risk and not price_confirmed)
    if weights.get("low_confidence_simulation"):
        weights["simulation_confidence_level"] = "low" if weights.get("simulation_confidence_level") == "low" else "medium"
    return weights


def _scenario_ranking_from_adjusted_weights(
    symbol: str,
    weights: dict[str, Any],
    previous_ranking: dict[str, Any],
    reason_parts: list[str],
) -> dict[str, Any]:
    scenario_defs = [
        ("expected_path", "综合期望情景", "base_path_weight", "3d-20d"),
        ("bounce_path", "反抽情景", "bounce_path_weight", "10d-20d"),
        ("bearish_path", "失败反抽情景", "bearish_path_weight", "3d-10d"),
        ("analog_average_path", "历史均值情景", "analog_path_weight", "20d-60d"),
    ]
    total = sum(max(_float_or_none(weights.get(weight_key)) or 0.0, 0.0) for _, _, weight_key, _ in scenario_defs) or 1.0
    previous_by_scenario = {
        item.get("scenario"): item for item in (previous_ranking.get("all_scenarios") or []) if isinstance(item, dict)
    }
    ranked: list[dict[str, Any]] = []
    for scenario, label, weight_key, horizon in scenario_defs:
        probability = max(_float_or_none(weights.get(weight_key)) or 0.0, 0.0) / total
        prior = previous_by_scenario.get(scenario) or {}
        reason = str(prior.get("reason") or f"{label} weight after current multi-source model.")
        if reason_parts:
            reason = f"{reason} News/Event overlay: {'; '.join(reason_parts)}."
        ranked.append(
            {
                "scenario": scenario,
                "label": label,
                "probability": round(probability, 4),
                "reason": reason,
                "expected_horizon": prior.get("expected_horizon") or horizon,
                "confidence": weights.get("simulation_confidence_level") or prior.get("confidence") or "medium",
            }
        )
    ranked.sort(key=lambda item: item["probability"], reverse=True)
    primary, secondary, tertiary = ranked[0], ranked[1], ranked[2]
    risk = next((item for item in ranked if item["scenario"] == "bearish_path"), tertiary)
    gap = round(primary["probability"] - secondary["probability"], 4)
    return {
        "primary": primary,
        "secondary": secondary,
        "tertiary": tertiary,
        "all_scenarios": ranked,
        "primary_scenario": primary["scenario"],
        "secondary_scenario": secondary["scenario"],
        "risk_scenario": risk["scenario"],
        "scenario_probability": primary["probability"],
        "probability_gap": gap,
        "primary_secondary_gap": gap,
        "close_call": gap < 0.08,
        "path_reliability": weights.get("simulation_confidence_level", "medium"),
        "switching_conditions": _news_switching_conditions(symbol, primary["scenario"], secondary["scenario"]),
        "primary_to_secondary_switch_conditions": _news_switching_conditions(symbol, primary["scenario"], secondary["scenario"]),
        "ranking_note": "Scenario ranking includes a bounded News/Event overlay when a major event or macro calendar risk is detected. It is probabilistic, not deterministic.",
        "close_call_note": "路径分歧较大，不宜过度押注单一路径。" if gap < 0.08 else "",
    }


def _news_switching_conditions(symbol: str, primary: str, secondary: str) -> list[str]:
    conditions = ["VIX 与新闻方向背离", "HYG/LQD 转弱", "重大新闻没有被价格继续确认"]
    if primary == "bounce_path":
        conditions.extend([f"{symbol} 跌破主路径失效价", "油价或美元重新走强"])
    elif primary == "bearish_path":
        conditions.extend(["VIX 快速回落", f"{symbol} 重新站上主路径确认价"])
    else:
        conditions.extend(["主路径和第二路径概率差距扩大", "宏观事件风险下降"])
    if secondary:
        conditions.append(f"第二路径 {secondary} 获得多源确认")
    return conditions


def _update_scenario_cards_for_news(simulated_symbol: dict[str, Any], weights: dict[str, Any]) -> None:
    mapping = {
        "Base case": "base_path_weight",
        "Bounce case": "bounce_path_weight",
        "Bearish case": "bearish_path_weight",
        "Historical analog case": "analog_path_weight",
    }
    for card in simulated_symbol.get("scenario_cards", []):
        key = mapping.get(card.get("name"))
        if key:
            card["probability_weight"] = weights[key]


def _apply_news_event_path_shock(
    *,
    simulated_symbol: dict[str, Any],
    direction: str,
    strength: float,
    reaction_score: float,
    price_confirmed: bool,
    major_count: int,
    validation_type: str,
) -> dict[str, Any]:
    if major_count <= 0 or not price_confirmed or direction not in {"supports_bounce", "supports_trend_reversal", "supports_downside", "supports_risk_expansion"}:
        overlay = {
            "applied": False,
            "validation_type": validation_type,
            "reason": "No confirmed major directional event; short-term paths were not moved.",
            "not_a_trading_signal": True,
        }
        simulated_symbol["news_event_path_overlay"] = overlay
        return overlay
    paths = simulated_symbol.get("paths") or {}
    split_index = int(paths.get("split_index") or 0)
    sign = 1.0 if direction in {"supports_bounce", "supports_trend_reversal"} else -1.0
    shock = min(0.008, 0.002 + 0.008 * strength * max(reaction_score, 0.35))
    path_shocks = {
        "expected_path": 1.0,
        "bounce_path": 1.15 if sign > 0 else 0.35,
        "bearish_path": 0.35 if sign > 0 else 1.15,
        "analog_average_path": 0.55,
    }
    for path_key, multiplier in path_shocks.items():
        values = paths.get(path_key)
        if not isinstance(values, list):
            continue
        for offset, fade in ((1, 1.0), (2, 0.72), (3, 0.45)):
            index = split_index + offset
            if index >= len(values) or values[index] is None:
                continue
            adjusted = float(values[index]) * (1.0 + sign * shock * multiplier * fade)
            values[index] = round(adjusted, 4)
    _refresh_confidence_band(paths)
    _adjust_short_horizon_summary(simulated_symbol, sign, shock)
    overlay = {
        "applied": True,
        "validation_type": validation_type,
        "direction": direction,
        "shock_return_1d": round(sign * shock, 4),
        "shock_return_3d": round(sign * shock * 0.45, 4),
        "source": "news_event_price_reaction_overlay",
        "reason": "Confirmed major event adjusted only the 1d/3d probability path; historical records are not rewritten.",
        "not_a_trading_signal": True,
    }
    simulated_symbol["news_event_path_overlay"] = overlay
    return overlay


def _refresh_confidence_band(paths: dict[str, Any]) -> None:
    upper = paths.get("confidence_band_upper")
    lower = paths.get("confidence_band_lower")
    expected = paths.get("expected_path")
    bounce = paths.get("bounce_path")
    bearish = paths.get("bearish_path")
    analog = paths.get("analog_average_path")
    if not all(isinstance(item, list) for item in (upper, lower, expected, bounce, bearish, analog)):
        return
    for index in range(min(len(upper), len(lower), len(expected), len(bounce), len(bearish), len(analog))):
        values = [item[index] for item in (expected, bounce, bearish, analog) if item[index] is not None]
        if values:
            upper[index] = round(max(values), 4)
            lower[index] = round(min(values), 4)


def _adjust_short_horizon_summary(simulated_symbol: dict[str, Any], sign: float, shock: float) -> None:
    summary = simulated_symbol.get("horizon_summary") or {}
    row = summary.get("3d")
    if not isinstance(row, dict):
        return
    row["expected_return"] = _round_return((_float_or_none(row.get("expected_return")) or 0.0) + sign * shock * 0.45)
    up = _float_or_none(row.get("up_probability")) or 0.5
    down = _float_or_none(row.get("down_probability")) or 0.5
    if sign > 0:
        up = _clip(up + shock * 4.0, 0.0, 0.95)
        down = _clip(down - shock * 2.5, 0.0, 0.95)
    else:
        down = _clip(down + shock * 4.0, 0.0, 0.95)
        up = _clip(up - shock * 2.5, 0.0, 0.95)
    total = up + down
    if total > 1.0:
        up, down = up / total, down / total
    row["up_probability"] = round(up, 4)
    row["down_probability"] = round(down, 4)
    row["risk_note"] = f"{row.get('risk_note', '')} News/Event overlay adjusted short-term probability path; not a guaranteed forecast.".strip()


def _apply_news_event_risk_warning(
    simulated_symbol: dict[str, Any],
    overview_symbol: dict[str, Any],
    intelligence_v4: dict[str, Any],
    symbol: str,
) -> None:
    existing = copy.deepcopy(simulated_symbol.get("market_edge_status") or {})
    if not existing:
        existing = copy.deepcopy((intelligence_v4.get("edge_status_by_symbol") or {}).get(symbol) or {})
    existing.update(
        {
            "market_edge_status": "RISK_WARNING",
            "has_usable_prediction_edge_today": False,
            "risk_warning": True,
            "summary": "重大 risk-off 新闻已被价格反应确认，风险路径权重上升；这不是交易建议。",
        }
    )
    for target in (simulated_symbol, overview_symbol):
        target["market_edge_status"] = copy.deepcopy(existing)
    (intelligence_v4.setdefault("edge_status_by_symbol", {}))[symbol] = copy.deepcopy(existing)


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


def _breadth_impact_report(
    without_true_breadth: dict[str, Any],
    with_true_breadth: dict[str, Any],
    paths_without_true_breadth: dict[str, Any],
    paths_with_true_breadth: dict[str, Any],
) -> dict[str, Any]:
    before_quality = without_true_breadth.get("data_quality_report", {}).get("summary", {})
    after_quality = with_true_breadth.get("data_quality_report", {}).get("summary", {})
    high_confidence = with_true_breadth.get("high_confidence_edge_report") or {}
    breadth_forward = high_confidence.get("breadth_forward_validation") or {}
    symbols: dict[str, Any] = {}
    changed = 0
    supports = 0
    conflicts = 0
    for symbol in SYMBOLS:
        before_path = paths_without_true_breadth.get("symbols", {}).get(symbol, {})
        after_path = paths_with_true_breadth.get("symbols", {}).get(symbol, {})
        before_edge = without_true_breadth.get("edge_status_by_symbol", {}).get(symbol, {})
        after_edge = with_true_breadth.get("edge_status_by_symbol", {}).get(symbol, {})
        before_predictors = without_true_breadth.get("predictor_outputs_by_symbol", {}).get(symbol, {})
        after_predictors = with_true_breadth.get("predictor_outputs_by_symbol", {}).get(symbol, {})
        before_rank = before_path.get("scenario_ranking", {})
        after_rank = after_path.get("scenario_ranking", {})
        before_confirmation = without_true_breadth.get("signal_confirmation_by_symbol", {}).get(symbol, {})
        after_confirmation = with_true_breadth.get("signal_confirmation_by_symbol", {}).get(symbol, {})
        before_confidence = without_true_breadth.get("model_confidence_by_symbol", {}).get(symbol, {})
        after_confidence = with_true_breadth.get("model_confidence_by_symbol", {}).get(symbol, {})
        features = after_path.get("feature_snapshot_v3") or {}
        breadth = features.get("breadth") or {}
        resonance = after_path.get("internal_resonance") or {}
        support = _score01_local(breadth.get("breadth_confirmation_score"), _score01_local(breadth.get("breadth_improvement_score")))
        conflict = _score01_local(breadth.get("breadth_conflict_score"), _score01_local(breadth.get("breadth_deterioration_score")))
        primary_scenario = after_rank.get("primary_scenario") or (after_rank.get("primary") or {}).get("scenario")
        supports_primary = support >= 0.55 and conflict < 0.55
        conflicts_primary = conflict >= 0.55 or resonance.get("resonance_state") == "surface_only"
        before_failed = float((before_predictors.get("downside_continuation_predictor") or {}).get("probability") or 0.0)
        after_failed = float((after_predictors.get("downside_continuation_predictor") or {}).get("probability") or 0.0)
        before_risk = float((before_predictors.get("risk_expansion_predictor") or {}).get("probability") or 0.0)
        after_risk = float((after_predictors.get("risk_expansion_predictor") or {}).get("probability") or 0.0)
        row = {
            "symbol": symbol,
            "baseline": "without_true_breadth_provider",
            "edge_status_without_breadth": before_edge.get("market_edge_status"),
            "edge_status_with_breadth": after_edge.get("market_edge_status"),
            "edge_status_changed": before_edge.get("market_edge_status") != after_edge.get("market_edge_status"),
            "primary_scenario_without_breadth": before_rank.get("primary_scenario"),
            "primary_scenario_with_breadth": after_rank.get("primary_scenario"),
            "primary_scenario_changed": before_rank.get("primary_scenario") != after_rank.get("primary_scenario"),
            "secondary_scenario_without_breadth": before_rank.get("secondary_scenario"),
            "secondary_scenario_with_breadth": after_rank.get("secondary_scenario"),
            "secondary_scenario_changed": before_rank.get("secondary_scenario") != after_rank.get("secondary_scenario"),
            "failed_bounce_risk_without_breadth": round(before_failed, 4),
            "failed_bounce_risk_with_breadth": round(after_failed, 4),
            "failed_bounce_risk_delta": round(after_failed - before_failed, 4),
            "risk_expansion_without_breadth": round(before_risk, 4),
            "risk_expansion_with_breadth": round(after_risk, 4),
            "risk_expansion_delta": round(after_risk - before_risk, 4),
            "signal_confirmation_without_breadth": before_confirmation.get("confirmation_score"),
            "signal_confirmation_with_breadth": after_confirmation.get("confirmation_score"),
            "signal_confirmation_delta": (after_confirmation.get("confirmation_score") or 0) - (before_confirmation.get("confirmation_score") or 0),
            "model_confidence_without_breadth": before_confidence.get("confidence_score"),
            "model_confidence_with_breadth": after_confidence.get("confidence_score"),
            "model_confidence_delta": (after_confidence.get("confidence_score") or 0) - (before_confidence.get("confidence_score") or 0),
            "breadth_supports_primary_scenario": supports_primary,
            "breadth_conflicts_primary_scenario": conflicts_primary,
            "breadth_confirmation_score": round(support * 100.0, 2),
            "breadth_conflict_score": round(conflict * 100.0, 2),
            "internal_resonance_score": resonance.get("resonance_score"),
            "internal_resonance_state": resonance.get("resonance_state"),
            "broad_participation": bool(resonance.get("broad_participation")),
            "breadth_reason": _breadth_reason(symbol, primary_scenario, support, conflict, resonance, breadth),
            "breadth_risk_note": _breadth_risk_note(symbol, support, conflict, resonance, after_failed),
        }
        if row["edge_status_changed"] or row["primary_scenario_changed"] or row["secondary_scenario_changed"] or abs(row["failed_bounce_risk_delta"]) >= 0.01:
            changed += 1
        supports += int(supports_primary)
        conflicts += int(conflicts_primary)
        symbols[symbol] = row
    return {
        "version": "breadth_impact_audit_v1",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "status": "information_quality_audit_forward_validation_pending",
        "summary": {
            "data_completeness_without_true_breadth": before_quality.get("data_completeness_score"),
            "data_completeness_with_true_breadth": after_quality.get("data_completeness_score"),
            "changed_symbol_count": changed,
            "breadth_supports_primary_count": supports,
            "breadth_conflicts_primary_count": conflicts,
            "forward_validation_status": breadth_forward.get("status") or "not_enough_forward_samples",
            "conclusion": "breadth improves information quality, not proven alpha yet.",
        },
        "symbols": symbols,
        "forward_validation": {
            "status": breadth_forward.get("status") or "not_enough_forward_samples",
            "completed_sample_counter": breadth_forward.get("completed_sample_counter"),
            "breadth_confirmed_bounce_signals": breadth_forward.get("breadth_confirmed_bounce_signals"),
            "breadth_conflicted_bounce_signals": breadth_forward.get("breadth_conflicted_bounce_signals"),
            "breadth_confirmed_reversal_signals": breadth_forward.get("breadth_confirmed_reversal_signals"),
            "breadth_conflicted_reversal_signals": breadth_forward.get("breadth_conflicted_reversal_signals"),
            "evidence_note": breadth_forward.get("evidence_note") or "not_enough_forward_samples",
        },
        "notes": [
            "This audit compares the same run with true breadth provider disabled vs enabled.",
            "The audit does not change Alpha v1 and does not prove tradable alpha.",
            "Forward validation is required before treating breadth-confirmed signals as a proven edge.",
        ],
    }


def _score01_local(value: Any, default: float = 0.0) -> float:
    parsed = _float_or_none(value)
    if parsed is None:
        return default
    if parsed > 1.0:
        parsed = parsed / 100.0
    return min(1.0, max(0.0, parsed))


def _breadth_reason(symbol: str, primary_scenario: str | None, support: float, conflict: float, resonance: dict[str, Any], breadth: dict[str, Any]) -> str:
    state = resonance.get("resonance_state") or "unknown"
    above20 = _float_or_none(breadth.get("percent_above_20d"))
    above50 = _float_or_none(breadth.get("percent_above_50d"))
    if support >= 0.65 and conflict < 0.55:
        return f"{symbol} breadth supports {primary_scenario}: internal resonance is {state}, support score {support:.0%}, above 20d/50d MA {above20:.0%}/{above50:.0%}." if above20 is not None and above50 is not None else f"{symbol} breadth supports {primary_scenario}: internal resonance is {state}, support score {support:.0%}."
    if conflict >= 0.55:
        return f"{symbol} breadth conflicts with {primary_scenario}: conflict score {conflict:.0%}, internal resonance is {state}."
    return f"{symbol} breadth is mixed for {primary_scenario}: support score {support:.0%}, conflict score {conflict:.0%}, internal resonance is {state}."


def _breadth_risk_note(symbol: str, support: float, conflict: float, resonance: dict[str, Any], failed_bounce: float) -> str:
    if resonance.get("surface_strength_without_participation"):
        return f"{symbol} index strength may be surface-only; failed-bounce risk should remain capped higher until participation broadens."
    if conflict >= 0.55 or failed_bounce >= 0.55:
        return f"{symbol} breadth conflict or failed-bounce risk is elevated; watch new lows, percent above 20/50d MA and sector participation."
    if support >= 0.65:
        return f"{symbol} breadth improves confidence in the primary path, but forward validation is still required."
    return f"{symbol} breadth is useful context but not strong enough to validate the primary path by itself."


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


def _write_options_status_report(path: Path, bundle: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_options_status_markdown(bundle), encoding="utf-8")


def _write_flow_status_report(path: Path, bundle: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_flow_positioning_status_markdown(bundle), encoding="utf-8")


def _write_forecast_accuracy_scorecard_report(path: Path, scorecard: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_forecast_accuracy_scorecard_markdown(scorecard), encoding="utf-8")


def _write_historical_replay_benchmark_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_historical_replay_benchmark_markdown(report), encoding="utf-8")


def _write_breadth_impact_status_report(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# Breadth Impact Audit",
        "",
        f"Generated at: `{report.get('generated_at')}`",
        "",
        "## Summary",
        "",
    ]
    summary = report.get("summary") or {}
    for key in (
        "data_completeness_without_true_breadth",
        "data_completeness_with_true_breadth",
        "changed_symbol_count",
        "breadth_supports_primary_count",
        "breadth_conflicts_primary_count",
        "forward_validation_status",
        "conclusion",
    ):
        lines.append(f"- {key}: `{summary.get(key)}`")
    lines.extend(
        [
            "",
            "## Symbol Impact",
            "",
            "| symbol | supports primary | conflicts primary | edge before | edge after | primary before | primary after | failed bounce delta | confirmation delta | confidence delta | reason | risk note |",
            "|---|---:|---:|---|---|---|---|---:|---:|---:|---|---|",
        ]
    )
    for symbol in SYMBOLS:
        row = (report.get("symbols") or {}).get(symbol, {})
        lines.append(
            "| "
            + " | ".join(
                [
                    symbol,
                    str(row.get("breadth_supports_primary_scenario")),
                    str(row.get("breadth_conflicts_primary_scenario")),
                    str(row.get("edge_status_without_breadth")),
                    str(row.get("edge_status_with_breadth")),
                    str(row.get("primary_scenario_without_breadth")),
                    str(row.get("primary_scenario_with_breadth")),
                    str(row.get("failed_bounce_risk_delta")),
                    str(row.get("signal_confirmation_delta")),
                    str(row.get("model_confidence_delta")),
                    str(row.get("breadth_reason")),
                    str(row.get("breadth_risk_note")),
                ]
            )
            + " |"
        )
    forward = report.get("forward_validation") or {}
    lines.extend(
        [
            "",
            "## Forward Validation",
            "",
            f"- status: `{forward.get('status')}`",
            f"- evidence_note: `{forward.get('evidence_note')}`",
            "",
            "## Guardrail",
            "",
            "- Breadth improves information quality, not proven alpha yet.",
            "- If completed samples are insufficient, keep status as not_enough_forward_samples.",
            "- Alpha v1 threshold remains frozen at 0.32534311.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _load_price_history(series_by_symbol: dict[str, DownloadedSeries] | None = None, window: int = PAST_WINDOW) -> dict[str, list[dict[str, Any]]]:
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
                "high": _float_or_none(row.get("high")) or float(row["close"]),
                "low": _float_or_none(row.get("low")) or float(row["close"]),
                "volume": _float_or_none(row.get("volume")),
                "source": series.source,
            }
            for row in series.rows
            if row.get("date") and float(row.get("close") or 0.0) > 0
        ]
        history[series.symbol] = clean_rows[-window:]
    return history


def _attach_forecast_price_levels(
    market_overview: dict[str, Any],
    simulated_paths: dict[str, Any],
    forecast_price_levels: dict[str, Any],
) -> None:
    for symbol, payload in (forecast_price_levels.get("symbols") or {}).items():
        if symbol in (simulated_paths.get("symbols") or {}):
            simulated_paths["symbols"][symbol]["forecast_price_levels"] = payload
        if symbol in (market_overview.get("symbols") or {}):
            market_overview["symbols"][symbol]["forecast_price_levels_summary"] = payload.get("summary")


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
        "dashboard_status": "forecast_validation",
        "status_note": "Alpha v1 is still a research candidate and only a bounce scenario input. The dashboard is for probability-path forecasting, not execution recommendations.",
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


def _apply_news_event_quality(data_quality: dict[str, Any], news_event_bundle: dict[str, Any]) -> None:
    summary = data_quality.setdefault("summary", {})
    coverage = data_quality.setdefault("coverage_categories", {})
    sources = data_quality.setdefault("sources", {})
    status = news_event_bundle.get("status") or "missing"
    raw_count = int(news_event_bundle.get("raw_item_count") or 0)
    major_count = int(news_event_bundle.get("major_event_count") or 0)
    provider_failed = bool(news_event_bundle.get("provider_failed"))
    reaction = news_event_bundle.get("price_reaction_confirmation") or {}
    narrative = news_event_bundle.get("market_narrative") or {}
    source_status = "available" if major_count > 0 and not provider_failed else "partial" if raw_count > 0 and not provider_failed else "provider_failed" if provider_failed else "missing"
    missing_reason = (
        "provider_failed"
        if provider_failed
        else "no_major_event_detected"
        if raw_count > 0 and major_count == 0
        else "no_news_items"
        if raw_count == 0
        else None
    )
    news_event_quality = {
        "available": major_count > 0 and not provider_failed,
        "status": source_status,
        "provider": "finnhub+gdelt",
        "headline_count": raw_count,
        "major_event_count": major_count,
        "stale": bool(news_event_bundle.get("stale")),
        "last_update": news_event_bundle.get("generated_at"),
        "event_detection_confidence": news_event_bundle.get("event_detection_confidence"),
        "price_reaction_confirmed": bool(reaction.get("price_reaction_confirmed")),
        "missing_reason": missing_reason,
        "news_event_partial": raw_count > 0 and major_count == 0 and not provider_failed,
        "event_risk_level": news_event_bundle.get("event_risk_level"),
        "news_direction": news_event_bundle.get("news_direction"),
    }
    coverage["news"] = {
        "status": source_status,
        "detail": "News/Event Intelligence: Finnhub/GDELT headlines. Full availability requires major event recognition and price-reaction confirmation.",
        "expected_items": 4,
        "available_items": 4 if major_count else 2 if raw_count else 0,
        "real_data": raw_count > 0 and not provider_failed,
        "proxy_used": False,
        "fallback_used": bool(news_event_bundle.get("stale")),
    }
    coverage["news_event"] = {
        "status": source_status,
        "detail": "Event classification, narrative detection, economic calendar risk and market price-reaction confirmation.",
        "expected_items": 5,
        "available_items": 5 if major_count else 3 if raw_count else 0,
        "real_data": raw_count > 0 and not provider_failed,
        "proxy_used": False,
        "fallback_used": bool(news_event_bundle.get("stale")),
        "headline_count": raw_count,
        "major_event_count": major_count,
    }
    sources["news_event_provider"] = {
        "symbol": "news_event_provider",
        "source": "finnhub+gdelt",
        "status": source_status,
        "rows": raw_count,
        "latest_date": data_quality.get("as_of") or summary.get("latest_date"),
        "real_data": raw_count > 0 and not provider_failed,
        "fallback_used": bool(news_event_bundle.get("stale")),
        "stale_data": bool(news_event_bundle.get("stale")),
        "missing_data": raw_count == 0 or provider_failed,
        "point_in_time_safe": True,
        "major_event_count": major_count,
        "narrative": narrative.get("market_narrative"),
        "event_detection_confidence": news_event_bundle.get("event_detection_confidence"),
        "price_reaction_confirmed": bool(reaction.get("price_reaction_confirmed")),
        "missing_reason": missing_reason,
    }
    summary["news_event"] = news_event_quality
    summary["news_event_available"] = major_count > 0 and not provider_failed
    summary["news_event_partial"] = raw_count > 0 and major_count == 0 and not provider_failed
    summary["news_event_provider_failed"] = provider_failed
    summary["news_event_major_count"] = major_count
    summary["news_event_narrative"] = narrative.get("market_narrative")
    summary["news_event_price_confirmed"] = bool(reaction.get("price_reaction_confirmed"))
    summary["news_event_event_risk_level"] = news_event_bundle.get("event_risk_level")
    summary["news_event_missing_reason"] = missing_reason
    if raw_count > 0 and not provider_failed:
        current_score = float(summary.get("data_completeness_score") or 0)
        summary["data_completeness_score_before_news_event"] = current_score
        summary["data_completeness_score"] = min(100, round(current_score + (2 if major_count else 1), 2))
        unavailable = set(summary.get("unavailable_categories") or [])
        unavailable.discard("news")
        summary["unavailable_categories"] = sorted(unavailable)


def _attach_news_event_intelligence(
    overview: dict[str, Any],
    simulated_paths: dict[str, Any],
    news_event_bundle: dict[str, Any],
) -> None:
    summary = {
        "status": news_event_bundle.get("status"),
        "validation_type": news_event_bundle.get("validation_type"),
        "dashboard_note": news_event_bundle.get("dashboard_note"),
        "market_narrative": news_event_bundle.get("market_narrative"),
        "price_reaction_confirmation": news_event_bundle.get("price_reaction_confirmation"),
        "economic_calendar_risk": news_event_bundle.get("economic_calendar_risk"),
        "event_risk_level": news_event_bundle.get("event_risk_level"),
        "news_direction": news_event_bundle.get("news_direction"),
        "major_event_count": news_event_bundle.get("major_event_count"),
        "prediction_logic_effect": news_event_bundle.get("prediction_logic_effect"),
    }
    overview["news_event_summary"] = summary
    simulated_paths["news_event_summary"] = summary
    impacts = news_event_bundle.get("symbol_impacts") or {}
    for symbol in SYMBOLS:
        impact = impacts.get(symbol, {})
        overview_symbol = (overview.get("symbols") or {}).get(symbol)
        simulated_symbol = (simulated_paths.get("symbols") or {}).get(symbol)
        patch_payload = {
                "status": news_event_bundle.get("status"),
                "validation_type": news_event_bundle.get("validation_type"),
                "dashboard_note": news_event_bundle.get("dashboard_note"),
                "market_narrative": news_event_bundle.get("market_narrative"),
                "price_reaction_confirmation": news_event_bundle.get("price_reaction_confirmation"),
                "economic_calendar_risk": news_event_bundle.get("economic_calendar_risk"),
                "event_risk_level": news_event_bundle.get("event_risk_level"),
                "news_direction": news_event_bundle.get("news_direction"),
                "symbol_impact": impact,
                "prediction_logic_effect": ((news_event_bundle.get("prediction_logic_effect") or {}).get("symbols") or {}).get(symbol),
                "major_events": (news_event_bundle.get("major_events") or [])[:6],
        }
        if isinstance(overview_symbol, dict):
            overview_symbol["news_event_intelligence"] = {
                **(overview_symbol.get("news_event_intelligence") or {}),
                **patch_payload,
            }
        if isinstance(simulated_symbol, dict):
            simulated_symbol["news_event_intelligence"] = {
                **(simulated_symbol.get("news_event_intelligence") or {}),
                **patch_payload,
            }


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


def _round_return(value: float | None) -> float | None:
    return round(value, 4) if value is not None and math.isfinite(value) else None


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


def _write_forecast_price_levels_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_forecast_price_levels_markdown(payload), encoding="utf-8")


def _write_price_volume_structure_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_price_volume_structure_markdown(payload), encoding="utf-8")


def _write_confluence_score_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_confluence_score_markdown(payload), encoding="utf-8")


def _write_market_alerts_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_market_alerts_markdown(payload), encoding="utf-8")


def _write_news_event_status_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_news_event_status_markdown(payload), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
