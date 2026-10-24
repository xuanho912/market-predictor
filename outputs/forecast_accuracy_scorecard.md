# Forecast Accuracy Scorecard

Generated at: `2026-10-24T01:22:37.063257+00:00`

## Sample Counts

- total_forecasts: `376`
- raw_forecast_rows: `376`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `372`
- completed_3d: `364`
- completed_5d: `356`
- completed_10d: `336`
- completed_20d: `296`
- completed_60d: `136`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `372`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2554`
- primary_path_mean_absolute_error: `0.010125`
- primary_path_median_absolute_error: `0.008355`
- secondary_scenario_hit_rate: `0.3333`
- primary_vs_secondary_accuracy_spread: `-0.078`
- primary_closer_than_secondary_rate: `0.3602`
- close_call_primary_closer_rate: `0.342`

### 3d
- completed_count: `364`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.016555`
- primary_path_median_absolute_error: `0.013026`
- secondary_scenario_hit_rate: `0.3022`
- primary_vs_secondary_accuracy_spread: `-0.0522`
- primary_closer_than_secondary_rate: `0.3736`
- close_call_primary_closer_rate: `0.4233`

### 5d
- completed_count: `356`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2612`
- primary_path_mean_absolute_error: `0.022522`
- primary_path_median_absolute_error: `0.018756`
- secondary_scenario_hit_rate: `0.2921`
- primary_vs_secondary_accuracy_spread: `-0.0309`
- primary_closer_than_secondary_rate: `0.3764`
- close_call_primary_closer_rate: `0.3862`

### 10d
- completed_count: `336`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2381`
- primary_path_mean_absolute_error: `0.032752`
- primary_path_median_absolute_error: `0.027676`
- secondary_scenario_hit_rate: `0.3333`
- primary_vs_secondary_accuracy_spread: `-0.0952`
- primary_closer_than_secondary_rate: `0.3333`
- close_call_primary_closer_rate: `0.3478`

### 20d
- completed_count: `296`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1453`
- primary_path_mean_absolute_error: `0.057009`
- primary_path_median_absolute_error: `0.053984`
- secondary_scenario_hit_rate: `0.2804`
- primary_vs_secondary_accuracy_spread: `-0.1351`
- primary_closer_than_secondary_rate: `0.3142`
- close_call_primary_closer_rate: `0.369`

### 60d
- completed_count: `136`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.071699`
- primary_path_median_absolute_error: `0.063702`
- secondary_scenario_hit_rate: `0.2132`
- primary_vs_secondary_accuracy_spread: `-0.0882`
- primary_closer_than_secondary_rate: `0.4118`
- close_call_primary_closer_rate: `0.5`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
