# Forecast Accuracy Scorecard

Generated at: `2026-11-07T07:15:56.364352+00:00`

## Sample Counts

- total_forecasts: `416`
- raw_forecast_rows: `416`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `412`
- completed_3d: `404`
- completed_5d: `396`
- completed_10d: `376`
- completed_20d: `336`
- completed_60d: `176`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `412`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2597`
- primary_path_mean_absolute_error: `0.010705`
- primary_path_median_absolute_error: `0.008819`
- secondary_scenario_hit_rate: `0.3422`
- primary_vs_secondary_accuracy_spread: `-0.0825`
- primary_closer_than_secondary_rate: `0.3617`
- close_call_primary_closer_rate: `0.3395`

### 3d
- completed_count: `404`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2797`
- primary_path_mean_absolute_error: `0.016599`
- primary_path_median_absolute_error: `0.013013`
- secondary_scenario_hit_rate: `0.2995`
- primary_vs_secondary_accuracy_spread: `-0.0198`
- primary_closer_than_secondary_rate: `0.396`
- close_call_primary_closer_rate: `0.4387`

### 5d
- completed_count: `396`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2601`
- primary_path_mean_absolute_error: `0.023217`
- primary_path_median_absolute_error: `0.019316`
- secondary_scenario_hit_rate: `0.3005`
- primary_vs_secondary_accuracy_spread: `-0.0404`
- primary_closer_than_secondary_rate: `0.3687`
- close_call_primary_closer_rate: `0.3702`

### 10d
- completed_count: `376`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.258`
- primary_path_mean_absolute_error: `0.032631`
- primary_path_median_absolute_error: `0.027676`
- secondary_scenario_hit_rate: `0.3191`
- primary_vs_secondary_accuracy_spread: `-0.0612`
- primary_closer_than_secondary_rate: `0.3457`
- close_call_primary_closer_rate: `0.3418`

### 20d
- completed_count: `336`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1696`
- primary_path_mean_absolute_error: `0.057482`
- primary_path_median_absolute_error: `0.054296`
- secondary_scenario_hit_rate: `0.2708`
- primary_vs_secondary_accuracy_spread: `-0.1012`
- primary_closer_than_secondary_rate: `0.3363`
- close_call_primary_closer_rate: `0.3913`

### 60d
- completed_count: `176`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.075821`
- primary_path_median_absolute_error: `0.070618`
- secondary_scenario_hit_rate: `0.2557`
- primary_vs_secondary_accuracy_spread: `-0.1307`
- primary_closer_than_secondary_rate: `0.3807`
- close_call_primary_closer_rate: `0.4592`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
