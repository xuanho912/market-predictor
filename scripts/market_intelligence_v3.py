from __future__ import annotations

import csv
import json
import math
import statistics
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from app.services.data_providers.auto_download import DownloadedSeries, is_real_market_data
from scripts.market_intelligence_v2 import build_period_specific_analog_support
from scripts.providers.fred_provider import DEFAULT_FRED_SERIES, fetch_fred_bundle


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TARGET_SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
HORIZONS = (3, 5, 10, 20, 60)
V3_MARKET_SYMBOLS = (
    "^VIX9D",
    "^VIX3M",
    "^VIX6M",
    "^VVIX",
    "^SKEW",
    "RSP",
    "SPHB",
    "SPLV",
    "XLC",
    "XLY",
    "XLP",
    "XLE",
    "XLF",
    "XLV",
    "XLI",
    "XLK",
    "XLB",
    "XLU",
    "XLRE",
)
FRED_SERIES = DEFAULT_FRED_SERIES


@dataclass(frozen=True)
class FredSeries:
    name: str
    series_id: str
    rows: list[dict[str, float | str]]
    source: str
    real_data: bool


def build_market_intelligence_v3(
    *,
    series_by_symbol: dict[str, DownloadedSeries],
    overview: dict[str, Any],
    simulated_paths: dict[str, Any],
    analogs: dict[str, dict[str, Any]],
    prior_intelligence: dict[str, Any],
    finnhub_bundle: dict[str, Any] | None = None,
    fred_bundle: dict[str, Any] | None = None,
    breadth_bundle: dict[str, Any] | None = None,
    options_bundle: dict[str, Any] | None = None,
    flow_bundle: dict[str, Any] | None = None,
) -> dict[str, Any]:
    finnhub_bundle = finnhub_bundle or _empty_finnhub_bundle()
    fred_bundle = fred_bundle or fetch_fred_bundle()
    fred_series = load_fred_series_bundle(fred_bundle=fred_bundle)
    feature_snapshot = build_feature_snapshot_v3(series_by_symbol, fred_series, finnhub_bundle, breadth_bundle=breadth_bundle, options_bundle=options_bundle, flow_bundle=flow_bundle)
    data_quality = build_data_quality_report_v3(series_by_symbol, fred_series, feature_snapshot, overview.get("as_of"), finnhub_bundle, breadth_bundle=breadth_bundle, options_bundle=options_bundle, flow_bundle=flow_bundle)
    model_confidence_by_symbol: dict[str, Any] = {}
    predictor_outputs_by_symbol: dict[str, Any] = {}
    signal_agreement_by_symbol: dict[str, Any] = {}
    edge_status_by_symbol: dict[str, Any] = {}

    for symbol in TARGET_SYMBOLS:
        overview_symbol = overview.get("symbols", {}).get(symbol, {})
        simulated_symbol = simulated_paths.get("symbols", {}).get(symbol, {})
        if not overview_symbol or not simulated_symbol:
            continue

        analog = analogs.get(symbol, {})
        analog_support = simulated_symbol.get("historical_support_by_horizon") or build_period_specific_analog_support(analog)
        features = feature_snapshot["symbols"].get(symbol, {})
        signal_agreement = build_signal_agreement_score(
            overview_symbol=overview_symbol,
            analog_support=analog_support,
            features=features,
            data_quality=data_quality,
        )
        predictors = build_predictors(
            overview_symbol=overview_symbol,
            analog_support=analog_support,
            features=features,
            signal_agreement=signal_agreement,
            data_quality=data_quality,
        )
        confidence = enhance_model_confidence(
            prior_confidence=simulated_symbol.get("model_confidence") or overview_symbol.get("model_confidence") or {},
            data_quality=data_quality,
            signal_agreement=signal_agreement,
            predictors=predictors,
            analog_support=analog_support,
        )
        edge_status = build_market_edge_status(
            data_quality=data_quality,
            signal_agreement=signal_agreement,
            confidence=confidence,
            analog_support=analog_support,
            overview_symbol=overview_symbol,
            predictors=predictors,
        )
        path_weight_model = build_path_weight_model(
            overview_symbol=overview_symbol,
            signal_agreement=signal_agreement,
            analog_support=analog_support,
            features=features,
            data_quality=data_quality,
            predictors=predictors,
            confidence=confidence,
        )
        scenario_ranking = build_scenario_ranking(
            overview_symbol=overview_symbol,
            path_weight_model=path_weight_model,
            signal_agreement=signal_agreement,
            analog_support=analog_support,
            features=features,
            predictors=predictors,
            confidence=confidence,
        )
        horizon_predictions = enhance_horizon_predictions(
            simulated_symbol.get("prediction_horizons", {}),
            predictors,
            analog_support,
            edge_status,
        )
        judgment = build_v3_judgment(symbol, edge_status, predictors, horizon_predictions, signal_agreement, confidence)

        patch = {
            "market_intelligence_version": "v3",
            "feature_snapshot_v3": features,
            "signal_agreement": signal_agreement,
            "predictors": predictors,
            "market_edge_status": edge_status,
            "model_confidence": confidence,
            "prediction_horizons": horizon_predictions,
            "current_integrated_judgment": judgment,
            "path_weight_model": path_weight_model,
            "base_path_weight": path_weight_model["base_path_weight"],
            "bounce_path_weight": path_weight_model["bounce_path_weight"],
            "bearish_path_weight": path_weight_model["bearish_path_weight"],
            "analog_path_weight": path_weight_model["analog_path_weight"],
            "low_confidence_simulation": path_weight_model["low_confidence_simulation"],
            "scenario_ranking": scenario_ranking,
        }
        overview_symbol.update(patch)
        simulated_symbol.update(patch)
        simulated_symbol["scenario_weights"] = {
            "base_scenario": path_weight_model["base_path_weight"],
            "bounce_scenario": path_weight_model["bounce_path_weight"],
            "bearish_scenario": path_weight_model["bearish_path_weight"],
            "historical_analog_average": path_weight_model["analog_path_weight"],
        }
        simulated_symbol["path_confidence"] = path_weight_model["simulation_confidence_level"]
        _update_scenario_card_weights_v3(simulated_symbol, path_weight_model)
        model_confidence_by_symbol[symbol] = confidence
        predictor_outputs_by_symbol[symbol] = predictors
        signal_agreement_by_symbol[symbol] = signal_agreement
        edge_status_by_symbol[symbol] = edge_status

    overview["data_quality_summary"] = data_quality["summary"]
    overview["model_confidence_by_symbol"] = model_confidence_by_symbol
    overview["signal_agreement_by_symbol"] = signal_agreement_by_symbol
    overview["edge_status_by_symbol"] = edge_status_by_symbol
    simulated_paths["data_quality_summary"] = data_quality["summary"]

    high_confidence_report = build_high_confidence_signal_report(analogs, simulated_paths)
    return {
        "version": "market_intelligence_engine_v3",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "data_quality_report": data_quality,
        "feature_snapshot_v3": feature_snapshot,
        "signal_agreement_by_symbol": signal_agreement_by_symbol,
        "predictor_outputs_by_symbol": predictor_outputs_by_symbol,
        "model_confidence_by_symbol": model_confidence_by_symbol,
        "edge_status_by_symbol": edge_status_by_symbol,
        "high_confidence_signal_report": high_confidence_report,
        "finnhub_status": _finnhub_status_summary(finnhub_bundle),
        "fred_status": _fred_bundle_summary(fred_bundle),
        "breadth_status": _breadth_bundle_summary(breadth_bundle),
        "options_status": _options_bundle_summary(options_bundle),
        "flow_status": _flow_bundle_summary(flow_bundle),
        "warnings": [
            "Alpha v1 threshold remains frozen at 0.32534311.",
            "True breadth is used when SPY/QQQ/DIA constituent data is available; IWM remains explicitly proxy-only.",
            "Options structure is partial unless VIX term plus VVIX/SKEW are available; put/call and gamma remain missing until real feeds exist.",
            "NO_EDGE is allowed and preferred when signals conflict or data is insufficient.",
        ],
        "prior_engine": prior_intelligence.get("version", "market_intelligence_engine_v2"),
    }


def load_fred_series_bundle(lookback_days: int = 1800, fred_bundle: dict[str, Any] | None = None) -> dict[str, FredSeries]:
    if fred_bundle is None:
        fred_bundle = fetch_fred_bundle(lookback_days=lookback_days)
    series_payloads = fred_bundle.get("series") or {}
    converted: dict[str, FredSeries] = {}
    for name, series_id in FRED_SERIES.items():
        payload = series_payloads.get(name) or {}
        rows = list(payload.get("rows") or [])[-lookback_days:]
        converted[name] = FredSeries(
            name=name,
            series_id=str(payload.get("series_id") or series_id),
            rows=rows,
            source=str(payload.get("source") or "missing"),
            real_data=bool(payload.get("real_data")) and bool(rows),
        )
    return converted


def load_fred_series(name: str, series_id: str, lookback_days: int) -> FredSeries:
    cache = _fred_cache_file(series_id)
    try:
        url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        text = urllib.request.urlopen(request, timeout=20).read().decode("utf-8")
        rows = _parse_fred_csv(text, lookback_days)
        if rows:
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(json.dumps({"series_id": series_id, "rows": rows}, ensure_ascii=False), encoding="utf-8")
            return FredSeries(name=name, series_id=series_id, rows=rows, source="fred", real_data=True)
    except Exception:
        pass
    if cache.exists():
        payload = json.loads(cache.read_text(encoding="utf-8"))
        rows = list(payload.get("rows", []))[-lookback_days:]
        if rows:
            return FredSeries(name=name, series_id=series_id, rows=rows, source="local-cache-fred", real_data=True)
    return FredSeries(name=name, series_id=series_id, rows=[], source="missing", real_data=False)


def build_feature_snapshot_v3(
    series_by_symbol: dict[str, DownloadedSeries],
    fred_series: dict[str, FredSeries],
    finnhub_bundle: dict[str, Any],
    breadth_bundle: dict[str, Any] | None = None,
    options_bundle: dict[str, Any] | None = None,
    flow_bundle: dict[str, Any] | None = None,
) -> dict[str, Any]:
    closes = {symbol: _closes(series_by_symbol.get(symbol)) for symbol in set(TARGET_SYMBOLS + V3_MARKET_SYMBOLS + ("^VIX", "HYG", "LQD", "TLT", "UUP", "^TNX"))}
    volumes = {symbol: _volumes(series_by_symbol.get(symbol)) for symbol in closes}
    fred = {name: _fred_values(series) for name, series in fred_series.items()}
    sector_symbols = ("XLC", "XLY", "XLP", "XLE", "XLF", "XLV", "XLI", "XLK", "XLB", "XLU", "XLRE")
    sector_closes = {symbol: closes.get(symbol, []) for symbol in sector_symbols}

    vix = closes.get("^VIX", [])
    vix9d = closes.get("^VIX9D", [])
    vix3m = closes.get("^VIX3M", [])
    vix6m = closes.get("^VIX6M", [])
    vvix = closes.get("^VVIX", [])
    skew = closes.get("^SKEW", [])
    hyg = closes.get("HYG", [])
    lqd = closes.get("LQD", [])
    tlt = closes.get("TLT", [])
    uup = closes.get("UUP", [])
    rsp = closes.get("RSP", [])
    spy = closes.get("SPY", [])
    sphb = closes.get("SPHB", [])
    splv = closes.get("SPLV", [])

    symbols: dict[str, Any] = {}
    for symbol in TARGET_SYMBOLS:
        target = closes.get(symbol, [])
        target_volume = volumes.get(symbol, [])
        finnhub_symbol = _finnhub_symbol_snapshot(finnhub_bundle, symbol)
        breadth = _breadth_from_bundle(symbol, breadth_bundle) or _breadth_proxy(sector_closes, rsp, spy)
        flow = _flow_from_bundle(symbol, flow_bundle) or _flow_proxy(target_volume, target, sphb, splv, sector_closes)
        credit = _credit_snapshot(hyg, lqd, fred)
        rates = _rates_snapshot(tlt, uup, fred)
        volatility = _volatility_snapshot(vix, vix9d, vix3m, vix6m, vvix, skew)
        volatility.update(_options_from_bundle(symbol, options_bundle))
        market_structure = _market_structure_snapshot(closes, sector_closes)
        macro_calendar = _macro_event_calendar_snapshot()
        fallback_macro_risk = bool(macro_calendar.get("macro_event_risk_flag"))
        finnhub_macro = _finnhub_macro_snapshot(finnhub_bundle)
        macro_calendar.update(finnhub_macro)
        macro_calendar["fallback_macro_event_risk_flag"] = fallback_macro_risk
        macro_calendar["macro_event_risk_flag"] = fallback_macro_risk or bool(finnhub_macro.get("macro_event_risk_flag"))
        news = _finnhub_news_snapshot(finnhub_bundle)
        rates["rates_pressure_score"] = _clip((rates.get("liquidity_stress_proxy") or 0.0) * 0.65 + (0.15 if macro_calendar.get("macro_event_risk_flag") else 0.0), 0.0, 1.0)
        symbols[symbol] = {
            "price": {
                "current_price": _last(target),
                "return_20d": _return(target, 20),
                "return_60d": _return(target, 60),
                "drawdown_depth": _drawdown(target, 60),
                "rsi_14": _rsi(target, 14),
                "realized_vol_20d": _realized_vol(target, 20),
                "volume_zscore_20d": _zscore_last(target_volume, 20),
            },
            "volatility_options": volatility,
            "breadth": breadth,
            "credit": credit,
            "rates_liquidity": rates,
            "market_structure": market_structure,
            "macro_event_calendar": macro_calendar,
            "flow_positioning_proxy": flow,
            "news": news,
            "daily_market_brief": _daily_market_brief(symbol, finnhub_symbol, news, macro_calendar, rates),
            "finnhub": finnhub_symbol,
        }

    return {
        "version": "market_intelligence_engine_v3_features",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "symbols": symbols,
    }


