# Forecast Accuracy Scorecard

Generated at: `2026-09-24T23:18:09.644623+00:00`

## Sample Counts

- total_forecasts: `292`
- raw_forecast_rows: `292`
- deduped_legacy_rows: `0`
- pending_forecasts: `241`
- completed_1d: `286`
- completed_3d: `279`
- completed_5d: `271`
- completed_10d: `251`
- completed_20d: `211`
- completed_60d: `51`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `286`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2727`
- primary_path_mean_absolute_error: `0.010026`
- primary_path_median_absolute_error: `0.007877`
- secondary_scenario_hit_rate: `0.3392`
- primary_vs_secondary_accuracy_spread: `-0.0664`
- primary_closer_than_secondary_rate: `0.3916`
- close_call_primary_closer_rate: `0.3497`

### 3d
- completed_count: `279`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2545`
- primary_path_mean_absolute_error: `0.016382`
- primary_path_median_absolute_error: `0.012774`
- secondary_scenario_hit_rate: `0.3226`
- primary_vs_secondary_accuracy_spread: `-0.0681`
- primary_closer_than_secondary_rate: `0.3871`
- close_call_primary_closer_rate: `0.4204`

### 5d
- completed_count: `271`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2841`
- primary_path_mean_absolute_error: `0.021906`
- primary_path_median_absolute_error: `0.016236`
- secondary_scenario_hit_rate: `0.2804`
- primary_vs_secondary_accuracy_spread: `0.0037`
- primary_closer_than_secondary_rate: `0.417`
- close_call_primary_closer_rate: `0.3987`

### 10d
- completed_count: `251`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.239`
- primary_path_mean_absolute_error: `0.03315`
- primary_path_median_absolute_error: `0.02761`
- secondary_scenario_hit_rate: `0.3307`
- primary_vs_secondary_accuracy_spread: `-0.0916`
- primary_closer_than_secondary_rate: `0.3347`
- close_call_primary_closer_rate: `0.3333`

### 20d
- completed_count: `211`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1185`
- primary_path_mean_absolute_error: `0.061218`
- primary_path_median_absolute_error: `0.058598`
- secondary_scenario_hit_rate: `0.2938`
- primary_vs_secondary_accuracy_spread: `-0.1754`
- primary_closer_than_secondary_rate: `0.2607`
- close_call_primary_closer_rate: `0.2903`

### 60d
- completed_count: `51`
- sample_gate: `moderate_evidence`
- primary_scenario_hit_rate: `0.1176`
- primary_path_mean_absolute_error: `0.071802`
- primary_path_median_absolute_error: `0.051247`
- secondary_scenario_hit_rate: `0.2157`
- primary_vs_secondary_accuracy_spread: `-0.098`
- primary_closer_than_secondary_rate: `0.3922`
- close_call_primary_closer_rate: `0.4`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_has_early_advantage_but_requires_more_samples`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
