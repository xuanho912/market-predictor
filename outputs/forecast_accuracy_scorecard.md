# Forecast Accuracy Scorecard

Generated at: `2026-09-02T08:10:01.321536+00:00`

## Sample Counts

- total_forecasts: `228`
- raw_forecast_rows: `228`
- deduped_legacy_rows: `0`
- pending_forecasts: `228`
- completed_1d: `222`
- completed_3d: `214`
- completed_5d: `206`
- completed_10d: `186`
- completed_20d: `146`
- completed_60d: `0`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `222`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2973`
- primary_path_mean_absolute_error: `0.009898`
- primary_path_median_absolute_error: `0.007623`
- secondary_scenario_hit_rate: `0.3243`
- primary_vs_secondary_accuracy_spread: `-0.027`
- primary_closer_than_secondary_rate: `0.4234`
- close_call_primary_closer_rate: `0.3556`

### 3d
- completed_count: `214`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2383`
- primary_path_mean_absolute_error: `0.016266`
- primary_path_median_absolute_error: `0.012757`
- secondary_scenario_hit_rate: `0.3505`
- primary_vs_secondary_accuracy_spread: `-0.1121`
- primary_closer_than_secondary_rate: `0.3879`
- close_call_primary_closer_rate: `0.4173`

### 5d
- completed_count: `206`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2233`
- primary_path_mean_absolute_error: `0.023086`
- primary_path_median_absolute_error: `0.018502`
- secondary_scenario_hit_rate: `0.301`
- primary_vs_secondary_accuracy_spread: `-0.0777`
- primary_closer_than_secondary_rate: `0.3932`
- close_call_primary_closer_rate: `0.3697`

### 10d
- completed_count: `186`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2097`
- primary_path_mean_absolute_error: `0.034419`
- primary_path_median_absolute_error: `0.027996`
- secondary_scenario_hit_rate: `0.3387`
- primary_vs_secondary_accuracy_spread: `-0.129`
- primary_closer_than_secondary_rate: `0.3065`
- close_call_primary_closer_rate: `0.2692`

### 20d
- completed_count: `146`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1164`
- primary_path_mean_absolute_error: `0.059222`
- primary_path_median_absolute_error: `0.058866`
- secondary_scenario_hit_rate: `0.2808`
- primary_vs_secondary_accuracy_spread: `-0.1644`
- primary_closer_than_secondary_rate: `0.2671`
- close_call_primary_closer_rate: `0.2785`

### 60d
- completed_count: `0`
- sample_gate: `insufficient_samples`
- primary_scenario_hit_rate: `None`
- primary_path_mean_absolute_error: `None`
- primary_path_median_absolute_error: `None`
- secondary_scenario_hit_rate: `None`
- primary_vs_secondary_accuracy_spread: `None`
- primary_closer_than_secondary_rate: `None`
- close_call_primary_closer_rate: `None`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `insufficient_samples_for_high_confidence_validation`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
