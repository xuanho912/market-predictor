# Historical Replay Benchmark

Generated at: `2026-10-12T21:20:02.741088+00:00`
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
- primary_hit_rate: `0.7`
- secondary_hit_rate: `0.3`
- primary_vs_secondary_accuracy_spread: `0.4`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.021304`
- secondary_mean_absolute_error: `0.01787`
- primary_error_advantage: `-0.003434`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.35`
- primary_vs_secondary_accuracy_spread: `0.3`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.023501`
- secondary_mean_absolute_error: `0.021143`
- primary_error_advantage: `-0.002358`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.027768`
- secondary_mean_absolute_error: `0.025811`
- primary_error_advantage: `-0.001957`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.059712`
- secondary_mean_absolute_error: `0.042526`
- primary_error_advantage: `-0.017186`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2125`
- secondary_hit_rate: `0.7875`
- primary_vs_secondary_accuracy_spread: `-0.575`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.084157`
- secondary_mean_absolute_error: `0.061754`
- primary_error_advantage: `-0.022403`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3`, path_mae `0.018338`, as_primary `0`, as_primary_hit `None`, avg `-0.009944`, median `-0.010184`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.018982`, as_primary `0`, as_primary_hit `None`, avg `-0.013774`, median `-0.016241`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.024372`, as_primary `0`, as_primary_hit `None`, avg `-0.010865`, median `-0.011875`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.036488`, as_primary `0`, as_primary_hit `None`, avg `0.016344`, median `0.017588`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.057292`, as_primary `0`, as_primary_hit `None`, avg `0.052968`, median `0.059055`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3`, path_mae `0.020347`, as_primary `0`, as_primary_hit `None`, avg `-0.009944`, median `-0.010184`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.021288`, as_primary `0`, as_primary_hit `None`, avg `-0.013774`, median `-0.016241`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.0289`, as_primary `0`, as_primary_hit `None`, avg `-0.010865`, median `-0.011875`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.053788`, as_primary `0`, as_primary_hit `None`, avg `0.016344`, median `0.017588`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.076675`, as_primary `0`, as_primary_hit `None`, avg `0.052968`, median `0.059055`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7`, path_mae `0.021304`, as_primary `80`, as_primary_hit `0.3`, avg `-0.009944`, median `-0.010184`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.023501`, as_primary `80`, as_primary_hit `0.35`, avg `-0.013774`, median `-0.016241`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.027768`, as_primary `80`, as_primary_hit `0.375`, avg `-0.010865`, median `-0.011875`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.059712`, as_primary `80`, as_primary_hit `0.6625`, avg `0.016344`, median `0.017588`
- 60d: sample `80`, direction_hit `0.2125`, path_mae `0.084157`, as_primary `80`, as_primary_hit `0.7875`, avg `0.052968`, median `0.059055`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3`, path_mae `0.016641`, as_primary `0`, as_primary_hit `None`, avg `-0.009944`, median `-0.010184`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.018168`, as_primary `0`, as_primary_hit `None`, avg `-0.013774`, median `-0.016241`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.023607`, as_primary `0`, as_primary_hit `None`, avg `-0.010865`, median `-0.011875`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.035076`, as_primary `0`, as_primary_hit `None`, avg `0.016344`, median `0.017588`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.05529`, as_primary `0`, as_primary_hit `None`, avg `0.052968`, median `0.059055`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.021304`, avg `-0.009944`, median `-0.010184`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.4625`, primary_mae `0.023501`, avg `-0.013774`, median `-0.016241`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.027768`, avg `-0.010865`, median `-0.011875`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.3625`, primary_mae `0.059712`, avg `0.016344`, median `0.017588`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3625`, primary_mae `0.084157`, avg `0.052968`, median `0.059055`

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
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.475`, primary_mae `0.019783`, avg `-0.010619`, median `-0.010538`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.525`, primary_mae `0.02673`, avg `-0.015603`, median `-0.017873`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.4`, primary_mae `0.027232`, avg `-0.013631`, median `-0.010944`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.063786`, avg `0.00802`, median `0.016081`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.425`, primary_mae `0.083858`, avg `0.031802`, median `0.048423`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.725`, primary_closer `0.325`, primary_mae `0.022824`, avg `-0.009269`, median `-0.010148`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.020273`, avg `-0.011946`, median `-0.013717`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.028305`, avg `-0.008099`, median `-0.013166`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.055638`, avg `0.024668`, median `0.019681`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.084456`, avg `0.074134`, median `0.076263`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.019783, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.020273, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.027232, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.055638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.083858, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.3, 'primary_vs_secondary_accuracy_spread': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016641, 'direction_hit_rate': 0.3}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021304, 'direction_hit_rate': 0.7}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.019783, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.35, 'primary_vs_secondary_accuracy_spread': 0.3, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018168, 'direction_hit_rate': 0.35}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023501, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.020273, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023607, 'direction_hit_rate': 0.375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0289, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.027232, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035076, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059712, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.055638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2125, 'secondary_hit_rate': 0.7875, 'primary_vs_secondary_accuracy_spread': -0.575, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05529, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.084157, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.083858, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.016852`, avg `-0.016807`, median `-0.030767`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.031311`, avg `-0.01718`, median `-0.020293`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.025217`, avg `-0.012488`, median `-0.014252`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.089956`, avg `0.014597`, median `0.027639`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.143914`, avg `0.053341`, median `0.065914`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.022135`, avg `-0.011447`, median `-0.010538`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.031664`, avg `-0.017488`, median `-0.019358`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.029755`, avg `-0.014115`, median `-0.012632`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.079611`, avg `0.008553`, median `0.023936`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.131061`, avg `0.037191`, median `0.054785`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.9375`, primary_closer `0.1875`, primary_mae `0.02748`, avg `-0.014266`, median `-0.011068`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.022138`, avg `-0.019366`, median `-0.023937`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.040154`, avg `-0.015715`, median `-0.035238`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.090977`, avg `0.028136`, median `0.019624`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.092989`, avg `0.07826`, median `0.086109`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.021304`, avg `-0.009944`, median `-0.010184`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.4625`, primary_mae `0.023501`, avg `-0.013774`, median `-0.016241`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.027768`, avg `-0.010865`, median `-0.011875`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.3625`, primary_mae `0.059712`, avg `0.016344`, median `0.017588`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3625`, primary_mae `0.084157`, avg `0.052968`, median `0.059055`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.021304`, avg `-0.009944`, median `-0.010184`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.4625`, primary_mae `0.023501`, avg `-0.013774`, median `-0.016241`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.027768`, avg `-0.010865`, median `-0.011875`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.3625`, primary_mae `0.059712`, avg `0.016344`, median `0.017588`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3625`, primary_mae `0.084157`, avg `0.052968`, median `0.059055`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.475`, primary_mae `0.019783`, avg `-0.010619`, median `-0.010538`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.525`, primary_mae `0.02673`, avg `-0.015603`, median `-0.017873`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.4`, primary_mae `0.027232`, avg `-0.013631`, median `-0.010944`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.063786`, avg `0.00802`, median `0.016081`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.425`, primary_mae `0.083858`, avg `0.031802`, median `0.048423`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.725`, primary_closer `0.325`, primary_mae `0.022824`, avg `-0.009269`, median `-0.010148`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.020273`, avg `-0.011946`, median `-0.013717`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.028305`, avg `-0.008099`, median `-0.013166`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.055638`, avg `0.024668`, median `0.019681`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.084456`, avg `0.074134`, median `0.076263`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.021304`, avg `-0.009944`, median `-0.010184`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.4625`, primary_mae `0.023501`, avg `-0.013774`, median `-0.016241`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.027768`, avg `-0.010865`, median `-0.011875`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.3625`, primary_mae `0.059712`, avg `0.016344`, median `0.017588`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3625`, primary_mae `0.084157`, avg `0.052968`, median `0.059055`

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
