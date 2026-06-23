# Historical Replay Benchmark

Generated at: `2026-06-23T05:17:21.461933+00:00`
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
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.016907`
- secondary_mean_absolute_error: `0.013555`
- primary_error_advantage: `-0.003352`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.01917`
- secondary_mean_absolute_error: `0.017294`
- primary_error_advantage: `-0.001876`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.023429`
- secondary_mean_absolute_error: `0.022419`
- primary_error_advantage: `-0.00101`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.043247`
- secondary_mean_absolute_error: `0.037435`
- primary_error_advantage: `-0.005812`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.060292`
- secondary_mean_absolute_error: `0.045352`
- primary_error_advantage: `-0.01494`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014824`, as_primary `0`, as_primary_hit `None`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.017352`, as_primary `0`, as_primary_hit `None`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.020545`, as_primary `0`, as_primary_hit `None`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.029054`, as_primary `0`, as_primary_hit `None`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.04803`, as_primary `0`, as_primary_hit `None`, avg `0.025555`, median `0.034522`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.016907`, as_primary `80`, as_primary_hit `0.525`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.01917`, as_primary `80`, as_primary_hit `0.5`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.023429`, as_primary `80`, as_primary_hit `0.475`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.043247`, as_primary `80`, as_primary_hit `0.675`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.060292`, as_primary `80`, as_primary_hit `0.625`, avg `0.025555`, median `0.034522`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.013559`, as_primary `0`, as_primary_hit `None`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.017626`, as_primary `0`, as_primary_hit `None`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.025387`, as_primary `0`, as_primary_hit `None`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.054782`, as_primary `0`, as_primary_hit `None`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.375`, path_mae `0.05577`, as_primary `0`, as_primary_hit `None`, avg `0.025555`, median `0.034522`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.013605`, as_primary `0`, as_primary_hit `None`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.016487`, as_primary `0`, as_primary_hit `None`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.019719`, as_primary `0`, as_primary_hit `None`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.027929`, as_primary `0`, as_primary_hit `None`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.045352`, as_primary `0`, as_primary_hit `None`, avg `0.025555`, median `0.034522`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.017996`, avg `0.001373`, median `0.003621`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.021685`, avg `-0.003496`, median `-0.005063`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.020845`, avg `0.002161`, median `0.003043`
- 20d: sample `40`, primary_hit `0.75`, primary_closer `0.275`, primary_mae `0.042711`, avg `0.014246`, median `0.025671`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.35`, primary_mae `0.069214`, avg `0.039343`, median `0.058439`

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.15`, primary_mae `0.022851`, avg `0.003281`, median `0.001083`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.019678`, avg `0.004539`, median `0.003971`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.034503`, avg `0.002708`, median `-0.0029`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.15`, primary_mae `0.0479`, avg `-0.000345`, median `0.000934`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.051894`, avg `0.041442`, median `0.059526`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.008786`, avg `-0.000679`, median `-0.00191`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.013634`, avg `-0.003409`, median `0.000495`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.65`, primary_mae `0.017522`, avg `-0.008895`, median `-0.007514`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.8`, primary_mae `0.039667`, avg `-0.004368`, median `0.012401`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.050847`, avg `-0.017907`, median `-0.018214`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.3`, primary_mae `0.015818`, avg `0.001301`, median `-0.000944`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.016656`, avg `0.000565`, median `0.002701`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.026013`, avg `-0.003094`, median `-0.00658`
- 20d: sample `40`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.043784`, avg `-0.002356`, median `0.008408`
- 60d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.051371`, avg `0.011767`, median `0.02685`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.017996`, avg `0.001373`, median `0.003621`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.021685`, avg `-0.003496`, median `-0.005063`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.020845`, avg `0.002161`, median `0.003043`
- 20d: sample `40`, primary_hit `0.75`, primary_closer `0.275`, primary_mae `0.042711`, avg `0.014246`, median `0.025671`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.35`, primary_mae `0.069214`, avg `0.039343`, median `0.058439`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.015818, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016656, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.020845, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.042711, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.051371, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013559, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016907, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.015818, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016487, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01917, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016656, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019719, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025387, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.020845, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027929, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054782, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.042711, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045352, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060292, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.051371, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.02002`, avg `-0.006049`, median `-0.006094`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.022632`, avg `-0.014197`, median `-0.014993`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.01226`, avg `0.009468`, median `0.006918`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.125`, primary_mae `0.021365`, avg `0.027297`, median `0.028979`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.031297`, avg `0.065314`, median `0.086868`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.015931`, avg `0.001017`, median `0.002901`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.018426`, avg `-0.004899`, median `-0.008169`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.017692`, avg `0.003732`, median `-0.001836`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.125`, primary_mae `0.024635`, avg `0.027228`, median `0.028445`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.033265`, avg `0.064819`, median `0.070816`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.007947`, avg `-0.002368`, median `-0.003287`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.01433`, avg `-0.005035`, median `-0.003092`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.625`, primary_mae `0.017914`, avg `-0.010765`, median `-0.011075`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.8125`, primary_mae `0.037612`, avg `-0.004019`, median `0.012401`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.058201`, avg `-0.020865`, median `-0.042779`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.3375`, primary_mae `0.016907`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4125`, primary_mae `0.01917`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.023429`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.043247`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.060292`, avg `0.025555`, median `0.034522`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.3375`, primary_mae `0.016907`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4125`, primary_mae `0.01917`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.023429`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.043247`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.060292`, avg `0.025555`, median `0.034522`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.15`, primary_mae `0.022851`, avg `0.003281`, median `0.001083`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.019678`, avg `0.004539`, median `0.003971`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.034503`, avg `0.002708`, median `-0.0029`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.15`, primary_mae `0.0479`, avg `-0.000345`, median `0.000934`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.051894`, avg `0.041442`, median `0.059526`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.4`, primary_mae `0.014926`, avg `0.000689`, median `0.001912`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.45`, primary_mae `0.019001`, avg `-0.003467`, median `-0.002562`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.019738`, avg `-0.001524`, median `-0.001708`
- 20d: sample `60`, primary_hit `0.7333`, primary_closer `0.45`, primary_mae `0.041696`, avg `0.008042`, median `0.017679`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.063092`, avg `0.020259`, median `0.030835`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.3375`, primary_mae `0.016907`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4125`, primary_mae `0.01917`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.023429`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.043247`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.060292`, avg `0.025555`, median `0.034522`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.3375`, primary_mae `0.016907`, avg `0.001337`, median `0.001912`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4125`, primary_mae `0.01917`, avg `-0.001466`, median `-0.000558`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.023429`, avg `-0.000466`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.043247`, avg `0.005945`, median `0.015533`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.060292`, avg `0.025555`, median `0.034522`

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
