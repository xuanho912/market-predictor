# Historical Replay Benchmark

Generated at: `2026-08-28T22:23:23.906037+00:00`
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
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.015825`
- secondary_mean_absolute_error: `0.015869`
- primary_error_advantage: `4.4e-05`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.019989`
- secondary_mean_absolute_error: `0.018829`
- primary_error_advantage: `-0.00116`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.033816`
- secondary_mean_absolute_error: `0.027609`
- primary_error_advantage: `-0.006207`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.051551`
- secondary_mean_absolute_error: `0.040837`
- primary_error_advantage: `-0.010714`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.076007`
- secondary_mean_absolute_error: `0.062031`
- primary_error_advantage: `-0.013976`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.015501`, as_primary `0`, as_primary_hit `None`, avg `-0.001004`, median `0.001162`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.019013`, as_primary `0`, as_primary_hit `None`, avg `-0.001687`, median `0.000311`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.026317`, as_primary `0`, as_primary_hit `None`, avg `0.000368`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.031166`, as_primary `0`, as_primary_hit `None`, avg `0.008283`, median `0.015541`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.054011`, as_primary `0`, as_primary_hit `None`, avg `0.035709`, median `0.041158`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.015802`, as_primary `60`, as_primary_hit `0.5333`, avg `-0.001004`, median `0.001162`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.019895`, as_primary `60`, as_primary_hit `0.5167`, avg `-0.001687`, median `0.000311`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.035822`, as_primary `60`, as_primary_hit `0.4667`, avg `0.000368`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.045383`, as_primary `60`, as_primary_hit `0.7167`, avg `0.008283`, median `0.015541`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.069261`, as_primary `60`, as_primary_hit `0.7`, avg `0.035709`, median `0.041158`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.020749`, as_primary `20`, as_primary_hit `0.5`, avg `-0.001004`, median `0.001162`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.024241`, as_primary `20`, as_primary_hit `0.5`, avg `-0.001687`, median `0.000311`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.033663`, as_primary `20`, as_primary_hit `0.3`, avg `0.000368`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.061436`, as_primary `20`, as_primary_hit `0.55`, avg `0.008283`, median `0.015541`
- 60d: sample `80`, direction_hit `0.3125`, path_mae `0.078985`, as_primary `20`, as_primary_hit `0.65`, avg `0.035709`, median `0.041158`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.015598`, as_primary `0`, as_primary_hit `None`, avg `-0.001004`, median `0.001162`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.018829`, as_primary `0`, as_primary_hit `None`, avg `-0.001687`, median `0.000311`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.024189`, as_primary `0`, as_primary_hit `None`, avg `0.000368`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.031461`, as_primary `0`, as_primary_hit `None`, avg `0.008283`, median `0.015541`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.052157`, as_primary `0`, as_primary_hit `None`, avg `0.035709`, median `0.041158`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.015825`, avg `-0.001004`, median `0.001162`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.019989`, avg `-0.001687`, median `0.000311`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.033816`, avg `0.000368`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.051551`, avg `0.008283`, median `0.015541`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.076007`, avg `0.035709`, median `0.041158`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.013697`, avg `0.002778`, median `0.002198`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.019666`, avg `0.000324`, median `0.001088`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.525`, primary_mae `0.034719`, avg `0.001814`, median `-0.007787`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.3`, primary_mae `0.060109`, avg `0.003277`, median `0.011092`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.085289`, avg `0.046484`, median `0.055734`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.017952`, avg `-0.004787`, median `-0.004159`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.020311`, avg `-0.003699`, median `-0.004713`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.032914`, avg `-0.001078`, median `-0.006389`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.525`, primary_mae `0.042993`, avg `0.013288`, median `0.02076`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.066726`, avg `0.024933`, median `0.021301`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.013697, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019666, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.032914, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.042993, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.066726, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015501, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020749, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.013697, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018829, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024241, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019666, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024189, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035822, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.032914, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031166, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061436, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.042993, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052157, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.078985, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.066726, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.009103`, avg `-0.004637`, median `-0.000127`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.016588`, avg `-0.006638`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.015313`, avg `0.011856`, median `0.020076`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.75`, primary_mae `0.031707`, avg `0.026272`, median `0.030181`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.050556`, avg `0.063734`, median `0.076071`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.014851`, avg `-0.002081`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.017768`, avg `-0.005947`, median `-0.006113`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022514`, avg `0.006531`, median `0.003189`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.6875`, primary_mae `0.041426`, avg `0.018039`, median `0.030181`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.068105`, avg `0.047`, median `0.073193`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.007036`, avg `-0.000674`, median `-0.000413`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.011391`, avg `-0.00523`, median `-0.002888`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.022793`, avg `-0.004459`, median `-0.008001`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.125`, primary_mae `0.077862`, avg `0.004469`, median `0.014833`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.093494`, avg `0.037659`, median `0.058786`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.015825`, avg `-0.001004`, median `0.001162`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.019989`, avg `-0.001687`, median `0.000311`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.033816`, avg `0.000368`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.051551`, avg `0.008283`, median `0.015541`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.076007`, avg `0.035709`, median `0.041158`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.015825`, avg `-0.001004`, median `0.001162`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.019989`, avg `-0.001687`, median `0.000311`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.033816`, avg `0.000368`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.051551`, avg `0.008283`, median `0.015541`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.076007`, avg `0.035709`, median `0.041158`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.4667`, primary_mae `0.014166`, avg `0.000531`, median `0.001162`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.4333`, primary_mae `0.019104`, avg `-0.001975`, median `-0.002115`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.03097`, avg `0.002423`, median `-0.006389`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.4333`, primary_mae `0.053349`, avg `0.009242`, median `0.017157`
- 60d: sample `60`, primary_hit `0.6333`, primary_closer `0.45`, primary_mae `0.080719`, avg `0.046436`, median `0.059722`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.015825`, avg `-0.001004`, median `0.001162`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.019989`, avg `-0.001687`, median `0.000311`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.033816`, avg `0.000368`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.051551`, avg `0.008283`, median `0.015541`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.076007`, avg `0.035709`, median `0.041158`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.015825`, avg `-0.001004`, median `0.001162`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.019989`, avg `-0.001687`, median `0.000311`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.033816`, avg `0.000368`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.051551`, avg `0.008283`, median `0.015541`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.076007`, avg `0.035709`, median `0.041158`

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
