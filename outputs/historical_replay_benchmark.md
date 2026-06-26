# Historical Replay Benchmark

Generated at: `2026-06-26T23:46:26.575229+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.015949`
- secondary_mean_absolute_error: `0.01553`
- primary_error_advantage: `-0.000419`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.018753`
- secondary_mean_absolute_error: `0.018221`
- primary_error_advantage: `-0.000532`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.031198`
- secondary_mean_absolute_error: `0.023221`
- primary_error_advantage: `-0.007977`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3625`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.046674`
- secondary_mean_absolute_error: `0.032885`
- primary_error_advantage: `-0.013789`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.725`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.05532`
- secondary_mean_absolute_error: `0.044064`
- primary_error_advantage: `-0.011256`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3125`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.014907`, as_primary `0`, as_primary_hit `None`, avg `0.000979`, median `-0.001489`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.017656`, as_primary `0`, as_primary_hit `None`, avg `-0.001577`, median `-0.004934`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.022499`, as_primary `0`, as_primary_hit `None`, avg `0.000261`, median `-0.001443`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.028278`, as_primary `0`, as_primary_hit `None`, avg `0.012699`, median `0.020248`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.04262`, as_primary `0`, as_primary_hit `None`, avg `0.046609`, median `0.063468`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.015911`, as_primary `60`, as_primary_hit `0.5167`, avg `0.000979`, median `-0.001489`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.018783`, as_primary `60`, as_primary_hit `0.45`, avg `-0.001577`, median `-0.004934`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.029666`, as_primary `60`, as_primary_hit `0.4667`, avg `0.000261`, median `-0.001443`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.040212`, as_primary `60`, as_primary_hit `0.75`, avg `0.012699`, median `0.020248`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.054203`, as_primary `60`, as_primary_hit `0.85`, avg `0.046609`, median `0.063468`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.015936`, as_primary `20`, as_primary_hit `0.35`, avg `0.000979`, median `-0.001489`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.018184`, as_primary `20`, as_primary_hit `0.4`, avg `-0.001577`, median `-0.004934`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.028423`, as_primary `20`, as_primary_hit `0.5`, avg `0.000261`, median `-0.001443`
- 20d: sample `80`, direction_hit `0.2625`, path_mae `0.057912`, as_primary `20`, as_primary_hit `0.7`, avg `0.012699`, median `0.020248`
- 60d: sample `80`, direction_hit `0.2`, path_mae `0.065409`, as_primary `20`, as_primary_hit `0.65`, avg `0.046609`, median `0.063468`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.014715`, as_primary `0`, as_primary_hit `None`, avg `0.000979`, median `-0.001489`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.017453`, as_primary `0`, as_primary_hit `None`, avg `-0.001577`, median `-0.004934`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.021351`, as_primary `0`, as_primary_hit `None`, avg `0.000261`, median `-0.001443`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.029129`, as_primary `0`, as_primary_hit `None`, avg `0.012699`, median `0.020248`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.045479`, as_primary `0`, as_primary_hit `None`, avg `0.046609`, median `0.063468`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.01479`, avg `0.000524`, median `-0.001489`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.016289`, avg `-0.00517`, median `-0.008169`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.02685`, avg `-0.000645`, median `-0.001702`
- 20d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.0412`, avg `0.011852`, median `0.019063`
- 60d: sample `40`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.037976`, avg `0.039988`, median `0.053577`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.017107`, avg `0.001433`, median `-0.000668`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.021218`, avg `0.002016`, median `0.001653`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.035545`, avg `0.001167`, median `-0.000285`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.052148`, avg `0.013547`, median `0.027925`
- 60d: sample `40`, primary_hit `0.8`, primary_closer `0.275`, primary_mae `0.072664`, avg `0.053231`, median `0.069752`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.015949`, avg `0.000979`, median `-0.001489`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5`, primary_mae `0.018753`, avg `-0.001577`, median `-0.004934`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.3625`, primary_mae `0.031198`, avg `0.000261`, median `-0.001443`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.4`, primary_mae `0.046674`, avg `0.012699`, median `0.020248`
- 60d: sample `80`, primary_hit `0.725`, primary_closer `0.3125`, primary_mae `0.05532`, avg `0.046609`, median `0.063468`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.015949, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4875, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.018753, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.031198, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6375, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.046674, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.3125, 'primary_mean_absolute_error': 0.05532, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014715, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015936, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.015949, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017453, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018783, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4875, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.018753, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021351, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029666, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.031198, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028278, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057912, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6375, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.046674, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04262, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065409, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.3125, 'primary_mean_absolute_error': 0.05532, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.016848`, avg `0.003004`, median `-0.000179`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.022804`, avg `0.008808`, median `0.017435`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.041331`, avg `0.002268`, median `0.004064`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.031801`, avg `0.030931`, median `0.034557`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.035422`, avg `0.054415`, median `0.061862`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.018996`, avg `0.006317`, median `0.006401`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.022862`, avg `0.009147`, median `0.017473`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.036086`, avg `0.000822`, median `0.004064`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.046569`, avg `0.018492`, median `0.030088`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.056711`, avg `0.041447`, median `0.059044`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.013826`, avg `-0.002921`, median `-0.003574`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.013587`, avg `-0.007779`, median `-0.01159`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.031468`, avg `-0.009563`, median `-0.009328`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.052573`, avg `-0.005875`, median `0.009366`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.047803`, avg `0.015071`, median `0.037766`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.015949`, avg `0.000979`, median `-0.001489`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5`, primary_mae `0.018753`, avg `-0.001577`, median `-0.004934`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.3625`, primary_mae `0.031198`, avg `0.000261`, median `-0.001443`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.4`, primary_mae `0.046674`, avg `0.012699`, median `0.020248`
- 60d: sample `80`, primary_hit `0.725`, primary_closer `0.3125`, primary_mae `0.05532`, avg `0.046609`, median `0.063468`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.015949`, avg `0.000979`, median `-0.001489`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5`, primary_mae `0.018753`, avg `-0.001577`, median `-0.004934`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.3625`, primary_mae `0.031198`, avg `0.000261`, median `-0.001443`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.4`, primary_mae `0.046674`, avg `0.012699`, median `0.020248`
- 60d: sample `80`, primary_hit `0.725`, primary_closer `0.3125`, primary_mae `0.05532`, avg `0.046609`, median `0.063468`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.0156`, avg `-0.00143`, median `-0.003948`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.018625`, avg `-0.000944`, median `-0.001187`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.036151`, avg `-0.000836`, median `-0.004104`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.062609`, avg `0.004185`, median `0.017625`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.2`, primary_mae `0.088863`, avg `0.053574`, median `0.072856`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.45`, primary_mae `0.016065`, avg `0.001782`, median `-0.000961`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.5167`, primary_mae `0.018796`, avg `-0.001788`, median `-0.005851`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.3833`, primary_mae `0.029546`, avg `0.000627`, median `-0.001153`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.041363`, avg `0.015537`, median `0.020767`
- 60d: sample `60`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.04414`, avg `0.044287`, median `0.058512`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.015949`, avg `0.000979`, median `-0.001489`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5`, primary_mae `0.018753`, avg `-0.001577`, median `-0.004934`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.3625`, primary_mae `0.031198`, avg `0.000261`, median `-0.001443`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.4`, primary_mae `0.046674`, avg `0.012699`, median `0.020248`
- 60d: sample `80`, primary_hit `0.725`, primary_closer `0.3125`, primary_mae `0.05532`, avg `0.046609`, median `0.063468`

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
