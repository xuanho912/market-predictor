# Historical Replay Benchmark

Generated at: `2026-06-15T14:41:20.750310+00:00`
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
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.015559`
- secondary_mean_absolute_error: `0.013521`
- primary_error_advantage: `-0.002038`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.02116`
- secondary_mean_absolute_error: `0.017799`
- primary_error_advantage: `-0.003361`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.029796`
- secondary_mean_absolute_error: `0.026604`
- primary_error_advantage: `-0.003192`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.052387`
- secondary_mean_absolute_error: `0.045713`
- primary_error_advantage: `-0.006674`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.0767`
- secondary_mean_absolute_error: `0.060681`
- primary_error_advantage: `-0.016019`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.014235`, as_primary `0`, as_primary_hit `None`, avg `0.004916`, median `0.005843`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.01881`, as_primary `0`, as_primary_hit `None`, avg `0.005673`, median `0.005601`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.024028`, as_primary `0`, as_primary_hit `None`, avg `0.007044`, median `0.00719`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.034569`, as_primary `0`, as_primary_hit `None`, avg `0.009445`, median `0.017134`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.058307`, as_primary `0`, as_primary_hit `None`, avg `0.028139`, median `0.033835`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.015559`, as_primary `80`, as_primary_hit `0.6375`, avg `0.004916`, median `0.005843`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.02116`, as_primary `80`, as_primary_hit `0.6375`, avg `0.005673`, median `0.005601`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.029796`, as_primary `80`, as_primary_hit `0.5875`, avg `0.007044`, median `0.00719`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.052387`, as_primary `80`, as_primary_hit `0.6875`, avg `0.009445`, median `0.017134`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.0767`, as_primary `80`, as_primary_hit `0.5875`, avg `0.028139`, median `0.033835`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.01403`, as_primary `0`, as_primary_hit `None`, avg `0.004916`, median `0.005843`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.018547`, as_primary `0`, as_primary_hit `None`, avg `0.005673`, median `0.005601`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.028492`, as_primary `0`, as_primary_hit `None`, avg `0.007044`, median `0.00719`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.061958`, as_primary `0`, as_primary_hit `None`, avg `0.009445`, median `0.017134`
- 60d: sample `80`, direction_hit `0.4125`, path_mae `0.071006`, as_primary `0`, as_primary_hit `None`, avg `0.028139`, median `0.033835`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.012962`, as_primary `0`, as_primary_hit `None`, avg `0.004916`, median `0.005843`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.01697`, as_primary `0`, as_primary_hit `None`, avg `0.005673`, median `0.005601`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.022632`, as_primary `0`, as_primary_hit `None`, avg `0.007044`, median `0.00719`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.032767`, as_primary `0`, as_primary_hit `None`, avg `0.009445`, median `0.017134`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.053731`, as_primary `0`, as_primary_hit `None`, avg `0.028139`, median `0.033835`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.015559`, avg `0.004916`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.02116`, avg `0.005673`, median `0.005601`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.029796`, avg `0.007044`, median `0.00719`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3625`, primary_mae `0.052387`, avg `0.009445`, median `0.017134`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.0767`, avg `0.028139`, median `0.033835`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.55`, primary_mae `0.014822`, avg `0.006685`, median `0.00609`
- 5d: sample `40`, primary_hit `0.75`, primary_closer `0.525`, primary_mae `0.017862`, avg `0.008257`, median `0.008615`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.525`, primary_mae `0.026032`, avg `0.005138`, median `0.00719`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.054626`, avg `0.002509`, median `0.01201`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.080115`, avg `0.010788`, median `-0.00576`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.016296`, avg `0.003147`, median `0.00509`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.3`, primary_mae `0.024457`, avg `0.00309`, median `0.001516`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.325`, primary_mae `0.033561`, avg `0.008949`, median `0.006918`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.225`, primary_mae `0.050149`, avg `0.01638`, median `0.020209`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.325`, primary_mae `0.073285`, avg `0.04549`, median `0.051612`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.014822, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.017862, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.026032, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.050149, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.073285, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012962, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015559, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.014822, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01697, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02116, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.017862, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022632, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029796, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.026032, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032767, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061958, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.050149, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053731, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0767, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.073285, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.01568`, avg `-0.007791`, median `-0.007158`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.023023`, avg `-0.011833`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.01504`, avg `0.008706`, median `0.006918`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.0`, primary_mae `0.022072`, avg `0.028852`, median `0.030181`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.032369`, avg `0.054535`, median `0.055714`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.016113`, avg `-0.004745`, median `-0.006238`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.019209`, avg `-0.005696`, median `-0.007506`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.015703`, avg `0.008511`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.125`, primary_mae `0.030111`, avg `0.021476`, median `0.027661`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.055254`, avg `0.032715`, median `0.039481`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.016113`, avg `-0.004745`, median `-0.006238`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.019209`, avg `-0.005696`, median `-0.007506`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.015703`, avg `0.008511`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.125`, primary_mae `0.030111`, avg `0.021476`, median `0.027661`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.055254`, avg `0.032715`, median `0.039481`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.015559`, avg `0.004916`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.02116`, avg `0.005673`, median `0.005601`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.029796`, avg `0.007044`, median `0.00719`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3625`, primary_mae `0.052387`, avg `0.009445`, median `0.017134`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.0767`, avg `0.028139`, median `0.033835`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.015559`, avg `0.004916`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.02116`, avg `0.005673`, median `0.005601`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.029796`, avg `0.007044`, median `0.00719`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3625`, primary_mae `0.052387`, avg `0.009445`, median `0.017134`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.0767`, avg `0.028139`, median `0.033835`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.015559`, avg `0.004916`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.02116`, avg `0.005673`, median `0.005601`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.029796`, avg `0.007044`, median `0.00719`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3625`, primary_mae `0.052387`, avg `0.009445`, median `0.017134`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.0767`, avg `0.028139`, median `0.033835`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.015559`, avg `0.004916`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.02116`, avg `0.005673`, median `0.005601`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.029796`, avg `0.007044`, median `0.00719`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3625`, primary_mae `0.052387`, avg `0.009445`, median `0.017134`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.0767`, avg `0.028139`, median `0.033835`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.015559`, avg `0.004916`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.02116`, avg `0.005673`, median `0.005601`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.029796`, avg `0.007044`, median `0.00719`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3625`, primary_mae `0.052387`, avg `0.009445`, median `0.017134`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.0767`, avg `0.028139`, median `0.033835`

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
