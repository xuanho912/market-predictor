# Historical Replay Benchmark

Generated at: `2026-09-01T23:34:52.879327+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
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
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.018388`
- secondary_mean_absolute_error: `0.015411`
- primary_error_advantage: `-0.002977`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.021246`
- secondary_mean_absolute_error: `0.01772`
- primary_error_advantage: `-0.003526`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.029991`
- secondary_mean_absolute_error: `0.026567`
- primary_error_advantage: `-0.003424`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.060224`
- secondary_mean_absolute_error: `0.0397`
- primary_error_advantage: `-0.020524`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.103078`
- secondary_mean_absolute_error: `0.06933`
- primary_error_advantage: `-0.033748`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.014713`, as_primary `0`, as_primary_hit `None`, avg `0.002469`, median `0.002876`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.016305`, as_primary `0`, as_primary_hit `None`, avg `-3.8e-05`, median `0.001271`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.024893`, as_primary `0`, as_primary_hit `None`, avg `0.000369`, median `-0.005954`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.033253`, as_primary `0`, as_primary_hit `None`, avg `0.015547`, median `0.025937`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.067832`, as_primary `0`, as_primary_hit `None`, avg `0.040882`, median `0.066037`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.015593`, as_primary `0`, as_primary_hit `None`, avg `0.002469`, median `0.002876`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.018624`, as_primary `0`, as_primary_hit `None`, avg `-3.8e-05`, median `0.001271`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.030672`, as_primary `0`, as_primary_hit `None`, avg `0.000369`, median `-0.005954`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.04524`, as_primary `0`, as_primary_hit `None`, avg `0.015547`, median `0.025937`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.072252`, as_primary `0`, as_primary_hit `None`, avg `0.040882`, median `0.066037`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.018388`, as_primary `80`, as_primary_hit `0.6125`, avg `0.002469`, median `0.002876`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.021246`, as_primary `80`, as_primary_hit `0.5625`, avg `-3.8e-05`, median `0.001271`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.029991`, as_primary `80`, as_primary_hit `0.45`, avg `0.000369`, median `-0.005954`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.060224`, as_primary `80`, as_primary_hit `0.6875`, avg `0.015547`, median `0.025937`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.103078`, as_primary `80`, as_primary_hit `0.725`, avg `0.040882`, median `0.066037`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013827`, as_primary `0`, as_primary_hit `None`, avg `0.002469`, median `0.002876`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.016232`, as_primary `0`, as_primary_hit `None`, avg `-3.8e-05`, median `0.001271`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.024239`, as_primary `0`, as_primary_hit `None`, avg `0.000369`, median `-0.005954`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.033086`, as_primary `0`, as_primary_hit `None`, avg `0.015547`, median `0.025937`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.066235`, as_primary `0`, as_primary_hit `None`, avg `0.040882`, median `0.066037`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.018388`, avg `0.002469`, median `0.002876`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.021246`, avg `-3.8e-05`, median `0.001271`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.4875`, primary_mae `0.029991`, avg `0.000369`, median `-0.005954`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.060224`, avg `0.015547`, median `0.025937`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.103078`, avg `0.040882`, median `0.066037`

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
- 3d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.018845`, avg `0.006513`, median `0.009904`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.023569`, avg `0.007698`, median `0.008552`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.037117`, avg `0.004968`, median `-0.001366`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.064277`, avg `0.017015`, median `0.032391`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.375`, primary_mae `0.116364`, avg `0.041176`, median `0.072105`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.017931`, avg `-0.001576`, median `-0.000413`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.018924`, avg `-0.007775`, median `-0.001116`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.022864`, avg `-0.00423`, median `-0.006567`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.056172`, avg `0.014078`, median `0.020543`
- 60d: sample `40`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.089792`, avg `0.040588`, median `0.060495`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.017931, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.018924, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.022864, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.056172, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.089792, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013827, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018388, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.017931, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016232, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021246, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.018924, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024239, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030672, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.022864, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033086, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060224, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.056172, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066235, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.103078, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.089792, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.020037`, avg `-0.009181`, median `-0.005846`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.022742`, avg `-0.013975`, median `-0.014509`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.023269`, avg `-6e-05`, median `-0.003208`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.05827`, avg `0.028723`, median `0.032598`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.130095`, avg `0.078668`, median `0.096964`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.022619`, avg `-0.007039`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.022379`, avg `-0.013701`, median `-0.014548`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.023639`, avg `-0.001757`, median `-0.003556`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.049637`, avg `0.024316`, median `0.031427`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.109385`, avg `0.058043`, median `0.088952`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.018414`, avg `0.001249`, median `0.005818`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.025828`, avg `0.005864`, median `0.008552`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.041675`, avg `0.016046`, median `0.022458`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.040713`, avg `0.032052`, median `0.032391`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.375`, primary_mae `0.045754`, avg `0.081832`, median `0.075075`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.018388`, avg `0.002469`, median `0.002876`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.021246`, avg `-3.8e-05`, median `0.001271`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.4875`, primary_mae `0.029991`, avg `0.000369`, median `-0.005954`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.060224`, avg `0.015547`, median `0.025937`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.103078`, avg `0.040882`, median `0.066037`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.018388`, avg `0.002469`, median `0.002876`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.021246`, avg `-3.8e-05`, median `0.001271`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.4875`, primary_mae `0.029991`, avg `0.000369`, median `-0.005954`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.060224`, avg `0.015547`, median `0.025937`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.103078`, avg `0.040882`, median `0.066037`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.017931`, avg `-0.001576`, median `-0.000413`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.018924`, avg `-0.007775`, median `-0.001116`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.022864`, avg `-0.00423`, median `-0.006567`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.056172`, avg `0.014078`, median `0.020543`
- 60d: sample `40`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.089792`, avg `0.040588`, median `0.060495`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.35`, primary_closer `0.3167`, primary_mae `0.020827`, avg `0.003106`, median `0.006292`
- 5d: sample `60`, primary_hit `0.4333`, primary_closer `0.4333`, primary_mae `0.023591`, avg `0.001332`, median `0.001825`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.4667`, primary_mae `0.032192`, avg `0.002021`, median `-0.00478`
- 20d: sample `60`, primary_hit `0.3`, primary_closer `0.3167`, primary_mae `0.058336`, avg `0.018679`, median `0.031029`
- 60d: sample `60`, primary_hit `0.25`, primary_closer `0.3833`, primary_mae `0.11151`, avg `0.043772`, median `0.072105`

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
