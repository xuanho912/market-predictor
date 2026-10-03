# Forecast Accuracy Scorecard

Generated at: `2026-10-03T01:35:19.824226+00:00`

## Sample Counts

- total_forecasts: `316`
- raw_forecast_rows: `316`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `312`
- completed_3d: `304`
- completed_5d: `296`
- completed_10d: `276`
- completed_20d: `236`
- completed_60d: `76`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `312`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2596`
- primary_path_mean_absolute_error: `0.010141`
- primary_path_median_absolute_error: `0.00826`
- secondary_scenario_hit_rate: `0.3365`
- primary_vs_secondary_accuracy_spread: `-0.0769`
- primary_closer_than_secondary_rate: `0.3718`
- close_call_primary_closer_rate: `0.345`

### 3d
- completed_count: `304`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2566`
- primary_path_mean_absolute_error: `0.016176`
- primary_path_median_absolute_error: `0.012624`
- secondary_scenario_hit_rate: `0.3092`
- primary_vs_secondary_accuracy_spread: `-0.0526`
- primary_closer_than_secondary_rate: `0.3882`
- close_call_primary_closer_rate: `0.4142`

### 5d
- completed_count: `296`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2703`
- primary_path_mean_absolute_error: `0.021853`
- primary_path_median_absolute_error: `0.016576`
- secondary_scenario_hit_rate: `0.2804`
- primary_vs_secondary_accuracy_spread: `-0.0101`
- primary_closer_than_secondary_rate: `0.402`
- close_call_primary_closer_rate: `0.381`

### 10d
- completed_count: `276`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2319`
- primary_path_mean_absolute_error: `0.032966`
- primary_path_median_absolute_error: `0.0276`
- secondary_scenario_hit_rate: `0.3297`
- primary_vs_secondary_accuracy_spread: `-0.0978`
- primary_closer_than_secondary_rate: `0.3225`
- close_call_primary_closer_rate: `0.3355`

### 20d
- completed_count: `236`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1356`
- primary_path_mean_absolute_error: `0.059445`
- primary_path_median_absolute_error: `0.054715`
- secondary_scenario_hit_rate: `0.2754`
- primary_vs_secondary_accuracy_spread: `-0.1398`
- primary_closer_than_secondary_rate: `0.2881`
- close_call_primary_closer_rate: `0.3151`

### 60d
- completed_count: `76`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1184`
- primary_path_mean_absolute_error: `0.070775`
- primary_path_median_absolute_error: `0.050587`
- secondary_scenario_hit_rate: `0.2763`
- primary_vs_secondary_accuracy_spread: `-0.1579`
- primary_closer_than_secondary_rate: `0.3947`
- close_call_primary_closer_rate: `0.4595`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
