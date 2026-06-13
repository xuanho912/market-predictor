from app.db.tables.predictions_log import PREDICTIONS_LOG_COLUMNS


def test_predictions_log_has_required_columns() -> None:
    required = {
        "timestamp",
        "symbol",
        "horizon",
        "regime",
        "up_probability",
        "down_probability",
        "sideways_probability",
        "bounce_probability",
        "crash_probability",
        "actual_future_return",
        "error_metrics",
    }

    assert required.issubset(PREDICTIONS_LOG_COLUMNS)
