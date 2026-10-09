# Forecast Accuracy Scorecard

Generated at: `2026-10-09T02:57:29.589321+00:00`

## Sample Counts

- total_forecasts: `332`
- raw_forecast_rows: `332`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `328`
- completed_3d: `320`
- completed_5d: `312`
- completed_10d: `292`
- completed_20d: `252`
- completed_60d: `92`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `328`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2622`
- primary_path_mean_absolute_error: `0.010017`
- primary_path_median_absolute_error: `0.008075`
- secondary_scenario_hit_rate: `0.3384`
- primary_vs_secondary_accuracy_spread: `-0.0762`
- primary_closer_than_secondary_rate: `0.3689`
- close_call_primary_closer_rate: `0.3408`

### 3d
- completed_count: `320`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2562`
- primary_path_mean_absolute_error: `0.016364`
- primary_path_median_absolute_error: `0.012624`
- secondary_scenario_hit_rate: `0.2969`
- primary_vs_secondary_accuracy_spread: `-0.0406`
- primary_closer_than_secondary_rate: `0.3875`
- close_call_primary_closer_rate: `0.422`

### 5d
- completed_count: `312`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2692`
- primary_path_mean_absolute_error: `0.021978`
- primary_path_median_absolute_error: `0.0176`
- secondary_scenario_hit_rate: `0.2756`
- primary_vs_secondary_accuracy_spread: `-0.0064`
- primary_closer_than_secondary_rate: `0.3974`
- close_call_primary_closer_rate: `0.3918`

### 10d
- completed_count: `292`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.226`
- primary_path_mean_absolute_error: `0.032777`
- primary_path_median_absolute_error: `0.0276`
- secondary_scenario_hit_rate: `0.3322`
- primary_vs_secondary_accuracy_spread: `-0.1062`
- primary_closer_than_secondary_rate: `0.3185`
- close_call_primary_closer_rate: `0.3373`

### 20d
- completed_count: `252`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1389`
- primary_path_mean_absolute_error: `0.058645`
- primary_path_median_absolute_error: `0.054354`
- secondary_scenario_hit_rate: `0.2698`
- primary_vs_secondary_accuracy_spread: `-0.131`
- primary_closer_than_secondary_rate: `0.2897`
- close_call_primary_closer_rate: `0.3267`

### 60d
- completed_count: `92`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1304`
- primary_path_mean_absolute_error: `0.069634`
- primary_path_median_absolute_error: `0.051195`
- secondary_scenario_hit_rate: `0.2609`
- primary_vs_secondary_accuracy_spread: `-0.1304`
- primary_closer_than_secondary_rate: `0.4022`
- close_call_primary_closer_rate: `0.5`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
