# Forecast Accuracy Scorecard

Generated at: `2026-07-28T21:37:45.362132+00:00`

## Sample Counts

- total_forecasts: `128`
- raw_forecast_rows: `128`
- deduped_legacy_rows: `0`
- pending_forecasts: `128`
- completed_1d: `124`
- completed_3d: `116`
- completed_5d: `108`
- completed_10d: `88`
- completed_20d: `48`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `124`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3548`
- primary_path_mean_absolute_error: `0.009735`
- primary_path_median_absolute_error: `0.007709`
- secondary_scenario_hit_rate: `0.2823`
- primary_vs_secondary_accuracy_spread: `0.0726`
- primary_closer_than_secondary_rate: `0.5081`
- close_call_primary_closer_rate: `0.4444`

### 3d
- completed_count: `116`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2931`
- primary_path_mean_absolute_error: `0.013686`
- primary_path_median_absolute_error: `0.011974`
- secondary_scenario_hit_rate: `0.3362`
- primary_vs_secondary_accuracy_spread: `-0.0431`
- primary_closer_than_secondary_rate: `0.4052`
- close_call_primary_closer_rate: `0.4483`

### 5d
- completed_count: `108`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3056`
- primary_path_mean_absolute_error: `0.016812`
- primary_path_median_absolute_error: `0.011392`
- secondary_scenario_hit_rate: `0.2593`
- primary_vs_secondary_accuracy_spread: `0.0463`
- primary_closer_than_secondary_rate: `0.4722`
- close_call_primary_closer_rate: `0.4364`

### 10d
- completed_count: `88`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2386`
- primary_path_mean_absolute_error: `0.026265`
- primary_path_median_absolute_error: `0.021591`
- secondary_scenario_hit_rate: `0.2955`
- primary_vs_secondary_accuracy_spread: `-0.0568`
- primary_closer_than_secondary_rate: `0.3636`
- close_call_primary_closer_rate: `0.2444`

### 20d
- completed_count: `48`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.052332`
- primary_path_median_absolute_error: `0.043345`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3333`
- close_call_primary_closer_rate: `0.3333`

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
