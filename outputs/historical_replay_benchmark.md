# Historical Replay Benchmark

Generated at: `2026-07-28T14:41:10.314093+00:00`
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
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.022798`
- secondary_mean_absolute_error: `0.021219`
- primary_error_advantage: `-0.001579`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.027844`
- secondary_mean_absolute_error: `0.024999`
- primary_error_advantage: `-0.002845`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.575`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.035696`
- secondary_mean_absolute_error: `0.025134`
- primary_error_advantage: `-0.010562`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.073192`
- secondary_mean_absolute_error: `0.052796`
- primary_error_advantage: `-0.020396`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.106038`
- secondary_mean_absolute_error: `0.082934`
- primary_error_advantage: `-0.023104`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.6`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.018906`, as_primary `0`, as_primary_hit `None`, avg `-0.000925`, median `0.001169`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.021693`, as_primary `0`, as_primary_hit `None`, avg `-0.001699`, median `0.001877`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.024142`, as_primary `0`, as_primary_hit `None`, avg `0.007065`, median `0.003908`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.040279`, as_primary `0`, as_primary_hit `None`, avg `0.017758`, median `0.026059`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.070175`, as_primary `0`, as_primary_hit `None`, avg `0.036082`, median `0.058049`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.019809`, as_primary `20`, as_primary_hit `0.45`, avg `-0.000925`, median `0.001169`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.023355`, as_primary `20`, as_primary_hit `0.4`, avg `-0.001699`, median `0.001877`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.030275`, as_primary `20`, as_primary_hit `0.3`, avg `0.007065`, median `0.003908`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.058826`, as_primary `20`, as_primary_hit `0.65`, avg `0.017758`, median `0.026059`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.079747`, as_primary `20`, as_primary_hit `0.7`, avg `0.036082`, median `0.058049`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.023967`, as_primary `60`, as_primary_hit `0.6`, avg `-0.000925`, median `0.001169`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.030029`, as_primary `60`, as_primary_hit `0.5833`, avg `-0.001699`, median `0.001877`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.03382`, as_primary `60`, as_primary_hit `0.6333`, avg `0.007065`, median `0.003908`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.077837`, as_primary `60`, as_primary_hit `0.6167`, avg `0.017758`, median `0.026059`
- 60d: sample `80`, direction_hit `0.3375`, path_mae `0.11124`, as_primary `60`, as_primary_hit `0.65`, avg `0.036082`, median `0.058049`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.019295`, as_primary `0`, as_primary_hit `None`, avg `-0.000925`, median `0.001169`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.021475`, as_primary `0`, as_primary_hit `None`, avg `-0.001699`, median `0.001877`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.023504`, as_primary `0`, as_primary_hit `None`, avg `0.007065`, median `0.003908`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.040841`, as_primary `0`, as_primary_hit `None`, avg `0.017758`, median `0.026059`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.06965`, as_primary `0`, as_primary_hit `None`, avg `0.036082`, median `0.058049`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.022798`, avg `-0.000925`, median `0.001169`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.027844`, avg `-0.001699`, median `0.001877`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.035696`, avg `0.007065`, median `0.003908`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.073192`, avg `0.017758`, median `0.026059`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.106038`, avg `0.036082`, median `0.058049`

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
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.0273`, avg `0.00418`, median `0.009336`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.035795`, avg `0.00554`, median `0.006622`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.325`, primary_mae `0.046928`, avg `0.018373`, median `0.029364`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.275`, primary_mae `0.091332`, avg `0.027247`, median `0.047695`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.2`, primary_mae `0.140176`, avg `0.043949`, median `0.081631`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.018295`, avg `-0.00603`, median `0.000402`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.575`, primary_mae `0.019893`, avg `-0.008938`, median `-0.000971`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.024463`, avg `-0.004244`, median `-0.007064`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.055051`, avg `0.008268`, median `0.016081`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.6`, primary_mae `0.071901`, avg `0.028214`, median `0.041779`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.018295, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.019893, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.024463, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.055051, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.071901, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018906, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023967, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.018295, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021475, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030029, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.019893, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023504, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03382, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.024463, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040279, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.077837, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.055051, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06965, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.11124, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.071901, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.011799`, avg `-0.004826`, median `0.000402`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.875`, primary_mae `0.011491`, avg `-0.008522`, median `-0.002888`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.021019`, avg `-0.0043`, median `-0.007304`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.057026`, avg `0.005427`, median `-0.001572`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.0521`, avg `0.020496`, median `0.014967`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.015228`, avg `-0.003469`, median `0.000402`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.625`, primary_mae `0.01366`, avg `-0.004888`, median `0.000725`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.024678`, avg `-0.003643`, median `-0.007304`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.060762`, avg `0.00624`, median `0.001236`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.054762`, avg `0.019535`, median `0.003188`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.022766`, avg `-0.002536`, median `-0.000629`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.036937`, avg `-0.008744`, median `-0.007423`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.051198`, avg `0.003774`, median `0.014884`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.100295`, avg `0.007335`, median `0.021621`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.181459`, avg `0.012609`, median `0.068241`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.022798`, avg `-0.000925`, median `0.001169`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.027844`, avg `-0.001699`, median `0.001877`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.035696`, avg `0.007065`, median `0.003908`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.073192`, avg `0.017758`, median `0.026059`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.106038`, avg `0.036082`, median `0.058049`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.022798`, avg `-0.000925`, median `0.001169`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.027844`, avg `-0.001699`, median `0.001877`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.035696`, avg `0.007065`, median `0.003908`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.073192`, avg `0.017758`, median `0.026059`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.106038`, avg `0.036082`, median `0.058049`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.018295`, avg `-0.00603`, median `0.000402`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.575`, primary_mae `0.019893`, avg `-0.008938`, median `-0.000971`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.024463`, avg `-0.004244`, median `-0.007064`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.055051`, avg `0.008268`, median `0.016081`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.6`, primary_mae `0.071901`, avg `0.028214`, median `0.041779`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.0273`, avg `0.00418`, median `0.009336`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.035795`, avg `0.00554`, median `0.006622`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.325`, primary_mae `0.046928`, avg `0.018373`, median `0.029364`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.275`, primary_mae `0.091332`, avg `0.027247`, median `0.047695`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.2`, primary_mae `0.140176`, avg `0.043949`, median `0.081631`

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
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.013986`, avg `-0.002222`, median `0.000684`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.6`, primary_mae `0.013878`, avg `-0.001849`, median `0.000725`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.025353`, avg `-0.003917`, median `-0.007304`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.059573`, avg `0.001606`, median `0.001236`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.056031`, avg `0.013958`, median `0.003188`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.022798`, avg `-0.000925`, median `0.001169`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.027844`, avg `-0.001699`, median `0.001877`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.035696`, avg `0.007065`, median `0.003908`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.073192`, avg `0.017758`, median `0.026059`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.106038`, avg `0.036082`, median `0.058049`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
