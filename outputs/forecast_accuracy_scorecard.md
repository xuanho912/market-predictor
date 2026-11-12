# Forecast Accuracy Scorecard

Generated at: `2026-11-12T11:52:26.309434+00:00`

## Sample Counts

- total_forecasts: `428`
- raw_forecast_rows: `428`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `424`
- completed_3d: `416`
- completed_5d: `408`
- completed_10d: `388`
- completed_20d: `348`
- completed_60d: `188`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `424`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2642`
- primary_path_mean_absolute_error: `0.010859`
- primary_path_median_absolute_error: `0.008819`
- secondary_scenario_hit_rate: `0.3443`
- primary_vs_secondary_accuracy_spread: `-0.0802`
- primary_closer_than_secondary_rate: `0.3656`
- close_call_primary_closer_rate: `0.3455`

### 3d
- completed_count: `416`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2764`
- primary_path_mean_absolute_error: `0.017246`
- primary_path_median_absolute_error: `0.013157`
- secondary_scenario_hit_rate: `0.3101`
- primary_vs_secondary_accuracy_spread: `-0.0337`
- primary_closer_than_secondary_rate: `0.3894`
- close_call_primary_closer_rate: `0.4326`

### 5d
- completed_count: `408`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2574`
- primary_path_mean_absolute_error: `0.023245`
- primary_path_median_absolute_error: `0.01928`
- secondary_scenario_hit_rate: `0.3039`
- primary_vs_secondary_accuracy_spread: `-0.0466`
- primary_closer_than_secondary_rate: `0.3676`
- close_call_primary_closer_rate: `0.3721`

### 10d
- completed_count: `388`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2603`
- primary_path_mean_absolute_error: `0.032796`
- primary_path_median_absolute_error: `0.027871`
- secondary_scenario_hit_rate: `0.3144`
- primary_vs_secondary_accuracy_spread: `-0.0541`
- primary_closer_than_secondary_rate: `0.3479`
- close_call_primary_closer_rate: `0.335`

### 20d
- completed_count: `348`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1782`
- primary_path_mean_absolute_error: `0.057397`
- primary_path_median_absolute_error: `0.054275`
- secondary_scenario_hit_rate: `0.2672`
- primary_vs_secondary_accuracy_spread: `-0.0891`
- primary_closer_than_secondary_rate: `0.342`
- close_call_primary_closer_rate: `0.3936`

### 60d
- completed_count: `188`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1277`
- primary_path_mean_absolute_error: `0.077848`
- primary_path_median_absolute_error: `0.070618`
- secondary_scenario_hit_rate: `0.2394`
- primary_vs_secondary_accuracy_spread: `-0.1117`
- primary_closer_than_secondary_rate: `0.3723`
- close_call_primary_closer_rate: `0.4476`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
