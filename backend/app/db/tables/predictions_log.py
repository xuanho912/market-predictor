from __future__ import annotations


PREDICTIONS_LOG_COLUMNS = (
    "timestamp",
    "symbol",
    "horizon",
    "regime",
    "up_probability",
    "down_probability",
    "sideways_probability",
    "bounce_probability",
    "crash_probability",
    "trend_reversal_probability",
    "actual_future_return",
    "error_metrics",
    "model_version",
    "feature_snapshot_version",
)


PREDICTIONS_LOG_DESCRIPTION = (
    "One row per forecast timestamp, symbol, and horizon. "
    "Actual future returns and error metrics are nullable until the horizon has realized."
)
