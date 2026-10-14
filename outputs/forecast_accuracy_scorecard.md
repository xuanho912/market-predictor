# Forecast Accuracy Scorecard

Generated at: `2026-10-14T06:13:56.044221+00:00`

## Sample Counts

- total_forecasts: `344`
- raw_forecast_rows: `344`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `340`
- completed_3d: `332`
- completed_5d: `324`
- completed_10d: `304`
- completed_20d: `264`
- completed_60d: `104`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `340`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2618`
- primary_path_mean_absolute_error: `0.009968`
- primary_path_median_absolute_error: `0.008075`
- secondary_scenario_hit_rate: `0.3441`
- primary_vs_secondary_accuracy_spread: `-0.0824`
- primary_closer_than_secondary_rate: `0.3676`
- close_call_primary_closer_rate: `0.3441`

### 3d
- completed_count: `332`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.256`
- primary_path_mean_absolute_error: `0.016213`
- primary_path_median_absolute_error: `0.012757`
- secondary_scenario_hit_rate: `0.3072`
- primary_vs_secondary_accuracy_spread: `-0.0512`
- primary_closer_than_secondary_rate: `0.3825`
- close_call_primary_closer_rate: `0.4176`

### 5d
- completed_count: `324`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2593`
- primary_path_mean_absolute_error: `0.022193`
- primary_path_median_absolute_error: `0.01786`
- secondary_scenario_hit_rate: `0.287`
- primary_vs_secondary_accuracy_spread: `-0.0278`
- primary_closer_than_secondary_rate: `0.3858`
- close_call_primary_closer_rate: `0.3864`

### 10d
- completed_count: `304`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2204`
- primary_path_mean_absolute_error: `0.032587`
- primary_path_median_absolute_error: `0.027368`
- secondary_scenario_hit_rate: `0.3421`
- primary_vs_secondary_accuracy_spread: `-0.1217`
- primary_closer_than_secondary_rate: `0.3125`
- close_call_primary_closer_rate: `0.3314`

### 20d
- completed_count: `264`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1326`
- primary_path_mean_absolute_error: `0.058584`
- primary_path_median_absolute_error: `0.054354`
- secondary_scenario_hit_rate: `0.2879`
- primary_vs_secondary_accuracy_spread: `-0.1553`
- primary_closer_than_secondary_rate: `0.2765`
- close_call_primary_closer_rate: `0.3245`

### 60d
- completed_count: `104`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1442`
- primary_path_mean_absolute_error: `0.069138`
- primary_path_median_absolute_error: `0.051247`
- secondary_scenario_hit_rate: `0.2308`
- primary_vs_secondary_accuracy_spread: `-0.0865`
- primary_closer_than_secondary_rate: `0.4327`
- close_call_primary_closer_rate: `0.5185`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
