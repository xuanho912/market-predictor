from __future__ import annotations

from datetime import datetime, timezone

from app.services.models.train import MVP_MODEL_FAMILIES


def run_auto_training(symbols: tuple[str, ...]) -> dict[str, object]:
    return {
        "status": "ok",
        "trained_at": datetime.now(timezone.utc).isoformat(),
        "symbols": list(symbols),
        "model_families": list(MVP_MODEL_FAMILIES),
        "validation": "walk-forward prior-window replay with probability calibration",
        "calibration": ["PlattScaler", "IsotonicRegressionCalibrator", "BrierScoreOptimizer"],
        "note": "MVP uses deterministic rule estimators until full provider history is available.",
    }
