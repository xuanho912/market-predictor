from __future__ import annotations

import json
import math
import os
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from app.services.data_providers.auto_download import DownloadedSeries


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TARGET_SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
EQUITY_FUTURES_SYMBOLS = ("ES=F", "NQ=F", "RTY=F", "YM=F")
OIL_PROXY_SYMBOLS = ("USO", "CL=F")
NEWS_EVENT_MARKET_SYMBOLS = OIL_PROXY_SYMBOLS + EQUITY_FUTURES_SYMBOLS
DEFAULT_TIMEOUT_SECONDS = 10
MAX_GDELT_ITEMS = 40

EVENT_RULES: tuple[dict[str, Any], ...] = (
    {
        "event_type": "geopolitical_risk_easing",
        "narrative": "geopolitics_easing_risk_on",
        "direction": "risk_on",
        "horizon": "1d-5d",
        "keywords": (
            "ceasefire",
            "peace deal",
            "peace talks",
            "de-escalation",
            "truce",
            "reopening",
            "hormuz reopening",
            "diplomatic breakthrough",
            "us iran deal",
            "u.s. iran deal",
            "iran agreement",
            "iran peace",
            "war risk eases",
            "geopolitical risk eases",
            "strait of hormuz reopening",
        ),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "^VIX", "HYG", "LQD", "USO", "CL=F", "UUP", "ES=F", "NQ=F"),
        "importance": 0.80,
    },
    {
        "event_type": "geopolitical_risk_escalation",
        "narrative": "geopolitics_escalation_risk_off",
        "direction": "risk_off",
        "horizon": "intraday-5d",
        "keywords": ("missile", "strike", "war", "attack", "blockade", "hormuz closed", "retaliation", "invasion", "sanctions escalation"),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "^VIX", "USO", "UUP", "TLT"),
        "importance": 0.88,
    },
    {
        "event_type": "oil_shock_relief",
        "narrative": "oil_relief_rally",
        "direction": "risk_on",
        "horizon": "1d-5d",
        "keywords": (
            "oil falls",
            "oil prices fall",
            "oil tumbles",
            "oil plunges",
            "oil plunging",
            "oil slumps",
            "oil falling",
            "oil drops",
            "crude falls",
            "crude drops",
            "crude tumbles",
            "crude plunges",
            "crude plunging",
            "brent falls",
            "brent plunges",
            "supply restored",
            "hormuz reopening",
            "oil shock eases",
        ),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "USO", "CL=F", "XLE", "^VIX"),
        "importance": 0.74,
    },
    {
        "event_type": "oil_shock_risk",
        "narrative": "oil_shock_risk",
        "direction": "risk_off",
        "horizon": "intraday-10d",
        "keywords": ("oil spikes", "oil surges", "crude spikes", "crude surges", "supply disruption", "tanker attack", "hormuz threat"),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "USO", "XLE", "^VIX"),
        "importance": 0.78,
    },
    {
        "event_type": "market_futures_risk_on",
        "narrative": "equity_futures_rally",
        "direction": "risk_on",
        "horizon": "intraday-3d",
        "keywords": (
            "stock futures rise",
            "stock futures jump",
            "stock futures surge",
            "s&p futures rise",
            "s&p 500 futures rise",
            "nasdaq futures rise",
            "dow futures rise",
            "equity futures rally",
            "futures point higher",
        ),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "ES=F", "NQ=F", "RTY=F", "YM=F", "^VIX"),
        "importance": 0.70,
    },
    {
        "event_type": "market_futures_risk_off",
        "narrative": "equity_futures_selloff",
        "direction": "risk_off",
        "horizon": "intraday-3d",
        "keywords": (
            "stock futures fall",
            "stock futures slide",
            "stock futures plunge",
            "s&p futures fall",
            "s&p 500 futures fall",
            "nasdaq futures fall",
            "dow futures fall",
            "equity futures sell off",
            "futures point lower",
        ),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "ES=F", "NQ=F", "RTY=F", "YM=F", "^VIX"),
        "importance": 0.72,
    },
    {
        "event_type": "fed_dovish",
        "narrative": "fed_cut_hopes",
        "direction": "risk_on",
        "horizon": "1d-20d",
        "keywords": ("rate cut", "dovish", "easing", "soft landing", "fed signals cuts", "powell dovish"),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "TLT", "UUP"),
        "importance": 0.70,
    },
    {
        "event_type": "fed_hawkish",
        "narrative": "fed_hawkish_risk",
        "direction": "risk_off",
        "horizon": "1d-20d",
        "keywords": ("hawkish", "higher for longer", "rate hikes", "fed warns", "powell hawkish", "tightening"),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "TLT", "UUP"),
        "importance": 0.72,
    },
    {
        "event_type": "inflation_cooling",
        "narrative": "inflation_cooling",
        "direction": "risk_on",
        "horizon": "1d-20d",
        "keywords": ("inflation cools", "cpi cools", "pce cools", "disinflation", "prices ease"),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "TLT", "UUP"),
        "importance": 0.66,
    },
    {
        "event_type": "inflation_hot",
        "narrative": "inflation_fear",
        "direction": "risk_off",
        "horizon": "1d-20d",
        "keywords": ("hot inflation", "cpi hotter", "pce hotter", "inflation accelerates", "sticky inflation"),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "TLT", "UUP"),
        "importance": 0.70,
    },
    {
        "event_type": "growth_positive",
        "narrative": "growth_positive",
        "direction": "risk_on",
        "horizon": "3d-20d",
        "keywords": ("strong growth", "retail sales beat", "jobs beat", "pmi beats", "earnings beat", "guidance raised"),
        "assets": ("SPY", "QQQ", "IWM", "DIA"),
        "importance": 0.58,
    },
    {
        "event_type": "growth_negative",
        "narrative": "recession_fear",
        "direction": "risk_off",
        "horizon": "3d-20d",
        "keywords": ("recession", "jobs miss", "retail sales miss", "pmi contracts", "guidance cut", "slowdown"),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "TLT", "UUP"),
        "importance": 0.68,
    },
    {
        "event_type": "credit_stress",
        "narrative": "credit_stress",
        "direction": "risk_off",
        "horizon": "3d-60d",
        "keywords": ("credit stress", "default", "downgrade", "bank stress", "liquidity crunch", "funding stress", "commercial real estate stress"),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "HYG", "LQD", "^VIX"),
        "importance": 0.82,
    },
    {
        "event_type": "credit_relief",
        "narrative": "credit_relief",
        "direction": "risk_on",
        "horizon": "3d-20d",
        "keywords": ("credit spreads tighten", "bank relief", "funding markets improve", "downgrade risk eases", "credit relief"),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "HYG", "LQD"),
        "importance": 0.64,
    },
    {
        "event_type": "liquidity_support",
        "narrative": "liquidity_support",
        "direction": "risk_on",
        "horizon": "1d-20d",
        "keywords": ("liquidity injection", "repo support", "central bank support", "stimulus", "policy support", "rescue package"),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "HYG", "TLT"),
        "importance": 0.76,
    },
    {
        "event_type": "liquidity_tightening",
        "narrative": "liquidity_tightening",
        "direction": "risk_off",
        "horizon": "3d-60d",
        "keywords": ("liquidity drain", "quantitative tightening", "repo stress", "funding squeeze", "reserve drain"),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "HYG", "UUP"),
        "importance": 0.78,
    },
    {
        "event_type": "market_microstructure_event",
        "narrative": "market_microstructure_event",
        "direction": "mixed",
        "horizon": "intraday-3d",
        "keywords": ("options expiry", "0dte", "gamma", "rebalancing", "index reconstitution", "short squeeze", "liquidation"),
        "assets": ("SPY", "QQQ", "IWM", "DIA", "^VIX"),
        "importance": 0.56,
    },
)


