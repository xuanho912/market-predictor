# Forecast Accuracy Scorecard

Generated at: `2026-07-12T13:59:12.068063+00:00`

## Sample Counts

- total_forecasts: `80`
- raw_forecast_rows: `80`
- deduped_legacy_rows: `0`
- pending_forecasts: `80`
- completed_1d: `76`
- completed_3d: `68`
- completed_5d: `60`
- completed_10d: `40`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `76`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.4079`
- primary_path_mean_absolute_error: `0.009987`
- primary_path_median_absolute_error: `0.00682`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `0.1579`
- primary_closer_than_secondary_rate: `0.5526`
- close_call_primary_closer_rate: `0.5946`

### 3d
- completed_count: `68`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2794`
- primary_path_mean_absolute_error: `0.013007`
- primary_path_median_absolute_error: `0.011847`
- secondary_scenario_hit_rate: `0.3676`
- primary_vs_secondary_accuracy_spread: `-0.0882`
- primary_closer_than_secondary_rate: `0.3824`
- close_call_primary_closer_rate: `0.5`

### 5d
- completed_count: `60`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.35`
- primary_path_mean_absolute_error: `0.017316`
- primary_path_median_absolute_error: `0.009586`
- secondary_scenario_hit_rate: `0.2667`
- primary_vs_secondary_accuracy_spread: `0.0833`
- primary_closer_than_secondary_rate: `0.5`
- close_call_primary_closer_rate: `0.5161`

### 10d
- completed_count: `40`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.225`
- primary_path_mean_absolute_error: `0.02218`
- primary_path_median_absolute_error: `0.020002`
- secondary_scenario_hit_rate: `0.225`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- close_call_primary_closer_rate: `0.3529`

### 20d
- completed_count: `0`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `None`
- primary_path_mean_absolute_error: `None`
- primary_path_median_absolute_error: `None`
- secondary_scenario_hit_rate: `None`
- primary_vs_secondary_accuracy_spread: `None`
- primary_closer_than_secondary_rate: `None`
- close_call_primary_closer_rate: `None`

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
