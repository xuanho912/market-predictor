from __future__ import annotations

import json
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


CORE_SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")
EASTERN = ZoneInfo("America/New_York")
MARKET_CLOSE_BUFFER = time(16, 30)
MARKET_OPEN_UNCONFIRMED = "market_open_unconfirmed"


def build_data_freshness_status(
    *,
    data_quality_report: dict[str, Any],
    dashboard_as_of: str | None = None,
    now: datetime | None = None,
) -> dict[str, Any]:
    now_utc = _to_utc(now or datetime.now(timezone.utc))
    now_et = now_utc.astimezone(EASTERN)
    today_et = now_et.date()
    expected_latest = expected_latest_trading_date(now_utc)
    is_today_trading_day = is_us_market_trading_day(today_et)

    provider_status = _provider_status(data_quality_report)
    core_dates = _core_market_dates(provider_status)
    latest_market_date = _min_date(core_dates.values()) or _parse_date(dashboard_as_of)
    provider_failed = not core_dates or all(value is None for value in core_dates.values())

    intraday_unconfirmed = bool(
        latest_market_date
        and latest_market_date == today_et
        and is_today_trading_day
        and now_et.time() < MARKET_CLOSE_BUFFER
    )
    stale_days = _trading_days_between(latest_market_date, expected_latest) if latest_market_date else None
    is_latest = bool(latest_market_date and latest_market_date >= expected_latest)

    summary = data_quality_report.get("summary") or {}
    any_provider_stale = bool(summary.get("stale_data")) or any(
        bool(item.get("stale_data")) for item in provider_status.values()
    )

    if provider_failed:
        freshness_status = "provider_failed"
    elif intraday_unconfirmed:
        freshness_status = MARKET_OPEN_UNCONFIRMED
    elif not is_latest and stale_days and stale_days > 0:
        freshness_status = "stale"
    elif not is_today_trading_day and is_latest:
        freshness_status = "market_closed"
    else:
        freshness_status = "fresh"

    affected_symbols = _affected_symbols(
        core_dates=core_dates,
        latest_market_date=latest_market_date,
        expected_latest=expected_latest,
        intraday_unconfirmed=intraday_unconfirmed,
        provider_failed=provider_failed,
    )
    provider_note = (
        "部分辅助数据源使用缓存或存在 stale 标记，但核心 SPY/QQQ/IWM/DIA 行情已到最新应有交易日。"
        if freshness_status in {"fresh", "market_closed"} and any_provider_stale
        else ""
    )
    latest_confirmed_market_date = expected_latest if intraday_unconfirmed else latest_market_date
    warning_message = _warning_message(
        freshness_status=freshness_status,
        latest_market_date=latest_market_date,
        expected_latest=expected_latest,
        now_et=now_et,
        provider_note=provider_note,
    )

    can_append_forecast_record = freshness_status not in {"stale", "provider_failed", MARKET_OPEN_UNCONFIRMED}

    return {
        "version": "data_freshness_gate_v3",
        "generated_at": now_utc.isoformat(),
        "current_date": today_et.isoformat(),
        "current_time_us_eastern": now_et.isoformat(),
        "latest_market_date": _date_str(latest_market_date),
        "latest_confirmed_market_date": _date_str(latest_confirmed_market_date),
        "expected_latest_trading_date": expected_latest.isoformat(),
        "is_latest_trading_day": is_latest,
        "is_today_us_market_trading_day": is_today_trading_day,
        "latest_market_session_status": "intraday_unconfirmed" if intraday_unconfirmed else "completed_or_prior_session",
        "can_append_forecast_record": can_append_forecast_record,
        "can_backfill_completed_outcomes": bool(latest_market_date),
        "stale_days": stale_days if stale_days is not None else "unknown",
        "data_freshness_status": freshness_status,
        "affected_symbols": affected_symbols,
        "provider_status": provider_status,
        "last_successful_core_market_update": _date_str(latest_market_date),
        "last_successful_update": _last_successful_update(provider_status, latest_market_date),
        "warning_message": warning_message,
        "guardrails": [
            "If status is stale or provider_failed, the dashboard must not present the snapshot as a current-day forecast.",
            "If status is market_open_unconfirmed, the snapshot is intraday only and must not append a baseline forecast record.",
            "Backfilling completed historical outcomes is allowed even when a new forecast append is blocked.",
            "Stale/cache fallback data may be shown only with an explicit warning.",
            "Synthetic data is never allowed to create a live forecast signal.",
        ],
    }


