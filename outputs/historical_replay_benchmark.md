# Historical Replay Benchmark

Generated at: `2026-07-16T06:07:04.842347+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `not_proven_or_mixed`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_mixed_or_not_better_keep_confidence_capped`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.013139`
- secondary_mean_absolute_error: `0.011602`
- primary_error_advantage: `-0.001537`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.019041`
- secondary_mean_absolute_error: `0.015043`
- primary_error_advantage: `-0.003998`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.025494`
- secondary_mean_absolute_error: `0.023405`
- primary_error_advantage: `-0.002089`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.060399`
- secondary_mean_absolute_error: `0.042572`
- primary_error_advantage: `-0.017827`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.067562`
- secondary_mean_absolute_error: `0.073338`
- primary_error_advantage: `0.005776`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.011524`, as_primary `0`, as_primary_hit `None`, avg `-0.000512`, median `0.000463`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.015042`, as_primary `0`, as_primary_hit `None`, avg `0.000889`, median `0.003801`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.020391`, as_primary `0`, as_primary_hit `None`, avg `0.000494`, median `-8e-06`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.030433`, as_primary `0`, as_primary_hit `None`, avg `0.001087`, median `0.007557`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.0643`, as_primary `0`, as_primary_hit `None`, avg `-0.000395`, median `-0.004015`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.011609`, as_primary `20`, as_primary_hit `0.6`, avg `-0.000512`, median `0.000463`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.015259`, as_primary `20`, as_primary_hit `0.55`, avg `0.000889`, median `0.003801`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.024861`, as_primary `20`, as_primary_hit `0.55`, avg `0.000494`, median `-8e-06`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.046202`, as_primary `20`, as_primary_hit `0.65`, avg `0.001087`, median `0.007557`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.073215`, as_primary `20`, as_primary_hit `0.6`, avg `-0.000395`, median `-0.004015`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.013198`, as_primary `60`, as_primary_hit `0.5`, avg `-0.000512`, median `0.000463`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.019059`, as_primary `60`, as_primary_hit `0.6167`, avg `0.000889`, median `0.003801`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.025523`, as_primary `60`, as_primary_hit `0.4833`, avg `0.000494`, median `-8e-06`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.062135`, as_primary `60`, as_primary_hit `0.6167`, avg `0.001087`, median `0.007557`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.072752`, as_primary `60`, as_primary_hit `0.4333`, avg `-0.000395`, median `-0.004015`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.011707`, as_primary `0`, as_primary_hit `None`, avg `-0.000512`, median `0.000463`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.01489`, as_primary `0`, as_primary_hit `None`, avg `0.000889`, median `0.003801`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.019856`, as_primary `0`, as_primary_hit `None`, avg `0.000494`, median `-8e-06`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.030784`, as_primary `0`, as_primary_hit `None`, avg `0.001087`, median `0.007557`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.061867`, as_primary `0`, as_primary_hit `None`, avg `-0.000395`, median `-0.004015`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.008637`, avg `0.003782`, median `0.002975`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.014094`, avg `0.006578`, median `0.006047`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.029141`, avg `0.003347`, median `0.002929`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.045771`, avg `0.001503`, median `0.009961`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.067562`, avg `0.017648`, median `0.046764`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.01464`, avg `-0.001943`, median `-0.000483`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.3667`, primary_mae `0.02069`, avg `-0.001008`, median `0.00337`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.5167`, primary_mae `0.024279`, avg `-0.000457`, median `-0.000945`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.3167`, primary_mae `0.065276`, avg `0.000949`, median `0.003951`
- 60d: sample `60`, primary_hit `0.5667`, primary_closer `0.5833`, primary_mae `0.067563`, avg `-0.006409`, median `-0.008836`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.015386`, avg `-0.004481`, median `-0.004035`
- 5d: sample `40`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.021627`, avg `-0.000712`, median `0.00337`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.02119`, avg `-0.00247`, median `-0.002374`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.056882`, avg `0.00127`, median `0.00675`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.575`, primary_mae `0.074196`, avg `-0.013486`, median `-0.03052`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.010893`, avg `0.003457`, median `0.00544`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.016455`, avg `0.002489`, median `0.005308`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.029799`, avg `0.003459`, median `0.004339`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.225`, primary_mae `0.063917`, avg `0.000905`, median `0.007557`
- 60d: sample `40`, primary_hit `0.525`, primary_closer `0.575`, primary_mae `0.060929`, avg `0.012697`, median `0.015994`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.010893, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.016455, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.02119, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.056882, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.060929, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011524, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013198, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.010893, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01489, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019059, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.016455, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019856, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025523, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.02119, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030433, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062135, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.056882, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061867, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073215, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.060929, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.007152`, avg `0.005437`, median `0.003333`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.013112`, avg `0.003605`, median `0.00286`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.036095`, avg `-0.007875`, median `-0.013851`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.056891`, avg `-0.005878`, median `-0.005931`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.068554`, avg `0.01802`, median `0.056385`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.007747`, avg `0.004033`, median `0.002975`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.014065`, avg `0.00339`, median `0.002795`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.031216`, avg `-0.002855`, median `-0.00151`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.1875`, primary_mae `0.049351`, avg `-0.001366`, median `0.00878`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.075799`, avg `-0.000112`, median `-0.003306`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.022589`, avg `-0.004852`, median `-0.002198`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.1875`, primary_mae `0.031726`, avg `-0.002152`, median `0.00171`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.031318`, avg `-0.001966`, median `-0.005041`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.081858`, avg `0.00573`, median `0.014663`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.103168`, avg `-0.001441`, median `-0.017896`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.013139`, avg `-0.000512`, median `0.000463`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.019041`, avg `0.000889`, median `0.003801`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.025494`, avg `0.000494`, median `-8e-06`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.3125`, primary_mae `0.060399`, avg `0.001087`, median `0.007557`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.575`, primary_mae `0.067562`, avg `-0.000395`, median `-0.004015`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.013139`, avg `-0.000512`, median `0.000463`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.019041`, avg `0.000889`, median `0.003801`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.025494`, avg `0.000494`, median `-8e-06`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.3125`, primary_mae `0.060399`, avg `0.001087`, median `0.007557`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.575`, primary_mae `0.067562`, avg `-0.000395`, median `-0.004015`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.010893`, avg `0.003457`, median `0.00544`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.016455`, avg `0.002489`, median `0.005308`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.029799`, avg `0.003459`, median `0.004339`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.225`, primary_mae `0.063917`, avg `0.000905`, median `0.007557`
- 60d: sample `40`, primary_hit `0.525`, primary_closer `0.575`, primary_mae `0.060929`, avg `0.012697`, median `0.015994`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.01464`, avg `-0.001943`, median `-0.000483`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.3667`, primary_mae `0.02069`, avg `-0.001008`, median `0.00337`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.5167`, primary_mae `0.024279`, avg `-0.000457`, median `-0.000945`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.3167`, primary_mae `0.065276`, avg `0.000949`, median `0.003951`
- 60d: sample `60`, primary_hit `0.5667`, primary_closer `0.5833`, primary_mae `0.067563`, avg `-0.006409`, median `-0.008836`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.013139`, avg `-0.000512`, median `0.000463`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.019041`, avg `0.000889`, median `0.003801`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.025494`, avg `0.000494`, median `-8e-06`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.3125`, primary_mae `0.060399`, avg `0.001087`, median `0.007557`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.575`, primary_mae `0.067562`, avg `-0.000395`, median `-0.004015`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

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
