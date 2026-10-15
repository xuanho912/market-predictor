# Forecast Accuracy Scorecard

Generated at: `2026-10-15T05:58:26.253633+00:00`

## Sample Counts

- total_forecasts: `348`
- raw_forecast_rows: `348`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `344`
- completed_3d: `336`
- completed_5d: `328`
- completed_10d: `308`
- completed_20d: `268`
- completed_60d: `108`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `344`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2616`
- primary_path_mean_absolute_error: `0.009947`
- primary_path_median_absolute_error: `0.008075`
- secondary_scenario_hit_rate: `0.343`
- primary_vs_secondary_accuracy_spread: `-0.0814`
- primary_closer_than_secondary_rate: `0.3721`
- close_call_primary_closer_rate: `0.3457`

### 3d
- completed_count: `336`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.256`
- primary_path_mean_absolute_error: `0.016228`
- primary_path_median_absolute_error: `0.01278`
- secondary_scenario_hit_rate: `0.3036`
- primary_vs_secondary_accuracy_spread: `-0.0476`
- primary_closer_than_secondary_rate: `0.3869`
- close_call_primary_closer_rate: `0.4239`

### 5d
- completed_count: `328`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2622`
- primary_path_mean_absolute_error: `0.022145`
- primary_path_median_absolute_error: `0.01786`
- secondary_scenario_hit_rate: `0.2896`
- primary_vs_secondary_accuracy_spread: `-0.0274`
- primary_closer_than_secondary_rate: `0.3872`
- close_call_primary_closer_rate: `0.3855`

### 10d
- completed_count: `308`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2273`
- primary_path_mean_absolute_error: `0.03223`
- primary_path_median_absolute_error: `0.026755`
- secondary_scenario_hit_rate: `0.3377`
- primary_vs_secondary_accuracy_spread: `-0.1104`
- primary_closer_than_secondary_rate: `0.3182`
- close_call_primary_closer_rate: `0.3333`

### 20d
- completed_count: `268`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1343`
- primary_path_mean_absolute_error: `0.058429`
- primary_path_median_absolute_error: `0.054226`
- secondary_scenario_hit_rate: `0.291`
- primary_vs_secondary_accuracy_spread: `-0.1567`
- primary_closer_than_secondary_rate: `0.2761`
- close_call_primary_closer_rate: `0.3245`

### 60d
- completed_count: `108`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1389`
- primary_path_mean_absolute_error: `0.069263`
- primary_path_median_absolute_error: `0.051247`
- secondary_scenario_hit_rate: `0.2315`
- primary_vs_secondary_accuracy_spread: `-0.0926`
- primary_closer_than_secondary_rate: `0.4352`
- close_call_primary_closer_rate: `0.5273`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
