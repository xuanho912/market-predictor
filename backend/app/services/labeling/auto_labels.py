from __future__ import annotations

from app.services.prediction_engine import HORIZONS


def generate_label_plan(symbols: tuple[str, ...]) -> dict[str, object]:
    return {
        "status": "ok",
        "symbols": list(symbols),
        "horizons": list(HORIZONS),
        "labels": [
            "future_return_1d",
            "future_return_3d",
            "future_return_5d",
            "future_return_10d",
            "future_return_20d",
            "future_return_60d",
            "trend_label",
            "pullback_20d",
            "pullback_60d",
            "bounce_10d",
            "bounce_20d",
            "crash_risk_60d",
        ],
        "point_in_time_policy": "features known at t; labels realized only after horizon completion",
    }
