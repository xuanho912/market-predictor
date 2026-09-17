# Forecast Accuracy Scorecard

Generated at: `2026-09-17T23:40:25.005979+00:00`

## Sample Counts

- total_forecasts: `272`
- raw_forecast_rows: `272`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `268`
- completed_3d: `260`
- completed_5d: `252`
- completed_10d: `232`
- completed_20d: `192`
- completed_60d: `32`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `268`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2799`
- primary_path_mean_absolute_error: `0.009983`
- primary_path_median_absolute_error: `0.007877`
- secondary_scenario_hit_rate: `0.3321`
- primary_vs_secondary_accuracy_spread: `-0.0522`
- primary_closer_than_secondary_rate: `0.3993`
- close_call_primary_closer_rate: `0.351`

### 3d
- completed_count: `260`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2654`
- primary_path_mean_absolute_error: `0.015634`
- primary_path_median_absolute_error: `0.012091`
- secondary_scenario_hit_rate: `0.3308`
- primary_vs_secondary_accuracy_spread: `-0.0654`
- primary_closer_than_secondary_rate: `0.4`
- close_call_primary_closer_rate: `0.4238`

### 5d
- completed_count: `252`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2857`
- primary_path_mean_absolute_error: `0.021153`
- primary_path_median_absolute_error: `0.014961`
- secondary_scenario_hit_rate: `0.2817`
- primary_vs_secondary_accuracy_spread: `0.004`
- primary_closer_than_secondary_rate: `0.4286`
- close_call_primary_closer_rate: `0.4`

### 10d
- completed_count: `232`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2241`
- primary_path_mean_absolute_error: `0.033739`
- primary_path_median_absolute_error: `0.027676`
- secondary_scenario_hit_rate: `0.3448`
- primary_vs_secondary_accuracy_spread: `-0.1207`
- primary_closer_than_secondary_rate: `0.3276`
- close_call_primary_closer_rate: `0.3147`

### 20d
- completed_count: `192`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1094`
- primary_path_mean_absolute_error: `0.061829`
- primary_path_median_absolute_error: `0.059492`
- secondary_scenario_hit_rate: `0.2969`
- primary_vs_secondary_accuracy_spread: `-0.1875`
- primary_closer_than_secondary_rate: `0.2396`
- close_call_primary_closer_rate: `0.2593`

### 60d
- completed_count: `32`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.061936`
- primary_path_median_absolute_error: `0.050587`
- secondary_scenario_hit_rate: `0.125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4375`
- close_call_primary_closer_rate: `0.7`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
