# Forecast Accuracy Scorecard

Generated at: `2026-10-10T02:18:02.591169+00:00`

## Sample Counts

- total_forecasts: `336`
- raw_forecast_rows: `336`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `332`
- completed_3d: `324`
- completed_5d: `316`
- completed_10d: `296`
- completed_20d: `256`
- completed_60d: `96`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `332`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2651`
- primary_path_mean_absolute_error: `0.010023`
- primary_path_median_absolute_error: `0.008169`
- secondary_scenario_hit_rate: `0.3404`
- primary_vs_secondary_accuracy_spread: `-0.0753`
- primary_closer_than_secondary_rate: `0.3705`
- close_call_primary_closer_rate: `0.3462`

### 3d
- completed_count: `324`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2531`
- primary_path_mean_absolute_error: `0.016382`
- primary_path_median_absolute_error: `0.01278`
- secondary_scenario_hit_rate: `0.3025`
- primary_vs_secondary_accuracy_spread: `-0.0494`
- primary_closer_than_secondary_rate: `0.3827`
- close_call_primary_closer_rate: `0.4148`

### 5d
- completed_count: `316`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2658`
- primary_path_mean_absolute_error: `0.022029`
- primary_path_median_absolute_error: `0.0176`
- secondary_scenario_hit_rate: `0.2753`
- primary_vs_secondary_accuracy_spread: `-0.0095`
- primary_closer_than_secondary_rate: `0.3924`
- close_call_primary_closer_rate: `0.3918`

### 10d
- completed_count: `296`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.223`
- primary_path_mean_absolute_error: `0.032882`
- primary_path_median_absolute_error: `0.027639`
- secondary_scenario_hit_rate: `0.3345`
- primary_vs_secondary_accuracy_spread: `-0.1115`
- primary_closer_than_secondary_rate: `0.3142`
- close_call_primary_closer_rate: `0.3333`

### 20d
- completed_count: `256`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1367`
- primary_path_mean_absolute_error: `0.058713`
- primary_path_median_absolute_error: `0.054444`
- secondary_scenario_hit_rate: `0.2734`
- primary_vs_secondary_accuracy_spread: `-0.1367`
- primary_closer_than_secondary_rate: `0.2852`
- close_call_primary_closer_rate: `0.3245`

### 60d
- completed_count: `96`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1354`
- primary_path_mean_absolute_error: `0.069143`
- primary_path_median_absolute_error: `0.051195`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.1146`
- primary_closer_than_secondary_rate: `0.4167`
- close_call_primary_closer_rate: `0.5`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
