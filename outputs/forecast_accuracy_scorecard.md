# Forecast Accuracy Scorecard

Generated at: `2026-07-16T22:35:39.080176+00:00`

## Sample Counts

- total_forecasts: `96`
- raw_forecast_rows: `96`
- deduped_legacy_rows: `0`
- pending_forecasts: `96`
- completed_1d: `92`
- completed_3d: `84`
- completed_5d: `76`
- completed_10d: `56`
- completed_20d: `16`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `92`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3913`
- primary_path_mean_absolute_error: `0.009728`
- primary_path_median_absolute_error: `0.006466`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `0.1413`
- primary_closer_than_secondary_rate: `0.5435`
- close_call_primary_closer_rate: `0.5435`

### 3d
- completed_count: `84`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2619`
- primary_path_mean_absolute_error: `0.013066`
- primary_path_median_absolute_error: `0.011856`
- secondary_scenario_hit_rate: `0.381`
- primary_vs_secondary_accuracy_spread: `-0.119`
- primary_closer_than_secondary_rate: `0.3452`
- close_call_primary_closer_rate: `0.4186`

### 5d
- completed_count: `76`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3421`
- primary_path_mean_absolute_error: `0.016454`
- primary_path_median_absolute_error: `0.009358`
- secondary_scenario_hit_rate: `0.2763`
- primary_vs_secondary_accuracy_spread: `0.0658`
- primary_closer_than_secondary_rate: `0.5`
- close_call_primary_closer_rate: `0.4865`

### 10d
- completed_count: `56`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.02365`
- primary_path_median_absolute_error: `0.020874`
- secondary_scenario_hit_rate: `0.3393`
- primary_vs_secondary_accuracy_spread: `-0.0893`
- primary_closer_than_secondary_rate: `0.3929`
- close_call_primary_closer_rate: `0.3448`

### 20d
- completed_count: `16`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `0.0`
- primary_path_mean_absolute_error: `0.046668`
- primary_path_median_absolute_error: `0.038018`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.375`
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
