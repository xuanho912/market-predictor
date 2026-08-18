# Forecast Accuracy Scorecard

Generated at: `2026-08-18T04:22:53.431531+00:00`

## Sample Counts

- total_forecasts: `184`
- raw_forecast_rows: `184`
- deduped_legacy_rows: `0`
- pending_forecasts: `184`
- completed_1d: `180`
- completed_3d: `172`
- completed_5d: `164`
- completed_10d: `144`
- completed_20d: `104`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `180`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.35`
- primary_path_mean_absolute_error: `0.009646`
- primary_path_median_absolute_error: `0.007404`
- secondary_scenario_hit_rate: `0.3`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4944`
- close_call_primary_closer_rate: `0.44`

### 3d
- completed_count: `172`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2616`
- primary_path_mean_absolute_error: `0.015678`
- primary_path_median_absolute_error: `0.01226`
- secondary_scenario_hit_rate: `0.3372`
- primary_vs_secondary_accuracy_spread: `-0.0756`
- primary_closer_than_secondary_rate: `0.4128`
- close_call_primary_closer_rate: `0.4433`

### 5d
- completed_count: `164`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2378`
- primary_path_mean_absolute_error: `0.022824`
- primary_path_median_absolute_error: `0.016578`
- secondary_scenario_hit_rate: `0.311`
- primary_vs_secondary_accuracy_spread: `-0.0732`
- primary_closer_than_secondary_rate: `0.4329`
- close_call_primary_closer_rate: `0.3978`

### 10d
- completed_count: `144`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2153`
- primary_path_mean_absolute_error: `0.035819`
- primary_path_median_absolute_error: `0.029068`
- secondary_scenario_hit_rate: `0.3819`
- primary_vs_secondary_accuracy_spread: `-0.1667`
- primary_closer_than_secondary_rate: `0.3056`
- close_call_primary_closer_rate: `0.2237`

### 20d
- completed_count: `104`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1346`
- primary_path_mean_absolute_error: `0.053312`
- primary_path_median_absolute_error: `0.049736`
- secondary_scenario_hit_rate: `0.2692`
- primary_vs_secondary_accuracy_spread: `-0.1346`
- primary_closer_than_secondary_rate: `0.3077`
- close_call_primary_closer_rate: `0.2963`

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

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `insufficient_samples_for_high_confidence_validation`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
