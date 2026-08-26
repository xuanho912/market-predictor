# Forecast Accuracy Scorecard

Generated at: `2026-08-26T13:20:49.767704+00:00`

## Sample Counts

- total_forecasts: `208`
- raw_forecast_rows: `208`
- deduped_legacy_rows: `0`
- pending_forecasts: `208`
- completed_1d: `204`
- completed_3d: `196`
- completed_5d: `188`
- completed_10d: `168`
- completed_20d: `128`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `204`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3137`
- primary_path_mean_absolute_error: `0.010196`
- primary_path_median_absolute_error: `0.008169`
- secondary_scenario_hit_rate: `0.3235`
- primary_vs_secondary_accuracy_spread: `-0.0098`
- primary_closer_than_secondary_rate: `0.4461`
- close_call_primary_closer_rate: `0.3846`

### 3d
- completed_count: `196`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2398`
- primary_path_mean_absolute_error: `0.016117`
- primary_path_median_absolute_error: `0.012757`
- secondary_scenario_hit_rate: `0.3571`
- primary_vs_secondary_accuracy_spread: `-0.1173`
- primary_closer_than_secondary_rate: `0.3878`
- close_call_primary_closer_rate: `0.422`

### 5d
- completed_count: `188`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2234`
- primary_path_mean_absolute_error: `0.023261`
- primary_path_median_absolute_error: `0.018502`
- secondary_scenario_hit_rate: `0.3032`
- primary_vs_secondary_accuracy_spread: `-0.0798`
- primary_closer_than_secondary_rate: `0.4043`
- close_call_primary_closer_rate: `0.3714`

### 10d
- completed_count: `168`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2143`
- primary_path_mean_absolute_error: `0.03455`
- primary_path_median_absolute_error: `0.028296`
- secondary_scenario_hit_rate: `0.3512`
- primary_vs_secondary_accuracy_spread: `-0.1369`
- primary_closer_than_secondary_rate: `0.3214`
- close_call_primary_closer_rate: `0.2737`

### 20d
- completed_count: `128`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1172`
- primary_path_mean_absolute_error: `0.05848`
- primary_path_median_absolute_error: `0.058866`
- secondary_scenario_hit_rate: `0.2734`
- primary_vs_secondary_accuracy_spread: `-0.1562`
- primary_closer_than_secondary_rate: `0.2578`
- close_call_primary_closer_rate: `0.2462`

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