def fetch_news_event_bundle(
    *,
    finnhub_bundle: dict[str, Any],
    series_by_symbol: dict[str, DownloadedSeries],
    simulated_paths: dict[str, Any] | None = None,
    validation_type: str = "daily",
) -> dict[str, Any]:
    now = datetime.now(timezone.utc)
    finnhub_items = _items_from_finnhub(finnhub_bundle)
    gdelt_status, gdelt_items = _fetch_gdelt_items()
    economic_risk = _economic_calendar_risk(finnhub_bundle, now)
    raw_items = _dedupe_items(finnhub_items + gdelt_items)
    classified = [_classify_item(item, now) for item in raw_items]
    major_events = [
        item
        for item in classified
        if item["event_type"] != "unknown" and item["importance_score"] >= 35 and item["freshness_score"] >= 10
    ]
    major_events.sort(key=lambda item: (item["importance_score"] * 0.7 + item["freshness_score"] * 0.3), reverse=True)
    narrative = _detect_narrative(major_events)
    price_confirmation = _price_reaction_confirmation(narrative, series_by_symbol)
    symbol_impacts = _symbol_impacts(narrative, price_confirmation, simulated_paths or {})
    provider_failed = not finnhub_items and gdelt_status["status"] not in {"available", "stale_cache"}
    status = "available" if major_events else "news_event_partial" if raw_items else "missing"
    if provider_failed:
        status = "provider_failed"
    event_detection_confidence = _mean_score([item.get("confidence_score") for item in major_events])
    stale = bool(gdelt_status.get("stale")) or bool(finnhub_bundle.get("cache_used"))
    event_risk_level = _event_risk_level(narrative, price_confirmation, major_events, economic_risk)
    return {
        "version": "news_event_intelligence_v1",
        "generated_at": now.isoformat(),
        "validation_type": validation_type,
        "status": status,
        "provider_failed": provider_failed,
        "stale": stale,
        "event_detection_confidence": event_detection_confidence,
        "event_risk_level": event_risk_level,
        "news_direction": _news_direction(narrative),
        "sources": {
            "finnhub_market_news": {
                "status": (finnhub_bundle.get("market_news") or {}).get("status", "missing"),
                "item_count": len(finnhub_items),
                "source": (finnhub_bundle.get("market_news") or {}).get("source", "finnhub"),
            },
            "finnhub_economic_calendar": {
                "status": (finnhub_bundle.get("economic_calendar") or {}).get("status", "missing"),
                "event_count": (finnhub_bundle.get("economic_calendar") or {}).get("event_count", 0),
                "source": (finnhub_bundle.get("economic_calendar") or {}).get("source", "finnhub"),
            },
            "gdelt_public_news": gdelt_status,
        },
        "economic_calendar_risk": economic_risk,
        "raw_item_count": len(raw_items),
        "major_event_count": len(major_events),
        "major_events": major_events[:20],
        "market_narrative": narrative,
        "price_reaction_confirmation": price_confirmation,
        "symbol_impacts": symbol_impacts,
        "dashboard_note": _dashboard_note(narrative, price_confirmation),
        "limits": [
            "News/event intelligence is an explanatory forecast input, not a standalone forecast model.",
            "Headline classification is rules-based and must be forward validated before it can raise model confidence materially.",
            "The provider never exposes API keys and never lets frontend call Finnhub directly.",
            "Economic calendar items are treated as event-risk context, not automatic directional forecasts.",
        ],
    }


