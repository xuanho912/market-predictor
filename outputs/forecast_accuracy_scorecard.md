# Forecast Accuracy Scorecard

Generated at: `2026-06-18T00:01:55.205056+00:00`

## Sample Counts

- total_forecasts: `20`
- pending_forecasts: `20`
- completed_1d: `16`
- completed_3d: `8`
- completed_5d: `0`
- completed_10d: `0`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `insufficient_samples`
- validation_warning: 当前预测准确度仍未被前向样本验证，不能称为 high precision / stable alpha / validated forecasting system。

## Primary Scenario Accuracy

### 1d
- completed_count: `16`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `0.0`
- primary_path_mean_absolute_error: `0.010505`
- primary_path_median_absolute_error: `0.009632`
- secondary_scenario_hit_rate: `0.0625`
- primary_vs_secondary_accuracy_spread: `-0.0625`
- primary_closer_than_secondary_rate: `0.25`
- close_call_primary_closer_rate: `None`

### 3d
- completed_count: `8`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `0.0`
- primary_path_mean_absolute_error: `0.009736`
- primary_path_median_absolute_error: `0.007093`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.25`
- close_call_primary_closer_rate: `None`

### 5d
- completed_count: `0`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `None`
- primary_path_mean_absolute_error: `None`
- primary_path_median_absolute_error: `None`
- secondary_scenario_hit_rate: `None`
- primary_vs_secondary_accuracy_spread: `None`
- primary_closer_than_secondary_rate: `None`
- close_call_primary_closer_rate: `None`

### 10d
- completed_count: `0`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `None`
- primary_path_mean_absolute_error: `None`
- primary_path_median_absolute_error: `None`
- secondary_scenario_hit_rate: `None`
- primary_vs_secondary_accuracy_spread: `None`
- primary_closer_than_secondary_rate: `None`
- close_call_primary_closer_rate: `None`

### 20d
- completed_count: `0`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `None`
- primary_path_mean_absolute_error: `None`
- primary_path_median_absolute_error: `None`
- secondary_scenario_hit_rate: `None`
- primary_vs_secondary_accuracy_spread: `None`
- primary_closer_than_secondary_rate: `None`
- close_call_primary_closer_rate: `None`

### 60d
- completed_count: `0`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `None`
- primary_path_mean_absolute_error: `None`
- primary_path_median_absolute_error: `None`
- secondary_scenario_hit_rate: `None`
- primary_vs_secondary_accuracy_spread: `None`
- primary_closer_than_secondary_rate: `None`
- close_call_primary_closer_rate: `None`

## Core Questions

- edge_vs_no_edge: `insufficient_samples_for_edge_validation`
- high_confidence_better: `insufficient_samples_for_high_confidence_validation`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
