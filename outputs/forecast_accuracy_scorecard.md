# Forecast Accuracy Scorecard

Generated at: `2026-07-01T05:56:38.507021+00:00`

## Sample Counts

- total_forecasts: `52`
- raw_forecast_rows: `52`
- deduped_legacy_rows: `0`
- pending_forecasts: `52`
- completed_1d: `48`
- completed_3d: `40`
- completed_5d: `32`
- completed_10d: `12`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `early_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `48`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.3542`
- primary_path_mean_absolute_error: `0.011732`
- primary_path_median_absolute_error: `0.00992`
- secondary_scenario_hit_rate: `0.2708`
- primary_vs_secondary_accuracy_spread: `0.0833`
- primary_closer_than_secondary_rate: `0.4792`
- close_call_primary_closer_rate: `0.5417`

### 3d
- completed_count: `40`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.012705`
- primary_path_median_absolute_error: `0.011191`
- secondary_scenario_hit_rate: `0.35`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.35`
- close_call_primary_closer_rate: `0.5882`

### 5d
- completed_count: `32`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.3438`
- primary_path_mean_absolute_error: `0.018056`
- primary_path_median_absolute_error: `0.009358`
- secondary_scenario_hit_rate: `0.1875`
- primary_vs_secondary_accuracy_spread: `0.1562`
- primary_closer_than_secondary_rate: `0.5312`
- close_call_primary_closer_rate: `0.6`

### 10d
- completed_count: `12`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `0.1667`
- primary_path_mean_absolute_error: `0.014845`
- primary_path_median_absolute_error: `0.011135`
- secondary_scenario_hit_rate: `0.1667`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.5833`
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