def render_news_event_status_markdown(payload: dict[str, Any]) -> str:
    narrative = payload.get("market_narrative") or {}
    reaction = payload.get("price_reaction_confirmation") or {}
    lines = [
        "# News / Event Intelligence Status",
        "",
        f"- generated_at: `{payload.get('generated_at')}`",
        f"- status: `{payload.get('status')}`",
        f"- validation_type: `{payload.get('validation_type')}`",
        f"- major_event_count: `{payload.get('major_event_count')}`",
        f"- event_detection_confidence: `{payload.get('event_detection_confidence')}`",
        f"- event_risk_level: `{payload.get('event_risk_level')}`",
        f"- narrative: `{narrative.get('market_narrative')}`",
        f"- narrative_direction: `{narrative.get('narrative_direction')}`",
        f"- narrative_strength: `{narrative.get('narrative_strength')}`",
        f"- price_reaction_confirmed: `{reaction.get('price_reaction_confirmed')}`",
        f"- confirmation_score: `{reaction.get('confirmation_score')}`",
        "",
        "## Dashboard Note",
        "",
        str(payload.get("dashboard_note") or "No clear narrative."),
        "",
        "## Economic Calendar Risk",
        "",
    ]
    economic_risk = payload.get("economic_calendar_risk") or {}
    lines.extend(
        [
            f"- status: `{economic_risk.get('status')}`",
            f"- macro_event_risk_flag: `{economic_risk.get('macro_event_risk_flag')}`",
            f"- macro_event_risk_score: `{economic_risk.get('macro_event_risk_score')}`",
            f"- high_importance_event_count: `{economic_risk.get('high_importance_event_count')}`",
            "",
            "## Major Events",
            "",
        ]
    )
    for event in (payload.get("major_events") or [])[:10]:
        lines.extend(
            [
                f"### {event.get('event_type')} / {event.get('expected_market_direction')}",
                "",
                f"- headline: {event.get('headline')}",
                f"- source: {event.get('source')}",
                f"- published_at: `{event.get('published_at')}`",
                f"- importance_score: `{event.get('importance_score')}`",
                f"- confidence: `{event.get('confidence')}`",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def _items_from_finnhub(bundle: dict[str, Any]) -> list[dict[str, Any]]:
    news = (bundle.get("market_news") or {}).get("items") or []
    items: list[dict[str, Any]] = []
    for item in news:
        if not isinstance(item, dict):
            continue
        items.append(
            {
                "headline": item.get("headline"),
                "summary": item.get("summary"),
                "source": item.get("source") or "Finnhub",
                "published_at": _parse_timestamp(item.get("datetime")),
                "url": item.get("url"),
                "provider": "finnhub",
            }
        )
    return items


def _fetch_gdelt_items() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if os.getenv("NEWS_EVENT_ENABLE_GDELT", "true").lower() in {"0", "false", "no"}:
        return {"status": "disabled", "source": "gdelt", "stale": False}, []
    cache_path = _cache_file("gdelt_market_news")
    query = (
        '(market OR stocks OR "stock futures" OR "s&p futures" OR "nasdaq futures" '
        'OR inflation OR Fed OR oil OR crude OR "oil falls" OR "oil plunges" '
        'OR Iran OR "US Iran" OR "U.S. Iran" OR "peace deal" OR "ceasefire" '
        'OR "Strait of Hormuz" OR "Hormuz reopening" OR credit)'
    )
    params = {
        "query": query,
        "mode": "ArtList",
        "format": "json",
        "maxrecords": str(MAX_GDELT_ITEMS),
        "sort": "HybridRel",
    }
    url = "https://api.gdeltproject.org/api/v2/doc/doc?" + urllib.parse.urlencode(params)
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "market-predictor-news-event/1.0"})
        with urllib.request.urlopen(request, timeout=DEFAULT_TIMEOUT_SECONDS) as response:
            raw = response.read().decode("utf-8")
        payload = json.loads(raw) if raw else {}
        _write_cache(cache_path, payload)
        return {"status": "available", "source": "gdelt", "stale": False}, _items_from_gdelt(payload)
    except Exception as exc:
        cached = _read_cache(cache_path)
        if cached is not None:
            return {
                "status": "stale_cache",
                "source": "local-cache-gdelt",
                "stale": True,
                "error_type": type(exc).__name__,
            }, _items_from_gdelt(cached)
        return {"status": "failed", "source": "gdelt", "stale": False, "error_type": type(exc).__name__}, []


