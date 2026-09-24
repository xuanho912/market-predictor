# Forecast Accuracy Scorecard

Generated at: `2026-09-24T06:14:47.686233+00:00`

## Sample Counts

- total_forecasts: `288`
- raw_forecast_rows: `288`
- deduped_legacy_rows: `0`
- pending_forecasts: `241`
- completed_1d: `282`
- completed_3d: `275`
- completed_5d: `267`
- completed_10d: `247`
- completed_20d: `207`
- completed_60d: `47`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `282`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.273`
- primary_path_mean_absolute_error: `0.010095`
- primary_path_median_absolute_error: `0.007936`
- secondary_scenario_hit_rate: `0.3369`
- primary_vs_secondary_accuracy_spread: `-0.0638`
- primary_closer_than_secondary_rate: `0.3936`
- close_call_primary_closer_rate: `0.3522`

### 3d
- completed_count: `275`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2582`
- primary_path_mean_absolute_error: `0.016421`
- primary_path_median_absolute_error: `0.012774`
- secondary_scenario_hit_rate: `0.3236`
- primary_vs_secondary_accuracy_spread: `-0.0655`
- primary_closer_than_secondary_rate: `0.3891`
- close_call_primary_closer_rate: `0.4286`

### 5d
- completed_count: `267`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2846`
- primary_path_mean_absolute_error: `0.021872`
- primary_path_median_absolute_error: `0.016043`
- secondary_scenario_hit_rate: `0.2734`
- primary_vs_secondary_accuracy_spread: `0.0112`
- primary_closer_than_secondary_rate: `0.4195`
- close_call_primary_closer_rate: `0.3974`

### 10d
- completed_count: `247`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2429`
- primary_path_mean_absolute_error: `0.033106`
- primary_path_median_absolute_error: `0.027589`
- secondary_scenario_hit_rate: `0.3279`
- primary_vs_secondary_accuracy_spread: `-0.085`
- primary_closer_than_secondary_rate: `0.3401`
- close_call_primary_closer_rate: `0.3333`

### 20d
- completed_count: `207`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1159`
- primary_path_mean_absolute_error: `0.061281`
- primary_path_median_absolute_error: `0.058694`
- secondary_scenario_hit_rate: `0.2947`
- primary_vs_secondary_accuracy_spread: `-0.1787`
- primary_closer_than_secondary_rate: `0.256`
- close_call_primary_closer_rate: `0.2833`

### 60d
- completed_count: `47`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.1064`
- primary_path_mean_absolute_error: `0.070056`
- primary_path_median_absolute_error: `0.051247`
- secondary_scenario_hit_rate: `0.1915`
- primary_vs_secondary_accuracy_spread: `-0.0851`
- primary_closer_than_secondary_rate: `0.383`
- close_call_primary_closer_rate: `0.3913`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
