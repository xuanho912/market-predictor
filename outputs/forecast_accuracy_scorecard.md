# Forecast Accuracy Scorecard

Generated at: `2026-11-25T03:38:11.841110+00:00`

## Sample Counts

- total_forecasts: `464`
- raw_forecast_rows: `464`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `460`
- completed_3d: `452`
- completed_5d: `444`
- completed_10d: `424`
- completed_20d: `384`
- completed_60d: `224`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `460`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2783`
- primary_path_mean_absolute_error: `0.011437`
- primary_path_median_absolute_error: `0.00912`
- secondary_scenario_hit_rate: `0.3304`
- primary_vs_secondary_accuracy_spread: `-0.0522`
- primary_closer_than_secondary_rate: `0.3783`
- close_call_primary_closer_rate: `0.3493`

### 3d
- completed_count: `452`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.281`
- primary_path_mean_absolute_error: `0.018193`
- primary_path_median_absolute_error: `0.013643`
- secondary_scenario_hit_rate: `0.3119`
- primary_vs_secondary_accuracy_spread: `-0.031`
- primary_closer_than_secondary_rate: `0.396`
- close_call_primary_closer_rate: `0.4323`

### 5d
- completed_count: `444`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2725`
- primary_path_mean_absolute_error: `0.025088`
- primary_path_median_absolute_error: `0.020033`
- secondary_scenario_hit_rate: `0.2995`
- primary_vs_secondary_accuracy_spread: `-0.027`
- primary_closer_than_secondary_rate: `0.3784`
- close_call_primary_closer_rate: `0.3799`

### 10d
- completed_count: `424`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2877`
- primary_path_mean_absolute_error: `0.03342`
- primary_path_median_absolute_error: `0.028189`
- secondary_scenario_hit_rate: `0.309`
- primary_vs_secondary_accuracy_spread: `-0.0212`
- primary_closer_than_secondary_rate: `0.375`
- close_call_primary_closer_rate: `0.3455`

### 20d
- completed_count: `384`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.224`
- primary_path_mean_absolute_error: `0.056668`
- primary_path_median_absolute_error: `0.054029`
- secondary_scenario_hit_rate: `0.263`
- primary_vs_secondary_accuracy_spread: `-0.0391`
- primary_closer_than_secondary_rate: `0.375`
- close_call_primary_closer_rate: `0.4`

### 60d
- completed_count: `224`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1696`
- primary_path_mean_absolute_error: `0.083261`
- primary_path_median_absolute_error: `0.073612`
- secondary_scenario_hit_rate: `0.2411`
- primary_vs_secondary_accuracy_spread: `-0.0714`
- primary_closer_than_secondary_rate: `0.3795`
- close_call_primary_closer_rate: `0.438`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_not_better_than_no_edge_keep_confidence_capped`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
