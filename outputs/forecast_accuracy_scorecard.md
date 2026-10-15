# Forecast Accuracy Scorecard

Generated at: `2026-10-15T23:11:21.915216+00:00`

## Sample Counts

- total_forecasts: `352`
- raw_forecast_rows: `352`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `348`
- completed_3d: `340`
- completed_5d: `332`
- completed_10d: `312`
- completed_20d: `272`
- completed_60d: `112`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `348`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2586`
- primary_path_mean_absolute_error: `0.010062`
- primary_path_median_absolute_error: `0.00826`
- secondary_scenario_hit_rate: `0.3448`
- primary_vs_secondary_accuracy_spread: `-0.0862`
- primary_closer_than_secondary_rate: `0.3678`
- close_call_primary_closer_rate: `0.3457`

### 3d
- completed_count: `340`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2529`
- primary_path_mean_absolute_error: `0.016343`
- primary_path_median_absolute_error: `0.0129`
- secondary_scenario_hit_rate: `0.3088`
- primary_vs_secondary_accuracy_spread: `-0.0559`
- primary_closer_than_secondary_rate: `0.3824`
- close_call_primary_closer_rate: `0.4194`

### 5d
- completed_count: `332`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2681`
- primary_path_mean_absolute_error: `0.022053`
- primary_path_median_absolute_error: `0.017761`
- secondary_scenario_hit_rate: `0.2892`
- primary_vs_secondary_accuracy_spread: `-0.0211`
- primary_closer_than_secondary_rate: `0.3916`
- close_call_primary_closer_rate: `0.3901`

### 10d
- completed_count: `312`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2276`
- primary_path_mean_absolute_error: `0.032319`
- primary_path_median_absolute_error: `0.027019`
- secondary_scenario_hit_rate: `0.3365`
- primary_vs_secondary_accuracy_spread: `-0.109`
- primary_closer_than_secondary_rate: `0.3173`
- close_call_primary_closer_rate: `0.3333`

### 20d
- completed_count: `272`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1324`
- primary_path_mean_absolute_error: `0.058225`
- primary_path_median_absolute_error: `0.054137`
- secondary_scenario_hit_rate: `0.2868`
- primary_vs_secondary_accuracy_spread: `-0.1544`
- primary_closer_than_secondary_rate: `0.2831`
- close_call_primary_closer_rate: `0.3333`

### 60d
- completed_count: `112`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1339`
- primary_path_mean_absolute_error: `0.07011`
- primary_path_median_absolute_error: `0.055933`
- secondary_scenario_hit_rate: `0.2232`
- primary_vs_secondary_accuracy_spread: `-0.0893`
- primary_closer_than_secondary_rate: `0.4196`
- close_call_primary_closer_rate: `0.5179`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
