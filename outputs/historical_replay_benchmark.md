# Historical Replay Benchmark

Generated at: `2026-06-15T15:21:00.550773+00:00`
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
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.014841`
- secondary_mean_absolute_error: `0.013363`
- primary_error_advantage: `-0.001478`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.3625`
- primary_vs_secondary_accuracy_spread: `0.275`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.020305`
- secondary_mean_absolute_error: `0.016664`
- primary_error_advantage: `-0.003641`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.028409`
- secondary_mean_absolute_error: `0.026981`
- primary_error_advantage: `-0.001428`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.7125`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.049693`
- secondary_mean_absolute_error: `0.050497`
- primary_error_advantage: `0.000804`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.073362`
- secondary_mean_absolute_error: `0.058982`
- primary_error_advantage: `-0.01438`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.013622`, as_primary `0`, as_primary_hit `None`, avg `0.004789`, median `0.005077`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.016764`, as_primary `0`, as_primary_hit `None`, avg `0.005953`, median `0.005205`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.02173`, as_primary `0`, as_primary_hit `None`, avg `0.008715`, median `0.008315`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.032541`, as_primary `0`, as_primary_hit `None`, avg `0.009907`, median `0.017271`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.056795`, as_primary `0`, as_primary_hit `None`, avg `0.02784`, median `0.032906`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.014841`, as_primary `80`, as_primary_hit `0.6375`, avg `0.004789`, median `0.005077`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.020305`, as_primary `80`, as_primary_hit `0.6375`, avg `0.005953`, median `0.005205`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.028409`, as_primary `80`, as_primary_hit `0.625`, avg `0.008715`, median `0.008315`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.049693`, as_primary `80`, as_primary_hit `0.7125`, avg `0.009907`, median `0.017271`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.073362`, as_primary `80`, as_primary_hit `0.6`, avg `0.02784`, median `0.032906`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.013624`, as_primary `0`, as_primary_hit `None`, avg `0.004789`, median `0.005077`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.017025`, as_primary `0`, as_primary_hit `None`, avg `0.005953`, median `0.005205`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.029071`, as_primary `0`, as_primary_hit `None`, avg `0.008715`, median `0.008315`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.061446`, as_primary `0`, as_primary_hit `None`, avg `0.009907`, median `0.017271`
- 60d: sample `80`, direction_hit `0.4`, path_mae `0.069879`, as_primary `0`, as_primary_hit `None`, avg `0.02784`, median `0.032906`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.012615`, as_primary `0`, as_primary_hit `None`, avg `0.004789`, median `0.005077`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.015387`, as_primary `0`, as_primary_hit `None`, avg `0.005953`, median `0.005205`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.020813`, as_primary `0`, as_primary_hit `None`, avg `0.008715`, median `0.008315`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.031097`, as_primary `0`, as_primary_hit `None`, avg `0.009907`, median `0.017271`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.052997`, as_primary `0`, as_primary_hit `None`, avg `0.02784`, median `0.032906`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4`, primary_mae `0.014841`, avg `0.004789`, median `0.005077`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3625`, primary_mae `0.020305`, avg `0.005953`, median `0.005205`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4875`, primary_mae `0.028409`, avg `0.008715`, median `0.008315`
- 20d: sample `80`, primary_hit `0.7125`, primary_closer `0.475`, primary_mae `0.049693`, avg `0.009907`, median `0.017271`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.3875`, primary_mae `0.073362`, avg `0.02784`, median `0.032906`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.01342`, avg `0.006355`, median `0.005077`
- 5d: sample `40`, primary_hit `0.775`, primary_closer `0.425`, primary_mae `0.017357`, avg `0.00953`, median `0.008615`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.6`, primary_mae `0.026634`, avg `0.007993`, median `0.008571`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.675`, primary_mae `0.05233`, avg `0.002167`, median `0.01201`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.072893`, avg `0.007936`, median `-0.00576`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.016261`, avg `0.003223`, median `0.00509`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.023252`, avg `0.002375`, median `-0.000454`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.030183`, avg `0.009437`, median `0.008315`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.275`, primary_mae `0.047056`, avg `0.017646`, median `0.021541`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.35`, primary_mae `0.07383`, avg `0.047744`, median `0.059526`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01342, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.017357, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.026634, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.047056, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.072893, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012615, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014841, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01342, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_vs_secondary_accuracy_spread': 0.275, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015387, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020305, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.017357, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020813, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029071, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.026634, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7125, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031097, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061446, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.047056, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052997, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073362, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.072893, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.015955`, avg `-0.006411`, median `-0.005474`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.019385`, avg `-0.007563`, median `-0.010372`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.011877`, avg `0.008453`, median `0.006918`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.125`, primary_mae `0.024016`, avg `0.023947`, median `0.028979`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.045213`, avg `0.037866`, median `0.039481`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.016617`, avg `-0.004897`, median `-0.006238`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.016864`, avg `-0.005108`, median `-0.007506`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.015651`, avg `0.007767`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.026747`, avg `0.02262`, median `0.028979`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.057198`, avg `0.031912`, median `0.039481`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.016617`, avg `-0.004897`, median `-0.006238`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.016864`, avg `-0.005108`, median `-0.007506`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.015651`, avg `0.007767`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.026747`, avg `0.02262`, median `0.028979`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.057198`, avg `0.031912`, median `0.039481`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### low_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4`, primary_mae `0.014841`, avg `0.004789`, median `0.005077`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3625`, primary_mae `0.020305`, avg `0.005953`, median `0.005205`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4875`, primary_mae `0.028409`, avg `0.008715`, median `0.008315`
- 20d: sample `80`, primary_hit `0.7125`, primary_closer `0.475`, primary_mae `0.049693`, avg `0.009907`, median `0.017271`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.3875`, primary_mae `0.073362`, avg `0.02784`, median `0.032906`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4`, primary_mae `0.014841`, avg `0.004789`, median `0.005077`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3625`, primary_mae `0.020305`, avg `0.005953`, median `0.005205`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4875`, primary_mae `0.028409`, avg `0.008715`, median `0.008315`
- 20d: sample `80`, primary_hit `0.7125`, primary_closer `0.475`, primary_mae `0.049693`, avg `0.009907`, median `0.017271`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.3875`, primary_mae `0.073362`, avg `0.02784`, median `0.032906`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4`, primary_mae `0.014841`, avg `0.004789`, median `0.005077`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3625`, primary_mae `0.020305`, avg `0.005953`, median `0.005205`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4875`, primary_mae `0.028409`, avg `0.008715`, median `0.008315`
- 20d: sample `80`, primary_hit `0.7125`, primary_closer `0.475`, primary_mae `0.049693`, avg `0.009907`, median `0.017271`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.3875`, primary_mae `0.073362`, avg `0.02784`, median `0.032906`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4`, primary_mae `0.014841`, avg `0.004789`, median `0.005077`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3625`, primary_mae `0.020305`, avg `0.005953`, median `0.005205`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4875`, primary_mae `0.028409`, avg `0.008715`, median `0.008315`
- 20d: sample `80`, primary_hit `0.7125`, primary_closer `0.475`, primary_mae `0.049693`, avg `0.009907`, median `0.017271`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.3875`, primary_mae `0.073362`, avg `0.02784`, median `0.032906`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4`, primary_mae `0.014841`, avg `0.004789`, median `0.005077`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3625`, primary_mae `0.020305`, avg `0.005953`, median `0.005205`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4875`, primary_mae `0.028409`, avg `0.008715`, median `0.008315`
- 20d: sample `80`, primary_hit `0.7125`, primary_closer `0.475`, primary_mae `0.049693`, avg `0.009907`, median `0.017271`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.3875`, primary_mae `0.073362`, avg `0.02784`, median `0.032906`

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
