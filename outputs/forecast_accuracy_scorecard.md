# Forecast Accuracy Scorecard

Generated at: `2026-08-28T12:51:09.556852+00:00`

## Sample Counts

- total_forecasts: `216`
- raw_forecast_rows: `216`
- deduped_legacy_rows: `0`
- pending_forecasts: `216`
- completed_1d: `212`
- completed_3d: `204`
- completed_5d: `196`
- completed_10d: `176`
- completed_20d: `136`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `212`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3066`
- primary_path_mean_absolute_error: `0.009998`
- primary_path_median_absolute_error: `0.007877`
- secondary_scenario_hit_rate: `0.3208`
- primary_vs_secondary_accuracy_spread: `-0.0142`
- primary_closer_than_secondary_rate: `0.4387`
- close_call_primary_closer_rate: `0.376`

### 3d
- completed_count: `204`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2353`
- primary_path_mean_absolute_error: `0.016331`
- primary_path_median_absolute_error: `0.012788`
- secondary_scenario_hit_rate: `0.3529`
- primary_vs_secondary_accuracy_spread: `-0.1176`
- primary_closer_than_secondary_rate: `0.3824`
- close_call_primary_closer_rate: `0.4103`

### 5d
- completed_count: `196`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2194`
- primary_path_mean_absolute_error: `0.023314`
- primary_path_median_absolute_error: `0.018905`
- secondary_scenario_hit_rate: `0.301`
- primary_vs_secondary_accuracy_spread: `-0.0816`
- primary_closer_than_secondary_rate: `0.398`
- close_call_primary_closer_rate: `0.3761`

### 10d
- completed_count: `176`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2045`
- primary_path_mean_absolute_error: `0.034331`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3523`
- primary_vs_secondary_accuracy_spread: `-0.1477`
- primary_closer_than_secondary_rate: `0.3068`
- close_call_primary_closer_rate: `0.2653`

### 20d
- completed_count: `136`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1103`
- primary_path_mean_absolute_error: `0.060004`
- primary_path_median_absolute_error: `0.061807`
- secondary_scenario_hit_rate: `0.2868`
- primary_vs_secondary_accuracy_spread: `-0.1765`
- primary_closer_than_secondary_rate: `0.25`
- close_call_primary_closer_rate: `0.2429`

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
