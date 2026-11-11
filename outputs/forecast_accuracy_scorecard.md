# Forecast Accuracy Scorecard

Generated at: `2026-11-11T19:38:57.566944+00:00`

## Sample Counts

- total_forecasts: `424`
- raw_forecast_rows: `424`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `420`
- completed_3d: `412`
- completed_5d: `404`
- completed_10d: `384`
- completed_20d: `344`
- completed_60d: `184`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `420`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2595`
- primary_path_mean_absolute_error: `0.01087`
- primary_path_median_absolute_error: `0.008981`
- secondary_scenario_hit_rate: `0.3452`
- primary_vs_secondary_accuracy_spread: `-0.0857`
- primary_closer_than_secondary_rate: `0.3619`
- close_call_primary_closer_rate: `0.338`

### 3d
- completed_count: `412`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2767`
- primary_path_mean_absolute_error: `0.016944`
- primary_path_median_absolute_error: `0.013076`
- secondary_scenario_hit_rate: `0.3083`
- primary_vs_secondary_accuracy_spread: `-0.0316`
- primary_closer_than_secondary_rate: `0.3908`
- close_call_primary_closer_rate: `0.4326`

### 5d
- completed_count: `404`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2599`
- primary_path_mean_absolute_error: `0.023208`
- primary_path_median_absolute_error: `0.01928`
- secondary_scenario_hit_rate: `0.297`
- primary_vs_secondary_accuracy_spread: `-0.0371`
- primary_closer_than_secondary_rate: `0.3713`
- close_call_primary_closer_rate: `0.3774`

### 10d
- completed_count: `384`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2604`
- primary_path_mean_absolute_error: `0.032712`
- primary_path_median_absolute_error: `0.027754`
- secondary_scenario_hit_rate: `0.3177`
- primary_vs_secondary_accuracy_spread: `-0.0573`
- primary_closer_than_secondary_rate: `0.3464`
- close_call_primary_closer_rate: `0.335`

### 20d
- completed_count: `344`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1773`
- primary_path_mean_absolute_error: `0.057468`
- primary_path_median_absolute_error: `0.054296`
- secondary_scenario_hit_rate: `0.2703`
- primary_vs_secondary_accuracy_spread: `-0.093`
- primary_closer_than_secondary_rate: `0.3401`
- close_call_primary_closer_rate: `0.3936`

### 60d
- completed_count: `184`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1196`
- primary_path_mean_absolute_error: `0.078612`
- primary_path_median_absolute_error: `0.072083`
- secondary_scenario_hit_rate: `0.2446`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3641`
- close_call_primary_closer_rate: `0.4412`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
