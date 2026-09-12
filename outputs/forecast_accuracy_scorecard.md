# Forecast Accuracy Scorecard

Generated at: `2026-09-12T00:46:55.474613+00:00`

## Sample Counts

- total_forecasts: `256`
- raw_forecast_rows: `256`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `252`
- completed_3d: `244`
- completed_5d: `236`
- completed_10d: `216`
- completed_20d: `176`
- completed_60d: `16`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `252`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2817`
- primary_path_mean_absolute_error: `0.009937`
- primary_path_median_absolute_error: `0.007877`
- secondary_scenario_hit_rate: `0.3373`
- primary_vs_secondary_accuracy_spread: `-0.0556`
- primary_closer_than_secondary_rate: `0.4048`
- close_call_primary_closer_rate: `0.3467`

### 3d
- completed_count: `244`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2541`
- primary_path_mean_absolute_error: `0.015849`
- primary_path_median_absolute_error: `0.012091`
- secondary_scenario_hit_rate: `0.3402`
- primary_vs_secondary_accuracy_spread: `-0.0861`
- primary_closer_than_secondary_rate: `0.3934`
- close_call_primary_closer_rate: `0.4122`

### 5d
- completed_count: `236`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2542`
- primary_path_mean_absolute_error: `0.021803`
- primary_path_median_absolute_error: `0.016339`
- secondary_scenario_hit_rate: `0.2966`
- primary_vs_secondary_accuracy_spread: `-0.0424`
- primary_closer_than_secondary_rate: `0.4068`
- close_call_primary_closer_rate: `0.3836`

### 10d
- completed_count: `216`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2083`
- primary_path_mean_absolute_error: `0.034412`
- primary_path_median_absolute_error: `0.028296`
- secondary_scenario_hit_rate: `0.3426`
- primary_vs_secondary_accuracy_spread: `-0.1343`
- primary_closer_than_secondary_rate: `0.3194`
- close_call_primary_closer_rate: `0.3101`

### 20d
- completed_count: `176`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1023`
- primary_path_mean_absolute_error: `0.060073`
- primary_path_median_absolute_error: `0.059096`
- secondary_scenario_hit_rate: `0.2955`
- primary_vs_secondary_accuracy_spread: `-0.1932`
- primary_closer_than_secondary_rate: `0.2386`
- close_call_primary_closer_rate: `0.2551`

### 60d
- completed_count: `16`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `0.0`
- primary_path_mean_absolute_error: `0.066077`
- primary_path_median_absolute_error: `0.051247`
- secondary_scenario_hit_rate: `0.1875`
- primary_vs_secondary_accuracy_spread: `-0.1875`
- primary_closer_than_secondary_rate: `0.375`
- close_call_primary_closer_rate: `None`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
