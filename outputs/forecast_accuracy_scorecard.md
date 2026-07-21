# Forecast Accuracy Scorecard

Generated at: `2026-07-21T00:08:12.973481+00:00`

## Sample Counts

- total_forecasts: `104`
- raw_forecast_rows: `104`
- deduped_legacy_rows: `0`
- pending_forecasts: `104`
- completed_1d: `100`
- completed_3d: `92`
- completed_5d: `84`
- completed_10d: `64`
- completed_20d: `24`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `100`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.36`
- primary_path_mean_absolute_error: `0.009679`
- primary_path_median_absolute_error: `0.007071`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `0.11`
- primary_closer_than_secondary_rate: `0.52`
- close_call_primary_closer_rate: `0.5`

### 3d
- completed_count: `92`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2717`
- primary_path_mean_absolute_error: `0.013267`
- primary_path_median_absolute_error: `0.011856`
- secondary_scenario_hit_rate: `0.3587`
- primary_vs_secondary_accuracy_spread: `-0.087`
- primary_closer_than_secondary_rate: `0.3696`
- close_call_primary_closer_rate: `0.4348`

### 5d
- completed_count: `84`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3095`
- primary_path_mean_absolute_error: `0.017108`
- primary_path_median_absolute_error: `0.009831`
- secondary_scenario_hit_rate: `0.2738`
- primary_vs_secondary_accuracy_spread: `0.0357`
- primary_closer_than_secondary_rate: `0.4881`
- close_call_primary_closer_rate: `0.4651`

### 10d
- completed_count: `64`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.025159`
- primary_path_median_absolute_error: `0.021062`
- secondary_scenario_hit_rate: `0.3438`
- primary_vs_secondary_accuracy_spread: `-0.0938`
- primary_closer_than_secondary_rate: `0.3906`
- close_call_primary_closer_rate: `0.3125`

### 20d
- completed_count: `24`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.1667`
- primary_path_mean_absolute_error: `0.040023`
- primary_path_median_absolute_error: `0.036739`
- secondary_scenario_hit_rate: `0.2083`
- primary_vs_secondary_accuracy_spread: `-0.0417`
- primary_closer_than_secondary_rate: `0.5417`
- close_call_primary_closer_rate: `1.0`

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

- edge_vs_no_edge: `insufficient_samples_for_edge_validation`
- high_confidence_better: `insufficient_samples_for_high_confidence_validation`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
