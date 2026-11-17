# Forecast Accuracy Scorecard

Generated at: `2026-11-17T05:03:48.980663+00:00`

## Sample Counts

- total_forecasts: `440`
- raw_forecast_rows: `440`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `436`
- completed_3d: `428`
- completed_5d: `420`
- completed_10d: `400`
- completed_20d: `360`
- completed_60d: `200`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `436`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2638`
- primary_path_mean_absolute_error: `0.010895`
- primary_path_median_absolute_error: `0.009055`
- secondary_scenario_hit_rate: `0.344`
- primary_vs_secondary_accuracy_spread: `-0.0803`
- primary_closer_than_secondary_rate: `0.3647`
- close_call_primary_closer_rate: `0.3407`

### 3d
- completed_count: `428`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2734`
- primary_path_mean_absolute_error: `0.017396`
- primary_path_median_absolute_error: `0.013244`
- secondary_scenario_hit_rate: `0.3131`
- primary_vs_secondary_accuracy_spread: `-0.0397`
- primary_closer_than_secondary_rate: `0.3902`
- close_call_primary_closer_rate: `0.4305`

### 5d
- completed_count: `420`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2571`
- primary_path_mean_absolute_error: `0.023667`
- primary_path_median_absolute_error: `0.019518`
- secondary_scenario_hit_rate: `0.3024`
- primary_vs_secondary_accuracy_spread: `-0.0452`
- primary_closer_than_secondary_rate: `0.369`
- close_call_primary_closer_rate: `0.375`

### 10d
- completed_count: `400`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2625`
- primary_path_mean_absolute_error: `0.032827`
- primary_path_median_absolute_error: `0.028189`
- secondary_scenario_hit_rate: `0.3125`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.355`
- close_call_primary_closer_rate: `0.3429`

### 20d
- completed_count: `360`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1889`
- primary_path_mean_absolute_error: `0.056516`
- primary_path_median_absolute_error: `0.054029`
- secondary_scenario_hit_rate: `0.2694`
- primary_vs_secondary_accuracy_spread: `-0.0806`
- primary_closer_than_secondary_rate: `0.35`
- close_call_primary_closer_rate: `0.3915`

### 60d
- completed_count: `200`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.135`
- primary_path_mean_absolute_error: `0.078617`
- primary_path_median_absolute_error: `0.070618`
- secondary_scenario_hit_rate: `0.235`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.37`
- close_call_primary_closer_rate: `0.4336`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