def _items_from_gdelt(payload: dict[str, Any]) -> list[dict[str, Any]]:
    articles = payload.get("articles") if isinstance(payload, dict) else []
    items: list[dict[str, Any]] = []
    for article in articles if isinstance(articles, list) else []:
        if not isinstance(article, dict):
            continue
        items.append(
            {
                "headline": article.get("title"),
                "summary": article.get("seendate") or "",
                "source": article.get("domain") or "GDELT",
                "published_at": _parse_timestamp(article.get("seendate")),
                "url": article.get("url"),
                "provider": "gdelt",
            }
        )
    return items


def _classify_item(item: dict[str, Any], now: datetime) -> dict[str, Any]:
    headline = str(item.get("headline") or "").strip()
    text = f"{headline} {item.get('summary') or ''}".lower()
    condition_tags = _event_condition_tags(text)
    best_rule: dict[str, Any] | None = None
    best_hits = 0
    for rule in EVENT_RULES:
        hits = sum(1 for keyword in rule["keywords"] if keyword in text)
        if hits > best_hits:
            best_rule = rule
            best_hits = hits
    published_at = item.get("published_at")
    freshness = _freshness_score(published_at, now)
    if not best_rule:
        return {
            "headline": headline,
            "source": item.get("source"),
            "published_at": published_at,
            "event_type": "unknown",
            "affected_assets": [],
            "expected_market_direction": "unknown",
            "expected_horizon": "unknown",
            "confidence": "low",
            "importance_score": 0,
            "freshness_score": freshness,
            "detected_event_conditions": condition_tags,
            "provider": item.get("provider"),
        }
    importance = int(round(min(100.0, best_rule["importance"] * 100 + best_hits * 7 + len(condition_tags) * 3 + freshness * 0.10)))
    confidence_score = min(100, 35 + best_hits * 18 + len(condition_tags) * 4 + int(freshness * 0.25))
    return {
        "headline": headline,
        "source": item.get("source"),
        "published_at": published_at,
        "event_type": best_rule["event_type"],
        "affected_assets": list(best_rule["assets"]),
        "expected_market_direction": best_rule["direction"],
        "expected_horizon": best_rule["horizon"],
        "confidence": "high" if confidence_score >= 75 else "medium" if confidence_score >= 50 else "low",
        "confidence_score": confidence_score,
        "importance_score": importance,
        "freshness_score": freshness,
        "narrative": best_rule["narrative"],
        "detected_event_conditions": condition_tags,
        "provider": item.get("provider"),
    }


def _event_condition_tags(text: str) -> list[str]:
    checks = [
        (
            "geopolitical_risk_easing",
            ("peace deal", "ceasefire", "truce", "de-escalation", "war risk eases", "geopolitical risk eases", "hormuz reopening", "strait of hormuz reopening", "iran agreement", "iran peace"),
        ),
        (
            "oil_shock_relief",
            (
                "oil falls",
                "oil prices fall",
                "oil tumbles",
                "oil plunges",
                "oil plunging",
                "oil slumps",
                "oil falling",
                "oil drops",
                "crude falls",
                "crude drops",
                "crude tumbles",
                "crude plunges",
                "crude plunging",
                "brent falls",
                "brent plunges",
                "oil shock eases",
            ),
        ),
        (
            "equity_futures_rally",
            ("stock futures rise", "stock futures jump", "stock futures surge", "s&p futures rise", "nasdaq futures rise", "dow futures rise", "equity futures rally", "futures point higher"),
        ),
        (
            "geopolitical_risk_escalation",
            ("missile", "strike", "war", "attack", "blockade", "hormuz closed", "retaliation", "invasion"),
        ),
        (
            "oil_shock_risk",
            ("oil spikes", "oil surges", "crude spikes", "supply disruption", "hormuz threat"),
        ),
        (
            "equity_futures_selloff",
            ("stock futures fall", "stock futures slide", "stock futures plunge", "futures point lower"),
        ),
    ]
    tags: list[str] = []
    for tag, keywords in checks:
        if any(keyword in text for keyword in keywords):
            tags.append(tag)
    return tags


