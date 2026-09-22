# Forecast Accuracy Scorecard

Generated at: `2026-09-22T17:00:32.526048+00:00`

## Sample Counts

- total_forecasts: `280`
- raw_forecast_rows: `280`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `276`
- completed_3d: `268`
- completed_5d: `260`
- completed_10d: `240`
- completed_20d: `200`
- completed_60d: `40`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `276`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2754`
- primary_path_mean_absolute_error: `0.010018`
- primary_path_median_absolute_error: `0.007799`
- secondary_scenario_hit_rate: `0.3333`
- primary_vs_secondary_accuracy_spread: `-0.058`
- primary_closer_than_secondary_rate: `0.3949`
- close_call_primary_closer_rate: `0.3548`

### 3d
- completed_count: `268`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2612`
- primary_path_mean_absolute_error: `0.016144`
- primary_path_median_absolute_error: `0.012428`
- secondary_scenario_hit_rate: `0.3209`
- primary_vs_secondary_accuracy_spread: `-0.0597`
- primary_closer_than_secondary_rate: `0.3918`
- close_call_primary_closer_rate: `0.4238`

### 5d
- completed_count: `260`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2923`
- primary_path_mean_absolute_error: `0.021267`
- primary_path_median_absolute_error: `0.014961`
- secondary_scenario_hit_rate: `0.2769`
- primary_vs_secondary_accuracy_spread: `0.0154`
- primary_closer_than_secondary_rate: `0.4308`
- close_call_primary_closer_rate: `0.3974`

### 10d
- completed_count: `240`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2375`
- primary_path_mean_absolute_error: `0.033186`
- primary_path_median_absolute_error: `0.027239`
- secondary_scenario_hit_rate: `0.3375`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.3375`
- close_call_primary_closer_rate: `0.3265`

### 20d
- completed_count: `200`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.11`
- primary_path_mean_absolute_error: `0.061674`
- primary_path_median_absolute_error: `0.059096`
- secondary_scenario_hit_rate: `0.295`
- primary_vs_secondary_accuracy_spread: `-0.185`
- primary_closer_than_secondary_rate: `0.25`
- close_call_primary_closer_rate: `0.2743`

### 60d
- completed_count: `40`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.065979`
- primary_path_median_absolute_error: `0.050587`
- secondary_scenario_hit_rate: `0.15`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.425`
- close_call_primary_closer_rate: `0.5294`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
