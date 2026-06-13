from __future__ import annotations

from fastapi import FastAPI, HTTPException, Query

from app.db.storage import initialize_database, load_history, save_prediction
from app.schemas.predictions import BacktestSummary, FeatureSnapshot, HorizonForecast, PredictionSnapshot
from app.services.analysis.historical_analogs import (
    build_alpha_v1_analog_report,
    build_historical_analog_report,
    build_similar_days_payload,
)
from app.services.backtesting.summary import build_backtest_summary
from app.services.backtesting.walk_forward_engine import build_evaluation_report, run_walk_forward_backtest
from app.services.data_providers.auto_download import refresh_market_data
from app.services.data_providers.catalog import PROVIDER_CATALOG
from app.services.feature_engineering.pipeline import generate_core_feature_groups
from app.services.feature_engineering.registry import FEATURE_GROUPS, FEATURE_TRANSFORMS
from app.services.labeling.auto_labels import generate_label_plan
from app.services.models.auto_train import run_auto_training
from app.services.prediction_engine import SUPPORTED_SYMBOLS, build_prediction, latest_features, normalize_symbol
from app.services.scheduler import start_scheduler
from app.services.signals.regime import REGIME_VALUES
from app.services.validation.forward_alpha_tracker import (
    alpha_status_payload,
    latest_alpha_payload,
    report_payload,
    run_daily_forward_observation,
    signal_rows_payload,
)

app = FastAPI(
    title="market-predictor API",
    description="Probability-first market trend prediction engine.",
    version="0.2.0",
)

LAST_REFRESH_SUMMARY: dict[str, object] = {"status": "not_started"}
LAST_TRAINING_SUMMARY: dict[str, object] = {"status": "not_started"}
LAST_LABEL_SUMMARY: dict[str, object] = {"status": "not_started"}


def refresh_predictions() -> None:
    global LAST_LABEL_SUMMARY, LAST_REFRESH_SUMMARY, LAST_TRAINING_SUMMARY
    downloaded = refresh_market_data()
    feature_groups = generate_core_feature_groups(downloaded)
    LAST_LABEL_SUMMARY = generate_label_plan(SUPPORTED_SYMBOLS)
    LAST_TRAINING_SUMMARY = run_auto_training(SUPPORTED_SYMBOLS)
    LAST_REFRESH_SUMMARY = {
        "status": "ok",
        "downloaded_series": [{"symbol": item.symbol, "source": item.source, "rows": len(item.rows)} for item in downloaded],
        "generated_feature_groups": sorted(feature_groups),
        "labels": LAST_LABEL_SUMMARY,
        "training": LAST_TRAINING_SUMMARY,
    }
    for symbol in SUPPORTED_SYMBOLS:
        save_prediction(build_prediction(symbol))


@app.on_event("startup")
def startup() -> None:
    initialize_database()
    refresh_predictions()
    start_scheduler(refresh_predictions, run_daily_forward_observation)


@app.get("/health")
@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "engine": "market-predictor", "trading_enabled": "false"}


@app.get("/api/markets")
def markets() -> dict[str, list[str]]:
    return {"symbols": list(SUPPORTED_SYMBOLS)}


@app.get("/api/prediction/latest", response_model=PredictionSnapshot)
def prediction_latest(symbol: str = Query(default="SPY")) -> PredictionSnapshot:
    try:
        snapshot = build_prediction(normalize_symbol(symbol))
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    save_prediction(snapshot)
    return snapshot


@app.get("/api/prediction/history", response_model=list[PredictionSnapshot])
def prediction_history(symbol: str = Query(default="SPY"), limit: int = Query(default=50, ge=1, le=500)) -> list[PredictionSnapshot]:
    try:
        normalized = normalize_symbol(symbol)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    history = load_history(normalized, limit=limit)
    if history:
        return history
    snapshot = build_prediction(normalized)
    save_prediction(snapshot)
    return [snapshot]


@app.get("/api/prediction/horizon", response_model=HorizonForecast)
def prediction_horizon(symbol: str = Query(default="SPY"), horizon: str = Query(default="5d")) -> HorizonForecast:
    snapshot = prediction_latest(symbol)
    for forecast in snapshot.horizons:
        if forecast.horizon == horizon:
            return forecast
    raise HTTPException(status_code=404, detail=f"Unsupported horizon: {horizon}")


