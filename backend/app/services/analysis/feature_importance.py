from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass
from random import Random
from typing import Callable


FeatureRow = dict[str, float | str]
PredictFn = Callable[[list[FeatureRow]], list[float]]
ScoreFn = Callable[[list[int], list[float]], float]


@dataclass(frozen=True)
class FeatureImportanceReport:
    top_20_predictive_features: list[dict[str, float | str]]
    useless_features: list[str]
    unstable_features: list[str]
    regime_specific_features: dict[str, list[str]]
    ablation_by_group: dict[str, float]
    correlation_leakage_flags: list[dict[str, float | str]]
    shap_status: str


def permutation_importance(
    rows: list[FeatureRow],
    y_true: list[int],
    predict_fn: PredictFn,
    score_fn: ScoreFn,
    feature_names: list[str],
    repeats: int = 5,
    seed: int = 17,
) -> list[dict[str, float | str]]:
    if len(rows) != len(y_true):
        raise ValueError("rows and y_true must have the same length")
    baseline = score_fn(y_true, predict_fn(rows))
    random = Random(seed)
    results: list[dict[str, float | str]] = []
    for feature in feature_names:
        drops: list[float] = []
        for _ in range(repeats):
            shuffled_values = [row.get(feature, 0.0) for row in rows]
            random.shuffle(shuffled_values)
            shuffled_rows = [dict(row) for row in rows]
            for row, value in zip(shuffled_rows, shuffled_values):
                row[feature] = value
            drops.append(baseline - score_fn(y_true, predict_fn(shuffled_rows)))
        results.append({"feature": feature, "importance": round(sum(drops) / len(drops), 6)})
    return sorted(results, key=lambda item: float(item["importance"]), reverse=True)


def shap_importance_if_available(model: object, rows: list[FeatureRow]) -> dict[str, object]:
    try:
        import shap  # type: ignore[import-not-found]
    except Exception:
        return {"status": "unavailable", "reason": "shap package is not installed"}
    try:
        explainer = shap.Explainer(model)
        values = explainer(rows)
        return {"status": "ok", "values": str(values)}
    except Exception as error:  # pragma: no cover - depends on optional model/shap runtime
        return {"status": "failed", "reason": str(error)}


def ablation_test_by_group(
    rows: list[FeatureRow],
    y_true: list[int],
    predict_fn: PredictFn,
    score_fn: ScoreFn,
    feature_groups: dict[str, list[str]],
) -> dict[str, float]:
    baseline = score_fn(y_true, predict_fn(rows))
    results: dict[str, float] = {}
    for group, features in feature_groups.items():
        ablated_rows = [dict(row) for row in rows]
        for row in ablated_rows:
            for feature in features:
                if feature in row:
                    row[feature] = 0.0
        results[group] = round(baseline - score_fn(y_true, predict_fn(ablated_rows)), 6)
    return results


def correlation_leakage_check(rows: list[FeatureRow], future_targets: dict[str, list[float]], threshold: float = 0.98) -> list[dict[str, float | str]]:
    numeric_features = _numeric_feature_names(rows)
    flags: list[dict[str, float | str]] = []
    for feature in numeric_features:
        feature_values = [float(row.get(feature, 0.0)) for row in rows]
        for target_name, target_values in future_targets.items():
            if len(feature_values) != len(target_values):
                continue
            correlation = _correlation(feature_values, target_values)
            if abs(correlation) >= threshold:
                flags.append({"feature": feature, "target": target_name, "correlation": round(correlation, 6)})
    return sorted(flags, key=lambda item: abs(float(item["correlation"])), reverse=True)


