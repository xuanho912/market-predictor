# Historical Replay Benchmark

Generated at: `2026-08-19T23:12:54.302471+00:00`
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
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.016111`
- secondary_mean_absolute_error: `0.013803`
- primary_error_advantage: `-0.002308`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.022824`
- secondary_mean_absolute_error: `0.017424`
- primary_error_advantage: `-0.0054`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.033165`
- secondary_mean_absolute_error: `0.02599`
- primary_error_advantage: `-0.007175`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3333`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.058149`
- secondary_mean_absolute_error: `0.044011`
- primary_error_advantage: `-0.014138`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.2667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.081118`
- secondary_mean_absolute_error: `0.066266`
- primary_error_advantage: `-0.014852`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.015274`, as_primary `0`, as_primary_hit `None`, avg `0.003615`, median `0.005013`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.020483`, as_primary `0`, as_primary_hit `None`, avg `0.004049`, median `0.003864`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.026845`, as_primary `0`, as_primary_hit `None`, avg `0.006161`, median `0.010225`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.041097`, as_primary `0`, as_primary_hit `None`, avg `0.015394`, median `0.017926`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.066898`, as_primary `0`, as_primary_hit `None`, avg `0.026943`, median `0.040689`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.018659`, as_primary `60`, as_primary_hit `0.5833`, avg `0.003615`, median `0.005013`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.028334`, as_primary `60`, as_primary_hit `0.6333`, avg `0.004049`, median `0.003864`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.03655`, as_primary `60`, as_primary_hit `0.6167`, avg `0.006161`, median `0.010225`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.062107`, as_primary `60`, as_primary_hit `0.6833`, avg `0.015394`, median `0.017926`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.0848`, as_primary `60`, as_primary_hit `0.55`, avg `0.026943`, median `0.040689`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015242`, as_primary `20`, as_primary_hit `0.6`, avg `0.003615`, median `0.005013`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.020615`, as_primary `20`, as_primary_hit `0.45`, avg `0.004049`, median `0.003864`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.039054`, as_primary `20`, as_primary_hit `0.75`, avg `0.006161`, median `0.010225`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.073432`, as_primary `20`, as_primary_hit `0.8`, avg `0.015394`, median `0.017926`
- 60d: sample `80`, direction_hit `0.3875`, path_mae `0.086274`, as_primary `20`, as_primary_hit `0.8`, avg `0.026943`, median `0.040689`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.013791`, as_primary `0`, as_primary_hit `None`, avg `0.003615`, median `0.005013`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.017378`, as_primary `0`, as_primary_hit `None`, avg `0.004049`, median `0.003864`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.024689`, as_primary `0`, as_primary_hit `None`, avg `0.006161`, median `0.010225`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.037061`, as_primary `0`, as_primary_hit `None`, avg `0.015394`, median `0.017926`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.06514`, as_primary `0`, as_primary_hit `None`, avg `0.026943`, median `0.040689`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.016111`, avg `0.003615`, median `0.005013`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3625`, primary_mae `0.022824`, avg `0.004049`, median `0.003864`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.033165`, avg `0.006161`, median `0.010225`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.058149`, avg `0.015394`, median `0.017926`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.081118`, avg `0.026943`, median `0.040689`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.015209`, avg `0.00157`, median `0.001491`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.325`, primary_mae `0.019373`, avg `0.004798`, median `0.004963`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.525`, primary_mae `0.026233`, avg `0.002368`, median `0.010085`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.042078`, avg `0.010271`, median `0.012453`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.071122`, avg `0.014353`, median `-0.004635`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.017014`, avg `0.00566`, median `0.006103`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.026274`, avg `0.0033`, median `0.00203`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.040098`, avg `0.009953`, median `0.010562`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.25`, primary_mae `0.07422`, avg `0.020516`, median `0.023344`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.091114`, avg `0.039533`, median `0.064891`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015209, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.019373, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.026233, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.042078, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.071122, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013791, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018659, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015209, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017378, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028334, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.019373, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024689, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039054, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.026233, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037061, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073432, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.042078, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06514, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.086274, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.071122, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.016456`, avg `0.005624`, median `0.005338`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.017441`, avg `0.010667`, median `0.009586`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.018994`, avg `0.018814`, median `0.023382`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.049987`, avg `0.02311`, median `0.015956`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.095087`, avg `-0.000717`, median `-0.025539`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.021017`, avg `0.001864`, median `0.005338`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.023241`, avg `0.007078`, median `0.00778`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.03127`, avg `0.008295`, median `0.013095`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.05313`, avg `0.021521`, median `0.023697`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.069882`, avg `0.026504`, median `0.013133`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.018663`, avg `0.00607`, median `0.005519`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.025321`, avg `0.00113`, median `-0.005981`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.042747`, avg `0.01685`, median `0.010562`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.084155`, avg `0.037119`, median `0.022139`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.085622`, avg `0.071792`, median `0.072493`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.016111`, avg `0.003615`, median `0.005013`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3625`, primary_mae `0.022824`, avg `0.004049`, median `0.003864`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.033165`, avg `0.006161`, median `0.010225`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.058149`, avg `0.015394`, median `0.017926`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.081118`, avg `0.026943`, median `0.040689`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.016111`, avg `0.003615`, median `0.005013`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3625`, primary_mae `0.022824`, avg `0.004049`, median `0.003864`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.033165`, avg `0.006161`, median `0.010225`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.058149`, avg `0.015394`, median `0.017926`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.081118`, avg `0.026943`, median `0.040689`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.015209`, avg `0.00157`, median `0.001491`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.325`, primary_mae `0.019373`, avg `0.004798`, median `0.004963`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.525`, primary_mae `0.026233`, avg `0.002368`, median `0.010085`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.042078`, avg `0.010271`, median `0.012453`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.071122`, avg `0.014353`, median `-0.004635`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.016464`, avg `0.005053`, median `0.005519`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.022089`, avg `0.000584`, median `-0.005524`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.040032`, avg `0.016206`, median `0.012095`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.081487`, avg `0.037002`, median `0.029023`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.35`, primary_mae `0.081432`, avg `0.067743`, median `0.072493`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.016111`, avg `0.003615`, median `0.005013`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3625`, primary_mae `0.022824`, avg `0.004049`, median `0.003864`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.033165`, avg `0.006161`, median `0.010225`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.058149`, avg `0.015394`, median `0.017926`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.081118`, avg `0.026943`, median `0.040689`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.016111`, avg `0.003615`, median `0.005013`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3625`, primary_mae `0.022824`, avg `0.004049`, median `0.003864`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.033165`, avg `0.006161`, median `0.010225`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.058149`, avg `0.015394`, median `0.017926`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.081118`, avg `0.026943`, median `0.040689`

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
