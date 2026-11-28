# Forecast Accuracy Scorecard

Generated at: `2026-11-28T20:07:01.308140+00:00`

## Sample Counts

- total_forecasts: `472`
- raw_forecast_rows: `472`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `468`
- completed_3d: `460`
- completed_5d: `452`
- completed_10d: `432`
- completed_20d: `392`
- completed_60d: `232`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `468`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2735`
- primary_path_mean_absolute_error: `0.011588`
- primary_path_median_absolute_error: `0.009204`
- secondary_scenario_hit_rate: `0.3269`
- primary_vs_secondary_accuracy_spread: `-0.0534`
- primary_closer_than_secondary_rate: `0.3739`
- close_call_primary_closer_rate: `0.3478`

### 3d
- completed_count: `460`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2783`
- primary_path_mean_absolute_error: `0.018824`
- primary_path_median_absolute_error: `0.014261`
- secondary_scenario_hit_rate: `0.3087`
- primary_vs_secondary_accuracy_spread: `-0.0304`
- primary_closer_than_secondary_rate: `0.3913`
- close_call_primary_closer_rate: `0.4323`

### 5d
- completed_count: `452`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2721`
- primary_path_mean_absolute_error: `0.025176`
- primary_path_median_absolute_error: `0.020033`
- secondary_scenario_hit_rate: `0.3009`
- primary_vs_secondary_accuracy_spread: `-0.0288`
- primary_closer_than_secondary_rate: `0.3761`
- close_call_primary_closer_rate: `0.3799`

### 10d
- completed_count: `432`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.287`
- primary_path_mean_absolute_error: `0.034059`
- primary_path_median_absolute_error: `0.028495`
- secondary_scenario_hit_rate: `0.3056`
- primary_vs_secondary_accuracy_spread: `-0.0185`
- primary_closer_than_secondary_rate: `0.3727`
- close_call_primary_closer_rate: `0.3393`

### 20d
- completed_count: `392`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2245`
- primary_path_mean_absolute_error: `0.057332`
- primary_path_median_absolute_error: `0.054137`
- secondary_scenario_hit_rate: `0.2653`
- primary_vs_secondary_accuracy_spread: `-0.0408`
- primary_closer_than_secondary_rate: `0.375`
- close_call_primary_closer_rate: `0.3951`

### 60d
- completed_count: `232`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.194`
- primary_path_mean_absolute_error: `0.082296`
- primary_path_median_absolute_error: `0.073168`
- secondary_scenario_hit_rate: `0.2328`
- primary_vs_secondary_accuracy_spread: `-0.0388`
- primary_closer_than_secondary_rate: `0.4009`
- close_call_primary_closer_rate: `0.4615`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_not_better_than_no_edge_keep_confidence_capped`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
