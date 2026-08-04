# Historical Replay Benchmark

Generated at: `2026-08-04T06:18:41.558819+00:00`
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
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.014813`
- secondary_mean_absolute_error: `0.016144`
- primary_error_advantage: `0.001331`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.019077`
- secondary_mean_absolute_error: `0.019884`
- primary_error_advantage: `0.000807`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.026812`
- secondary_mean_absolute_error: `0.024652`
- primary_error_advantage: `-0.00216`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.04461`
- secondary_mean_absolute_error: `0.036974`
- primary_error_advantage: `-0.007636`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.070567`
- secondary_mean_absolute_error: `0.068937`
- primary_error_advantage: `-0.00163`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.015055`, as_primary `0`, as_primary_hit `None`, avg `0.006132`, median `0.006883`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.01889`, as_primary `0`, as_primary_hit `None`, avg `0.008757`, median `0.00805`
- 10d: sample `80`, direction_hit `0.8`, path_mae `0.02113`, as_primary `0`, as_primary_hit `None`, avg `0.018822`, median `0.020959`
- 20d: sample `80`, direction_hit `0.825`, path_mae `0.027541`, as_primary `0`, as_primary_hit `None`, avg `0.031419`, median `0.032252`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.062008`, as_primary `0`, as_primary_hit `None`, avg `0.047019`, median `0.074654`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.016037`, as_primary `40`, as_primary_hit `0.775`, avg `0.006132`, median `0.006883`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.020262`, as_primary `40`, as_primary_hit `0.75`, avg `0.008757`, median `0.00805`
- 10d: sample `80`, direction_hit `0.8`, path_mae `0.026542`, as_primary `40`, as_primary_hit `0.85`, avg `0.018822`, median `0.020959`
- 20d: sample `80`, direction_hit `0.825`, path_mae `0.039768`, as_primary `40`, as_primary_hit `0.825`, avg `0.031419`, median `0.032252`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.068434`, as_primary `40`, as_primary_hit `0.95`, avg `0.047019`, median `0.074654`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.325`, path_mae `0.014974`, as_primary `40`, as_primary_hit `0.575`, avg `0.006132`, median `0.006883`
- 5d: sample `80`, direction_hit `0.3375`, path_mae `0.019528`, as_primary `40`, as_primary_hit `0.575`, avg `0.008757`, median `0.00805`
- 10d: sample `80`, direction_hit `0.2`, path_mae `0.02511`, as_primary `40`, as_primary_hit `0.75`, avg `0.018822`, median `0.020959`
- 20d: sample `80`, direction_hit `0.175`, path_mae `0.045988`, as_primary `40`, as_primary_hit `0.825`, avg `0.031419`, median `0.032252`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.071722`, as_primary `40`, as_primary_hit `0.575`, avg `0.047019`, median `0.074654`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.014712`, as_primary `0`, as_primary_hit `None`, avg `0.006132`, median `0.006883`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.018184`, as_primary `0`, as_primary_hit `None`, avg `0.008757`, median `0.00805`
- 10d: sample `80`, direction_hit `0.8`, path_mae `0.01942`, as_primary `0`, as_primary_hit `None`, avg `0.018822`, median `0.020959`
- 20d: sample `80`, direction_hit `0.825`, path_mae `0.026462`, as_primary `0`, as_primary_hit `None`, avg `0.031419`, median `0.032252`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.060917`, as_primary `0`, as_primary_hit `None`, avg `0.047019`, median `0.074654`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.014813`, avg `0.006132`, median `0.006883`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.5`, primary_mae `0.019077`, avg `0.008757`, median `0.00805`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.026812`, avg `0.018822`, median `0.020959`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.04461`, avg `0.031419`, median `0.032252`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.070567`, avg `0.047019`, median `0.074654`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.5333`, primary_mae `0.013022`, avg `0.007912`, median `0.010299`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.5`, primary_mae `0.016404`, avg `0.011039`, median `0.009975`
- 10d: sample `60`, primary_hit `0.6333`, primary_closer `0.5333`, primary_mae `0.020683`, avg `0.018254`, median `0.018762`
- 20d: sample `60`, primary_hit `0.6`, primary_closer `0.4333`, primary_mae `0.037541`, avg `0.034105`, median `0.03144`
- 60d: sample `60`, primary_hit `0.7667`, primary_closer `0.55`, primary_mae `0.052558`, avg `0.057501`, median `0.075722`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.020183`, avg `0.000792`, median `-0.000629`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.027096`, avg `0.00191`, median `-0.001159`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.0452`, avg `0.020524`, median `0.02695`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.065815`, avg `0.02336`, median `0.032537`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.124593`, avg `0.015573`, median `0.041972`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.013022, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.016404, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.020683, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.037541, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7667, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.052558, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014712, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016037, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.013022, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018184, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020262, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.016404, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01942, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026542, 'direction_hit_rate': 0.8}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.020683, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026462, 'direction_hit_rate': 0.825}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045988, 'direction_hit_rate': 0.175}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.037541, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060917, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071722, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7667, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.052558, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019768`, avg `0.000906`, median `0.005307`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.016222`, avg `0.00731`, median `0.008828`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.033689`, avg `0.005545`, median `0.007789`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.625`, primary_mae `0.037039`, avg `0.042307`, median `0.050926`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.043184`, avg `0.081873`, median `0.106633`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.015689`, avg `0.004815`, median `0.008014`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.018728`, avg `0.007273`, median `0.008828`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.1875`, primary_mae `0.03045`, avg `0.013324`, median `0.01205`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.046644`, avg `0.033992`, median `0.026122`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.5`, primary_mae `0.036236`, avg `0.09135`, median `0.104666`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.1875`, primary_closer `0.5`, primary_mae `0.019244`, avg `0.013899`, median `0.01429`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.020333`, avg `0.017914`, median `0.013495`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.8125`, primary_mae `0.024947`, avg `0.028132`, median `0.031355`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.4375`, primary_mae `0.045625`, avg `0.040169`, median `0.043617`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.6875`, primary_mae `0.10629`, avg `0.014611`, median `0.064957`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.014813`, avg `0.006132`, median `0.006883`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.5`, primary_mae `0.019077`, avg `0.008757`, median `0.00805`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.026812`, avg `0.018822`, median `0.020959`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.04461`, avg `0.031419`, median `0.032252`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.070567`, avg `0.047019`, median `0.074654`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.014813`, avg `0.006132`, median `0.006883`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.5`, primary_mae `0.019077`, avg `0.008757`, median `0.00805`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.026812`, avg `0.018822`, median `0.020959`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.04461`, avg `0.031419`, median `0.032252`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.070567`, avg `0.047019`, median `0.074654`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.775`, primary_closer `0.5`, primary_mae `0.009927`, avg `0.007184`, median `0.009174`
- 5d: sample `40`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.013532`, avg `0.009791`, median `0.009975`
- 10d: sample `40`, primary_hit `0.85`, primary_closer `0.4`, primary_mae `0.018334`, avg `0.015496`, median `0.013673`
- 20d: sample `40`, primary_hit `0.825`, primary_closer `0.4`, primary_mae `0.034816`, avg `0.032217`, median `0.028861`
- 60d: sample `40`, primary_hit `0.95`, primary_closer `0.475`, primary_mae `0.029491`, avg `0.078878`, median `0.084406`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.6`, primary_mae `0.019214`, avg `0.009368`, median `0.011572`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.6`, primary_mae `0.02215`, avg `0.013534`, median `0.008083`
- 10d: sample `20`, primary_hit `0.2`, primary_closer `0.8`, primary_mae `0.025379`, avg `0.023771`, median `0.031223`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.5`, primary_mae `0.042991`, avg `0.037881`, median `0.037526`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.7`, primary_mae `0.098691`, avg `0.014745`, median `0.060674`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.014813`, avg `0.006132`, median `0.006883`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.5`, primary_mae `0.019077`, avg `0.008757`, median `0.00805`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.026812`, avg `0.018822`, median `0.020959`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.04461`, avg `0.031419`, median `0.032252`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.070567`, avg `0.047019`, median `0.074654`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.014813`, avg `0.006132`, median `0.006883`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.5`, primary_mae `0.019077`, avg `0.008757`, median `0.00805`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.026812`, avg `0.018822`, median `0.020959`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.04461`, avg `0.031419`, median `0.032252`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.070567`, avg `0.047019`, median `0.074654`

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
