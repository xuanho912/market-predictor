# Forecast Accuracy Scorecard

Generated at: `2026-11-20T03:48:19.458137+00:00`

## Sample Counts

- total_forecasts: `452`
- raw_forecast_rows: `452`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `448`
- completed_3d: `440`
- completed_5d: `432`
- completed_10d: `412`
- completed_20d: `372`
- completed_60d: `212`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `448`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2723`
- primary_path_mean_absolute_error: `0.010819`
- primary_path_median_absolute_error: `0.008926`
- secondary_scenario_hit_rate: `0.3371`
- primary_vs_secondary_accuracy_spread: `-0.0647`
- primary_closer_than_secondary_rate: `0.375`
- close_call_primary_closer_rate: `0.3493`

### 3d
- completed_count: `440`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.275`
- primary_path_mean_absolute_error: `0.017939`
- primary_path_median_absolute_error: `0.013417`
- secondary_scenario_hit_rate: `0.3136`
- primary_vs_secondary_accuracy_spread: `-0.0386`
- primary_closer_than_secondary_rate: `0.3909`
- close_call_primary_closer_rate: `0.4323`

### 5d
- completed_count: `432`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2593`
- primary_path_mean_absolute_error: `0.024593`
- primary_path_median_absolute_error: `0.020033`
- secondary_scenario_hit_rate: `0.3032`
- primary_vs_secondary_accuracy_spread: `-0.044`
- primary_closer_than_secondary_rate: `0.3681`
- close_call_primary_closer_rate: `0.3705`

### 10d
- completed_count: `412`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2743`
- primary_path_mean_absolute_error: `0.033103`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3107`
- primary_vs_secondary_accuracy_spread: `-0.0364`
- primary_closer_than_secondary_rate: `0.3641`
- close_call_primary_closer_rate: `0.3442`

### 20d
- completed_count: `372`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2097`
- primary_path_mean_absolute_error: `0.05606`
- primary_path_median_absolute_error: `0.053786`
- secondary_scenario_hit_rate: `0.2661`
- primary_vs_secondary_accuracy_spread: `-0.0565`
- primary_closer_than_secondary_rate: `0.3656`
- close_call_primary_closer_rate: `0.399`

### 60d
- completed_count: `212`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1651`
- primary_path_mean_absolute_error: `0.078963`
- primary_path_median_absolute_error: `0.071055`
- secondary_scenario_hit_rate: `0.2311`
- primary_vs_secondary_accuracy_spread: `-0.066`
- primary_closer_than_secondary_rate: `0.3868`
- close_call_primary_closer_rate: `0.456`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_not_better_than_no_edge_keep_confidence_capped`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
