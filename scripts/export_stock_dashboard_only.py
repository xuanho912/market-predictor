from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BACKEND_ROOT = PROJECT_ROOT / "backend"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from scripts.providers.stock_data_provider import fetch_stock_data_bundle, load_stock_watchlist
from scripts.stock_prediction_engine import (
    build_stock_prediction_dashboard,
    export_stock_forecast_records_json,
    render_stock_prediction_report,
)
from scripts.stock_radar_ranking_engine import (
    build_stock_radar_validation_scorecard,
    build_top_stock_candidates,
    render_stock_radar_validation_scorecard,
    render_top_stock_candidates_report,
)


PUBLIC_DIR = PROJECT_ROOT / "frontend" / "public"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"


def _read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_text(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(payload, encoding="utf-8")


def main() -> int:
    market_dashboard = _read_json(PUBLIC_DIR / "prediction-dashboard.json")
    if not market_dashboard:
        print("missing frontend/public/prediction-dashboard.json; run full export first")
        return 2

    watchlist_config = load_stock_watchlist()
    stock_data_bundle = fetch_stock_data_bundle(watchlist_config=watchlist_config, lookback_days=520)
    stock_prediction_dashboard = build_stock_prediction_dashboard(
        stock_data_bundle=stock_data_bundle,
        market_dashboard=market_dashboard,
        write_ledger=False,
    )
    top_stock_candidates = build_top_stock_candidates(stock_prediction_dashboard, write_ledger=False)
    stock_radar_validation_scorecard = build_stock_radar_validation_scorecard()
    stock_forecast_records = export_stock_forecast_records_json()

    stock_prediction_dashboard["top_stock_candidates"] = top_stock_candidates
    stock_prediction_dashboard["stock_radar_validation_scorecard"] = stock_radar_validation_scorecard
    market_dashboard["stock_prediction_dashboard"] = stock_prediction_dashboard
    market_dashboard["top_stock_candidates"] = top_stock_candidates
    market_dashboard["stock_radar_validation_scorecard"] = stock_radar_validation_scorecard

    _write_json(PUBLIC_DIR / "stock-prediction-dashboard.json", stock_prediction_dashboard)
    _write_json(PUBLIC_DIR / "top-stock-candidates.json", top_stock_candidates)
    _write_json(PUBLIC_DIR / "stock-forecast-records.json", stock_forecast_records)
    _write_json(PUBLIC_DIR / "stock-radar-validation-scorecard.json", stock_radar_validation_scorecard)
    _write_json(PUBLIC_DIR / "prediction-dashboard.json", market_dashboard)

    _write_text(OUTPUTS_DIR / "stock_prediction_report.md", render_stock_prediction_report(stock_prediction_dashboard))
    _write_text(OUTPUTS_DIR / "top_stock_candidates_report.md", render_top_stock_candidates_report(top_stock_candidates))
    _write_text(OUTPUTS_DIR / "stock_radar_validation_scorecard.md", render_stock_radar_validation_scorecard(stock_radar_validation_scorecard))

    print(
        "wrote stock dashboard:",
        f"{len(stock_prediction_dashboard.get('symbols') or {})} symbols",
        f"{len(top_stock_candidates.get('top_candidates') or [])} candidates",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
