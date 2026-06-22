# Historical Replay Benchmark

Generated at: `2026-06-22T16:01:54.253394+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'high', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay', 'forward validation completed samples are below the minimum gate'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.015317`
- secondary_mean_absolute_error: `0.013219`
- primary_error_advantage: `-0.002098`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.016624`
- secondary_mean_absolute_error: `0.015422`
- primary_error_advantage: `-0.001202`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.024912`
- secondary_mean_absolute_error: `0.020032`
- primary_error_advantage: `-0.00488`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.03839`
- secondary_mean_absolute_error: `0.026057`
- primary_error_advantage: `-0.012333`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.057403`
- secondary_mean_absolute_error: `0.050515`
- primary_error_advantage: `-0.006888`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.013665`, as_primary `0`, as_primary_hit `None`, avg `-0.000142`, median `-0.000961`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.015408`, as_primary `0`, as_primary_hit `None`, avg `-0.003108`, median `-0.001899`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.020487`, as_primary `0`, as_primary_hit `None`, avg `-0.002479`, median `-0.002895`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.026209`, as_primary `0`, as_primary_hit `None`, avg `0.007118`, median `0.015161`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.051224`, as_primary `0`, as_primary_hit `None`, avg `0.023037`, median `0.039962`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.015317`, as_primary `80`, as_primary_hit `0.475`, avg `-0.000142`, median `-0.000961`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.016624`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.003108`, median `-0.001899`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.024912`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.002479`, median `-0.002895`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.03839`, as_primary `80`, as_primary_hit `0.675`, avg `0.007118`, median `0.015161`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.057403`, as_primary `80`, as_primary_hit `0.6125`, avg `0.023037`, median `0.039962`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.013918`, as_primary `0`, as_primary_hit `None`, avg `-0.000142`, median `-0.000961`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.018162`, as_primary `0`, as_primary_hit `None`, avg `-0.003108`, median `-0.001899`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.025894`, as_primary `0`, as_primary_hit `None`, avg `-0.002479`, median `-0.002895`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.053665`, as_primary `0`, as_primary_hit `None`, avg `0.007118`, median `0.015161`
- 60d: sample `80`, direction_hit `0.3875`, path_mae `0.062284`, as_primary `0`, as_primary_hit `None`, avg `0.023037`, median `0.039962`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.013219`, as_primary `0`, as_primary_hit `None`, avg `-0.000142`, median `-0.000961`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.015422`, as_primary `0`, as_primary_hit `None`, avg `-0.003108`, median `-0.001899`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.020032`, as_primary `0`, as_primary_hit `None`, avg `-0.002479`, median `-0.002895`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.026057`, as_primary `0`, as_primary_hit `None`, avg `0.007118`, median `0.015161`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.050515`, as_primary `0`, as_primary_hit `None`, avg `0.023037`, median `0.039962`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015317`, avg `-0.000142`, median `-0.000961`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.016624`, avg `-0.003108`, median `-0.001899`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.024912`, avg `-0.002479`, median `-0.002895`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.03839`, avg `0.007118`, median `0.015161`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.057403`, avg `0.023037`, median `0.039962`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.013767`, avg `-0.001599`, median `-0.00191`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.015428`, avg `-0.004686`, median `-0.001899`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.02311`, avg `-0.00694`, median `-0.007701`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.039887`, avg `-0.002628`, median `0.005773`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.053816`, avg `0.00522`, median `0.002524`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.016867`, avg `0.001315`, median `-0.000152`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.017821`, avg `-0.001529`, median `-0.00156`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.026713`, avg `0.001982`, median `-0.001153`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.3`, primary_mae `0.036894`, avg `0.016863`, median `0.028346`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.45`, primary_mae `0.060989`, avg `0.040854`, median `0.061862`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013767, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.015428, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.02311, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.036894, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.053816, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013219, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015317, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013767, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015408, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018162, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.015428, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020032, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025894, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.02311, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026057, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053665, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.036894, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050515, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062284, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.053816, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.016952`, avg `-0.005957`, median `-0.006094`
- 5d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.015484`, avg `-0.018169`, median `-0.014993`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.011207`, avg `0.004766`, median `0.006144`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.125`, primary_mae `0.017352`, avg `0.028135`, median `0.030181`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.027189`, avg `0.075992`, median `0.086868`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.017426`, avg `-0.002565`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.014892`, avg `-0.009072`, median `-0.010753`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.01282`, avg `0.003059`, median `-0.000811`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.017336`, avg `0.029764`, median `0.030181`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.5625`, primary_mae `0.032758`, avg `0.074865`, median `0.088952`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.017426`, avg `-0.002565`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.014892`, avg `-0.009072`, median `-0.010753`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.01282`, avg `0.003059`, median `-0.000811`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.017336`, avg `0.029764`, median `0.030181`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.5625`, primary_mae `0.032758`, avg `0.074865`, median `0.088952`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015317`, avg `-0.000142`, median `-0.000961`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.016624`, avg `-0.003108`, median `-0.001899`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.024912`, avg `-0.002479`, median `-0.002895`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.03839`, avg `0.007118`, median `0.015161`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.057403`, avg `0.023037`, median `0.039962`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015317`, avg `-0.000142`, median `-0.000961`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.016624`, avg `-0.003108`, median `-0.001899`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.024912`, avg `-0.002479`, median `-0.002895`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.03839`, avg `0.007118`, median `0.015161`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.057403`, avg `0.023037`, median `0.039962`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.013767`, avg `-0.001599`, median `-0.00191`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.015428`, avg `-0.004686`, median `-0.001899`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.02311`, avg `-0.00694`, median `-0.007701`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.039887`, avg `-0.002628`, median `0.005773`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.053816`, avg `0.00522`, median `0.002524`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.016867`, avg `0.001315`, median `-0.000152`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.017821`, avg `-0.001529`, median `-0.00156`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.026713`, avg `0.001982`, median `-0.001153`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.3`, primary_mae `0.036894`, avg `0.016863`, median `0.028346`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.45`, primary_mae `0.060989`, avg `0.040854`, median `0.061862`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015317`, avg `-0.000142`, median `-0.000961`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.016624`, avg `-0.003108`, median `-0.001899`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.024912`, avg `-0.002479`, median `-0.002895`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.03839`, avg `0.007118`, median `0.015161`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.057403`, avg `0.023037`, median `0.039962`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015317`, avg `-0.000142`, median `-0.000961`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.016624`, avg `-0.003108`, median `-0.001899`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.024912`, avg `-0.002479`, median `-0.002895`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.03839`, avg `0.007118`, median `0.015161`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.057403`, avg `0.023037`, median `0.039962`

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
