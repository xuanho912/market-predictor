# Forecast Accuracy Scorecard

Generated at: `2026-08-10T23:24:40.651784+00:00`

## Sample Counts

- total_forecasts: `164`
- raw_forecast_rows: `164`
- deduped_legacy_rows: `0`
- pending_forecasts: `164`
- completed_1d: `160`
- completed_3d: `152`
- completed_5d: `144`
- completed_10d: `124`
- completed_20d: `84`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `160`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.35`
- primary_path_mean_absolute_error: `0.010399`
- primary_path_median_absolute_error: `0.008169`
- secondary_scenario_hit_rate: `0.3`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.5`
- close_call_primary_closer_rate: `0.4444`

### 3d
- completed_count: `152`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2632`
- primary_path_mean_absolute_error: `0.016574`
- primary_path_median_absolute_error: `0.013064`
- secondary_scenario_hit_rate: `0.3487`
- primary_vs_secondary_accuracy_spread: `-0.0855`
- primary_closer_than_secondary_rate: `0.4013`
- close_call_primary_closer_rate: `0.4524`

### 5d
- completed_count: `144`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2569`
- primary_path_mean_absolute_error: `0.023846`
- primary_path_median_absolute_error: `0.0176`
- secondary_scenario_hit_rate: `0.2986`
- primary_vs_secondary_accuracy_spread: `-0.0417`
- primary_closer_than_secondary_rate: `0.4167`
- close_call_primary_closer_rate: `0.3684`

### 10d
- completed_count: `124`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2097`
- primary_path_mean_absolute_error: `0.031343`
- primary_path_median_absolute_error: `0.026349`
- secondary_scenario_hit_rate: `0.371`
- primary_vs_secondary_accuracy_spread: `-0.1613`
- primary_closer_than_secondary_rate: `0.3145`
- close_call_primary_closer_rate: `0.2063`

### 20d
- completed_count: `84`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1667`
- primary_path_mean_absolute_error: `0.049423`
- primary_path_median_absolute_error: `0.040664`
- secondary_scenario_hit_rate: `0.2738`
- primary_vs_secondary_accuracy_spread: `-0.1071`
- primary_closer_than_secondary_rate: `0.3571`
- close_call_primary_closer_rate: `0.3256`

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
