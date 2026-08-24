# Forecast Accuracy Scorecard

Generated at: `2026-08-24T20:58:01.581952+00:00`

## Sample Counts

- total_forecasts: `204`
- raw_forecast_rows: `204`
- deduped_legacy_rows: `0`
- pending_forecasts: `204`
- completed_1d: `200`
- completed_3d: `192`
- completed_5d: `184`
- completed_10d: `164`
- completed_20d: `124`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `200`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.32`
- primary_path_mean_absolute_error: `0.010058`
- primary_path_median_absolute_error: `0.007936`
- secondary_scenario_hit_rate: `0.315`
- primary_vs_secondary_accuracy_spread: `0.005`
- primary_closer_than_secondary_rate: `0.455`
- close_call_primary_closer_rate: `0.3982`

### 3d
- completed_count: `192`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2448`
- primary_path_mean_absolute_error: `0.016135`
- primary_path_median_absolute_error: `0.012757`
- secondary_scenario_hit_rate: `0.349`
- primary_vs_secondary_accuracy_spread: `-0.1042`
- primary_closer_than_secondary_rate: `0.3906`
- close_call_primary_closer_rate: `0.4167`

### 5d
- completed_count: `184`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2228`
- primary_path_mean_absolute_error: `0.023608`
- primary_path_median_absolute_error: `0.019272`
- secondary_scenario_hit_rate: `0.3098`
- primary_vs_secondary_accuracy_spread: `-0.087`
- primary_closer_than_secondary_rate: `0.3967`
- close_call_primary_closer_rate: `0.3627`

### 10d
- completed_count: `164`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2195`
- primary_path_mean_absolute_error: `0.034405`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3598`
- primary_vs_secondary_accuracy_spread: `-0.1402`
- primary_closer_than_secondary_rate: `0.3232`
- close_call_primary_closer_rate: `0.2796`

### 20d
- completed_count: `124`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.121`
- primary_path_mean_absolute_error: `0.057698`
- primary_path_median_absolute_error: `0.058348`
- secondary_scenario_hit_rate: `0.2742`
- primary_vs_secondary_accuracy_spread: `-0.1532`
- primary_closer_than_secondary_rate: `0.2661`
- close_call_primary_closer_rate: `0.254`

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
