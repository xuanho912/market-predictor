# Forecast Accuracy Scorecard

Generated at: `2026-08-31T19:11:10.876360+00:00`

## Sample Counts

- total_forecasts: `220`
- raw_forecast_rows: `220`
- deduped_legacy_rows: `0`
- pending_forecasts: `220`
- completed_1d: `215`
- completed_3d: `207`
- completed_5d: `199`
- completed_10d: `179`
- completed_20d: `139`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `215`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.3023`
- primary_path_mean_absolute_error: `0.010012`
- primary_path_median_absolute_error: `0.007881`
- secondary_scenario_hit_rate: `0.3209`
- primary_vs_secondary_accuracy_spread: `-0.0186`
- primary_closer_than_secondary_rate: `0.4326`
- close_call_primary_closer_rate: `0.3672`

### 3d
- completed_count: `207`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2319`
- primary_path_mean_absolute_error: `0.016276`
- primary_path_median_absolute_error: `0.012787`
- secondary_scenario_hit_rate: `0.3527`
- primary_vs_secondary_accuracy_spread: `-0.1208`
- primary_closer_than_secondary_rate: `0.3865`
- close_call_primary_closer_rate: `0.4167`

### 5d
- completed_count: `199`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2211`
- primary_path_mean_absolute_error: `0.023381`
- primary_path_median_absolute_error: `0.019209`
- secondary_scenario_hit_rate: `0.3015`
- primary_vs_secondary_accuracy_spread: `-0.0804`
- primary_closer_than_secondary_rate: `0.397`
- close_call_primary_closer_rate: `0.375`

### 10d
- completed_count: `179`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2011`
- primary_path_mean_absolute_error: `0.034812`
- primary_path_median_absolute_error: `0.028519`
- secondary_scenario_hit_rate: `0.3464`
- primary_vs_secondary_accuracy_spread: `-0.1453`
- primary_closer_than_secondary_rate: `0.3017`
- close_call_primary_closer_rate: `0.26`

### 20d
- completed_count: `139`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1079`
- primary_path_mean_absolute_error: `0.060235`
- primary_path_median_absolute_error: `0.061081`
- secondary_scenario_hit_rate: `0.2806`
- primary_vs_secondary_accuracy_spread: `-0.1727`
- primary_closer_than_secondary_rate: `0.2518`
- close_call_primary_closer_rate: `0.2535`

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
