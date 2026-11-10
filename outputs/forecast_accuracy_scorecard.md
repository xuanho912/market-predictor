# Forecast Accuracy Scorecard

Generated at: `2026-11-10T11:48:15.553461+00:00`

## Sample Counts

- total_forecasts: `420`
- raw_forecast_rows: `420`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `416`
- completed_3d: `408`
- completed_5d: `400`
- completed_10d: `380`
- completed_20d: `340`
- completed_60d: `180`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `416`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2596`
- primary_path_mean_absolute_error: `0.010913`
- primary_path_median_absolute_error: `0.009112`
- secondary_scenario_hit_rate: `0.3438`
- primary_vs_secondary_accuracy_spread: `-0.0841`
- primary_closer_than_secondary_rate: `0.3606`
- close_call_primary_closer_rate: `0.3395`

### 3d
- completed_count: `408`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2794`
- primary_path_mean_absolute_error: `0.016655`
- primary_path_median_absolute_error: `0.013013`
- secondary_scenario_hit_rate: `0.3015`
- primary_vs_secondary_accuracy_spread: `-0.0221`
- primary_closer_than_secondary_rate: `0.3946`
- close_call_primary_closer_rate: `0.4326`

### 5d
- completed_count: `400`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2575`
- primary_path_mean_absolute_error: `0.023281`
- primary_path_median_absolute_error: `0.019316`
- secondary_scenario_hit_rate: `0.3`
- primary_vs_secondary_accuracy_spread: `-0.0425`
- primary_closer_than_secondary_rate: `0.37`
- close_call_primary_closer_rate: `0.3762`

### 10d
- completed_count: `380`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2605`
- primary_path_mean_absolute_error: `0.032537`
- primary_path_median_absolute_error: `0.027676`
- secondary_scenario_hit_rate: `0.3184`
- primary_vs_secondary_accuracy_spread: `-0.0579`
- primary_closer_than_secondary_rate: `0.3474`
- close_call_primary_closer_rate: `0.3401`

### 20d
- completed_count: `340`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1735`
- primary_path_mean_absolute_error: `0.057515`
- primary_path_median_absolute_error: `0.054296`
- secondary_scenario_hit_rate: `0.2706`
- primary_vs_secondary_accuracy_spread: `-0.0971`
- primary_closer_than_secondary_rate: `0.3382`
- close_call_primary_closer_rate: `0.3925`

### 60d
- completed_count: `180`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1222`
- primary_path_mean_absolute_error: `0.077225`
- primary_path_median_absolute_error: `0.071055`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.1278`
- primary_closer_than_secondary_rate: `0.3722`
- close_call_primary_closer_rate: `0.45`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
