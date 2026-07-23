# Forecast Accuracy Scorecard

Generated at: `2026-07-23T23:45:55.126586+00:00`

## Sample Counts

- total_forecasts: `116`
- raw_forecast_rows: `116`
- deduped_legacy_rows: `0`
- pending_forecasts: `116`
- completed_1d: `112`
- completed_3d: `104`
- completed_5d: `96`
- completed_10d: `76`
- completed_20d: `36`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `112`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3839`
- primary_path_mean_absolute_error: `0.009429`
- primary_path_median_absolute_error: `0.007071`
- secondary_scenario_hit_rate: `0.2411`
- primary_vs_secondary_accuracy_spread: `0.1429`
- primary_closer_than_secondary_rate: `0.5357`
- close_call_primary_closer_rate: `0.4821`

### 3d
- completed_count: `104`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2788`
- primary_path_mean_absolute_error: `0.013305`
- primary_path_median_absolute_error: `0.011856`
- secondary_scenario_hit_rate: `0.3558`
- primary_vs_secondary_accuracy_spread: `-0.0769`
- primary_closer_than_secondary_rate: `0.3846`
- close_call_primary_closer_rate: `0.4444`

### 5d
- completed_count: `96`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2917`
- primary_path_mean_absolute_error: `0.017138`
- primary_path_median_absolute_error: `0.011392`
- secondary_scenario_hit_rate: `0.2708`
- primary_vs_secondary_accuracy_spread: `0.0208`
- primary_closer_than_secondary_rate: `0.4479`
- close_call_primary_closer_rate: `0.4167`

### 10d
- completed_count: `76`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2368`
- primary_path_mean_absolute_error: `0.025167`
- primary_path_median_absolute_error: `0.020874`
- secondary_scenario_hit_rate: `0.3158`
- primary_vs_secondary_accuracy_spread: `-0.0789`
- primary_closer_than_secondary_rate: `0.3816`
- close_call_primary_closer_rate: `0.2703`

### 20d
- completed_count: `36`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.1667`
- primary_path_mean_absolute_error: `0.043856`
- primary_path_median_absolute_error: `0.038708`
- secondary_scenario_hit_rate: `0.2222`
- primary_vs_secondary_accuracy_spread: `-0.0556`
- primary_closer_than_secondary_rate: `0.4444`
- close_call_primary_closer_rate: `0.5714`

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
