# Forecast Accuracy Scorecard

Generated at: `2026-08-21T23:12:17.834714+00:00`

## Sample Counts

- total_forecasts: `200`
- raw_forecast_rows: `200`
- deduped_legacy_rows: `0`
- pending_forecasts: `200`
- completed_1d: `196`
- completed_3d: `188`
- completed_5d: `180`
- completed_10d: `160`
- completed_20d: `120`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `196`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3214`
- primary_path_mean_absolute_error: `0.010047`
- primary_path_median_absolute_error: `0.007936`
- secondary_scenario_hit_rate: `0.3214`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4592`
- close_call_primary_closer_rate: `0.4037`

### 3d
- completed_count: `188`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.015985`
- primary_path_median_absolute_error: `0.012544`
- secondary_scenario_hit_rate: `0.3457`
- primary_vs_secondary_accuracy_spread: `-0.0957`
- primary_closer_than_secondary_rate: `0.3989`
- close_call_primary_closer_rate: `0.4286`

### 5d
- completed_count: `180`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2278`
- primary_path_mean_absolute_error: `0.023245`
- primary_path_median_absolute_error: `0.018905`
- secondary_scenario_hit_rate: `0.3167`
- primary_vs_secondary_accuracy_spread: `-0.0889`
- primary_closer_than_secondary_rate: `0.4056`
- close_call_primary_closer_rate: `0.37`

### 10d
- completed_count: `160`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2188`
- primary_path_mean_absolute_error: `0.034634`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3688`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3187`
- close_call_primary_closer_rate: `0.2667`

### 20d
- completed_count: `120`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.05688`
- primary_path_median_absolute_error: `0.054492`
- secondary_scenario_hit_rate: `0.275`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.275`
- close_call_primary_closer_rate: `0.2623`

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
