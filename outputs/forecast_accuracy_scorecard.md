# Forecast Accuracy Scorecard

Generated at: `2026-10-30T10:29:53.446899+00:00`

## Sample Counts

- total_forecasts: `392`
- raw_forecast_rows: `392`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `388`
- completed_3d: `380`
- completed_5d: `372`
- completed_10d: `352`
- completed_20d: `312`
- completed_60d: `152`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `388`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2655`
- primary_path_mean_absolute_error: `0.010002`
- primary_path_median_absolute_error: `0.008075`
- secondary_scenario_hit_rate: `0.3351`
- primary_vs_secondary_accuracy_spread: `-0.0696`
- primary_closer_than_secondary_rate: `0.3686`
- close_call_primary_closer_rate: `0.3448`

### 3d
- completed_count: `380`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2605`
- primary_path_mean_absolute_error: `0.016369`
- primary_path_median_absolute_error: `0.0129`
- secondary_scenario_hit_rate: `0.2974`
- primary_vs_secondary_accuracy_spread: `-0.0368`
- primary_closer_than_secondary_rate: `0.3816`
- close_call_primary_closer_rate: `0.4264`

### 5d
- completed_count: `372`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2608`
- primary_path_mean_absolute_error: `0.022438`
- primary_path_median_absolute_error: `0.018826`
- secondary_scenario_hit_rate: `0.2903`
- primary_vs_secondary_accuracy_spread: `-0.0296`
- primary_closer_than_secondary_rate: `0.3737`
- close_call_primary_closer_rate: `0.3834`

### 10d
- completed_count: `352`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2301`
- primary_path_mean_absolute_error: `0.032892`
- primary_path_median_absolute_error: `0.027871`
- secondary_scenario_hit_rate: `0.3324`
- primary_vs_secondary_accuracy_spread: `-0.1023`
- primary_closer_than_secondary_rate: `0.321`
- close_call_primary_closer_rate: `0.3386`

### 20d
- completed_count: `312`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1571`
- primary_path_mean_absolute_error: `0.056557`
- primary_path_median_absolute_error: `0.053984`
- secondary_scenario_hit_rate: `0.2788`
- primary_vs_secondary_accuracy_spread: `-0.1218`
- primary_closer_than_secondary_rate: `0.3205`
- close_call_primary_closer_rate: `0.3743`

### 60d
- completed_count: `152`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1184`
- primary_path_mean_absolute_error: `0.071978`
- primary_path_median_absolute_error: `0.06665`
- secondary_scenario_hit_rate: `0.2303`
- primary_vs_secondary_accuracy_spread: `-0.1118`
- primary_closer_than_secondary_rate: `0.4079`
- close_call_primary_closer_rate: `0.4881`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
