# Forecast Accuracy Scorecard

Generated at: `2026-08-01T04:39:16.844196+00:00`

## Sample Counts

- total_forecasts: `140`
- raw_forecast_rows: `140`
- deduped_legacy_rows: `0`
- pending_forecasts: `140`
- completed_1d: `136`
- completed_3d: `128`
- completed_5d: `120`
- completed_10d: `100`
- completed_20d: `60`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `136`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3603`
- primary_path_mean_absolute_error: `0.010128`
- primary_path_median_absolute_error: `0.007799`
- secondary_scenario_hit_rate: `0.2721`
- primary_vs_secondary_accuracy_spread: `0.0882`
- primary_closer_than_secondary_rate: `0.5147`
- close_call_primary_closer_rate: `0.4714`

### 3d
- completed_count: `128`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2812`
- primary_path_mean_absolute_error: `0.014032`
- primary_path_median_absolute_error: `0.012132`
- secondary_scenario_hit_rate: `0.3359`
- primary_vs_secondary_accuracy_spread: `-0.0547`
- primary_closer_than_secondary_rate: `0.4062`
- close_call_primary_closer_rate: `0.4615`

### 5d
- completed_count: `120`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2917`
- primary_path_mean_absolute_error: `0.017924`
- primary_path_median_absolute_error: `0.011887`
- secondary_scenario_hit_rate: `0.2833`
- primary_vs_secondary_accuracy_spread: `0.0083`
- primary_closer_than_secondary_rate: `0.4667`
- close_call_primary_closer_rate: `0.4098`

### 10d
- completed_count: `100`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.025831`
- primary_path_median_absolute_error: `0.021591`
- secondary_scenario_hit_rate: `0.28`
- primary_vs_secondary_accuracy_spread: `-0.03`
- primary_closer_than_secondary_rate: `0.38`
- close_call_primary_closer_rate: `0.24`

### 20d
- completed_count: `60`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1333`
- primary_path_mean_absolute_error: `0.054949`
- primary_path_median_absolute_error: `0.052941`
- secondary_scenario_hit_rate: `0.3`
- primary_vs_secondary_accuracy_spread: `-0.1667`
- primary_closer_than_secondary_rate: `0.3167`
- close_call_primary_closer_rate: `0.2903`

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
