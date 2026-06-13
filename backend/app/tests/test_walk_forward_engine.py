from app.services.backtesting.walk_forward_engine import build_evaluation_report, run_walk_forward_backtest


def test_walk_forward_backtest_outputs_required_metrics() -> None:
    result = run_walk_forward_backtest("SPY", days=220, train_window=80, persist=False)

    assert result["prediction_count"] > 0
    assert "accuracy_by_horizon" in result
    assert "brier_score_by_horizon" in result
    assert "calibration_curve_by_horizon" in result
    assert "regime_breakdown_performance" in result


def test_evaluation_report_contains_edge_score() -> None:
    report = build_evaluation_report("QQQ")

    assert "overall_prediction_accuracy" in report
    assert "by_regime_accuracy" in report
    assert "by_horizon_accuracy" in report
    assert "expected_trading_edge_score" in report