def build_data_quality_report_v3(
    series_by_symbol: dict[str, DownloadedSeries],
    fred_series: dict[str, FredSeries],
    feature_snapshot: dict[str, Any],
    as_of: str | None,
    finnhub_bundle: dict[str, Any],
    breadth_bundle: dict[str, Any] | None = None,
    options_bundle: dict[str, Any] | None = None,
    flow_bundle: dict[str, Any] | None = None,
) -> dict[str, Any]:
    market_required = set(TARGET_SYMBOLS + ("^VIX", "HYG", "LQD", "TLT", "UUP", "^TNX") + V3_MARKET_SYMBOLS)
    source_rows: dict[str, Any] = {}
    latest_dates: list[str] = []
    for symbol in sorted(market_required):
        series = series_by_symbol.get(symbol)
        latest = _latest_date(series)
        if latest:
            latest_dates.append(latest)
        source_rows[symbol] = _market_source_status(symbol, series, latest)
    for name, series in sorted(fred_series.items()):
        latest = _latest_fred_date(series)
        if latest:
            latest_dates.append(latest)
        source_rows[name] = _fred_source_status(name, series, latest)
    source_rows.update(_finnhub_source_rows(finnhub_bundle))
    source_rows.update(_breadth_source_rows(breadth_bundle))
    source_rows.update(_options_source_rows(options_bundle))
    source_rows.update(_flow_source_rows(flow_bundle))

    reference_date = max(latest_dates) if latest_dates else as_of
    for row in source_rows.values():
        provider_stale = bool(row.get("stale_data"))
        row["stale_data"] = False if row.get("missing_data") else provider_stale or _is_stale(row.get("latest_date"), reference_date, max_days=10 if row.get("source") in {"fred-api", "fred-public-csv", "local-cache-fred"} else 5)
        if row["stale_data"] and row["status"] == "available":
            row["status"] = "stale"

    macro_status = {
        "symbol": "macro_event_calendar",
        "source": "deterministic_calendar_fallback",
        "status": "fallback",
        "rows": 1,
        "latest_date": reference_date,
        "real_data": False,
        "fallback_used": True,
        "stale_data": False,
        "missing_data": False,
        "point_in_time_safe": True,
        "detail": "CPI/FOMC/NFP/options-expiry/month-end flags are rule-based calendar approximations.",
    }
    source_rows["macro_event_calendar"] = macro_status

    coverage = _coverage_categories_v3(source_rows, feature_snapshot)
    completeness_score = _data_completeness_score_v3(coverage, source_rows)
    unavailable = [name for name, payload in coverage.items() if payload["status"] in {"missing", "not_available"}]
    any_synthetic = any(row["source"] == "synthetic-fallback" for row in source_rows.values())
    any_fallback = any(row.get("fallback_used") for row in source_rows.values())
    any_stale = any(row.get("stale_data") for row in source_rows.values())
    any_missing = any(row.get("missing_data") for row in source_rows.values())
    real_core = all(source_rows.get(symbol, {}).get("real_data") for symbol in TARGET_SYMBOLS + ("^VIX", "HYG", "LQD", "TLT", "UUP", "^TNX"))
    finnhub_status = _finnhub_status_summary(finnhub_bundle)
    breadth_status = _breadth_bundle_summary(breadth_bundle)
    options_status = _options_bundle_summary(options_bundle)
    flow_status = _flow_bundle_summary(flow_bundle)
    yahoo_fallback_used = any(str(row.get("source", "")).startswith(("yfinance", "yahoo-chart", "local-cache-yfinance", "local-cache-yahoo-chart")) for row in source_rows.values())

    return {
        "version": "market_intelligence_engine_v3_data_quality",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "as_of": reference_date or as_of,
        "summary": {
            "data_source_status": "real_core_with_proxies" if real_core else "partial_or_failed",
            "real_market_data": real_core,
            "finnhub_available": finnhub_status["finnhub_available"],
            "finnhub_missing": finnhub_status["finnhub_missing"],
            "finnhub_rate_limited": finnhub_status["finnhub_rate_limited"],
            "yahoo_fallback_used": yahoo_fallback_used,
            "fred_required": True,
            "options_required": True,
            "breadth_required": True,
            "true_breadth_available": breadth_status["true_breadth_available"],
            "breadth_provider_available": breadth_status["provider_available"],
            "breadth_proxy_only_symbols": breadth_status["breadth_proxy_only_symbols"],
            "average_breadth_quality_score": breadth_status["average_breadth_quality_score"],
            "options_available": options_status["options_available"],
            "vix_term_available": options_status["vix_term_available"],
            "vvix_available": options_status["vvix_available"],
            "skew_available": options_status["skew_available"],
            "put_call_available": options_status["put_call_available"],
            "gamma_available": options_status["gamma_available"],
            "options_partial": options_status["options_partial"],
            "options_missing": options_status["options_missing"],
            "options_stale": options_status["options_stale"],
            "options_source": options_status["options_source"],
            "flow_required": True,
            "flow_available": flow_status["flow_available"],
            "flow_proxy_only": flow_status["flow_proxy_only"],
            "true_flow_available": flow_status["true_flow_available"],
            "average_flow_quality_score": flow_status["average_flow_quality_score"],
            "overall_flow_confirmation_score": flow_status["overall_flow_confirmation_score"],
            "overall_flow_conflict_score": flow_status["overall_flow_conflict_score"],
            "missing_real_flow_feeds": flow_status["missing_real_flow_feeds"],
            "fallback_used": any_fallback,
            "synthetic_used": any_synthetic,
            "stale_data": any_stale,
            "missing_data": any_missing,
            "data_completeness_score": completeness_score,
            "target_completeness_score": 75,
            "unavailable_categories": unavailable,
            "missing_key_sources": [name for name, row in source_rows.items() if row.get("missing_data")],
            "latest_date": reference_date,
            "quality_note": "Score includes real data plus explicitly labeled proxy/fallback categories; it is not equal to institutional-grade data coverage.",
        },
        "sources": source_rows,
        "coverage_categories": coverage,
        "notes": [
            "Flow / positioning is proxy-only unless a true fund-flow, CFTC, dealer-positioning or prime-brokerage feed is explicitly connected.",
            "Macro event risk uses rule-based calendar fallback until a real economic calendar is connected.",
            "Options coverage is partial unless real VIX term plus VVIX/SKEW are available; put/call and gamma are not inferred.",
            "Put/call ratio, gamma exposure and true fund flow remain missing unless a real feed is added.",
        ],
    }


def build_signal_agreement_score(
    *,
    overview_symbol: dict[str, Any],
    analog_support: dict[str, Any],
    features: dict[str, Any],
    data_quality: dict[str, Any],
) -> dict[str, Any]:
    supporting: list[dict[str, Any]] = []
    conflicting: list[dict[str, Any]] = []

    def add(condition: bool, bucket: list[dict[str, Any]], name: str, score: float, detail: str) -> None:
        if condition:
            bucket.append({"name": name, "score": round(score, 3), "detail": detail})

    vol = features.get("volatility_options", {})
    credit = features.get("credit", {})
    breadth = features.get("breadth", {})
    price = features.get("price", {})
    rates = features.get("rates_liquidity", {})
    flow = features.get("flow_positioning_proxy", {})
    news = features.get("news", {})
    macro = features.get("macro_event_calendar", {})
    vix_change_5d = _float_or_none(vol.get("vix_change_5d")) or 0.0
    vix_change_20d = _float_or_none(vol.get("vix_change_20d")) or 0.0
    credit_stability = _float_or_none(credit.get("credit_stabilization_score")) or 0.0
    credit_deterioration = _float_or_none(credit.get("credit_deterioration_score")) or 0.0
    breadth_score = _score01(breadth.get("breadth_improvement_score"))
    breadth_confirmation = _score01(breadth.get("breadth_confirmation_score"), breadth_score)
    breadth_conflict = _score01(breadth.get("breadth_conflict_score"))
    breadth_quality = _score01(breadth.get("breadth_quality_score"), 0.5)
    trend_20d = _float_or_none(price.get("return_20d")) or 0.0
    liquidity_stress = _float_or_none(rates.get("liquidity_stress_proxy")) or 0.0
    rates_pressure = _float_or_none(rates.get("rates_pressure_score")) or liquidity_stress
    risk_off_rotation = _score01(flow.get("risk_off_flow_score"), _score01(flow.get("risk_off_rotation_score")))
    flow_confirmation = _score01(flow.get("flow_confirmation_score"), 0.0)
    flow_conflict = _score01(flow.get("flow_conflict_score"), risk_off_rotation)
    flow_quality = _score01(flow.get("flow_quality_score"), 0.0)
    news_risk = _float_or_none(news.get("news_risk_score"))
    macro_event_risk = bool(macro.get("macro_event_risk_flag"))
    failed_bounce = float(overview_symbol.get("downside_continuation_probability") or 0.0)

    add(bool(overview_symbol.get("live_signal")), supporting, "Alpha v1 bounce signal", 0.16, "Frozen Alpha v1 is currently triggered.")
    add(analog_support.get("short_term_support") == "supportive", supporting, "short-term historical analogs", 0.13, "3d/5d/10d analogs lean positive.")
    add(analog_support.get("medium_term_support") == "supportive", supporting, "medium-term historical analogs", 0.15, "20d/60d analogs lean positive.")
    add(vix_change_5d < 0 and vix_change_20d <= 0, supporting, "VIX direction", 0.11, "Volatility is not rising on 5d/20d windows.")
    add(credit_stability > 0.45, supporting, "credit stabilization", 0.12, "Credit proxy is stable or improving.")
    add(breadth_confirmation > 0.55, supporting, "breadth confirmation", 0.13, "Constituent/proxy breadth supports the current path.")
    add(trend_20d > 0, supporting, "trend momentum", 0.08, "20d momentum is positive.")
    add(liquidity_stress < 0.40, supporting, "liquidity proxy", 0.08, "Liquidity proxy is not stressed.")
    add(news_risk is not None and news_risk < 0.35, supporting, "news risk low", 0.06, "Finnhub market-news risk score is low.")
    add(flow_confirmation > 0.58 and flow_quality >= 0.45, supporting, "flow confirmation", 0.10, "Proxy flow/positioning confirms risk appetite or participation.")

    add(analog_support.get("short_term_support") == "weak", conflicting, "short-term analog conflict", 0.16, "3d/5d/10d analogs are weak or negative.")
    add(analog_support.get("medium_term_support") == "weak", conflicting, "medium-term analog conflict", 0.15, "20d/60d analogs are weak or negative.")
    add(vix_change_5d > 0 or vix_change_20d > 0, conflicting, "VIX rising", 0.12, "Volatility is rising.")
    add(credit_deterioration > 0.45, conflicting, "credit deterioration", 0.14, "Credit proxy is deteriorating.")
    add(breadth_conflict > 0.55 or breadth_score < 0.42, conflicting, "breadth weak", 0.13, "Breadth is weak or diverging from the index.")
    add(breadth_quality < 0.45, conflicting, "breadth quality weak", 0.06, "Breadth data quality is too low for strong confirmation.")
    add(failed_bounce > 0.55, conflicting, "failed bounce risk", 0.14, "Downside continuation probability is elevated.")
    add(liquidity_stress > 0.55, conflicting, "liquidity stress", 0.12, "Liquidity proxy is stressed.")
    add(rates_pressure > 0.55, conflicting, "rates pressure", 0.10, "Rates pressure proxy is elevated.")
    add(flow_conflict > 0.55 or risk_off_rotation > 0.55, conflicting, "flow conflict", 0.11, "Proxy flow/positioning favors defensive/risk-off assets or weak participation.")
    add(flow_quality < 0.35, conflicting, "flow quality weak", 0.05, "Flow proxy coverage is too weak for high confidence.")
    add(news_risk is not None and news_risk > 0.55, conflicting, "news risk", 0.10, "Finnhub news-risk score is elevated.")
    add(macro_event_risk, conflicting, "macro event risk", 0.08, "Upcoming macro event risk is flagged.")

    support_score = sum(item["score"] for item in supporting)
    conflict_score = sum(item["score"] for item in conflicting)
    raw = 50.0 + support_score * 65.0 - conflict_score * 65.0
    completeness = float(data_quality.get("summary", {}).get("data_completeness_score") or 0.0)
    if completeness < 70:
        raw = min(raw, 62.0)
    score = int(round(_clip(raw, 0.0, 100.0)))
    level = "strong" if score >= 70 else "mixed" if score >= 45 else "weak"
    return {
        "signal_agreement_score": score,
        "agreement_level": level,
        "supporting_signals": supporting,
        "conflicting_signals": conflicting,
        "data_completeness_cap_applied": completeness < 70,
    }


