# Historical Replay Benchmark

Generated at: `2026-08-12T03:32:14.478792+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
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
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.015957`
- secondary_mean_absolute_error: `0.013007`
- primary_error_advantage: `-0.00295`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.022719`
- secondary_mean_absolute_error: `0.016128`
- primary_error_advantage: `-0.006591`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.03469`
- secondary_mean_absolute_error: `0.025167`
- primary_error_advantage: `-0.009523`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.061789`
- secondary_mean_absolute_error: `0.037147`
- primary_error_advantage: `-0.024642`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.225`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.076431`
- secondary_mean_absolute_error: `0.061508`
- primary_error_advantage: `-0.014923`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

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
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.35`, primary_mae `0.016058`, avg `0.002359`, median `0.003167`
- 5d: sample `40`, primary_hit `0.725`, primary_closer `0.325`, primary_mae `0.025828`, avg `0.003644`, median `0.00416`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.038181`, avg `0.007377`, median `0.00013`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.275`, primary_mae `0.062453`, avg `0.016927`, median `0.011276`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.08581`, avg `0.024167`, median `0.007512`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.015857`, avg `0.002244`, median `0.006103`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.019611`, avg `0.003682`, median `0.005323`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.031198`, avg `0.003652`, median `0.005212`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.25`, primary_mae `0.061124`, avg `0.005491`, median `0.015334`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.067052`, avg `0.023899`, median `0.049838`

## Predictor Performance

### bounce_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.015957`, avg `0.002302`, median `0.004273`
- 5d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.022719`, avg `0.003663`, median `0.004845`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.03469`, avg `0.005515`, median `0.002713`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.2625`, primary_mae `0.061789`, avg `0.011209`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.076431`, avg `0.024033`, median `0.038298`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015957, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.022719, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5375, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.03469, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6625, 'primary_closer_than_secondary_rate': 0.2625, 'primary_mean_absolute_error': 0.061789, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5625, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.076431, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013007, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016388, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015957, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016128, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022719, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.022719, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025167, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03469, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5375, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.03469, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037147, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.068941, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6625, 'primary_closer_than_secondary_rate': 0.2625, 'primary_mean_absolute_error': 0.061789, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061508, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.086161, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5625, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.076431, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

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
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.02142`, avg `-0.007024`, median `-0.002198`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.1875`, primary_mae `0.024179`, avg `-0.003863`, median `-0.001055`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.027516`, avg `-0.002261`, median `-0.005041`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.060683`, avg `0.001043`, median `0.014663`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.079695`, avg `0.004666`, median `-0.012556`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.015957`, avg `0.002302`, median `0.004273`
- 5d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.022719`, avg `0.003663`, median `0.004845`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.03469`, avg `0.005515`, median `0.002713`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.2625`, primary_mae `0.061789`, avg `0.011209`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.076431`, avg `0.024033`, median `0.038298`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.015957`, avg `0.002302`, median `0.004273`
- 5d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.022719`, avg `0.003663`, median `0.004845`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.03469`, avg `0.005515`, median `0.002713`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.2625`, primary_mae `0.061789`, avg `0.011209`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.076431`, avg `0.024033`, median `0.038298`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.013554`, avg `-0.002913`, median `-0.00051`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.015077`, avg `0.00193`, median `0.002849`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.02009`, avg `0.001012`, median `-8e-05`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.3`, primary_mae `0.041362`, avg `0.00494`, median `0.010494`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.066362`, avg `0.000607`, median `-0.017782`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.024114`, avg `0.007899`, median `0.011608`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.2`, primary_mae `0.043598`, avg `0.00437`, median `0.010594`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.06114`, avg `0.016412`, median `0.006552`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.095269`, avg `0.035622`, median `0.022145`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.110969`, avg `0.064751`, median `0.071616`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.015957`, avg `0.002302`, median `0.004273`
- 5d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.022719`, avg `0.003663`, median `0.004845`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.03469`, avg `0.005515`, median `0.002713`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.2625`, primary_mae `0.061789`, avg `0.011209`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.076431`, avg `0.024033`, median `0.038298`

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
