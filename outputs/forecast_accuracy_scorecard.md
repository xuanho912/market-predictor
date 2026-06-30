# Forecast Accuracy Scorecard

Generated at: `2026-06-30T05:19:52.768944+00:00`

## Sample Counts

- total_forecasts: `48`
- raw_forecast_rows: `48`
- deduped_legacy_rows: `0`
- pending_forecasts: `48`
- completed_1d: `44`
- completed_3d: `36`
- completed_5d: `28`
- completed_10d: `8`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `early_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `44`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.3636`
- primary_path_mean_absolute_error: `0.012019`
- primary_path_median_absolute_error: `0.010246`
- secondary_scenario_hit_rate: `0.2727`
- primary_vs_secondary_accuracy_spread: `0.0909`
- primary_closer_than_secondary_rate: `0.4773`
- close_call_primary_closer_rate: `0.5238`

### 3d
- completed_count: `36`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.012659`
- primary_path_median_absolute_error: `0.011191`
- secondary_scenario_hit_rate: `0.3333`
- primary_vs_secondary_accuracy_spread: `-0.0833`
- primary_closer_than_secondary_rate: `0.3611`
- close_call_primary_closer_rate: `0.6429`

### 5d
- completed_count: `28`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.3929`
- primary_path_mean_absolute_error: `0.016107`
- primary_path_median_absolute_error: `0.008924`
- secondary_scenario_hit_rate: `0.1429`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.5714`
- close_call_primary_closer_rate: `0.8333`

### 10d
- completed_count: `8`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.008941`
- primary_path_median_absolute_error: `0.006645`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.75`
- close_call_primary_closer_rate: `None`

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
- primary_beats_secondary: `primary_path_more_accurate_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
