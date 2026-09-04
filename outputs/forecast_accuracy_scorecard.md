# Forecast Accuracy Scorecard

Generated at: `2026-09-04T06:00:16.731817+00:00`

## Sample Counts

- total_forecasts: `236`
- raw_forecast_rows: `236`
- deduped_legacy_rows: `0`
- pending_forecasts: `236`
- completed_1d: `232`
- completed_3d: `224`
- completed_5d: `216`
- completed_10d: `196`
- completed_20d: `156`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `232`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2845`
- primary_path_mean_absolute_error: `0.010063`
- primary_path_median_absolute_error: `0.007877`
- secondary_scenario_hit_rate: `0.3362`
- primary_vs_secondary_accuracy_spread: `-0.0517`
- primary_closer_than_secondary_rate: `0.4052`
- close_call_primary_closer_rate: `0.3357`

### 3d
- completed_count: `224`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2366`
- primary_path_mean_absolute_error: `0.016207`
- primary_path_median_absolute_error: `0.012544`
- secondary_scenario_hit_rate: `0.3571`
- primary_vs_secondary_accuracy_spread: `-0.1205`
- primary_closer_than_secondary_rate: `0.3839`
- close_call_primary_closer_rate: `0.4088`

### 5d
- completed_count: `216`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2269`
- primary_path_mean_absolute_error: `0.022821`
- primary_path_median_absolute_error: `0.018052`
- secondary_scenario_hit_rate: `0.3009`
- primary_vs_secondary_accuracy_spread: `-0.0741`
- primary_closer_than_secondary_rate: `0.3889`
- close_call_primary_closer_rate: `0.3643`

### 10d
- completed_count: `196`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2041`
- primary_path_mean_absolute_error: `0.034579`
- primary_path_median_absolute_error: `0.028296`
- secondary_scenario_hit_rate: `0.3418`
- primary_vs_secondary_accuracy_spread: `-0.1378`
- primary_closer_than_secondary_rate: `0.301`
- close_call_primary_closer_rate: `0.2752`

### 20d
- completed_count: `156`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1154`
- primary_path_mean_absolute_error: `0.059002`
- primary_path_median_absolute_error: `0.058646`
- secondary_scenario_hit_rate: `0.2756`
- primary_vs_secondary_accuracy_spread: `-0.1603`
- primary_closer_than_secondary_rate: `0.2628`
- close_call_primary_closer_rate: `0.2759`

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
