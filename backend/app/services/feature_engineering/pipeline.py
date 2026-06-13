from __future__ import annotations

from app.services.data_providers.auto_download import DownloadedSeries


def generate_core_feature_groups(series: list[DownloadedSeries]) -> dict[str, dict[str, float]]:
    by_symbol = {item.symbol: item for item in series}
    spy = by_symbol.get("SPY")
    qqq = by_symbol.get("QQQ")
    vix = by_symbol.get("^VIX")
    tnx = by_symbol.get("^TNX")
    hyg = by_symbol.get("HYG")
    lqd = by_symbol.get("LQD")
    return {
        "price": _price_features(spy),
        "vol": _vol_features(vix),
        "credit": _credit_features(hyg, lqd),
        "macro": _macro_proxy_features(tnx),
        "liquidity": _liquidity_proxy_features(tnx, hyg),
        "breadth": _breadth_proxy_features(spy, qqq),
    }


def _price_features(series: DownloadedSeries | None) -> dict[str, float]:
    closes = _closes(series)
    return {
        "price__spy__return__1d__change": _return(closes, 1),
        "price__spy__return__20d__change": _return(closes, 20),
        "price__spy__trend__60d__level": _return(closes, 60),
    }


def _vol_features(series: DownloadedSeries | None) -> dict[str, float]:
    closes = _closes(series)
    latest = closes[-1] if closes else 20.0
    return {
        "volatility__vix__level__1d__level": latest / 100.0,
        "volatility__vix__change__20d__change": _return(closes, 20),
    }


def _credit_features(hyg: DownloadedSeries | None, lqd: DownloadedSeries | None) -> dict[str, float]:
    hyg_return = _return(_closes(hyg), 20)
    lqd_return = _return(_closes(lqd), 20)
    return {
        "credit__hyg_lqd__relative_return__20d__cross_signal": hyg_return - lqd_return,
        "credit__spread_proxy__stress__20d__level": max(0.0, lqd_return - hyg_return),
    }


def _macro_proxy_features(tnx: DownloadedSeries | None) -> dict[str, float]:
    closes = _closes(tnx)
    return {"macro__rates_proxy__change__60d__change": _return(closes, 60)}


def _liquidity_proxy_features(tnx: DownloadedSeries | None, hyg: DownloadedSeries | None) -> dict[str, float]:
    return {
        "liquidity__rates_credit__stress__20d__cross_signal": max(0.0, _return(_closes(tnx), 20) - _return(_closes(hyg), 20))
    }


def _breadth_proxy_features(spy: DownloadedSeries | None, qqq: DownloadedSeries | None) -> dict[str, float]:
    spy_return = _return(_closes(spy), 20)
    qqq_return = _return(_closes(qqq), 20)
    return {
        "breadth__spy_qqq__participation__20d__cross_signal": 1.0 if spy_return * qqq_return > 0 else -1.0,
        "breadth__spy_qqq__divergence__20d__divergence": abs(spy_return - qqq_return),
    }


def _closes(series: DownloadedSeries | None) -> list[float]:
    if series is None:
        return []
    return [float(row["close"]) for row in series.rows if "close" in row]


def _return(closes: list[float], periods: int) -> float:
    if len(closes) <= periods or closes[-1 - periods] == 0:
        return 0.0
    return closes[-1] / closes[-1 - periods] - 1.0
