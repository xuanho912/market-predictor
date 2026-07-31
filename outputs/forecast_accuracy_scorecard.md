# Forecast Accuracy Scorecard

Generated at: `2026-07-31T04:46:29.832528+00:00`

## Sample Counts

- total_forecasts: `136`
- raw_forecast_rows: `136`
- deduped_legacy_rows: `0`
- pending_forecasts: `136`
- completed_1d: `132`
- completed_3d: `124`
- completed_5d: `116`
- completed_10d: `96`
- completed_20d: `56`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `132`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3561`
- primary_path_mean_absolute_error: `0.010261`
- primary_path_median_absolute_error: `0.007877`
- secondary_scenario_hit_rate: `0.2803`
- primary_vs_secondary_accuracy_spread: `0.0758`
- primary_closer_than_secondary_rate: `0.5076`
- close_call_primary_closer_rate: `0.4545`

### 3d
- completed_count: `124`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2903`
- primary_path_mean_absolute_error: `0.013794`
- primary_path_median_absolute_error: `0.012088`
- secondary_scenario_hit_rate: `0.3306`
- primary_vs_secondary_accuracy_spread: `-0.0403`
- primary_closer_than_secondary_rate: `0.4113`
- close_call_primary_closer_rate: `0.4603`

### 5d
- completed_count: `116`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3017`
- primary_path_mean_absolute_error: `0.017215`
- primary_path_median_absolute_error: `0.011526`
- secondary_scenario_hit_rate: `0.2586`
- primary_vs_secondary_accuracy_spread: `0.0431`
- primary_closer_than_secondary_rate: `0.4828`
- close_call_primary_closer_rate: `0.431`

### 10d
- completed_count: `96`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.026067`
- primary_path_median_absolute_error: `0.021591`
- secondary_scenario_hit_rate: `0.2812`
- primary_vs_secondary_accuracy_spread: `-0.0312`
- primary_closer_than_secondary_rate: `0.375`
- close_call_primary_closer_rate: `0.2292`

### 20d
- completed_count: `56`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.054749`
- primary_path_median_absolute_error: `0.048519`
- secondary_scenario_hit_rate: `0.2857`
- primary_vs_secondary_accuracy_spread: `-0.1607`
- primary_closer_than_secondary_rate: `0.3214`
- close_call_primary_closer_rate: `0.3103`

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
