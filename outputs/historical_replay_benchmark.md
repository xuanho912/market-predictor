# Historical Replay Benchmark

Generated at: `2026-08-20T21:58:27.024366+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `not_proven_or_mixed`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_supportive_but_not_forward_validated`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.019764`
- secondary_mean_absolute_error: `0.015017`
- primary_error_advantage: `-0.004747`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.0221`
- secondary_mean_absolute_error: `0.019045`
- primary_error_advantage: `-0.003055`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.039603`
- secondary_mean_absolute_error: `0.031057`
- primary_error_advantage: `-0.008546`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.078591`
- secondary_mean_absolute_error: `0.056511`
- primary_error_advantage: `-0.02208`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.078228`
- secondary_mean_absolute_error: `0.07189`
- primary_error_advantage: `-0.006338`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.013767`, as_primary `0`, as_primary_hit `None`, avg `0.003395`, median `0.005581`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.019113`, as_primary `0`, as_primary_hit `None`, avg `0.004154`, median `0.003922`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.02649`, as_primary `0`, as_primary_hit `None`, avg `0.003502`, median `0.002128`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.045049`, as_primary `0`, as_primary_hit `None`, avg `0.007305`, median `0.010234`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.062305`, as_primary `0`, as_primary_hit `None`, avg `0.022992`, median `0.032298`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.017327`, as_primary `0`, as_primary_hit `None`, avg `0.003395`, median `0.005581`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.024116`, as_primary `0`, as_primary_hit `None`, avg `0.004154`, median `0.003922`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.036666`, as_primary `0`, as_primary_hit `None`, avg `0.003502`, median `0.002128`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.070661`, as_primary `0`, as_primary_hit `None`, avg `0.007305`, median `0.010234`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.080151`, as_primary `0`, as_primary_hit `None`, avg `0.022992`, median `0.032298`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.35`, path_mae `0.019764`, as_primary `80`, as_primary_hit `0.65`, avg `0.003395`, median `0.005581`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.0221`, as_primary `80`, as_primary_hit `0.65`, avg `0.004154`, median `0.003922`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.039603`, as_primary `80`, as_primary_hit `0.5125`, avg `0.003502`, median `0.002128`
- 20d: sample `80`, direction_hit `0.4`, path_mae `0.078591`, as_primary `80`, as_primary_hit `0.6`, avg `0.007305`, median `0.010234`
- 60d: sample `80`, direction_hit `0.4125`, path_mae `0.078228`, as_primary `80`, as_primary_hit `0.5875`, avg `0.022992`, median `0.032298`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.013632`, as_primary `0`, as_primary_hit `None`, avg `0.003395`, median `0.005581`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.016923`, as_primary `0`, as_primary_hit `None`, avg `0.004154`, median `0.003922`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.025634`, as_primary `0`, as_primary_hit `None`, avg `0.003502`, median `0.002128`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.041265`, as_primary `0`, as_primary_hit `None`, avg `0.007305`, median `0.010234`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.060352`, as_primary `0`, as_primary_hit `None`, avg `0.022992`, median `0.032298`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.019764`, avg `0.003395`, median `0.005581`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.0221`, avg `0.004154`, median `0.003922`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.039603`, avg `0.003502`, median `0.002128`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.078591`, avg `0.007305`, median `0.010234`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.45`, primary_mae `0.078228`, avg `0.022992`, median `0.032298`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.013973`, avg `-0.000616`, median `0.000402`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.013012`, avg `0.000473`, median `0.001088`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.021238`, avg `-0.011627`, median `-0.014927`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.05491`, avg `-0.018988`, median `-0.015662`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.066999`, avg `-0.015176`, median `-0.030547`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3333`, primary_closer `0.3833`, primary_mae `0.021694`, avg `0.004732`, median `0.007972`
- 5d: sample `60`, primary_hit `0.35`, primary_closer `0.4833`, primary_mae `0.025129`, avg `0.005381`, median `0.004966`
- 10d: sample `60`, primary_hit `0.4`, primary_closer `0.4333`, primary_mae `0.045725`, avg `0.008545`, median `0.011297`
- 20d: sample `60`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.086485`, avg `0.01607`, median `0.015268`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.4167`, primary_mae `0.081971`, avg `0.035714`, median `0.049838`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013973, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.013012, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.021238, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.05491, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.066999, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013632, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019764, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013973, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016923, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024116, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.013012, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025634, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039603, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.021238, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041265, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.078591, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.05491, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060352, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.080151, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.066999, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.024449`, avg `-0.001457`, median `-0.000883`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.75`, primary_mae `0.015438`, avg `-3e-05`, median `0.003509`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.01945`, avg `0.00654`, median `0.011059`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.060431`, avg `0.016255`, median `0.014663`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.75`, primary_mae `0.039852`, avg `-0.002876`, median `-0.025539`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.027536`, avg `-0.002788`, median `0.002617`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.021533`, avg `0.001526`, median `0.003509`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.02536`, avg `0.00676`, median `0.011059`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.063648`, avg `0.011268`, median `0.02136`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.064522`, avg `0.013195`, median `-0.004019`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.023694`, avg `0.009217`, median `0.010987`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.031479`, avg `0.003414`, median `-0.005981`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.060623`, avg `0.019106`, median `0.016311`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.110577`, avg `0.044186`, median `0.022139`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.375`, primary_mae `0.088452`, avg `0.076044`, median `0.072312`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.019764`, avg `0.003395`, median `0.005581`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.0221`, avg `0.004154`, median `0.003922`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.039603`, avg `0.003502`, median `0.002128`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.078591`, avg `0.007305`, median `0.010234`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.45`, primary_mae `0.078228`, avg `0.022992`, median `0.032298`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.019764`, avg `0.003395`, median `0.005581`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.0221`, avg `0.004154`, median `0.003922`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.039603`, avg `0.003502`, median `0.002128`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.078591`, avg `0.007305`, median `0.010234`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.45`, primary_mae `0.078228`, avg `0.022992`, median `0.032298`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.020622`, avg `-0.001239`, median `0.000684`
- 5d: sample `40`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.017035`, avg `0.001754`, median `0.00235`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.023349`, avg `-0.001952`, median `-0.007304`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.060137`, avg `-0.002182`, median `0.003008`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.067837`, avg `-0.002188`, median `-0.020541`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.025497`, avg `0.001986`, median `0.004683`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.026888`, avg `0.002666`, median `0.002329`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.425`, primary_mae `0.04263`, avg `0.011034`, median `0.013756`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.082212`, avg `0.023421`, median `0.017664`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.475`, primary_mae `0.076388`, avg `0.041263`, median `0.040689`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.019764`, avg `0.003395`, median `0.005581`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.0221`, avg `0.004154`, median `0.003922`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.039603`, avg `0.003502`, median `0.002128`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.078591`, avg `0.007305`, median `0.010234`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.45`, primary_mae `0.078228`, avg `0.022992`, median `0.032298`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.019764`, avg `0.003395`, median `0.005581`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.0221`, avg `0.004154`, median `0.003922`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.039603`, avg `0.003502`, median `0.002128`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.078591`, avg `0.007305`, median `0.010234`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.45`, primary_mae `0.078228`, avg `0.022992`, median `0.032298`

### flow_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
