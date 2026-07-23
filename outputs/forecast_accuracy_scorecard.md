# Forecast Accuracy Scorecard

Generated at: `2026-07-23T06:20:08.717534+00:00`

## Sample Counts

- total_forecasts: `112`
- raw_forecast_rows: `112`
- deduped_legacy_rows: `0`
- pending_forecasts: `112`
- completed_1d: `108`
- completed_3d: `100`
- completed_5d: `92`
- completed_10d: `72`
- completed_20d: `32`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `108`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3611`
- primary_path_mean_absolute_error: `0.009593`
- primary_path_median_absolute_error: `0.007198`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `0.1111`
- primary_closer_than_secondary_rate: `0.5185`
- close_call_primary_closer_rate: `0.4727`

### 3d
- completed_count: `100`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.26`
- primary_path_mean_absolute_error: `0.013681`
- primary_path_median_absolute_error: `0.011864`
- secondary_scenario_hit_rate: `0.37`
- primary_vs_secondary_accuracy_spread: `-0.11`
- primary_closer_than_secondary_rate: `0.36`
- close_call_primary_closer_rate: `0.4`

### 5d
- completed_count: `92`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3043`
- primary_path_mean_absolute_error: `0.01687`
- primary_path_median_absolute_error: `0.010646`
- secondary_scenario_hit_rate: `0.2717`
- primary_vs_secondary_accuracy_spread: `0.0326`
- primary_closer_than_secondary_rate: `0.4674`
- close_call_primary_closer_rate: `0.4348`

### 10d
- completed_count: `72`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.024444`
- primary_path_median_absolute_error: `0.020874`
- secondary_scenario_hit_rate: `0.3194`
- primary_vs_secondary_accuracy_spread: `-0.0694`
- primary_closer_than_secondary_rate: `0.4028`
- close_call_primary_closer_rate: `0.2857`

### 20d
- completed_count: `32`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.1562`
- primary_path_mean_absolute_error: `0.041451`
- primary_path_median_absolute_error: `0.038018`
- secondary_scenario_hit_rate: `0.2188`
- primary_vs_secondary_accuracy_spread: `-0.0625`
- primary_closer_than_secondary_rate: `0.4688`
- close_call_primary_closer_rate: `0.7`

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
