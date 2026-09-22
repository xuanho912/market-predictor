# Historical Replay Benchmark

Generated at: `2026-09-22T08:50:09.785973+00:00`
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
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.014542`
- secondary_mean_absolute_error: `0.014891`
- primary_error_advantage: `0.000349`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.017512`
- secondary_mean_absolute_error: `0.018185`
- primary_error_advantage: `0.000673`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.3375`
- primary_vs_secondary_accuracy_spread: `0.325`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.0197`
- secondary_mean_absolute_error: `0.019487`
- primary_error_advantage: `-0.000213`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.059691`
- secondary_mean_absolute_error: `0.050542`
- primary_error_advantage: `-0.009149`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.088711`
- secondary_mean_absolute_error: `0.068375`
- primary_error_advantage: `-0.020336`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.014081`, as_primary `0`, as_primary_hit `None`, avg `-0.005659`, median `-0.004464`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.017285`, as_primary `0`, as_primary_hit `None`, avg `-0.010323`, median `-0.009891`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.018964`, as_primary `0`, as_primary_hit `None`, avg `-0.010307`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.037148`, as_primary `0`, as_primary_hit `None`, avg `0.008677`, median `0.011176`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.061634`, as_primary `0`, as_primary_hit `None`, avg `0.029175`, median `0.044101`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.014865`, as_primary `0`, as_primary_hit `None`, avg `-0.005659`, median `-0.004464`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.019153`, as_primary `0`, as_primary_hit `None`, avg `-0.010323`, median `-0.009891`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.023578`, as_primary `0`, as_primary_hit `None`, avg `-0.010307`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.057975`, as_primary `0`, as_primary_hit `None`, avg `0.008677`, median `0.011176`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.073801`, as_primary `0`, as_primary_hit `None`, avg `0.029175`, median `0.044101`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.014542`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.005659`, median `-0.004464`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.017512`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.010323`, median `-0.009891`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.0197`, as_primary `80`, as_primary_hit `0.3375`, avg `-0.010307`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.45`, path_mae `0.059691`, as_primary `80`, as_primary_hit `0.55`, avg `0.008677`, median `0.011176`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.088711`, as_primary `80`, as_primary_hit `0.725`, avg `0.029175`, median `0.044101`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.013839`, as_primary `0`, as_primary_hit `None`, avg `-0.005659`, median `-0.004464`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.016148`, as_primary `0`, as_primary_hit `None`, avg `-0.010323`, median `-0.009891`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.016956`, as_primary `0`, as_primary_hit `None`, avg `-0.010307`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.035608`, as_primary `0`, as_primary_hit `None`, avg `0.008677`, median `0.011176`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.059806`, as_primary `0`, as_primary_hit `None`, avg `0.029175`, median `0.044101`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.014542`, avg `-0.005659`, median `-0.004464`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4875`, primary_mae `0.017512`, avg `-0.010323`, median `-0.009891`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.4875`, primary_mae `0.0197`, avg `-0.010307`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.059691`, avg `0.008677`, median `0.011176`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.088711`, avg `0.029175`, median `0.044101`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.013493`, avg `0.004966`, median `0.010429`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.016144`, avg `0.000366`, median `0.001988`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.020125`, avg `0.005299`, median `0.003334`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.2`, primary_mae `0.052905`, avg `0.016588`, median `0.01199`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.045192`, avg `0.031143`, median `0.029695`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.8`, primary_closer `0.45`, primary_mae `0.010988`, avg `-0.010554`, median `-0.009953`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.017411`, avg `-0.018657`, median `-0.021882`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.45`, primary_mae `0.021339`, avg `-0.030954`, median `-0.035238`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.079499`, avg `-0.004843`, median `-0.019479`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.138467`, avg `0.022645`, median `0.054522`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.016844`, avg `-0.008524`, median `-0.009018`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.625`, primary_mae `0.018246`, avg `-0.0115`, median `-0.014224`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.525`, primary_mae `0.018668`, avg `-0.007786`, median `-0.009197`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.05318`, avg `0.011481`, median `0.017343`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.085593`, avg `0.031456`, median `0.058364`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.010988, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016144, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.018668, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.052905, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.045192, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013839, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014865, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.010988, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016148, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019153, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016144, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.3375, 'primary_vs_secondary_accuracy_spread': 0.325, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016956, 'direction_hit_rate': 0.3375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023578, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.018668, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035608, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059691, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.052905, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059806, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.088711, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.045192, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.012052`, avg `-0.018856`, median `-0.016078`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.015565`, avg `-0.01519`, median `-0.02258`
- 10d: sample `8`, primary_hit `1.0`, primary_closer `0.625`, primary_mae `0.013501`, avg `-0.015127`, median `-0.016097`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.073772`, avg `0.017035`, median `0.025462`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.124071`, avg `0.034259`, median `0.059414`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.021052`, avg `-0.008711`, median `-0.009708`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.023679`, avg `-0.012095`, median `-0.01025`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.020592`, avg `-0.008624`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.075513`, avg `0.011013`, median `0.020913`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.130541`, avg `0.035483`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.010905`, avg `-0.011694`, median `-0.009953`
- 5d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.015454`, avg `-0.022588`, median `-0.023937`
- 10d: sample `16`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.017305`, avg `-0.03311`, median `-0.038709`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.083701`, avg `0.002879`, median `-0.009325`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.149562`, avg `0.041966`, median `0.061566`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.014542`, avg `-0.005659`, median `-0.004464`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4875`, primary_mae `0.017512`, avg `-0.010323`, median `-0.009891`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.4875`, primary_mae `0.0197`, avg `-0.010307`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.059691`, avg `0.008677`, median `0.011176`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.088711`, avg `0.029175`, median `0.044101`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.014542`, avg `-0.005659`, median `-0.004464`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4875`, primary_mae `0.017512`, avg `-0.010323`, median `-0.009891`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.4875`, primary_mae `0.0197`, avg `-0.010307`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.059691`, avg `0.008677`, median `0.011176`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.088711`, avg `0.029175`, median `0.044101`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.65`, primary_mae `0.01444`, avg `-0.005425`, median `-0.004782`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.7`, primary_mae `0.014743`, avg `-0.007573`, median `-0.0084`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.015374`, avg `-0.005327`, median `-0.008001`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.035638`, avg `0.015794`, median `0.017343`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.050711`, avg `0.037812`, median `0.059526`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.014542`, avg `-0.005659`, median `-0.004464`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4875`, primary_mae `0.017512`, avg `-0.010323`, median `-0.009891`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.4875`, primary_mae `0.0197`, avg `-0.010307`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.059691`, avg `0.008677`, median `0.011176`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.088711`, avg `0.029175`, median `0.044101`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.014542`, avg `-0.005659`, median `-0.004464`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4875`, primary_mae `0.017512`, avg `-0.010323`, median `-0.009891`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.4875`, primary_mae `0.0197`, avg `-0.010307`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.059691`, avg `0.008677`, median `0.011176`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.088711`, avg `0.029175`, median `0.044101`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.016371`, avg `-0.003328`, median `-0.002653`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.018947`, avg `-0.007531`, median `-0.003`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.021044`, avg `-0.002473`, median `-0.006203`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.061813`, avg `0.011878`, median `0.013057`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.4`, primary_mae `0.082834`, avg `0.028121`, median `0.030631`

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
