# Forecast Accuracy Scorecard

Generated at: `2026-09-05T00:55:41.295768+00:00`

## Sample Counts

- total_forecasts: `240`
- raw_forecast_rows: `240`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `236`
- completed_3d: `228`
- completed_5d: `220`
- completed_10d: `200`
- completed_20d: `160`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `236`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2881`
- primary_path_mean_absolute_error: `0.009933`
- primary_path_median_absolute_error: `0.007709`
- secondary_scenario_hit_rate: `0.339`
- primary_vs_secondary_accuracy_spread: `-0.0508`
- primary_closer_than_secondary_rate: `0.4068`
- close_call_primary_closer_rate: `0.3356`

### 3d
- completed_count: `228`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2325`
- primary_path_mean_absolute_error: `0.016377`
- primary_path_median_absolute_error: `0.01278`
- secondary_scenario_hit_rate: `0.3553`
- primary_vs_secondary_accuracy_spread: `-0.1228`
- primary_closer_than_secondary_rate: `0.3772`
- close_call_primary_closer_rate: `0.3972`

### 5d
- completed_count: `220`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2273`
- primary_path_mean_absolute_error: `0.022578`
- primary_path_median_absolute_error: `0.0176`
- secondary_scenario_hit_rate: `0.3091`
- primary_vs_secondary_accuracy_spread: `-0.0818`
- primary_closer_than_secondary_rate: `0.3864`
- close_call_primary_closer_rate: `0.3609`

### 10d
- completed_count: `200`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.205`
- primary_path_mean_absolute_error: `0.034613`
- primary_path_median_absolute_error: `0.028296`
- secondary_scenario_hit_rate: `0.345`
- primary_vs_secondary_accuracy_spread: `-0.14`
- primary_closer_than_secondary_rate: `0.305`
- close_call_primary_closer_rate: `0.2832`

### 20d
- completed_count: `160`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1125`
- primary_path_mean_absolute_error: `0.059144`
- primary_path_median_absolute_error: `0.058866`
- secondary_scenario_hit_rate: `0.2812`
- primary_vs_secondary_accuracy_spread: `-0.1688`
- primary_closer_than_secondary_rate: `0.2562`
- close_call_primary_closer_rate: `0.2667`

### 60d
- completed_count: `0`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `None`
- primary_path_mean_absolute_error: `None`
- primary_path_median_absolute_error: `None`
- secondary_scenario_hit_rate: `None`
- primary_vs_secondary_accuracy_spread: `None`
- primary_closer_than_secondary_rate: `None`
- close_call_primary_closer_rate: `None`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
