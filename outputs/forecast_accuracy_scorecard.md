# Forecast Accuracy Scorecard

Generated at: `2026-07-07T07:05:42.221155+00:00`

## Sample Counts

- total_forecasts: `64`
- raw_forecast_rows: `64`
- deduped_legacy_rows: `0`
- pending_forecasts: `64`
- completed_1d: `60`
- completed_3d: `52`
- completed_5d: `44`
- completed_10d: `24`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `60`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3833`
- primary_path_mean_absolute_error: `0.010891`
- primary_path_median_absolute_error: `0.008016`
- secondary_scenario_hit_rate: `0.2667`
- primary_vs_secondary_accuracy_spread: `0.1167`
- primary_closer_than_secondary_rate: `0.5333`
- close_call_primary_closer_rate: `0.5806`

### 3d
- completed_count: `52`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2692`
- primary_path_mean_absolute_error: `0.01321`
- primary_path_median_absolute_error: `0.011537`
- secondary_scenario_hit_rate: `0.3462`
- primary_vs_secondary_accuracy_spread: `-0.0769`
- primary_closer_than_secondary_rate: `0.3846`
- close_call_primary_closer_rate: `0.5385`

### 5d
- completed_count: `44`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.3182`
- primary_path_mean_absolute_error: `0.018784`
- primary_path_median_absolute_error: `0.010695`
- secondary_scenario_hit_rate: `0.2727`
- primary_vs_secondary_accuracy_spread: `0.0455`
- primary_closer_than_secondary_rate: `0.4773`
- close_call_primary_closer_rate: `0.4762`

### 10d
- completed_count: `24`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.2083`
- primary_path_mean_absolute_error: `0.01634`
- primary_path_median_absolute_error: `0.014348`
- secondary_scenario_hit_rate: `0.125`
- primary_vs_secondary_accuracy_spread: `0.0833`
- primary_closer_than_secondary_rate: `0.5417`
- close_call_primary_closer_rate: `0.8`

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