def build_predictors(
    *,
    overview_symbol: dict[str, Any],
    analog_support: dict[str, Any],
    features: dict[str, Any],
    signal_agreement: dict[str, Any],
    data_quality: dict[str, Any],
) -> dict[str, Any]:
    vol = features.get("volatility_options", {})
    credit = features.get("credit", {})
    breadth = features.get("breadth", {})
    rates = features.get("rates_liquidity", {})
    price = features.get("price", {})
    flow = features.get("flow_positioning_proxy", {})
    news = features.get("news", {})
    macro = features.get("macro_event_calendar", {})
    bounce_base = float(overview_symbol.get("bounce_probability") or 0.0)
    downside_base = float(overview_symbol.get("downside_continuation_probability") or 0.0)
    reversal_base = float(overview_symbol.get("trend_reversal_probability") or 0.0)
    agreement = float(signal_agreement.get("signal_agreement_score") or 0.0) / 100.0
    data_score = float(data_quality.get("summary", {}).get("data_completeness_score") or 0.0) / 100.0
    vix_rollover = 1.0 if (_float_or_none(vol.get("vix_change_5d")) or 0.0) < 0 else 0.0
    credit_stability = _float_or_none(credit.get("credit_stabilization_score")) or 0.0
    credit_deterioration = _float_or_none(credit.get("credit_deterioration_score")) or 0.0
    breadth_improvement = _score01(breadth.get("breadth_improvement_score"))
    breadth_deterioration = _score01(breadth.get("breadth_deterioration_score"))
    breadth_confirmation = _score01(breadth.get("breadth_confirmation_score"), breadth_improvement)
    breadth_conflict = _score01(breadth.get("breadth_conflict_score"), breadth_deterioration)
    liquidity_stress = _float_or_none(rates.get("liquidity_stress_proxy")) or 0.0
    rates_pressure = _float_or_none(rates.get("rates_pressure_score")) or liquidity_stress
    trend_20d = _float_or_none(price.get("return_20d")) or 0.0
    trend_60d = _float_or_none(price.get("return_60d")) or 0.0
    risk_off_rotation = _score01(flow.get("risk_off_flow_score"), _score01(flow.get("risk_off_rotation_score")))
    flow_confirmation = _score01(flow.get("flow_confirmation_score"), 0.0)
    flow_conflict = _score01(flow.get("flow_conflict_score"), risk_off_rotation)
    flow_quality = _score01(flow.get("flow_quality_score"), 0.0)
    crowding_proxy = _score01(flow.get("crowding_proxy_score"), 0.0)
    vix_percentile = _float_or_none(vol.get("vix_percentile_1y")) or 0.5
    news_risk = _float_or_none(news.get("news_risk_score")) or 0.0
    macro_event_risk = 1.0 if macro.get("macro_event_risk_flag") else 0.0

    short_support = analog_support.get("short_term_support", "neutral")
    medium_support = analog_support.get("medium_term_support", "neutral")
    bounce_probability = _clip(
        bounce_base * 0.42
        + agreement * 0.18
        + vix_rollover * 0.08
        + credit_stability * 0.12
        + breadth_confirmation * 0.12
        + flow_confirmation * 0.06
        - flow_conflict * 0.04
        + (0.08 if short_support == "supportive" else -0.05 if short_support == "weak" else 0.0),
        0.0,
        0.95,
    )
    downside_probability = _clip(
        downside_base * 0.42
        + credit_deterioration * 0.15
        + liquidity_stress * 0.13
        + breadth_conflict * 0.10
        + flow_conflict * 0.10
        + crowding_proxy * 0.04
        + max(-trend_20d, 0.0) * 2.2
        + (0.08 if short_support == "weak" else 0.0),
        0.0,
        0.95,
    )
    reversal_probability = _clip(
        reversal_base * 0.38
        + max(trend_60d, 0.0) * 1.3
        + breadth_confirmation * 0.15
        + flow_confirmation * 0.06
        + credit_stability * 0.14
        + (0.12 if medium_support == "supportive" else -0.08 if medium_support == "weak" else 0.0),
        0.0,
        0.92,
    )
    risk_expansion_probability = _clip(
        vix_percentile * 0.22
        + credit_deterioration * 0.23
        + liquidity_stress * 0.20
        + breadth_deterioration * 0.10
        + flow_conflict * 0.14
        + crowding_proxy * 0.05
        + news_risk * 0.08
        + rates_pressure * 0.10
        + macro_event_risk * 0.05
        + max(-trend_60d, 0.0) * 1.2
        + (0.08 if analog_support.get("worst_path_risk") == "high" else 0.0),
        0.0,
        0.92,
    )

    return {
        "bounce_predictor": _predictor_payload(
            probability=bounce_probability,
            confidence=_predictor_confidence(data_score, agreement, short_support),
            main_drivers=_drivers([
                ("Alpha v1 bounce probability", bounce_base),
                ("VIX rollover", vix_rollover),
                ("credit stabilization", credit_stability),
                ("breadth confirmation", breadth_confirmation),
                ("flow confirmation", flow_confirmation),
                ("short-term analog support", 1.0 if short_support == "supportive" else 0.0),
            ]),
            invalidation_conditions=["VIX turns higher again", "HYG/LQD relative strength weakens", "price breaks the recent low", "short-term analog support remains weak"],
            historical_analog_support=short_support,
            best_horizon="3d-10d",
        ),
        "downside_continuation_predictor": _predictor_payload(
            probability=downside_probability,
            confidence=_predictor_confidence(data_score, 1.0 - agreement, "supportive" if downside_probability > 0.55 else "neutral"),
            main_drivers=_drivers([
                ("base downside continuation", downside_base),
                ("credit deterioration", credit_deterioration),
                ("liquidity stress proxy", liquidity_stress),
                ("rates pressure", rates_pressure),
                ("risk-off rotation", risk_off_rotation),
                ("flow conflict", flow_conflict),
                ("breadth conflict", breadth_conflict),
                ("negative 20d trend", max(-trend_20d, 0.0) * 6.0),
            ]),
            invalidation_conditions=["VIX falls and stays lower", "credit spreads/proxies stabilize", "breadth recovers above 50d", "price reclaims short-term trend"],
            historical_analog_support=short_support,
            best_horizon="5d-20d",
        ),
        "trend_reversal_predictor": _predictor_payload(
            probability=reversal_probability,
            confidence=_predictor_confidence(data_score, agreement, medium_support),
            main_drivers=_drivers([
                ("medium-term analog support", 1.0 if medium_support == "supportive" else 0.0),
                ("60d trend", max(trend_60d, 0.0) * 6.0),
                ("breadth confirmation", breadth_confirmation),
                ("flow confirmation", flow_confirmation),
                ("credit stabilization", credit_stability),
            ]),
            invalidation_conditions=["20d/60d analogs turn weak", "breadth rolls over", "credit deterioration resumes", "recovery fails near moving-average resistance"],
            historical_analog_support=medium_support,
            best_horizon="20d-60d",
        ),
        "risk_expansion_predictor": _predictor_payload(
            probability=risk_expansion_probability,
            confidence=_predictor_confidence(data_score, max(risk_expansion_probability, 1.0 - agreement), "supportive" if risk_expansion_probability > 0.55 else "neutral"),
            main_drivers=_drivers([
                ("VIX percentile", vix_percentile),
                ("credit deterioration", credit_deterioration),
                ("liquidity stress proxy", liquidity_stress),
                ("news risk", news_risk),
                ("macro event risk", macro_event_risk),
                ("risk-off rotation", risk_off_rotation),
                ("flow conflict", flow_conflict),
                ("breadth deterioration", breadth_deterioration),
                ("negative 60d trend", max(-trend_60d, 0.0) * 4.0),
            ]),
            invalidation_conditions=["credit proxy stabilizes", "VIX term structure normalizes", "defensive rotation fades", "risk assets regain broad participation"],
            historical_analog_support=analog_support.get("worst_path_risk", "unknown"),
            best_horizon="20d-60d",
        ),
    }


def enhance_model_confidence(
    *,
    prior_confidence: dict[str, Any],
    data_quality: dict[str, Any],
    signal_agreement: dict[str, Any],
    predictors: dict[str, Any],
    analog_support: dict[str, Any],
) -> dict[str, Any]:
    prior_score = float(prior_confidence.get("confidence_score") or 0.0)
    completeness = float(data_quality.get("summary", {}).get("data_completeness_score") or 0.0)
    agreement = float(signal_agreement.get("signal_agreement_score") or 0.0)
    predictor_spread = _predictor_spread(predictors)
    analog_score = 70.0 if analog_support.get("medium_term_support") == "supportive" else 45.0 if analog_support.get("medium_term_support") == "weak" else 55.0
    raw = prior_score * 0.20 + completeness * 0.30 + agreement * 0.28 + analog_score * 0.12 + (1.0 - predictor_spread) * 100.0 * 0.10
    if completeness < 70:
        raw = min(raw, 64.0)
    if signal_agreement.get("agreement_level") == "weak":
        raw = min(raw, 55.0)
    score = int(round(_clip(raw, 0.0, 88.0)))
    level = "high" if score >= 75 else "medium" if score >= 55 else "low"
    why = []
    missing = data_quality.get("summary", {}).get("unavailable_categories", [])
    if missing:
        why.append(f"仍有缺失/未接入类别：{', '.join(missing)}。")
    if completeness < 75:
        why.append("数据完整度尚未达到 75+ 的目标。")
    if signal_agreement.get("agreement_level") != "strong":
        why.append("信号一致性还不是 strong。")
    if analog_support.get("short_term_support") == "weak":
        why.append("短周期历史相似样本偏弱。")
    return {
        "confidence_score": score,
        "confidence_level": level,
        "components": {
            "prior_confidence": prior_score / 100.0,
            "data_completeness": completeness / 100.0,
            "signal_agreement": agreement / 100.0,
            "analog_support": analog_score / 100.0,
            "predictor_consistency": 1.0 - predictor_spread,
        },
        "why_confidence_is_limited": why or ["数据、信号和历史样本当前相对一致，但仍不是确定性预测。"],
    }


def build_market_edge_status(
    *,
    data_quality: dict[str, Any],
    signal_agreement: dict[str, Any],
    confidence: dict[str, Any],
    analog_support: dict[str, Any],
    overview_symbol: dict[str, Any],
    predictors: dict[str, Any],
) -> dict[str, Any]:
    completeness = int(data_quality.get("summary", {}).get("data_completeness_score") or 0)
    agreement = int(signal_agreement.get("signal_agreement_score") or 0)
    confidence_score = int(confidence.get("confidence_score") or 0)
    analog_conflict = analog_support.get("short_term_support") == "weak" and analog_support.get("medium_term_support") == "weak"
    regime_known = overview_symbol.get("market_state") not in {None, "", "unknown", "no_edge"}
    risk_expansion = predictors.get("risk_expansion_predictor", {}).get("probability", 0.0)
    conditions = {
        "data_completeness_ge_70": completeness >= 70,
        "signal_agreement_ge_65": agreement >= 65,
        "historical_analog_not_conflicting": not analog_conflict,
        "confidence_score_ge_60": confidence_score >= 60,
        "current_regime_identified": regime_known,
        "risk_conditions_not_conflicting": risk_expansion < 0.55,
    }
    passed = sum(1 for value in conditions.values() if value)
    if all(conditions.values()):
        status = "STRONG_EDGE"
    elif passed >= 5 and agreement >= 58 and confidence_score >= 58:
        status = "MODERATE_EDGE"
    elif passed >= 3 and confidence_score >= 45:
        status = "WEAK_EDGE"
    else:
        status = "NO_EDGE"
    return {
        "market_edge_status": status,
        "has_usable_prediction_edge_today": status in {"MODERATE_EDGE", "STRONG_EDGE"},
        "conditions": conditions,
        "passed_conditions": passed,
        "summary": _edge_summary(status),
    }


def enhance_horizon_predictions(
    predictions: dict[str, Any],
    predictors: dict[str, Any],
    analog_support: dict[str, Any],
    edge_status: dict[str, Any],
) -> dict[str, Any]:
    enhanced = dict(predictions)
    bounce = predictors["bounce_predictor"]["probability"]
    downside = predictors["downside_continuation_predictor"]["probability"]
    reversal = predictors["trend_reversal_predictor"]["probability"]
    risk_expansion = predictors["risk_expansion_predictor"]["probability"]
    for horizon in HORIZONS:
        key = f"{horizon}d"
        row = dict(enhanced.get(key, {}))
        support = analog_support.get("by_horizon", {}).get(key, {})
        if horizon <= 10:
            row["bounce_probability"] = _clip((row.get("bounce_probability") or bounce) * 0.45 + bounce * 0.55, 0.0, 1.0)
            row["failed_bounce_risk"] = _clip((row.get("failed_bounce_risk") or downside) * 0.45 + downside * 0.55, 0.0, 1.0)
        else:
            row["trend_reversal_probability"] = reversal
            row["risk_expansion_probability"] = risk_expansion
        if edge_status["market_edge_status"] == "NO_EDGE":
            row["expected_direction"] = "无优势/观望"
        row["market_edge_status"] = edge_status["market_edge_status"]
        row["analog_avg_return"] = support.get("avg_return")
        row["analog_hit_rate"] = support.get("hit_rate")
        row["analog_worst_path"] = support.get("worst_case")
        row["analog_best_path"] = support.get("best_case")
        enhanced[key] = row
    return enhanced


def build_path_weight_model(
    *,
    overview_symbol: dict[str, Any],
    signal_agreement: dict[str, Any],
    analog_support: dict[str, Any],
    features: dict[str, Any],
    data_quality: dict[str, Any],
    predictors: dict[str, Any],
    confidence: dict[str, Any],
) -> dict[str, Any]:
    volatility = features.get("volatility_options", {})
    credit = features.get("credit", {})
    breadth = features.get("breadth", {})
    news = features.get("news", {})
    macro = features.get("macro_event_calendar", {})
    rates = features.get("rates_liquidity", {})
    bounce_probability = float(overview_symbol.get("bounce_probability") or 0.0)
    failed_bounce_risk = float(predictors.get("downside_continuation_predictor", {}).get("probability") or overview_symbol.get("downside_continuation_probability") or 0.0)
    signal_agreement_score = float(signal_agreement.get("signal_agreement_score") or 0.0) / 100.0
    historical_support_score = _historical_support_score(analog_support)
    credit_stability = _float_or_none(credit.get("credit_stabilization_score")) or 0.0
    vix_change_5d = _float_or_none(volatility.get("vix_change_5d")) or 0.0
    vix_change_20d = _float_or_none(volatility.get("vix_change_20d")) or 0.0
    volatility_reversal = 1.0 if vix_change_5d < 0 and vix_change_20d <= 0 else 0.55 if vix_change_5d < 0 else 0.15
    breadth_support = _score01(breadth.get("breadth_confirmation_score"), _score01(breadth.get("breadth_improvement_score")))
    breadth_conflict = _score01(breadth.get("breadth_conflict_score"), _score01(breadth.get("breadth_deterioration_score")))
    news_risk = _float_or_none(news.get("news_risk_score")) or 0.0
    macro_event_risk = 1.0 if macro.get("macro_event_risk_flag") else 0.0
    rates_pressure = _float_or_none(rates.get("rates_pressure_score")) or 0.0
    data_completeness = float(data_quality.get("summary", {}).get("data_completeness_score") or 0.0) / 100.0
    confidence_score = float(confidence.get("confidence_score") or 0.0) / 100.0

    raw = {
        "base_path_weight": 0.24 + (1.0 - abs(signal_agreement_score - 0.50) * 2.0) * 0.10 + (1.0 - max(bounce_probability, failed_bounce_risk)) * 0.08,
        "bounce_path_weight": 0.12
        + bounce_probability * 0.30
        + signal_agreement_score * 0.12
        + historical_support_score * 0.12
        + credit_stability * 0.09
        + volatility_reversal * 0.08
        + breadth_support * 0.08,
        "bearish_path_weight": 0.12
        + failed_bounce_risk * 0.32
        + (1.0 - signal_agreement_score) * 0.12
        + (1.0 - historical_support_score) * 0.09
        + (1.0 - credit_stability) * 0.08
        + (1.0 - volatility_reversal) * 0.07
        + news_risk * 0.06
        + breadth_conflict * 0.08
        + rates_pressure * 0.06
        + macro_event_risk * 0.04
        + max(0.0, 0.75 - data_completeness) * 0.10,
        "analog_path_weight": 0.18 + historical_support_score * 0.18 + data_completeness * 0.10 + signal_agreement_score * 0.08,
    }
    total = sum(max(value, 0.001) for value in raw.values())
    weights = {key: round(max(value, 0.001) / total, 4) for key, value in raw.items()}
    low_confidence = data_completeness < 0.70
    confidence_level = "low" if low_confidence or confidence_score < 0.55 else "high" if confidence_score >= 0.75 and signal_agreement_score >= 0.75 else "medium"
    weights.update(
        {
            "low_confidence_simulation": low_confidence,
            "simulation_confidence_level": confidence_level,
            "weight_factors": {
                "bounce_probability": round(bounce_probability, 4),
                "failed_bounce_risk": round(failed_bounce_risk, 4),
                "signal_agreement": round(signal_agreement_score, 4),
                "historical_analog_support": round(historical_support_score, 4),
                "credit_stability": round(credit_stability, 4),
                "volatility_reversal": round(volatility_reversal, 4),
                "breadth_support": round(breadth_support, 4),
                "breadth_conflict": round(breadth_conflict, 4),
                "news_risk": round(news_risk, 4),
                "macro_event_risk": round(macro_event_risk, 4),
                "rates_pressure": round(rates_pressure, 4),
                "data_completeness": round(data_completeness, 4),
            },
            "weight_source_notes": [
                "base_path_weight rises when signals are mixed and neither bounce nor failed-bounce risk dominates.",
                "bounce_path_weight rises with bounce probability, signal agreement, supportive analogs, credit stability, volatility reversal and breadth support.",
                "bearish_path_weight rises with failed-bounce risk, weak agreement, weak analog support, credit instability, rising volatility and lower data completeness.",
                "analog_path_weight rises when historical analog sample support and data completeness are stronger.",
            ],
        }
    )
    return weights


