# Historical Replay Benchmark

Generated at: `2026-09-03T01:07:55.713489+00:00`
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
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.023349`
- secondary_mean_absolute_error: `0.016273`
- primary_error_advantage: `-0.007076`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.027997`
- secondary_mean_absolute_error: `0.020955`
- primary_error_advantage: `-0.007042`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3875`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.039541`
- secondary_mean_absolute_error: `0.03122`
- primary_error_advantage: `-0.008321`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.15`
- secondary_hit_rate: `0.85`
- primary_vs_secondary_accuracy_spread: `-0.7`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.049446`
- secondary_mean_absolute_error: `0.036607`
- primary_error_advantage: `-0.012839`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.07743`
- secondary_mean_absolute_error: `0.060102`
- primary_error_advantage: `-0.017328`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.015771`, as_primary `0`, as_primary_hit `None`, avg `0.005406`, median `0.011156`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.020282`, as_primary `0`, as_primary_hit `None`, avg `0.008448`, median `0.012347`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.028927`, as_primary `0`, as_primary_hit `None`, avg `0.016169`, median `0.018382`
- 20d: sample `80`, direction_hit `0.85`, path_mae `0.030737`, as_primary `0`, as_primary_hit `None`, avg `0.034364`, median `0.033694`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.062895`, as_primary `0`, as_primary_hit `None`, avg `0.05198`, median `0.075373`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.017176`, as_primary `0`, as_primary_hit `None`, avg `0.005406`, median `0.011156`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.022726`, as_primary `0`, as_primary_hit `None`, avg `0.008448`, median `0.012347`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.035199`, as_primary `0`, as_primary_hit `None`, avg `0.016169`, median `0.018382`
- 20d: sample `80`, direction_hit `0.85`, path_mae `0.044494`, as_primary `0`, as_primary_hit `None`, avg `0.034364`, median `0.033694`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.070261`, as_primary `0`, as_primary_hit `None`, avg `0.05198`, median `0.075373`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.35`, path_mae `0.023349`, as_primary `80`, as_primary_hit `0.65`, avg `0.005406`, median `0.011156`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.027997`, as_primary `80`, as_primary_hit `0.65`, avg `0.008448`, median `0.012347`
- 10d: sample `80`, direction_hit `0.3125`, path_mae `0.039541`, as_primary `80`, as_primary_hit `0.6875`, avg `0.016169`, median `0.018382`
- 20d: sample `80`, direction_hit `0.15`, path_mae `0.049446`, as_primary `80`, as_primary_hit `0.85`, avg `0.034364`, median `0.033694`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.07743`, as_primary `80`, as_primary_hit `0.725`, avg `0.05198`, median `0.075373`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.016273`, as_primary `0`, as_primary_hit `None`, avg `0.005406`, median `0.011156`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.020324`, as_primary `0`, as_primary_hit `None`, avg `0.008448`, median `0.012347`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.027487`, as_primary `0`, as_primary_hit `None`, avg `0.016169`, median `0.018382`
- 20d: sample `80`, direction_hit `0.85`, path_mae `0.029201`, as_primary `0`, as_primary_hit `None`, avg `0.034364`, median `0.033694`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.06188`, as_primary `0`, as_primary_hit `None`, avg `0.05198`, median `0.075373`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.015071`, avg `0.004951`, median `0.009174`
- 5d: sample `40`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.018891`, avg `0.009326`, median `0.011166`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.475`, primary_mae `0.025756`, avg `0.011982`, median `0.015135`
- 20d: sample `40`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.044815`, avg `0.035189`, median `0.033589`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.049509`, avg `0.067281`, median `0.084406`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.375`, primary_closer `0.275`, primary_mae `0.031626`, avg `0.005862`, median `0.012554`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.037104`, avg `0.007569`, median `0.013359`
- 10d: sample `40`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.053327`, avg `0.020356`, median `0.024797`
- 20d: sample `40`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.054078`, avg `0.033539`, median `0.033974`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.105351`, avg `0.036679`, median `0.061361`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.3375`, primary_mae `0.023349`, avg `0.005406`, median `0.011156`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.027997`, avg `0.008448`, median `0.012347`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.4125`, primary_mae `0.039541`, avg `0.016169`, median `0.018382`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.049446`, avg `0.034364`, median `0.033694`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.07743`, avg `0.05198`, median `0.075373`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.023349, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.027997, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3125, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.039541, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.049446, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.07743, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015771, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023349, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.023349, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020282, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027997, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.027997, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027487, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039541, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3125, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.039541, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.15, 'secondary_hit_rate': 0.85, 'primary_vs_secondary_accuracy_spread': -0.7, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029201, 'direction_hit_rate': 0.85}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049446, 'direction_hit_rate': 0.15}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.049446, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06188, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07743, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.07743, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.017688`, avg `0.001549`, median `0.005307`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.75`, primary_mae `0.015623`, avg `0.005751`, median `0.008828`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.75`, primary_mae `0.019688`, avg `0.012164`, median `0.017428`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.052264`, avg `0.058072`, median `0.060676`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.04987`, avg `0.104031`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.014506`, avg `0.008964`, median `0.017216`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.016466`, avg `0.01295`, median `0.017715`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.6875`, primary_mae `0.019389`, avg `0.017364`, median `0.018985`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.040264`, avg `0.043371`, median `0.050926`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.3125`, primary_mae `0.048216`, avg `0.086325`, median `0.099615`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.029233`, avg `0.017259`, median `0.019675`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.034369`, avg `0.016216`, median `0.019955`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.04615`, avg `0.032087`, median `0.028523`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.3125`, primary_mae `0.041374`, avg `0.044056`, median `0.041794`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.091522`, avg `0.051307`, median `0.040665`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.3375`, primary_mae `0.023349`, avg `0.005406`, median `0.011156`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.027997`, avg `0.008448`, median `0.012347`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.4125`, primary_mae `0.039541`, avg `0.016169`, median `0.018382`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.049446`, avg `0.034364`, median `0.033694`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.07743`, avg `0.05198`, median `0.075373`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.3375`, primary_mae `0.023349`, avg `0.005406`, median `0.011156`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.027997`, avg `0.008448`, median `0.012347`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.4125`, primary_mae `0.039541`, avg `0.016169`, median `0.018382`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.049446`, avg `0.034364`, median `0.033694`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.07743`, avg `0.05198`, median `0.075373`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.3375`, primary_mae `0.023349`, avg `0.005406`, median `0.011156`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.027997`, avg `0.008448`, median `0.012347`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.4125`, primary_mae `0.039541`, avg `0.016169`, median `0.018382`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.049446`, avg `0.034364`, median `0.033694`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.07743`, avg `0.05198`, median `0.075373`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.3375`, primary_mae `0.023349`, avg `0.005406`, median `0.011156`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.027997`, avg `0.008448`, median `0.012347`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.4125`, primary_mae `0.039541`, avg `0.016169`, median `0.018382`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.049446`, avg `0.034364`, median `0.033694`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.07743`, avg `0.05198`, median `0.075373`

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
