# Forecast Accuracy Scorecard

Generated at: `2026-09-17T06:13:13.849175+00:00`

## Sample Counts

- total_forecasts: `268`
- raw_forecast_rows: `268`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `264`
- completed_3d: `256`
- completed_5d: `248`
- completed_10d: `228`
- completed_20d: `188`
- completed_60d: `28`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `264`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2841`
- primary_path_mean_absolute_error: `0.009763`
- primary_path_median_absolute_error: `0.007709`
- secondary_scenario_hit_rate: `0.3371`
- primary_vs_secondary_accuracy_spread: `-0.053`
- primary_closer_than_secondary_rate: `0.4053`
- close_call_primary_closer_rate: `0.351`

### 3d
- completed_count: `256`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2656`
- primary_path_mean_absolute_error: `0.015636`
- primary_path_median_absolute_error: `0.012091`
- secondary_scenario_hit_rate: `0.3359`
- primary_vs_secondary_accuracy_spread: `-0.0703`
- primary_closer_than_secondary_rate: `0.3984`
- close_call_primary_closer_rate: `0.4238`

### 5d
- completed_count: `248`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2863`
- primary_path_mean_absolute_error: `0.021192`
- primary_path_median_absolute_error: `0.014773`
- secondary_scenario_hit_rate: `0.2863`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4315`
- close_call_primary_closer_rate: `0.4`

### 10d
- completed_count: `228`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2193`
- primary_path_mean_absolute_error: `0.03407`
- primary_path_median_absolute_error: `0.027871`
- secondary_scenario_hit_rate: `0.3465`
- primary_vs_secondary_accuracy_spread: `-0.1272`
- primary_closer_than_secondary_rate: `0.3246`
- close_call_primary_closer_rate: `0.3191`

### 20d
- completed_count: `188`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1064`
- primary_path_mean_absolute_error: `0.061569`
- primary_path_median_absolute_error: `0.059096`
- secondary_scenario_hit_rate: `0.2979`
- primary_vs_secondary_accuracy_spread: `-0.1915`
- primary_closer_than_secondary_rate: `0.2394`
- close_call_primary_closer_rate: `0.2571`

### 60d
- completed_count: `28`
- sample_gate: `early_evidence`
- primary_scenario_hit_rate: `0.1071`
- primary_path_mean_absolute_error: `0.064184`
- primary_path_median_absolute_error: `0.051247`
- secondary_scenario_hit_rate: `0.1429`
- primary_vs_secondary_accuracy_spread: `-0.0357`
- primary_closer_than_secondary_rate: `0.3929`
- close_call_primary_closer_rate: `0.6667`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
