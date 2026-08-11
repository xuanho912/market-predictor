# Historical Replay Benchmark

Generated at: `2026-08-11T22:23:28.315813+00:00`
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
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.015957`
- secondary_mean_absolute_error: `0.013166`
- primary_error_advantage: `-0.002791`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.022719`
- secondary_mean_absolute_error: `0.017925`
- primary_error_advantage: `-0.004794`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.03469`
- secondary_mean_absolute_error: `0.030245`
- primary_error_advantage: `-0.004445`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.061789`
- secondary_mean_absolute_error: `0.054908`
- primary_error_advantage: `-0.006881`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.076431`
- secondary_mean_absolute_error: `0.078264`
- primary_error_advantage: `0.001833`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.013379`, as_primary `0`, as_primary_hit `None`, avg `0.002302`, median `0.004273`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.017393`, as_primary `0`, as_primary_hit `None`, avg `0.003663`, median `0.004845`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.026922`, as_primary `0`, as_primary_hit `None`, avg `0.005515`, median `0.002713`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.039738`, as_primary `0`, as_primary_hit `None`, avg `0.011209`, median `0.01201`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.066154`, as_primary `0`, as_primary_hit `None`, avg `0.024033`, median `0.038298`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.015957`, as_primary `80`, as_primary_hit `0.625`, avg `0.002302`, median `0.004273`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.022719`, as_primary `80`, as_primary_hit `0.675`, avg `0.003663`, median `0.004845`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.03469`, as_primary `80`, as_primary_hit `0.5375`, avg `0.005515`, median `0.002713`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.061789`, as_primary `80`, as_primary_hit `0.6625`, avg `0.011209`, median `0.01201`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.076431`, as_primary `80`, as_primary_hit `0.5625`, avg `0.024033`, median `0.038298`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.016388`, as_primary `0`, as_primary_hit `None`, avg `0.002302`, median `0.004273`
- 5d: sample `80`, direction_hit `0.325`, path_mae `0.021034`, as_primary `0`, as_primary_hit `None`, avg `0.003663`, median `0.004845`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.033934`, as_primary `0`, as_primary_hit `None`, avg `0.005515`, median `0.002713`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.068941`, as_primary `0`, as_primary_hit `None`, avg `0.011209`, median `0.01201`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.086161`, as_primary `0`, as_primary_hit `None`, avg `0.024033`, median `0.038298`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.013007`, as_primary `0`, as_primary_hit `None`, avg `0.002302`, median `0.004273`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.016128`, as_primary `0`, as_primary_hit `None`, avg `0.003663`, median `0.004845`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.025167`, as_primary `0`, as_primary_hit `None`, avg `0.005515`, median `0.002713`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.037147`, as_primary `0`, as_primary_hit `None`, avg `0.011209`, median `0.01201`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.061508`, as_primary `0`, as_primary_hit `None`, avg `0.024033`, median `0.038298`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.015957`, avg `0.002302`, median `0.004273`
- 5d: sample `80`, primary_hit `0.675`, primary_closer `0.4125`, primary_mae `0.022719`, avg `0.003663`, median `0.004845`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.03469`, avg `0.005515`, median `0.002713`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.425`, primary_mae `0.061789`, avg `0.011209`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.45`, primary_mae `0.076431`, avg `0.024033`, median `0.038298`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.014907`, avg `0.003951`, median `0.004555`
- 5d: sample `60`, primary_hit `0.7167`, primary_closer `0.45`, primary_mae `0.022927`, avg `0.004571`, median `0.00573`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4667`, primary_mae `0.037934`, avg `0.006126`, median `0.002713`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.4833`, primary_mae `0.064689`, avg `0.011063`, median `0.011276`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.4833`, primary_mae `0.077883`, avg `0.026167`, median `0.044393`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.019108`, avg `-0.002646`, median `0.002617`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.022097`, avg `0.00094`, median `0.00171`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.024957`, avg `0.003681`, median `0.006104`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.053087`, avg `0.011647`, median `0.02136`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.072074`, avg `0.017631`, median `0.003555`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014907, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.022097, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.024957, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.053087, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.072074, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013007, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016388, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014907, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016128, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022719, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.022097, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025167, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03469, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.024957, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037147, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.068941, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.053087, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061508, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.086161, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.072074, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.019378`, avg `-0.003813`, median `-0.002198`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.018893`, avg `0.000899`, median `0.003509`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.022405`, avg `0.002265`, median `0.002208`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.052642`, avg `0.009259`, median `0.014663`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.091568`, avg `-0.012738`, median `-0.032183`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.02142`, avg `-0.007024`, median `-0.002198`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.1875`, primary_mae `0.024179`, avg `-0.003863`, median `-0.001055`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.027516`, avg `-0.002261`, median `-0.005041`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.060683`, avg `0.001043`, median `0.014663`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.079695`, avg `0.004666`, median `-0.012556`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.025866`, avg `0.004971`, median `0.010545`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.1875`, primary_mae `0.045449`, avg `0.001129`, median `0.005967`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.064499`, avg `0.012211`, median `-0.002227`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.1875`, primary_mae `0.099251`, avg `0.028551`, median `0.013042`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.124333`, avg `0.052406`, median `0.052729`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.015957`, avg `0.002302`, median `0.004273`
- 5d: sample `80`, primary_hit `0.675`, primary_closer `0.4125`, primary_mae `0.022719`, avg `0.003663`, median `0.004845`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.03469`, avg `0.005515`, median `0.002713`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.425`, primary_mae `0.061789`, avg `0.011209`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.45`, primary_mae `0.076431`, avg `0.024033`, median `0.038298`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.015957`, avg `0.002302`, median `0.004273`
- 5d: sample `80`, primary_hit `0.675`, primary_closer `0.4125`, primary_mae `0.022719`, avg `0.003663`, median `0.004845`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.03469`, avg `0.005515`, median `0.002713`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.425`, primary_mae `0.061789`, avg `0.011209`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.45`, primary_mae `0.076431`, avg `0.024033`, median `0.038298`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.013554`, avg `-0.002913`, median `-0.00051`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.425`, primary_mae `0.015077`, avg `0.00193`, median `0.002849`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.02009`, avg `0.001012`, median `-8e-05`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.041362`, avg `0.00494`, median `0.010494`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.066362`, avg `0.000607`, median `-0.017782`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.024114`, avg `0.007899`, median `0.011608`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.2`, primary_mae `0.043598`, avg `0.00437`, median `0.010594`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.06114`, avg `0.016412`, median `0.006552`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.095269`, avg `0.035622`, median `0.022145`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.110969`, avg `0.064751`, median `0.071616`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.015957`, avg `0.002302`, median `0.004273`
- 5d: sample `80`, primary_hit `0.675`, primary_closer `0.4125`, primary_mae `0.022719`, avg `0.003663`, median `0.004845`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.03469`, avg `0.005515`, median `0.002713`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.425`, primary_mae `0.061789`, avg `0.011209`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.45`, primary_mae `0.076431`, avg `0.024033`, median `0.038298`

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
