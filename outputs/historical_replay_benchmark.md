# Historical Replay Benchmark

Generated at: `2026-06-27T05:06:19.089543+00:00`
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
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.015147`
- secondary_mean_absolute_error: `0.013774`
- primary_error_advantage: `-0.001373`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.01928`
- secondary_mean_absolute_error: `0.016862`
- primary_error_advantage: `-0.002418`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.027974`
- secondary_mean_absolute_error: `0.020109`
- primary_error_advantage: `-0.007865`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.055126`
- secondary_mean_absolute_error: `0.031791`
- primary_error_advantage: `-0.023335`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.7`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.3`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.053793`
- secondary_mean_absolute_error: `0.047643`
- primary_error_advantage: `-0.00615`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

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
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.016231`, as_primary `40`, as_primary_hit `0.5`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.01917`, as_primary `40`, as_primary_hit `0.45`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.023429`, as_primary `40`, as_primary_hit `0.475`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.043247`, as_primary `40`, as_primary_hit `0.725`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.060292`, as_primary `40`, as_primary_hit `0.825`, avg `0.025555`, median `0.034522`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.013623`, as_primary `40`, as_primary_hit `0.55`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.017626`, as_primary `40`, as_primary_hit `0.55`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.025387`, as_primary `40`, as_primary_hit `0.475`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.054782`, as_primary `40`, as_primary_hit `0.625`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.375`, path_mae `0.055769`, as_primary `40`, as_primary_hit `0.425`, avg `0.025555`, median `0.034522`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.013476`, as_primary `0`, as_primary_hit `None`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.016487`, as_primary `0`, as_primary_hit `None`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.019719`, as_primary `0`, as_primary_hit `None`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.027929`, as_primary `0`, as_primary_hit `None`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.045352`, as_primary `0`, as_primary_hit `None`, avg `0.025555`, median `0.034522`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.016129`, avg `-0.000273`, median `0.000401`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.018502`, avg `-0.006385`, median `-0.008169`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.018166`, avg `0.003141`, median `-0.001481`
- 20d: sample `20`, primary_hit `0.95`, primary_closer `0.5`, primary_mae `0.022733`, avg `0.02849`, median `0.028709`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.45`, primary_mae `0.028975`, avg `0.070033`, median `0.07382`

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.019905`, avg `0.003281`, median `0.001083`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.019678`, avg `0.004539`, median `0.003971`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.034503`, avg `0.002708`, median `-0.0029`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.15`, primary_mae `0.0479`, avg `-0.000345`, median `0.000934`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.051894`, avg `0.041442`, median `0.059526`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.012277`, avg `0.00117`, median `0.002632`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.019471`, avg `-0.002009`, median `0.002906`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.325`, primary_mae `0.029613`, avg `-0.003857`, median `-0.003297`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.2`, primary_mae `0.074936`, avg `-0.002183`, median `0.01042`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.425`, primary_mae `0.067152`, avg `-0.004627`, median `-0.00576`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.019905`, avg `0.003281`, median `0.001083`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.019678`, avg `0.004539`, median `0.003971`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.034503`, avg `0.002708`, median `-0.0029`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.15`, primary_mae `0.0479`, avg `-0.000345`, median `0.000934`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.051894`, avg `0.041442`, median `0.059526`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.008611`, avg `-0.000679`, median `-0.00191`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.015969`, avg `-0.003409`, median `0.000495`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.026904`, avg `-0.008895`, median `-0.007514`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.2`, primary_mae `0.07265`, avg `-0.004368`, median `0.012401`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.04707`, avg `-0.017907`, median `-0.018214`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.016036`, avg `0.001373`, median `0.003621`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.020737`, avg `-0.003496`, median `-0.005063`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.025244`, avg `0.002161`, median `0.003043`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.049977`, avg `0.014246`, median `0.025671`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.325`, primary_mae `0.058105`, avg `0.039343`, median `0.058439`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.008611, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015969, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.025244, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.15, 'primary_mean_absolute_error': 0.0479, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.04707, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013476, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016231, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.008611, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016487, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01917, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015969, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019719, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025387, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.025244, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027929, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054782, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.15, 'primary_mean_absolute_error': 0.0479, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.3, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045352, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060292, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.04707, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.020813`, avg `0.003937`, median `-0.002538`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.019783`, avg `0.003281`, median `0.003059`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.032176`, avg `0.012288`, median `0.005454`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.049979`, avg `0.004341`, median `0.010601`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.043109`, avg `0.047065`, median `0.069591`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.018579`, avg `0.005185`, median `0.003213`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.01904`, avg `0.006215`, median `0.003971`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.033623`, avg `0.005277`, median `-0.002764`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.1875`, primary_mae `0.048052`, avg `0.000665`, median `0.004841`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.055846`, avg `0.038732`, median `0.052495`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.007411`, avg `-0.002368`, median `-0.003287`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.015247`, avg `-0.005035`, median `-0.003092`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.025487`, avg `-0.010765`, median `-0.011075`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.07182`, avg `-0.004019`, median `0.012401`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.054851`, avg `-0.020865`, median `-0.042779`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.015147`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.01928`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.027974`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.2625`, primary_mae `0.055126`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.053793`, avg `0.025555`, median `0.034522`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.015147`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.01928`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.027974`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.2625`, primary_mae `0.055126`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.053793`, avg `0.025555`, median `0.034522`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.019905`, avg `0.003281`, median `0.001083`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.019678`, avg `0.004539`, median `0.003971`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.034503`, avg `0.002708`, median `-0.0029`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.15`, primary_mae `0.0479`, avg `-0.000345`, median `0.000934`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.051894`, avg `0.041442`, median `0.059526`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.5333`, primary_mae `0.013561`, avg `0.000689`, median `0.001912`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.4`, primary_mae `0.019148`, avg `-0.003467`, median `-0.002562`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.3667`, primary_mae `0.025797`, avg `-0.001524`, median `-0.001708`
- 20d: sample `60`, primary_hit `0.5667`, primary_closer `0.3`, primary_mae `0.057535`, avg `0.008042`, median `0.017679`
- 60d: sample `60`, primary_hit `0.7`, primary_closer `0.4333`, primary_mae `0.054426`, avg `0.020259`, median `0.030835`

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
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.015147`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.01928`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.027974`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.2625`, primary_mae `0.055126`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.053793`, avg `0.025555`, median `0.034522`

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
