# Historical Replay Benchmark

Generated at: `2026-10-29T01:22:48.861450+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `PROMISING`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_mixed_or_not_better_keep_confidence_capped`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.01875`
- secondary_mean_absolute_error: `0.019816`
- primary_error_advantage: `0.001066`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.025705`
- secondary_mean_absolute_error: `0.027271`
- primary_error_advantage: `0.001566`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.040003`
- secondary_mean_absolute_error: `0.04909`
- primary_error_advantage: `0.009087`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6167`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.061515`
- secondary_mean_absolute_error: `0.062373`
- primary_error_advantage: `0.000858`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.048299`
- secondary_mean_absolute_error: `0.052318`
- primary_error_advantage: `0.004019`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.017193`, as_primary `0`, as_primary_hit `None`, avg `0.004118`, median `0.008703`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.023152`, as_primary `0`, as_primary_hit `None`, avg `0.002707`, median `0.005702`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.035869`, as_primary `0`, as_primary_hit `None`, avg `-0.001761`, median `0.004986`
- 20d: sample `80`, direction_hit `0.5125`, path_mae `0.041801`, as_primary `0`, as_primary_hit `None`, avg `-0.003452`, median `0.000794`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.044388`, as_primary `0`, as_primary_hit `None`, avg `0.068673`, median `0.070768`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.01931`, as_primary `40`, as_primary_hit `0.65`, avg `0.004118`, median `0.008703`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.027906`, as_primary `40`, as_primary_hit `0.575`, avg `0.002707`, median `0.005702`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.045212`, as_primary `40`, as_primary_hit `0.55`, avg `-0.001761`, median `0.004986`
- 20d: sample `80`, direction_hit `0.5125`, path_mae `0.062324`, as_primary `40`, as_primary_hit `0.575`, avg `-0.003452`, median `0.000794`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.049918`, as_primary `40`, as_primary_hit `0.875`, avg `0.068673`, median `0.070768`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.019757`, as_primary `40`, as_primary_hit `0.6`, avg `0.004118`, median `0.008703`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.025832`, as_primary `40`, as_primary_hit `0.575`, avg `0.002707`, median `0.005702`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.04788`, as_primary `40`, as_primary_hit `0.55`, avg `-0.001761`, median `0.004986`
- 20d: sample `80`, direction_hit `0.4875`, path_mae `0.066998`, as_primary `40`, as_primary_hit `0.45`, avg `-0.003452`, median `0.000794`
- 60d: sample `80`, direction_hit `0.1375`, path_mae `0.051052`, as_primary `40`, as_primary_hit `0.85`, avg `0.068673`, median `0.070768`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.017897`, as_primary `0`, as_primary_hit `None`, avg `0.004118`, median `0.008703`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.022928`, as_primary `0`, as_primary_hit `None`, avg `0.002707`, median `0.005702`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.03468`, as_primary `0`, as_primary_hit `None`, avg `-0.001761`, median `0.004986`
- 20d: sample `80`, direction_hit `0.5125`, path_mae `0.04093`, as_primary `0`, as_primary_hit `None`, avg `-0.003452`, median `0.000794`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.043684`, as_primary `0`, as_primary_hit `None`, avg `0.068673`, median `0.070768`

## Edge Status Performance

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.575`, primary_mae `0.018374`, avg `0.006328`, median `0.011428`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.028115`, avg `0.003431`, median `0.002693`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.044166`, avg `0.000319`, median `0.008776`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.575`, primary_mae `0.073506`, avg `-0.000694`, median `0.014674`
- 60d: sample `40`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.048102`, avg `0.064306`, median `0.06755`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.019127`, avg `0.001909`, median `0.007275`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.023295`, avg `0.001984`, median `0.007226`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.035839`, avg `-0.00384`, median `0.004986`
- 20d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.049524`, avg `-0.006209`, median `-0.013843`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.5`, primary_mae `0.048496`, avg `0.073039`, median `0.075016`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.02042`, avg `0.006103`, median `0.018118`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.0322`, avg `0.004961`, median `0.004099`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.04051`, avg `0.005743`, median `0.02112`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.076223`, avg `-0.001566`, median `0.007553`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.4`, primary_mae `0.040072`, avg `0.061063`, median `0.062686`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.019127`, avg `0.001909`, median `0.007275`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.023295`, avg `0.001984`, median `0.007226`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.035839`, avg `-0.00384`, median `0.004986`
- 20d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.049524`, avg `-0.006209`, median `-0.013843`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.5`, primary_mae `0.048496`, avg `0.073039`, median `0.075016`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.016327`, avg `0.006552`, median `0.00957`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.02403`, avg `0.001902`, median `-0.000823`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.65`, primary_mae `0.047822`, avg `-0.005105`, median `0.000755`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.070789`, avg `0.000177`, median `0.014674`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.6`, primary_mae `0.056132`, avg `0.067549`, median `0.091555`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.016327, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.023295, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.035839, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.049524, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.040072, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017193, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019757, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.016327, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022928, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027906, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.023295, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03468, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04788, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.035839, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04093, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066998, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.049524, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043684, 'direction_hit_rate': 0.8625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051052, 'direction_hit_rate': 0.1375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.040072, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.01694`, avg `0.011129`, median `0.018909`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.03233`, avg `0.008236`, median `0.016774`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.046351`, avg `0.003698`, median `0.004277`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.076446`, avg `-0.003955`, median `-0.002353`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.048351`, avg `0.055409`, median `0.067424`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.018226`, avg `0.00809`, median `0.018118`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.029918`, avg `0.006789`, median `0.008332`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.041184`, avg `0.005001`, median `0.030411`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.068789`, avg `0.004771`, median `0.024009`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.4375`, primary_mae `0.039423`, avg `0.062166`, median `0.067424`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.024708`, avg `0.004748`, median `0.009216`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.02448`, avg `0.006219`, median `0.011017`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.035149`, avg `0.012153`, median `0.010405`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.042777`, avg `0.007538`, median `0.001267`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.3125`, primary_mae `0.059323`, avg `0.119667`, median `0.125416`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.01875`, avg `0.004118`, median `0.008703`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4625`, primary_mae `0.025705`, avg `0.002707`, median `0.005702`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.040003`, avg `-0.001761`, median `0.004986`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.061515`, avg `-0.003452`, median `0.000794`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.048299`, avg `0.068673`, median `0.070768`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.01875`, avg `0.004118`, median `0.008703`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4625`, primary_mae `0.025705`, avg `0.002707`, median `0.005702`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.040003`, avg `-0.001761`, median `0.004986`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.061515`, avg `-0.003452`, median `0.000794`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.048299`, avg `0.068673`, median `0.070768`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.55`, primary_mae `0.016532`, avg `0.004733`, median `0.008503`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.5167`, primary_mae `0.025586`, avg `0.001869`, median `0.001561`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.6167`, primary_mae `0.041247`, avg `-0.005555`, median `-0.003821`
- 20d: sample `60`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.06783`, avg `-0.006546`, median `-0.003369`
- 60d: sample `60`, primary_hit `0.6833`, primary_closer `0.5333`, primary_mae `0.046238`, avg `0.053984`, median `0.059547`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.025406`, avg `0.002272`, median `0.009216`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.026062`, avg `0.005224`, median `0.011017`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.03627`, avg `0.009622`, median `0.010405`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.04257`, avg `0.00583`, median `0.001267`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.4`, primary_mae `0.054482`, avg `0.112737`, median `0.111654`

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
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.020867`, avg `0.004412`, median `0.009346`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.025046`, avg `0.003563`, median `0.008365`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.042046`, avg `0.002259`, median `0.009633`
- 20d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.056679`, avg `0.003004`, median `0.003955`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.055307`, avg `0.090143`, median `0.1012`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.01875`, avg `0.004118`, median `0.008703`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4625`, primary_mae `0.025705`, avg `0.002707`, median `0.005702`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.040003`, avg `-0.001761`, median `0.004986`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.061515`, avg `-0.003452`, median `0.000794`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.048299`, avg `0.068673`, median `0.070768`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
