# Forecast Accuracy Scorecard

Generated at: `2026-09-03T16:28:29.958206+00:00`

## Sample Counts

- total_forecasts: `232`
- raw_forecast_rows: `232`
- deduped_legacy_rows: `0`
- pending_forecasts: `232`
- completed_1d: `228`
- completed_3d: `220`
- completed_5d: `212`
- completed_10d: `192`
- completed_20d: `152`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `228`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2895`
- primary_path_mean_absolute_error: `0.010025`
- primary_path_median_absolute_error: `0.007799`
- secondary_scenario_hit_rate: `0.3289`
- primary_vs_secondary_accuracy_spread: `-0.0395`
- primary_closer_than_secondary_rate: `0.4123`
- close_call_primary_closer_rate: `0.3404`

### 3d
- completed_count: `220`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2318`
- primary_path_mean_absolute_error: `0.016226`
- primary_path_median_absolute_error: `0.012544`
- secondary_scenario_hit_rate: `0.3545`
- primary_vs_secondary_accuracy_spread: `-0.1227`
- primary_closer_than_secondary_rate: `0.3818`
- close_call_primary_closer_rate: `0.406`

### 5d
- completed_count: `212`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2264`
- primary_path_mean_absolute_error: `0.022892`
- primary_path_median_absolute_error: `0.018052`
- secondary_scenario_hit_rate: `0.3019`
- primary_vs_secondary_accuracy_spread: `-0.0755`
- primary_closer_than_secondary_rate: `0.3915`
- close_call_primary_closer_rate: `0.368`

### 10d
- completed_count: `192`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2083`
- primary_path_mean_absolute_error: `0.034453`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3333`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3021`
- close_call_primary_closer_rate: `0.2685`

### 20d
- completed_count: `152`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1184`
- primary_path_mean_absolute_error: `0.059257`
- primary_path_median_absolute_error: `0.058866`
- secondary_scenario_hit_rate: `0.2763`
- primary_vs_secondary_accuracy_spread: `-0.1579`
- primary_closer_than_secondary_rate: `0.2697`
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
