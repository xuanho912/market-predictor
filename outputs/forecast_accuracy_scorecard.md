# Forecast Accuracy Scorecard

Generated at: `2026-11-05T01:56:17.356837+00:00`

## Sample Counts

- total_forecasts: `408`
- raw_forecast_rows: `408`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `404`
- completed_3d: `396`
- completed_5d: `388`
- completed_10d: `368`
- completed_20d: `328`
- completed_60d: `168`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `404`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2624`
- primary_path_mean_absolute_error: `0.01023`
- primary_path_median_absolute_error: `0.008377`
- secondary_scenario_hit_rate: `0.3366`
- primary_vs_secondary_accuracy_spread: `-0.0743`
- primary_closer_than_secondary_rate: `0.3663`
- close_call_primary_closer_rate: `0.3443`

### 3d
- completed_count: `396`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2652`
- primary_path_mean_absolute_error: `0.016753`
- primary_path_median_absolute_error: `0.013076`
- secondary_scenario_hit_rate: `0.3056`
- primary_vs_secondary_accuracy_spread: `-0.0404`
- primary_closer_than_secondary_rate: `0.3838`
- close_call_primary_closer_rate: `0.4279`

### 5d
- completed_count: `388`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2603`
- primary_path_mean_absolute_error: `0.022573`
- primary_path_median_absolute_error: `0.018826`
- secondary_scenario_hit_rate: `0.2912`
- primary_vs_secondary_accuracy_spread: `-0.0309`
- primary_closer_than_secondary_rate: `0.3711`
- close_call_primary_closer_rate: `0.3793`

### 10d
- completed_count: `368`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2473`
- primary_path_mean_absolute_error: `0.032533`
- primary_path_median_absolute_error: `0.027639`
- secondary_scenario_hit_rate: `0.3207`
- primary_vs_secondary_accuracy_spread: `-0.0734`
- primary_closer_than_secondary_rate: `0.337`
- close_call_primary_closer_rate: `0.3385`

### 20d
- completed_count: `328`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1616`
- primary_path_mean_absolute_error: `0.057074`
- primary_path_median_absolute_error: `0.054296`
- secondary_scenario_hit_rate: `0.2713`
- primary_vs_secondary_accuracy_spread: `-0.1098`
- primary_closer_than_secondary_rate: `0.3262`
- close_call_primary_closer_rate: `0.3855`

### 60d
- completed_count: `168`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.131`
- primary_path_mean_absolute_error: `0.073427`
- primary_path_median_absolute_error: `0.06856`
- secondary_scenario_hit_rate: `0.25`
- primary_vs_secondary_accuracy_spread: `-0.119`
- primary_closer_than_secondary_rate: `0.3988`
- close_call_primary_closer_rate: `0.4737`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
