# Forecast Accuracy Scorecard

Generated at: `2026-08-05T00:14:48.029056+00:00`

## Sample Counts

- total_forecasts: `148`
- raw_forecast_rows: `148`
- deduped_legacy_rows: `0`
- pending_forecasts: `148`
- completed_1d: `144`
- completed_3d: `136`
- completed_5d: `128`
- completed_10d: `108`
- completed_20d: `68`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `144`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3472`
- primary_path_mean_absolute_error: `0.010786`
- primary_path_median_absolute_error: `0.00826`
- secondary_scenario_hit_rate: `0.2917`
- primary_vs_secondary_accuracy_spread: `0.0556`
- primary_closer_than_secondary_rate: `0.5`
- close_call_primary_closer_rate: `0.4474`

### 3d
- completed_count: `136`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2721`
- primary_path_mean_absolute_error: `0.016045`
- primary_path_median_absolute_error: `0.012788`
- secondary_scenario_hit_rate: `0.3382`
- primary_vs_secondary_accuracy_spread: `-0.0662`
- primary_closer_than_secondary_rate: `0.3971`
- close_call_primary_closer_rate: `0.4571`

### 5d
- completed_count: `128`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2734`
- primary_path_mean_absolute_error: `0.02033`
- primary_path_median_absolute_error: `0.013457`
- secondary_scenario_hit_rate: `0.2969`
- primary_vs_secondary_accuracy_spread: `-0.0234`
- primary_closer_than_secondary_rate: `0.4375`
- close_call_primary_closer_rate: `0.3846`

### 10d
- completed_count: `108`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2407`
- primary_path_mean_absolute_error: `0.02697`
- primary_path_median_absolute_error: `0.022587`
- secondary_scenario_hit_rate: `0.3148`
- primary_vs_secondary_accuracy_spread: `-0.0741`
- primary_closer_than_secondary_rate: `0.3611`
- close_call_primary_closer_rate: `0.2364`

### 20d
- completed_count: `68`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1471`
- primary_path_mean_absolute_error: `0.052599`
- primary_path_median_absolute_error: `0.044895`
- secondary_scenario_hit_rate: `0.3088`
- primary_vs_secondary_accuracy_spread: `-0.1618`
- primary_closer_than_secondary_rate: `0.3088`
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