def render_data_freshness_markdown(status: dict[str, Any]) -> str:
    lines = [
        "# Data Freshness Status",
        "",
        f"Generated at: `{status.get('generated_at')}`",
        "",
        "## Summary",
        "",
        f"- current_date: `{status.get('current_date')}`",
        f"- current_time_us_eastern: `{status.get('current_time_us_eastern')}`",
        f"- latest_market_date: `{status.get('latest_market_date')}`",
        f"- latest_confirmed_market_date: `{status.get('latest_confirmed_market_date')}`",
        f"- expected_latest_trading_date: `{status.get('expected_latest_trading_date')}`",
        f"- is_latest_trading_day: `{status.get('is_latest_trading_day')}`",
        f"- latest_market_session_status: `{status.get('latest_market_session_status')}`",
        f"- can_append_forecast_record: `{status.get('can_append_forecast_record')}`",
        f"- can_backfill_completed_outcomes: `{status.get('can_backfill_completed_outcomes')}`",
        f"- stale_days: `{status.get('stale_days')}`",
        f"- data_freshness_status: `{status.get('data_freshness_status')}`",
        f"- last_successful_core_market_update: `{status.get('last_successful_core_market_update')}`",
        f"- last_successful_update: `{status.get('last_successful_update')}`",
        f"- warning_message: {status.get('warning_message')}",
        "",
        "## Affected Symbols",
        "",
    ]
    affected = status.get("affected_symbols") or []
    lines.extend(f"- `{symbol}`" for symbol in affected) if affected else lines.append("- none")

    lines.extend(["", "## Provider Status", ""])
    for name, payload in sorted((status.get("provider_status") or {}).items()):
        lines.append(
            "- "
            f"{name}: status=`{payload.get('status')}`, latest_date=`{payload.get('latest_date')}`, "
            f"source=`{payload.get('source')}`, stale=`{payload.get('stale_data')}`, "
            f"fallback=`{payload.get('fallback_used')}`, real_data=`{payload.get('real_data')}`"
        )

    lines.extend(["", "## Guardrails", ""])
    lines.extend(f"- {item}" for item in status.get("guardrails") or [])
    lines.append("")
    return "\n".join(lines)


def expected_latest_trading_date(now_utc: datetime | None = None) -> date:
    now_utc = _to_utc(now_utc or datetime.now(timezone.utc))
    now_et = now_utc.astimezone(EASTERN)
    candidate = now_et.date()
    if is_us_market_trading_day(candidate) and now_et.time() >= MARKET_CLOSE_BUFFER:
        return candidate
    return previous_us_market_trading_day(candidate)


def is_us_market_trading_day(day: date) -> bool:
    if day.weekday() >= 5:
        return False
    return day not in us_market_holidays(day.year)


def previous_us_market_trading_day(day: date) -> date:
    candidate = day - timedelta(days=1)
    while not is_us_market_trading_day(candidate):
        candidate -= timedelta(days=1)
    return candidate


def us_market_holidays(year: int) -> set[date]:
    return {
        _observed(date(year, 1, 1)),
        _nth_weekday(year, 1, 0, 3),
        _nth_weekday(year, 2, 0, 3),
        _good_friday(year),
        _last_weekday(year, 5, 0),
        _observed(date(year, 6, 19)),
        _observed(date(year, 7, 4)),
        _nth_weekday(year, 9, 0, 1),
        _nth_weekday(year, 11, 3, 4),
        _observed(date(year, 12, 25)),
    }


