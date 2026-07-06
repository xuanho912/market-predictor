# Forecast Accuracy Scorecard

Generated at: `2026-07-06T15:57:44.898601+00:00`

## Sample Counts

- total_forecasts: `60`
- raw_forecast_rows: `60`
- deduped_legacy_rows: `0`
- pending_forecasts: `60`
- completed_1d: `56`
- completed_3d: `48`
- completed_5d: `40`
- completed_10d: `20`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `56`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3571`
- primary_path_mean_absolute_error: `0.011179`
- primary_path_median_absolute_error: `0.008723`
- secondary_scenario_hit_rate: `0.2857`
- primary_vs_secondary_accuracy_spread: `0.0714`
- primary_closer_than_secondary_rate: `0.5`
- close_call_primary_closer_rate: `0.5517`

### 3d
- completed_count: `48`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.012928`
- primary_path_median_absolute_error: `0.011537`
- secondary_scenario_hit_rate: `0.3542`
- primary_vs_secondary_accuracy_spread: `-0.1042`
- primary_closer_than_secondary_rate: `0.3542`
- close_call_primary_closer_rate: `0.5417`

### 5d
- completed_count: `40`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.3`
- primary_path_mean_absolute_error: `0.018525`
- primary_path_median_absolute_error: `0.01045`
- secondary_scenario_hit_rate: `0.275`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.475`
- close_call_primary_closer_rate: `0.4706`

### 10d
- completed_count: `20`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.2`
- primary_path_mean_absolute_error: `0.016294`
- primary_path_median_absolute_error: `0.011981`
- secondary_scenario_hit_rate: `0.15`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.55`
- close_call_primary_closer_rate: `1.0`

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
