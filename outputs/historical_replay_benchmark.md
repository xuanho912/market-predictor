# Historical Replay Benchmark

Generated at: `2026-11-14T18:05:25.686553+00:00`
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
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.020187`
- secondary_mean_absolute_error: `0.018124`
- primary_error_advantage: `-0.002063`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.025666`
- secondary_mean_absolute_error: `0.021645`
- primary_error_advantage: `-0.004021`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.04156`
- secondary_mean_absolute_error: `0.0355`
- primary_error_advantage: `-0.00606`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.072481`
- secondary_mean_absolute_error: `0.071151`
- primary_error_advantage: `-0.00133`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.114312`
- secondary_mean_absolute_error: `0.094362`
- primary_error_advantage: `-0.01995`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.017449`, as_primary `0`, as_primary_hit `None`, avg `0.001834`, median `-0.002`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.021499`, as_primary `0`, as_primary_hit `None`, avg `0.003985`, median `0.003016`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.032442`, as_primary `0`, as_primary_hit `None`, avg `0.004911`, median `-0.00812`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.04611`, as_primary `0`, as_primary_hit `None`, avg `0.015771`, median `0.017081`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.082151`, as_primary `0`, as_primary_hit `None`, avg `0.020201`, median `0.004525`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.020128`, as_primary `60`, as_primary_hit `0.3667`, avg `0.001834`, median `-0.002`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.026263`, as_primary `60`, as_primary_hit `0.5`, avg `0.003985`, median `0.003016`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.045557`, as_primary `60`, as_primary_hit `0.3667`, avg `0.004911`, median `-0.00812`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.070479`, as_primary `60`, as_primary_hit `0.5833`, avg `0.015771`, median `0.017081`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.111888`, as_primary `60`, as_primary_hit `0.45`, avg `0.020201`, median `0.004525`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.018184`, as_primary `20`, as_primary_hit `0.75`, avg `0.001834`, median `-0.002`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.021048`, as_primary `20`, as_primary_hit `0.7`, avg `0.003985`, median `0.003016`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.031503`, as_primary `20`, as_primary_hit `0.55`, avg `0.004911`, median `-0.00812`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.073154`, as_primary `20`, as_primary_hit `0.7`, avg `0.015771`, median `0.017081`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.096786`, as_primary `20`, as_primary_hit `0.75`, avg `0.020201`, median `0.004525`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.017202`, as_primary `0`, as_primary_hit `None`, avg `0.001834`, median `-0.002`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.019757`, as_primary `0`, as_primary_hit `None`, avg `0.003985`, median `0.003016`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.027826`, as_primary `0`, as_primary_hit `None`, avg `0.004911`, median `-0.00812`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.043528`, as_primary `0`, as_primary_hit `None`, avg `0.015771`, median `0.017081`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.075412`, as_primary `0`, as_primary_hit `None`, avg `0.020201`, median `0.004525`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.020187`, avg `0.001834`, median `-0.002`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.025666`, avg `0.003985`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.375`, primary_mae `0.04156`, avg `0.004911`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.525`, primary_mae `0.072481`, avg `0.015771`, median `0.017081`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.114312`, avg `0.020201`, median `0.004525`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.4167`, primary_mae `0.020344`, avg `-0.003039`, median `-0.00764`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.3167`, primary_mae `0.025039`, avg `-0.000384`, median `-4.9e-05`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.3167`, primary_mae `0.037666`, avg `0.000976`, median `-0.009821`
- 20d: sample `60`, primary_hit `0.5833`, primary_closer `0.5333`, primary_mae `0.060442`, avg `0.008551`, median `0.013391`
- 60d: sample `60`, primary_hit `0.45`, primary_closer `0.4333`, primary_mae `0.104775`, avg `0.00331`, median `-0.012327`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.019716`, avg `0.016456`, median `0.022255`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.55`, primary_mae `0.02755`, avg `0.017091`, median `0.018988`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.05324`, avg `0.016716`, median `0.018187`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.108596`, avg `0.03743`, median `0.030573`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.142924`, avg `0.070873`, median `0.05308`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019716, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.025039, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.037666, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.060442, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.104775, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017202, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020128, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019716, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019757, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026263, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.025039, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027826, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045557, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.037666, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043528, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073154, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.060442, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075412, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.111888, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.104775, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.016739`, avg `-0.014139`, median `-0.01401`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.021578`, avg `-0.017817`, median `-0.02258`
- 10d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.028821`, avg `-0.015109`, median `-0.013277`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.062332`, avg `0.004121`, median `-0.006947`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.099774`, avg `0.010735`, median `0.003168`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.017736`, avg `-0.010207`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.019711`, avg `-0.011084`, median `-0.009462`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.029332`, avg `-0.007888`, median `-0.013277`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.060069`, avg `0.008055`, median `0.005646`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.100463`, avg `0.00842`, median `0.003555`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.019271`, avg `0.018381`, median `0.027772`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.027662`, avg `0.019934`, median `0.02246`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.056226`, avg `0.019542`, median `0.018187`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.111901`, avg `0.042417`, median `0.026931`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.148565`, avg `0.071647`, median `0.059733`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.020187`, avg `0.001834`, median `-0.002`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.025666`, avg `0.003985`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.375`, primary_mae `0.04156`, avg `0.004911`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.525`, primary_mae `0.072481`, avg `0.015771`, median `0.017081`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.114312`, avg `0.020201`, median `0.004525`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.020187`, avg `0.001834`, median `-0.002`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.025666`, avg `0.003985`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.375`, primary_mae `0.04156`, avg `0.004911`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.525`, primary_mae `0.072481`, avg `0.015771`, median `0.017081`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.114312`, avg `0.020201`, median `0.004525`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.4167`, primary_mae `0.020344`, avg `-0.003039`, median `-0.00764`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.3167`, primary_mae `0.025039`, avg `-0.000384`, median `-4.9e-05`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.3167`, primary_mae `0.037666`, avg `0.000976`, median `-0.009821`
- 20d: sample `60`, primary_hit `0.5833`, primary_closer `0.5333`, primary_mae `0.060442`, avg `0.008551`, median `0.013391`
- 60d: sample `60`, primary_hit `0.45`, primary_closer `0.4333`, primary_mae `0.104775`, avg `0.00331`, median `-0.012327`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.019716`, avg `0.016456`, median `0.022255`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.55`, primary_mae `0.02755`, avg `0.017091`, median `0.018988`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.05324`, avg `0.016716`, median `0.018187`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.108596`, avg `0.03743`, median `0.030573`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.142924`, avg `0.070873`, median `0.05308`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.020187`, avg `0.001834`, median `-0.002`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.025666`, avg `0.003985`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.375`, primary_mae `0.04156`, avg `0.004911`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.525`, primary_mae `0.072481`, avg `0.015771`, median `0.017081`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.114312`, avg `0.020201`, median `0.004525`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.020187`, avg `0.001834`, median `-0.002`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.025666`, avg `0.003985`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.375`, primary_mae `0.04156`, avg `0.004911`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.525`, primary_mae `0.072481`, avg `0.015771`, median `0.017081`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.114312`, avg `0.020201`, median `0.004525`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.020187`, avg `0.001834`, median `-0.002`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.025666`, avg `0.003985`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.375`, primary_mae `0.04156`, avg `0.004911`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.525`, primary_mae `0.072481`, avg `0.015771`, median `0.017081`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.114312`, avg `0.020201`, median `0.004525`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
