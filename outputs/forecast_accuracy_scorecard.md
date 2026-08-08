# Forecast Accuracy Scorecard

Generated at: `2026-08-08T04:41:44.165640+00:00`

## Sample Counts

- total_forecasts: `160`
- raw_forecast_rows: `160`
- deduped_legacy_rows: `0`
- pending_forecasts: `160`
- completed_1d: `156`
- completed_3d: `148`
- completed_5d: `140`
- completed_10d: `120`
- completed_20d: `80`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `156`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3462`
- primary_path_mean_absolute_error: `0.010502`
- primary_path_median_absolute_error: `0.00826`
- secondary_scenario_hit_rate: `0.2949`
- primary_vs_secondary_accuracy_spread: `0.0513`
- primary_closer_than_secondary_rate: `0.5`
- close_call_primary_closer_rate: `0.4483`

### 3d
- completed_count: `148`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2703`
- primary_path_mean_absolute_error: `0.016761`
- primary_path_median_absolute_error: `0.013144`
- secondary_scenario_hit_rate: `0.3446`
- primary_vs_secondary_accuracy_spread: `-0.0743`
- primary_closer_than_secondary_rate: `0.3986`
- close_call_primary_closer_rate: `0.45`

### 5d
- completed_count: `140`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2643`
- primary_path_mean_absolute_error: `0.023522`
- primary_path_median_absolute_error: `0.016971`
- secondary_scenario_hit_rate: `0.3071`
- primary_vs_secondary_accuracy_spread: `-0.0429`
- primary_closer_than_secondary_rate: `0.4214`
- close_call_primary_closer_rate: `0.375`

### 10d
- completed_count: `120`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2167`
- primary_path_mean_absolute_error: `0.030266`
- primary_path_median_absolute_error: `0.025493`
- secondary_scenario_hit_rate: `0.3667`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.325`
- close_call_primary_closer_rate: `0.2131`

### 20d
- completed_count: `80`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.175`
- primary_path_mean_absolute_error: `0.04902`
- primary_path_median_absolute_error: `0.040664`
- secondary_scenario_hit_rate: `0.275`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.35`
- close_call_primary_closer_rate: `0.3077`

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
