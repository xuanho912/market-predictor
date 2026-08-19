# Forecast Accuracy Scorecard

Generated at: `2026-08-19T13:11:38.724248+00:00`

## Sample Counts

- total_forecasts: `188`
- raw_forecast_rows: `188`
- deduped_legacy_rows: `0`
- pending_forecasts: `188`
- completed_1d: `184`
- completed_3d: `176`
- completed_5d: `168`
- completed_10d: `148`
- completed_20d: `108`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `184`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3424`
- primary_path_mean_absolute_error: `0.009759`
- primary_path_median_absolute_error: `0.007551`
- secondary_scenario_hit_rate: `0.2989`
- primary_vs_secondary_accuracy_spread: `0.0435`
- primary_closer_than_secondary_rate: `0.4891`
- close_call_primary_closer_rate: `0.4314`

### 3d
- completed_count: `176`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2557`
- primary_path_mean_absolute_error: `0.015625`
- primary_path_median_absolute_error: `0.01226`
- secondary_scenario_hit_rate: `0.3466`
- primary_vs_secondary_accuracy_spread: `-0.0909`
- primary_closer_than_secondary_rate: `0.4034`
- close_call_primary_closer_rate: `0.4388`

### 5d
- completed_count: `168`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2381`
- primary_path_mean_absolute_error: `0.022886`
- primary_path_median_absolute_error: `0.017107`
- secondary_scenario_hit_rate: `0.3214`
- primary_vs_secondary_accuracy_spread: `-0.0833`
- primary_closer_than_secondary_rate: `0.4286`
- close_call_primary_closer_rate: `0.3895`

### 10d
- completed_count: `148`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.223`
- primary_path_mean_absolute_error: `0.035283`
- primary_path_median_absolute_error: `0.02869`
- secondary_scenario_hit_rate: `0.3716`
- primary_vs_secondary_accuracy_spread: `-0.1486`
- primary_closer_than_secondary_rate: `0.3108`
- close_call_primary_closer_rate: `0.2375`

### 20d
- completed_count: `108`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1389`
- primary_path_mean_absolute_error: `0.053962`
- primary_path_median_absolute_error: `0.051253`
- secondary_scenario_hit_rate: `0.2593`
- primary_vs_secondary_accuracy_spread: `-0.1204`
- primary_closer_than_secondary_rate: `0.3056`
- close_call_primary_closer_rate: `0.2909`

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
