# Historical Replay Benchmark

Generated at: `2026-08-18T13:12:10.247948+00:00`
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
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.018026`
- secondary_mean_absolute_error: `0.014007`
- primary_error_advantage: `-0.004019`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.026266`
- secondary_mean_absolute_error: `0.019252`
- primary_error_advantage: `-0.007014`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3875`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.033121`
- secondary_mean_absolute_error: `0.023063`
- primary_error_advantage: `-0.010058`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.7375`
- secondary_hit_rate: `0.9375`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.04108`
- secondary_mean_absolute_error: `0.027451`
- primary_error_advantage: `-0.013629`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3125`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.825`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.071352`
- secondary_mean_absolute_error: `0.058512`
- primary_error_advantage: `-0.01284`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7`, path_mae `0.014157`, as_primary `0`, as_primary_hit `None`, avg `0.007177`, median `0.008622`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.021382`, as_primary `0`, as_primary_hit `None`, avg `0.009779`, median `0.009975`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.026067`, as_primary `0`, as_primary_hit `None`, avg `0.019647`, median `0.017418`
- 20d: sample `80`, direction_hit `0.9375`, path_mae `0.035249`, as_primary `0`, as_primary_hit `None`, avg `0.040128`, median `0.031001`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.058125`, as_primary `0`, as_primary_hit `None`, avg `0.04995`, median `0.056803`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7`, path_mae `0.018132`, as_primary `60`, as_primary_hit `0.7167`, avg `0.007177`, median `0.008622`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.029378`, as_primary `60`, as_primary_hit `0.6833`, avg `0.009779`, median `0.009975`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.033934`, as_primary `60`, as_primary_hit `0.7667`, avg `0.019647`, median `0.017418`
- 20d: sample `80`, direction_hit `0.9375`, path_mae `0.050066`, as_primary `60`, as_primary_hit `0.95`, avg `0.040128`, median `0.031001`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.071159`, as_primary `60`, as_primary_hit `0.8333`, avg `0.04995`, median `0.056803`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3`, path_mae `0.021528`, as_primary `20`, as_primary_hit `0.65`, avg `0.007177`, median `0.008622`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.027726`, as_primary `20`, as_primary_hit `0.55`, avg `0.009779`, median `0.009975`
- 10d: sample `80`, direction_hit `0.2875`, path_mae `0.02885`, as_primary `20`, as_primary_hit `0.55`, avg `0.019647`, median `0.017418`
- 20d: sample `80`, direction_hit `0.0625`, path_mae `0.035859`, as_primary `20`, as_primary_hit `0.9`, avg `0.040128`, median `0.031001`
- 60d: sample `80`, direction_hit `0.175`, path_mae `0.082556`, as_primary `20`, as_primary_hit `0.8`, avg `0.04995`, median `0.056803`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7`, path_mae `0.014007`, as_primary `0`, as_primary_hit `None`, avg `0.007177`, median `0.008622`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.019252`, as_primary `0`, as_primary_hit `None`, avg `0.009779`, median `0.009975`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.023063`, as_primary `0`, as_primary_hit `None`, avg `0.019647`, median `0.017418`
- 20d: sample `80`, direction_hit `0.9375`, path_mae `0.027451`, as_primary `0`, as_primary_hit `None`, avg `0.040128`, median `0.031001`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.058512`, as_primary `0`, as_primary_hit `None`, avg `0.04995`, median `0.056803`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.7167`, primary_closer `0.4167`, primary_mae `0.015217`, avg `0.007233`, median `0.008328`
- 5d: sample `60`, primary_hit `0.6833`, primary_closer `0.3833`, primary_mae `0.025446`, avg `0.010309`, median `0.011847`
- 10d: sample `60`, primary_hit `0.7667`, primary_closer `0.3667`, primary_mae `0.027655`, avg `0.01903`, median `0.018404`
- 20d: sample `60`, primary_hit `0.95`, primary_closer `0.2667`, primary_mae `0.036585`, avg `0.033977`, median `0.028861`
- 60d: sample `60`, primary_hit `0.8333`, primary_closer `0.4167`, primary_mae `0.057368`, avg `0.046898`, median `0.057989`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.026452`, avg `0.007009`, median `0.008622`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.028723`, avg `0.008189`, median `0.003514`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.04952`, avg `0.021497`, median `0.004425`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.45`, primary_mae `0.054565`, avg `0.058581`, median `0.033477`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.113307`, avg `0.059106`, median `0.049401`

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
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.018026`, avg `0.007177`, median `0.008622`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.026266`, avg `0.009779`, median `0.009975`
- 10d: sample `80`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.033121`, avg `0.019647`, median `0.017418`
- 20d: sample `80`, primary_hit `0.7375`, primary_closer `0.3125`, primary_mae `0.04108`, avg `0.040128`, median `0.031001`
- 60d: sample `80`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.071352`, avg `0.04995`, median `0.056803`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.018026, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.026266, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6875, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.033121, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.7375, 'primary_closer_than_secondary_rate': 0.3125, 'primary_mean_absolute_error': 0.04108, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.071352, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014007, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021528, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.018026, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019252, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029378, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.026266, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023063, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033934, 'direction_hit_rate': 0.7125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6875, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.033121, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7375, 'secondary_hit_rate': 0.9375, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027451, 'direction_hit_rate': 0.9375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050066, 'direction_hit_rate': 0.9375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.7375, 'primary_closer_than_secondary_rate': 0.3125, 'primary_mean_absolute_error': 0.04108, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.825, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058125, 'direction_hit_rate': 0.825}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.082556, 'direction_hit_rate': 0.175}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.071352, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.007004`, avg `0.018679`, median `0.018163`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.016563`, avg `0.022737`, median `0.026166`
- 10d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.023586`, avg `0.028959`, median `0.033393`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.024924`, avg `0.059291`, median `0.069475`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.625`, primary_mae `0.015242`, avg `0.092921`, median `0.091366`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.01739`, avg `0.00755`, median `0.012678`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.029005`, avg `0.00932`, median `0.009975`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.038283`, avg `0.014262`, median `0.009092`
- 20d: sample `16`, primary_hit `1.0`, primary_closer `0.25`, primary_mae `0.041139`, avg `0.0424`, median `0.032962`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.4375`, primary_mae `0.046271`, avg `0.063202`, median `0.085138`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.025528`, avg `0.004885`, median `0.005184`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.027271`, avg `0.00598`, median `0.001408`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.046127`, avg `0.017393`, median `-0.002698`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.4375`, primary_mae `0.052375`, avg `0.055577`, median `0.033477`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.102447`, avg `0.038965`, median `0.036588`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.018026`, avg `0.007177`, median `0.008622`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.026266`, avg `0.009779`, median `0.009975`
- 10d: sample `80`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.033121`, avg `0.019647`, median `0.017418`
- 20d: sample `80`, primary_hit `0.7375`, primary_closer `0.3125`, primary_mae `0.04108`, avg `0.040128`, median `0.031001`
- 60d: sample `80`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.071352`, avg `0.04995`, median `0.056803`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.018026`, avg `0.007177`, median `0.008622`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.026266`, avg `0.009779`, median `0.009975`
- 10d: sample `80`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.033121`, avg `0.019647`, median `0.017418`
- 20d: sample `80`, primary_hit `0.7375`, primary_closer `0.3125`, primary_mae `0.04108`, avg `0.040128`, median `0.031001`
- 60d: sample `80`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.071352`, avg `0.04995`, median `0.056803`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.7167`, primary_closer `0.4167`, primary_mae `0.015217`, avg `0.007233`, median `0.008328`
- 5d: sample `60`, primary_hit `0.6833`, primary_closer `0.3833`, primary_mae `0.025446`, avg `0.010309`, median `0.011847`
- 10d: sample `60`, primary_hit `0.7667`, primary_closer `0.3667`, primary_mae `0.027655`, avg `0.01903`, median `0.018404`
- 20d: sample `60`, primary_hit `0.95`, primary_closer `0.2667`, primary_mae `0.036585`, avg `0.033977`, median `0.028861`
- 60d: sample `60`, primary_hit `0.8333`, primary_closer `0.4167`, primary_mae `0.057368`, avg `0.046898`, median `0.057989`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.026452`, avg `0.007009`, median `0.008622`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.028723`, avg `0.008189`, median `0.003514`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.04952`, avg `0.021497`, median `0.004425`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.45`, primary_mae `0.054565`, avg `0.058581`, median `0.033477`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.113307`, avg `0.059106`, median `0.049401`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.018026`, avg `0.007177`, median `0.008622`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.026266`, avg `0.009779`, median `0.009975`
- 10d: sample `80`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.033121`, avg `0.019647`, median `0.017418`
- 20d: sample `80`, primary_hit `0.7375`, primary_closer `0.3125`, primary_mae `0.04108`, avg `0.040128`, median `0.031001`
- 60d: sample `80`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.071352`, avg `0.04995`, median `0.056803`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.018026`, avg `0.007177`, median `0.008622`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.026266`, avg `0.009779`, median `0.009975`
- 10d: sample `80`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.033121`, avg `0.019647`, median `0.017418`
- 20d: sample `80`, primary_hit `0.7375`, primary_closer `0.3125`, primary_mae `0.04108`, avg `0.040128`, median `0.031001`
- 60d: sample `80`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.071352`, avg `0.04995`, median `0.056803`

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
