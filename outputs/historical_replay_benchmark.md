# Historical Replay Benchmark

Generated at: `2026-10-14T01:33:29.483324+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'low', 'reasons': [], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.016107`
- secondary_mean_absolute_error: `0.014305`
- primary_error_advantage: `-0.001802`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.017236`
- secondary_mean_absolute_error: `0.017157`
- primary_error_advantage: `-7.9e-05`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.5625`
- primary_mean_absolute_error: `0.021766`
- secondary_mean_absolute_error: `0.024403`
- primary_error_advantage: `0.002637`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.6`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.038633`
- secondary_mean_absolute_error: `0.029351`
- primary_error_advantage: `-0.009282`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.175`
- secondary_hit_rate: `0.825`
- primary_vs_secondary_accuracy_spread: `-0.65`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.043919`
- secondary_mean_absolute_error: `0.042514`
- primary_error_advantage: `-0.001405`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014806`, as_primary `0`, as_primary_hit `None`, avg `0.001593`, median `0.006415`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.017397`, as_primary `0`, as_primary_hit `None`, avg `0.000723`, median `0.003739`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.024269`, as_primary `0`, as_primary_hit `None`, avg `0.003085`, median `0.004054`
- 20d: sample `80`, direction_hit `0.8125`, path_mae `0.025956`, as_primary `0`, as_primary_hit `None`, avg `0.024566`, median `0.028479`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.042754`, as_primary `0`, as_primary_hit `None`, avg `0.070957`, median `0.085189`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014733`, as_primary `0`, as_primary_hit `None`, avg `0.001593`, median `0.006415`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.019424`, as_primary `0`, as_primary_hit `None`, avg `0.000723`, median `0.003739`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.02915`, as_primary `0`, as_primary_hit `None`, avg `0.003085`, median `0.004054`
- 20d: sample `80`, direction_hit `0.8125`, path_mae `0.037671`, as_primary `0`, as_primary_hit `None`, avg `0.024566`, median `0.028479`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.048182`, as_primary `0`, as_primary_hit `None`, avg `0.070957`, median `0.085189`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.016107`, as_primary `80`, as_primary_hit `0.5875`, avg `0.001593`, median `0.006415`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.017236`, as_primary `80`, as_primary_hit `0.5125`, avg `0.000723`, median `0.003739`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.021766`, as_primary `80`, as_primary_hit `0.575`, avg `0.003085`, median `0.004054`
- 20d: sample `80`, direction_hit `0.1875`, path_mae `0.038633`, as_primary `80`, as_primary_hit `0.8125`, avg `0.024566`, median `0.028479`
- 60d: sample `80`, direction_hit `0.175`, path_mae `0.043919`, as_primary `80`, as_primary_hit `0.825`, avg `0.070957`, median `0.085189`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.01496`, as_primary `0`, as_primary_hit `None`, avg `0.001593`, median `0.006415`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.016549`, as_primary `0`, as_primary_hit `None`, avg `0.000723`, median `0.003739`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.021944`, as_primary `0`, as_primary_hit `None`, avg `0.003085`, median `0.004054`
- 20d: sample `80`, direction_hit `0.8125`, path_mae `0.024618`, as_primary `0`, as_primary_hit `None`, avg `0.024566`, median `0.028479`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.041053`, as_primary `0`, as_primary_hit `None`, avg `0.070957`, median `0.085189`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.016107`, avg `0.001593`, median `0.006415`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5375`, primary_mae `0.017236`, avg `0.000723`, median `0.003739`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.5625`, primary_mae `0.021766`, avg `0.003085`, median `0.004054`
- 20d: sample `80`, primary_hit `0.1875`, primary_closer `0.4`, primary_mae `0.038633`, avg `0.024566`, median `0.028479`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.525`, primary_mae `0.043919`, avg `0.070957`, median `0.085189`

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
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.020444`, avg `-0.005282`, median `-0.00545`
- 5d: sample `20`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.020188`, avg `-0.007699`, median `-0.009043`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.036699`, avg `-0.007156`, median `-0.023721`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.063718`, avg `-0.000168`, median `-0.004359`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.7`, primary_mae `0.048703`, avg `0.084293`, median `0.103937`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.014083`, avg `0.00819`, median `0.012314`
- 5d: sample `40`, primary_hit `0.3`, primary_closer `0.525`, primary_mae `0.015838`, avg `0.009196`, median `0.011847`
- 10d: sample `40`, primary_hit `0.225`, primary_closer `0.6`, primary_mae `0.017031`, avg `0.012626`, median `0.012642`
- 20d: sample `40`, primary_hit `0.1`, primary_closer `0.45`, primary_mae `0.036005`, avg `0.038789`, median `0.034963`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.45`, primary_mae `0.036595`, avg `0.084197`, median `0.088956`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.015819`, avg `-0.004728`, median `-0.006849`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.017078`, avg `-0.007801`, median `-0.014292`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.016301`, avg `-0.005755`, median `-0.009917`
- 20d: sample `20`, primary_hit `0.05`, primary_closer `0.35`, primary_mae `0.018803`, avg `0.020854`, median `0.015844`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.053781`, avg `0.031141`, median `0.023239`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.014083, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.015838, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.016301, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.018803, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.075, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.036595, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014733, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016107, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.014083, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016549, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019424, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.015838, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.5625, 'best_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021766, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02915, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.016301, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024618, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038633, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.018803, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.175, 'secondary_hit_rate': 0.825, 'primary_vs_secondary_accuracy_spread': -0.65, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041053, 'direction_hit_rate': 0.825}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048182, 'direction_hit_rate': 0.825}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.075, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.036595, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.019529`, avg `0.011441`, median `0.019319`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.019187`, avg `0.013802`, median `0.011781`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.023003`, avg `0.016973`, median `0.017921`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.049309`, avg `0.061725`, median `0.060676`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.035595`, avg `0.085751`, median `0.098383`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.017762`, avg `0.009829`, median `0.01387`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.017208`, avg `0.012137`, median `0.012047`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.6875`, primary_mae `0.021675`, avg `0.014023`, median `0.014898`
- 20d: sample `16`, primary_hit `0.0`, primary_closer `0.5`, primary_mae `0.039323`, avg `0.051739`, median `0.050926`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.625`, primary_mae `0.033746`, avg `0.077996`, median `0.091366`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.020457`, avg `-0.000608`, median `-0.000629`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.018913`, avg `-0.00558`, median `-0.009043`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.038335`, avg `-0.003279`, median `-0.009699`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.066064`, avg `0.003312`, median `0.009321`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.6875`, primary_mae `0.040776`, avg `0.09068`, median `0.100635`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.016107`, avg `0.001593`, median `0.006415`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5375`, primary_mae `0.017236`, avg `0.000723`, median `0.003739`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.5625`, primary_mae `0.021766`, avg `0.003085`, median `0.004054`
- 20d: sample `80`, primary_hit `0.1875`, primary_closer `0.4`, primary_mae `0.038633`, avg `0.024566`, median `0.028479`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.525`, primary_mae `0.043919`, avg `0.070957`, median `0.085189`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.016107`, avg `0.001593`, median `0.006415`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5375`, primary_mae `0.017236`, avg `0.000723`, median `0.003739`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.5625`, primary_mae `0.021766`, avg `0.003085`, median `0.004054`
- 20d: sample `80`, primary_hit `0.1875`, primary_closer `0.4`, primary_mae `0.038633`, avg `0.024566`, median `0.028479`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.525`, primary_mae `0.043919`, avg `0.070957`, median `0.085189`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.014083`, avg `0.00819`, median `0.012314`
- 5d: sample `40`, primary_hit `0.3`, primary_closer `0.525`, primary_mae `0.015838`, avg `0.009196`, median `0.011847`
- 10d: sample `40`, primary_hit `0.225`, primary_closer `0.6`, primary_mae `0.017031`, avg `0.012626`, median `0.012642`
- 20d: sample `40`, primary_hit `0.1`, primary_closer `0.45`, primary_mae `0.036005`, avg `0.038789`, median `0.034963`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.45`, primary_mae `0.036595`, avg `0.084197`, median `0.088956`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.018132`, avg `-0.005005`, median `-0.00676`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.55`, primary_mae `0.018633`, avg `-0.00775`, median `-0.012588`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.525`, primary_mae `0.0265`, avg `-0.006456`, median `-0.011941`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.041261`, avg `0.010343`, median `0.015289`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.6`, primary_mae `0.051242`, avg `0.057717`, median `0.070115`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.016107`, avg `0.001593`, median `0.006415`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5375`, primary_mae `0.017236`, avg `0.000723`, median `0.003739`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.5625`, primary_mae `0.021766`, avg `0.003085`, median `0.004054`
- 20d: sample `80`, primary_hit `0.1875`, primary_closer `0.4`, primary_mae `0.038633`, avg `0.024566`, median `0.028479`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.525`, primary_mae `0.043919`, avg `0.070957`, median `0.085189`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.013359`, avg `0.000807`, median `0.006415`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.014968`, avg `-0.000467`, median `0.007174`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.014266`, avg `0.001566`, median `0.003538`
- 20d: sample `40`, primary_hit `0.075`, primary_closer `0.375`, primary_mae `0.025279`, avg `0.024621`, median `0.025369`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.45`, primary_mae `0.045842`, avg `0.056204`, median `0.056479`

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
