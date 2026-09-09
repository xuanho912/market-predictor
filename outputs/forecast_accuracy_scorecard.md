# Forecast Accuracy Scorecard

Generated at: `2026-09-09T23:31:06.718005+00:00`

## Sample Counts

- total_forecasts: `248`
- raw_forecast_rows: `248`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `244`
- completed_3d: `236`
- completed_5d: `228`
- completed_10d: `208`
- completed_20d: `168`
- completed_60d: `8`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `244`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2828`
- primary_path_mean_absolute_error: `0.009845`
- primary_path_median_absolute_error: `0.007799`
- secondary_scenario_hit_rate: `0.3443`
- primary_vs_secondary_accuracy_spread: `-0.0615`
- primary_closer_than_secondary_rate: `0.4057`
- close_call_primary_closer_rate: `0.3378`

### 3d
- completed_count: `236`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2415`
- primary_path_mean_absolute_error: `0.016104`
- primary_path_median_absolute_error: `0.01226`
- secondary_scenario_hit_rate: `0.3475`
- primary_vs_secondary_accuracy_spread: `-0.1059`
- primary_closer_than_secondary_rate: `0.3856`
- close_call_primary_closer_rate: `0.4041`

### 5d
- completed_count: `228`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2368`
- primary_path_mean_absolute_error: `0.022303`
- primary_path_median_absolute_error: `0.017107`
- secondary_scenario_hit_rate: `0.307`
- primary_vs_secondary_accuracy_spread: `-0.0702`
- primary_closer_than_secondary_rate: `0.3904`
- close_call_primary_closer_rate: `0.3688`

### 10d
- completed_count: `208`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2019`
- primary_path_mean_absolute_error: `0.034447`
- primary_path_median_absolute_error: `0.028296`
- secondary_scenario_hit_rate: `0.3365`
- primary_vs_secondary_accuracy_spread: `-0.1346`
- primary_closer_than_secondary_rate: `0.3173`
- close_call_primary_closer_rate: `0.3058`

### 20d
- completed_count: `168`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1071`
- primary_path_mean_absolute_error: `0.059835`
- primary_path_median_absolute_error: `0.060059`
- secondary_scenario_hit_rate: `0.2917`
- primary_vs_secondary_accuracy_spread: `-0.1845`
- primary_closer_than_secondary_rate: `0.25`
- close_call_primary_closer_rate: `0.2632`

### 60d
- completed_count: `8`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `0.0`
- primary_path_mean_absolute_error: `0.041192`
- primary_path_median_absolute_error: `0.042548`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.5`
- close_call_primary_closer_rate: `None`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
