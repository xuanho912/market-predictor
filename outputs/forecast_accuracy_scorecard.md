# Forecast Accuracy Scorecard

Generated at: `2026-11-03T03:05:54.741610+00:00`

## Sample Counts

- total_forecasts: `400`
- raw_forecast_rows: `400`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `396`
- completed_3d: `388`
- completed_5d: `380`
- completed_10d: `360`
- completed_20d: `320`
- completed_60d: `160`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `396`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2677`
- primary_path_mean_absolute_error: `0.01002`
- primary_path_median_absolute_error: `0.008169`
- secondary_scenario_hit_rate: `0.3359`
- primary_vs_secondary_accuracy_spread: `-0.0682`
- primary_closer_than_secondary_rate: `0.3712`
- close_call_primary_closer_rate: `0.3462`

### 3d
- completed_count: `388`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2629`
- primary_path_mean_absolute_error: `0.016697`
- primary_path_median_absolute_error: `0.013013`
- secondary_scenario_hit_rate: `0.3015`
- primary_vs_secondary_accuracy_spread: `-0.0387`
- primary_closer_than_secondary_rate: `0.3814`
- close_call_primary_closer_rate: `0.4236`

### 5d
- completed_count: `380`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2605`
- primary_path_mean_absolute_error: `0.022321`
- primary_path_median_absolute_error: `0.018662`
- secondary_scenario_hit_rate: `0.2868`
- primary_vs_secondary_accuracy_spread: `-0.0263`
- primary_closer_than_secondary_rate: `0.3737`
- close_call_primary_closer_rate: `0.3858`

### 10d
- completed_count: `360`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2417`
- primary_path_mean_absolute_error: `0.032694`
- primary_path_median_absolute_error: `0.027676`
- secondary_scenario_hit_rate: `0.3278`
- primary_vs_secondary_accuracy_spread: `-0.0861`
- primary_closer_than_secondary_rate: `0.3306`
- close_call_primary_closer_rate: `0.3386`

### 20d
- completed_count: `320`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1594`
- primary_path_mean_absolute_error: `0.056591`
- primary_path_median_absolute_error: `0.054073`
- secondary_scenario_hit_rate: `0.2781`
- primary_vs_secondary_accuracy_spread: `-0.1187`
- primary_closer_than_secondary_rate: `0.325`
- close_call_primary_closer_rate: `0.3815`

### 60d
- completed_count: `160`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1313`
- primary_path_mean_absolute_error: `0.072371`
- primary_path_median_absolute_error: `0.06687`
- secondary_scenario_hit_rate: `0.2437`
- primary_vs_secondary_accuracy_spread: `-0.1125`
- primary_closer_than_secondary_rate: `0.4062`
- close_call_primary_closer_rate: `0.4889`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
