# Forecast Accuracy Scorecard

Generated at: `2026-07-14T04:21:47.180589+00:00`

## Sample Counts

- total_forecasts: `84`
- raw_forecast_rows: `84`
- deduped_legacy_rows: `0`
- pending_forecasts: `84`
- completed_1d: `80`
- completed_3d: `72`
- completed_5d: `64`
- completed_10d: `44`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `80`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.4`
- primary_path_mean_absolute_error: `0.009965`
- primary_path_median_absolute_error: `0.00682`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.55`
- close_call_primary_closer_rate: `0.5641`

### 3d
- completed_count: `72`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2778`
- primary_path_mean_absolute_error: `0.012781`
- primary_path_median_absolute_error: `0.011536`
- secondary_scenario_hit_rate: `0.3611`
- primary_vs_secondary_accuracy_spread: `-0.0833`
- primary_closer_than_secondary_rate: `0.375`
- close_call_primary_closer_rate: `0.4857`

### 5d
- completed_count: `64`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3438`
- primary_path_mean_absolute_error: `0.017604`
- primary_path_median_absolute_error: `0.009586`
- secondary_scenario_hit_rate: `0.2969`
- primary_vs_secondary_accuracy_spread: `0.0469`
- primary_closer_than_secondary_rate: `0.4844`
- close_call_primary_closer_rate: `0.5`

### 10d
- completed_count: `44`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.2273`
- primary_path_mean_absolute_error: `0.023256`
- primary_path_median_absolute_error: `0.020747`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.0227`
- primary_closer_than_secondary_rate: `0.4091`
- close_call_primary_closer_rate: `0.3333`

### 20d
- completed_count: `0`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `None`
- primary_path_mean_absolute_error: `None`
- primary_path_median_absolute_error: `None`
- secondary_scenario_hit_rate: `None`
- primary_vs_secondary_accuracy_spread: `None`
- primary_closer_than_secondary_rate: `None`
- close_call_primary_closer_rate: `None`

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

- edge_vs_no_edge: `insufficient_samples_for_edge_validation`
- high_confidence_better: `insufficient_samples_for_high_confidence_validation`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
