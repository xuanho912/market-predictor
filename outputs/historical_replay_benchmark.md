# Historical Replay Benchmark

Generated at: `2026-07-27T22:38:36.513314+00:00`
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
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.023229`
- secondary_mean_absolute_error: `0.019496`
- primary_error_advantage: `-0.003733`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.03048`
- secondary_mean_absolute_error: `0.023286`
- primary_error_advantage: `-0.007194`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.031908`
- secondary_mean_absolute_error: `0.026135`
- primary_error_advantage: `-0.005773`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.625`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.075483`
- secondary_mean_absolute_error: `0.046126`
- primary_error_advantage: `-0.029357`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.112378`
- secondary_mean_absolute_error: `0.071585`
- primary_error_advantage: `-0.040793`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.018242`, as_primary `0`, as_primary_hit `None`, avg `-0.002193`, median `0.001169`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.021839`, as_primary `0`, as_primary_hit `None`, avg `-0.003647`, median `0.000725`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.023394`, as_primary `0`, as_primary_hit `None`, avg `0.00606`, median `0.009616`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.03804`, as_primary `0`, as_primary_hit `None`, avg `0.016269`, median `0.021309`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.066122`, as_primary `0`, as_primary_hit `None`, avg `0.030379`, median `0.054511`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.019472`, as_primary `0`, as_primary_hit `None`, avg `-0.002193`, median `0.001169`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.025976`, as_primary `0`, as_primary_hit `None`, avg `-0.003647`, median `0.000725`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.028087`, as_primary `0`, as_primary_hit `None`, avg `0.00606`, median `0.009616`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.055966`, as_primary `0`, as_primary_hit `None`, avg `0.016269`, median `0.021309`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.0724`, as_primary `0`, as_primary_hit `None`, avg `0.030379`, median `0.054511`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.023229`, as_primary `80`, as_primary_hit `0.5625`, avg `-0.002193`, median `0.001169`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.03048`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.003647`, median `0.000725`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.031908`, as_primary `80`, as_primary_hit `0.5625`, avg `0.00606`, median `0.009616`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.075483`, as_primary `80`, as_primary_hit `0.65`, avg `0.016269`, median `0.021309`
- 60d: sample `80`, direction_hit `0.3375`, path_mae `0.112378`, as_primary `80`, as_primary_hit `0.6625`, avg `0.030379`, median `0.054511`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.018827`, as_primary `0`, as_primary_hit `None`, avg `-0.002193`, median `0.001169`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.02168`, as_primary `0`, as_primary_hit `None`, avg `-0.003647`, median `0.000725`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.02272`, as_primary `0`, as_primary_hit `None`, avg `0.00606`, median `0.009616`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.039261`, as_primary `0`, as_primary_hit `None`, avg `0.016269`, median `0.021309`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.06507`, as_primary `0`, as_primary_hit `None`, avg `0.030379`, median `0.054511`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.023229`, avg `-0.002193`, median `0.001169`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.03048`, avg `-0.003647`, median `0.000725`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.031908`, avg `0.00606`, median `0.009616`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.075483`, avg `0.016269`, median `0.021309`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.2875`, primary_mae `0.112378`, avg `0.030379`, median `0.054511`

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
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.3`, primary_mae `0.024794`, avg `0.001737`, median `0.006504`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.3`, primary_mae `0.034714`, avg `0.002414`, median `0.005202`
- 10d: sample `40`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.045079`, avg `0.016582`, median `0.025887`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.275`, primary_mae `0.088266`, avg `0.021733`, median `0.045529`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.2`, primary_mae `0.138259`, avg `0.025493`, median `0.061703`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.021664`, avg `-0.006123`, median `0.000684`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.026245`, avg `-0.009709`, median `-0.004452`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.018738`, avg `-0.004463`, median `-0.007064`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.0627`, avg `0.010804`, median `0.019669`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.086498`, avg `0.035264`, median `0.048423`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.021664, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.026245, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.018738, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.0627, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.086498, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018242, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023229, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.021664, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02168, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03048, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.026245, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02272, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031908, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.018738, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03804, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075483, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.0627, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06507, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.112378, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.086498, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.016111`, avg `-0.003324`, median `0.000684`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.013724`, avg `-0.007791`, median `-0.002888`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019187`, avg `-0.000342`, median `-0.003431`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.053362`, avg `0.012209`, median `0.009143`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.058389`, avg `0.031452`, median `0.045303`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.017264`, avg `-0.00091`, median `0.001086`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.018694`, avg `-0.00021`, median `0.001032`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022211`, avg `0.000728`, median `-0.003431`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.057344`, avg `0.011961`, median `0.017821`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.059661`, avg `0.028517`, median `0.039695`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.023591`, avg `-0.006218`, median `-0.003306`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.040063`, avg `-0.009526`, median `-0.007423`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.049413`, avg `0.00258`, median `0.016209`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.099184`, avg `0.002111`, median `0.017443`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.1875`, primary_mae `0.156408`, avg `-0.00768`, median `0.002694`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.023229`, avg `-0.002193`, median `0.001169`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.03048`, avg `-0.003647`, median `0.000725`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.031908`, avg `0.00606`, median `0.009616`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.075483`, avg `0.016269`, median `0.021309`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.2875`, primary_mae `0.112378`, avg `0.030379`, median `0.054511`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.023229`, avg `-0.002193`, median `0.001169`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.03048`, avg `-0.003647`, median `0.000725`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.031908`, avg `0.00606`, median `0.009616`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.075483`, avg `0.016269`, median `0.021309`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.2875`, primary_mae `0.112378`, avg `0.030379`, median `0.054511`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.021664`, avg `-0.006123`, median `0.000684`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.026245`, avg `-0.009709`, median `-0.004452`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.018738`, avg `-0.004463`, median `-0.007064`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.0627`, avg `0.010804`, median `0.019669`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.086498`, avg `0.035264`, median `0.048423`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.3`, primary_mae `0.024794`, avg `0.001737`, median `0.006504`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.3`, primary_mae `0.034714`, avg `0.002414`, median `0.005202`
- 10d: sample `40`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.045079`, avg `0.016582`, median `0.025887`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.275`, primary_mae `0.088266`, avg `0.021733`, median `0.045529`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.2`, primary_mae `0.138259`, avg `0.025493`, median `0.061703`

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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4`, primary_closer `0.3167`, primary_mae `0.021905`, avg `0.000263`, median `0.001736`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.028835`, avg `0.000223`, median `0.001877`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.037167`, avg `0.009624`, median `0.017629`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.35`, primary_mae `0.077092`, avg `0.0162`, median `0.020543`
- 60d: sample `60`, primary_hit `0.3667`, primary_closer `0.2833`, primary_mae `0.111631`, avg `0.024334`, median `0.05117`

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