def _detect_narrative(events: list[dict[str, Any]]) -> dict[str, Any]:
    if not events:
        return {
            "market_narrative": "no_clear_narrative",
            "summary": "当前没有识别到足够清晰的重大新闻叙事。",
            "supporting_headlines": [],
            "conflicting_headlines": [],
            "affected_symbols": list(TARGET_SYMBOLS),
            "affected_scenarios": [],
            "narrative_strength": 0,
            "narrative_direction": "mixed",
            "detected_event_conditions": [],
        }
    grouped: dict[str, list[dict[str, Any]]] = {}
    for event in events:
        grouped.setdefault(str(event.get("narrative") or "no_clear_narrative"), []).append(event)
    narrative_name, narrative_events = max(
        grouped.items(),
        key=lambda pair: sum(float(item.get("importance_score") or 0) * (0.6 + float(item.get("freshness_score") or 0) / 250.0) for item in pair[1]),
    )
    direction = _narrative_direction(narrative_events)
    strength = int(round(min(100.0, sum(float(item.get("importance_score") or 0) for item in narrative_events[:5]) / 3.0)))
    conflicting = [
        item
        for item in events
        if item not in narrative_events and _direction_to_narrative(item.get("expected_market_direction")) != direction
    ]
    condition_tags = sorted(
        {
            str(tag)
            for item in narrative_events
            for tag in (item.get("detected_event_conditions") or [])
            if tag
        }
    )
    return {
        "market_narrative": narrative_name,
        "summary": _narrative_summary(narrative_name, direction),
        "supporting_headlines": [_headline_payload(item) for item in narrative_events[:6]],
        "conflicting_headlines": [_headline_payload(item) for item in conflicting[:6]],
        "affected_symbols": sorted({symbol for item in narrative_events for symbol in item.get("affected_assets", []) if symbol in TARGET_SYMBOLS}) or list(TARGET_SYMBOLS),
        "affected_scenarios": _affected_scenarios(direction),
        "narrative_strength": strength,
        "narrative_direction": direction,
        "detected_event_conditions": condition_tags,
    }


def _price_reaction_confirmation(narrative: dict[str, Any], series_by_symbol: dict[str, DownloadedSeries]) -> dict[str, Any]:
    direction = narrative.get("narrative_direction")
    condition_tags = {str(tag) for tag in (narrative.get("detected_event_conditions") or []) if tag}
    market_check_symbols = TARGET_SYMBOLS + ("^VIX", "HYG", "LQD", "TLT", "UUP") + OIL_PROXY_SYMBOLS + EQUITY_FUTURES_SYMBOLS
    returns = {symbol: _return(series_by_symbol.get(symbol), 1) for symbol in market_check_symbols}
    equity_returns = [value for symbol, value in returns.items() if symbol in TARGET_SYMBOLS and value is not None]
    avg_equity = sum(equity_returns) / len(equity_returns) if equity_returns else None
    futures_returns = [value for symbol in EQUITY_FUTURES_SYMBOLS if (value := returns.get(symbol)) is not None]
    avg_equity_futures = sum(futures_returns) / len(futures_returns) if futures_returns else None
    vix = returns.get("^VIX")
    hyg_lqd = _relative_return(series_by_symbol.get("HYG"), series_by_symbol.get("LQD"), 1)
    oil_returns = [value for symbol in OIL_PROXY_SYMBOLS if (value := returns.get(symbol)) is not None]
    oil = sum(oil_returns) / len(oil_returns) if oil_returns else None
    uup = returns.get("UUP")
    tlt = returns.get("TLT")
    checks: list[tuple[bool, str]] = []
    contradictions: list[str] = []
    if direction in {"supports_bounce", "supports_trend_reversal"}:
        equity_or_futures_positive = (
            (avg_equity is not None and avg_equity > 0) or (avg_equity_futures is not None and avg_equity_futures > 0)
        )
        checks = [
            (equity_or_futures_positive, "股票ETF或股指期货上涨"),
            (vix is not None and vix < 0, "VIX 下跌"),
            (hyg_lqd is not None and hyg_lqd >= -0.002, "HYG/LQD 稳定或走强"),
            (uup is None or uup < 0.004, "美元没有明显走强"),
        ]
        if "oil_shock_relief" in condition_tags or "oil" in str(narrative.get("market_narrative")):
            checks.append((oil is not None and oil < 0, "油价/原油代理回落"))
    elif direction in {"supports_downside", "supports_risk_expansion"}:
        equity_or_futures_negative = (
            (avg_equity is not None and avg_equity < 0) or (avg_equity_futures is not None and avg_equity_futures < 0)
        )
        checks = [
            (equity_or_futures_negative, "股票ETF或股指期货下跌"),
            (vix is not None and vix > 0, "VIX 上升"),
            (hyg_lqd is not None and hyg_lqd < 0, "HYG/LQD 走弱"),
            (uup is not None and uup > 0, "美元走强"),
        ]
        if "oil_shock_risk" in condition_tags or "oil_shock" in str(narrative.get("market_narrative")):
            checks.append((oil is not None and oil > 0, "油价/原油代理上升"))
    else:
        checks = []
    passed = [label for ok, label in checks if ok]
    failed = [label for ok, label in checks if not ok]
    if failed and direction != "mixed":
        contradictions.extend(failed)
    score = int(round((len(passed) / len(checks)) * 100)) if checks else 0
    return {
        "price_reaction_confirmed": bool(checks) and score >= 60,
        "confirmation_score": score,
        "asset_reaction_summary": {
            "avg_equity_1d_return": _round_return(avg_equity),
            "avg_equity_futures_1d_return": _round_return(avg_equity_futures),
            "vix_1d_return": _round_return(vix),
            "hyg_lqd_1d_relative_return": _round_return(hyg_lqd),
            "oil_proxy_1d_return": _round_return(oil),
            "uup_1d_return": _round_return(uup),
            "tlt_1d_return": _round_return(tlt),
            "equity_futures_symbols_used": [symbol for symbol in EQUITY_FUTURES_SYMBOLS if returns.get(symbol) is not None],
            "oil_proxy_symbols_used": [symbol for symbol in OIL_PROXY_SYMBOLS if returns.get(symbol) is not None],
            "confirmed_checks": passed,
            "failed_checks": failed,
        },
        "contradiction_warning": (
            "新闻方向尚未被价格反应确认，可能已经被定价或市场不认可。"
            if contradictions and score < 60
            else None
        ),
    }


