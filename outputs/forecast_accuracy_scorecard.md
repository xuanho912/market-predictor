# Forecast Accuracy Scorecard

Generated at: `2026-08-11T23:27:53.753420+00:00`

## Sample Counts

- total_forecasts: `168`
- raw_forecast_rows: `168`
- deduped_legacy_rows: `0`
- pending_forecasts: `168`
- completed_1d: `164`
- completed_3d: `156`
- completed_5d: `148`
- completed_10d: `128`
- completed_20d: `88`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `164`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3537`
- primary_path_mean_absolute_error: `0.010227`
- primary_path_median_absolute_error: `0.007936`
- secondary_scenario_hit_rate: `0.2988`
- primary_vs_secondary_accuracy_spread: `0.0549`
- primary_closer_than_secondary_rate: `0.5`
- close_call_primary_closer_rate: `0.4409`

### 3d
- completed_count: `156`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2564`
- primary_path_mean_absolute_error: `0.01631`
- primary_path_median_absolute_error: `0.012788`
- secondary_scenario_hit_rate: `0.3462`
- primary_vs_secondary_accuracy_spread: `-0.0897`
- primary_closer_than_secondary_rate: `0.4038`
- close_call_primary_closer_rate: `0.4483`

### 5d
- completed_count: `148`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2568`
- primary_path_mean_absolute_error: `0.023541`
- primary_path_median_absolute_error: `0.017107`
- secondary_scenario_hit_rate: `0.3041`
- primary_vs_secondary_accuracy_spread: `-0.0473`
- primary_closer_than_secondary_rate: `0.4189`
- close_call_primary_closer_rate: `0.375`

### 10d
- completed_count: `128`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2031`
- primary_path_mean_absolute_error: `0.032345`
- primary_path_median_absolute_error: `0.027628`
- secondary_scenario_hit_rate: `0.375`
- primary_vs_secondary_accuracy_spread: `-0.1719`
- primary_closer_than_secondary_rate: `0.3047`
- close_call_primary_closer_rate: `0.2`

### 20d
- completed_count: `88`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1591`
- primary_path_mean_absolute_error: `0.050102`
- primary_path_median_absolute_error: `0.041429`
- secondary_scenario_hit_rate: `0.2727`
- primary_vs_secondary_accuracy_spread: `-0.1136`
- primary_closer_than_secondary_rate: `0.3409`
- close_call_primary_closer_rate: `0.3111`

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
