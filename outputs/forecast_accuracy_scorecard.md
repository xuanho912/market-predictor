# Forecast Accuracy Scorecard

Generated at: `2026-09-23T01:35:13.026447+00:00`

## Sample Counts

- total_forecasts: `284`
- raw_forecast_rows: `284`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `280`
- completed_3d: `272`
- completed_5d: `264`
- completed_10d: `244`
- completed_20d: `204`
- completed_60d: `44`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `280`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2714`
- primary_path_mean_absolute_error: `0.010064`
- primary_path_median_absolute_error: `0.007877`
- secondary_scenario_hit_rate: `0.3357`
- primary_vs_secondary_accuracy_spread: `-0.0643`
- primary_closer_than_secondary_rate: `0.3929`
- close_call_primary_closer_rate: `0.3544`

### 3d
- completed_count: `272`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2647`
- primary_path_mean_absolute_error: `0.016272`
- primary_path_median_absolute_error: `0.012624`
- secondary_scenario_hit_rate: `0.3235`
- primary_vs_secondary_accuracy_spread: `-0.0588`
- primary_closer_than_secondary_rate: `0.3934`
- close_call_primary_closer_rate: `0.4314`

### 5d
- completed_count: `264`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2879`
- primary_path_mean_absolute_error: `0.021584`
- primary_path_median_absolute_error: `0.015233`
- secondary_scenario_hit_rate: `0.2765`
- primary_vs_secondary_accuracy_spread: `0.0114`
- primary_closer_than_secondary_rate: `0.4242`
- close_call_primary_closer_rate: `0.3974`

### 10d
- completed_count: `244`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2377`
- primary_path_mean_absolute_error: `0.033116`
- primary_path_median_absolute_error: `0.027239`
- secondary_scenario_hit_rate: `0.332`
- primary_vs_secondary_accuracy_spread: `-0.0943`
- primary_closer_than_secondary_rate: `0.3402`
- close_call_primary_closer_rate: `0.3311`

### 20d
- completed_count: `204`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1127`
- primary_path_mean_absolute_error: `0.061387`
- primary_path_median_absolute_error: `0.058866`
- secondary_scenario_hit_rate: `0.2892`
- primary_vs_secondary_accuracy_spread: `-0.1765`
- primary_closer_than_secondary_rate: `0.2549`
- close_call_primary_closer_rate: `0.2821`

### 60d
- completed_count: `44`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.1136`
- primary_path_mean_absolute_error: `0.065542`
- primary_path_median_absolute_error: `0.044802`
- secondary_scenario_hit_rate: `0.1591`
- primary_vs_secondary_accuracy_spread: `-0.0455`
- primary_closer_than_secondary_rate: `0.4091`
- close_call_primary_closer_rate: `0.4762`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