def _symbol_impacts(narrative: dict[str, Any], reaction: dict[str, Any], simulated_paths: dict[str, Any]) -> dict[str, Any]:
    impacts: dict[str, Any] = {}
    direction = narrative.get("narrative_direction")
    scenario_bias = _affected_scenarios(direction)
    symbols = (simulated_paths.get("symbols") or {}) if isinstance(simulated_paths, dict) else {}
    for symbol in TARGET_SYMBOLS:
        ranking = (symbols.get(symbol) or {}).get("scenario_ranking") or {}
        primary = (ranking.get("primary") or {}).get("scenario")
        secondary = (ranking.get("secondary") or {}).get("scenario")
        risk = (ranking.get("tertiary") or {}).get("scenario")
        supports_primary = primary in scenario_bias
        conflicts_primary = bool(scenario_bias) and not supports_primary
        impact = "neutral"
        if supports_primary and reaction.get("price_reaction_confirmed"):
            impact = "supports_primary"
        elif supports_primary:
            impact = "text_support_unconfirmed"
        elif conflicts_primary and reaction.get("price_reaction_confirmed"):
            impact = "conflicts_primary"
        elif conflicts_primary:
            impact = "potential_conflict_unconfirmed"
        impacts[symbol] = {
            "primary_scenario": primary,
            "secondary_scenario": secondary,
            "risk_scenario": risk,
            "news_supports_primary_scenario": supports_primary,
            "news_conflicts_primary_scenario": conflicts_primary,
            "scenario_bias": scenario_bias,
            "impact": impact,
            "expected_changes": _expected_changes(direction, reaction.get("price_reaction_confirmed")),
            "explanation": _symbol_explanation(symbol, direction, supports_primary, conflicts_primary, reaction),
        }
    return impacts


def _economic_calendar_risk(finnhub_bundle: dict[str, Any], now: datetime) -> dict[str, Any]:
    calendar = finnhub_bundle.get("economic_calendar") or {}
    events = calendar.get("events") or []
    high_keywords = ("cpi", "pce", "inflation", "fomc", "fed", "payroll", "nonfarm", "nfp", "unemployment", "rate")
    medium_keywords = ("retail", "pmi", "ism", "gdp", "consumer confidence", "jobless", "claims", "ppi")
    macro_events: list[dict[str, Any]] = []
    for event in events if isinstance(events, list) else []:
        if not isinstance(event, dict):
            continue
        name = str(event.get("event") or event.get("name") or "").strip()
        if not name:
            continue
        lower = name.lower()
        event_time = _calendar_event_datetime(event, now)
        days_to_event = (event_time.date() - now.date()).days if event_time is not None else None
        high = any(keyword in lower for keyword in high_keywords)
        medium = any(keyword in lower for keyword in medium_keywords)
        if not high and not medium:
            continue
        if days_to_event is not None and (days_to_event < -1 or days_to_event > 7):
            continue
        importance = "high" if high else "medium"
        macro_events.append(
            {
                "date": event.get("date"),
                "event": name,
                "country": event.get("country"),
                "impact": event.get("impact") or importance,
                "actual": event.get("actual"),
                "estimate": event.get("estimate"),
                "importance": importance,
                "days_to_event": days_to_event,
                "expected_horizon": "intraday-3d" if days_to_event is not None and days_to_event <= 1 else "1d-5d",
                "directional_read": "unknown_until_release",
                "source": calendar.get("source", "finnhub"),
            }
        )
    high_count = sum(1 for event in macro_events if event.get("importance") == "high")
    risk_score = min(100, high_count * 35 + max(0, len(macro_events) - high_count) * 18)
    return {
        "status": calendar.get("status", "missing"),
        "source": calendar.get("source", "finnhub"),
        "event_count": calendar.get("event_count", 0),
        "high_importance_event_count": high_count,
        "macro_event_risk_flag": risk_score >= 35,
        "macro_event_risk_score": risk_score,
        "macro_events": macro_events[:12],
        "risk_note": (
            "Major macro events are present. Treat path confidence as event-sensitive."
            if risk_score >= 35
            else "No near-term high-importance macro event detected from the available calendar."
        ),
    }


