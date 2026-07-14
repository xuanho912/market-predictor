# Forecast Accuracy Scorecard

Generated at: `2026-07-14T23:40:43.131998+00:00`

## Sample Counts

- total_forecasts: `88`
- raw_forecast_rows: `88`
- deduped_legacy_rows: `0`
- pending_forecasts: `88`
- completed_1d: `84`
- completed_3d: `76`
- completed_5d: `68`
- completed_10d: `48`
- completed_20d: `8`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `84`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3929`
- primary_path_mean_absolute_error: `0.010147`
- primary_path_median_absolute_error: `0.007198`
- secondary_scenario_hit_rate: `0.2619`
- primary_vs_secondary_accuracy_spread: `0.131`
- primary_closer_than_secondary_rate: `0.5357`
- close_call_primary_closer_rate: `0.5349`

### 3d
- completed_count: `76`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2763`
- primary_path_mean_absolute_error: `0.012788`
- primary_path_median_absolute_error: `0.011536`
- secondary_scenario_hit_rate: `0.3421`
- primary_vs_secondary_accuracy_spread: `-0.0658`
- primary_closer_than_secondary_rate: `0.3684`
- close_call_primary_closer_rate: `0.4595`

### 5d
- completed_count: `68`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3529`
- primary_path_mean_absolute_error: `0.01686`
- primary_path_median_absolute_error: `0.009358`
- secondary_scenario_hit_rate: `0.2794`
- primary_vs_secondary_accuracy_spread: `0.0735`
- primary_closer_than_secondary_rate: `0.5`
- close_call_primary_closer_rate: `0.5`

### 10d
- completed_count: `48`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.2292`
- primary_path_mean_absolute_error: `0.023982`
- primary_path_median_absolute_error: `0.020935`
- secondary_scenario_hit_rate: `0.2917`
- primary_vs_secondary_accuracy_spread: `-0.0625`
- primary_closer_than_secondary_rate: `0.3958`
- close_call_primary_closer_rate: `0.3333`

### 20d
- completed_count: `8`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `0.0`
- primary_path_mean_absolute_error: `0.031809`
- primary_path_median_absolute_error: `0.032429`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.5`
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