def _update_scenario_card_weights_v3(simulated_symbol: dict[str, Any], path_weight_model: dict[str, Any]) -> None:
    mapping = {
        "Base case": "base_path_weight",
        "Bounce case": "bounce_path_weight",
        "Bearish case": "bearish_path_weight",
        "Historical analog case": "analog_path_weight",
    }
    for card in simulated_symbol.get("scenario_cards", []):
        key = mapping.get(card.get("name"))
        if key:
            card["probability_weight"] = path_weight_model[key]


def build_scenario_ranking(
    *,
    overview_symbol: dict[str, Any],
    path_weight_model: dict[str, Any],
    signal_agreement: dict[str, Any],
    analog_support: dict[str, Any],
    features: dict[str, Any],
    predictors: dict[str, Any],
    confidence: dict[str, Any],
) -> dict[str, Any]:
    scenarios = [
        {
            "scenario": "expected_path",
            "label": "综合期望情景",
            "weight_key": "base_path_weight",
            "expected_horizon": "3d-20d",
        },
        {
            "scenario": "bounce_path",
            "label": "反抽情景",
            "weight_key": "bounce_path_weight",
            "expected_horizon": "10d-20d",
        },
        {
            "scenario": "bearish_path",
            "label": "失败反抽情景",
            "weight_key": "bearish_path_weight",
            "expected_horizon": "3d-10d",
        },
        {
            "scenario": "analog_average_path",
            "label": "历史均值情景",
            "weight_key": "analog_path_weight",
            "expected_horizon": "20d-60d",
        },
    ]
    raw_weights = {item["scenario"]: max(float(path_weight_model.get(item["weight_key"]) or 0.0), 0.0) for item in scenarios}
    total = sum(raw_weights.values()) or 1.0
    normalized = {key: value / total for key, value in raw_weights.items()}
    enriched = []
    for item in scenarios:
        scenario = item["scenario"]
        probability = normalized[scenario]
        enriched.append(
            {
                "scenario": scenario,
                "label": item["label"],
                "probability": round(probability, 4),
                "reason": _scenario_ranking_reason(
                    scenario=scenario,
                    overview_symbol=overview_symbol,
                    path_weight_model=path_weight_model,
                    signal_agreement=signal_agreement,
                    analog_support=analog_support,
                    features=features,
                    predictors=predictors,
                ),
                "expected_horizon": item["expected_horizon"],
                "confidence": _scenario_confidence(probability, confidence, path_weight_model),
            }
        )
    enriched.sort(key=lambda item: item["probability"], reverse=True)
    primary, secondary, tertiary = enriched[0], enriched[1], enriched[2]
    gap = round(primary["probability"] - secondary["probability"], 4)
    close_call = gap < 0.08
    switch_conditions = _primary_switch_conditions(primary["scenario"], secondary["scenario"], overview_symbol, analog_support, features)
    return {
        "primary": primary,
        "secondary": secondary,
        "tertiary": tertiary,
        "all_scenarios": enriched,
        "primary_secondary_gap": gap,
        "close_call": close_call,
        "path_reliability": path_weight_model.get("simulation_confidence_level", "low"),
        "primary_to_secondary_switch_conditions": switch_conditions,
        "ranking_note": (
            "情景排序基于当前路径权重、信号一致性、历史相似样本、信用/波动率/宽度代理和数据完整度；"
            "这是概率情景排序，不是确定性预测，也不是 confirmed alpha。"
        ),
        "close_call_note": "路径分歧较大，不宜过度押注单一路径。" if close_call else "",
    }


def _scenario_ranking_reason(
    *,
    scenario: str,
    overview_symbol: dict[str, Any],
    path_weight_model: dict[str, Any],
    signal_agreement: dict[str, Any],
    analog_support: dict[str, Any],
    features: dict[str, Any],
    predictors: dict[str, Any],
) -> str:
    factors = path_weight_model.get("weight_factors", {})
    signal_score = float(signal_agreement.get("signal_agreement_score") or 0.0)
    data_completeness = float(factors.get("data_completeness") or 0.0)
    bounce_probability = float(overview_symbol.get("bounce_probability") or 0.0)
    downside_probability = float(overview_symbol.get("downside_continuation_probability") or predictors.get("downside_continuation_predictor", {}).get("probability") or 0.0)
    failed_bounce_risk = float(predictors.get("downside_continuation_predictor", {}).get("probability") or downside_probability)
    credit_stability = float(factors.get("credit_stability") or 0.0)
    volatility_reversal = float(factors.get("volatility_reversal") or 0.0)
    breadth_support = float(factors.get("breadth_support") or 0.0)
    sample_count = int(analog_support.get("sample_count") or 0)
    support_20d = analog_support.get("by_horizon", {}).get("20d", {}).get("support")
    support_60d = analog_support.get("by_horizon", {}).get("60d", {}).get("support")
    hit_20d = _float_or_none(analog_support.get("by_horizon", {}).get("20d", {}).get("hit_rate")) or 0.0
    hit_60d = _float_or_none(analog_support.get("by_horizon", {}).get("60d", {}).get("hit_rate")) or 0.0
    market_state = overview_symbol.get("market_state")

    if scenario == "bounce_path":
        reasons = [f"反抽概率 {bounce_probability:.0%}"]
        if overview_symbol.get("live_signal"):
            reasons.append("Alpha v1 当前触发")
        if support_20d == "supportive" or support_60d == "supportive":
            reasons.append("20d/60d 历史相似情景偏支持")
        if volatility_reversal >= 0.55:
            reasons.append("波动率有回落迹象")
        if credit_stability >= 0.55:
            reasons.append("信用代理相对稳定")
        if breadth_support >= 0.50:
            reasons.append("宽度代理改善")
        if signal_score >= 65:
            reasons.append(f"信号一致性 {signal_score:.0f}/100")
        return "，".join(reasons) + "。"

    if scenario == "bearish_path":
        reasons = [f"失败反抽/下跌延续风险 {max(failed_bounce_risk, downside_probability):.0%}"]
        if market_state in {"risk_off", "panic", "failed_bounce_risk", "downside_continuation"}:
            reasons.append(f"当前状态偏 {market_state}")
        if volatility_reversal < 0.55:
            reasons.append("波动率没有明确回落")
        if credit_stability < 0.50:
            reasons.append("信用代理偏弱")
        if analog_support.get("worst_path_risk") in {"high", "medium"}:
            reasons.append("历史最差路径风险不可忽视")
        return "，".join(reasons) + "。"

    if scenario == "analog_average_path":
        reasons = [f"历史相似样本数 {sample_count}"]
        if support_20d:
            reasons.append(f"20d 历史支持为 {support_20d}")
        if support_60d:
            reasons.append(f"60d 历史支持为 {support_60d}")
        if hit_20d or hit_60d:
            reasons.append(f"20d/60d 胜率约 {hit_20d:.0%}/{hit_60d:.0%}")
        if analog_support.get("analog_sample_quality"):
            reasons.append(f"样本质量 {analog_support.get('analog_sample_quality')}")
        return "，".join(reasons) + "。"

    reasons = []
    if signal_score < 65:
        reasons.append("信号一致性不够强")
    if market_state in {"sideways", "no_edge"}:
        reasons.append(f"市场状态偏 {market_state}")
    if data_completeness < 0.75:
        reasons.append(f"数据完整度约 {data_completeness:.0%}")
    if not reasons:
        reasons.append("综合期望路径用于平衡反抽、失败反抽和历史均值情景")
    return "，".join(reasons) + "。"


def _scenario_confidence(probability: float, confidence: dict[str, Any], path_weight_model: dict[str, Any]) -> str:
    if path_weight_model.get("low_confidence_simulation"):
        return "low"
    confidence_score = float(confidence.get("confidence_score") or 0.0) / 100.0
    if probability >= 0.34 and confidence_score >= 0.70:
        return "high"
    if probability >= 0.22 and confidence_score >= 0.55:
        return "medium"
    return "low"


def _primary_switch_conditions(
    primary_scenario: str,
    secondary_scenario: str,
    overview_symbol: dict[str, Any],
    analog_support: dict[str, Any],
    features: dict[str, Any],
) -> list[str]:
    symbol = overview_symbol.get("symbol", "symbol")
    common_risk = [
        "VIX 重新上升或波动率回落失败",
        "HYG/LQD 相对强度转弱，信用代理恶化",
        f"{symbol} 跌破近期低点",
        "historical support 从 supportive 转为 weak 或 conflicting",
    ]
    if primary_scenario == "bounce_path":
        return common_risk
    if primary_scenario == "analog_average_path":
        return [
            "新的历史相似样本分布转弱",
            "20d/60d 胜率跌破 50%",
            "当前市场与相似样本差异扩大",
            *common_risk[:2],
        ]
    if primary_scenario == "expected_path":
        return [
            "信号一致性明显增强并偏向反抽或下跌延续",
            "market edge 从 NO_EDGE/WEAK_EDGE 切换为更强状态",
            "波动率、信用或宽度代理出现同向突破",
        ]
    return [
        "VIX 快速回落并维持低位",
        "信用代理企稳，HYG/LQD 修复",
        "价格重新站回短期趋势线",
        "20d/60d 历史相似支持转强",
    ]


def _historical_support_score(analog_support: dict[str, Any]) -> float:
    values = [analog_support.get("short_term_support"), analog_support.get("medium_term_support")]
    score = 0.0
    for value in values:
        if value == "supportive":
            score += 1.0
        elif value == "neutral":
            score += 0.55
        elif value == "low_sample":
            score += 0.35
        else:
            score += 0.15
    return _clip(score / max(len(values), 1), 0.0, 1.0)


def build_v3_judgment(
    symbol: str,
    edge_status: dict[str, Any],
    predictors: dict[str, Any],
    horizon_predictions: dict[str, Any],
    signal_agreement: dict[str, Any],
    confidence: dict[str, Any],
) -> str:
    edge = edge_status["market_edge_status"]
    bounce = predictors["bounce_predictor"]["probability"]
    downside = predictors["downside_continuation_predictor"]["probability"]
    risk = predictors["risk_expansion_predictor"]["probability"]
    h5 = horizon_predictions.get("5d", {}).get("expected_direction", "未知")
    h20 = horizon_predictions.get("20d", {}).get("expected_direction", "未知")
    return (
        f"{symbol} 当前可用预测优势：{edge}。"
        f"反抽预测器 {bounce:.0%}，下跌延续预测器 {downside:.0%}，风险扩散预测器 {risk:.0%}。"
        f"5d 判断：{h5}；20d 判断：{h20}。"
        f"信号一致性 {signal_agreement.get('signal_agreement_score')} 分，模型可信度 {confidence.get('confidence_score')} 分。"
        "如果是 NO_EDGE 或 WEAK_EDGE，应以观察为主，不应强行下结论。"
    )


def build_high_confidence_signal_report(analogs: dict[str, dict[str, Any]], simulated_paths: dict[str, Any]) -> dict[str, Any]:
    cases: list[dict[str, Any]] = []
    for symbol, analog in analogs.items():
        for case in analog.get("top_similar_cases", []):
            enriched = dict(case)
            enriched["symbol"] = symbol
            enriched["proxy_confidence"] = _float_or_none(case.get("similarity_score")) or 0.0
            cases.append(enriched)
    cases = [case for case in cases if case.get("proxy_confidence") is not None]
    cases.sort(key=lambda item: item["proxy_confidence"], reverse=True)
    buckets = {
        "top_10_confidence_signals": cases[: max(1, math.ceil(len(cases) * 0.10))],
        "top_20_confidence_signals": cases[: max(1, math.ceil(len(cases) * 0.20))],
        "strong_signal_only": [
            case
            for case in cases
            if simulated_paths.get("symbols", {}).get(case["symbol"], {}).get("market_edge_status", {}).get("market_edge_status") in {"MODERATE_EDGE", "STRONG_EDGE"}
        ],
        "low_confidence_reference": cases[-max(1, math.ceil(len(cases) * 0.20)) :] if cases else [],
    }
    by_bucket = {name: _bucket_metrics(rows) for name, rows in buckets.items()}
    by_symbol = {symbol: _bucket_metrics([case for case in cases if case["symbol"] == symbol]) for symbol in TARGET_SYMBOLS}
    by_regime: dict[str, list[dict[str, Any]]] = {}
    for case in cases:
        by_regime.setdefault(str(case.get("regime", "unknown")), []).append(case)
    by_regime_metrics = {regime: _bucket_metrics(rows) for regime, rows in by_regime.items()}
    wins = 0
    comparisons: dict[str, bool] = {}
    for horizon in (3, 5, 10, 20, 60):
        high = by_bucket["top_20_confidence_signals"].get("horizons", {}).get(f"{horizon}d", {})
        low = by_bucket["low_confidence_reference"].get("horizons", {}).get(f"{horizon}d", {})
        better = (high.get("hit_rate") or 0.0) > (low.get("hit_rate") or 0.0) and (high.get("avg_return") or 0.0) > (low.get("avg_return") or 0.0)
        comparisons[f"{horizon}d"] = better
        wins += int(better)
    high_better = wins >= 3
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "historical_proxy_only_not_forward_confirmed",
        "sample_size": len(cases),
        "method_note": "Uses current historical analog case set as a proxy confidence study. Forward-only confidence validation is still insufficient until more frozen signals mature.",
        "by_bucket": by_bucket,
        "by_symbol": by_symbol,
        "by_regime": by_regime_metrics,
        "high_vs_low_comparison_by_horizon": comparisons,
        "high_confidence_better_than_low_confidence": high_better,
        "conclusion": "confidence_useful_proxy" if high_better else "confidence_not_yet_validated",
    }


