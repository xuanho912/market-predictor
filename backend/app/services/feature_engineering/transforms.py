from __future__ import annotations


def level(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    return values[-1]


def change(values: list[float], periods: int) -> float:
    if periods <= 0:
        raise ValueError("periods must be positive")
    if len(values) <= periods:
        raise ValueError("not enough values for requested change")
    return values[-1] - values[-1 - periods]


def acceleration(values: list[float], periods: int) -> float:
    if len(values) <= periods * 2:
        raise ValueError("not enough values for requested acceleration")
    current_change = values[-1] - values[-1 - periods]
    prior_change = values[-1 - periods] - values[-1 - periods * 2]
    return current_change - prior_change


def percentile_rank(history: list[float], value: float) -> float:
    if not history:
        raise ValueError("history must not be empty")
    count = sum(1 for item in history if item <= value)
    return count / len(history)


def cross_signal(primary_direction: float, confirming_direction: float) -> int:
    if primary_direction == 0 or confirming_direction == 0:
        return 0
    return 1 if primary_direction * confirming_direction > 0 else -1


def divergence(primary_direction: float, confirming_direction: float) -> int:
    signal = cross_signal(primary_direction, confirming_direction)
    return 1 if signal == -1 else 0