def _calendar_event_datetime(event: dict[str, Any], now: datetime) -> datetime | None:
    raw = event.get("date") or event.get("time")
    parsed = _parse_timestamp(raw)
    if parsed:
        try:
            return datetime.fromisoformat(parsed.replace("Z", "+00:00")).astimezone(timezone.utc)
        except ValueError:
            return None
    if isinstance(raw, str) and raw:
        try:
            return datetime.fromisoformat(raw[:10]).replace(tzinfo=timezone.utc)
        except ValueError:
            return None
    return now + timedelta(days=30)


def _event_risk_level(
    narrative: dict[str, Any],
    reaction: dict[str, Any],
    events: list[dict[str, Any]],
    economic_risk: dict[str, Any],
) -> str:
    strength = float(narrative.get("narrative_strength") or 0.0)
    direction = narrative.get("narrative_direction")
    macro_score = float(economic_risk.get("macro_event_risk_score") or 0.0)
    major_risk_off = any(item.get("expected_market_direction") == "risk_off" for item in events[:5])
    unconfirmed = bool(events) and not bool(reaction.get("price_reaction_confirmed"))
    if direction == "supports_risk_expansion" and (strength >= 45 or major_risk_off):
        return "high"
    if macro_score >= 70:
        return "high"
    if strength >= 45 or macro_score >= 35 or unconfirmed:
        return "medium"
    return "low"


def _news_direction(narrative: dict[str, Any]) -> str:
    direction = narrative.get("narrative_direction")
    if direction in {"supports_bounce", "supports_trend_reversal"}:
        return "risk_on"
    if direction in {"supports_downside", "supports_risk_expansion"}:
        return "risk_off"
    return "mixed"


def _dashboard_note(narrative: dict[str, Any], reaction: dict[str, Any]) -> str:
    name = narrative.get("market_narrative")
    if name == "no_clear_narrative":
        return "当前没有识别到足够清晰的重大新闻叙事，新闻层不应主导路径判断。"
    confirm = "已被价格反应初步确认" if reaction.get("price_reaction_confirmed") else "尚未被价格反应充分确认"
    return f"当前新闻叙事为 {name}，方向为 {narrative.get('narrative_direction')}，{confirm}。{narrative.get('summary')}"


def _narrative_direction(events: list[dict[str, Any]]) -> str:
    risk_on = sum(1 for item in events if item.get("expected_market_direction") == "risk_on")
    risk_off = sum(1 for item in events if item.get("expected_market_direction") == "risk_off")
    if risk_on > risk_off:
        return "supports_bounce"
    if risk_off > risk_on:
        return "supports_risk_expansion"
    return "mixed"


def _direction_to_narrative(direction: Any) -> str:
    if direction == "risk_on":
        return "supports_bounce"
    if direction == "risk_off":
        return "supports_risk_expansion"
    return "mixed"


def _affected_scenarios(direction: Any) -> list[str]:
    if direction == "supports_bounce":
        return ["bounce_path", "expected_path", "analog_average_path"]
    if direction == "supports_trend_reversal":
        return ["bounce_path", "expected_path", "analog_average_path"]
    if direction in {"supports_downside", "supports_risk_expansion"}:
        return ["bearish_path"]
    return []


def _expected_changes(direction: Any, confirmed: bool) -> list[str]:
    suffix = "price_confirmed" if confirmed else "needs_price_confirmation"
    if direction in {"supports_bounce", "supports_trend_reversal"}:
        return [f"bounce_path_support_higher:{suffix}", f"failed_bounce_risk_lower:{suffix}", f"risk_expansion_lower:{suffix}"]
    if direction in {"supports_downside", "supports_risk_expansion"}:
        return [f"bearish_path_weight_higher:{suffix}", f"failed_bounce_risk_higher:{suffix}", f"risk_expansion_higher:{suffix}"]
    return ["no_clear_path_change"]


def _symbol_explanation(symbol: str, direction: Any, supports: bool, conflicts: bool, reaction: dict[str, Any]) -> str:
    if direction == "mixed":
        return f"{symbol} 当前新闻叙事混合，不能单独改变路径判断。"
    relation = "支持当前主路径" if supports else "与当前主路径冲突" if conflicts else "对当前主路径影响有限"
    confirm = "价格反应已初步确认" if reaction.get("price_reaction_confirmed") else "价格反应尚未充分确认"
    return f"{symbol} 新闻层{relation}，但仍需结合 VIX、HYG/LQD 和价格触发位；{confirm}。"


