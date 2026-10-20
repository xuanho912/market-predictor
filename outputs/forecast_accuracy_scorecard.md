# Forecast Accuracy Scorecard

Generated at: `2026-10-20T00:56:06.664306+00:00`

## Sample Counts

- total_forecasts: `360`
- raw_forecast_rows: `360`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `356`
- completed_3d: `348`
- completed_5d: `340`
- completed_10d: `320`
- completed_20d: `280`
- completed_60d: `120`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `356`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2584`
- primary_path_mean_absolute_error: `0.010176`
- primary_path_median_absolute_error: `0.008377`
- secondary_scenario_hit_rate: `0.3427`
- primary_vs_secondary_accuracy_spread: `-0.0843`
- primary_closer_than_secondary_rate: `0.3652`
- close_call_primary_closer_rate: `0.3439`

### 3d
- completed_count: `348`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.016396`
- primary_path_median_absolute_error: `0.0129`
- secondary_scenario_hit_rate: `0.3075`
- primary_vs_secondary_accuracy_spread: `-0.0575`
- primary_closer_than_secondary_rate: `0.3793`
- close_call_primary_closer_rate: `0.4202`

### 5d
- completed_count: `340`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2676`
- primary_path_mean_absolute_error: `0.022177`
- primary_path_median_absolute_error: `0.018152`
- secondary_scenario_hit_rate: `0.2882`
- primary_vs_secondary_accuracy_spread: `-0.0206`
- primary_closer_than_secondary_rate: `0.3882`
- close_call_primary_closer_rate: `0.3871`

### 10d
- completed_count: `320`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2344`
- primary_path_mean_absolute_error: `0.032563`
- primary_path_median_absolute_error: `0.0276`
- secondary_scenario_hit_rate: `0.3344`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.3219`
- close_call_primary_closer_rate: `0.3353`

### 20d
- completed_count: `280`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1429`
- primary_path_mean_absolute_error: `0.057477`
- primary_path_median_absolute_error: `0.053802`
- secondary_scenario_hit_rate: `0.2821`
- primary_vs_secondary_accuracy_spread: `-0.1393`
- primary_closer_than_secondary_rate: `0.3`
- close_call_primary_closer_rate: `0.3481`

### 60d
- completed_count: `120`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.070518`
- primary_path_median_absolute_error: `0.060001`
- secondary_scenario_hit_rate: `0.2167`
- primary_vs_secondary_accuracy_spread: `-0.0917`
- primary_closer_than_secondary_rate: `0.425`
- close_call_primary_closer_rate: `0.5246`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
