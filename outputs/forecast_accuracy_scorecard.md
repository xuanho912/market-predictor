# Forecast Accuracy Scorecard

Generated at: `2026-08-13T05:25:02.493041+00:00`

## Sample Counts

- total_forecasts: `172`
- raw_forecast_rows: `172`
- deduped_legacy_rows: `0`
- pending_forecasts: `172`
- completed_1d: `168`
- completed_3d: `160`
- completed_5d: `152`
- completed_10d: `132`
- completed_20d: `92`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `168`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3571`
- primary_path_mean_absolute_error: `0.010022`
- primary_path_median_absolute_error: `0.007799`
- secondary_scenario_hit_rate: `0.2917`
- primary_vs_secondary_accuracy_spread: `0.0655`
- primary_closer_than_secondary_rate: `0.5119`
- close_call_primary_closer_rate: `0.4526`

### 3d
- completed_count: `160`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2625`
- primary_path_mean_absolute_error: `0.016204`
- primary_path_median_absolute_error: `0.012788`
- secondary_scenario_hit_rate: `0.35`
- primary_vs_secondary_accuracy_spread: `-0.0875`
- primary_closer_than_secondary_rate: `0.4062`
- close_call_primary_closer_rate: `0.4444`

### 5d
- completed_count: `152`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.023345`
- primary_path_median_absolute_error: `0.017107`
- secondary_scenario_hit_rate: `0.2961`
- primary_vs_secondary_accuracy_spread: `-0.0461`
- primary_closer_than_secondary_rate: `0.4342`
- close_call_primary_closer_rate: `0.4048`

### 10d
- completed_count: `132`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.197`
- primary_path_mean_absolute_error: `0.03391`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3788`
- primary_vs_secondary_accuracy_spread: `-0.1818`
- primary_closer_than_secondary_rate: `0.2955`
- close_call_primary_closer_rate: `0.197`

### 20d
- completed_count: `92`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1522`
- primary_path_mean_absolute_error: `0.050536`
- primary_path_median_absolute_error: `0.043345`
- secondary_scenario_hit_rate: `0.2717`
- primary_vs_secondary_accuracy_spread: `-0.1196`
- primary_closer_than_secondary_rate: `0.337`
- close_call_primary_closer_rate: `0.3261`

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
