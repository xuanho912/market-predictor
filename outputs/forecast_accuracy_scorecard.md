# Forecast Accuracy Scorecard

Generated at: `2026-09-19T08:20:01.716068+00:00`

## Sample Counts

- total_forecasts: `276`
- raw_forecast_rows: `276`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `272`
- completed_3d: `264`
- completed_5d: `256`
- completed_10d: `236`
- completed_20d: `196`
- completed_60d: `36`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `272`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2794`
- primary_path_mean_absolute_error: `0.009898`
- primary_path_median_absolute_error: `0.007709`
- secondary_scenario_hit_rate: `0.3272`
- primary_vs_secondary_accuracy_spread: `-0.0478`
- primary_closer_than_secondary_rate: `0.4007`
- close_call_primary_closer_rate: `0.3595`

### 3d
- completed_count: `264`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2652`
- primary_path_mean_absolute_error: `0.015733`
- primary_path_median_absolute_error: `0.012132`
- secondary_scenario_hit_rate: `0.3258`
- primary_vs_secondary_accuracy_spread: `-0.0606`
- primary_closer_than_secondary_rate: `0.3977`
- close_call_primary_closer_rate: `0.4238`

### 5d
- completed_count: `256`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2891`
- primary_path_mean_absolute_error: `0.021134`
- primary_path_median_absolute_error: `0.014961`
- secondary_scenario_hit_rate: `0.2812`
- primary_vs_secondary_accuracy_spread: `0.0078`
- primary_closer_than_secondary_rate: `0.4297`
- close_call_primary_closer_rate: `0.3974`

### 10d
- completed_count: `236`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2331`
- primary_path_mean_absolute_error: `0.033405`
- primary_path_median_absolute_error: `0.0276`
- secondary_scenario_hit_rate: `0.3432`
- primary_vs_secondary_accuracy_spread: `-0.1102`
- primary_closer_than_secondary_rate: `0.3347`
- close_call_primary_closer_rate: `0.3219`

### 20d
- completed_count: `196`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1122`
- primary_path_mean_absolute_error: `0.061469`
- primary_path_median_absolute_error: `0.059096`
- secondary_scenario_hit_rate: `0.2959`
- primary_vs_secondary_accuracy_spread: `-0.1837`
- primary_closer_than_secondary_rate: `0.2449`
- close_call_primary_closer_rate: `0.2661`

### 60d
- completed_count: `36`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.1389`
- primary_path_mean_absolute_error: `0.064434`
- primary_path_median_absolute_error: `0.050587`
- secondary_scenario_hit_rate: `0.1111`
- primary_vs_secondary_accuracy_spread: `0.0278`
- primary_closer_than_secondary_rate: `0.4444`
- close_call_primary_closer_rate: `0.6429`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