def _narrative_summary(name: str, direction: str) -> str:
    summaries = {
        "geopolitics_easing_risk_on": "地缘风险缓和通常支持风险资产反抽，并降低短线风险扩散概率。",
        "oil_relief_rally": "油价冲击缓和通常支持通胀压力下降和风险偏好修复。",
        "fed_cut_hopes": "降息预期升温通常支持估值和久期资产，但需要利率和美元确认。",
        "inflation_fear": "通胀重新升温会提高利率压力，压低风险资产路径可信度。",
        "recession_fear": "增长转弱会增加下跌延续和风险扩散概率。",
        "credit_stress": "信用压力是风险扩散的重要确认信号。",
        "credit_relief": "信用缓和支持反抽或趋势修复，但仍需市场宽度确认。",
        "equity_futures_rally": "股指期货大涨通常表示盘前风险偏好修复，但仍需要现货指数、VIX 和信用代理确认。",
        "equity_futures_selloff": "股指期货走弱通常表示盘前风险偏好恶化，需要观察现货开盘、VIX 和信用代理是否同步恶化。",
        "geopolitics_escalation_risk_off": "地缘风险升级会提高尾部风险和风险扩散概率，尤其需要观察油价、VIX、美元和信用代理。",
        "oil_shock_risk": "油价冲击会抬高通胀和增长压力，若同时伴随 VIX 上升和信用走弱，风险路径权重会提高。",
    }
    return summaries.get(name, f"当前新闻叙事方向为 {direction}，需要价格反应确认。")


def _headline_payload(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "headline": item.get("headline"),
        "source": item.get("source"),
        "published_at": item.get("published_at"),
        "event_type": item.get("event_type"),
        "expected_market_direction": item.get("expected_market_direction"),
        "importance_score": item.get("importance_score"),
        "confidence": item.get("confidence"),
        "detected_event_conditions": item.get("detected_event_conditions") or [],
    }


def _mean_score(values: list[Any]) -> int:
    clean: list[float] = []
    for value in values:
        try:
            parsed = float(value)
        except (TypeError, ValueError):
            continue
        if math.isfinite(parsed):
            clean.append(parsed)
    return int(round(sum(clean) / len(clean))) if clean else 0


def _dedupe_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    clean: list[dict[str, Any]] = []
    for item in items:
        headline = str(item.get("headline") or "").strip()
        if not headline:
            continue
        key = headline.lower()[:180]
        if key in seen:
            continue
        seen.add(key)
        clean.append(item)
    return clean


def _parse_timestamp(value: Any) -> str | None:
    if value in (None, ""):
        return None
    if isinstance(value, (int, float)) and math.isfinite(float(value)):
        try:
            return datetime.fromtimestamp(float(value), timezone.utc).isoformat()
        except Exception:
            return None
    text = str(value).strip()
    for fmt in ("%Y%m%dT%H%M%SZ", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(text, fmt).replace(tzinfo=timezone.utc).isoformat()
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).astimezone(timezone.utc).isoformat()
    except ValueError:
        return None


def _freshness_score(published_at: str | None, now: datetime) -> int:
    if not published_at:
        return 35
    try:
        parsed = datetime.fromisoformat(published_at.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return 35
    hours = max((now - parsed).total_seconds() / 3600.0, 0.0)
    return int(round(max(0.0, 100.0 - hours * 2.4)))


def _return(series: DownloadedSeries | None, days: int) -> float | None:
    closes = _closes(series)
    if len(closes) <= days or closes[-days - 1] == 0:
        return None
    return closes[-1] / closes[-days - 1] - 1.0


def _relative_return(left: DownloadedSeries | None, right: DownloadedSeries | None, days: int) -> float | None:
    left_return = _return(left, days)
    right_return = _return(right, days)
    if left_return is None or right_return is None:
        return None
    return left_return - right_return


def _closes(series: DownloadedSeries | None) -> list[float]:
    if not series:
        return []
    values: list[float] = []
    for row in series.rows:
        if isinstance(row, dict):
            raw_close = row.get("close", row.get("Close", row.get("adj_close", row.get("Adj Close"))))
        else:
            raw_close = getattr(row, "close", None)
        try:
            close = float(raw_close)
        except (TypeError, ValueError):
            continue
        if math.isfinite(close):
            values.append(close)
    return values


def _round_return(value: float | None) -> float | None:
    return round(value, 4) if value is not None and math.isfinite(value) else None


def _cache_file(cache_key: str) -> Path:
    safe = "".join(character if character.isalnum() or character in {"_", "-"} else "_" for character in cache_key)
    configured = os.getenv("NEWS_EVENT_CACHE_DIR")
    base = Path(configured) if configured else PROJECT_ROOT / "data" / "news_event_cache"
    return base / f"{safe}.json"


def _write_cache(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"cached_at": datetime.now(timezone.utc).isoformat(), "payload": payload}, ensure_ascii=False), encoding="utf-8")


def _read_cache(path: Path) -> Any | None:
    if not path.exists():
        return None
    try:
        cached = json.loads(path.read_text(encoding="utf-8"))
        return cached.get("payload")
    except Exception:
        return None
