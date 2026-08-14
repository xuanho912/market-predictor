# Forecast Accuracy Scorecard

Generated at: `2026-08-14T03:32:19.943478+00:00`

## Sample Counts

- total_forecasts: `176`
- raw_forecast_rows: `176`
- deduped_legacy_rows: `0`
- pending_forecasts: `176`
- completed_1d: `172`
- completed_3d: `164`
- completed_5d: `156`
- completed_10d: `136`
- completed_20d: `96`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `172`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3663`
- primary_path_mean_absolute_error: `0.009853`
- primary_path_median_absolute_error: `0.00762`
- secondary_scenario_hit_rate: `0.2907`
- primary_vs_secondary_accuracy_spread: `0.0756`
- primary_closer_than_secondary_rate: `0.5174`
- close_call_primary_closer_rate: `0.4536`

### 3d
- completed_count: `164`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2683`
- primary_path_mean_absolute_error: `0.015998`
- primary_path_median_absolute_error: `0.012763`
- secondary_scenario_hit_rate: `0.3415`
- primary_vs_secondary_accuracy_spread: `-0.0732`
- primary_closer_than_secondary_rate: `0.4146`
- close_call_primary_closer_rate: `0.4516`

### 5d
- completed_count: `156`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.023202`
- primary_path_median_absolute_error: `0.017107`
- secondary_scenario_hit_rate: `0.2949`
- primary_vs_secondary_accuracy_spread: `-0.0449`
- primary_closer_than_secondary_rate: `0.4359`
- close_call_primary_closer_rate: `0.4023`

### 10d
- completed_count: `136`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1985`
- primary_path_mean_absolute_error: `0.034865`
- primary_path_median_absolute_error: `0.028296`
- secondary_scenario_hit_rate: `0.3824`
- primary_vs_secondary_accuracy_spread: `-0.1838`
- primary_closer_than_secondary_rate: `0.2941`
- close_call_primary_closer_rate: `0.2`

### 20d
- completed_count: `96`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1458`
- primary_path_mean_absolute_error: `0.051307`
- primary_path_median_absolute_error: `0.04522`
- secondary_scenario_hit_rate: `0.2604`
- primary_vs_secondary_accuracy_spread: `-0.1146`
- primary_closer_than_secondary_rate: `0.3229`
- close_call_primary_closer_rate: `0.3125`

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
