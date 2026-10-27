# Forecast Accuracy Scorecard

Generated at: `2026-10-27T00:00:55.628750+00:00`

## Sample Counts

- total_forecasts: `380`
- raw_forecast_rows: `380`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `376`
- completed_3d: `368`
- completed_5d: `360`
- completed_10d: `340`
- completed_20d: `300`
- completed_60d: `140`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `376`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.258`
- primary_path_mean_absolute_error: `0.010152`
- primary_path_median_absolute_error: `0.008377`
- secondary_scenario_hit_rate: `0.3351`
- primary_vs_secondary_accuracy_spread: `-0.0771`
- primary_closer_than_secondary_rate: `0.3617`
- close_call_primary_closer_rate: `0.3418`

### 3d
- completed_count: `368`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2527`
- primary_path_mean_absolute_error: `0.016446`
- primary_path_median_absolute_error: `0.0129`
- secondary_scenario_hit_rate: `0.3016`
- primary_vs_secondary_accuracy_spread: `-0.0489`
- primary_closer_than_secondary_rate: `0.375`
- close_call_primary_closer_rate: `0.4219`

### 5d
- completed_count: `360`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2583`
- primary_path_mean_absolute_error: `0.022553`
- primary_path_median_absolute_error: `0.018826`
- secondary_scenario_hit_rate: `0.2917`
- primary_vs_secondary_accuracy_spread: `-0.0333`
- primary_closer_than_secondary_rate: `0.3722`
- close_call_primary_closer_rate: `0.3862`

### 10d
- completed_count: `340`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2353`
- primary_path_mean_absolute_error: `0.032801`
- primary_path_median_absolute_error: `0.027754`
- secondary_scenario_hit_rate: `0.3353`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.3294`
- close_call_primary_closer_rate: `0.3441`

### 20d
- completed_count: `300`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.15`
- primary_path_mean_absolute_error: `0.056671`
- primary_path_median_absolute_error: `0.053786`
- secondary_scenario_hit_rate: `0.28`
- primary_vs_secondary_accuracy_spread: `-0.13`
- primary_closer_than_secondary_rate: `0.32`
- close_call_primary_closer_rate: `0.3728`

### 60d
- completed_count: `140`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1214`
- primary_path_mean_absolute_error: `0.071932`
- primary_path_median_absolute_error: `0.065154`
- secondary_scenario_hit_rate: `0.2143`
- primary_vs_secondary_accuracy_spread: `-0.0929`
- primary_closer_than_secondary_rate: `0.4143`
- close_call_primary_closer_rate: `0.5139`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
