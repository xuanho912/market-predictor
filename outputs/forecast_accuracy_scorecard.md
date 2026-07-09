# Forecast Accuracy Scorecard

Generated at: `2026-07-09T07:06:17.431095+00:00`

## Sample Counts

- total_forecasts: `72`
- raw_forecast_rows: `72`
- deduped_legacy_rows: `0`
- pending_forecasts: `72`
- completed_1d: `68`
- completed_3d: `60`
- completed_5d: `52`
- completed_10d: `32`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `68`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3971`
- primary_path_mean_absolute_error: `0.010389`
- primary_path_median_absolute_error: `0.007493`
- secondary_scenario_hit_rate: `0.2794`
- primary_vs_secondary_accuracy_spread: `0.1176`
- primary_closer_than_secondary_rate: `0.5441`
- close_call_primary_closer_rate: `0.5625`

### 3d
- completed_count: `60`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2833`
- primary_path_mean_absolute_error: `0.013171`
- primary_path_median_absolute_error: `0.011536`
- secondary_scenario_hit_rate: `0.35`
- primary_vs_secondary_accuracy_spread: `-0.0667`
- primary_closer_than_secondary_rate: `0.3833`
- close_call_primary_closer_rate: `0.5161`

### 5d
- completed_count: `52`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3269`
- primary_path_mean_absolute_error: `0.018868`
- primary_path_median_absolute_error: `0.010695`
- secondary_scenario_hit_rate: `0.2885`
- primary_vs_secondary_accuracy_spread: `0.0385`
- primary_closer_than_secondary_rate: `0.4615`
- close_call_primary_closer_rate: `0.4231`

### 10d
- completed_count: `32`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.2188`
- primary_path_mean_absolute_error: `0.020383`
- primary_path_median_absolute_error: `0.017931`
- secondary_scenario_hit_rate: `0.1562`
- primary_vs_secondary_accuracy_spread: `0.0625`
- primary_closer_than_secondary_rate: `0.4688`
- close_call_primary_closer_rate: `0.4`

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
