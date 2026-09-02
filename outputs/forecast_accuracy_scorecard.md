# Forecast Accuracy Scorecard

Generated at: `2026-09-02T23:33:40.177430+00:00`

## Sample Counts

- total_forecasts: `232`
- raw_forecast_rows: `232`
- deduped_legacy_rows: `0`
- pending_forecasts: `232`
- completed_1d: `226`
- completed_3d: `218`
- completed_5d: `210`
- completed_10d: `190`
- completed_20d: `150`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `226`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.292`
- primary_path_mean_absolute_error: `0.010035`
- primary_path_median_absolute_error: `0.007799`
- secondary_scenario_hit_rate: `0.3274`
- primary_vs_secondary_accuracy_spread: `-0.0354`
- primary_closer_than_secondary_rate: `0.4159`
- close_call_primary_closer_rate: `0.3453`

### 3d
- completed_count: `218`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2339`
- primary_path_mean_absolute_error: `0.016208`
- primary_path_median_absolute_error: `0.012544`
- secondary_scenario_hit_rate: `0.3486`
- primary_vs_secondary_accuracy_spread: `-0.1147`
- primary_closer_than_secondary_rate: `0.3853`
- close_call_primary_closer_rate: `0.4122`

### 5d
- completed_count: `210`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2238`
- primary_path_mean_absolute_error: `0.022873`
- primary_path_median_absolute_error: `0.018052`
- secondary_scenario_hit_rate: `0.3048`
- primary_vs_secondary_accuracy_spread: `-0.081`
- primary_closer_than_secondary_rate: `0.3905`
- close_call_primary_closer_rate: `0.3659`

### 10d
- completed_count: `190`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2105`
- primary_path_mean_absolute_error: `0.034394`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3368`
- primary_vs_secondary_accuracy_spread: `-0.1263`
- primary_closer_than_secondary_rate: `0.3053`
- close_call_primary_closer_rate: `0.271`

### 20d
- completed_count: `150`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1133`
- primary_path_mean_absolute_error: `0.059191`
- primary_path_median_absolute_error: `0.058866`
- secondary_scenario_hit_rate: `0.28`
- primary_vs_secondary_accuracy_spread: `-0.1667`
- primary_closer_than_secondary_rate: `0.2667`
- close_call_primary_closer_rate: `0.2771`

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
