# Forecast Accuracy Scorecard

Generated at: `2026-11-24T05:30:57.658497+00:00`

## Sample Counts

- total_forecasts: `460`
- raw_forecast_rows: `460`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `456`
- completed_3d: `448`
- completed_5d: `440`
- completed_10d: `420`
- completed_20d: `380`
- completed_60d: `220`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `456`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2763`
- primary_path_mean_absolute_error: `0.01144`
- primary_path_median_absolute_error: `0.009117`
- secondary_scenario_hit_rate: `0.3311`
- primary_vs_secondary_accuracy_spread: `-0.0548`
- primary_closer_than_secondary_rate: `0.3772`
- close_call_primary_closer_rate: `0.3493`

### 3d
- completed_count: `448`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2835`
- primary_path_mean_absolute_error: `0.018132`
- primary_path_median_absolute_error: `0.013474`
- secondary_scenario_hit_rate: `0.308`
- primary_vs_secondary_accuracy_spread: `-0.0246`
- primary_closer_than_secondary_rate: `0.3996`
- close_call_primary_closer_rate: `0.4323`

### 5d
- completed_count: `440`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2659`
- primary_path_mean_absolute_error: `0.025209`
- primary_path_median_absolute_error: `0.020189`
- secondary_scenario_hit_rate: `0.3023`
- primary_vs_secondary_accuracy_spread: `-0.0364`
- primary_closer_than_secondary_rate: `0.3727`
- close_call_primary_closer_rate: `0.3799`

### 10d
- completed_count: `420`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2857`
- primary_path_mean_absolute_error: `0.033254`
- primary_path_median_absolute_error: `0.028189`
- secondary_scenario_hit_rate: `0.3071`
- primary_vs_secondary_accuracy_spread: `-0.0214`
- primary_closer_than_secondary_rate: `0.3738`
- close_call_primary_closer_rate: `0.3426`

### 20d
- completed_count: `380`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2237`
- primary_path_mean_absolute_error: `0.056167`
- primary_path_median_absolute_error: `0.053786`
- secondary_scenario_hit_rate: `0.2632`
- primary_vs_secondary_accuracy_spread: `-0.0395`
- primary_closer_than_secondary_rate: `0.3763`
- close_call_primary_closer_rate: `0.4061`

### 60d
- completed_count: `220`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1682`
- primary_path_mean_absolute_error: `0.08213`
- primary_path_median_absolute_error: `0.073168`
- secondary_scenario_hit_rate: `0.2364`
- primary_vs_secondary_accuracy_spread: `-0.0682`
- primary_closer_than_secondary_rate: `0.3818`
- close_call_primary_closer_rate: `0.4436`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_not_better_than_no_edge_keep_confidence_capped`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
