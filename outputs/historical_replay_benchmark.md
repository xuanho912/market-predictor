# Historical Replay Benchmark

Generated at: `2026-07-09T15:37:35.898691+00:00`
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
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.014356`
- secondary_mean_absolute_error: `0.012486`
- primary_error_advantage: `-0.00187`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.018003`
- secondary_mean_absolute_error: `0.015356`
- primary_error_advantage: `-0.002647`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.026883`
- secondary_mean_absolute_error: `0.021667`
- primary_error_advantage: `-0.005216`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.045196`
- secondary_mean_absolute_error: `0.051994`
- primary_error_advantage: `0.006798`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.2`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.065802`
- secondary_mean_absolute_error: `0.058446`
- primary_error_advantage: `-0.007356`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.012926`, as_primary `0`, as_primary_hit `None`, avg `-0.001246`, median `-0.00052`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.015885`, as_primary `0`, as_primary_hit `None`, avg `-0.003008`, median `-8.2e-05`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.020839`, as_primary `0`, as_primary_hit `None`, avg `0.001345`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.030209`, as_primary `0`, as_primary_hit `None`, avg `0.004432`, median `0.011504`
- 60d: sample `80`, direction_hit `0.55`, path_mae `0.054046`, as_primary `0`, as_primary_hit `None`, avg `0.013157`, median `0.015172`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.014356`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.001246`, median `-0.00052`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.018003`, as_primary `80`, as_primary_hit `0.5`, avg `-0.003008`, median `-8.2e-05`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.026883`, as_primary `80`, as_primary_hit `0.475`, avg `0.001345`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.045196`, as_primary `80`, as_primary_hit `0.675`, avg `0.004432`, median `0.011504`
- 60d: sample `80`, direction_hit `0.55`, path_mae `0.065802`, as_primary `80`, as_primary_hit `0.55`, avg `0.013157`, median `0.015172`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.0131`, as_primary `0`, as_primary_hit `None`, avg `-0.001246`, median `-0.00052`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.016207`, as_primary `0`, as_primary_hit `None`, avg `-0.003008`, median `-8.2e-05`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.022984`, as_primary `0`, as_primary_hit `None`, avg `0.001345`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.063979`, as_primary `0`, as_primary_hit `None`, avg `0.004432`, median `0.011504`
- 60d: sample `80`, direction_hit `0.45`, path_mae `0.071217`, as_primary `0`, as_primary_hit `None`, avg `0.013157`, median `0.015172`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.012387`, as_primary `0`, as_primary_hit `None`, avg `-0.001246`, median `-0.00052`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.015549`, as_primary `0`, as_primary_hit `None`, avg `-0.003008`, median `-8.2e-05`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.020034`, as_primary `0`, as_primary_hit `None`, avg `0.001345`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.030448`, as_primary `0`, as_primary_hit `None`, avg `0.004432`, median `0.011504`
- 60d: sample `80`, direction_hit `0.55`, path_mae `0.053488`, as_primary `0`, as_primary_hit `None`, avg `0.013157`, median `0.015172`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.01395`, avg `-0.00053`, median `-0.001297`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.018528`, avg `-0.001271`, median `0.000781`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.029625`, avg `-0.001147`, median `-0.004397`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.75`, primary_mae `0.046624`, avg `-0.00292`, median `0.007521`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.065458`, avg `-0.007156`, median `-0.012825`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.014762`, avg `-0.001963`, median `0.00062`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.017478`, avg `-0.004745`, median `-0.000848`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.024141`, avg `0.003836`, median `-0.000811`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.225`, primary_mae `0.043769`, avg `0.011784`, median `0.017271`
- 60d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.066145`, avg `0.03347`, median `0.049565`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.01395`, avg `-0.00053`, median `-0.001297`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.018528`, avg `-0.001271`, median `0.000781`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.029625`, avg `-0.001147`, median `-0.004397`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.75`, primary_mae `0.046624`, avg `-0.00292`, median `0.007521`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.065458`, avg `-0.007156`, median `-0.012825`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.014762`, avg `-0.001963`, median `0.00062`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.017478`, avg `-0.004745`, median `-0.000848`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.024141`, avg `0.003836`, median `-0.000811`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.225`, primary_mae `0.043769`, avg `0.011784`, median `0.017271`
- 60d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.066145`, avg `0.03347`, median `0.049565`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.01395, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.017478, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.024141, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.043769, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.065458, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012387, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014356, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.01395, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015549, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018003, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.017478, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020034, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026883, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.024141, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030209, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.063979, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.043769, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053488, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071217, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.065458, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.015788`, avg `-0.014051`, median `-0.008899`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.018127`, avg `-0.017492`, median `-0.014548`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.018494`, avg `-0.006656`, median `-0.00918`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.036318`, avg `0.01926`, median `0.030181`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.054448`, avg `0.061772`, median `0.076071`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.014217`, avg `-0.007694`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.016639`, avg `-0.012241`, median `-0.014548`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.017818`, avg `-0.000615`, median `-0.006389`
- 20d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.032513`, avg `0.025451`, median `0.030181`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.061788`, avg `0.058014`, median `0.068996`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.014217`, avg `-0.007694`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.016639`, avg `-0.012241`, median `-0.014548`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.017818`, avg `-0.000615`, median `-0.006389`
- 20d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.032513`, avg `0.025451`, median `0.030181`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.061788`, avg `0.058014`, median `0.068996`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4125`, primary_mae `0.014356`, avg `-0.001246`, median `-0.00052`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.018003`, avg `-0.003008`, median `-8.2e-05`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.026883`, avg `0.001345`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4875`, primary_mae `0.045196`, avg `0.004432`, median `0.011504`
- 60d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.065802`, avg `0.013157`, median `0.015172`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4125`, primary_mae `0.014356`, avg `-0.001246`, median `-0.00052`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.018003`, avg `-0.003008`, median `-8.2e-05`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.026883`, avg `0.001345`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4875`, primary_mae `0.045196`, avg `0.004432`, median `0.011504`
- 60d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.065802`, avg `0.013157`, median `0.015172`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4125`, primary_mae `0.014356`, avg `-0.001246`, median `-0.00052`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.018003`, avg `-0.003008`, median `-8.2e-05`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.026883`, avg `0.001345`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4875`, primary_mae `0.045196`, avg `0.004432`, median `0.011504`
- 60d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.065802`, avg `0.013157`, median `0.015172`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4125`, primary_mae `0.014356`, avg `-0.001246`, median `-0.00052`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.018003`, avg `-0.003008`, median `-8.2e-05`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.026883`, avg `0.001345`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4875`, primary_mae `0.045196`, avg `0.004432`, median `0.011504`
- 60d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.065802`, avg `0.013157`, median `0.015172`

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
