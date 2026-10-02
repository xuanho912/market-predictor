# Forecast Accuracy Scorecard

Generated at: `2026-10-02T07:04:35.960885+00:00`

## Sample Counts

- total_forecasts: `312`
- raw_forecast_rows: `312`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `308`
- completed_3d: `300`
- completed_5d: `292`
- completed_10d: `272`
- completed_20d: `232`
- completed_60d: `72`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `308`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.263`
- primary_path_mean_absolute_error: `0.01`
- primary_path_median_absolute_error: `0.008075`
- secondary_scenario_hit_rate: `0.3409`
- primary_vs_secondary_accuracy_spread: `-0.0779`
- primary_closer_than_secondary_rate: `0.3766`
- close_call_primary_closer_rate: `0.345`

### 3d
- completed_count: `300`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2567`
- primary_path_mean_absolute_error: `0.016113`
- primary_path_median_absolute_error: `0.012428`
- secondary_scenario_hit_rate: `0.31`
- primary_vs_secondary_accuracy_spread: `-0.0533`
- primary_closer_than_secondary_rate: `0.3867`
- close_call_primary_closer_rate: `0.4142`

### 5d
- completed_count: `292`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2705`
- primary_path_mean_absolute_error: `0.021769`
- primary_path_median_absolute_error: `0.016363`
- secondary_scenario_hit_rate: `0.2808`
- primary_vs_secondary_accuracy_spread: `-0.0103`
- primary_closer_than_secondary_rate: `0.4041`
- close_call_primary_closer_rate: `0.3855`

### 10d
- completed_count: `272`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2316`
- primary_path_mean_absolute_error: `0.032899`
- primary_path_median_absolute_error: `0.027368`
- secondary_scenario_hit_rate: `0.3272`
- primary_vs_secondary_accuracy_spread: `-0.0956`
- primary_closer_than_secondary_rate: `0.3235`
- close_call_primary_closer_rate: `0.3333`

### 20d
- completed_count: `232`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1336`
- primary_path_mean_absolute_error: `0.0599`
- primary_path_median_absolute_error: `0.055268`
- secondary_scenario_hit_rate: `0.2802`
- primary_vs_secondary_accuracy_spread: `-0.1466`
- primary_closer_than_secondary_rate: `0.2802`
- close_call_primary_closer_rate: `0.3077`

### 60d
- completed_count: `72`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1111`
- primary_path_mean_absolute_error: `0.071489`
- primary_path_median_absolute_error: `0.050587`
- secondary_scenario_hit_rate: `0.2778`
- primary_vs_secondary_accuracy_spread: `-0.1667`
- primary_closer_than_secondary_rate: `0.4028`
- close_call_primary_closer_rate: `0.4571`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
