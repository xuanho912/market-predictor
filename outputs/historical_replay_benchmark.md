# Historical Replay Benchmark

Generated at: `2026-06-25T05:18:52.654481+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.015236`
- secondary_mean_absolute_error: `0.013675`
- primary_error_advantage: `-0.001561`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.01871`
- secondary_mean_absolute_error: `0.017598`
- primary_error_advantage: `-0.001112`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.027297`
- secondary_mean_absolute_error: `0.02149`
- primary_error_advantage: `-0.005807`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.054859`
- secondary_mean_absolute_error: `0.037156`
- primary_error_advantage: `-0.017703`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.054277`
- secondary_mean_absolute_error: `0.049237`
- primary_error_advantage: `-0.00504`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014345`, as_primary `0`, as_primary_hit `None`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.017352`, as_primary `0`, as_primary_hit `None`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.020545`, as_primary `0`, as_primary_hit `None`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.029054`, as_primary `0`, as_primary_hit `None`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.04803`, as_primary `0`, as_primary_hit `None`, avg `0.025555`, median `0.034522`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.016231`, as_primary `20`, as_primary_hit `0.5`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.01917`, as_primary `20`, as_primary_hit `0.55`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.023429`, as_primary `20`, as_primary_hit `0.5`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.043247`, as_primary `20`, as_primary_hit `0.5`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.060292`, as_primary `20`, as_primary_hit `0.7`, avg `0.025555`, median `0.034522`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.013623`, as_primary `60`, as_primary_hit `0.5333`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.017626`, as_primary `60`, as_primary_hit `0.4833`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.025387`, as_primary `60`, as_primary_hit `0.4667`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.054782`, as_primary `60`, as_primary_hit `0.7333`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.375`, path_mae `0.055769`, as_primary `60`, as_primary_hit `0.6`, avg `0.025555`, median `0.034522`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.013476`, as_primary `0`, as_primary_hit `None`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.016487`, as_primary `0`, as_primary_hit `None`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.019719`, as_primary `0`, as_primary_hit `None`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.027929`, as_primary `0`, as_primary_hit `None`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.045352`, as_primary `0`, as_primary_hit `None`, avg `0.025555`, median `0.034522`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.012548`, avg `-0.000476`, median `-0.000961`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.016094`, avg `-0.004897`, median `-0.005593`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.021181`, avg `-0.002877`, median `-0.00223`
- 20d: sample `40`, primary_hit `0.175`, primary_closer `0.35`, primary_mae `0.047157`, avg `0.012061`, median `0.020369`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.6`, primary_mae `0.038989`, avg `0.026063`, median `0.034522`

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.019905`, avg `0.003281`, median `0.001083`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.019678`, avg `0.004539`, median `0.003971`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.034503`, avg `0.002708`, median `-0.0029`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.0479`, avg `-0.000345`, median `0.000934`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.051894`, avg `0.041442`, median `0.059526`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.015944`, avg `0.00302`, median `0.008294`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.022972`, avg `-0.000608`, median `0.005265`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.032322`, avg `0.001181`, median `0.005897`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.2`, primary_mae `0.077222`, avg `2e-06`, median `0.001982`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.2`, primary_mae `0.087234`, avg `0.008653`, median `0.000394`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.014258`, avg `0.001301`, median `-0.000944`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.017823`, avg `0.000565`, median `0.002701`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.030704`, avg `-0.003094`, median `-0.00658`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060275`, avg `-0.002356`, median `0.008408`
- 60d: sample `40`, primary_hit `0.675`, primary_closer `0.625`, primary_mae `0.049482`, avg `0.011767`, median `0.02685`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.016214`, avg `0.001373`, median `0.003621`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.019596`, avg `-0.003496`, median `-0.005063`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.02389`, avg `0.002161`, median `0.003043`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.049443`, avg `0.014246`, median `0.025671`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.059071`, avg `0.039343`, median `0.058439`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014258, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.017823, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.02389, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.049443, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.049482, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013476, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016231, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014258, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016487, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01917, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.017823, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019719, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025387, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.02389, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027929, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054782, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.049443, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045352, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060292, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.049482, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.020812`, avg `0.003937`, median `-0.002538`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.019783`, avg `0.003281`, median `0.003059`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.032176`, avg `0.012288`, median `0.005454`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.049979`, avg `0.004341`, median `0.010601`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.043109`, avg `0.047065`, median `0.069591`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.018579`, avg `0.005185`, median `0.003213`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.01904`, avg `0.006215`, median `0.003971`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.033623`, avg `0.005277`, median `-0.002764`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.048052`, avg `0.000665`, median `0.004841`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.055846`, avg `0.038732`, median `0.052495`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.625`, primary_mae `0.01459`, avg `0.006554`, median `0.010786`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.023116`, avg `0.003187`, median `0.008063`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.033633`, avg `0.000887`, median `0.005897`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.077735`, avg `-0.001286`, median `0.001982`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.084587`, avg `0.024815`, median `0.0031`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.015236`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.01871`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.027297`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.35`, primary_mae `0.054859`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.054277`, avg `0.025555`, median `0.034522`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.015236`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.01871`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.027297`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.35`, primary_mae `0.054859`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.054277`, avg `0.025555`, median `0.034522`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.014258`, avg `0.001301`, median `-0.000944`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.017823`, avg `0.000565`, median `0.002701`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.030704`, avg `-0.003094`, median `-0.00658`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060275`, avg `-0.002356`, median `0.008408`
- 60d: sample `40`, primary_hit `0.675`, primary_closer `0.625`, primary_mae `0.049482`, avg `0.011767`, median `0.02685`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.5333`, primary_mae `0.01368`, avg `0.000689`, median `0.001912`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.4667`, primary_mae `0.018387`, avg `-0.003467`, median `-0.002562`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4`, primary_mae `0.024895`, avg `-0.001524`, median `-0.001708`
- 20d: sample `60`, primary_hit `0.2667`, primary_closer `0.3`, primary_mae `0.057178`, avg `0.008042`, median `0.017679`
- 60d: sample `60`, primary_hit `0.4`, primary_closer `0.4667`, primary_mae `0.055071`, avg `0.020259`, median `0.030835`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.015236`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.01871`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.027297`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.35`, primary_mae `0.054859`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.054277`, avg `0.025555`, median `0.034522`

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
