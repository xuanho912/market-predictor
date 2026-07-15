# Forecast Accuracy Scorecard

Generated at: `2026-07-15T22:36:06.084278+00:00`

## Sample Counts

- total_forecasts: `92`
- raw_forecast_rows: `92`
- deduped_legacy_rows: `0`
- pending_forecasts: `92`
- completed_1d: `88`
- completed_3d: `80`
- completed_5d: `72`
- completed_10d: `52`
- completed_20d: `12`
- completed_60d: `0`
- current_evidence_level: `moderate_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `88`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3864`
- primary_path_mean_absolute_error: `0.009909`
- primary_path_median_absolute_error: `0.00682`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `0.1364`
- primary_closer_than_secondary_rate: `0.5341`
- close_call_primary_closer_rate: `0.5333`

### 3d
- completed_count: `80`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2625`
- primary_path_mean_absolute_error: `0.01269`
- primary_path_median_absolute_error: `0.011847`
- secondary_scenario_hit_rate: `0.3625`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.35`
- close_call_primary_closer_rate: `0.4359`

### 5d
- completed_count: `72`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3472`
- primary_path_mean_absolute_error: `0.016318`
- primary_path_median_absolute_error: `0.009112`
- secondary_scenario_hit_rate: `0.2639`
- primary_vs_secondary_accuracy_spread: `0.0833`
- primary_closer_than_secondary_rate: `0.5139`
- close_call_primary_closer_rate: `0.5143`

### 10d
- completed_count: `52`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.2308`
- primary_path_mean_absolute_error: `0.024191`
- primary_path_median_absolute_error: `0.020874`
- secondary_scenario_hit_rate: `0.3269`
- primary_vs_secondary_accuracy_spread: `-0.0962`
- primary_closer_than_secondary_rate: `0.3846`
- close_call_primary_closer_rate: `0.3077`

### 20d
- completed_count: `12`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `0.0`
- primary_path_mean_absolute_error: `0.040591`
- primary_path_median_absolute_error: `0.03546`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.4167`
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
