# Forecast Accuracy Scorecard

Generated at: `2026-09-29T00:40:35.025316+00:00`

## Sample Counts

- total_forecasts: `300`
- raw_forecast_rows: `300`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `296`
- completed_3d: `288`
- completed_5d: `280`
- completed_10d: `260`
- completed_20d: `220`
- completed_60d: `60`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `296`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2703`
- primary_path_mean_absolute_error: `0.010085`
- primary_path_median_absolute_error: `0.007936`
- secondary_scenario_hit_rate: `0.3412`
- primary_vs_secondary_accuracy_spread: `-0.0709`
- primary_closer_than_secondary_rate: `0.3885`
- close_call_primary_closer_rate: `0.3512`

### 3d
- completed_count: `288`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2604`
- primary_path_mean_absolute_error: `0.016186`
- primary_path_median_absolute_error: `0.012624`
- secondary_scenario_hit_rate: `0.3229`
- primary_vs_secondary_accuracy_spread: `-0.0625`
- primary_closer_than_secondary_rate: `0.3924`
- close_call_primary_closer_rate: `0.4242`

### 5d
- completed_count: `280`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.275`
- primary_path_mean_absolute_error: `0.021933`
- primary_path_median_absolute_error: `0.016339`
- secondary_scenario_hit_rate: `0.2857`
- primary_vs_secondary_accuracy_spread: `-0.0107`
- primary_closer_than_secondary_rate: `0.4036`
- close_call_primary_closer_rate: `0.3861`

### 10d
- completed_count: `260`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2346`
- primary_path_mean_absolute_error: `0.03287`
- primary_path_median_absolute_error: `0.027019`
- secondary_scenario_hit_rate: `0.3308`
- primary_vs_secondary_accuracy_spread: `-0.0962`
- primary_closer_than_secondary_rate: `0.3308`
- close_call_primary_closer_rate: `0.3311`

### 20d
- completed_count: `220`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1182`
- primary_path_mean_absolute_error: `0.061141`
- primary_path_median_absolute_error: `0.058348`
- secondary_scenario_hit_rate: `0.2909`
- primary_vs_secondary_accuracy_spread: `-0.1727`
- primary_closer_than_secondary_rate: `0.2636`
- close_call_primary_closer_rate: `0.2932`

### 60d
- completed_count: `60`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1`
- primary_path_mean_absolute_error: `0.072977`
- primary_path_median_absolute_error: `0.051247`
- secondary_scenario_hit_rate: `0.2333`
- primary_vs_secondary_accuracy_spread: `-0.1333`
- primary_closer_than_secondary_rate: `0.4333`
- close_call_primary_closer_rate: `0.4194`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
