# Forecast Accuracy Scorecard

Generated at: `2026-08-19T23:34:23.999748+00:00`

## Sample Counts

- total_forecasts: `192`
- raw_forecast_rows: `192`
- deduped_legacy_rows: `0`
- pending_forecasts: `192`
- completed_1d: `188`
- completed_3d: `180`
- completed_5d: `172`
- completed_10d: `152`
- completed_20d: `112`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `188`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3351`
- primary_path_mean_absolute_error: `0.009789`
- primary_path_median_absolute_error: `0.007623`
- secondary_scenario_hit_rate: `0.3085`
- primary_vs_secondary_accuracy_spread: `0.0266`
- primary_closer_than_secondary_rate: `0.4787`
- close_call_primary_closer_rate: `0.419`

### 3d
- completed_count: `180`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.015805`
- primary_path_median_absolute_error: `0.012544`
- secondary_scenario_hit_rate: `0.35`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.3944`
- close_call_primary_closer_rate: `0.43`

### 5d
- completed_count: `172`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2384`
- primary_path_mean_absolute_error: `0.02302`
- primary_path_median_absolute_error: `0.0176`
- secondary_scenario_hit_rate: `0.314`
- primary_vs_secondary_accuracy_spread: `-0.0756`
- primary_closer_than_secondary_rate: `0.4244`
- close_call_primary_closer_rate: `0.3814`

### 10d
- completed_count: `152`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2171`
- primary_path_mean_absolute_error: `0.035`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3684`
- primary_vs_secondary_accuracy_spread: `-0.1513`
- primary_closer_than_secondary_rate: `0.3224`
- close_call_primary_closer_rate: `0.2619`

### 20d
- completed_count: `112`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1339`
- primary_path_mean_absolute_error: `0.05508`
- primary_path_median_absolute_error: `0.051919`
- secondary_scenario_hit_rate: `0.2768`
- primary_vs_secondary_accuracy_spread: `-0.1429`
- primary_closer_than_secondary_rate: `0.2946`
- close_call_primary_closer_rate: `0.2857`

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
