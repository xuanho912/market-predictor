# Forecast Accuracy Scorecard

Generated at: `2026-09-11T08:20:12.720063+00:00`

## Sample Counts

- total_forecasts: `252`
- raw_forecast_rows: `252`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `248`
- completed_3d: `240`
- completed_5d: `232`
- completed_10d: `212`
- completed_20d: `172`
- completed_60d: `12`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `248`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2863`
- primary_path_mean_absolute_error: `0.009764`
- primary_path_median_absolute_error: `0.007709`
- secondary_scenario_hit_rate: `0.3427`
- primary_vs_secondary_accuracy_spread: `-0.0565`
- primary_closer_than_secondary_rate: `0.4113`
- close_call_primary_closer_rate: `0.3467`

### 3d
- completed_count: `240`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2542`
- primary_path_mean_absolute_error: `0.015937`
- primary_path_median_absolute_error: `0.012091`
- secondary_scenario_hit_rate: `0.3417`
- primary_vs_secondary_accuracy_spread: `-0.0875`
- primary_closer_than_secondary_rate: `0.3958`
- close_call_primary_closer_rate: `0.4082`

### 5d
- completed_count: `232`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2414`
- primary_path_mean_absolute_error: `0.022124`
- primary_path_median_absolute_error: `0.016712`
- secondary_scenario_hit_rate: `0.3017`
- primary_vs_secondary_accuracy_spread: `-0.0603`
- primary_closer_than_secondary_rate: `0.3966`
- close_call_primary_closer_rate: `0.3706`

### 10d
- completed_count: `212`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2075`
- primary_path_mean_absolute_error: `0.034233`
- primary_path_median_absolute_error: `0.028296`
- secondary_scenario_hit_rate: `0.3349`
- primary_vs_secondary_accuracy_spread: `-0.1274`
- primary_closer_than_secondary_rate: `0.3208`
- close_call_primary_closer_rate: `0.312`

### 20d
- completed_count: `172`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1047`
- primary_path_mean_absolute_error: `0.060821`
- primary_path_median_absolute_error: `0.061807`
- secondary_scenario_hit_rate: `0.2849`
- primary_vs_secondary_accuracy_spread: `-0.1802`
- primary_closer_than_secondary_rate: `0.2442`
- close_call_primary_closer_rate: `0.2577`

### 60d
- completed_count: `12`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `0.0`
- primary_path_mean_absolute_error: `0.05692`
- primary_path_median_absolute_error: `0.051247`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.4167`
- close_call_primary_closer_rate: `None`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
