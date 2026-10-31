# Forecast Accuracy Scorecard

Generated at: `2026-10-31T01:18:28.352938+00:00`

## Sample Counts

- total_forecasts: `396`
- raw_forecast_rows: `396`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `392`
- completed_3d: `384`
- completed_5d: `376`
- completed_10d: `356`
- completed_20d: `316`
- completed_60d: `156`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `392`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2653`
- primary_path_mean_absolute_error: `0.010079`
- primary_path_median_absolute_error: `0.00826`
- secondary_scenario_hit_rate: `0.3393`
- primary_vs_secondary_accuracy_spread: `-0.074`
- primary_closer_than_secondary_rate: `0.3673`
- close_call_primary_closer_rate: `0.3415`

### 3d
- completed_count: `384`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2604`
- primary_path_mean_absolute_error: `0.016522`
- primary_path_median_absolute_error: `0.0129`
- secondary_scenario_hit_rate: `0.2995`
- primary_vs_secondary_accuracy_spread: `-0.0391`
- primary_closer_than_secondary_rate: `0.3802`
- close_call_primary_closer_rate: `0.425`

### 5d
- completed_count: `376`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.258`
- primary_path_mean_absolute_error: `0.022366`
- primary_path_median_absolute_error: `0.018756`
- secondary_scenario_hit_rate: `0.2872`
- primary_vs_secondary_accuracy_spread: `-0.0293`
- primary_closer_than_secondary_rate: `0.3723`
- close_call_primary_closer_rate: `0.3827`

### 10d
- completed_count: `356`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.236`
- primary_path_mean_absolute_error: `0.032782`
- primary_path_median_absolute_error: `0.027754`
- secondary_scenario_hit_rate: `0.3315`
- primary_vs_secondary_accuracy_spread: `-0.0955`
- primary_closer_than_secondary_rate: `0.3258`
- close_call_primary_closer_rate: `0.3386`

### 20d
- completed_count: `316`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1582`
- primary_path_mean_absolute_error: `0.056551`
- primary_path_median_absolute_error: `0.054029`
- secondary_scenario_hit_rate: `0.2816`
- primary_vs_secondary_accuracy_spread: `-0.1234`
- primary_closer_than_secondary_rate: `0.3196`
- close_call_primary_closer_rate: `0.3743`

### 60d
- completed_count: `156`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1282`
- primary_path_mean_absolute_error: `0.071448`
- primary_path_median_absolute_error: `0.06665`
- secondary_scenario_hit_rate: `0.2372`
- primary_vs_secondary_accuracy_spread: `-0.109`
- primary_closer_than_secondary_rate: `0.4103`
- close_call_primary_closer_rate: `0.4943`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
