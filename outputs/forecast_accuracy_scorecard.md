# Forecast Accuracy Scorecard

Generated at: `2026-08-06T06:16:37.425656+00:00`

## Sample Counts

- total_forecasts: `152`
- raw_forecast_rows: `152`
- deduped_legacy_rows: `0`
- pending_forecasts: `152`
- completed_1d: `148`
- completed_3d: `140`
- completed_5d: `132`
- completed_10d: `112`
- completed_20d: `72`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `148`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3446`
- primary_path_mean_absolute_error: `0.0107`
- primary_path_median_absolute_error: `0.00826`
- secondary_scenario_hit_rate: `0.2905`
- primary_vs_secondary_accuracy_spread: `0.0541`
- primary_closer_than_secondary_rate: `0.5`
- close_call_primary_closer_rate: `0.45`

### 3d
- completed_count: `140`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2714`
- primary_path_mean_absolute_error: `0.016868`
- primary_path_median_absolute_error: `0.013064`
- secondary_scenario_hit_rate: `0.35`
- primary_vs_secondary_accuracy_spread: `-0.0786`
- primary_closer_than_secondary_rate: `0.3929`
- close_call_primary_closer_rate: `0.4444`

### 5d
- completed_count: `132`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2652`
- primary_path_mean_absolute_error: `0.022116`
- primary_path_median_absolute_error: `0.014511`
- secondary_scenario_hit_rate: `0.303`
- primary_vs_secondary_accuracy_spread: `-0.0379`
- primary_closer_than_secondary_rate: `0.4242`
- close_call_primary_closer_rate: `0.3788`

### 10d
- completed_count: `112`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2321`
- primary_path_mean_absolute_error: `0.027966`
- primary_path_median_absolute_error: `0.023426`
- secondary_scenario_hit_rate: `0.3393`
- primary_vs_secondary_accuracy_spread: `-0.1071`
- primary_closer_than_secondary_rate: `0.3482`
- close_call_primary_closer_rate: `0.2321`

### 20d
- completed_count: `72`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1528`
- primary_path_mean_absolute_error: `0.05115`
- primary_path_median_absolute_error: `0.043345`
- secondary_scenario_hit_rate: `0.2917`
- primary_vs_secondary_accuracy_spread: `-0.1389`
- primary_closer_than_secondary_rate: `0.3194`
- close_call_primary_closer_rate: `0.2857`

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
