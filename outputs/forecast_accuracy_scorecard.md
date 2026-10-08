# Forecast Accuracy Scorecard

Generated at: `2026-10-08T00:33:01.465994+00:00`

## Sample Counts

- total_forecasts: `328`
- raw_forecast_rows: `328`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `324`
- completed_3d: `316`
- completed_5d: `308`
- completed_10d: `288`
- completed_20d: `248`
- completed_60d: `88`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `324`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2623`
- primary_path_mean_absolute_error: `0.010036`
- primary_path_median_absolute_error: `0.008075`
- secondary_scenario_hit_rate: `0.3364`
- primary_vs_secondary_accuracy_spread: `-0.0741`
- primary_closer_than_secondary_rate: `0.3704`
- close_call_primary_closer_rate: `0.3409`

### 3d
- completed_count: `316`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2563`
- primary_path_mean_absolute_error: `0.016406`
- primary_path_median_absolute_error: `0.012757`
- secondary_scenario_hit_rate: `0.3006`
- primary_vs_secondary_accuracy_spread: `-0.0443`
- primary_closer_than_secondary_rate: `0.3861`
- close_call_primary_closer_rate: `0.4211`

### 5d
- completed_count: `308`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2727`
- primary_path_mean_absolute_error: `0.021867`
- primary_path_median_absolute_error: `0.016989`
- secondary_scenario_hit_rate: `0.2792`
- primary_vs_secondary_accuracy_spread: `-0.0065`
- primary_closer_than_secondary_rate: `0.4026`
- close_call_primary_closer_rate: `0.3918`

### 10d
- completed_count: `288`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2292`
- primary_path_mean_absolute_error: `0.032595`
- primary_path_median_absolute_error: `0.027019`
- secondary_scenario_hit_rate: `0.3299`
- primary_vs_secondary_accuracy_spread: `-0.1007`
- primary_closer_than_secondary_rate: `0.3229`
- close_call_primary_closer_rate: `0.3394`

### 20d
- completed_count: `248`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1411`
- primary_path_mean_absolute_error: `0.05864`
- primary_path_median_absolute_error: `0.054122`
- secondary_scenario_hit_rate: `0.2702`
- primary_vs_secondary_accuracy_spread: `-0.129`
- primary_closer_than_secondary_rate: `0.2944`
- close_call_primary_closer_rate: `0.3267`

### 60d
- completed_count: `88`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1364`
- primary_path_mean_absolute_error: `0.069353`
- primary_path_median_absolute_error: `0.051195`
- secondary_scenario_hit_rate: `0.2614`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4091`
- close_call_primary_closer_rate: `0.5111`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
