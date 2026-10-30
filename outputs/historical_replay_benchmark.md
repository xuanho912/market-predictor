# Historical Replay Benchmark

Generated at: `2026-10-30T00:18:27.338890+00:00`
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
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.019624`
- secondary_mean_absolute_error: `0.020353`
- primary_error_advantage: `0.000729`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.028484`
- secondary_mean_absolute_error: `0.026421`
- primary_error_advantage: `-0.002063`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.043044`
- secondary_mean_absolute_error: `0.044631`
- primary_error_advantage: `0.001587`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.060049`
- secondary_mean_absolute_error: `0.063443`
- primary_error_advantage: `0.003394`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.050039`
- secondary_mean_absolute_error: `0.04935`
- primary_error_advantage: `-0.000689`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.017881`, as_primary `0`, as_primary_hit `None`, avg `0.003102`, median `0.007812`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.024065`, as_primary `0`, as_primary_hit `None`, avg `0.001048`, median `0.004099`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.034783`, as_primary `0`, as_primary_hit `None`, avg `-0.001638`, median `0.001504`
- 20d: sample `80`, direction_hit `0.5125`, path_mae `0.041151`, as_primary `0`, as_primary_hit `None`, avg `-0.004544`, median `0.000794`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.044634`, as_primary `0`, as_primary_hit `None`, avg `0.067591`, median `0.069096`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.018015`, as_primary `60`, as_primary_hit `0.6333`, avg `0.003102`, median `0.007812`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.026761`, as_primary `60`, as_primary_hit `0.55`, avg `0.001048`, median `0.004099`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.042362`, as_primary `60`, as_primary_hit `0.5`, avg `-0.001638`, median `0.001504`
- 20d: sample `80`, direction_hit `0.5125`, path_mae `0.061033`, as_primary `60`, as_primary_hit `0.5`, avg `-0.004544`, median `0.000794`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.049801`, as_primary `60`, as_primary_hit `0.8167`, avg `0.067591`, median `0.069096`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.022139`, as_primary `20`, as_primary_hit `0.55`, avg `0.003102`, median `0.007812`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.027766`, as_primary `20`, as_primary_hit `0.6`, avg `0.001048`, median `0.004099`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.047111`, as_primary `20`, as_primary_hit `0.65`, avg `-0.001638`, median `0.001504`
- 20d: sample `80`, direction_hit `0.4875`, path_mae `0.067705`, as_primary `20`, as_primary_hit `0.55`, avg `-0.004544`, median `0.000794`
- 60d: sample `80`, direction_hit `0.1375`, path_mae `0.049623`, as_primary `20`, as_primary_hit `1.0`, avg `0.067591`, median `0.069096`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.017955`, as_primary `0`, as_primary_hit `None`, avg `0.003102`, median `0.007812`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.024075`, as_primary `0`, as_primary_hit `None`, avg `0.001048`, median `0.004099`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.034627`, as_primary `0`, as_primary_hit `None`, avg `-0.001638`, median `0.001504`
- 20d: sample `80`, direction_hit `0.5125`, path_mae `0.04055`, as_primary `0`, as_primary_hit `None`, avg `-0.004544`, median `0.000794`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.043411`, as_primary `0`, as_primary_hit `None`, avg `0.067591`, median `0.069096`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.019624`, avg `0.003102`, median `0.007812`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.028484`, avg `0.001048`, median `0.004099`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.043044`, avg `-0.001638`, median `0.001504`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.4625`, primary_mae `0.060049`, avg `-0.004544`, median `0.000794`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.050039`, avg `0.067591`, median `0.069096`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6333`, primary_closer `0.5667`, primary_mae `0.016101`, avg `0.004674`, median `0.008503`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.5167`, primary_mae `0.026919`, avg `0.002404`, median `0.002693`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.5333`, primary_mae `0.045376`, avg `-0.003602`, median `-0.00147`
- 20d: sample `60`, primary_hit `0.5`, primary_closer `0.5167`, primary_mae `0.065308`, avg `-0.007306`, median `-0.003369`
- 60d: sample `60`, primary_hit `0.8167`, primary_closer `0.45`, primary_mae `0.050449`, avg `0.053269`, median `0.059043`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.25`, primary_mae `0.030195`, avg `-0.001616`, median `0.004933`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.03318`, avg `-0.003017`, median `0.00779`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.036048`, avg `0.004255`, median `0.009633`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.044274`, avg `0.003742`, median `0.001267`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.5`, primary_mae `0.04881`, avg `0.110559`, median `0.104383`

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

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.016101, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.026919, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.036048, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.044274, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.0, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.04881, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017881, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022139, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.016101, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024065, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027766, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.026919, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034627, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.047111, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.036048, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04055, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067705, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.044274, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043411, 'direction_hit_rate': 0.8625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049801, 'direction_hit_rate': 0.8625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.0, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.04881, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016794`, avg `0.011129`, median `0.018909`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.031813`, avg `0.008236`, median `0.016774`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.045823`, avg `0.003698`, median `0.004277`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.070879`, avg `-0.003955`, median `-0.002353`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.047285`, avg `0.055409`, median `0.067424`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.020478`, avg `0.001653`, median `0.010214`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.032947`, avg `-0.001018`, median `0.001372`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.047209`, avg `-0.002354`, median `-0.008604`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.083344`, avg `-0.01642`, median `-0.02913`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.045966`, avg `0.054329`, median `0.057737`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.125`, primary_mae `0.034113`, avg `0.004144`, median `0.009216`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.034568`, avg `0.007024`, median `0.011017`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.125`, primary_mae `0.042214`, avg `0.013957`, median `0.010815`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.048054`, avg `0.010904`, median `0.002641`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.375`, primary_mae `0.051787`, avg `0.124893`, median `0.125416`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.019624`, avg `0.003102`, median `0.007812`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.028484`, avg `0.001048`, median `0.004099`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.043044`, avg `-0.001638`, median `0.001504`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.4625`, primary_mae `0.060049`, avg `-0.004544`, median `0.000794`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.050039`, avg `0.067591`, median `0.069096`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.019624`, avg `0.003102`, median `0.007812`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.028484`, avg `0.001048`, median `0.004099`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.043044`, avg `-0.001638`, median `0.001504`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.4625`, primary_mae `0.060049`, avg `-0.004544`, median `0.000794`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.050039`, avg `0.067591`, median `0.069096`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6333`, primary_closer `0.5667`, primary_mae `0.016101`, avg `0.004674`, median `0.008503`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.5167`, primary_mae `0.026919`, avg `0.002404`, median `0.002693`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.5333`, primary_mae `0.045376`, avg `-0.003602`, median `-0.00147`
- 20d: sample `60`, primary_hit `0.5`, primary_closer `0.5167`, primary_mae `0.065308`, avg `-0.007306`, median `-0.003369`
- 60d: sample `60`, primary_hit `0.8167`, primary_closer `0.45`, primary_mae `0.050449`, avg `0.053269`, median `0.059043`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.25`, primary_mae `0.030195`, avg `-0.001616`, median `0.004933`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.03318`, avg `-0.003017`, median `0.00779`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.036048`, avg `0.004255`, median `0.009633`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.044274`, avg `0.003742`, median `0.001267`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.5`, primary_mae `0.04881`, avg `0.110559`, median `0.104383`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.019624`, avg `0.003102`, median `0.007812`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.028484`, avg `0.001048`, median `0.004099`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.043044`, avg `-0.001638`, median `0.001504`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.4625`, primary_mae `0.060049`, avg `-0.004544`, median `0.000794`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.050039`, avg `0.067591`, median `0.069096`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4833`, primary_mae `0.021445`, avg `0.00351`, median `0.009346`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.4667`, primary_mae `0.028716`, avg `0.001138`, median `0.004099`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.5`, primary_mae `0.040535`, avg `0.002904`, median `0.009633`
- 20d: sample `60`, primary_hit `0.5333`, primary_closer `0.5`, primary_mae `0.062566`, avg `5.9e-05`, median `0.003955`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.048421`, avg `0.079692`, median `0.085223`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.019624`, avg `0.003102`, median `0.007812`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.028484`, avg `0.001048`, median `0.004099`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.043044`, avg `-0.001638`, median `0.001504`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.4625`, primary_mae `0.060049`, avg `-0.004544`, median `0.000794`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.050039`, avg `0.067591`, median `0.069096`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
