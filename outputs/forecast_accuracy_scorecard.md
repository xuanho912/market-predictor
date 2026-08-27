# Forecast Accuracy Scorecard

Generated at: `2026-08-27T14:48:41.493561+00:00`

## Sample Counts

- total_forecasts: `212`
- raw_forecast_rows: `212`
- deduped_legacy_rows: `0`
- pending_forecasts: `212`
- completed_1d: `208`
- completed_3d: `200`
- completed_5d: `192`
- completed_10d: `172`
- completed_20d: `132`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `208`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3077`
- primary_path_mean_absolute_error: `0.010069`
- primary_path_median_absolute_error: `0.007936`
- secondary_scenario_hit_rate: `0.3221`
- primary_vs_secondary_accuracy_spread: `-0.0144`
- primary_closer_than_secondary_rate: `0.4423`
- close_call_primary_closer_rate: `0.3802`

### 3d
- completed_count: `200`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.24`
- primary_path_mean_absolute_error: `0.016149`
- primary_path_median_absolute_error: `0.012757`
- secondary_scenario_hit_rate: `0.35`
- primary_vs_secondary_accuracy_spread: `-0.11`
- primary_closer_than_secondary_rate: `0.39`
- close_call_primary_closer_rate: `0.4248`

### 5d
- completed_count: `192`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.224`
- primary_path_mean_absolute_error: `0.023245`
- primary_path_median_absolute_error: `0.018502`
- secondary_scenario_hit_rate: `0.3021`
- primary_vs_secondary_accuracy_spread: `-0.0781`
- primary_closer_than_secondary_rate: `0.401`
- close_call_primary_closer_rate: `0.3704`

### 10d
- completed_count: `172`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2093`
- primary_path_mean_absolute_error: `0.034892`
- primary_path_median_absolute_error: `0.02869`
- secondary_scenario_hit_rate: `0.343`
- primary_vs_secondary_accuracy_spread: `-0.1337`
- primary_closer_than_secondary_rate: `0.314`
- close_call_primary_closer_rate: `0.268`

### 20d
- completed_count: `132`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1136`
- primary_path_mean_absolute_error: `0.059464`
- primary_path_median_absolute_error: `0.060059`
- secondary_scenario_hit_rate: `0.2879`
- primary_vs_secondary_accuracy_spread: `-0.1742`
- primary_closer_than_secondary_rate: `0.25`
- close_call_primary_closer_rate: `0.2424`

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
