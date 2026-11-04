# Forecast Accuracy Scorecard

Generated at: `2026-11-04T11:35:57.080743+00:00`

## Sample Counts

- total_forecasts: `404`
- raw_forecast_rows: `404`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `400`
- completed_3d: `392`
- completed_5d: `384`
- completed_10d: `364`
- completed_20d: `324`
- completed_60d: `164`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `400`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.265`
- primary_path_mean_absolute_error: `0.010086`
- primary_path_median_absolute_error: `0.00826`
- secondary_scenario_hit_rate: `0.335`
- primary_vs_secondary_accuracy_spread: `-0.07`
- primary_closer_than_secondary_rate: `0.37`
- close_call_primary_closer_rate: `0.3476`

### 3d
- completed_count: `392`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2628`
- primary_path_mean_absolute_error: `0.016791`
- primary_path_median_absolute_error: `0.013076`
- secondary_scenario_hit_rate: `0.3061`
- primary_vs_secondary_accuracy_spread: `-0.0434`
- primary_closer_than_secondary_rate: `0.3801`
- close_call_primary_closer_rate: `0.4195`

### 5d
- completed_count: `384`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2578`
- primary_path_mean_absolute_error: `0.022508`
- primary_path_median_absolute_error: `0.018756`
- secondary_scenario_hit_rate: `0.2917`
- primary_vs_secondary_accuracy_spread: `-0.0339`
- primary_closer_than_secondary_rate: `0.3698`
- close_call_primary_closer_rate: `0.38`

### 10d
- completed_count: `364`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2473`
- primary_path_mean_absolute_error: `0.032633`
- primary_path_median_absolute_error: `0.027676`
- secondary_scenario_hit_rate: `0.3242`
- primary_vs_secondary_accuracy_spread: `-0.0769`
- primary_closer_than_secondary_rate: `0.3352`
- close_call_primary_closer_rate: `0.3386`

### 20d
- completed_count: `324`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1605`
- primary_path_mean_absolute_error: `0.056732`
- primary_path_median_absolute_error: `0.054226`
- secondary_scenario_hit_rate: `0.2747`
- primary_vs_secondary_accuracy_spread: `-0.1142`
- primary_closer_than_secondary_rate: `0.3272`
- close_call_primary_closer_rate: `0.3864`

### 60d
- completed_count: `164`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1341`
- primary_path_mean_absolute_error: `0.072423`
- primary_path_median_absolute_error: `0.067287`
- secondary_scenario_hit_rate: `0.2439`
- primary_vs_secondary_accuracy_spread: `-0.1098`
- primary_closer_than_secondary_rate: `0.4024`
- close_call_primary_closer_rate: `0.4839`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
