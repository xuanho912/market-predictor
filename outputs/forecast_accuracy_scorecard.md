# Forecast Accuracy Scorecard

Generated at: `2026-10-21T08:54:27.826811+00:00`

## Sample Counts

- total_forecasts: `364`
- raw_forecast_rows: `364`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `360`
- completed_3d: `352`
- completed_5d: `344`
- completed_10d: `324`
- completed_20d: `284`
- completed_60d: `124`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `360`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2556`
- primary_path_mean_absolute_error: `0.010203`
- primary_path_median_absolute_error: `0.008451`
- secondary_scenario_hit_rate: `0.3389`
- primary_vs_secondary_accuracy_spread: `-0.0833`
- primary_closer_than_secondary_rate: `0.3611`
- close_call_primary_closer_rate: `0.3439`

### 3d
- completed_count: `352`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.25`
- primary_path_mean_absolute_error: `0.016362`
- primary_path_median_absolute_error: `0.0129`
- secondary_scenario_hit_rate: `0.304`
- primary_vs_secondary_accuracy_spread: `-0.054`
- primary_closer_than_secondary_rate: `0.3778`
- close_call_primary_closer_rate: `0.4233`

### 5d
- completed_count: `344`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2645`
- primary_path_mean_absolute_error: `0.022304`
- primary_path_median_absolute_error: `0.018502`
- secondary_scenario_hit_rate: `0.2936`
- primary_vs_secondary_accuracy_spread: `-0.0291`
- primary_closer_than_secondary_rate: `0.3837`
- close_call_primary_closer_rate: `0.383`

### 10d
- completed_count: `324`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2346`
- primary_path_mean_absolute_error: `0.03281`
- primary_path_median_absolute_error: `0.027676`
- secondary_scenario_hit_rate: `0.3364`
- primary_vs_secondary_accuracy_spread: `-0.1019`
- primary_closer_than_secondary_rate: `0.321`
- close_call_primary_closer_rate: `0.3352`

### 20d
- completed_count: `284`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1408`
- primary_path_mean_absolute_error: `0.057514`
- primary_path_median_absolute_error: `0.053802`
- secondary_scenario_hit_rate: `0.2817`
- primary_vs_secondary_accuracy_spread: `-0.1408`
- primary_closer_than_secondary_rate: `0.3028`
- close_call_primary_closer_rate: `0.3478`

### 60d
- completed_count: `124`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.121`
- primary_path_mean_absolute_error: `0.070743`
- primary_path_median_absolute_error: `0.061834`
- secondary_scenario_hit_rate: `0.2097`
- primary_vs_secondary_accuracy_spread: `-0.0887`
- primary_closer_than_secondary_rate: `0.4194`
- close_call_primary_closer_rate: `0.5238`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
