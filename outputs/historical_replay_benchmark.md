# Historical Replay Benchmark

Generated at: `2026-06-24T05:13:59.309343+00:00`
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
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.01569`
- secondary_mean_absolute_error: `0.014879`
- primary_error_advantage: `-0.000811`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.01871`
- secondary_mean_absolute_error: `0.018087`
- primary_error_advantage: `-0.000623`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.027297`
- secondary_mean_absolute_error: `0.021519`
- primary_error_advantage: `-0.005778`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.054859`
- secondary_mean_absolute_error: `0.04317`
- primary_error_advantage: `-0.011689`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3875`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.6125`
- primary_mean_absolute_error: `0.054277`
- secondary_mean_absolute_error: `0.061785`
- primary_error_advantage: `0.007508`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.6125`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014456`, as_primary `0`, as_primary_hit `None`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.017352`, as_primary `0`, as_primary_hit `None`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.020545`, as_primary `0`, as_primary_hit `None`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.029054`, as_primary `0`, as_primary_hit `None`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.04803`, as_primary `0`, as_primary_hit `None`, avg `0.025555`, median `0.034522`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.016153`, as_primary `20`, as_primary_hit `0.5`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.01917`, as_primary `20`, as_primary_hit `0.55`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.023429`, as_primary `20`, as_primary_hit `0.5`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.043247`, as_primary `20`, as_primary_hit `0.5`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.060292`, as_primary `20`, as_primary_hit `0.7`, avg `0.025555`, median `0.034522`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.014416`, as_primary `60`, as_primary_hit `0.5333`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.017626`, as_primary `60`, as_primary_hit `0.4833`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.025387`, as_primary `60`, as_primary_hit `0.4667`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.054782`, as_primary `60`, as_primary_hit `0.7333`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.375`, path_mae `0.055769`, as_primary `60`, as_primary_hit `0.6`, avg `0.025555`, median `0.034522`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.013601`, as_primary `0`, as_primary_hit `None`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.016487`, as_primary `0`, as_primary_hit `None`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.019719`, as_primary `0`, as_primary_hit `None`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.027929`, as_primary `0`, as_primary_hit `None`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.045352`, as_primary `0`, as_primary_hit `None`, avg `0.025555`, median `0.034522`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.01569`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.01871`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.027297`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.054859`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.6125`, primary_mae `0.054277`, avg `0.025555`, median `0.034522`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.014124`, avg `0.001301`, median `-0.000944`
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
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.017256`, avg `0.001373`, median `0.003621`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.6`, primary_mae `0.019596`, avg `-0.003496`, median `-0.005063`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.02389`, avg `0.002161`, median `0.003043`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.425`, primary_mae `0.049443`, avg `0.014246`, median `0.025671`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.6`, primary_mae `0.059071`, avg `0.039343`, median `0.058439`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.014124, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.017823, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.02389, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.049443, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.049482, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013601, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016153, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.014124, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016487, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01917, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.017823, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019719, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025387, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.02389, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027929, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054782, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.049443, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.6125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045352, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060292, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.049482, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.019852`, avg `0.003937`, median `-0.002538`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.019783`, avg `0.003281`, median `0.003059`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.032176`, avg `0.012288`, median `0.005454`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.049979`, avg `0.004341`, median `0.010601`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.04311`, avg `0.047065`, median `0.069591`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.017619`, avg `0.005185`, median `0.003213`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.01904`, avg `0.006215`, median `0.003971`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.033623`, avg `0.005277`, median `-0.002764`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.048052`, avg `0.000665`, median `0.004841`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.055846`, avg `0.038732`, median `0.052495`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.6875`, primary_mae `0.015618`, avg `0.006554`, median `0.010786`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.6875`, primary_mae `0.023116`, avg `0.003187`, median `0.008063`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.033633`, avg `0.000887`, median `0.005897`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.077735`, avg `-0.001286`, median `0.001982`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.084588`, avg `0.024815`, median `0.0031`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.01569`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.01871`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.027297`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.054859`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.6125`, primary_mae `0.054277`, avg `0.025555`, median `0.034522`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.01569`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.01871`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.027297`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.054859`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.6125`, primary_mae `0.054277`, avg `0.025555`, median `0.034522`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.014124`, avg `0.001301`, median `-0.000944`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.017823`, avg `0.000565`, median `0.002701`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.030704`, avg `-0.003094`, median `-0.00658`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060275`, avg `-0.002356`, median `0.008408`
- 60d: sample `40`, primary_hit `0.675`, primary_closer `0.625`, primary_mae `0.049482`, avg `0.011767`, median `0.02685`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.014584`, avg `0.000689`, median `0.001912`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.5333`, primary_mae `0.018387`, avg `-0.003467`, median `-0.002562`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.024895`, avg `-0.001524`, median `-0.001708`
- 20d: sample `60`, primary_hit `0.2667`, primary_closer `0.35`, primary_mae `0.057178`, avg `0.008042`, median `0.017679`
- 60d: sample `60`, primary_hit `0.4`, primary_closer `0.6167`, primary_mae `0.055071`, avg `0.020259`, median `0.030835`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.01569`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.01871`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.027297`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.054859`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.6125`, primary_mae `0.054277`, avg `0.025555`, median `0.034522`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.01569`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.01871`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.027297`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.054859`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.6125`, primary_mae `0.054277`, avg `0.025555`, median `0.034522`

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
