# Forecast Accuracy Scorecard

Generated at: `2026-09-16T06:07:26.063578+00:00`

## Sample Counts

- total_forecasts: `264`
- raw_forecast_rows: `264`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `260`
- completed_3d: `252`
- completed_5d: `244`
- completed_10d: `224`
- completed_20d: `184`
- completed_60d: `24`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `260`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2846`
- primary_path_mean_absolute_error: `0.009776`
- primary_path_median_absolute_error: `0.007623`
- secondary_scenario_hit_rate: `0.3346`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4077`
- close_call_primary_closer_rate: `0.351`

### 3d
- completed_count: `252`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2579`
- primary_path_mean_absolute_error: `0.015722`
- primary_path_median_absolute_error: `0.012091`
- secondary_scenario_hit_rate: `0.3373`
- primary_vs_secondary_accuracy_spread: `-0.0794`
- primary_closer_than_secondary_rate: `0.3929`
- close_call_primary_closer_rate: `0.42`

### 5d
- completed_count: `244`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2787`
- primary_path_mean_absolute_error: `0.021333`
- primary_path_median_absolute_error: `0.014961`
- secondary_scenario_hit_rate: `0.2869`
- primary_vs_secondary_accuracy_spread: `-0.0082`
- primary_closer_than_secondary_rate: `0.4262`
- close_call_primary_closer_rate: `0.3919`

### 10d
- completed_count: `224`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2098`
- primary_path_mean_absolute_error: `0.034515`
- primary_path_median_absolute_error: `0.028296`
- secondary_scenario_hit_rate: `0.3482`
- primary_vs_secondary_accuracy_spread: `-0.1384`
- primary_closer_than_secondary_rate: `0.317`
- close_call_primary_closer_rate: `0.3066`

### 20d
- completed_count: `184`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.0978`
- primary_path_mean_absolute_error: `0.062189`
- primary_path_median_absolute_error: `0.061807`
- secondary_scenario_hit_rate: `0.3043`
- primary_vs_secondary_accuracy_spread: `-0.2065`
- primary_closer_than_secondary_rate: `0.2283`
- close_call_primary_closer_rate: `0.2451`

### 60d
- completed_count: `24`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.059758`
- primary_path_median_absolute_error: `0.050587`
- secondary_scenario_hit_rate: `0.1667`
- primary_vs_secondary_accuracy_spread: `-0.0417`
- primary_closer_than_secondary_rate: `0.4583`
- close_call_primary_closer_rate: `0.8`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
