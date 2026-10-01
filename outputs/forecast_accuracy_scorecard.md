# Forecast Accuracy Scorecard

Generated at: `2026-10-01T18:27:34.239353+00:00`

## Sample Counts

- total_forecasts: `308`
- raw_forecast_rows: `308`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `304`
- completed_3d: `296`
- completed_5d: `288`
- completed_10d: `268`
- completed_20d: `228`
- completed_60d: `68`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `304`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2664`
- primary_path_mean_absolute_error: `0.010056`
- primary_path_median_absolute_error: `0.008169`
- secondary_scenario_hit_rate: `0.3421`
- primary_vs_secondary_accuracy_spread: `-0.0757`
- primary_closer_than_secondary_rate: `0.3816`
- close_call_primary_closer_rate: `0.3491`

### 3d
- completed_count: `296`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2568`
- primary_path_mean_absolute_error: `0.016184`
- primary_path_median_absolute_error: `0.012624`
- secondary_scenario_hit_rate: `0.3142`
- primary_vs_secondary_accuracy_spread: `-0.0574`
- primary_closer_than_secondary_rate: `0.3851`
- close_call_primary_closer_rate: `0.4167`

### 5d
- completed_count: `288`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2743`
- primary_path_mean_absolute_error: `0.021734`
- primary_path_median_absolute_error: `0.016339`
- secondary_scenario_hit_rate: `0.2812`
- primary_vs_secondary_accuracy_spread: `-0.0069`
- primary_closer_than_secondary_rate: `0.4062`
- close_call_primary_closer_rate: `0.3879`

### 10d
- completed_count: `268`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2313`
- primary_path_mean_absolute_error: `0.032963`
- primary_path_median_absolute_error: `0.027019`
- secondary_scenario_hit_rate: `0.3321`
- primary_vs_secondary_accuracy_spread: `-0.1007`
- primary_closer_than_secondary_rate: `0.3246`
- close_call_primary_closer_rate: `0.3311`

### 20d
- completed_count: `228`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1272`
- primary_path_mean_absolute_error: `0.06025`
- primary_path_median_absolute_error: `0.055559`
- secondary_scenario_hit_rate: `0.2851`
- primary_vs_secondary_accuracy_spread: `-0.1579`
- primary_closer_than_secondary_rate: `0.2719`
- close_call_primary_closer_rate: `0.305`

### 60d
- completed_count: `68`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.0882`
- primary_path_mean_absolute_error: `0.072724`
- primary_path_median_absolute_error: `0.051247`
- secondary_scenario_hit_rate: `0.2794`
- primary_vs_secondary_accuracy_spread: `-0.1912`
- primary_closer_than_secondary_rate: `0.3971`
- close_call_primary_closer_rate: `0.4375`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
