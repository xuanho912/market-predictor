# Forecast Accuracy Scorecard

Generated at: `2026-08-21T13:13:40.282157+00:00`

## Sample Counts

- total_forecasts: `196`
- raw_forecast_rows: `196`
- deduped_legacy_rows: `0`
- pending_forecasts: `196`
- completed_1d: `192`
- completed_3d: `184`
- completed_5d: `176`
- completed_10d: `156`
- completed_20d: `116`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `192`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3281`
- primary_path_mean_absolute_error: `0.009903`
- primary_path_median_absolute_error: `0.007799`
- secondary_scenario_hit_rate: `0.3125`
- primary_vs_secondary_accuracy_spread: `0.0156`
- primary_closer_than_secondary_rate: `0.4688`
- close_call_primary_closer_rate: `0.4074`

### 3d
- completed_count: `184`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2446`
- primary_path_mean_absolute_error: `0.016193`
- primary_path_median_absolute_error: `0.012757`
- secondary_scenario_hit_rate: `0.3478`
- primary_vs_secondary_accuracy_spread: `-0.1033`
- primary_closer_than_secondary_rate: `0.3913`
- close_call_primary_closer_rate: `0.4216`

### 5d
- completed_count: `176`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.233`
- primary_path_mean_absolute_error: `0.022992`
- primary_path_median_absolute_error: `0.018502`
- secondary_scenario_hit_rate: `0.3239`
- primary_vs_secondary_accuracy_spread: `-0.0909`
- primary_closer_than_secondary_rate: `0.4148`
- close_call_primary_closer_rate: `0.3776`

### 10d
- completed_count: `156`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2179`
- primary_path_mean_absolute_error: `0.0348`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3718`
- primary_vs_secondary_accuracy_spread: `-0.1538`
- primary_closer_than_secondary_rate: `0.3205`
- close_call_primary_closer_rate: `0.2644`

### 20d
- completed_count: `116`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1293`
- primary_path_mean_absolute_error: `0.055637`
- primary_path_median_absolute_error: `0.052414`
- secondary_scenario_hit_rate: `0.2759`
- primary_vs_secondary_accuracy_spread: `-0.1466`
- primary_closer_than_secondary_rate: `0.2845`
- close_call_primary_closer_rate: `0.2759`

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
