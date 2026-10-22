# Forecast Accuracy Scorecard

Generated at: `2026-10-22T00:27:21.696107+00:00`

## Sample Counts

- total_forecasts: `368`
- raw_forecast_rows: `368`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `364`
- completed_3d: `356`
- completed_5d: `348`
- completed_10d: `328`
- completed_20d: `288`
- completed_60d: `128`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `364`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2527`
- primary_path_mean_absolute_error: `0.01019`
- primary_path_median_absolute_error: `0.008451`
- secondary_scenario_hit_rate: `0.3352`
- primary_vs_secondary_accuracy_spread: `-0.0824`
- primary_closer_than_secondary_rate: `0.3571`
- close_call_primary_closer_rate: `0.3439`

### 3d
- completed_count: `356`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2472`
- primary_path_mean_absolute_error: `0.016597`
- primary_path_median_absolute_error: `0.013026`
- secondary_scenario_hit_rate: `0.3034`
- primary_vs_secondary_accuracy_spread: `-0.0562`
- primary_closer_than_secondary_rate: `0.3736`
- close_call_primary_closer_rate: `0.4233`

### 5d
- completed_count: `348`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2615`
- primary_path_mean_absolute_error: `0.022458`
- primary_path_median_absolute_error: `0.018662`
- secondary_scenario_hit_rate: `0.296`
- primary_vs_secondary_accuracy_spread: `-0.0345`
- primary_closer_than_secondary_rate: `0.3793`
- close_call_primary_closer_rate: `0.383`

### 10d
- completed_count: `328`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2378`
- primary_path_mean_absolute_error: `0.032738`
- primary_path_median_absolute_error: `0.027676`
- secondary_scenario_hit_rate: `0.3354`
- primary_vs_secondary_accuracy_spread: `-0.0976`
- primary_closer_than_secondary_rate: `0.3262`
- close_call_primary_closer_rate: `0.3408`

### 20d
- completed_count: `288`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1424`
- primary_path_mean_absolute_error: `0.057257`
- primary_path_median_absolute_error: `0.053802`
- secondary_scenario_hit_rate: `0.2778`
- primary_vs_secondary_accuracy_spread: `-0.1354`
- primary_closer_than_secondary_rate: `0.3125`
- close_call_primary_closer_rate: `0.3636`

### 60d
- completed_count: `128`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.070653`
- primary_path_median_absolute_error: `0.061834`
- secondary_scenario_hit_rate: `0.2109`
- primary_vs_secondary_accuracy_spread: `-0.0859`
- primary_closer_than_secondary_rate: `0.4219`
- close_call_primary_closer_rate: `0.5231`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
