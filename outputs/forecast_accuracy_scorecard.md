# Forecast Accuracy Scorecard

Generated at: `2026-06-23T23:39:21.393837+00:00`

## Sample Counts

- total_forecasts: `32`
- raw_forecast_rows: `32`
- deduped_legacy_rows: `0`
- pending_forecasts: `32`
- completed_1d: `28`
- completed_3d: `20`
- completed_5d: `12`
- completed_10d: `0`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `early_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `28`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.4286`
- primary_path_mean_absolute_error: `0.013858`
- primary_path_median_absolute_error: `0.010793`
- secondary_scenario_hit_rate: `0.2143`
- primary_vs_secondary_accuracy_spread: `0.2143`
- primary_closer_than_secondary_rate: `0.4643`
- close_call_primary_closer_rate: `0.6667`

### 3d
- completed_count: `20`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.2`
- primary_path_mean_absolute_error: `0.011281`
- primary_path_median_absolute_error: `0.010146`
- secondary_scenario_hit_rate: `0.3`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.3`
- close_call_primary_closer_rate: `1.0`

### 5d
- completed_count: `12`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `0.5`
- primary_path_mean_absolute_error: `0.016713`
- primary_path_median_absolute_error: `0.008924`
- secondary_scenario_hit_rate: `0.1667`
- primary_vs_secondary_accuracy_spread: `0.3333`
- primary_closer_than_secondary_rate: `0.5`
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
