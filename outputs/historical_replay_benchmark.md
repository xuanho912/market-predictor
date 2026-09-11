# Historical Replay Benchmark

Generated at: `2026-09-11T22:42:43.670955+00:00`
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
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.017428`
- secondary_mean_absolute_error: `0.014129`
- primary_error_advantage: `-0.003299`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.022621`
- secondary_mean_absolute_error: `0.017943`
- primary_error_advantage: `-0.004678`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.028053`
- secondary_mean_absolute_error: `0.022918`
- primary_error_advantage: `-0.005135`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.065253`
- secondary_mean_absolute_error: `0.039838`
- primary_error_advantage: `-0.025415`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.110678`
- secondary_mean_absolute_error: `0.083214`
- primary_error_advantage: `-0.027464`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.013703`, as_primary `0`, as_primary_hit `None`, avg `-0.002009`, median `0.000878`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.01812`, as_primary `0`, as_primary_hit `None`, avg `-0.004909`, median `0.000283`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.026748`, as_primary `0`, as_primary_hit `None`, avg `-0.004386`, median `-0.007623`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.041118`, as_primary `0`, as_primary_hit `None`, avg `0.002905`, median `0.007561`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.083653`, as_primary `0`, as_primary_hit `None`, avg `0.015041`, median `0.041161`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.016321`, as_primary `0`, as_primary_hit `None`, avg `-0.002009`, median `0.000878`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.023912`, as_primary `0`, as_primary_hit `None`, avg `-0.004909`, median `0.000283`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.039202`, as_primary `0`, as_primary_hit `None`, avg `-0.004386`, median `-0.007623`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.060755`, as_primary `0`, as_primary_hit `None`, avg `0.002905`, median `0.007561`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.098834`, as_primary `0`, as_primary_hit `None`, avg `0.015041`, median `0.041161`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.017428`, as_primary `80`, as_primary_hit `0.5625`, avg `-0.002009`, median `0.000878`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.022621`, as_primary `80`, as_primary_hit `0.5`, avg `-0.004909`, median `0.000283`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.028053`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.004386`, median `-0.007623`
- 20d: sample `80`, direction_hit `0.45`, path_mae `0.065253`, as_primary `80`, as_primary_hit `0.55`, avg `0.002905`, median `0.007561`
- 60d: sample `80`, direction_hit `0.4`, path_mae `0.110678`, as_primary `80`, as_primary_hit `0.6`, avg `0.015041`, median `0.041161`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.014129`, as_primary `0`, as_primary_hit `None`, avg `-0.002009`, median `0.000878`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.017943`, as_primary `0`, as_primary_hit `None`, avg `-0.004909`, median `0.000283`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.022918`, as_primary `0`, as_primary_hit `None`, avg `-0.004386`, median `-0.007623`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.039838`, as_primary `0`, as_primary_hit `None`, avg `0.002905`, median `0.007561`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.083214`, as_primary `0`, as_primary_hit `None`, avg `0.015041`, median `0.041161`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.017428`, avg `-0.002009`, median `0.000878`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.022621`, avg `-0.004909`, median `0.000283`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4`, primary_mae `0.028053`, avg `-0.004386`, median `-0.007623`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.065253`, avg `0.002905`, median `0.007561`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.110678`, avg `0.015041`, median `0.041161`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.017428`, avg `-0.002009`, median `0.000878`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.022621`, avg `-0.004909`, median `0.000283`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4`, primary_mae `0.028053`, avg `-0.004386`, median `-0.007623`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.065253`, avg `0.002905`, median `0.007561`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.110678`, avg `0.015041`, median `0.041161`

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

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.017428, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022621, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6125, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.028053, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.065253, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.110678, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013703, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017428, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.017428, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017943, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023912, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022621, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022918, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039202, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6125, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.028053, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039838, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065253, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.065253, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.083214, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.110678, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.110678, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.024257`, avg `-0.006324`, median `0.000341`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.029518`, avg `-0.011979`, median `-0.006529`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.016388`, avg `-0.003551`, median `-0.006514`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.062788`, avg `0.027332`, median `0.031583`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.113303`, avg `0.068599`, median `0.080389`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.024932`, avg `-0.007017`, median `-0.00023`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.029572`, avg `-0.011916`, median `-0.002934`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.015047`, avg `-0.001421`, median `-0.006514`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.052661`, avg `0.019961`, median `0.024617`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.092761`, avg `0.047295`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.016768`, avg `0.003359`, median `0.003143`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.1875`, primary_mae `0.028267`, avg `0.000526`, median `0.000558`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.044504`, avg `-0.011494`, median `-0.02037`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.094152`, avg `-0.017301`, median `-0.001846`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.192191`, avg `-0.011157`, median `0.087814`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.017428`, avg `-0.002009`, median `0.000878`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.022621`, avg `-0.004909`, median `0.000283`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4`, primary_mae `0.028053`, avg `-0.004386`, median `-0.007623`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.065253`, avg `0.002905`, median `0.007561`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.110678`, avg `0.015041`, median `0.041161`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.017428`, avg `-0.002009`, median `0.000878`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.022621`, avg `-0.004909`, median `0.000283`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4`, primary_mae `0.028053`, avg `-0.004386`, median `-0.007623`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.065253`, avg `0.002905`, median `0.007561`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.110678`, avg `0.015041`, median `0.041161`

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
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.017428`, avg `-0.002009`, median `0.000878`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.022621`, avg `-0.004909`, median `0.000283`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4`, primary_mae `0.028053`, avg `-0.004386`, median `-0.007623`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.065253`, avg `0.002905`, median `0.007561`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.110678`, avg `0.015041`, median `0.041161`

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
