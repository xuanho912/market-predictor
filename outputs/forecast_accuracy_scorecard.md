# Forecast Accuracy Scorecard

Generated at: `2026-08-03T22:38:42.285007+00:00`

## Sample Counts

- total_forecasts: `144`
- raw_forecast_rows: `144`
- deduped_legacy_rows: `0`
- pending_forecasts: `144`
- completed_1d: `140`
- completed_3d: `132`
- completed_5d: `124`
- completed_10d: `104`
- completed_20d: `64`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `140`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3571`
- primary_path_mean_absolute_error: `0.010382`
- primary_path_median_absolute_error: `0.00802`
- secondary_scenario_hit_rate: `0.2857`
- primary_vs_secondary_accuracy_spread: `0.0714`
- primary_closer_than_secondary_rate: `0.5071`
- close_call_primary_closer_rate: `0.4583`

### 3d
- completed_count: `132`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2727`
- primary_path_mean_absolute_error: `0.01522`
- primary_path_median_absolute_error: `0.012544`
- secondary_scenario_hit_rate: `0.3409`
- primary_vs_secondary_accuracy_spread: `-0.0682`
- primary_closer_than_secondary_rate: `0.3939`
- close_call_primary_closer_rate: `0.4545`

### 5d
- completed_count: `124`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2823`
- primary_path_mean_absolute_error: `0.018788`
- primary_path_median_absolute_error: `0.012381`
- secondary_scenario_hit_rate: `0.2903`
- primary_vs_secondary_accuracy_spread: `-0.0081`
- primary_closer_than_secondary_rate: `0.4516`
- close_call_primary_closer_rate: `0.3968`

### 10d
- completed_count: `104`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.026116`
- primary_path_median_absolute_error: `0.021931`
- secondary_scenario_hit_rate: `0.2981`
- primary_vs_secondary_accuracy_spread: `-0.0481`
- primary_closer_than_secondary_rate: `0.375`
- close_call_primary_closer_rate: `0.2407`

### 20d
- completed_count: `64`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.054581`
- primary_path_median_absolute_error: `0.052941`
- secondary_scenario_hit_rate: `0.3281`
- primary_vs_secondary_accuracy_spread: `-0.2031`
- primary_closer_than_secondary_rate: `0.2969`
- close_call_primary_closer_rate: `0.2812`

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
