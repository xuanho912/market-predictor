# Forecast Accuracy Scorecard

Generated at: `2026-10-29T10:26:46.784009+00:00`

## Sample Counts

- total_forecasts: `388`
- raw_forecast_rows: `388`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `384`
- completed_3d: `376`
- completed_5d: `368`
- completed_10d: `348`
- completed_20d: `308`
- completed_60d: `148`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `384`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2604`
- primary_path_mean_absolute_error: `0.010023`
- primary_path_median_absolute_error: `0.008075`
- secondary_scenario_hit_rate: `0.3359`
- primary_vs_secondary_accuracy_spread: `-0.0755`
- primary_closer_than_secondary_rate: `0.3646`
- close_call_primary_closer_rate: `0.34`

### 3d
- completed_count: `376`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.258`
- primary_path_mean_absolute_error: `0.016436`
- primary_path_median_absolute_error: `0.013013`
- secondary_scenario_hit_rate: `0.3005`
- primary_vs_secondary_accuracy_spread: `-0.0426`
- primary_closer_than_secondary_rate: `0.3777`
- close_call_primary_closer_rate: `0.4235`

### 5d
- completed_count: `368`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2609`
- primary_path_mean_absolute_error: `0.022458`
- primary_path_median_absolute_error: `0.018826`
- secondary_scenario_hit_rate: `0.2908`
- primary_vs_secondary_accuracy_spread: `-0.0299`
- primary_closer_than_secondary_rate: `0.3723`
- close_call_primary_closer_rate: `0.3854`

### 10d
- completed_count: `348`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2299`
- primary_path_mean_absolute_error: `0.032941`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3362`
- primary_vs_secondary_accuracy_spread: `-0.1063`
- primary_closer_than_secondary_rate: `0.3218`
- close_call_primary_closer_rate: `0.3404`

### 20d
- completed_count: `308`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1558`
- primary_path_mean_absolute_error: `0.056424`
- primary_path_median_absolute_error: `0.053786`
- secondary_scenario_hit_rate: `0.2792`
- primary_vs_secondary_accuracy_spread: `-0.1234`
- primary_closer_than_secondary_rate: `0.3214`
- close_call_primary_closer_rate: `0.3743`

### 60d
- completed_count: `148`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1149`
- primary_path_mean_absolute_error: `0.071848`
- primary_path_median_absolute_error: `0.065154`
- secondary_scenario_hit_rate: `0.223`
- primary_vs_secondary_accuracy_spread: `-0.1081`
- primary_closer_than_secondary_rate: `0.4122`
- close_call_primary_closer_rate: `0.5`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