def render_high_confidence_signal_report_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# High Confidence Signal Report",
        "",
        f"Generated at: `{report.get('generated_at')}`",
        "",
        "This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.",
        "",
        f"Status: `{report.get('status')}`",
        f"Sample size: `{report.get('sample_size')}`",
        f"Conclusion: `{report.get('conclusion')}`",
        "",
        "## Bucket Metrics",
        "",
    ]
    for bucket, payload in report.get("by_bucket", {}).items():
        lines.append(f"### {bucket}")
        lines.append(f"- sample_size: `{payload.get('sample_size')}`")
        for horizon, metrics in payload.get("horizons", {}).items():
            lines.append(
                f"- {horizon}: hit_rate `{_fmt(metrics.get('hit_rate'))}`, avg `{_fmt(metrics.get('avg_return'))}`, "
                f"median `{_fmt(metrics.get('median_return'))}`, brier `{_fmt(metrics.get('brier_score'))}`, calibration_gap `{_fmt(metrics.get('calibration_gap'))}`"
            )
        lines.append("")
    lines.extend(
        [
            "## Interpretation",
            "",
            "- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.",
            "- Forward-only validation still matters more than this historical proxy report.",
            "- Alpha v1 remains RESEARCH ALPHA CANDIDATE.",
            "",
        ]
    )
    return "\n".join(lines)


def _empty_finnhub_bundle() -> dict[str, Any]:
    return {
        "provider": "finnhub",
        "configured": False,
        "available": False,
        "missing": True,
        "rate_limited": False,
        "cache_used": False,
        "quotes": {},
        "candles": {},
        "news_sentiment": {},
        "economic_calendar": {"status": "missing_api_key", "events": [], "event_count": 0},
        "market_status": {"status": "missing_api_key", "payload": None},
        "market_holiday": {"status": "missing_api_key", "payload": None},
        "market_news": {"status": "missing_api_key", "items": [], "news_risk_score": None},
        "rates_data": {"status": "missing"},
        "alternative_data": {"status": "missing"},
    }


def _finnhub_status_summary(bundle: dict[str, Any]) -> dict[str, Any]:
    return {
        "finnhub_available": bool(bundle.get("available")),
        "finnhub_missing": bool(bundle.get("missing")) or not bool(bundle.get("configured")),
        "finnhub_rate_limited": bool(bundle.get("rate_limited")),
        "finnhub_cache_used": bool(bundle.get("cache_used")),
        "finnhub_successful_requests": int(bundle.get("successful_requests") or 0),
        "finnhub_failed_requests": int(bundle.get("failed_requests") or 0),
    }


def _fred_bundle_summary(bundle: dict[str, Any]) -> dict[str, Any]:
    return {
        "fred_available": bool(bundle.get("available")),
        "fred_missing": bool(bundle.get("missing")),
        "fred_rate_limited": bool(bundle.get("rate_limited")),
        "fred_fallback_used": bool(bundle.get("fallback_used")),
        "fred_cache_used": bool(bundle.get("cache_used")),
        "fred_successful_series": list(bundle.get("successful_series") or []),
        "fred_failed_series": list(bundle.get("failed_series") or []),
    }


def _breadth_bundle_summary(bundle: dict[str, Any] | None) -> dict[str, Any]:
    if not bundle:
        return {
            "provider_available": False,
            "true_breadth_available": False,
            "true_breadth_symbols": [],
            "breadth_proxy_only_symbols": [],
            "average_breadth_quality_score": 0,
        }
    summary = bundle.get("summary") or {}
    return {
        "provider_available": bool(summary.get("provider_available")),
        "true_breadth_available": bool(summary.get("true_breadth_available")),
        "true_breadth_symbols": list(summary.get("true_breadth_symbols") or []),
        "breadth_proxy_only_symbols": list(summary.get("breadth_proxy_only_symbols") or []),
        "stale_data": bool(summary.get("stale_data")),
        "average_breadth_quality_score": summary.get("average_breadth_quality_score"),
    }


def _options_bundle_summary(bundle: dict[str, Any] | None) -> dict[str, Any]:
    summary = (bundle or {}).get("summary") or {}
    return {
        "options_available": bool(summary.get("options_available")),
        "vix_term_available": bool(summary.get("vix_term_available")),
        "vvix_available": bool(summary.get("vvix_available")),
        "skew_available": bool(summary.get("skew_available")),
        "put_call_available": bool(summary.get("put_call_available")),
        "gamma_available": bool(summary.get("gamma_available")),
        "options_partial": bool(summary.get("options_partial")),
        "options_missing": bool(summary.get("options_missing", not bool(bundle))),
        "options_stale": bool(summary.get("options_stale")),
        "options_source": summary.get("options_source") or "missing",
        "options_quality_score": summary.get("options_quality_score") or 0,
        "missing_symbols": list(summary.get("missing_symbols") or []),
    }


def _flow_bundle_summary(bundle: dict[str, Any] | None) -> dict[str, Any]:
    summary = (bundle or {}).get("summary") or {}
    return {
        "flow_available": bool(summary.get("flow_available")),
        "flow_proxy_only": bool(summary.get("flow_proxy_only", bool(bundle))),
        "true_flow_available": bool(summary.get("true_flow_available")),
        "average_flow_quality_score": summary.get("average_flow_quality_score") or 0,
        "overall_flow_confirmation_score": summary.get("overall_flow_confirmation_score") or 0,
        "overall_flow_conflict_score": summary.get("overall_flow_conflict_score") or 0,
        "flow_symbols": list(summary.get("flow_symbols") or []),
        "missing_real_flow_feeds": list(summary.get("missing_real_flow_feeds") or []),
    }


def _finnhub_source_rows(bundle: dict[str, Any]) -> dict[str, Any]:
    rows: dict[str, Any] = {
        "FINNHUB_API": _finnhub_source_row(
            "FINNHUB_API",
            {
                "status": "available" if bundle.get("available") else "rate_limited" if bundle.get("rate_limited") else "missing",
                "source": "finnhub",
                "cache_used": bundle.get("cache_used", False),
                "payload": {"configured": bundle.get("configured", False)},
            },
        )
    }
    for symbol, result in (bundle.get("quotes") or {}).items():
        rows[f"finnhub_quote_{symbol}"] = _finnhub_source_row(f"finnhub_quote_{symbol}", result)
    for symbol, result in (bundle.get("candles") or {}).items():
        rows[f"finnhub_candle_{symbol}"] = _finnhub_source_row(f"finnhub_candle_{symbol}", result)
    for symbol, result in (bundle.get("news_sentiment") or {}).items():
        rows[f"finnhub_news_sentiment_{symbol}"] = _finnhub_source_row(f"finnhub_news_sentiment_{symbol}", result)
    for symbol in TARGET_SYMBOLS:
        rows.setdefault(f"finnhub_quote_{symbol}", _finnhub_source_row(f"finnhub_quote_{symbol}", {"status": "missing", "source": "finnhub"}))
        rows.setdefault(f"finnhub_candle_{symbol}", _finnhub_source_row(f"finnhub_candle_{symbol}", {"status": "missing", "source": "finnhub"}))
        rows.setdefault(f"finnhub_news_sentiment_{symbol}", _finnhub_source_row(f"finnhub_news_sentiment_{symbol}", {"status": "missing", "source": "finnhub"}))
    rows["finnhub_economic_calendar"] = _finnhub_source_row("finnhub_economic_calendar", bundle.get("economic_calendar") or {})
    rows["finnhub_market_news"] = _finnhub_source_row("finnhub_market_news", bundle.get("market_news") or {})
    rows["finnhub_market_status"] = _finnhub_source_row("finnhub_market_status", bundle.get("market_status") or {})
    rows["finnhub_market_holiday"] = _finnhub_source_row("finnhub_market_holiday", bundle.get("market_holiday") or {})
    rows["finnhub_rates_data"] = _finnhub_source_row("finnhub_rates_data", bundle.get("rates_data") or {})
    rows["finnhub_alternative_data"] = _finnhub_source_row("finnhub_alternative_data", bundle.get("alternative_data") or {})
    return rows


def _breadth_source_rows(bundle: dict[str, Any] | None) -> dict[str, Any]:
    rows: dict[str, Any] = {}
    if not bundle:
        return rows
    for symbol, payload in (bundle.get("universes") or {}).items():
        scores = payload.get("scores") or {}
        status = str(payload.get("status") or "missing")
        real_data = bool(payload.get("is_true_breadth")) and status in {"available", "stale", "partial"}
        rows[f"breadth_{symbol}"] = {
            "symbol": f"breadth_{symbol}",
            "source": payload.get("source") or "breadth_provider",
            "status": status,
            "rows": payload.get("constituents_used") or 0,
            "latest_date": payload.get("latest_date"),
            "real_data": real_data,
            "fallback_used": bool(payload.get("stale_constituents") or payload.get("stale_price_data") or payload.get("is_proxy")),
            "stale_data": bool(payload.get("stale_constituents") or payload.get("stale_price_data")),
            "missing_data": status in {"missing", "not_available"} or not (payload.get("metrics") or {}),
            "point_in_time_safe": real_data,
            "is_proxy": bool(payload.get("is_proxy")),
            "breadth_quality_score": scores.get("breadth_quality_score"),
            "coverage_ratio": payload.get("coverage_ratio"),
            "detail": payload.get("data_note"),
        }
    sector = bundle.get("sector_participation_proxy") or {}
    rows["breadth_sector_participation_proxy"] = {
        "symbol": "breadth_sector_participation_proxy",
        "source": sector.get("source", "sector-etf-participation-proxy"),
        "status": "proxy" if sector.get("sector_count") else "missing",
        "rows": sector.get("sector_count") or 0,
        "latest_date": None,
        "real_data": False,
        "fallback_used": True,
        "stale_data": False,
        "missing_data": not bool(sector.get("sector_count")),
        "point_in_time_safe": True,
        "is_proxy": True,
        "detail": sector.get("data_note"),
    }
    return rows


def _options_source_rows(bundle: dict[str, Any] | None) -> dict[str, Any]:
    rows: dict[str, Any] = {}
    if not bundle:
        return rows
    summary = bundle.get("summary") or {}
    rows["options_provider"] = {
        "symbol": "options_provider",
        "source": summary.get("options_source") or "options_volatility_structure",
        "status": "available" if summary.get("options_available") else "partial" if summary.get("options_partial") else "missing",
        "rows": len(bundle.get("sources") or {}),
        "latest_date": None,
        "real_data": bool(summary.get("options_available") or summary.get("options_partial")),
        "fallback_used": False,
        "stale_data": bool(summary.get("options_stale")),
        "missing_data": bool(summary.get("options_missing")),
        "point_in_time_safe": bool(summary.get("options_available") or summary.get("options_partial")),
        "options_quality_score": summary.get("options_quality_score"),
        "detail": summary.get("coverage_note"),
    }
    for symbol, payload in (bundle.get("sources") or {}).items():
        rows[f"options_{symbol.replace('^', '')}"] = {
            "symbol": symbol,
            "source": payload.get("source") or "options_volatility_structure",
            "status": payload.get("status") or "missing",
            "rows": payload.get("rows") or 0,
            "latest_date": payload.get("latest_date"),
            "latest_value": payload.get("latest_value"),
            "real_data": bool(payload.get("real_data")),
            "fallback_used": bool(payload.get("fallback_used")),
            "stale_data": bool(payload.get("stale_data")),
            "missing_data": bool(payload.get("missing_data")),
            "point_in_time_safe": bool(payload.get("point_in_time_safe")),
        }
    return rows


def _flow_source_rows(bundle: dict[str, Any] | None) -> dict[str, Any]:
    rows: dict[str, Any] = {}
    if not bundle:
        return rows
    summary = bundle.get("summary") or {}
    rows["flow_provider"] = {
        "symbol": "flow_provider",
        "source": bundle.get("provider") or "flow_positioning_proxy",
        "status": "proxy" if summary.get("flow_available") else "missing",
        "rows": len(bundle.get("symbols") or {}),
        "latest_date": bundle.get("latest_date"),
        "real_data": False,
        "fallback_used": True,
        "stale_data": False,
        "missing_data": not bool(summary.get("flow_available")),
        "point_in_time_safe": True,
        "is_proxy": True,
        "true_flow_available": False,
        "average_flow_quality_score": summary.get("average_flow_quality_score"),
        "flow_confirmation_score": summary.get("overall_flow_confirmation_score"),
        "flow_conflict_score": summary.get("overall_flow_conflict_score"),
        "detail": summary.get("data_note") or "Proxy-only flow / positioning. No true fund-flow feed.",
    }
    for symbol, payload in (bundle.get("symbols") or {}).items():
        scores = payload.get("scores") or {}
        rows[f"flow_{symbol}"] = {
            "symbol": f"flow_{symbol}",
            "source": payload.get("source") or "market_data_proxy",
            "status": payload.get("status") or "missing",
            "rows": 1,
            "latest_date": payload.get("latest_date"),
            "real_data": False,
            "fallback_used": True,
            "stale_data": False,
            "missing_data": payload.get("status") == "missing",
            "point_in_time_safe": True,
            "is_proxy": True,
            "true_flow_available": False,
            "flow_quality_score": scores.get("flow_quality_score"),
            "flow_confirmation_score": scores.get("flow_confirmation_score"),
            "flow_conflict_score": scores.get("flow_conflict_score"),
            "detail": payload.get("data_note"),
        }
    return rows


