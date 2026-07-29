# Forecast Accuracy Scorecard

Generated at: `2026-07-29T23:50:23.455872+00:00`

## Sample Counts

- total_forecasts: `132`
- raw_forecast_rows: `132`
- deduped_legacy_rows: `0`
- pending_forecasts: `132`
- completed_1d: `128`
- completed_3d: `120`
- completed_5d: `112`
- completed_10d: `92`
- completed_20d: `52`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `128`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3672`
- primary_path_mean_absolute_error: `0.009838`
- primary_path_median_absolute_error: `0.007709`
- secondary_scenario_hit_rate: `0.2734`
- primary_vs_secondary_accuracy_spread: `0.0938`
- primary_closer_than_secondary_rate: `0.5234`
- close_call_primary_closer_rate: `0.4615`

### 3d
- completed_count: `120`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3`
- primary_path_mean_absolute_error: `0.01364`
- primary_path_median_absolute_error: `0.011974`
- secondary_scenario_hit_rate: `0.325`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4167`
- close_call_primary_closer_rate: `0.459`

### 5d
- completed_count: `112`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3036`
- primary_path_mean_absolute_error: `0.016805`
- primary_path_median_absolute_error: `0.011392`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `0.0536`
- primary_closer_than_secondary_rate: `0.4911`
- close_call_primary_closer_rate: `0.4464`

### 10d
- completed_count: `92`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.026484`
- primary_path_median_absolute_error: `0.021591`
- secondary_scenario_hit_rate: `0.2826`
- primary_vs_secondary_accuracy_spread: `-0.0326`
- primary_closer_than_secondary_rate: `0.3804`
- close_call_primary_closer_rate: `0.2391`

### 20d
- completed_count: `52`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1154`
- primary_path_mean_absolute_error: `0.055072`
- primary_path_median_absolute_error: `0.044895`
- secondary_scenario_hit_rate: `0.2692`
- primary_vs_secondary_accuracy_spread: `-0.1538`
- primary_closer_than_secondary_rate: `0.3269`
- close_call_primary_closer_rate: `0.3077`

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
