from __future__ import annotations

import json
import os
import sqlite3
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from app.schemas.predictions import PredictionSnapshot


def database_path() -> Path:
    configured = os.getenv("PREDICTION_DB_PATH")
    if configured:
        return Path(configured)
    return Path(os.getenv("PREDICTION_STORE_PATH", "./data")) / "market_predictor.sqlite"


def connect() -> sqlite3.Connection:
    path = database_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    with connect() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS prediction_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT NOT NULL,
                forecast_timestamp TEXT NOT NULL,
                payload TEXT NOT NULL
            )
            """
        )
        connection.execute("CREATE INDEX IF NOT EXISTS idx_prediction_symbol_time ON prediction_records(symbol, forecast_timestamp)")
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS predictions_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                symbol TEXT NOT NULL,
                horizon TEXT NOT NULL,
                regime TEXT NOT NULL,
                up_probability REAL NOT NULL,
                down_probability REAL NOT NULL,
                sideways_probability REAL NOT NULL,
                bounce_probability REAL NOT NULL,
                crash_probability REAL NOT NULL,
                trend_reversal_probability REAL NOT NULL,
                actual_future_return REAL,
                error_metrics TEXT NOT NULL DEFAULT '{}',
                model_version TEXT NOT NULL,
                feature_snapshot_version TEXT NOT NULL
            )
            """
        )
        connection.execute("CREATE INDEX IF NOT EXISTS idx_predictions_log_symbol_time ON predictions_log(symbol, timestamp)")
        connection.execute("CREATE INDEX IF NOT EXISTS idx_predictions_log_symbol_horizon ON predictions_log(symbol, horizon)")


def save_prediction(snapshot: "PredictionSnapshot") -> None:
    initialize_database()
    with connect() as connection:
        connection.execute(
            "INSERT INTO prediction_records(symbol, forecast_timestamp, payload) VALUES (?, ?, ?)",
            (snapshot.symbol, snapshot.forecast_timestamp.isoformat(), snapshot.model_dump_json()),
        )
        _insert_prediction_log_rows(connection, snapshot)


def load_history(symbol: str, limit: int = 50) -> list["PredictionSnapshot"]:
    from app.schemas.predictions import PredictionSnapshot

    initialize_database()
    with connect() as connection:
        rows = connection.execute(
            """
            SELECT payload
            FROM prediction_records
            WHERE symbol = ?
            ORDER BY forecast_timestamp DESC
            LIMIT ?
            """,
            (symbol, limit),
        ).fetchall()
    return [PredictionSnapshot.model_validate(json.loads(row["payload"])) for row in rows]


def save_prediction_log_rows(rows: list[dict[str, Any]]) -> None:
    initialize_database()
    with connect() as connection:
        connection.executemany(
            """
            INSERT INTO predictions_log(
                timestamp,
                symbol,
                horizon,
                regime,
                up_probability,
                down_probability,
                sideways_probability,
                bounce_probability,
                crash_probability,
                trend_reversal_probability,
                actual_future_return,
                error_metrics,
                model_version,
                feature_snapshot_version
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    row["timestamp"],
                    row["symbol"],
                    row["horizon"],
                    row["regime"],
                    row["up_probability"],
                    row["down_probability"],
                    row["sideways_probability"],
                    row["bounce_probability"],
                    row["crash_probability"],
                    row["trend_reversal_probability"],
                    row.get("actual_future_return"),
                    json.dumps(row.get("error_metrics", {}), sort_keys=True),
                    row["model_version"],
                    row["feature_snapshot_version"],
                )
                for row in rows
            ],
        )


def load_prediction_log(symbol: str, limit: int = 500) -> list[dict[str, Any]]:
    initialize_database()
    with connect() as connection:
        rows = connection.execute(
            """
            SELECT *
            FROM predictions_log
            WHERE symbol = ?
            ORDER BY timestamp DESC
            LIMIT ?
            """,
            (symbol, limit),
        ).fetchall()
    records: list[dict[str, Any]] = []
    for row in rows:
        record = dict(row)
        record["error_metrics"] = json.loads(record.get("error_metrics") or "{}")
        records.append(record)
    return records


def _insert_prediction_log_rows(connection: sqlite3.Connection, snapshot: PredictionSnapshot) -> None:
    rows = []
    for forecast in snapshot.horizons:
        rows.append(
            {
                "timestamp": snapshot.forecast_timestamp.isoformat(),
                "symbol": snapshot.symbol,
                "horizon": forecast.horizon,
                "regime": snapshot.market_regime,
                "up_probability": forecast.up_probability,
                "down_probability": forecast.down_probability,
                "sideways_probability": forecast.sideways_probability,
                "bounce_probability": snapshot.bounce_probability,
                "crash_probability": snapshot.model_layers.long_term_vulnerability.crisis_probability_12m,
                "trend_reversal_probability": snapshot.trend_reversal_probability,
                "actual_future_return": None,
                "error_metrics": {},
                "model_version": snapshot.model_version,
                "feature_snapshot_version": snapshot.feature_snapshot_version,
            }
        )
    connection.executemany(
        """
        INSERT INTO predictions_log(
            timestamp,
            symbol,
            horizon,
            regime,
            up_probability,
            down_probability,
            sideways_probability,
            bounce_probability,
            crash_probability,
            trend_reversal_probability,
            actual_future_return,
            error_metrics,
            model_version,
            feature_snapshot_version
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                row["timestamp"],
                row["symbol"],
                row["horizon"],
                row["regime"],
                row["up_probability"],
                row["down_probability"],
                row["sideways_probability"],
                row["bounce_probability"],
                row["crash_probability"],
                row["trend_reversal_probability"],
                row["actual_future_return"],
                json.dumps(row["error_metrics"], sort_keys=True),
                row["model_version"],
                row["feature_snapshot_version"],
            )
            for row in rows
        ],
    )
