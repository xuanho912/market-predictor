# Historical Replay Benchmark

Generated at: `2026-07-27T15:16:36.691637+00:00`
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
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.023858`
- secondary_mean_absolute_error: `0.019624`
- primary_error_advantage: `-0.004234`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.030252`
- secondary_mean_absolute_error: `0.023023`
- primary_error_advantage: `-0.007229`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.034141`
- secondary_mean_absolute_error: `0.027526`
- primary_error_advantage: `-0.006615`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.079075`
- secondary_mean_absolute_error: `0.047563`
- primary_error_advantage: `-0.031512`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.118324`
- secondary_mean_absolute_error: `0.078024`
- primary_error_advantage: `-0.0403`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.018701`, as_primary `0`, as_primary_hit `None`, avg `-0.001502`, median `0.001169`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.021699`, as_primary `0`, as_primary_hit `None`, avg `-0.003508`, median `0.000725`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.024755`, as_primary `0`, as_primary_hit `None`, avg `0.005936`, median `0.003908`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.03957`, as_primary `0`, as_primary_hit `None`, avg `0.017522`, median `0.023882`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.070566`, as_primary `0`, as_primary_hit `None`, avg `0.031356`, median `0.058049`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.019758`, as_primary `0`, as_primary_hit `None`, avg `-0.001502`, median `0.001169`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.02407`, as_primary `0`, as_primary_hit `None`, avg `-0.003508`, median `0.000725`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.030224`, as_primary `0`, as_primary_hit `None`, avg `0.005936`, median `0.003908`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.057687`, as_primary `0`, as_primary_hit `None`, avg `0.017522`, median `0.023882`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.082338`, as_primary `0`, as_primary_hit `None`, avg `0.031356`, median `0.058049`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.023858`, as_primary `80`, as_primary_hit `0.5625`, avg `-0.001502`, median `0.001169`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.030252`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.003508`, median `0.000725`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.034141`, as_primary `80`, as_primary_hit `0.55`, avg `0.005936`, median `0.003908`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.079075`, as_primary `80`, as_primary_hit `0.65`, avg `0.017522`, median `0.023882`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.118324`, as_primary `80`, as_primary_hit `0.675`, avg `0.031356`, median `0.058049`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.019045`, as_primary `0`, as_primary_hit `None`, avg `-0.001502`, median `0.001169`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.021716`, as_primary `0`, as_primary_hit `None`, avg `-0.003508`, median `0.000725`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.024002`, as_primary `0`, as_primary_hit `None`, avg `0.005936`, median `0.003908`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.040699`, as_primary `0`, as_primary_hit `None`, avg `0.017522`, median `0.023882`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.070685`, as_primary `0`, as_primary_hit `None`, avg `0.031356`, median `0.058049`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.023858`, avg `-0.001502`, median `0.001169`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4125`, primary_mae `0.030252`, avg `-0.003508`, median `0.000725`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.034141`, avg `0.005936`, median `0.003908`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.3375`, primary_mae `0.079075`, avg `0.017522`, median `0.023882`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.3125`, primary_mae `0.118324`, avg `0.031356`, median `0.058049`

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
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.275`, primary_mae `0.026069`, avg `0.002785`, median `0.007128`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.034978`, avg `0.002522`, median `0.002964`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.225`, primary_mae `0.04867`, avg `0.016437`, median `0.029364`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.275`, primary_mae `0.095397`, avg `0.023858`, median `0.047695`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.225`, primary_mae `0.153763`, avg `0.028891`, median `0.074334`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.021647`, avg `-0.005789`, median `0.000684`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.025526`, avg `-0.009539`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.019613`, avg `-0.004565`, median `-0.007064`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.062754`, avg `0.011187`, median `0.019669`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.082885`, avg `0.033821`, median `0.04627`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.021647, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.025526, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.019613, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.062754, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.082885, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018701, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023858, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.021647, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021699, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030252, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.025526, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024002, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034141, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.019613, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03957, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.079075, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.062754, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070566, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.118324, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.082885, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.024091`, avg `-0.013711`, median `-0.018199`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.031369`, avg `-0.018719`, median `-0.024274`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.017046`, avg `-0.005373`, median `-0.006886`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.067828`, avg `0.019534`, median `0.020895`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.109177`, avg `0.051405`, median `0.068631`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.030113`, avg `-0.006839`, median `0.000341`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.037194`, avg `-0.013914`, median `-0.006529`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.017674`, avg `-0.004444`, median `-0.007383`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.071977`, avg `0.01574`, median `0.024617`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.11764`, avg `0.049448`, median `0.054967`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.025554`, avg `-0.005852`, median `-0.003306`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.038035`, avg `-0.014397`, median `-0.008733`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.052904`, avg `0.000964`, median `0.013887`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.10461`, avg `-0.00088`, median `0.021621`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.189498`, avg `0.000175`, median `0.057817`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.023858`, avg `-0.001502`, median `0.001169`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4125`, primary_mae `0.030252`, avg `-0.003508`, median `0.000725`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.034141`, avg `0.005936`, median `0.003908`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.3375`, primary_mae `0.079075`, avg `0.017522`, median `0.023882`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.3125`, primary_mae `0.118324`, avg `0.031356`, median `0.058049`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.023858`, avg `-0.001502`, median `0.001169`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4125`, primary_mae `0.030252`, avg `-0.003508`, median `0.000725`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.034141`, avg `0.005936`, median `0.003908`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.3375`, primary_mae `0.079075`, avg `0.017522`, median `0.023882`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.3125`, primary_mae `0.118324`, avg `0.031356`, median `0.058049`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.021647`, avg `-0.005789`, median `0.000684`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.025526`, avg `-0.009539`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.019613`, avg `-0.004565`, median `-0.007064`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.062754`, avg `0.011187`, median `0.019669`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.082885`, avg `0.033821`, median `0.04627`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.275`, primary_mae `0.026069`, avg `0.002785`, median `0.007128`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.034978`, avg `0.002522`, median `0.002964`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.225`, primary_mae `0.04867`, avg `0.016437`, median `0.029364`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.275`, primary_mae `0.095397`, avg `0.023858`, median `0.047695`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.225`, primary_mae `0.153763`, avg `0.028891`, median `0.074334`

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
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.023858`, avg `-0.001502`, median `0.001169`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4125`, primary_mae `0.030252`, avg `-0.003508`, median `0.000725`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.034141`, avg `0.005936`, median `0.003908`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.3375`, primary_mae `0.079075`, avg `0.017522`, median `0.023882`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.3125`, primary_mae `0.118324`, avg `0.031356`, median `0.058049`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
