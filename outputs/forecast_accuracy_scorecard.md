# Forecast Accuracy Scorecard

Generated at: `2026-07-17T23:41:11.511678+00:00`

## Sample Counts

- total_forecasts: `100`
- raw_forecast_rows: `100`
- deduped_legacy_rows: `0`
- pending_forecasts: `100`
- completed_1d: `96`
- completed_3d: `88`
- completed_5d: `80`
- completed_10d: `60`
- completed_20d: `20`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `96`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.375`
- primary_path_mean_absolute_error: `0.009637`
- primary_path_median_absolute_error: `0.006756`
- secondary_scenario_hit_rate: `0.2396`
- primary_vs_secondary_accuracy_spread: `0.1354`
- primary_closer_than_secondary_rate: `0.5312`
- close_call_primary_closer_rate: `0.5208`

### 3d
- completed_count: `88`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2614`
- primary_path_mean_absolute_error: `0.013096`
- primary_path_median_absolute_error: `0.011847`
- secondary_scenario_hit_rate: `0.3636`
- primary_vs_secondary_accuracy_spread: `-0.1023`
- primary_closer_than_secondary_rate: `0.3523`
- close_call_primary_closer_rate: `0.4222`

### 5d
- completed_count: `80`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.325`
- primary_path_mean_absolute_error: `0.016655`
- primary_path_median_absolute_error: `0.009471`
- secondary_scenario_hit_rate: `0.275`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4875`
- close_call_primary_closer_rate: `0.4615`

### 10d
- completed_count: `60`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.024016`
- primary_path_median_absolute_error: `0.020874`
- secondary_scenario_hit_rate: `0.35`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4`
- close_call_primary_closer_rate: `0.3226`

### 20d
- completed_count: `20`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.1`
- primary_path_mean_absolute_error: `0.041399`
- primary_path_median_absolute_error: `0.036739`
- secondary_scenario_hit_rate: `0.2`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.5`
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
