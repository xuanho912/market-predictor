# Forecast Accuracy Scorecard

Generated at: `2026-10-22T23:30:31.094274+00:00`

## Sample Counts

- total_forecasts: `372`
- raw_forecast_rows: `372`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `368`
- completed_3d: `360`
- completed_5d: `352`
- completed_10d: `332`
- completed_20d: `292`
- completed_60d: `132`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `368`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2554`
- primary_path_mean_absolute_error: `0.010163`
- primary_path_median_absolute_error: `0.008377`
- secondary_scenario_hit_rate: `0.3342`
- primary_vs_secondary_accuracy_spread: `-0.0788`
- primary_closer_than_secondary_rate: `0.3587`
- close_call_primary_closer_rate: `0.3438`

### 3d
- completed_count: `360`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2472`
- primary_path_mean_absolute_error: `0.016636`
- primary_path_median_absolute_error: `0.013076`
- secondary_scenario_hit_rate: `0.3`
- primary_vs_secondary_accuracy_spread: `-0.0528`
- primary_closer_than_secondary_rate: `0.3722`
- close_call_primary_closer_rate: `0.4233`

### 5d
- completed_count: `352`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2642`
- primary_path_mean_absolute_error: `0.022456`
- primary_path_median_absolute_error: `0.018756`
- secondary_scenario_hit_rate: `0.2926`
- primary_vs_secondary_accuracy_spread: `-0.0284`
- primary_closer_than_secondary_rate: `0.3807`
- close_call_primary_closer_rate: `0.3862`

### 10d
- completed_count: `332`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.241`
- primary_path_mean_absolute_error: `0.032785`
- primary_path_median_absolute_error: `0.027676`
- secondary_scenario_hit_rate: `0.3313`
- primary_vs_secondary_accuracy_spread: `-0.0904`
- primary_closer_than_secondary_rate: `0.3313`
- close_call_primary_closer_rate: `0.3462`

### 20d
- completed_count: `292`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1438`
- primary_path_mean_absolute_error: `0.057214`
- primary_path_median_absolute_error: `0.053984`
- secondary_scenario_hit_rate: `0.2774`
- primary_vs_secondary_accuracy_spread: `-0.1336`
- primary_closer_than_secondary_rate: `0.3116`
- close_call_primary_closer_rate: `0.3614`

### 60d
- completed_count: `132`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1288`
- primary_path_mean_absolute_error: `0.071301`
- primary_path_median_absolute_error: `0.063218`
- secondary_scenario_hit_rate: `0.2121`
- primary_vs_secondary_accuracy_spread: `-0.0833`
- primary_closer_than_secondary_rate: `0.4242`
- close_call_primary_closer_rate: `0.5303`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
