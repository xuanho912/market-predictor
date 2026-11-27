# Forecast Accuracy Scorecard

Generated at: `2026-11-27T04:57:53.958069+00:00`

## Sample Counts

- total_forecasts: `468`
- raw_forecast_rows: `468`
- deduped_legacy_rows: `0`
- pending_forecasts: `240`
- completed_1d: `464`
- completed_3d: `456`
- completed_5d: `448`
- completed_10d: `428`
- completed_20d: `388`
- completed_60d: `228`
- current_evidence_level: `stronger_evidence`
- validation_warning: Forward validation evidence is accumulating; do not promote models without horizon-specific proof.

## Primary Scenario Accuracy

### 1d
- completed_count: `464`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2759`
- primary_path_mean_absolute_error: `0.011396`
- primary_path_median_absolute_error: `0.009117`
- secondary_scenario_hit_rate: `0.3297`
- primary_vs_secondary_accuracy_spread: `-0.0539`
- primary_closer_than_secondary_rate: `0.3772`
- close_call_primary_closer_rate: `0.3478`

### 3d
- completed_count: `456`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2785`
- primary_path_mean_absolute_error: `0.018722`
- primary_path_median_absolute_error: `0.013985`
- secondary_scenario_hit_rate: `0.3114`
- primary_vs_secondary_accuracy_spread: `-0.0329`
- primary_closer_than_secondary_rate: `0.3925`
- close_call_primary_closer_rate: `0.4323`

### 5d
- completed_count: `448`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2746`
- primary_path_mean_absolute_error: `0.025054`
- primary_path_median_absolute_error: `0.019919`
- secondary_scenario_hit_rate: `0.3013`
- primary_vs_secondary_accuracy_spread: `-0.0268`
- primary_closer_than_secondary_rate: `0.3795`
- close_call_primary_closer_rate: `0.3799`

### 10d
- completed_count: `428`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2874`
- primary_path_mean_absolute_error: `0.033805`
- primary_path_median_absolute_error: `0.028396`
- secondary_scenario_hit_rate: `0.3084`
- primary_vs_secondary_accuracy_spread: `-0.021`
- primary_closer_than_secondary_rate: `0.3738`
- close_call_primary_closer_rate: `0.3408`

### 20d
- completed_count: `388`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.2242`
- primary_path_mean_absolute_error: `0.057051`
- primary_path_median_absolute_error: `0.054073`
- secondary_scenario_hit_rate: `0.2655`
- primary_vs_secondary_accuracy_spread: `-0.0412`
- primary_closer_than_secondary_rate: `0.3763`
- close_call_primary_closer_rate: `0.399`

### 60d
- completed_count: `228`
- sample_gate: `stronger_evidence`
- primary_scenario_hit_rate: `0.1842`
- primary_path_mean_absolute_error: `0.082649`
- primary_path_median_absolute_error: `0.073168`
- secondary_scenario_hit_rate: `0.2368`
- primary_vs_secondary_accuracy_spread: `-0.0526`
- primary_closer_than_secondary_rate: `0.3904`
- close_call_primary_closer_rate: `0.4539`

## Core Questions

- edge_vs_no_edge: `moderate_or_strong_edge_not_better_than_no_edge_keep_confidence_capped`
- high_confidence_better: `high_confidence_not_better_than_all_samples_keep_confidence_capped`
- primary_beats_secondary: `primary_path_not_better_than_secondary`

## Guardrails

- This validates forecast accuracy, not paper trading, PnL or execution.
- Alpha v1 remains a research forecast input with frozen threshold 0.32534311.
