# Historical Replay Benchmark

Generated at: `2026-09-17T17:03:16.160496+00:00`
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
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.020653`
- secondary_mean_absolute_error: `0.017945`
- primary_error_advantage: `-0.002708`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.022718`
- secondary_mean_absolute_error: `0.020361`
- primary_error_advantage: `-0.002357`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.0338`
- secondary_mean_absolute_error: `0.03028`
- primary_error_advantage: `-0.00352`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.062985`
- secondary_mean_absolute_error: `0.058163`
- primary_error_advantage: `-0.004822`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2625`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.475`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.103852`
- secondary_mean_absolute_error: `0.077909`
- primary_error_advantage: `-0.025943`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.017762`, as_primary `0`, as_primary_hit `None`, avg `-0.005388`, median `-0.001655`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018978`, as_primary `0`, as_primary_hit `None`, avg `-0.007656`, median `-0.005451`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.024031`, as_primary `0`, as_primary_hit `None`, avg `-0.005482`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.038707`, as_primary `0`, as_primary_hit `None`, avg `0.017001`, median `0.020913`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.065562`, as_primary `0`, as_primary_hit `None`, avg `0.043643`, median `0.059055`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.017945`, as_primary `0`, as_primary_hit `None`, avg `-0.005388`, median `-0.001655`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.020361`, as_primary `0`, as_primary_hit `None`, avg `-0.007656`, median `-0.005451`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.03028`, as_primary `0`, as_primary_hit `None`, avg `-0.005482`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.058163`, as_primary `0`, as_primary_hit `None`, avg `0.017001`, median `0.020913`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.077909`, as_primary `0`, as_primary_hit `None`, avg `0.043643`, median `0.059055`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.020653`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.005388`, median `-0.001655`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.022718`, as_primary `80`, as_primary_hit `0.45`, avg `-0.007656`, median `-0.005451`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.0338`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.005482`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.062985`, as_primary `80`, as_primary_hit `0.625`, avg `0.017001`, median `0.020913`
- 60d: sample `80`, direction_hit `0.2625`, path_mae `0.103852`, as_primary `80`, as_primary_hit `0.7375`, avg `0.043643`, median `0.059055`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.016876`, as_primary `0`, as_primary_hit `None`, avg `-0.005388`, median `-0.001655`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.017738`, as_primary `0`, as_primary_hit `None`, avg `-0.007656`, median `-0.005451`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.023746`, as_primary `0`, as_primary_hit `None`, avg `-0.005482`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.038977`, as_primary `0`, as_primary_hit `None`, avg `0.017001`, median `0.020913`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.065618`, as_primary `0`, as_primary_hit `None`, avg `0.043643`, median `0.059055`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.5333`, primary_mae `0.017185`, avg `-0.0036`, median `0.001736`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.020098`, avg `-0.003798`, median `0.001204`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.5333`, primary_mae `0.03194`, avg `0.000151`, median `-0.005954`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.4333`, primary_mae `0.053263`, avg `0.022323`, median `0.023936`
- 60d: sample `60`, primary_hit `0.2333`, primary_closer `0.4167`, primary_mae `0.080765`, avg `0.051487`, median `0.059117`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.031059`, avg `-0.010752`, median `-0.009555`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.030579`, avg `-0.019229`, median `-0.021584`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.039378`, avg `-0.022382`, median `-0.034185`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.09215`, avg `0.001036`, median `-0.009325`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.173114`, avg `0.020111`, median `0.054522`

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
- 3d: sample `40`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.025359`, avg `-0.010239`, median `-0.010064`
- 5d: sample `40`, primary_hit `0.725`, primary_closer `0.4`, primary_mae `0.028027`, avg `-0.016522`, median `-0.019238`
- 10d: sample `40`, primary_hit `0.775`, primary_closer `0.45`, primary_mae `0.033687`, avg `-0.017348`, median `-0.017012`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.083514`, avg `0.00424`, median `0.008479`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.145064`, avg `0.024568`, median `0.050237`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.015948`, avg `-0.000538`, median `0.006509`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.55`, primary_mae `0.017409`, avg `0.001211`, median `0.002565`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.033912`, avg `0.006384`, median `0.004753`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.425`, primary_mae `0.042455`, avg `0.029762`, median `0.030823`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.425`, primary_mae `0.06264`, avg `0.062718`, median `0.061815`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.015948, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.017409, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.033687, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.042455, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.06264, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016876, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020653, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.015948, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017738, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022718, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.017409, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023746, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0338, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.033687, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038707, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062985, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.042455, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.475, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065562, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.103852, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.06264, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.020641`, avg `0.003571`, median `0.011398`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.020252`, avg `0.009276`, median `0.011486`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.046246`, avg `0.021851`, median `0.019234`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.036972`, avg `0.034503`, median `0.035195`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.076059`, avg `0.085544`, median `0.085373`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.017723`, avg `0.000189`, median `0.009121`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.017975`, avg `0.003863`, median `0.003601`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.039874`, avg `0.013893`, median `0.016207`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.4375`, primary_mae `0.039273`, avg `0.036123`, median `0.046433`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.4375`, primary_mae `0.084884`, avg `0.096021`, median `0.1008`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.8125`, primary_closer `0.125`, primary_mae `0.031411`, avg `-0.009375`, median `-0.009555`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.03079`, avg `-0.019092`, median `-0.021584`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.038021`, avg `-0.024669`, median `-0.036852`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.088595`, avg `-0.003621`, median `-0.017251`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.169714`, avg `0.012061`, median `0.054522`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.020653`, avg `-0.005388`, median `-0.001655`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.022718`, avg `-0.007656`, median `-0.005451`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.0338`, avg `-0.005482`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4625`, primary_mae `0.062985`, avg `0.017001`, median `0.020913`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.3875`, primary_mae `0.103852`, avg `0.043643`, median `0.059055`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.020653`, avg `-0.005388`, median `-0.001655`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.022718`, avg `-0.007656`, median `-0.005451`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.0338`, avg `-0.005482`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4625`, primary_mae `0.062985`, avg `0.017001`, median `0.020913`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.3875`, primary_mae `0.103852`, avg `0.043643`, median `0.059055`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.020653`, avg `-0.005388`, median `-0.001655`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.022718`, avg `-0.007656`, median `-0.005451`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.0338`, avg `-0.005482`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4625`, primary_mae `0.062985`, avg `0.017001`, median `0.020913`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.3875`, primary_mae `0.103852`, avg `0.043643`, median `0.059055`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.020653`, avg `-0.005388`, median `-0.001655`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.022718`, avg `-0.007656`, median `-0.005451`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.0338`, avg `-0.005482`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4625`, primary_mae `0.062985`, avg `0.017001`, median `0.020913`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.3875`, primary_mae `0.103852`, avg `0.043643`, median `0.059055`

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
