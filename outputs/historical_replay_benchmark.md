# Historical Replay Benchmark

Generated at: `2026-09-29T00:40:35.256379+00:00`
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
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.017205`
- secondary_mean_absolute_error: `0.015128`
- primary_error_advantage: `-0.002077`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.018599`
- secondary_mean_absolute_error: `0.015805`
- primary_error_advantage: `-0.002794`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.020724`
- secondary_mean_absolute_error: `0.020301`
- primary_error_advantage: `-0.000423`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2625`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.475`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.04685`
- secondary_mean_absolute_error: `0.035447`
- primary_error_advantage: `-0.011403`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1`
- secondary_hit_rate: `0.9`
- primary_vs_secondary_accuracy_spread: `-0.8`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.042406`
- secondary_mean_absolute_error: `0.038374`
- primary_error_advantage: `-0.004032`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.015157`, as_primary `0`, as_primary_hit `None`, avg `-0.001128`, median `-0.001409`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.016886`, as_primary `0`, as_primary_hit `None`, avg `0.000673`, median `-0.000766`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.021196`, as_primary `0`, as_primary_hit `None`, avg `0.006414`, median `0.00857`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.031478`, as_primary `0`, as_primary_hit `None`, avg `0.021905`, median `0.030406`
- 60d: sample `80`, direction_hit `0.9`, path_mae `0.038199`, as_primary `0`, as_primary_hit `None`, avg `0.085138`, median `0.103255`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.015553`, as_primary `0`, as_primary_hit `None`, avg `-0.001128`, median `-0.001409`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.01749`, as_primary `0`, as_primary_hit `None`, avg `0.000673`, median `-0.000766`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.023394`, as_primary `0`, as_primary_hit `None`, avg `0.006414`, median `0.00857`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.043692`, as_primary `0`, as_primary_hit `None`, avg `0.021905`, median `0.030406`
- 60d: sample `80`, direction_hit `0.9`, path_mae `0.044264`, as_primary `0`, as_primary_hit `None`, avg `0.085138`, median `0.103255`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.017205`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.001128`, median `-0.001409`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.018599`, as_primary `80`, as_primary_hit `0.4875`, avg `0.000673`, median `-0.000766`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.020724`, as_primary `80`, as_primary_hit `0.625`, avg `0.006414`, median `0.00857`
- 20d: sample `80`, direction_hit `0.2625`, path_mae `0.04685`, as_primary `80`, as_primary_hit `0.7375`, avg `0.021905`, median `0.030406`
- 60d: sample `80`, direction_hit `0.1`, path_mae `0.042406`, as_primary `80`, as_primary_hit `0.9`, avg `0.085138`, median `0.103255`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.014766`, as_primary `0`, as_primary_hit `None`, avg `-0.001128`, median `-0.001409`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.015748`, as_primary `0`, as_primary_hit `None`, avg `0.000673`, median `-0.000766`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.020097`, as_primary `0`, as_primary_hit `None`, avg `0.006414`, median `0.00857`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.029714`, as_primary `0`, as_primary_hit `None`, avg `0.021905`, median `0.030406`
- 60d: sample `80`, direction_hit `0.9`, path_mae `0.038469`, as_primary `0`, as_primary_hit `None`, avg `0.085138`, median `0.103255`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.017205`, avg `-0.001128`, median `-0.001409`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.3875`, primary_mae `0.018599`, avg `0.000673`, median `-0.000766`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.020724`, avg `0.006414`, median `0.00857`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.3625`, primary_mae `0.04685`, avg `0.021905`, median `0.030406`
- 60d: sample `80`, primary_hit `0.1`, primary_closer `0.45`, primary_mae `0.042406`, avg `0.085138`, median `0.103255`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.021704`, avg `-0.004198`, median `-0.006398`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.021558`, avg `-0.001176`, median `-0.004042`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.033769`, avg `-0.001015`, median `-0.003925`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.067644`, avg `-0.005845`, median `-0.00055`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.4`, primary_mae `0.039149`, avg `0.111208`, median `0.115176`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.014207`, avg `0.000676`, median `0.000822`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.014766`, avg `0.003522`, median `0.004489`
- 10d: sample `40`, primary_hit `0.25`, primary_closer `0.575`, primary_mae `0.014932`, avg `0.009875`, median `0.011325`
- 20d: sample `40`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.043783`, avg `0.032933`, median `0.038653`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.525`, primary_mae `0.035704`, avg `0.09103`, median `0.10703`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.018704`, avg `-0.001666`, median `-0.002451`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.023304`, avg `-0.003174`, median `-0.010572`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.019263`, avg `0.00692`, median `0.003591`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.032191`, avg `0.027599`, median `0.026541`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.35`, primary_mae `0.059066`, avg `0.047285`, median `0.036672`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.014207, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.014766, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.014932, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.032191, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.075, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.035704, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014766, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017205, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.014207, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015748, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018599, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.014766, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020097, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023394, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.014932, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.475, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029714, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04685, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.032191, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1, 'secondary_hit_rate': 0.9, 'primary_vs_secondary_accuracy_spread': -0.8, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038199, 'direction_hit_rate': 0.9}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044264, 'direction_hit_rate': 0.9}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.075, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.035704, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.75`, primary_mae `0.012832`, avg `0.005815`, median `0.008014`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.015499`, avg `0.006695`, median `0.008828`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.014721`, avg `0.009347`, median `0.01205`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.035435`, avg `0.026788`, median `0.029102`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.625`, primary_mae `0.0093`, avg `0.114868`, median `0.11635`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.013408`, avg `0.001739`, median `0.003357`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.016802`, avg `0.006766`, median `0.008828`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.019419`, avg `0.010293`, median `0.016702`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.03832`, avg `0.031248`, median `0.029448`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.625`, primary_mae `0.025933`, avg `0.099981`, median `0.111461`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.018312`, avg `-0.008383`, median `-0.010622`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.02209`, avg `-0.001185`, median `-0.004042`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.036087`, avg `0.002851`, median `0.001244`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.069782`, avg `-0.004048`, median `0.012219`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.4375`, primary_mae `0.031977`, avg `0.11934`, median `0.115176`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.017205`, avg `-0.001128`, median `-0.001409`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.3875`, primary_mae `0.018599`, avg `0.000673`, median `-0.000766`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.020724`, avg `0.006414`, median `0.00857`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.3625`, primary_mae `0.04685`, avg `0.021905`, median `0.030406`
- 60d: sample `80`, primary_hit `0.1`, primary_closer `0.45`, primary_mae `0.042406`, avg `0.085138`, median `0.103255`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.017205`, avg `-0.001128`, median `-0.001409`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.3875`, primary_mae `0.018599`, avg `0.000673`, median `-0.000766`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.020724`, avg `0.006414`, median `0.00857`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.3625`, primary_mae `0.04685`, avg `0.021905`, median `0.030406`
- 60d: sample `80`, primary_hit `0.1`, primary_closer `0.45`, primary_mae `0.042406`, avg `0.085138`, median `0.103255`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.014207`, avg `0.000676`, median `0.000822`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.014766`, avg `0.003522`, median `0.004489`
- 10d: sample `40`, primary_hit `0.25`, primary_closer `0.575`, primary_mae `0.014932`, avg `0.009875`, median `0.011325`
- 20d: sample `40`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.043783`, avg `0.032933`, median `0.038653`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.525`, primary_mae `0.035704`, avg `0.09103`, median `0.10703`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.020204`, avg `-0.002932`, median `-0.003314`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.35`, primary_mae `0.022431`, avg `-0.002175`, median `-0.005877`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.026516`, avg `0.002953`, median `0.000722`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.049918`, avg `0.010877`, median `0.020612`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.049107`, avg `0.079247`, median `0.098227`

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
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.020204`, avg `-0.002932`, median `-0.003314`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.35`, primary_mae `0.022431`, avg `-0.002175`, median `-0.005877`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.026516`, avg `0.002953`, median `0.000722`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.049918`, avg `0.010877`, median `0.020612`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.049107`, avg `0.079247`, median `0.098227`

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
