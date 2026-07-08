# Forecast Accuracy Scorecard

Generated at: `2026-07-08T04:36:28.007283+00:00`

## Sample Counts

- total_forecasts: `68`
- raw_forecast_rows: `68`
- deduped_legacy_rows: `0`
- pending_forecasts: `68`
- completed_1d: `64`
- completed_3d: `56`
- completed_5d: `48`
- completed_10d: `28`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `64`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3906`
- primary_path_mean_absolute_error: `0.010812`
- primary_path_median_absolute_error: `0.008016`
- secondary_scenario_hit_rate: `0.2812`
- primary_vs_secondary_accuracy_spread: `0.1094`
- primary_closer_than_secondary_rate: `0.5312`
- close_call_primary_closer_rate: `0.5625`

### 3d
- completed_count: `56`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2857`
- primary_path_mean_absolute_error: `0.013334`
- primary_path_median_absolute_error: `0.011537`
- secondary_scenario_hit_rate: `0.3214`
- primary_vs_secondary_accuracy_spread: `-0.0357`
- primary_closer_than_secondary_rate: `0.3929`
- close_call_primary_closer_rate: `0.5517`

### 5d
- completed_count: `48`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.3125`
- primary_path_mean_absolute_error: `0.018901`
- primary_path_median_absolute_error: `0.010695`
- secondary_scenario_hit_rate: `0.2708`
- primary_vs_secondary_accuracy_spread: `0.0417`
- primary_closer_than_secondary_rate: `0.4583`
- close_call_primary_closer_rate: `0.4583`

### 10d
- completed_count: `28`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.01803`
- primary_path_median_absolute_error: `0.016201`
- secondary_scenario_hit_rate: `0.1429`
- primary_vs_secondary_accuracy_spread: `0.1071`
- primary_closer_than_secondary_rate: `0.5357`
- close_call_primary_closer_rate: `0.6667`

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
