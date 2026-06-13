from app.services.analysis.feature_importance import build_feature_importance_report


def test_feature_importance_report_has_required_sections() -> None:
    rows = [
        {"price__spy__return__20d__change": 0.1, "credit__spread__stress__20d__level": 0.2, "regime": "bull_market"},
        {"price__spy__return__20d__change": 0.2, "credit__spread__stress__20d__level": 0.8, "regime": "bear_market"},
        {"price__spy__return__20d__change": 0.3, "credit__spread__stress__20d__level": 0.7, "regime": "bear_market"},
        {"price__spy__return__20d__change": 0.8, "credit__spread__stress__20d__level": 0.2, "regime": "bull_market"},
        {"price__spy__return__20d__change": 0.9, "credit__spread__stress__20d__level": 0.1, "regime": "bull_market"},
        {"price__spy__return__20d__change": 0.1, "credit__spread__stress__20d__level": 0.9, "regime": "crisis"},
    ]
    y_true = [0, 1, 1, 0, 0, 1]
    report = build_feature_importance_report(rows, y_true, future_targets={"future_return_20d": [0.01, -0.03, -0.02, 0.02, 0.03, -0.05]})

    assert report.top_20_predictive_features
    assert isinstance(report.ablation_by_group, dict)
    assert report.shap_status in {"ok", "failed", "unavailable"}
