# Forecast Accuracy Scorecard

Generated at: `2026-11-06T02:56:10.673738+00:00`

## Sample Counts

- total_forecasts: `412`
- raw_forecast_rows: `412`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `408`
- completed_3d: `400`
- completed_5d: `392`
- completed_10d: `372`
- completed_20d: `332`
- completed_60d: `172`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `408`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2623`
- primary_path_mean_absolute_error: `0.01062`
- primary_path_median_absolute_error: `0.008611`
- secondary_scenario_hit_rate: `0.3382`
- primary_vs_secondary_accuracy_spread: `-0.076`
- primary_closer_than_secondary_rate: `0.3652`
- close_call_primary_closer_rate: `0.3395`

### 3d
- completed_count: `400`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2725`
- primary_path_mean_absolute_error: `0.016668`
- primary_path_median_absolute_error: `0.013026`
- secondary_scenario_hit_rate: `0.3025`
- primary_vs_secondary_accuracy_spread: `-0.03`
- primary_closer_than_secondary_rate: `0.39`
- close_call_primary_closer_rate: `0.4333`

### 5d
- completed_count: `392`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2602`
- primary_path_mean_absolute_error: `0.022964`
- primary_path_median_absolute_error: `0.019236`
- secondary_scenario_hit_rate: `0.2959`
- primary_vs_secondary_accuracy_spread: `-0.0357`
- primary_closer_than_secondary_rate: `0.3699`
- close_call_primary_closer_rate: `0.3756`

### 10d
- completed_count: `372`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2527`
- primary_path_mean_absolute_error: `0.032626`
- primary_path_median_absolute_error: `0.027676`
- secondary_scenario_hit_rate: `0.3199`
- primary_vs_secondary_accuracy_spread: `-0.0672`
- primary_closer_than_secondary_rate: `0.3414`
- close_call_primary_closer_rate: `0.3368`

### 20d
- completed_count: `332`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1627`
- primary_path_mean_absolute_error: `0.057481`
- primary_path_median_absolute_error: `0.054296`
- secondary_scenario_hit_rate: `0.2741`
- primary_vs_secondary_accuracy_spread: `-0.1114`
- primary_closer_than_secondary_rate: `0.3283`
- close_call_primary_closer_rate: `0.3846`

### 60d
- completed_count: `172`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1279`
- primary_path_mean_absolute_error: `0.075814`
- primary_path_median_absolute_error: `0.070618`
- secondary_scenario_hit_rate: `0.2442`
- primary_vs_secondary_accuracy_spread: `-0.1163`
- primary_closer_than_secondary_rate: `0.3895`
- close_call_primary_closer_rate: `0.4639`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
