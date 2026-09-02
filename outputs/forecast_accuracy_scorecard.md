# Forecast Accuracy Scorecard

Generated at: `2026-09-02T00:37:49.176064+00:00`

## Sample Counts

- total_forecasts: `228`
- raw_forecast_rows: `228`
- deduped_legacy_rows: `0`
- pending_forecasts: `228`
- completed_1d: `223`
- completed_3d: `215`
- completed_5d: `207`
- completed_10d: `187`
- completed_20d: `147`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `223`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.296`
- primary_path_mean_absolute_error: `0.009931`
- primary_path_median_absolute_error: `0.007692`
- secondary_scenario_hit_rate: `0.3274`
- primary_vs_secondary_accuracy_spread: `-0.0314`
- primary_closer_than_secondary_rate: `0.4215`
- close_call_primary_closer_rate: `0.3529`

### 3d
- completed_count: `215`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2372`
- primary_path_mean_absolute_error: `0.016311`
- primary_path_median_absolute_error: `0.012774`
- secondary_scenario_hit_rate: `0.3535`
- primary_vs_secondary_accuracy_spread: `-0.1163`
- primary_closer_than_secondary_rate: `0.386`
- close_call_primary_closer_rate: `0.4141`

### 5d
- completed_count: `207`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2222`
- primary_path_mean_absolute_error: `0.023196`
- primary_path_median_absolute_error: `0.0186`
- secondary_scenario_hit_rate: `0.2995`
- primary_vs_secondary_accuracy_spread: `-0.0773`
- primary_closer_than_secondary_rate: `0.3913`
- close_call_primary_closer_rate: `0.3667`

### 10d
- completed_count: `187`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2086`
- primary_path_mean_absolute_error: `0.034614`
- primary_path_median_absolute_error: `0.028072`
- secondary_scenario_hit_rate: `0.3369`
- primary_vs_secondary_accuracy_spread: `-0.1283`
- primary_closer_than_secondary_rate: `0.3048`
- close_call_primary_closer_rate: `0.2667`

### 20d
- completed_count: `147`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1156`
- primary_path_mean_absolute_error: `0.059666`
- primary_path_median_absolute_error: `0.059038`
- secondary_scenario_hit_rate: `0.2789`
- primary_vs_secondary_accuracy_spread: `-0.1633`
- primary_closer_than_secondary_rate: `0.2653`
- close_call_primary_closer_rate: `0.2785`

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
