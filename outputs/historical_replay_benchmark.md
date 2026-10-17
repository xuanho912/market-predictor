# Historical Replay Benchmark

Generated at: `2026-10-17T05:40:15.050643+00:00`
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
- primary_mean_absolute_error: `0.022918`
- secondary_mean_absolute_error: `0.01967`
- primary_error_advantage: `-0.003248`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.032816`
- secondary_mean_absolute_error: `0.023534`
- primary_error_advantage: `-0.009282`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.041951`
- secondary_mean_absolute_error: `0.036187`
- primary_error_advantage: `-0.005764`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.054551`
- secondary_mean_absolute_error: `0.038494`
- primary_error_advantage: `-0.016057`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.092452`
- secondary_mean_absolute_error: `0.073595`
- primary_error_advantage: `-0.018857`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.018902`, as_primary `0`, as_primary_hit `None`, avg `0.001899`, median `0.001872`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.022877`, as_primary `0`, as_primary_hit `None`, avg `0.003446`, median `0.00317`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.035626`, as_primary `0`, as_primary_hit `None`, avg `0.009098`, median `0.003466`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.03647`, as_primary `0`, as_primary_hit `None`, avg `0.02482`, median `0.022349`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.064994`, as_primary `0`, as_primary_hit `None`, avg `0.050394`, median `0.059722`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.020295`, as_primary `0`, as_primary_hit `None`, avg `0.001899`, median `0.001872`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.028813`, as_primary `0`, as_primary_hit `None`, avg `0.003446`, median `0.00317`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.044932`, as_primary `0`, as_primary_hit `None`, avg `0.009098`, median `0.003466`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.055182`, as_primary `0`, as_primary_hit `None`, avg `0.02482`, median `0.022349`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.085094`, as_primary `0`, as_primary_hit `None`, avg `0.050394`, median `0.059722`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.022918`, as_primary `80`, as_primary_hit `0.525`, avg `0.001899`, median `0.001872`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.032816`, as_primary `80`, as_primary_hit `0.6375`, avg `0.003446`, median `0.00317`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.041951`, as_primary `80`, as_primary_hit `0.5375`, avg `0.009098`, median `0.003466`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.054551`, as_primary `80`, as_primary_hit `0.675`, avg `0.02482`, median `0.022349`
- 60d: sample `80`, direction_hit `0.3125`, path_mae `0.092452`, as_primary `80`, as_primary_hit `0.6875`, avg `0.050394`, median `0.059722`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.018609`, as_primary `0`, as_primary_hit `None`, avg `0.001899`, median `0.001872`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.02187`, as_primary `0`, as_primary_hit `None`, avg `0.003446`, median `0.00317`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.033937`, as_primary `0`, as_primary_hit `None`, avg `0.009098`, median `0.003466`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.033336`, as_primary `0`, as_primary_hit `None`, avg `0.02482`, median `0.022349`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.065219`, as_primary `0`, as_primary_hit `None`, avg `0.050394`, median `0.059722`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.022918`, avg `0.001899`, median `0.001872`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.032816`, avg `0.003446`, median `0.00317`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4875`, primary_mae `0.041951`, avg `0.009098`, median `0.003466`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.054551`, avg `0.02482`, median `0.022349`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3625`, primary_mae `0.092452`, avg `0.050394`, median `0.059722`

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
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.026536`, avg `0.003646`, median `0.008219`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.034147`, avg `0.005467`, median `0.004384`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.048201`, avg `0.01438`, median `0.022026`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.06265`, avg `0.016376`, median `0.014402`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.140937`, avg `0.049913`, median `0.068319`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.012726`, avg `-0.000792`, median `0.001086`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.019087`, avg `0.001517`, median `0.00317`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.6`, primary_mae `0.021251`, avg `0.001832`, median `0.000297`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.034355`, avg `0.01927`, median `0.024572`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.054645`, avg `0.015194`, median `0.020611`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.026205`, avg `0.00237`, median `0.000375`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.039015`, avg `0.003399`, median `0.003026`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.049177`, avg `0.010091`, median `-0.000811`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.0606`, avg `0.031817`, median `0.035253`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.35`, primary_mae `0.087113`, avg `0.068233`, median `0.082445`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.012726, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.019087, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.021251, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.034355, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.054645, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018609, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022918, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.012726, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02187, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032816, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.019087, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033937, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044932, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.021251, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033336, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055182, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.034355, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064994, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.092452, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.054645, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.014477`, avg `0.000912`, median `0.007243`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.012795`, avg `0.000977`, median `0.003164`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.02388`, avg `-0.007047`, median `-0.014221`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.034038`, avg `0.016257`, median `0.024572`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.056167`, avg `-0.01494`, median `-0.039927`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.011684`, avg `0.000448`, median `0.00311`
- 5d: sample `16`, primary_hit `0.1875`, primary_closer `0.4375`, primary_mae `0.018301`, avg `0.003726`, median `0.00379`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.021697`, avg `0.001147`, median `0.003044`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.035724`, avg `0.02019`, median `0.027728`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.053267`, avg `0.014948`, median `0.020611`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.027641`, avg `0.004965`, median `0.012456`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.035826`, avg `0.008155`, median `0.007335`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.053418`, avg `0.020545`, median `0.029526`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.066919`, avg `0.020311`, median `0.01585`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.15168`, avg `0.065572`, median `0.090591`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.022918`, avg `0.001899`, median `0.001872`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.032816`, avg `0.003446`, median `0.00317`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4875`, primary_mae `0.041951`, avg `0.009098`, median `0.003466`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.054551`, avg `0.02482`, median `0.022349`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3625`, primary_mae `0.092452`, avg `0.050394`, median `0.059722`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.022918`, avg `0.001899`, median `0.001872`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.032816`, avg `0.003446`, median `0.00317`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4875`, primary_mae `0.041951`, avg `0.009098`, median `0.003466`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.054551`, avg `0.02482`, median `0.022349`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3625`, primary_mae `0.092452`, avg `0.050394`, median `0.059722`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.018206`, avg `-0.000121`, median `0.001086`
- 5d: sample `40`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.02363`, avg `0.000984`, median `0.003692`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.022603`, avg `0.00247`, median `-0.000101`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.45`, primary_mae `0.039543`, avg `0.022457`, median `0.027728`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.07325`, avg `0.028599`, median `0.047685`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.02763`, avg `0.003919`, median `0.004543`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.325`, primary_mae `0.042002`, avg `0.005907`, median `0.002603`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.0613`, avg `0.015727`, median `0.014793`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.06956`, avg `0.027184`, median `0.01653`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.111653`, avg `0.072188`, median `0.097008`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.022918`, avg `0.001899`, median `0.001872`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.032816`, avg `0.003446`, median `0.00317`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4875`, primary_mae `0.041951`, avg `0.009098`, median `0.003466`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.054551`, avg `0.02482`, median `0.022349`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3625`, primary_mae `0.092452`, avg `0.050394`, median `0.059722`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.022918`, avg `0.001899`, median `0.001872`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.032816`, avg `0.003446`, median `0.00317`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4875`, primary_mae `0.041951`, avg `0.009098`, median `0.003466`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.054551`, avg `0.02482`, median `0.022349`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3625`, primary_mae `0.092452`, avg `0.050394`, median `0.059722`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