def _finnhub_source_row(name: str, result: dict[str, Any]) -> dict[str, Any]:
    raw_status = str(result.get("status") or "missing")
    cache_used = bool(result.get("cache_used"))
    if raw_status == "available":
        status = "available"
        missing = False
        real_data = True
    elif cache_used:
        status = "fallback"
        missing = False
        real_data = True
    elif raw_status == "rate_limited":
        status = "rate_limited"
        missing = True
        real_data = False
    else:
        status = "missing"
        missing = True
        real_data = False
    return {
        "symbol": name,
        "source": result.get("source", "finnhub"),
        "status": status,
        "rows": _payload_size(result),
        "latest_date": None,
        "real_data": real_data,
        "fallback_used": cache_used,
        "rate_limited": raw_status == "rate_limited",
        "stale_data": False,
        "missing_data": missing,
        "point_in_time_safe": real_data,
    }


def _payload_size(result: dict[str, Any]) -> int:
    if "event_count" in result:
        return int(result.get("event_count") or 0)
    if "items" in result:
        return len(result.get("items") or [])
    payload = result.get("payload") if "payload" in result else result.get("data")
    if isinstance(payload, list):
        return len(payload)
    if isinstance(payload, dict):
        for key in ("c", "t", "economicCalendar"):
            value = payload.get(key)
            if isinstance(value, list):
                return len(value)
        return 1 if payload else 0
    return 0


def _finnhub_symbol_snapshot(bundle: dict[str, Any], symbol: str) -> dict[str, Any]:
    quote = (bundle.get("quotes") or {}).get(symbol, {})
    candle = (bundle.get("candles") or {}).get(symbol, {})
    sentiment = (bundle.get("news_sentiment") or {}).get(symbol, {})
    quote_payload = quote.get("payload") if isinstance(quote, dict) else None
    sentiment_payload = sentiment.get("payload") if isinstance(sentiment, dict) else None
    return {
        "quote_status": quote.get("status", "missing") if isinstance(quote, dict) else "missing",
        "quote_source": quote.get("source") if isinstance(quote, dict) else None,
        "quote_price": _float_or_none((quote_payload or {}).get("c")) if isinstance(quote_payload, dict) else None,
        "quote_previous_close": _float_or_none((quote_payload or {}).get("pc")) if isinstance(quote_payload, dict) else None,
        "quote_change_percent": _float_or_none((quote_payload or {}).get("dp")) if isinstance(quote_payload, dict) else None,
        "candle_status": candle.get("status", "missing") if isinstance(candle, dict) else "missing",
        "news_sentiment_status": sentiment.get("status", "missing") if isinstance(sentiment, dict) else "missing",
        "sentiment_score": _extract_sentiment_score(sentiment_payload),
    }


def _extract_sentiment_score(payload: Any) -> float | None:
    if not isinstance(payload, dict):
        return None
    for key in ("sentiment", "companyNewsScore", "sectorAverageBullishPercent", "buzz"):
        value = payload.get(key)
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, dict):
            for nested in ("score", "bullishPercent"):
                if isinstance(value.get(nested), (int, float)):
                    return float(value[nested])
    return None


def _finnhub_macro_snapshot(bundle: dict[str, Any]) -> dict[str, Any]:
    calendar = bundle.get("economic_calendar") or {}
    events = calendar.get("events") or []
    high_risk_keywords = ("cpi", "inflation", "fomc", "fed", "payroll", "nonfarm", "nfp", "unemployment", "pce", "rate")
    risk_events = []
    for event in events:
        text = f"{event.get('event') or ''} {event.get('impact') or ''}".lower()
        if any(keyword in text for keyword in high_risk_keywords):
            risk_events.append(event)
    return {
        "finnhub_economic_calendar_status": calendar.get("status", "missing"),
        "finnhub_event_count": len(events),
        "finnhub_macro_risk_events": risk_events[:10],
        "macro_event_risk_flag": bool(risk_events) or False,
    }


def _finnhub_news_snapshot(bundle: dict[str, Any]) -> dict[str, Any]:
    market_news = bundle.get("market_news") or {}
    items = market_news.get("items") or []
    return {
        "market_news_status": market_news.get("status", "missing"),
        "news_risk_score": _float_or_none(market_news.get("news_risk_score")),
        "top_headlines": [item.get("headline") for item in items[:5] if item.get("headline")],
        "news_item_count": len(items),
    }


def _daily_market_brief(
    symbol: str,
    finnhub_symbol: dict[str, Any],
    news: dict[str, Any],
    macro: dict[str, Any],
    rates: dict[str, Any],
) -> dict[str, Any]:
    quote_price = finnhub_symbol.get("quote_price")
    quote_text = f"Finnhub quote {quote_price:.2f}" if isinstance(quote_price, (int, float)) else "Finnhub quote unavailable"
    news_risk = news.get("news_risk_score")
    news_text = "news risk unavailable" if news_risk is None else f"news risk {float(news_risk):.0%}"
    macro_text = "macro event risk flagged" if macro.get("macro_event_risk_flag") else "no major macro event flag"
    rates_text = f"rates pressure {(rates.get('rates_pressure_score') or 0.0):.0%}"
    return {
        "symbol": symbol,
        "brief": f"{quote_text}; {news_text}; {macro_text}; {rates_text}.",
        "finnhub_quote_available": finnhub_symbol.get("quote_status") == "available",
        "news_risk_score": news_risk,
        "macro_event_risk_flag": bool(macro.get("macro_event_risk_flag")),
        "rates_pressure_score": rates.get("rates_pressure_score"),
    }


def _coverage_categories_v3(source_rows: dict[str, Any], feature_snapshot: dict[str, Any]) -> dict[str, Any]:
    def status(symbol: str) -> str:
        return source_rows.get(symbol, {}).get("status", "missing")

    sector_symbols = ("XLC", "XLY", "XLP", "XLE", "XLF", "XLV", "XLI", "XLK", "XLB", "XLU", "XLRE")
    sector_available = sum(1 for symbol in sector_symbols if source_rows.get(symbol, {}).get("real_data"))
    option_available = sum(1 for symbol in ("^VIX9D", "^VIX3M", "^VIX6M", "^VVIX", "^SKEW") if source_rows.get(symbol, {}).get("real_data"))
    option_provider = source_rows.get("options_provider", {})
    option_provider_status = option_provider.get("status")
    option_provider_count = int(bool(option_provider.get("real_data"))) + option_available
    fred_credit_available = sum(1 for name in ("HY_OAS", "IG_OAS", "BAA_SPREAD", "FINANCIAL_STRESS") if source_rows.get(name, {}).get("real_data"))
    fred_rates_available = sum(1 for name in ("DGS10", "DGS2", "DGS3MO", "DFII10", "RECESSION") if source_rows.get(name, {}).get("real_data"))
    true_breadth_available = sum(1 for name in ("breadth_SPY", "breadth_QQQ", "breadth_DIA") if source_rows.get(name, {}).get("real_data"))
    breadth_proxy_available = sum(1 for name in ("breadth_IWM",) if source_rows.get(name, {}).get("status") == "proxy")
    flow_provider = source_rows.get("flow_provider", {})
    flow_symbol_available = sum(1 for name in ("flow_SPY", "flow_QQQ", "flow_IWM", "flow_DIA") if source_rows.get(name, {}).get("status") in {"proxy", "available", "partial", "stale"})
    target_available = sum(1 for symbol in TARGET_SYMBOLS if source_rows.get(symbol, {}).get("real_data"))
    finnhub_news_available = source_rows.get("finnhub_market_news", {}).get("status") == "available"
    finnhub_calendar_available = source_rows.get("finnhub_economic_calendar", {}).get("status") == "available"

    return {
        "price": _coverage_payload_v3("available" if target_available == 4 else "missing", "SPY/QQQ/IWM/DIA OHLCV", target_available, 4, True),
        "volatility": _coverage_payload_v3("available" if status("^VIX") == "available" else "missing", "VIX level/change/percentile", int(status("^VIX") == "available"), 1, status("^VIX") == "available"),
        "options": _coverage_payload_v3(
            "available" if option_provider_status == "available" else "partial" if option_provider_status == "partial" or option_available >= 2 else "missing",
            "VIX term/VVIX/SKEW when real data exists; put/call and gamma remain explicitly missing",
            option_provider_count,
            7,
            option_provider_status in {"available", "partial"} or option_available >= 2,
        ),
        "breadth": _coverage_payload_v3(
            "available" if true_breadth_available >= 3 else "partial" if true_breadth_available else "proxy" if (breadth_proxy_available or (status("RSP") == "available" and sector_available >= 7)) else "missing",
            "Constituent breadth for SPY/QQQ/DIA when available; IWM/RSP/sector ETF proxy remains explicitly labeled",
            true_breadth_available + breadth_proxy_available + sector_available + int(status("RSP") == "available"),
            15,
            true_breadth_available >= 3,
        ),
        "credit": _coverage_payload_v3("available" if fred_credit_available >= 3 else "proxy" if status("HYG") == "available" and status("LQD") == "available" else "missing", "FRED HY/IG/BAA/stress plus HYG/LQD proxy", fred_credit_available + int(status("HYG") == "available") + int(status("LQD") == "available"), 6, fred_credit_available >= 3),
        "rates": _coverage_payload_v3("available" if fred_rates_available >= 4 else "partial" if status("^TNX") == "available" else "missing", "FRED 10Y/2Y/3M/TIPS/recession plus ^TNX", fred_rates_available + int(status("^TNX") == "available"), 6, fred_rates_available >= 4),
        "liquidity": _coverage_payload_v3("proxy" if status("TLT") == "available" and status("UUP") == "available" else "missing", "TLT/UUP/rates stress proxy, not reserves/repo/TGA", int(status("TLT") == "available") + int(status("UUP") == "available") + fred_rates_available, 5, False),
        "macro": _coverage_payload_v3("available" if finnhub_calendar_available else "fallback", "Finnhub economic calendar if available, otherwise rule-based CPI/FOMC/NFP/options-expiry/month-end calendar risk", 2 if finnhub_calendar_available else 1, 5, finnhub_calendar_available),
        "news": _coverage_payload_v3("available" if finnhub_news_available else "missing", "Finnhub market news risk score and daily market brief", int(finnhub_news_available), 1, finnhub_news_available),
        "flow": _coverage_payload_v3(
            "proxy" if flow_provider.get("status") == "proxy" or flow_symbol_available else "missing",
            "Proxy-only ETF volume, relative volume, HYG/LQD, TLT/UUP, high-beta/low-vol, equal-weight/cap-weight and sector rotation. True flow remains missing.",
            flow_symbol_available + int(status("SPHB") == "available") + int(status("SPLV") == "available") + int(status("RSP") == "available"),
            10,
            False,
        ),
        "market_structure": _coverage_payload_v3("proxy" if sector_available >= 7 else "missing", "Sector ETF participation, defensive/cyclical, small/large, growth/value proxies", sector_available, 11, False),
    }


def _data_completeness_score_v3(coverage: dict[str, Any], source_rows: dict[str, Any]) -> int:
    weights = {
        "price": 15,
        "volatility": 10,
        "options": 8,
        "breadth": 12,
        "credit": 12,
        "rates": 10,
        "liquidity": 8,
        "macro": 6,
        "news": 5,
        "flow": 7,
        "market_structure": 12,
    }
    values = {
        "available": 1.0,
        "partial": 0.65,
        "proxy": 0.78,
        "fallback": 0.45,
        "stale": 0.35,
        "missing": 0.0,
        "not_available": 0.0,
    }
    score = sum(weights[name] * values.get(payload.get("status"), 0.0) for name, payload in coverage.items())
    if any(row.get("source") == "synthetic-fallback" for row in source_rows.values()):
        score -= 20
    return int(round(_clip(score, 0.0, 100.0)))


def _market_source_status(symbol: str, series: DownloadedSeries | None, latest: str | None) -> dict[str, Any]:
    rows = len(series.rows) if series else 0
    real_data = bool(series and is_real_market_data(series))
    source = series.source if series else "missing"
    fallback = source.startswith("local-cache") or "fallback" in source
    return {
        "symbol": symbol,
        "source": source,
        "status": "available" if real_data else "fallback" if fallback and rows else "missing",
        "rows": rows,
        "latest_date": latest,
        "real_data": real_data,
        "fallback_used": fallback,
        "stale_data": False,
        "missing_data": rows == 0 or not real_data,
        "point_in_time_safe": bool(series and series.point_in_time_safe and real_data),
    }


def _fred_source_status(name: str, series: FredSeries, latest: str | None) -> dict[str, Any]:
    rows = len(series.rows)
    fallback = series.source.startswith("local-cache")
    latest_value = series.rows[-1].get("value") if series.rows else None
    return {
        "symbol": name,
        "source": series.source,
        "series_id": series.series_id,
        "status": "available" if series.real_data else "fallback" if fallback and rows else "missing",
        "rows": rows,
        "latest_date": latest,
        "latest_value": latest_value,
        "real_data": series.real_data,
        "fallback_used": fallback,
        "stale_data": fallback,
        "missing_data": rows == 0 or not series.real_data,
        "point_in_time_safe": series.real_data,
    }


def _coverage_payload_v3(status: str, detail: str, available_items: int, expected_items: int, real_data: bool) -> dict[str, Any]:
    return {
        "status": status,
        "detail": detail,
        "available_items": available_items,
        "expected_items": expected_items,
        "real_data": real_data,
        "fallback_used": status == "fallback",
        "proxy_used": status == "proxy",
    }


def _volatility_snapshot(vix: list[float], vix9d: list[float], vix3m: list[float], vix6m: list[float], vvix: list[float], skew: list[float]) -> dict[str, Any]:
    vix_level = _last(vix)
    vix3m_level = _last(vix3m)
    term_front = (vix_level / vix3m_level - 1.0) if vix_level and vix3m_level else None
    term_slope = ((_last(vix6m) or 0.0) - (vix_level or 0.0)) if vix and vix6m else None
    return {
        "vix_level": vix_level,
        "vix_change_5d": _change(vix, 5),
        "vix_change_20d": _change(vix, 20),
        "vix_percentile_1y": _percentile_rank(vix, vix_level, 252),
        "vix9d": _last(vix9d),
        "vix3m": vix3m_level,
        "vix6m": _last(vix6m),
        "vvix": _last(vvix),
        "skew": _last(skew),
        "put_call_ratio": "missing",
        "implied_vol_term_structure_proxy": term_front,
        "vix_term_slope_proxy": term_slope,
        "options_data_note": "VIX term proxies if available; put/call and gamma are not connected.",
    }