@app.get("/api/features/latest", response_model=FeatureSnapshot)
def features_latest(symbol: str = Query(default="SPY")) -> FeatureSnapshot:
    try:
        return latest_features(normalize_symbol(symbol))
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@app.get("/api/explanations/latest")
def explanations_latest(symbol: str = Query(default="SPY")) -> dict[str, object]:
    snapshot = prediction_latest(symbol)
    return {
        "symbol": snapshot.symbol,
        "forecast_timestamp": snapshot.forecast_timestamp,
        "market_regime": snapshot.market_regime,
        "top_reasons": snapshot.top_reasons,
        "risk_source_breakdown": snapshot.risk_source_breakdown,
    }


@app.get("/api/similar-days")
def similar_days(symbol: str = Query(default="SPY")) -> dict[str, object]:
    snapshot = prediction_latest(symbol)
    return {"symbol": snapshot.symbol, "historical_similar_days": snapshot.historical_similar_days}


@app.get("/api/analogs/latest")
def analogs_latest(symbol: str = Query(default="SPY"), top_k: int = Query(default=20, ge=1, le=100)) -> dict[str, object]:
    try:
        return build_historical_analog_report(normalize_symbol(symbol), top_k=top_k)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@app.get("/api/analogs/alpha-v1")
def analogs_alpha_v1(symbol: str = Query(default="SPY"), top_k: int = Query(default=20, ge=1, le=100)) -> dict[str, object]:
    try:
        return build_alpha_v1_analog_report(normalize_symbol(symbol), top_k=top_k)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@app.get("/api/analogs/similar-days")
def analogs_similar_days(symbol: str = Query(default="SPY"), top_k: int = Query(default=20, ge=1, le=100)) -> dict[str, object]:
    try:
        return build_similar_days_payload(normalize_symbol(symbol), top_k=top_k)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@app.get("/api/backtest/summary", response_model=BacktestSummary)
def backtest_summary(symbol: str = Query(default="SPY")) -> BacktestSummary:
    try:
        return build_backtest_summary(normalize_symbol(symbol))
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@app.post("/api/admin/refresh-data")
def admin_refresh_data() -> dict[str, object]:
    refresh_predictions()
    return {"status": "ok", "refreshed_symbols": list(SUPPORTED_SYMBOLS), "data_refresh": LAST_REFRESH_SUMMARY}


@app.post("/api/admin/retrain")
def admin_retrain() -> dict[str, object]:
    global LAST_TRAINING_SUMMARY
    LAST_TRAINING_SUMMARY = run_auto_training(SUPPORTED_SYMBOLS)
    return LAST_TRAINING_SUMMARY


@app.post("/api/admin/run-backtest")
def admin_run_backtest(symbol: str = Query(default="SPY")) -> BacktestSummary:
    run_walk_forward_backtest(symbol=symbol, persist=True)
    return backtest_summary(symbol)


@app.get("/api/evaluation/report")
def evaluation_report(symbol: str = Query(default="SPY")) -> dict[str, object]:
    try:
        return build_evaluation_report(normalize_symbol(symbol))
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@app.get("/api/alpha/v1/status")
def alpha_v1_status() -> dict[str, object]:
    return alpha_status_payload()


@app.get("/api/alpha/v1/latest")
def alpha_v1_latest() -> dict[str, object]:
    return latest_alpha_payload()


@app.get("/api/alpha/v1/signals")
def alpha_v1_signals() -> dict[str, object]:
    return signal_rows_payload()


@app.get("/api/alpha/v1/report")
def alpha_v1_report() -> dict[str, object]:
    return report_payload()


@app.get("/api/v1/metadata/feature-groups")
def feature_groups() -> dict[str, list[str]]:
    return {"groups": list(FEATURE_GROUPS)}


@app.get("/api/v1/metadata/feature-transforms")
def feature_transforms() -> dict[str, list[str]]:
    return {"transforms": list(FEATURE_TRANSFORMS)}


@app.get("/api/v1/metadata/regimes")
def regimes() -> dict[str, list[str]]:
    return {"regimes": list(REGIME_VALUES)}


@app.get("/api/v1/metadata/provider-catalog")
def provider_catalog() -> dict[str, list[dict[str, object]]]:
    return {
        "providers": [
            {
                "provider_id": provider.provider_id,
                "feature_group": provider.feature_group,
                "required_coverage": list(provider.required_coverage),
                "point_in_time_policy": provider.point_in_time_policy,
                "revision_policy": provider.revision_policy,
            }
            for provider in PROVIDER_CATALOG
        ]
    }
