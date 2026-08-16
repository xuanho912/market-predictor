# Forecast Accuracy Scorecard

Generated at: `2026-08-16T13:04:03.899219+00:00`

## Sample Counts

- total_forecasts: `180`
- raw_forecast_rows: `180`
- deduped_legacy_rows: `0`
- pending_forecasts: `180`
- completed_1d: `176`
- completed_3d: `168`
- completed_5d: `160`
- completed_10d: `140`
- completed_20d: `100`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `176`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.358`
- primary_path_mean_absolute_error: `0.009689`
- primary_path_median_absolute_error: `0.007198`
- secondary_scenario_hit_rate: `0.3011`
- primary_vs_secondary_accuracy_spread: `0.0568`
- primary_closer_than_secondary_rate: `0.5057`
- close_call_primary_closer_rate: `0.449`

### 3d
- completed_count: `168`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2679`
- primary_path_mean_absolute_error: `0.015762`
- primary_path_median_absolute_error: `0.012544`
- secondary_scenario_hit_rate: `0.3333`
- primary_vs_secondary_accuracy_spread: `-0.0655`
- primary_closer_than_secondary_rate: `0.4226`
- close_call_primary_closer_rate: `0.4526`

### 5d
- completed_count: `160`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2437`
- primary_path_mean_absolute_error: `0.022989`
- primary_path_median_absolute_error: `0.016578`
- secondary_scenario_hit_rate: `0.3`
- primary_vs_secondary_accuracy_spread: `-0.0563`
- primary_closer_than_secondary_rate: `0.4375`
- close_call_primary_closer_rate: `0.4`

### 10d
- completed_count: `140`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2071`
- primary_path_mean_absolute_error: `0.035619`
- primary_path_median_absolute_error: `0.029068`
- secondary_scenario_hit_rate: `0.3857`
- primary_vs_secondary_accuracy_spread: `-0.1786`
- primary_closer_than_secondary_rate: `0.3`
- close_call_primary_closer_rate: `0.2083`

### 20d
- completed_count: `100`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.14`
- primary_path_mean_absolute_error: `0.052332`
- primary_path_median_absolute_error: `0.047897`
- secondary_scenario_hit_rate: `0.27`
- primary_vs_secondary_accuracy_spread: `-0.13`
- primary_closer_than_secondary_rate: `0.31`
- close_call_primary_closer_rate: `0.3`

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
