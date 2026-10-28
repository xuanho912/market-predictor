# Forecast Accuracy Scorecard

Generated at: `2026-10-28T00:59:13.860864+00:00`

## Sample Counts

- total_forecasts: `384`
- raw_forecast_rows: `384`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `380`
- completed_3d: `372`
- completed_5d: `364`
- completed_10d: `344`
- completed_20d: `304`
- completed_60d: `144`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `380`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2605`
- primary_path_mean_absolute_error: `0.0101`
- primary_path_median_absolute_error: `0.00826`
- secondary_scenario_hit_rate: `0.3368`
- primary_vs_secondary_accuracy_spread: `-0.0763`
- primary_closer_than_secondary_rate: `0.3632`
- close_call_primary_closer_rate: `0.3401`

### 3d
- completed_count: `372`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2527`
- primary_path_mean_absolute_error: `0.016424`
- primary_path_median_absolute_error: `0.013013`
- secondary_scenario_hit_rate: `0.3011`
- primary_vs_secondary_accuracy_spread: `-0.0484`
- primary_closer_than_secondary_rate: `0.3737`
- close_call_primary_closer_rate: `0.4197`

### 5d
- completed_count: `364`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.261`
- primary_path_mean_absolute_error: `0.022507`
- primary_path_median_absolute_error: `0.018826`
- secondary_scenario_hit_rate: `0.2885`
- primary_vs_secondary_accuracy_spread: `-0.0275`
- primary_closer_than_secondary_rate: `0.3736`
- close_call_primary_closer_rate: `0.3862`

### 10d
- completed_count: `344`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2326`
- primary_path_mean_absolute_error: `0.032866`
- primary_path_median_absolute_error: `0.027871`
- secondary_scenario_hit_rate: `0.3343`
- primary_vs_secondary_accuracy_spread: `-0.1017`
- primary_closer_than_secondary_rate: `0.3256`
- close_call_primary_closer_rate: `0.3404`

### 20d
- completed_count: `304`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1513`
- primary_path_mean_absolute_error: `0.056676`
- primary_path_median_absolute_error: `0.053984`
- secondary_scenario_hit_rate: `0.2796`
- primary_vs_secondary_accuracy_spread: `-0.1283`
- primary_closer_than_secondary_rate: `0.3191`
- close_call_primary_closer_rate: `0.3728`

### 60d
- completed_count: `144`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1181`
- primary_path_mean_absolute_error: `0.07181`
- primary_path_median_absolute_error: `0.065154`
- secondary_scenario_hit_rate: `0.2153`
- primary_vs_secondary_accuracy_spread: `-0.0972`
- primary_closer_than_secondary_rate: `0.4167`
- close_call_primary_closer_rate: `0.5132`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
