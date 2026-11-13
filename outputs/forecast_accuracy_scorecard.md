# Forecast Accuracy Scorecard

Generated at: `2026-11-13T08:03:58.669805+00:00`

## Sample Counts

- total_forecasts: `432`
- raw_forecast_rows: `432`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `428`
- completed_3d: `420`
- completed_5d: `412`
- completed_10d: `392`
- completed_20d: `352`
- completed_60d: `192`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `428`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.264`
- primary_path_mean_absolute_error: `0.010863`
- primary_path_median_absolute_error: `0.008926`
- secondary_scenario_hit_rate: `0.3435`
- primary_vs_secondary_accuracy_spread: `-0.0794`
- primary_closer_than_secondary_rate: `0.3645`
- close_call_primary_closer_rate: `0.3408`

### 3d
- completed_count: `420`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2738`
- primary_path_mean_absolute_error: `0.017193`
- primary_path_median_absolute_error: `0.013157`
- secondary_scenario_hit_rate: `0.3143`
- primary_vs_secondary_accuracy_spread: `-0.0405`
- primary_closer_than_secondary_rate: `0.3881`
- close_call_primary_closer_rate: `0.4306`

### 5d
- completed_count: `412`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2549`
- primary_path_mean_absolute_error: `0.02354`
- primary_path_median_absolute_error: `0.019377`
- secondary_scenario_hit_rate: `0.3058`
- primary_vs_secondary_accuracy_spread: `-0.051`
- primary_closer_than_secondary_rate: `0.3641`
- close_call_primary_closer_rate: `0.3721`

### 10d
- completed_count: `392`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2602`
- primary_path_mean_absolute_error: `0.032858`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3112`
- primary_vs_secondary_accuracy_spread: `-0.051`
- primary_closer_than_secondary_rate: `0.3495`
- close_call_primary_closer_rate: `0.3366`

### 20d
- completed_count: `352`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1818`
- primary_path_mean_absolute_error: `0.057283`
- primary_path_median_absolute_error: `0.054226`
- secondary_scenario_hit_rate: `0.267`
- primary_vs_secondary_accuracy_spread: `-0.0852`
- primary_closer_than_secondary_rate: `0.3438`
- close_call_primary_closer_rate: `0.3915`

### 60d
- completed_count: `192`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1302`
- primary_path_mean_absolute_error: `0.078423`
- primary_path_median_absolute_error: `0.071055`
- secondary_scenario_hit_rate: `0.2396`
- primary_vs_secondary_accuracy_spread: `-0.1094`
- primary_closer_than_secondary_rate: `0.3698`
- close_call_primary_closer_rate: `0.4444`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
