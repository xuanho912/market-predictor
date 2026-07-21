# Forecast Accuracy Scorecard

Generated at: `2026-07-21T23:46:14.081822+00:00`

## Sample Counts

- total_forecasts: `108`
- raw_forecast_rows: `108`
- deduped_legacy_rows: `0`
- pending_forecasts: `108`
- completed_1d: `104`
- completed_3d: `96`
- completed_5d: `88`
- completed_10d: `68`
- completed_20d: `28`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `104`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3558`
- primary_path_mean_absolute_error: `0.009777`
- primary_path_median_absolute_error: `0.007198`
- secondary_scenario_hit_rate: `0.2596`
- primary_vs_secondary_accuracy_spread: `0.0962`
- primary_closer_than_secondary_rate: `0.5096`
- close_call_primary_closer_rate: `0.4815`

### 3d
- completed_count: `96`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2708`
- primary_path_mean_absolute_error: `0.013303`
- primary_path_median_absolute_error: `0.011856`
- secondary_scenario_hit_rate: `0.3646`
- primary_vs_secondary_accuracy_spread: `-0.0938`
- primary_closer_than_secondary_rate: `0.375`
- close_call_primary_closer_rate: `0.4167`

### 5d
- completed_count: `88`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3068`
- primary_path_mean_absolute_error: `0.016828`
- primary_path_median_absolute_error: `0.009586`
- secondary_scenario_hit_rate: `0.2727`
- primary_vs_secondary_accuracy_spread: `0.0341`
- primary_closer_than_secondary_rate: `0.4773`
- close_call_primary_closer_rate: `0.4444`

### 10d
- completed_count: `68`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.024791`
- primary_path_median_absolute_error: `0.021062`
- secondary_scenario_hit_rate: `0.3235`
- primary_vs_secondary_accuracy_spread: `-0.0735`
- primary_closer_than_secondary_rate: `0.4118`
- close_call_primary_closer_rate: `0.3125`

### 20d
- completed_count: `28`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.1429`
- primary_path_mean_absolute_error: `0.041448`
- primary_path_median_absolute_error: `0.038018`
- secondary_scenario_hit_rate: `0.2143`
- primary_vs_secondary_accuracy_spread: `-0.0714`
- primary_closer_than_secondary_rate: `0.4643`
- close_call_primary_closer_rate: `0.8333`

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
