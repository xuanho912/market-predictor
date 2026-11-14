# Forecast Accuracy Scorecard

Generated at: `2026-11-14T18:05:25.211768+00:00`

## Sample Counts

- total_forecasts: `436`
- raw_forecast_rows: `436`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `432`
- completed_3d: `424`
- completed_5d: `416`
- completed_10d: `396`
- completed_20d: `356`
- completed_60d: `196`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `432`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2662`
- primary_path_mean_absolute_error: `0.010813`
- primary_path_median_absolute_error: `0.008819`
- secondary_scenario_hit_rate: `0.3403`
- primary_vs_secondary_accuracy_spread: `-0.0741`
- primary_closer_than_secondary_rate: `0.3657`
- close_call_primary_closer_rate: `0.3393`

### 3d
- completed_count: `424`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2736`
- primary_path_mean_absolute_error: `0.017147`
- primary_path_median_absolute_error: `0.013157`
- secondary_scenario_hit_rate: `0.3137`
- primary_vs_secondary_accuracy_spread: `-0.0401`
- primary_closer_than_secondary_rate: `0.3915`
- close_call_primary_closer_rate: `0.4364`

### 5d
- completed_count: `416`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2524`
- primary_path_mean_absolute_error: `0.023666`
- primary_path_median_absolute_error: `0.019518`
- secondary_scenario_hit_rate: `0.3053`
- primary_vs_secondary_accuracy_spread: `-0.0529`
- primary_closer_than_secondary_rate: `0.363`
- close_call_primary_closer_rate: `0.3721`

### 10d
- completed_count: `396`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2601`
- primary_path_mean_absolute_error: `0.033022`
- primary_path_median_absolute_error: `0.028313`
- secondary_scenario_hit_rate: `0.3131`
- primary_vs_secondary_accuracy_spread: `-0.053`
- primary_closer_than_secondary_rate: `0.351`
- close_call_primary_closer_rate: `0.3365`

### 20d
- completed_count: `356`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1854`
- primary_path_mean_absolute_error: `0.056881`
- primary_path_median_absolute_error: `0.054137`
- secondary_scenario_hit_rate: `0.2669`
- primary_vs_secondary_accuracy_spread: `-0.0815`
- primary_closer_than_secondary_rate: `0.3483`
- close_call_primary_closer_rate: `0.3915`

### 60d
- completed_count: `196`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1378`
- primary_path_mean_absolute_error: `0.077466`
- primary_path_median_absolute_error: `0.070011`
- secondary_scenario_hit_rate: `0.2347`
- primary_vs_secondary_accuracy_spread: `-0.0969`
- primary_closer_than_secondary_rate: `0.3776`
- close_call_primary_closer_rate: `0.4495`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
