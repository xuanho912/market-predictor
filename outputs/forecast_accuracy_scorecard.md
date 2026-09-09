# Forecast Accuracy Scorecard

Generated at: `2026-09-09T08:26:32.202381+00:00`

## Sample Counts

- total_forecasts: `244`
- raw_forecast_rows: `244`
- deduped_legacy_rows: `0`
- pending_forecasts: `244`
- completed_1d: `240`
- completed_3d: `232`
- completed_5d: `224`
- completed_10d: `204`
- completed_20d: `164`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `240`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2833`
- primary_path_mean_absolute_error: `0.009897`
- primary_path_median_absolute_error: `0.007799`
- secondary_scenario_hit_rate: `0.3417`
- primary_vs_secondary_accuracy_spread: `-0.0583`
- primary_closer_than_secondary_rate: `0.4042`
- close_call_primary_closer_rate: `0.3333`

### 3d
- completed_count: `232`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2284`
- primary_path_mean_absolute_error: `0.01628`
- primary_path_median_absolute_error: `0.012757`
- secondary_scenario_hit_rate: `0.3534`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.375`
- close_call_primary_closer_rate: `0.3916`

### 5d
- completed_count: `224`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2321`
- primary_path_mean_absolute_error: `0.022453`
- primary_path_median_absolute_error: `0.0176`
- secondary_scenario_hit_rate: `0.308`
- primary_vs_secondary_accuracy_spread: `-0.0759`
- primary_closer_than_secondary_rate: `0.3884`
- close_call_primary_closer_rate: `0.365`

### 10d
- completed_count: `204`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2059`
- primary_path_mean_absolute_error: `0.034341`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3382`
- primary_vs_secondary_accuracy_spread: `-0.1324`
- primary_closer_than_secondary_rate: `0.3137`
- close_call_primary_closer_rate: `0.2991`

### 20d
- completed_count: `164`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1098`
- primary_path_mean_absolute_error: `0.059179`
- primary_path_median_absolute_error: `0.058866`
- secondary_scenario_hit_rate: `0.2866`
- primary_vs_secondary_accuracy_spread: `-0.1768`
- primary_closer_than_secondary_rate: `0.2561`
- close_call_primary_closer_rate: `0.2688`

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
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
