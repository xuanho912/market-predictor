from __future__ import annotations

import math
from dataclasses import dataclass


EPSILON = 1e-9


@dataclass(frozen=True)
class CalibrationResult:
    method: str
    raw_probability: float
    calibrated_probability: float


def clamp_probability(value: float) -> float:
    return min(max(value, EPSILON), 1.0 - EPSILON)


def identity_calibration(raw_probability: float) -> CalibrationResult:
    calibrated = clamp_probability(raw_probability)
    return CalibrationResult(method="identity", raw_probability=raw_probability, calibrated_probability=calibrated)


def brier_score(y_true: list[int], probabilities: list[float]) -> float:
    _validate_lengths(y_true, probabilities)
    return sum((clamp_probability(p) - y) ** 2 for y, p in zip(y_true, probabilities)) / len(y_true)


def log_loss_score(y_true: list[int], probabilities: list[float]) -> float:
    _validate_lengths(y_true, probabilities)
    total = 0.0
    for y, probability in zip(y_true, probabilities):
        p = clamp_probability(probability)
        total += -(y * math.log(p) + (1 - y) * math.log(1 - p))
    return total / len(y_true)


def calibration_curve(y_true: list[int], probabilities: list[float], bins: int = 10) -> list[dict[str, float]]:
    _validate_lengths(y_true, probabilities)
    if bins <= 0:
        raise ValueError("bins must be positive")
    bucketed: list[list[tuple[int, float]]] = [[] for _ in range(bins)]
    for y, probability in zip(y_true, probabilities):
        p = clamp_probability(probability)
        index = min(int(p * bins), bins - 1)
        bucketed[index].append((y, p))
    curve: list[dict[str, float]] = []
    for index, bucket in enumerate(bucketed):
        if bucket:
            observed = sum(y for y, _ in bucket) / len(bucket)
            predicted = sum(p for _, p in bucket) / len(bucket)
        else:
            observed = 0.0
            predicted = (index + 0.5) / bins
        curve.append({"bin": index, "predicted_probability": round(predicted, 6), "observed_frequency": round(observed, 6), "count": len(bucket)})
    return curve


class PlattScaler:
    """One-dimensional Platt scaling with deterministic gradient descent."""

    def __init__(self, learning_rate: float = 0.05, iterations: int = 500) -> None:
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.a = 1.0
        self.b = 0.0

    def fit(self, raw_scores: list[float], y_true: list[int]) -> "PlattScaler":
        _validate_lengths(y_true, raw_scores)
        for _ in range(self.iterations):
            grad_a = 0.0
            grad_b = 0.0
            for score, y in zip(raw_scores, y_true):
                prediction = 1.0 / (1.0 + math.exp(-(self.a * score + self.b)))
                error = prediction - y
                grad_a += error * score
                grad_b += error
            n = len(raw_scores)
            self.a -= self.learning_rate * grad_a / n
            self.b -= self.learning_rate * grad_b / n
        return self

    def predict_one(self, raw_score: float) -> float:
        return clamp_probability(1.0 / (1.0 + math.exp(-(self.a * raw_score + self.b))))

    def predict(self, raw_scores: list[float]) -> list[float]:
        return [self.predict_one(score) for score in raw_scores]


class IsotonicRegressionCalibrator:
    """Pure-Python monotonic probability calibration using PAVA."""

    def __init__(self) -> None:
        self.thresholds: list[float] = []
        self.values: list[float] = []

    def fit(self, probabilities: list[float], y_true: list[int]) -> "IsotonicRegressionCalibrator":
        _validate_lengths(y_true, probabilities)
        pairs = sorted((clamp_probability(p), float(y)) for p, y in zip(probabilities, y_true))
        blocks: list[dict[str, float]] = []
        for probability, target in pairs:
            blocks.append({"weight": 1.0, "sum_y": target, "max_probability": probability})
            while len(blocks) >= 2 and blocks[-2]["sum_y"] / blocks[-2]["weight"] > blocks[-1]["sum_y"] / blocks[-1]["weight"]:
                right = blocks.pop()
                left = blocks.pop()
                blocks.append(
                    {
                        "weight": left["weight"] + right["weight"],
                        "sum_y": left["sum_y"] + right["sum_y"],
                        "max_probability": right["max_probability"],
                    }
                )
        self.thresholds = [block["max_probability"] for block in blocks]
        self.values = [clamp_probability(block["sum_y"] / block["weight"]) for block in blocks]
        return self

    def predict_one(self, probability: float) -> float:
        if not self.thresholds:
            return clamp_probability(probability)
        p = clamp_probability(probability)
        for threshold, value in zip(self.thresholds, self.values):
            if p <= threshold:
                return value
        return self.values[-1]

    def predict(self, probabilities: list[float]) -> list[float]:
        return [self.predict_one(probability) for probability in probabilities]


class BrierScoreOptimizer:
    """Shrink model probabilities toward the validation base rate to minimize Brier score."""

    def __init__(self) -> None:
        self.alpha = 1.0
        self.base_rate = 0.5

    def fit(self, probabilities: list[float], y_true: list[int]) -> "BrierScoreOptimizer":
        _validate_lengths(y_true, probabilities)
        self.base_rate = sum(y_true) / len(y_true)
        best_alpha = 1.0
        best_score = float("inf")
        for step in range(101):
            alpha = step / 100.0
            calibrated = [alpha * clamp_probability(p) + (1 - alpha) * self.base_rate for p in probabilities]
            score = brier_score(y_true, calibrated)
            if score < best_score:
                best_score = score
                best_alpha = alpha
        self.alpha = best_alpha
        return self

    def predict_one(self, probability: float) -> float:
        return clamp_probability(self.alpha * clamp_probability(probability) + (1 - self.alpha) * self.base_rate)

    def predict(self, probabilities: list[float]) -> list[float]:
        return [self.predict_one(probability) for probability in probabilities]


def _validate_lengths(y_true: list[int], probabilities: list[float]) -> None:
    if not y_true or not probabilities:
        raise ValueError("inputs must not be empty")
    if len(y_true) != len(probabilities):
        raise ValueError("inputs must have the same length")
