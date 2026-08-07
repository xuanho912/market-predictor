# Forecast Accuracy Scorecard

Generated at: `2026-08-07T01:40:35.812491+00:00`

## Sample Counts

- total_forecasts: `156`
- raw_forecast_rows: `156`
- deduped_legacy_rows: `0`
- pending_forecasts: `156`
- completed_1d: `152`
- completed_3d: `144`
- completed_5d: `136`
- completed_10d: `116`
- completed_20d: `76`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `152`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3421`
- primary_path_mean_absolute_error: `0.010598`
- primary_path_median_absolute_error: `0.00826`
- secondary_scenario_hit_rate: `0.2961`
- primary_vs_secondary_accuracy_spread: `0.0461`
- primary_closer_than_secondary_rate: `0.5`
- close_call_primary_closer_rate: `0.4524`

### 3d
- completed_count: `144`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2639`
- primary_path_mean_absolute_error: `0.01703`
- primary_path_median_absolute_error: `0.01324`
- secondary_scenario_hit_rate: `0.3472`
- primary_vs_secondary_accuracy_spread: `-0.0833`
- primary_closer_than_secondary_rate: `0.3889`
- close_call_primary_closer_rate: `0.4342`

### 5d
- completed_count: `136`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2647`
- primary_path_mean_absolute_error: `0.022664`
- primary_path_median_absolute_error: `0.015487`
- secondary_scenario_hit_rate: `0.2941`
- primary_vs_secondary_accuracy_spread: `-0.0294`
- primary_closer_than_secondary_rate: `0.4265`
- close_call_primary_closer_rate: `0.3857`

### 10d
- completed_count: `116`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2241`
- primary_path_mean_absolute_error: `0.028838`
- primary_path_median_absolute_error: `0.024625`
- secondary_scenario_hit_rate: `0.3534`
- primary_vs_secondary_accuracy_spread: `-0.1293`
- primary_closer_than_secondary_rate: `0.3362`
- close_call_primary_closer_rate: `0.2241`

### 20d
- completed_count: `76`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1579`
- primary_path_mean_absolute_error: `0.050177`
- primary_path_median_absolute_error: `0.041429`
- secondary_scenario_hit_rate: `0.2895`
- primary_vs_secondary_accuracy_spread: `-0.1316`
- primary_closer_than_secondary_rate: `0.3289`
- close_call_primary_closer_rate: `0.2973`

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
