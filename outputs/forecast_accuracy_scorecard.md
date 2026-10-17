# Forecast Accuracy Scorecard

Generated at: `2026-10-17T01:05:56.634030+00:00`

## Sample Counts

- total_forecasts: `356`
- raw_forecast_rows: `356`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `352`
- completed_3d: `344`
- completed_5d: `336`
- completed_10d: `316`
- completed_20d: `276`
- completed_60d: `116`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `352`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2614`
- primary_path_mean_absolute_error: `0.010077`
- primary_path_median_absolute_error: `0.00826`
- secondary_scenario_hit_rate: `0.3438`
- primary_vs_secondary_accuracy_spread: `-0.0824`
- primary_closer_than_secondary_rate: `0.3693`
- close_call_primary_closer_rate: `0.3439`

### 3d
- completed_count: `344`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2529`
- primary_path_mean_absolute_error: `0.016398`
- primary_path_median_absolute_error: `0.0129`
- secondary_scenario_hit_rate: `0.3081`
- primary_vs_secondary_accuracy_spread: `-0.0552`
- primary_closer_than_secondary_rate: `0.3837`
- close_call_primary_closer_rate: `0.4202`

### 5d
- completed_count: `336`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2708`
- primary_path_mean_absolute_error: `0.022103`
- primary_path_median_absolute_error: `0.01786`
- secondary_scenario_hit_rate: `0.2917`
- primary_vs_secondary_accuracy_spread: `-0.0208`
- primary_closer_than_secondary_rate: `0.3929`
- close_call_primary_closer_rate: `0.3913`

### 10d
- completed_count: `316`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.231`
- primary_path_mean_absolute_error: `0.032437`
- primary_path_median_absolute_error: `0.027368`
- secondary_scenario_hit_rate: `0.3323`
- primary_vs_secondary_accuracy_spread: `-0.1013`
- primary_closer_than_secondary_rate: `0.3196`
- close_call_primary_closer_rate: `0.3333`

### 20d
- completed_count: `276`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1377`
- primary_path_mean_absolute_error: `0.057854`
- primary_path_median_absolute_error: `0.054073`
- secondary_scenario_hit_rate: `0.2826`
- primary_vs_secondary_accuracy_spread: `-0.1449`
- primary_closer_than_secondary_rate: `0.2935`
- close_call_primary_closer_rate: `0.3419`

### 60d
- completed_count: `116`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1293`
- primary_path_mean_absolute_error: `0.07011`
- primary_path_median_absolute_error: `0.058199`
- secondary_scenario_hit_rate: `0.2241`
- primary_vs_secondary_accuracy_spread: `-0.0948`
- primary_closer_than_secondary_rate: `0.4224`
- close_call_primary_closer_rate: `0.5345`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
