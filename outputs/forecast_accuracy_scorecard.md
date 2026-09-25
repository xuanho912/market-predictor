# Forecast Accuracy Scorecard

Generated at: `2026-09-25T17:15:46.642580+00:00`

## Sample Counts

- total_forecasts: `292`
- raw_forecast_rows: `292`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `288`
- completed_3d: `280`
- completed_5d: `272`
- completed_10d: `252`
- completed_20d: `212`
- completed_60d: `52`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `288`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2708`
- primary_path_mean_absolute_error: `0.010009`
- primary_path_median_absolute_error: `0.007877`
- secondary_scenario_hit_rate: `0.3403`
- primary_vs_secondary_accuracy_spread: `-0.0694`
- primary_closer_than_secondary_rate: `0.3924`
- close_call_primary_closer_rate: `0.3515`

### 3d
- completed_count: `280`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2571`
- primary_path_mean_absolute_error: `0.016325`
- primary_path_median_absolute_error: `0.012757`
- secondary_scenario_hit_rate: `0.3214`
- primary_vs_secondary_accuracy_spread: `-0.0643`
- primary_closer_than_secondary_rate: `0.3893`
- close_call_primary_closer_rate: `0.4241`

### 5d
- completed_count: `272`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2831`
- primary_path_mean_absolute_error: `0.021855`
- primary_path_median_absolute_error: `0.016139`
- secondary_scenario_hit_rate: `0.2831`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4154`
- close_call_primary_closer_rate: `0.3987`

### 10d
- completed_count: `252`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2381`
- primary_path_mean_absolute_error: `0.033059`
- primary_path_median_absolute_error: `0.0276`
- secondary_scenario_hit_rate: `0.3294`
- primary_vs_secondary_accuracy_spread: `-0.0913`
- primary_closer_than_secondary_rate: `0.3373`
- close_call_primary_closer_rate: `0.3333`

### 20d
- completed_count: `212`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1179`
- primary_path_mean_absolute_error: `0.061184`
- primary_path_median_absolute_error: `0.058578`
- secondary_scenario_hit_rate: `0.2925`
- primary_vs_secondary_accuracy_spread: `-0.1745`
- primary_closer_than_secondary_rate: `0.2642`
- close_call_primary_closer_rate: `0.296`

### 60d
- completed_count: `52`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1154`
- primary_path_mean_absolute_error: `0.070737`
- primary_path_median_absolute_error: `0.050587`
- secondary_scenario_hit_rate: `0.2115`
- primary_vs_secondary_accuracy_spread: `-0.0962`
- primary_closer_than_secondary_rate: `0.4038`
- close_call_primary_closer_rate: `0.4231`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
