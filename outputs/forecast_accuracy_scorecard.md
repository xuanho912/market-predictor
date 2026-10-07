# Forecast Accuracy Scorecard

Generated at: `2026-10-07T18:59:46.057215+00:00`

## Sample Counts

- total_forecasts: `324`
- raw_forecast_rows: `324`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `320`
- completed_3d: `312`
- completed_5d: `304`
- completed_10d: `284`
- completed_20d: `244`
- completed_60d: `84`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `320`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2594`
- primary_path_mean_absolute_error: `0.010112`
- primary_path_median_absolute_error: `0.00826`
- secondary_scenario_hit_rate: `0.3375`
- primary_vs_secondary_accuracy_spread: `-0.0781`
- primary_closer_than_secondary_rate: `0.3688`
- close_call_primary_closer_rate: `0.341`

### 3d
- completed_count: `312`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2564`
- primary_path_mean_absolute_error: `0.016421`
- primary_path_median_absolute_error: `0.01278`
- secondary_scenario_hit_rate: `0.3013`
- primary_vs_secondary_accuracy_spread: `-0.0449`
- primary_closer_than_secondary_rate: `0.3878`
- close_call_primary_closer_rate: `0.4211`

### 5d
- completed_count: `304`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2697`
- primary_path_mean_absolute_error: `0.021976`
- primary_path_median_absolute_error: `0.016989`
- secondary_scenario_hit_rate: `0.2796`
- primary_vs_secondary_accuracy_spread: `-0.0099`
- primary_closer_than_secondary_rate: `0.4013`
- close_call_primary_closer_rate: `0.3846`

### 10d
- completed_count: `284`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2289`
- primary_path_mean_absolute_error: `0.032695`
- primary_path_median_absolute_error: `0.027019`
- secondary_scenario_hit_rate: `0.331`
- primary_vs_secondary_accuracy_spread: `-0.1021`
- primary_closer_than_secondary_rate: `0.3204`
- close_call_primary_closer_rate: `0.3354`

### 20d
- completed_count: `244`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1393`
- primary_path_mean_absolute_error: `0.058899`
- primary_path_median_absolute_error: `0.054122`
- secondary_scenario_hit_rate: `0.2746`
- primary_vs_secondary_accuracy_spread: `-0.1352`
- primary_closer_than_secondary_rate: `0.291`
- close_call_primary_closer_rate: `0.3243`

### 60d
- completed_count: `84`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1429`
- primary_path_mean_absolute_error: `0.068983`
- primary_path_median_absolute_error: `0.050536`
- secondary_scenario_hit_rate: `0.2619`
- primary_vs_secondary_accuracy_spread: `-0.119`
- primary_closer_than_secondary_rate: `0.4167`
- close_call_primary_closer_rate: `0.5116`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
