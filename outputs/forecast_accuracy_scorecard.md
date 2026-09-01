# Forecast Accuracy Scorecard

Generated at: `2026-09-01T23:34:52.742216+00:00`

## Sample Counts

- total_forecasts: `228`
- raw_forecast_rows: `228`
- deduped_legacy_rows: `0`
- pending_forecasts: `228`
- completed_1d: `224`
- completed_3d: `216`
- completed_5d: `208`
- completed_10d: `188`
- completed_20d: `148`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `224`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2946`
- primary_path_mean_absolute_error: `0.00989`
- primary_path_median_absolute_error: `0.007623`
- secondary_scenario_hit_rate: `0.3259`
- primary_vs_secondary_accuracy_spread: `-0.0312`
- primary_closer_than_secondary_rate: `0.4196`
- close_call_primary_closer_rate: `0.3504`

### 3d
- completed_count: `216`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2361`
- primary_path_mean_absolute_error: `0.016284`
- primary_path_median_absolute_error: `0.012757`
- secondary_scenario_hit_rate: `0.3565`
- primary_vs_secondary_accuracy_spread: `-0.1204`
- primary_closer_than_secondary_rate: `0.3843`
- close_call_primary_closer_rate: `0.4109`

### 5d
- completed_count: `208`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.226`
- primary_path_mean_absolute_error: `0.023103`
- primary_path_median_absolute_error: `0.018502`
- secondary_scenario_hit_rate: `0.2981`
- primary_vs_secondary_accuracy_spread: `-0.0721`
- primary_closer_than_secondary_rate: `0.3942`
- close_call_primary_closer_rate: `0.3719`

### 10d
- completed_count: `188`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2074`
- primary_path_mean_absolute_error: `0.034479`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3351`
- primary_vs_secondary_accuracy_spread: `-0.1277`
- primary_closer_than_secondary_rate: `0.3032`
- close_call_primary_closer_rate: `0.2667`

### 20d
- completed_count: `148`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1216`
- primary_path_mean_absolute_error: `0.059289`
- primary_path_median_absolute_error: `0.058866`
- secondary_scenario_hit_rate: `0.277`
- primary_vs_secondary_accuracy_spread: `-0.1554`
- primary_closer_than_secondary_rate: `0.2703`
- close_call_primary_closer_rate: `0.2875`

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
