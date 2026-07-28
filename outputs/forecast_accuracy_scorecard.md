# Forecast Accuracy Scorecard

Generated at: `2026-07-28T04:33:01.770252+00:00`

## Sample Counts

- total_forecasts: `124`
- raw_forecast_rows: `124`
- deduped_legacy_rows: `0`
- pending_forecasts: `124`
- completed_1d: `120`
- completed_3d: `112`
- completed_5d: `104`
- completed_10d: `84`
- completed_20d: `44`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `120`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3583`
- primary_path_mean_absolute_error: `0.009567`
- primary_path_median_absolute_error: `0.007476`
- secondary_scenario_hit_rate: `0.275`
- primary_vs_secondary_accuracy_spread: `0.0833`
- primary_closer_than_secondary_rate: `0.5167`
- close_call_primary_closer_rate: `0.459`

### 3d
- completed_count: `112`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2946`
- primary_path_mean_absolute_error: `0.013245`
- primary_path_median_absolute_error: `0.011864`
- secondary_scenario_hit_rate: `0.3304`
- primary_vs_secondary_accuracy_spread: `-0.0357`
- primary_closer_than_secondary_rate: `0.4107`
- close_call_primary_closer_rate: `0.4643`

### 5d
- completed_count: `104`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2981`
- primary_path_mean_absolute_error: `0.016776`
- primary_path_median_absolute_error: `0.011392`
- secondary_scenario_hit_rate: `0.2596`
- primary_vs_secondary_accuracy_spread: `0.0385`
- primary_closer_than_secondary_rate: `0.4712`
- close_call_primary_closer_rate: `0.4444`

### 10d
- completed_count: `84`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2262`
- primary_path_mean_absolute_error: `0.026579`
- primary_path_median_absolute_error: `0.021591`
- secondary_scenario_hit_rate: `0.2976`
- primary_vs_secondary_accuracy_spread: `-0.0714`
- primary_closer_than_secondary_rate: `0.3571`
- close_call_primary_closer_rate: `0.2558`

### 20d
- completed_count: `44`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.1364`
- primary_path_mean_absolute_error: `0.049283`
- primary_path_median_absolute_error: `0.040393`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.1136`
- primary_closer_than_secondary_rate: `0.3636`
- close_call_primary_closer_rate: `0.381`

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
