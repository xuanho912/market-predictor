# Forecast Accuracy Scorecard

Generated at: `2026-09-15T06:13:15.373960+00:00`

## Sample Counts

- total_forecasts: `260`
- raw_forecast_rows: `260`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `256`
- completed_3d: `248`
- completed_5d: `240`
- completed_10d: `220`
- completed_20d: `180`
- completed_60d: `20`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `256`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2891`
- primary_path_mean_absolute_error: `0.009822`
- primary_path_median_absolute_error: `0.007709`
- secondary_scenario_hit_rate: `0.3359`
- primary_vs_secondary_accuracy_spread: `-0.0469`
- primary_closer_than_secondary_rate: `0.4102`
- close_call_primary_closer_rate: `0.351`

### 3d
- completed_count: `248`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2581`
- primary_path_mean_absolute_error: `0.015788`
- primary_path_median_absolute_error: `0.012091`
- secondary_scenario_hit_rate: `0.3387`
- primary_vs_secondary_accuracy_spread: `-0.0806`
- primary_closer_than_secondary_rate: `0.3952`
- close_call_primary_closer_rate: `0.42`

### 5d
- completed_count: `240`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2667`
- primary_path_mean_absolute_error: `0.021551`
- primary_path_median_absolute_error: `0.015516`
- secondary_scenario_hit_rate: `0.2917`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4167`
- close_call_primary_closer_rate: `0.3878`

### 10d
- completed_count: `220`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2091`
- primary_path_mean_absolute_error: `0.034501`
- primary_path_median_absolute_error: `0.028296`
- secondary_scenario_hit_rate: `0.3455`
- primary_vs_secondary_accuracy_spread: `-0.1364`
- primary_closer_than_secondary_rate: `0.3182`
- close_call_primary_closer_rate: `0.3083`

### 20d
- completed_count: `180`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1`
- primary_path_mean_absolute_error: `0.061054`
- primary_path_median_absolute_error: `0.060117`
- secondary_scenario_hit_rate: `0.3056`
- primary_vs_secondary_accuracy_spread: `-0.2056`
- primary_closer_than_secondary_rate: `0.2333`
- close_call_primary_closer_rate: `0.25`

### 60d
- completed_count: `20`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.05`
- primary_path_mean_absolute_error: `0.064346`
- primary_path_median_absolute_error: `0.051247`
- secondary_scenario_hit_rate: `0.2`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.45`
- close_call_primary_closer_rate: `0.6667`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
