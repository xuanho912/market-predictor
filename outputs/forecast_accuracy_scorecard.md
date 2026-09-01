# Forecast Accuracy Scorecard

Generated at: `2026-09-01T16:43:31.348807+00:00`

## Sample Counts

- total_forecasts: `224`
- raw_forecast_rows: `224`
- deduped_legacy_rows: `0`
- pending_forecasts: `224`
- completed_1d: `220`
- completed_3d: `212`
- completed_5d: `204`
- completed_10d: `184`
- completed_20d: `144`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `220`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2955`
- primary_path_mean_absolute_error: `0.009891`
- primary_path_median_absolute_error: `0.007709`
- secondary_scenario_hit_rate: `0.3227`
- primary_vs_secondary_accuracy_spread: `-0.0273`
- primary_closer_than_secondary_rate: `0.4227`
- close_call_primary_closer_rate: `0.3534`

### 3d
- completed_count: `212`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2358`
- primary_path_mean_absolute_error: `0.016094`
- primary_path_median_absolute_error: `0.012757`
- secondary_scenario_hit_rate: `0.3538`
- primary_vs_secondary_accuracy_spread: `-0.1179`
- primary_closer_than_secondary_rate: `0.3868`
- close_call_primary_closer_rate: `0.416`

### 5d
- completed_count: `204`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2255`
- primary_path_mean_absolute_error: `0.023112`
- primary_path_median_absolute_error: `0.018502`
- secondary_scenario_hit_rate: `0.2941`
- primary_vs_secondary_accuracy_spread: `-0.0686`
- primary_closer_than_secondary_rate: `0.3971`
- close_call_primary_closer_rate: `0.3761`

### 10d
- completed_count: `184`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1957`
- primary_path_mean_absolute_error: `0.035076`
- primary_path_median_absolute_error: `0.02869`
- secondary_scenario_hit_rate: `0.3424`
- primary_vs_secondary_accuracy_spread: `-0.1467`
- primary_closer_than_secondary_rate: `0.2935`
- close_call_primary_closer_rate: `0.2549`

### 20d
- completed_count: `144`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1111`
- primary_path_mean_absolute_error: `0.05958`
- primary_path_median_absolute_error: `0.058866`
- secondary_scenario_hit_rate: `0.2778`
- primary_vs_secondary_accuracy_spread: `-0.1667`
- primary_closer_than_secondary_rate: `0.2639`
- close_call_primary_closer_rate: `0.2763`

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
- high_confidence_better: `insufficient_samples_for_high_confidence_validation`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