def build_feature_importance_report(
    rows: list[FeatureRow],
    y_true: list[int],
    predict_fn: PredictFn | None = None,
    score_fn: ScoreFn | None = None,
    feature_groups: dict[str, list[str]] | None = None,
    future_targets: dict[str, list[float]] | None = None,
) -> FeatureImportanceReport:
    feature_names = _numeric_feature_names(rows)
    if predict_fn is None:
        predict_fn = _default_predict_fn(feature_names)
    if score_fn is None:
        score_fn = _default_score_fn
    if feature_groups is None:
        feature_groups = _infer_feature_groups(feature_names)
    if future_targets is None:
        future_targets = {}
    permutation = permutation_importance(rows, y_true, predict_fn, score_fn, feature_names)
    useless = [str(item["feature"]) for item in permutation if float(item["importance"]) <= 0.001]
    unstable = _unstable_features(rows, feature_names)
    return FeatureImportanceReport(
        top_20_predictive_features=permutation[:20],
        useless_features=useless,
        unstable_features=unstable,
        regime_specific_features=_regime_specific_features(rows, y_true, feature_names),
        ablation_by_group=ablation_test_by_group(rows, y_true, predict_fn, score_fn, feature_groups),
        correlation_leakage_flags=correlation_leakage_check(rows, future_targets),
        shap_status=shap_importance_if_available(model=None, rows=rows)["status"],
    )


def _numeric_feature_names(rows: list[FeatureRow]) -> list[str]:
    if not rows:
        return []
    names = set()
    for row in rows:
        for key, value in row.items():
            if key == "regime":
                continue
            if isinstance(value, (int, float)):
                names.add(key)
    return sorted(names)


def _infer_feature_groups(feature_names: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for feature in feature_names:
        groups[feature.split("__", 1)[0]].append(feature)
    return dict(groups)


def _default_predict_fn(feature_names: list[str]) -> PredictFn:
    def predict(rows: list[FeatureRow]) -> list[float]:
        probabilities: list[float] = []
        for row in rows:
            if not feature_names:
                probabilities.append(0.5)
                continue
            raw = sum(float(row.get(feature, 0.0)) for feature in feature_names) / len(feature_names)
            probabilities.append(min(max(raw, 0.0), 1.0))
        return probabilities

    return predict


def _default_score_fn(y_true: list[int], probabilities: list[float]) -> float:
    if not y_true:
        return 0.0
    correct = 0
    for y, probability in zip(y_true, probabilities):
        correct += int((probability >= 0.5) == bool(y))
    return correct / len(y_true)


def _unstable_features(rows: list[FeatureRow], feature_names: list[str]) -> list[str]:
    unstable: list[str] = []
    midpoint = len(rows) // 2
    if midpoint == 0:
        return unstable
    first = rows[:midpoint]
    second = rows[midpoint:]
    for feature in feature_names:
        first_mean = _mean([float(row.get(feature, 0.0)) for row in first])
        second_mean = _mean([float(row.get(feature, 0.0)) for row in second])
        if abs(first_mean - second_mean) > 0.35:
            unstable.append(feature)
    return unstable


def _regime_specific_features(rows: list[FeatureRow], y_true: list[int], feature_names: list[str]) -> dict[str, list[str]]:
    by_regime: dict[str, list[int]] = defaultdict(list)
    for index, row in enumerate(rows):
        by_regime[str(row.get("regime", "unknown"))].append(index)
    result: dict[str, list[str]] = {}
    for regime, indices in by_regime.items():
        if len(indices) < 5:
            continue
        regime_targets = [y_true[index] for index in indices]
        ranked = []
        for feature in feature_names:
            values = [float(rows[index].get(feature, 0.0)) for index in indices]
            ranked.append((feature, abs(_correlation(values, regime_targets))))
        result[regime] = [feature for feature, _ in sorted(ranked, key=lambda item: item[1], reverse=True)[:5]]
    return result


def _correlation(values: list[float], targets: list[float | int]) -> float:
    if len(values) < 2:
        return 0.0
    value_mean = _mean(values)
    target_values = [float(target) for target in targets]
    target_mean = _mean(target_values)
    numerator = sum((value - value_mean) * (target - target_mean) for value, target in zip(values, target_values))
    value_var = sum((value - value_mean) ** 2 for value in values)
    target_var = sum((target - target_mean) ** 2 for target in target_values)
    denominator = math.sqrt(value_var * target_var)
    return numerator / denominator if denominator else 0.0


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0
