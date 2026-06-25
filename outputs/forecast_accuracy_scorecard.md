# Forecast Accuracy Scorecard

Generated at: `2026-06-25T23:56:31.689544+00:00`

## Sample Counts

- total_forecasts: `40`
- raw_forecast_rows: `40`
- deduped_legacy_rows: `0`
- pending_forecasts: `40`
- completed_1d: `36`
- completed_3d: `28`
- completed_5d: `20`
- completed_10d: `0`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `early_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `36`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.3889`
- primary_path_mean_absolute_error: `0.012538`
- primary_path_median_absolute_error: `0.009086`
- secondary_scenario_hit_rate: `0.2778`
- primary_vs_secondary_accuracy_spread: `0.1111`
- primary_closer_than_secondary_rate: `0.4444`
- close_call_primary_closer_rate: `0.5`

### 3d
- completed_count: `28`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.2857`
- primary_path_mean_absolute_error: `0.012609`
- primary_path_median_absolute_error: `0.010146`
- secondary_scenario_hit_rate: `0.3214`
- primary_vs_secondary_accuracy_spread: `-0.0357`
- primary_closer_than_secondary_rate: `0.3571`
- close_call_primary_closer_rate: `1.0`

### 5d
- completed_count: `20`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.4`
- primary_path_mean_absolute_error: `0.017221`
- primary_path_median_absolute_error: `0.009358`
- secondary_scenario_hit_rate: `0.2`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.5`
- close_call_primary_closer_rate: `1.0`

### 10d
- completed_count: `0`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `None`
- primary_path_mean_absolute_error: `None`
- primary_path_median_absolute_error: `None`
- secondary_scenario_hit_rate: `None`
- primary_vs_secondary_accuracy_spread: `None`
- primary_closer_than_secondary_rate: `None`
- close_call_primary_closer_rate: `None`

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