def _options_from_bundle(symbol: str, options_bundle: dict[str, Any] | None) -> dict[str, Any]:
    if not options_bundle:
        return {
            "options_available": False,
            "vix_term_available": False,
            "put_call_available": False,
            "gamma_available": False,
            "options_quality_score": 0,
            "options_provider_status": "missing",
        }
    summary = options_bundle.get("summary") or {}
    market = options_bundle.get("market") or {}
    symbol_payload = (options_bundle.get("symbols") or {}).get(symbol) or {}
    merged = {**market, **symbol_payload}
    return {
        "options_available": bool(summary.get("options_available")),
        "vix_term_available": bool(summary.get("vix_term_available")),
        "vvix_available": bool(summary.get("vvix_available")),
        "skew_available": bool(summary.get("skew_available")),
        "put_call_available": bool(summary.get("put_call_available")),
        "gamma_available": bool(summary.get("gamma_available")),
        "options_partial": bool(summary.get("options_partial")),
        "options_missing": bool(summary.get("options_missing")),
        "options_stale": bool(summary.get("options_stale")),
        "options_source": summary.get("options_source"),
        "options_provider_status": "available" if summary.get("options_available") else "partial" if summary.get("options_partial") else "missing",
        "options_quality_score": _score01(merged.get("options_quality_score")),
        "vix9d_minus_vix": merged.get("vix9d_minus_vix"),
        "vix3m_minus_vix": merged.get("vix3m_minus_vix"),
        "vix6m_minus_vix": merged.get("vix6m_minus_vix"),
        "term_structure_state": merged.get("term_structure_state"),
        "volatility_reversal_score": _score01(merged.get("volatility_reversal_score")),
        "panic_release_score": _score01(merged.get("panic_release_score")),
        "tail_risk_score": _score01(merged.get("tail_risk_score")),
        "option_stress_score": _score01(merged.get("option_stress_score"), 0.45),
        "failed_bounce_options_risk": _score01(merged.get("failed_bounce_options_risk"), 0.45),
        "options_supports_bounce": bool(merged.get("options_supports_bounce")),
        "options_conflicts_bounce": bool(merged.get("options_conflicts_bounce")),
        "options_reason": merged.get("options_reason"),
        "options_risk_note": merged.get("options_risk_note"),
        "realized_volatility_20d": merged.get("realized_volatility_20d"),
        "implied_vs_realized_proxy": merged.get("implied_vs_realized_proxy"),
        "put_call_status": merged.get("put_call_status") or "missing",
        "gamma_status": merged.get("gamma_status") or "missing",
    }


def _breadth_proxy(sector_closes: dict[str, list[float]], rsp: list[float], spy: list[float]) -> dict[str, Any]:
    sector_values = list(sector_closes.values())
    above_20 = _percent_above_ma(sector_values, 20)
    above_50 = _percent_above_ma(sector_values, 50)
    above_200 = _percent_above_ma(sector_values, 200)
    sector_participation = above_20
    equal_weight_relative = _relative_return(rsp, spy, 20)
    improvement = _clip((above_20 or 0.0) * 0.45 + (above_50 or 0.0) * 0.25 + max(equal_weight_relative, 0.0) * 6.0, 0.0, 1.0)
    return {
        "advance_decline": "proxy_not_constituent_level",
        "new_highs_new_lows": "missing",
        "percent_above_20d_ma_proxy": above_20,
        "percent_above_50d_ma_proxy": above_50,
        "percent_above_200d_ma_proxy": above_200,
        "equal_weight_vs_cap_weight_20d": equal_weight_relative,
        "sector_participation": sector_participation,
        "breadth_improvement_score": improvement,
        "data_note": "Uses sector ETFs and RSP/SPY proxy, not real constituent breadth.",
    }


def _breadth_from_bundle(symbol: str, breadth_bundle: dict[str, Any] | None) -> dict[str, Any] | None:
    if not breadth_bundle:
        return None
    payload = (breadth_bundle.get("universes") or {}).get(symbol)
    if not payload:
        return None
    metrics = payload.get("metrics") or {}
    scores = payload.get("scores") or {}
    internal = payload.get("internal_resonance") or {}
    if not scores:
        return None
    improvement = _score01(scores.get("breadth_improvement_score"))
    deterioration = _score01(scores.get("breadth_deterioration_score"))
    confirmation = _score01(scores.get("breadth_confirmation_score"), improvement)
    conflict = _score01(scores.get("breadth_conflict_score"), deterioration)
    quality = _score01(scores.get("breadth_quality_score"), 0.5)
    return {
        "source": payload.get("source"),
        "status": payload.get("status"),
        "is_true_breadth": bool(payload.get("is_true_breadth")),
        "is_proxy": bool(payload.get("is_proxy")),
        "latest_date": payload.get("latest_date"),
        "constituents_used": payload.get("constituents_used"),
        "constituents_expected": payload.get("constituents_expected"),
        "coverage_ratio": payload.get("coverage_ratio"),
        "stale_constituents": payload.get("stale_constituents"),
        "stale_price_data": payload.get("stale_price_data"),
        "percent_above_20d": metrics.get("percent_above_20d"),
        "percent_above_50d": metrics.get("percent_above_50d"),
        "percent_above_200d": metrics.get("percent_above_200d"),
        "percent_above_20d_ma_proxy": metrics.get("percent_above_20d"),
        "percent_above_50d_ma_proxy": metrics.get("percent_above_50d"),
        "percent_above_200d_ma_proxy": metrics.get("percent_above_200d"),
        "advancers": metrics.get("advancers"),
        "decliners": metrics.get("decliners"),
        "advance_decline_ratio": metrics.get("advance_decline_ratio"),
        "up_volume_down_volume_ratio": metrics.get("up_volume_down_volume_ratio"),
        "new_highs_20d": metrics.get("new_highs_20d"),
        "new_lows_20d": metrics.get("new_lows_20d"),
        "new_highs_52w": metrics.get("new_highs_52w"),
        "new_lows_52w": metrics.get("new_lows_52w"),
        "percent_above_20d_change_5d": metrics.get("percent_above_20d_change_5d"),
        "percent_above_50d_change_10d": metrics.get("percent_above_50d_change_10d"),
        "improvement_acceleration": metrics.get("improvement_acceleration"),
        "price_rising_breadth_weakening": metrics.get("price_rising_breadth_weakening"),
        "price_falling_breadth_improving": metrics.get("price_falling_breadth_improving"),
        "equal_weight_vs_cap_weight_20d": metrics.get("rsp_spy_relative_strength_20d"),
        "iwm_spy_relative_strength_20d": metrics.get("iwm_spy_relative_strength_20d"),
        "breadth_improvement_score": improvement,
        "breadth_deterioration_score": deterioration,
        "breadth_confirmation_score": confirmation,
        "breadth_conflict_score": conflict,
        "breadth_quality_score": quality,
        "breadth_improvement_score_raw": scores.get("breadth_improvement_score"),
        "breadth_deterioration_score_raw": scores.get("breadth_deterioration_score"),
        "breadth_confirmation_score_raw": scores.get("breadth_confirmation_score"),
        "breadth_conflict_score_raw": scores.get("breadth_conflict_score"),
        "breadth_quality_score_raw": scores.get("breadth_quality_score"),
        "market_internal_resonance_score": _score01(internal.get("resonance_score")),
        "internal_resonance_score_raw": internal.get("resonance_score"),
        "internal_resonance_state": internal.get("resonance_state"),
        "internal_resonance_label": internal.get("resonance_label"),
        "internal_resonance_quality_score": _score01(internal.get("resonance_quality_score"), quality),
        "internal_resonance_quality_score_raw": internal.get("resonance_quality_score"),
        "broad_participation": bool(internal.get("broad_participation")),
        "surface_strength_without_participation": bool(internal.get("surface_strength_without_participation")),
        "supports_bounce_or_repair": bool(internal.get("supports_bounce_or_repair")),
        "supports_downside_or_failed_bounce": bool(internal.get("supports_downside_or_failed_bounce")),
        "internal_resonance_components": internal.get("components") or {},
        "internal_resonance_reason": internal.get("reason"),
        "data_note": payload.get("data_note"),
    }


def _flow_from_bundle(symbol: str, flow_bundle: dict[str, Any] | None) -> dict[str, Any] | None:
    if not flow_bundle:
        return None
    payload = (flow_bundle.get("symbols") or {}).get(symbol)
    if not payload:
        return None
    metrics = payload.get("metrics") or {}
    scores = payload.get("scores") or {}
    quality = _score01(scores.get("flow_quality_score"), 0.0)
    if quality <= 0:
        return None
    risk_off = _score01(scores.get("risk_off_flow_score"), 0.0)
    return {
        "source": payload.get("source"),
        "status": payload.get("status"),
        "is_proxy": bool(payload.get("is_proxy", True)),
        "true_flow_available": bool(payload.get("true_flow_available")),
        "latest_date": payload.get("latest_date"),
        "volume_zscore_20d": metrics.get("volume_zscore_20d"),
        "etf_relative_volume_20d": metrics.get("etf_relative_volume_20d"),
        "volume_confirmation_score": _score01(metrics.get("volume_confirmation_score"), 0.0),
        "high_beta_vs_low_vol_20d": metrics.get("high_beta_vs_low_vol_20d"),
        "small_cap_vs_large_cap_20d": metrics.get("small_cap_vs_large_cap_20d"),
        "equal_weight_vs_cap_weight_20d": metrics.get("equal_weight_vs_cap_weight_20d"),
        "credit_risk_appetite_20d": metrics.get("credit_risk_appetite_20d"),
        "risk_on_rotation_20d": metrics.get("risk_on_rotation_20d"),
        "defensive_vs_cyclical_20d": metrics.get("defensive_vs_cyclical_20d"),
        "sector_participation_proxy": metrics.get("sector_participation_proxy"),
        "risk_on_flow_score": _score01(scores.get("risk_on_flow_score"), 0.0),
        "risk_off_flow_score": risk_off,
        "risk_off_rotation_score": risk_off,
        "flow_confirmation_score": _score01(scores.get("flow_confirmation_score"), 0.0),
        "flow_conflict_score": _score01(scores.get("flow_conflict_score"), risk_off),
        "flow_quality_score": quality,
        "crowding_proxy_score": _score01(scores.get("crowding_proxy_score"), _score01(metrics.get("crowding_proxy_score"), 0.0)),
        "flow_confirmation_score_raw": scores.get("flow_confirmation_score"),
        "flow_conflict_score_raw": scores.get("flow_conflict_score"),
        "flow_quality_score_raw": scores.get("flow_quality_score"),
        "crowding_proxy_score_raw": scores.get("crowding_proxy_score"),
        "data_note": payload.get("data_note"),
    }


def _credit_snapshot(hyg: list[float], lqd: list[float], fred: dict[str, list[float]]) -> dict[str, Any]:
    hy_oas = fred.get("HY_OAS", [])
    ig_oas = fred.get("IG_OAS", [])
    baa_spread = fred.get("BAA_SPREAD", [])
    financial_stress = fred.get("FINANCIAL_STRESS", [])
    hyg_lqd = _relative_return(hyg, lqd, 20)
    hy_change = _change(hy_oas, 20)
    ig_change = _change(ig_oas, 20)
    baa_change = _change(baa_spread, 20)
    stress_change = _change(financial_stress, 20)
    hyg_drawdown = _drawdown(hyg, 60)
    stress_level = _last(financial_stress)
    deterioration = _clip(
        max(hy_change, 0.0) / 2.0
        + max(ig_change, 0.0) / 1.0
        + max(baa_change, 0.0) / 2.0
        + max(stress_change, 0.0) / 2.0
        + max(stress_level or 0.0, 0.0) / 6.0
        + max(-hyg_lqd, 0.0) * 5.0
        + max(-hyg_drawdown, 0.0) * 2.0,
        0.0,
        1.0,
    )
    stabilization = _clip(1.0 - deterioration + max(-hy_change, 0.0) / 2.0 + max(hyg_lqd, 0.0) * 3.0, 0.0, 1.0)
    return {
        "hy_oas": _last(hy_oas),
        "ig_oas": _last(ig_oas),
        "baa_spread_proxy": _last(baa_spread),
        "financial_stress_proxy": stress_level,
        "hy_oas_20d_change": hy_change,
        "ig_oas_20d_change": ig_change,
        "baa_spread_20d_change": baa_change,
        "financial_stress_20d_change": stress_change,
        "hyg_lqd_relative_strength_20d": hyg_lqd,
        "hyg_drawdown_60d": hyg_drawdown,
        "credit_deterioration_score": deterioration,
        "credit_stress_score": deterioration,
        "credit_stabilization_score": stabilization,
    }


def _rates_snapshot(tlt: list[float], uup: list[float], fred: dict[str, list[float]]) -> dict[str, Any]:
    dgs10 = fred.get("DGS10", [])
    dgs2 = fred.get("DGS2", [])
    dgs3mo = fred.get("DGS3MO", [])
    dfii10 = fred.get("DFII10", [])
    recession = fred.get("RECESSION", [])
    ten_two = (_last(dgs10) - _last(dgs2)) if _last(dgs10) is not None and _last(dgs2) is not None else None
    ten_three = (_last(dgs10) - _last(dgs3mo)) if _last(dgs10) is not None and _last(dgs3mo) is not None else None
    inversion_stress = _clip(max(-(ten_two or 0.0), 0.0) / 1.2 + max(-(ten_three or 0.0), 0.0) / 1.5, 0.0, 1.0)
    ten_year_change = _change(dgs10, 20)
    real_yield_change = _change(dfii10, 20)
    recession_latest = _last(recession)
    rates_pressure = _clip(max(ten_year_change, 0.0) / 1.0 + max(real_yield_change, 0.0) / 0.8 + inversion_stress * 0.35, 0.0, 1.0)
    liquidity_stress = _clip(
        inversion_stress * 0.35
        + rates_pressure * 0.25
        + max(_return(uup, 20), 0.0) * 4.0
        + max(-_return(tlt, 20), 0.0) * 2.0
        + max(recession_latest or 0.0, 0.0) * 0.25,
        0.0,
        1.0,
    )
    return {
        "ten_year_yield": _last(dgs10),
        "two_year_yield": _last(dgs2),
        "three_month_yield": _last(dgs3mo),
        "ten_year_minus_two_year": ten_two,
        "ten_year_minus_three_month": ten_three,
        "real_yield_proxy": _last(dfii10),
        "ten_year_yield_20d_change": ten_year_change,
        "real_yield_20d_change": real_yield_change,
        "rates_pressure_score": rates_pressure,
        "recession_proxy": recession_latest,
        "tnx_proxy": None,
        "tlt_return_20d": _return(tlt, 20),
        "uup_return_20d": _return(uup, 20),
        "liquidity_stress_proxy": liquidity_stress,
        "yield_curve_inversion_stress": inversion_stress,
    }


