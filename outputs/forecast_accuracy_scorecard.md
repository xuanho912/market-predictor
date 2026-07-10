# Forecast Accuracy Scorecard

Generated at: `2026-07-10T07:05:37.336411+00:00`

## Sample Counts

- total_forecasts: `76`
- raw_forecast_rows: `76`
- deduped_legacy_rows: `0`
- pending_forecasts: `76`
- completed_1d: `72`
- completed_3d: `64`
- completed_5d: `56`
- completed_10d: `36`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `72`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.4167`
- primary_path_mean_absolute_error: `0.010256`
- primary_path_median_absolute_error: `0.007493`
- secondary_scenario_hit_rate: `0.2639`
- primary_vs_secondary_accuracy_spread: `0.1528`
- primary_closer_than_secondary_rate: `0.5556`
- close_call_primary_closer_rate: `0.6`

### 3d
- completed_count: `64`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2812`
- primary_path_mean_absolute_error: `0.013193`
- primary_path_median_absolute_error: `0.011847`
- secondary_scenario_hit_rate: `0.3594`
- primary_vs_secondary_accuracy_spread: `-0.0781`
- primary_closer_than_secondary_rate: `0.375`
- close_call_primary_closer_rate: `0.5`

### 5d
- completed_count: `56`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3393`
- primary_path_mean_absolute_error: `0.01789`
- primary_path_median_absolute_error: `0.009586`
- secondary_scenario_hit_rate: `0.2857`
- primary_vs_secondary_accuracy_spread: `0.0536`
- primary_closer_than_secondary_rate: `0.4821`
- close_call_primary_closer_rate: `0.4828`

### 10d
- completed_count: `36`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.2222`
- primary_path_mean_absolute_error: `0.021367`
- primary_path_median_absolute_error: `0.020002`
- secondary_scenario_hit_rate: `0.1944`
- primary_vs_secondary_accuracy_spread: `0.0278`
- primary_closer_than_secondary_rate: `0.4444`
- close_call_primary_closer_rate: `0.3571`

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
