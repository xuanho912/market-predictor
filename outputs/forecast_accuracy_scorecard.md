# Forecast Accuracy Scorecard

Generated at: `2026-11-19T08:52:51.071309+00:00`

## Sample Counts

- total_forecasts: `448`
- raw_forecast_rows: `448`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `444`
- completed_3d: `436`
- completed_5d: `428`
- completed_10d: `408`
- completed_20d: `368`
- completed_60d: `208`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `444`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2658`
- primary_path_mean_absolute_error: `0.010826`
- primary_path_median_absolute_error: `0.008926`
- secondary_scenario_hit_rate: `0.3401`
- primary_vs_secondary_accuracy_spread: `-0.0743`
- primary_closer_than_secondary_rate: `0.3694`
- close_call_primary_closer_rate: `0.3493`

### 3d
- completed_count: `436`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2706`
- primary_path_mean_absolute_error: `0.017948`
- primary_path_median_absolute_error: `0.013417`
- secondary_scenario_hit_rate: `0.3165`
- primary_vs_secondary_accuracy_spread: `-0.0459`
- primary_closer_than_secondary_rate: `0.3853`
- close_call_primary_closer_rate: `0.4248`

### 5d
- completed_count: `428`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2593`
- primary_path_mean_absolute_error: `0.024117`
- primary_path_median_absolute_error: `0.019866`
- secondary_scenario_hit_rate: `0.3037`
- primary_vs_secondary_accuracy_spread: `-0.0444`
- primary_closer_than_secondary_rate: `0.3692`
- close_call_primary_closer_rate: `0.3722`

### 10d
- completed_count: `408`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2696`
- primary_path_mean_absolute_error: `0.033197`
- primary_path_median_absolute_error: `0.028189`
- secondary_scenario_hit_rate: `0.3137`
- primary_vs_secondary_accuracy_spread: `-0.0441`
- primary_closer_than_secondary_rate: `0.3603`
- close_call_primary_closer_rate: `0.3442`

### 20d
- completed_count: `368`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2038`
- primary_path_mean_absolute_error: `0.056018`
- primary_path_median_absolute_error: `0.053786`
- secondary_scenario_hit_rate: `0.2663`
- primary_vs_secondary_accuracy_spread: `-0.0625`
- primary_closer_than_secondary_rate: `0.3614`
- close_call_primary_closer_rate: `0.401`

### 60d
- completed_count: `208`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1538`
- primary_path_mean_absolute_error: `0.078795`
- primary_path_median_absolute_error: `0.070618`
- secondary_scenario_hit_rate: `0.2356`
- primary_vs_secondary_accuracy_spread: `-0.0817`
- primary_closer_than_secondary_rate: `0.3798`
- close_call_primary_closer_rate: `0.4463`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_not_better_than_no_edge_keep_confidence_capped`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
