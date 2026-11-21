# Forecast Accuracy Scorecard

Generated at: `2026-11-21T03:35:34.737665+00:00`

## Sample Counts

- total_forecasts: `456`
- raw_forecast_rows: `456`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `452`
- completed_3d: `444`
- completed_5d: `436`
- completed_10d: `416`
- completed_20d: `376`
- completed_60d: `216`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `452`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2788`
- primary_path_mean_absolute_error: `0.010961`
- primary_path_median_absolute_error: `0.009055`
- secondary_scenario_hit_rate: `0.3341`
- primary_vs_secondary_accuracy_spread: `-0.0553`
- primary_closer_than_secondary_rate: `0.3805`
- close_call_primary_closer_rate: `0.3493`

### 3d
- completed_count: `444`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2815`
- primary_path_mean_absolute_error: `0.018202`
- primary_path_median_absolute_error: `0.013643`
- secondary_scenario_hit_rate: `0.3108`
- primary_vs_secondary_accuracy_spread: `-0.0293`
- primary_closer_than_secondary_rate: `0.3964`
- close_call_primary_closer_rate: `0.4323`

### 5d
- completed_count: `436`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2592`
- primary_path_mean_absolute_error: `0.025318`
- primary_path_median_absolute_error: `0.020263`
- secondary_scenario_hit_rate: `0.305`
- primary_vs_secondary_accuracy_spread: `-0.0459`
- primary_closer_than_secondary_rate: `0.367`
- close_call_primary_closer_rate: `0.3717`

### 10d
- completed_count: `416`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2812`
- primary_path_mean_absolute_error: `0.033161`
- primary_path_median_absolute_error: `0.028189`
- secondary_scenario_hit_rate: `0.3077`
- primary_vs_secondary_accuracy_spread: `-0.0264`
- primary_closer_than_secondary_rate: `0.3702`
- close_call_primary_closer_rate: `0.3442`

### 20d
- completed_count: `376`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2154`
- primary_path_mean_absolute_error: `0.05638`
- primary_path_median_absolute_error: `0.053984`
- secondary_scenario_hit_rate: `0.266`
- primary_vs_secondary_accuracy_spread: `-0.0505`
- primary_closer_than_secondary_rate: `0.3697`
- close_call_primary_closer_rate: `0.4031`

### 60d
- completed_count: `216`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1667`
- primary_path_mean_absolute_error: `0.080908`
- primary_path_median_absolute_error: `0.072083`
- secondary_scenario_hit_rate: `0.2361`
- primary_vs_secondary_accuracy_spread: `-0.0694`
- primary_closer_than_secondary_rate: `0.3843`
- close_call_primary_closer_rate: `0.4496`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_not_better_than_no_edge_keep_confidence_capped`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