def _flow_proxy(target_volume: list[float], target: list[float], sphb: list[float], splv: list[float], sector_closes: dict[str, list[float]]) -> dict[str, Any]:
    defensive = _basket_return([sector_closes.get("XLP", []), sector_closes.get("XLU", []), sector_closes.get("XLV", [])], 20)
    cyclical = _basket_return([sector_closes.get("XLY", []), sector_closes.get("XLI", []), sector_closes.get("XLF", []), sector_closes.get("XLE", [])], 20)
    high_beta_vs_low_vol = _relative_return(sphb, splv, 20)
    volume_z = _zscore_last(target_volume, 20)
    rel_volume = _relative_volume(target_volume, 20)
    risk_off = _clip(max(defensive - cyclical, 0.0) * 5.0 + max(-high_beta_vs_low_vol, 0.0) * 4.0, 0.0, 1.0)
    return {
        "volume_zscore_20d": volume_z,
        "etf_relative_volume_20d": rel_volume,
        "high_beta_vs_low_vol_20d": high_beta_vs_low_vol,
        "defensive_vs_cyclical_20d": defensive - cyclical,
        "risk_off_rotation_score": risk_off,
        "data_note": "Proxy only; no true fund-flow or positioning feed connected.",
    }


def _market_structure_snapshot(closes: dict[str, list[float]], sector_closes: dict[str, list[float]]) -> dict[str, Any]:
    spy = closes.get("SPY", [])
    qqq = closes.get("QQQ", [])
    iwm = closes.get("IWM", [])
    rsp = closes.get("RSP", [])
    defensive = _basket_return([sector_closes.get("XLP", []), sector_closes.get("XLU", []), sector_closes.get("XLV", [])], 20)
    cyclical = _basket_return([sector_closes.get("XLY", []), sector_closes.get("XLI", []), sector_closes.get("XLF", []), sector_closes.get("XLE", [])], 20)
    return {
        "small_cap_vs_large_cap_20d": _relative_return(iwm, spy, 20),
        "growth_vs_large_cap_20d": _relative_return(qqq, spy, 20),
        "equal_weight_vs_cap_weight_20d": _relative_return(rsp, spy, 20),
        "defensive_vs_cyclical_20d": defensive - cyclical,
        "sector_participation_20d": _percent_above_ma(list(sector_closes.values()), 20),
    }


def _macro_event_calendar_snapshot(as_of: date | None = None) -> dict[str, Any]:
    current = as_of or date.today()
    fomc = _approx_next_fomc(current)
    cpi = _nth_weekday(current.year, current.month, 1, 2)
    if cpi < current:
        next_month = _add_month(current.replace(day=1), 1)
        cpi = _nth_weekday(next_month.year, next_month.month, 1, 2)
    nfp = _nth_weekday(current.year, current.month, 4, 1)
    if nfp < current:
        next_month = _add_month(current.replace(day=1), 1)
        nfp = _nth_weekday(next_month.year, next_month.month, 4, 1)
    opex = _nth_weekday(current.year, current.month, 4, 3)
    if opex < current:
        next_month = _add_month(current.replace(day=1), 1)
        opex = _nth_weekday(next_month.year, next_month.month, 4, 3)
    month_end_days = (_add_month(current.replace(day=1), 1) - timedelta(days=1) - current).days
    quarter_end_month = ((current.month - 1) // 3 + 1) * 3
    quarter_end = date(current.year, quarter_end_month, 1)
    quarter_end = _add_month(quarter_end, 1) - timedelta(days=1)
    macro_event_risk = min(_days_until(cpi, current), _days_until(fomc, current), _days_until(nfp, current), _days_until(opex, current)) <= 3
    return {
        "cpi_date": cpi.isoformat(),
        "fomc_date": fomc.isoformat(),
        "nfp_date": nfp.isoformat(),
        "options_expiry_week": 0 <= _days_until(opex, current) <= 5,
        "month_end_effect": 0 <= month_end_days <= 3,
        "quarter_end_effect": 0 <= (quarter_end - current).days <= 5,
        "macro_event_risk_flag": macro_event_risk,
        "data_note": "Fallback calendar approximation; replace with a real economic calendar for production.",
    }


def _bucket_metrics(cases: list[dict[str, Any]]) -> dict[str, Any]:
    horizons: dict[str, Any] = {}
    for horizon in HORIZONS:
        values = [_float_or_none(case.get(f"forward_return_{horizon}d")) for case in cases]
        clean = [value for value in values if value is not None]
        hit_rate = sum(1 for value in clean if value > 0) / len(clean) if clean else None
        predicted = [_float_or_none(case.get("proxy_confidence")) for case in cases if _float_or_none(case.get(f"forward_return_{horizon}d")) is not None]
        brier = None
        calibration_gap = None
        if clean and predicted:
            actual = [1.0 if value > 0 else 0.0 for value in clean]
            probs = [min(0.95, max(0.05, value or 0.5)) for value in predicted[: len(actual)]]
            brier = sum((prob - outcome) ** 2 for prob, outcome in zip(probs, actual)) / len(actual)
            calibration_gap = (sum(probs) / len(probs)) - (hit_rate or 0.0)
        horizons[f"{horizon}d"] = {
            "sample_size": len(clean),
            "hit_rate": hit_rate,
            "avg_return": sum(clean) / len(clean) if clean else None,
            "median_return": statistics.median(clean) if clean else None,
            "max_adverse_excursion": min((_float_or_none(case.get("max_adverse_excursion")) for case in cases if _float_or_none(case.get("max_adverse_excursion")) is not None), default=None),
            "max_favorable_excursion": max((_float_or_none(case.get("max_favorable_excursion")) for case in cases if _float_or_none(case.get("max_favorable_excursion")) is not None), default=None),
            "brier_score": brier,
            "calibration_gap": calibration_gap,
        }
    return {"sample_size": len(cases), "horizons": horizons}


def _predictor_payload(
    *,
    probability: float,
    confidence: float,
    main_drivers: list[str],
    invalidation_conditions: list[str],
    historical_analog_support: str,
    best_horizon: str,
) -> dict[str, Any]:
    return {
        "probability": round(probability, 4),
        "confidence": round(confidence, 4),
        "main_drivers": main_drivers,
        "invalidation_conditions": invalidation_conditions,
        "historical_analog_support": historical_analog_support,
        "best_horizon": best_horizon,
    }


def _predictor_confidence(data_score: float, agreement: float, analog_support: str) -> float:
    analog = 0.7 if analog_support == "supportive" else 0.45 if analog_support == "weak" else 0.55
    return _clip(data_score * 0.45 + agreement * 0.35 + analog * 0.20, 0.05, 0.90)


def _predictor_spread(predictors: dict[str, Any]) -> float:
    values = [float(payload.get("probability") or 0.0) for payload in predictors.values()]
    if not values:
        return 1.0
    return statistics.pstdev(values)


def _drivers(items: list[tuple[str, float]]) -> list[str]:
    ranked = sorted(items, key=lambda item: item[1], reverse=True)
    return [f"{name}: {value:.2f}" for name, value in ranked[:4]]


def _edge_summary(status: str) -> str:
    return {
        "NO_EDGE": "今天没有足够可用预测优势，应该观察而不是强行判断。",
        "WEAK_EDGE": "存在弱信号，但冲突或数据限制较多。",
        "MODERATE_EDGE": "存在中等预测优势，仍需控制情景风险。",
        "STRONG_EDGE": "数据、信号和历史样本较一致，但仍不是确定性预测。",
    }[status]


def _parse_fred_csv(text: str, lookback_days: int) -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for row in csv.DictReader(text.splitlines()):
        raw_value = row.get("value") or row.get("VALUE") or ""
        if raw_value in {"", "."}:
            continue
        try:
            value = float(raw_value)
        except ValueError:
            continue
        observation_date = row.get("observation_date") or row.get("DATE")
        if not observation_date:
            continue
        rows.append({"date": observation_date, "value": value})
    rows.sort(key=lambda item: str(item["date"]))
    return rows[-lookback_days:]


def _fred_cache_file(series_id: str) -> Path:
    return PROJECT_ROOT / "data" / "fred_cache" / f"{series_id}.json"


def _fmt(value: Any) -> str:
    parsed = _float_or_none(value)
    return "n/a" if parsed is None else f"{parsed:.4f}"


def _closes(series: DownloadedSeries | None) -> list[float]:
    if not series or not is_real_market_data(series):
        return []
    return [float(row["close"]) for row in series.rows if row.get("close") is not None and float(row.get("close") or 0.0) > 0]


def _volumes(series: DownloadedSeries | None) -> list[float]:
    if not series or not is_real_market_data(series):
        return []
    return [float(row.get("volume") or 0.0) for row in series.rows if row.get("volume") is not None]


def _fred_values(series: FredSeries) -> list[float]:
    return [float(row["value"]) for row in series.rows if row.get("value") is not None]


def _latest_date(series: DownloadedSeries | None) -> str | None:
    if not series or not series.rows:
        return None
    return max(str(row["date"]) for row in series.rows if row.get("date"))


def _latest_fred_date(series: FredSeries) -> str | None:
    if not series.rows:
        return None
    return max(str(row["date"]) for row in series.rows if row.get("date"))


def _is_stale(latest_date: str | None, reference_date: str | None, max_days: int) -> bool:
    if not latest_date or not reference_date:
        return True
    try:
        latest = datetime.fromisoformat(latest_date).date()
        reference = datetime.fromisoformat(reference_date).date()
    except ValueError:
        return True
    return (reference - latest).days > max_days


def _last(values: list[float]) -> float | None:
    return values[-1] if values else None


def _return(values: list[float], lookback: int) -> float:
    if len(values) <= lookback or values[-lookback - 1] == 0:
        return 0.0
    return values[-1] / values[-lookback - 1] - 1.0


def _change(values: list[float], lookback: int) -> float:
    if len(values) <= lookback:
        return 0.0
    return values[-1] - values[-lookback - 1]


def _relative_return(left: list[float], right: list[float], lookback: int) -> float:
    return _return(left, lookback) - _return(right, lookback)


def _drawdown(values: list[float], lookback: int) -> float:
    if not values:
        return 0.0
    window = values[-lookback:] if len(values) >= lookback else values
    peak = max(window)
    return values[-1] / peak - 1.0 if peak else 0.0


def _percentile_rank(values: list[float], value: float | None, lookback: int) -> float | None:
    if value is None or not values:
        return None
    window = values[-lookback:] if len(values) >= lookback else values
    below = sum(1 for item in window if item <= value)
    return below / len(window) if window else None


def _percent_above_ma(series_list: list[list[float]], lookback: int) -> float | None:
    valid = [values for values in series_list if len(values) >= lookback]
    if not valid:
        return None
    return sum(1 for values in valid if values[-1] > sum(values[-lookback:]) / lookback) / len(valid)


def _basket_return(series_list: list[list[float]], lookback: int) -> float:
    values = [_return(values, lookback) for values in series_list if len(values) > lookback]
    return sum(values) / len(values) if values else 0.0


def _rsi(values: list[float], period: int) -> float:
    if len(values) <= period:
        return 50.0
    gains: list[float] = []
    losses: list[float] = []
    for previous, current in zip(values[-period - 1 : -1], values[-period:]):
        change = current - previous
        gains.append(max(change, 0.0))
        losses.append(abs(min(change, 0.0)))
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100.0 - (100.0 / (1.0 + rs))


def _realized_vol(values: list[float], lookback: int) -> float:
    if len(values) <= lookback:
        return 0.0
    returns = [values[index] / values[index - 1] - 1.0 for index in range(len(values) - lookback, len(values)) if values[index - 1] != 0]
    if not returns:
        return 0.0
    mean = sum(returns) / len(returns)
    variance = sum((value - mean) ** 2 for value in returns) / len(returns)
    return math.sqrt(variance) * math.sqrt(252.0)


def _zscore_last(values: list[float], lookback: int) -> float:
    if len(values) < lookback:
        return 0.0
    window = values[-lookback:]
    mean = sum(window) / len(window)
    std = statistics.pstdev(window)
    return 0.0 if std == 0 else (window[-1] - mean) / std


def _relative_volume(values: list[float], lookback: int) -> float:
    if len(values) < lookback:
        return 1.0
    avg = sum(values[-lookback:]) / lookback
    return values[-1] / avg if avg else 1.0


def _nth_weekday(year: int, month: int, weekday: int, nth: int) -> date:
    current = date(year, month, 1)
    while current.weekday() != weekday:
        current += timedelta(days=1)
    return current + timedelta(days=7 * (nth - 1))


def _add_month(value: date, months: int) -> date:
    month = value.month - 1 + months
    year = value.year + month // 12
    month = month % 12 + 1
    return date(year, month, 1)


def _approx_next_fomc(current: date) -> date:
    months = (1, 3, 5, 6, 7, 9, 11, 12)
    candidates = [_nth_weekday(current.year, month, 2, 3) for month in months if month >= current.month]
    candidates += [_nth_weekday(current.year + 1, month, 2, 3) for month in months[:2]]
    return min(candidate for candidate in candidates if candidate >= current)


def _days_until(target: date, current: date) -> int:
    return (target - current).days


def _float_or_none(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _score01(value: Any, default: float = 0.0) -> float:
    parsed = _float_or_none(value)
    if parsed is None:
        return default
    if parsed > 1.0:
        parsed = parsed / 100.0
    return _clip(parsed, 0.0, 1.0)


def _clip(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))
