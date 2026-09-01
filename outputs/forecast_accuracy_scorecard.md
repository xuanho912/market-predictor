# Forecast Accuracy Scorecard

Generated at: `2026-09-01T06:19:25.868910+00:00`

## Sample Counts

- total_forecasts: `224`
- raw_forecast_rows: `224`
- deduped_legacy_rows: `0`
- pending_forecasts: `224`
- completed_1d: `218`
- completed_3d: `210`
- completed_5d: `202`
- completed_10d: `182`
- completed_20d: `142`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `218`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2982`
- primary_path_mean_absolute_error: `0.0099`
- primary_path_median_absolute_error: `0.007709`
- secondary_scenario_hit_rate: `0.3211`
- primary_vs_secondary_accuracy_spread: `-0.0229`
- primary_closer_than_secondary_rate: `0.4266`
- close_call_primary_closer_rate: `0.3588`

### 3d
- completed_count: `210`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2381`
- primary_path_mean_absolute_error: `0.016074`
- primary_path_median_absolute_error: `0.012757`
- secondary_scenario_hit_rate: `0.3476`
- primary_vs_secondary_accuracy_spread: `-0.1095`
- primary_closer_than_secondary_rate: `0.3905`
- close_call_primary_closer_rate: `0.4228`

### 5d
- completed_count: `202`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2228`
- primary_path_mean_absolute_error: `0.023096`
- primary_path_median_absolute_error: `0.018502`
- secondary_scenario_hit_rate: `0.297`
- primary_vs_secondary_accuracy_spread: `-0.0743`
- primary_closer_than_secondary_rate: `0.396`
- close_call_primary_closer_rate: `0.3739`

### 10d
- completed_count: `182`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1978`
- primary_path_mean_absolute_error: `0.035021`
- primary_path_median_absolute_error: `0.02869`
- secondary_scenario_hit_rate: `0.3462`
- primary_vs_secondary_accuracy_spread: `-0.1484`
- primary_closer_than_secondary_rate: `0.2967`
- close_call_primary_closer_rate: `0.2574`

### 20d
- completed_count: `142`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1056`
- primary_path_mean_absolute_error: `0.059514`
- primary_path_median_absolute_error: `0.058866`
- secondary_scenario_hit_rate: `0.2817`
- primary_vs_secondary_accuracy_spread: `-0.1761`
- primary_closer_than_secondary_rate: `0.2606`
- close_call_primary_closer_rate: `0.2667`

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