def write_data_freshness_outputs(status: dict[str, Any], *, public_dir: Path, outputs_dir: Path) -> None:
    public_dir.mkdir(parents=True, exist_ok=True)
    outputs_dir.mkdir(parents=True, exist_ok=True)
    (public_dir / "data-freshness-status.json").write_text(
        json.dumps(status, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (outputs_dir / "data_freshness_status.md").write_text(
        render_data_freshness_markdown(status),
        encoding="utf-8",
    )


def _provider_status(data_quality_report: dict[str, Any]) -> dict[str, Any]:
    sources = data_quality_report.get("sources") or {}
    provider_status: dict[str, Any] = {}
    for name, source in sources.items():
        if not isinstance(source, dict):
            continue
        provider_status[str(name)] = {
            "symbol": source.get("symbol") or name,
            "source": source.get("source"),
            "status": source.get("status") or ("available" if source.get("real_data") else "missing"),
            "latest_date": _date_str(_parse_date(source.get("latest_date"))),
            "rows": source.get("rows"),
            "real_data": bool(source.get("real_data")),
            "fallback_used": bool(source.get("fallback_used")),
            "stale_data": bool(source.get("stale_data")),
            "missing_data": bool(source.get("missing_data")),
            "point_in_time_safe": bool(source.get("point_in_time_safe", True)),
        }
    return provider_status


def _core_market_dates(provider_status: dict[str, Any]) -> dict[str, date | None]:
    dates: dict[str, date | None] = {}
    for symbol in CORE_SYMBOLS:
        candidates = [
            payload
            for payload in provider_status.values()
            if str(payload.get("symbol") or "").upper() == symbol
        ]
        parsed_dates = [_parse_date(item.get("latest_date")) for item in candidates]
        parsed_dates = [item for item in parsed_dates if item is not None]
        dates[symbol] = max(parsed_dates) if parsed_dates else None
    return dates


def _affected_symbols(
    *,
    core_dates: dict[str, date | None],
    latest_market_date: date | None,
    expected_latest: date,
    intraday_unconfirmed: bool,
    provider_failed: bool,
) -> list[str]:
    affected: list[str] = []
    for symbol in CORE_SYMBOLS:
        symbol_date = core_dates.get(symbol)
        if provider_failed or symbol_date is None:
            affected.append(symbol)
        elif symbol_date < expected_latest:
            affected.append(symbol)
        elif latest_market_date and symbol_date < latest_market_date:
            affected.append(symbol)
        elif intraday_unconfirmed:
            affected.append(symbol)
    return affected


def _last_successful_update(provider_status: dict[str, Any], fallback: date | None) -> str | None:
    dates = [
        _parse_date(payload.get("latest_date"))
        for payload in provider_status.values()
        if payload.get("real_data") and not payload.get("missing_data")
    ]
    dates = [item for item in dates if item is not None]
    return _date_str(max(dates) if dates else fallback)


def _trading_days_between(start: date | None, end: date) -> int | None:
    if start is None:
        return None
    if start >= end:
        return 0
    count = 0
    cursor = start
    while cursor < end:
        cursor += timedelta(days=1)
        if is_us_market_trading_day(cursor):
            count += 1
    return count


def _warning_message(
    *,
    freshness_status: str,
    latest_market_date: date | None,
    expected_latest: date,
    now_et: datetime,
    provider_note: str,
) -> str:
    latest = _date_str(latest_market_date) or "unknown"
    if freshness_status == "provider_failed":
        return "核心市场数据源失败，当前预测不可作为今日判断。"
    if freshness_status == "stale":
        return (
            "数据已过期，当前预测不可作为今日判断。"
            f" 核心行情最新日期为 {latest}，按美股交易日应至少更新到 {expected_latest.isoformat()}。"
        )
    if freshness_status == MARKET_OPEN_UNCONFIRMED:
        return (
            "当前行情日期来自美股盘中快照，尚未形成收盘确认数据。"
            f" 盘中快照日期为 {latest}；正式 baseline_v1 预测记录应等美东 "
            f"{MARKET_CLOSE_BUFFER.strftime('%H:%M')} 后重新生成。"
        )
    if freshness_status == "market_closed":
        return (
            f"美股当前没有新的完整交易日，使用最近完成交易日 {latest} 的数据。"
            f" 当前美东时间 {now_et.strftime('%Y-%m-%d %H:%M')}。"
        )
    base = f"核心行情已更新至最新应有交易日 {latest}。"
    return f"{base} {provider_note}".strip()


def _parse_date(value: Any) -> date | None:
    if value is None:
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, datetime):
        return value.date()
    text = str(value).strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
    except ValueError:
        pass
    try:
        return datetime.strptime(text[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def _date_str(value: date | None) -> str | None:
    return value.isoformat() if value else None


def _min_date(values: Any) -> date | None:
    parsed = [item for item in values if item is not None]
    return min(parsed) if parsed else None


def _to_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def _observed(day: date) -> date:
    if day.weekday() == 5:
        return day - timedelta(days=1)
    if day.weekday() == 6:
        return day + timedelta(days=1)
    return day


def _nth_weekday(year: int, month: int, weekday: int, nth: int) -> date:
    candidate = date(year, month, 1)
    while candidate.weekday() != weekday:
        candidate += timedelta(days=1)
    return candidate + timedelta(days=7 * (nth - 1))


def _last_weekday(year: int, month: int, weekday: int) -> date:
    candidate = date(year, 12, 31) if month == 12 else date(year, month + 1, 1) - timedelta(days=1)
    while candidate.weekday() != weekday:
        candidate -= timedelta(days=1)
    return candidate


def _good_friday(year: int) -> date:
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return date(year, month, day) - timedelta(days=2)
