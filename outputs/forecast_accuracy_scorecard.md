# Forecast Accuracy Scorecard

Generated at: `2026-11-18T03:57:33.504135+00:00`

## Sample Counts

- total_forecasts: `444`
- raw_forecast_rows: `444`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `440`
- completed_3d: `432`
- completed_5d: `424`
- completed_10d: `404`
- completed_20d: `364`
- completed_60d: `204`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `440`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2659`
- primary_path_mean_absolute_error: `0.010829`
- primary_path_median_absolute_error: `0.008819`
- secondary_scenario_hit_rate: `0.3409`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.3705`
- close_call_primary_closer_rate: `0.3493`

### 3d
- completed_count: `432`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2731`
- primary_path_mean_absolute_error: `0.017693`
- primary_path_median_absolute_error: `0.013375`
- secondary_scenario_hit_rate: `0.3125`
- primary_vs_secondary_accuracy_spread: `-0.0394`
- primary_closer_than_secondary_rate: `0.3889`
- close_call_primary_closer_rate: `0.4286`

### 5d
- completed_count: `424`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2594`
- primary_path_mean_absolute_error: `0.023809`
- primary_path_median_absolute_error: `0.019727`
- secondary_scenario_hit_rate: `0.3042`
- primary_vs_secondary_accuracy_spread: `-0.0448`
- primary_closer_than_secondary_rate: `0.3703`
- close_call_primary_closer_rate: `0.3773`

### 10d
- completed_count: `404`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2698`
- primary_path_mean_absolute_error: `0.032646`
- primary_path_median_absolute_error: `0.027871`
- secondary_scenario_hit_rate: `0.3094`
- primary_vs_secondary_accuracy_spread: `-0.0396`
- primary_closer_than_secondary_rate: `0.3614`
- close_call_primary_closer_rate: `0.3491`

### 20d
- completed_count: `364`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1951`
- primary_path_mean_absolute_error: `0.056252`
- primary_path_median_absolute_error: `0.053984`
- secondary_scenario_hit_rate: `0.2692`
- primary_vs_secondary_accuracy_spread: `-0.0742`
- primary_closer_than_secondary_rate: `0.3544`
- close_call_primary_closer_rate: `0.3915`

### 60d
- completed_count: `204`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.152`
- primary_path_mean_absolute_error: `0.078101`
- primary_path_median_absolute_error: `0.070011`
- secondary_scenario_hit_rate: `0.2304`
- primary_vs_secondary_accuracy_spread: `-0.0784`
- primary_closer_than_secondary_rate: `0.3824`
- close_call_primary_closer_rate: `0.453`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_not_better_than_no_edge_keep_confidence_capped`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
