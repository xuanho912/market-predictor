# Forecast Accuracy Scorecard

Generated at: `2026-09-26T01:11:12.795133+00:00`

## Sample Counts

- total_forecasts: `296`
- raw_forecast_rows: `296`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `292`
- completed_3d: `284`
- completed_5d: `276`
- completed_10d: `256`
- completed_20d: `216`
- completed_60d: `56`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `292`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2671`
- primary_path_mean_absolute_error: `0.010141`
- primary_path_median_absolute_error: `0.008075`
- secondary_scenario_hit_rate: `0.3425`
- primary_vs_secondary_accuracy_spread: `-0.0753`
- primary_closer_than_secondary_rate: `0.387`
- close_call_primary_closer_rate: `0.3494`

### 3d
- completed_count: `284`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2606`
- primary_path_mean_absolute_error: `0.016218`
- primary_path_median_absolute_error: `0.012624`
- secondary_scenario_hit_rate: `0.3169`
- primary_vs_secondary_accuracy_spread: `-0.0563`
- primary_closer_than_secondary_rate: `0.3944`
- close_call_primary_closer_rate: `0.4286`

### 5d
- completed_count: `276`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.279`
- primary_path_mean_absolute_error: `0.022028`
- primary_path_median_absolute_error: `0.016339`
- secondary_scenario_hit_rate: `0.2862`
- primary_vs_secondary_accuracy_spread: `-0.0072`
- primary_closer_than_secondary_rate: `0.4094`
- close_call_primary_closer_rate: `0.3935`

### 10d
- completed_count: `256`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2344`
- primary_path_mean_absolute_error: `0.032991`
- primary_path_median_absolute_error: `0.027368`
- secondary_scenario_hit_rate: `0.332`
- primary_vs_secondary_accuracy_spread: `-0.0977`
- primary_closer_than_secondary_rate: `0.332`
- close_call_primary_closer_rate: `0.3311`

### 20d
- completed_count: `216`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1157`
- primary_path_mean_absolute_error: `0.061196`
- primary_path_median_absolute_error: `0.058348`
- secondary_scenario_hit_rate: `0.2917`
- primary_vs_secondary_accuracy_spread: `-0.1759`
- primary_closer_than_secondary_rate: `0.2639`
- close_call_primary_closer_rate: `0.2946`

### 60d
- completed_count: `56`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1071`
- primary_path_mean_absolute_error: `0.071966`
- primary_path_median_absolute_error: `0.051247`
- secondary_scenario_hit_rate: `0.2321`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4107`
- close_call_primary_closer_rate: `0.4138`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
