# Forecast Accuracy Scorecard

Generated at: `2026-10-13T19:21:46.558940+00:00`

## Sample Counts

- total_forecasts: `340`
- raw_forecast_rows: `340`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `336`
- completed_3d: `328`
- completed_5d: `320`
- completed_10d: `300`
- completed_20d: `260`
- completed_60d: `100`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `336`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2649`
- primary_path_mean_absolute_error: `0.009945`
- primary_path_median_absolute_error: `0.007936`
- secondary_scenario_hit_rate: `0.3393`
- primary_vs_secondary_accuracy_spread: `-0.0744`
- primary_closer_than_secondary_rate: `0.372`
- close_call_primary_closer_rate: `0.3478`

### 3d
- completed_count: `328`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.253`
- primary_path_mean_absolute_error: `0.016361`
- primary_path_median_absolute_error: `0.012788`
- secondary_scenario_hit_rate: `0.3079`
- primary_vs_secondary_accuracy_spread: `-0.0549`
- primary_closer_than_secondary_rate: `0.3811`
- close_call_primary_closer_rate: `0.4134`

### 5d
- completed_count: `320`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2625`
- primary_path_mean_absolute_error: `0.022122`
- primary_path_median_absolute_error: `0.0176`
- secondary_scenario_hit_rate: `0.2812`
- primary_vs_secondary_accuracy_spread: `-0.0187`
- primary_closer_than_secondary_rate: `0.3875`
- close_call_primary_closer_rate: `0.3873`

### 10d
- completed_count: `300`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2233`
- primary_path_mean_absolute_error: `0.032525`
- primary_path_median_absolute_error: `0.027368`
- secondary_scenario_hit_rate: `0.3367`
- primary_vs_secondary_accuracy_spread: `-0.1133`
- primary_closer_than_secondary_rate: `0.3167`
- close_call_primary_closer_rate: `0.3314`

### 20d
- completed_count: `260`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1346`
- primary_path_mean_absolute_error: `0.05868`
- primary_path_median_absolute_error: `0.054444`
- secondary_scenario_hit_rate: `0.2808`
- primary_vs_secondary_accuracy_spread: `-0.1462`
- primary_closer_than_secondary_rate: `0.2808`
- close_call_primary_closer_rate: `0.3245`

### 60d
- completed_count: `100`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.14`
- primary_path_mean_absolute_error: `0.069093`
- primary_path_median_absolute_error: `0.051195`
- secondary_scenario_hit_rate: `0.24`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.42`
- close_call_primary_closer_rate: `0.5`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
