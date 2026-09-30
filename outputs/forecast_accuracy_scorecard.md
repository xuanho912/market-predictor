# Forecast Accuracy Scorecard

Generated at: `2026-09-30T01:41:37.733708+00:00`

## Sample Counts

- total_forecasts: `304`
- raw_forecast_rows: `304`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `300`
- completed_3d: `292`
- completed_5d: `284`
- completed_10d: `264`
- completed_20d: `224`
- completed_60d: `64`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `300`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2667`
- primary_path_mean_absolute_error: `0.010064`
- primary_path_median_absolute_error: `0.008075`
- secondary_scenario_hit_rate: `0.34`
- primary_vs_secondary_accuracy_spread: `-0.0733`
- primary_closer_than_secondary_rate: `0.3833`
- close_call_primary_closer_rate: `0.3491`

### 3d
- completed_count: `292`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2568`
- primary_path_mean_absolute_error: `0.016197`
- primary_path_median_absolute_error: `0.012624`
- secondary_scenario_hit_rate: `0.3185`
- primary_vs_secondary_accuracy_spread: `-0.0616`
- primary_closer_than_secondary_rate: `0.387`
- close_call_primary_closer_rate: `0.4217`

### 5d
- completed_count: `284`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2746`
- primary_path_mean_absolute_error: `0.021812`
- primary_path_median_absolute_error: `0.016339`
- secondary_scenario_hit_rate: `0.2817`
- primary_vs_secondary_accuracy_spread: `-0.007`
- primary_closer_than_secondary_rate: `0.4049`
- close_call_primary_closer_rate: `0.3851`

### 10d
- completed_count: `264`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2348`
- primary_path_mean_absolute_error: `0.032908`
- primary_path_median_absolute_error: `0.027019`
- secondary_scenario_hit_rate: `0.3295`
- primary_vs_secondary_accuracy_spread: `-0.0947`
- primary_closer_than_secondary_rate: `0.3295`
- close_call_primary_closer_rate: `0.3311`

### 20d
- completed_count: `224`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1205`
- primary_path_mean_absolute_error: `0.06086`
- primary_path_median_absolute_error: `0.057896`
- secondary_scenario_hit_rate: `0.2902`
- primary_vs_secondary_accuracy_spread: `-0.1696`
- primary_closer_than_secondary_rate: `0.2634`
- close_call_primary_closer_rate: `0.292`

### 60d
- completed_count: `64`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.0938`
- primary_path_mean_absolute_error: `0.072652`
- primary_path_median_absolute_error: `0.051247`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.1562`
- primary_closer_than_secondary_rate: `0.4219`
- close_call_primary_closer_rate: `0.4375`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
