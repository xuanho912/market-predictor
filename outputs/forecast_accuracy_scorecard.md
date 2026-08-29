# Forecast Accuracy Scorecard

Generated at: `2026-08-29T02:54:33.648699+00:00`

## Sample Counts

- total_forecasts: `220`
- raw_forecast_rows: `220`
- deduped_legacy_rows: `0`
- pending_forecasts: `220`
- completed_1d: `216`
- completed_3d: `208`
- completed_5d: `200`
- completed_10d: `180`
- completed_20d: `140`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `216`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3009`
- primary_path_mean_absolute_error: `0.009969`
- primary_path_median_absolute_error: `0.007877`
- secondary_scenario_hit_rate: `0.3194`
- primary_vs_secondary_accuracy_spread: `-0.0185`
- primary_closer_than_secondary_rate: `0.4306`
- close_call_primary_closer_rate: `0.3643`

### 3d
- completed_count: `208`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2308`
- primary_path_mean_absolute_error: `0.016248`
- primary_path_median_absolute_error: `0.01278`
- secondary_scenario_hit_rate: `0.3558`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3846`
- close_call_primary_closer_rate: `0.4132`

### 5d
- completed_count: `200`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.225`
- primary_path_mean_absolute_error: `0.023283`
- primary_path_median_absolute_error: `0.018905`
- secondary_scenario_hit_rate: `0.3`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4`
- close_call_primary_closer_rate: `0.3805`

### 10d
- completed_count: `180`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2`
- primary_path_mean_absolute_error: `0.03467`
- primary_path_median_absolute_error: `0.028296`
- secondary_scenario_hit_rate: `0.3444`
- primary_vs_secondary_accuracy_spread: `-0.1444`
- primary_closer_than_secondary_rate: `0.3`
- close_call_primary_closer_rate: `0.26`

### 20d
- completed_count: `140`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1143`
- primary_path_mean_absolute_error: `0.059833`
- primary_path_median_absolute_error: `0.060059`
- secondary_scenario_hit_rate: `0.2786`
- primary_vs_secondary_accuracy_spread: `-0.1643`
- primary_closer_than_secondary_rate: `0.2571`
- close_call_primary_closer_rate: `0.2639`

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
