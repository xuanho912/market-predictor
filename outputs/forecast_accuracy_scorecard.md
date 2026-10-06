# Forecast Accuracy Scorecard

Generated at: `2026-10-06T18:25:57.191625+00:00`

## Sample Counts

- total_forecasts: `320`
- raw_forecast_rows: `320`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `316`
- completed_3d: `308`
- completed_5d: `300`
- completed_10d: `280`
- completed_20d: `240`
- completed_60d: `80`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `316`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2595`
- primary_path_mean_absolute_error: `0.010147`
- primary_path_median_absolute_error: `0.00826`
- secondary_scenario_hit_rate: `0.3354`
- primary_vs_secondary_accuracy_spread: `-0.0759`
- primary_closer_than_secondary_rate: `0.3703`
- close_call_primary_closer_rate: `0.345`

### 3d
- completed_count: `308`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2597`
- primary_path_mean_absolute_error: `0.016218`
- primary_path_median_absolute_error: `0.012624`
- secondary_scenario_hit_rate: `0.3052`
- primary_vs_secondary_accuracy_spread: `-0.0455`
- primary_closer_than_secondary_rate: `0.3896`
- close_call_primary_closer_rate: `0.4211`

### 5d
- completed_count: `300`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2733`
- primary_path_mean_absolute_error: `0.021737`
- primary_path_median_absolute_error: `0.016576`
- secondary_scenario_hit_rate: `0.2767`
- primary_vs_secondary_accuracy_spread: `-0.0033`
- primary_closer_than_secondary_rate: `0.4067`
- close_call_primary_closer_rate: `0.3846`

### 10d
- completed_count: `280`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2286`
- primary_path_mean_absolute_error: `0.032922`
- primary_path_median_absolute_error: `0.0276`
- secondary_scenario_hit_rate: `0.3357`
- primary_vs_secondary_accuracy_spread: `-0.1071`
- primary_closer_than_secondary_rate: `0.3179`
- close_call_primary_closer_rate: `0.3291`

### 20d
- completed_count: `240`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1375`
- primary_path_mean_absolute_error: `0.059173`
- primary_path_median_absolute_error: `0.054316`
- secondary_scenario_hit_rate: `0.275`
- primary_vs_secondary_accuracy_spread: `-0.1375`
- primary_closer_than_secondary_rate: `0.2875`
- close_call_primary_closer_rate: `0.3197`

### 60d
- completed_count: `80`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.125`
- primary_path_mean_absolute_error: `0.07018`
- primary_path_median_absolute_error: `0.050536`
- secondary_scenario_hit_rate: `0.275`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3875`
- close_call_primary_closer_rate: `0.4615`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
