# Historical Replay Benchmark

Generated at: `2026-07-28T21:37:45.463306+00:00`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.024124`
- secondary_mean_absolute_error: `0.020401`
- primary_error_advantage: `-0.003723`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.575`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.034287`
- secondary_mean_absolute_error: `0.02511`
- primary_error_advantage: `-0.009177`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.6`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.038239`
- secondary_mean_absolute_error: `0.02872`
- primary_error_advantage: `-0.009519`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.65`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.078437`
- secondary_mean_absolute_error: `0.047058`
- primary_error_advantage: `-0.031379`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.10648`
- secondary_mean_absolute_error: `0.066968`
- primary_error_advantage: `-0.039512`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.019119`, as_primary `0`, as_primary_hit `None`, avg `-0.002`, median `0.000673`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.023634`, as_primary `0`, as_primary_hit `None`, avg `-0.001945`, median `0.001877`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.025461`, as_primary `0`, as_primary_hit `None`, avg `0.005508`, median `0.000986`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.039143`, as_primary `0`, as_primary_hit `None`, avg `0.018974`, median `0.020543`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.059879`, as_primary `0`, as_primary_hit `None`, avg `0.040664`, median `0.056396`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.022356`, as_primary `0`, as_primary_hit `None`, avg `-0.002`, median `0.000673`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.02864`, as_primary `0`, as_primary_hit `None`, avg `-0.001945`, median `0.001877`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.031205`, as_primary `0`, as_primary_hit `None`, avg `0.005508`, median `0.000986`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.059634`, as_primary `0`, as_primary_hit `None`, avg `0.018974`, median `0.020543`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.07074`, as_primary `0`, as_primary_hit `None`, avg `0.040664`, median `0.056396`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.024124`, as_primary `80`, as_primary_hit `0.525`, avg `-0.002`, median `0.000673`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.034287`, as_primary `80`, as_primary_hit `0.5375`, avg `-0.001945`, median `0.001877`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.038239`, as_primary `80`, as_primary_hit `0.5375`, avg `0.005508`, median `0.000986`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.078437`, as_primary `80`, as_primary_hit `0.6625`, avg `0.018974`, median `0.020543`
- 60d: sample `80`, direction_hit `0.3`, path_mae `0.10648`, as_primary `80`, as_primary_hit `0.7`, avg `0.040664`, median `0.056396`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.019275`, as_primary `0`, as_primary_hit `None`, avg `-0.002`, median `0.000673`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.023015`, as_primary `0`, as_primary_hit `None`, avg `-0.001945`, median `0.001877`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.024657`, as_primary `0`, as_primary_hit `None`, avg `0.005508`, median `0.000986`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.039705`, as_primary `0`, as_primary_hit `None`, avg `0.018974`, median `0.020543`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.059537`, as_primary `0`, as_primary_hit `None`, avg `0.040664`, median `0.056396`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.7`, primary_mae `0.013235`, avg `-0.004464`, median `0.000402`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.014902`, avg `-0.003731`, median `8.8e-05`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.022293`, avg `-0.006977`, median `-0.008686`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.058423`, avg `0.000456`, median `0.001236`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.052578`, avg `0.010504`, median `0.003188`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.35`, primary_mae `0.027753`, avg `-0.001178`, median `0.000971`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.040749`, avg `-0.001349`, median `0.00324`
- 10d: sample `60`, primary_hit `0.4167`, primary_closer `0.4167`, primary_mae `0.043554`, avg `0.009669`, median `0.011903`
- 20d: sample `60`, primary_hit `0.2833`, primary_closer `0.2833`, primary_mae `0.085109`, avg `0.025147`, median `0.030044`
- 60d: sample `60`, primary_hit `0.25`, primary_closer `0.2667`, primary_mae `0.124448`, avg `0.050717`, median `0.07049`

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
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.029274`, avg `0.003013`, median `0.003333`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.225`, primary_mae `0.043417`, avg `0.005606`, median `0.006405`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.057264`, avg `0.016821`, median `0.026095`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.25`, primary_mae `0.092335`, avg `0.029483`, median `0.042225`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.129362`, avg `0.051819`, median `0.072835`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.018973`, avg `-0.007012`, median `-4.2e-05`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.025158`, avg `-0.009495`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.019213`, avg `-0.005806`, median `-0.007304`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.06454`, avg `0.008465`, median `0.018008`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.083598`, avg `0.029508`, median `0.041779`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.018973, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.025158, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.019213, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.06454, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.083598, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019119, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024124, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.018973, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023015, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034287, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.025158, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024657, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038239, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.019213, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039143, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.078437, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.06454, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059537, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.10648, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.083598, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.875`, primary_mae `0.014348`, avg `-0.011661`, median `-0.004442`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `1.0`, primary_mae `0.015974`, avg `-0.013005`, median `-0.007038`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.016988`, avg `-0.01125`, median `-0.0116`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.054743`, avg `0.003144`, median `0.001236`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.055723`, avg `0.02412`, median `0.019638`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.6875`, primary_mae `0.013867`, avg `-0.004573`, median `0.000402`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.6875`, primary_mae `0.015726`, avg `-0.002815`, median `0.000725`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.020802`, avg `-0.005977`, median `-0.008686`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.059404`, avg `0.007805`, median `0.009546`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.05226`, avg `0.01818`, median `0.017729`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.033746`, avg `-0.000933`, median `0.000272`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.051339`, avg `-0.00536`, median `-0.005785`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.058904`, avg `0.004394`, median `0.016209`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.098558`, avg `0.009128`, median `0.021827`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.132912`, avg `0.005912`, median `0.018432`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.024124`, avg `-0.002`, median `0.000673`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.034287`, avg `-0.001945`, median `0.001877`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4625`, primary_mae `0.038239`, avg `0.005508`, median `0.000986`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.3`, primary_mae `0.078437`, avg `0.018974`, median `0.020543`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3375`, primary_mae `0.10648`, avg `0.040664`, median `0.056396`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.024124`, avg `-0.002`, median `0.000673`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.034287`, avg `-0.001945`, median `0.001877`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4625`, primary_mae `0.038239`, avg `0.005508`, median `0.000986`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.3`, primary_mae `0.078437`, avg `0.018974`, median `0.020543`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3375`, primary_mae `0.10648`, avg `0.040664`, median `0.056396`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.018973`, avg `-0.007012`, median `-4.2e-05`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.025158`, avg `-0.009495`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.019213`, avg `-0.005806`, median `-0.007304`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.06454`, avg `0.008465`, median `0.018008`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.083598`, avg `0.029508`, median `0.041779`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.029274`, avg `0.003013`, median `0.003333`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.225`, primary_mae `0.043417`, avg `0.005606`, median `0.006405`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.057264`, avg `0.016821`, median `0.026095`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.25`, primary_mae `0.092335`, avg `0.029483`, median `0.042225`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.129362`, avg `0.051819`, median `0.072835`

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
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.55`, primary_mae `0.019622`, avg `0.001027`, median `0.000952`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.025143`, avg `0.005545`, median `0.003601`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.038288`, avg `0.010053`, median `0.016707`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.072732`, avg `0.0248`, median `0.020543`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.085119`, avg `0.048312`, median `0.056396`

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
