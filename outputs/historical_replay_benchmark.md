# Historical Replay Benchmark

Generated at: `2026-07-14T22:37:16.352797+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.011966`
- secondary_mean_absolute_error: `0.011838`
- primary_error_advantage: `-0.000128`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.016807`
- secondary_mean_absolute_error: `0.016025`
- primary_error_advantage: `-0.000782`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.023798`
- secondary_mean_absolute_error: `0.023765`
- primary_error_advantage: `-3.3e-05`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.2125`
- primary_mean_absolute_error: `0.066171`
- secondary_mean_absolute_error: `0.037708`
- primary_error_advantage: `-0.028463`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.071259`
- secondary_mean_absolute_error: `0.065974`
- primary_error_advantage: `-0.005285`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.011625`, as_primary `0`, as_primary_hit `None`, avg `-0.000489`, median `0.001107`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.015394`, as_primary `0`, as_primary_hit `None`, avg `-0.000557`, median `0.003859`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.021472`, as_primary `0`, as_primary_hit `None`, avg `-0.002358`, median `-0.001038`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.031123`, as_primary `0`, as_primary_hit `None`, avg `0.003754`, median `0.011504`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.061438`, as_primary `0`, as_primary_hit `None`, avg `0.00537`, median `0.00973`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.011823`, as_primary `20`, as_primary_hit `0.7`, avg `-0.000489`, median `0.001107`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.016149`, as_primary `20`, as_primary_hit `0.65`, avg `-0.000557`, median `0.003859`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.024272`, as_primary `20`, as_primary_hit `0.55`, avg `-0.002358`, median `-0.001038`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.045351`, as_primary `20`, as_primary_hit `0.65`, avg `0.003754`, median `0.011504`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.068316`, as_primary `20`, as_primary_hit `0.65`, avg `0.00537`, median `0.00973`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.011952`, as_primary `60`, as_primary_hit `0.5`, avg `-0.000489`, median `0.001107`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.017198`, as_primary `60`, as_primary_hit `0.5333`, avg `-0.000557`, median `0.003859`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.025396`, as_primary `60`, as_primary_hit `0.45`, avg `-0.002358`, median `-0.001038`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.067361`, as_primary `60`, as_primary_hit `0.6833`, avg `0.003754`, median `0.011504`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.076755`, as_primary `60`, as_primary_hit `0.5`, avg `0.00537`, median `0.00973`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.011668`, as_primary `0`, as_primary_hit `None`, avg `-0.000489`, median `0.001107`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.01533`, as_primary `0`, as_primary_hit `None`, avg `-0.000557`, median `0.003859`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.021045`, as_primary `0`, as_primary_hit `None`, avg `-0.002358`, median `-0.001038`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.031933`, as_primary `0`, as_primary_hit `None`, avg `0.003754`, median `0.011504`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.059799`, as_primary `0`, as_primary_hit `None`, avg `0.00537`, median `0.00973`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.008509`, avg `0.001147`, median `0.000755`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.012833`, avg `0.003582`, median `0.006292`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.023701`, avg `-0.001125`, median `0.001302`
- 20d: sample `40`, primary_hit `0.5`, primary_closer `0.275`, primary_mae `0.054673`, avg `0.004813`, median `0.011191`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.55`, primary_mae `0.065022`, avg `0.000724`, median `0.005159`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.015422`, avg `-0.002126`, median `0.001894`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.020782`, avg `-0.004696`, median `-0.00071`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.023896`, avg `-0.003591`, median `-0.005889`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.15`, primary_mae `0.07767`, avg `0.002696`, median `0.012218`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.077495`, avg `0.010015`, median `0.012182`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.009047`, avg `-0.003758`, median `-0.002721`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.014216`, avg `-0.001881`, median `0.003801`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.024997`, avg `-0.004861`, median `0.001074`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.054824`, avg `-0.000262`, median `0.011191`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.059243`, avg `-0.019735`, median `-0.024343`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.4833`, primary_mae `0.012939`, avg `0.0006`, median `0.004226`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.4167`, primary_mae `0.017671`, avg `-0.000116`, median `0.003922`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.5`, primary_mae `0.023399`, avg `-0.001524`, median `-0.003167`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.2`, primary_mae `0.069954`, avg `0.005093`, median `0.012218`
- 60d: sample `60`, primary_hit `0.5167`, primary_closer `0.4833`, primary_mae `0.075264`, avg `0.013738`, median `0.012182`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.009047, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.014216, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.023399, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.054824, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.059243, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011625, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011952, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.009047, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01533, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017198, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.014216, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021045, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025396, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.023399, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.2125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031123, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067361, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.054824, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059799, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076755, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.059243, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.875`, primary_mae `0.007387`, avg `-0.000267`, median `1.1e-05`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.015434`, avg `0.000765`, median `-0.000869`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.024666`, avg `-0.007274`, median `-0.008901`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.071179`, avg `-0.007645`, median `-0.007303`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.072765`, avg `0.026771`, median `0.061365`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.007183`, avg `0.005151`, median `0.00544`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.012736`, avg `0.007434`, median `0.006733`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.023992`, avg `-0.00085`, median `-0.00151`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.053699`, avg `0.010612`, median `0.016877`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.073404`, avg `0.027124`, median `0.049905`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019708`, avg `-0.008137`, median `-0.00531`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.021677`, avg `-0.012778`, median `-0.006575`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.018933`, avg `-0.009992`, median `-0.014252`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.1875`, primary_mae `0.071018`, avg `0.000393`, median `0.020913`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.100638`, avg `0.014003`, median `0.024759`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.011966`, avg `-0.000489`, median `0.001107`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.016807`, avg `-0.000557`, median `0.003859`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.023798`, avg `-0.002358`, median `-0.001038`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.2125`, primary_mae `0.066171`, avg `0.003754`, median `0.011504`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.071259`, avg `0.00537`, median `0.00973`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.011966`, avg `-0.000489`, median `0.001107`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.016807`, avg `-0.000557`, median `0.003859`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.023798`, avg `-0.002358`, median `-0.001038`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.2125`, primary_mae `0.066171`, avg `0.003754`, median `0.011504`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.071259`, avg `0.00537`, median `0.00973`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.010153`, avg `-0.000334`, median `-0.000421`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.575`, primary_mae `0.016187`, avg `-0.001102`, median `0.003801`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.026796`, avg `-0.002247`, median `0.001074`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.2`, primary_mae `0.068674`, avg `0.000253`, median `0.010966`
- 60d: sample `40`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.053394`, avg `-0.007797`, median `-0.011052`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.5167`, primary_mae `0.013297`, avg `-0.00267`, median `-0.000421`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4833`, primary_mae `0.018594`, avg `-0.003758`, median `0.002154`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.024263`, avg `-0.004015`, median `-0.002374`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.1833`, primary_mae `0.070055`, avg `0.00171`, median `0.011504`
- 60d: sample `60`, primary_hit `0.5`, primary_closer `0.5167`, primary_mae `0.071411`, avg `9.9e-05`, median `0.001124`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.011966`, avg `-0.000489`, median `0.001107`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.016807`, avg `-0.000557`, median `0.003859`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.023798`, avg `-0.002358`, median `-0.001038`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.2125`, primary_mae `0.066171`, avg `0.003754`, median `0.011504`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.071259`, avg `0.00537`, median `0.00973`

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
