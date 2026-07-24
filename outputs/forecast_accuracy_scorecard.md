# Forecast Accuracy Scorecard

Generated at: `2026-07-24T22:40:46.649137+00:00`

## Sample Counts

- total_forecasts: `120`
- raw_forecast_rows: `120`
- deduped_legacy_rows: `0`
- pending_forecasts: `120`
- completed_1d: `116`
- completed_3d: `108`
- completed_5d: `100`
- completed_10d: `80`
- completed_20d: `40`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `116`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3707`
- primary_path_mean_absolute_error: `0.009585`
- primary_path_median_absolute_error: `0.007198`
- secondary_scenario_hit_rate: `0.2586`
- primary_vs_secondary_accuracy_spread: `0.1121`
- primary_closer_than_secondary_rate: `0.5259`
- close_call_primary_closer_rate: `0.4655`

### 3d
- completed_count: `108`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2963`
- primary_path_mean_absolute_error: `0.013272`
- primary_path_median_absolute_error: `0.011864`
- secondary_scenario_hit_rate: `0.3426`
- primary_vs_secondary_accuracy_spread: `-0.0463`
- primary_closer_than_secondary_rate: `0.4074`
- close_call_primary_closer_rate: `0.4545`

### 5d
- completed_count: `100`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.3`
- primary_path_mean_absolute_error: `0.016933`
- primary_path_median_absolute_error: `0.011392`
- secondary_scenario_hit_rate: `0.26`
- primary_vs_secondary_accuracy_spread: `0.04`
- primary_closer_than_secondary_rate: `0.46`
- close_call_primary_closer_rate: `0.42`

### 10d
- completed_count: `80`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.225`
- primary_path_mean_absolute_error: `0.026056`
- primary_path_median_absolute_error: `0.021062`
- secondary_scenario_hit_rate: `0.3125`
- primary_vs_secondary_accuracy_spread: `-0.0875`
- primary_closer_than_secondary_rate: `0.3625`
- close_call_primary_closer_rate: `0.2564`

### 20d
- completed_count: `40`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.15`
- primary_path_mean_absolute_error: `0.047368`
- primary_path_median_absolute_error: `0.03983`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4`
- close_call_primary_closer_rate: `0.4706`

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
