# Forecast Accuracy Scorecard

Generated at: `2026-07-01T23:55:40.915554+00:00`

## Sample Counts

- total_forecasts: `56`
- raw_forecast_rows: `56`
- deduped_legacy_rows: `0`
- pending_forecasts: `56`
- completed_1d: `52`
- completed_3d: `44`
- completed_5d: `36`
- completed_10d: `16`
- completed_20d: `0`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `52`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3462`
- primary_path_mean_absolute_error: `0.011332`
- primary_path_median_absolute_error: `0.008994`
- secondary_scenario_hit_rate: `0.2885`
- primary_vs_secondary_accuracy_spread: `0.0577`
- primary_closer_than_secondary_rate: `0.4808`
- close_call_primary_closer_rate: `0.5`

### 3d
- completed_count: `44`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.012742`
- primary_path_median_absolute_error: `0.011191`
- secondary_scenario_hit_rate: `0.3636`
- primary_vs_secondary_accuracy_spread: `-0.1136`
- primary_closer_than_secondary_rate: `0.3636`
- close_call_primary_closer_rate: `0.5714`

### 5d
- completed_count: `36`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.3056`
- primary_path_mean_absolute_error: `0.01892`
- primary_path_median_absolute_error: `0.01045`
- secondary_scenario_hit_rate: `0.2778`
- primary_vs_secondary_accuracy_spread: `0.0278`
- primary_closer_than_secondary_rate: `0.4722`
- close_call_primary_closer_rate: `0.4286`

### 10d
- completed_count: `16`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.017613`
- primary_path_median_absolute_error: `0.014348`
- secondary_scenario_hit_rate: `0.1875`
- primary_vs_secondary_accuracy_spread: `-0.0625`
- primary_closer_than_secondary_rate: `0.4375`
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
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
