# Historical Replay Benchmark

Generated at: `2026-11-24T05:30:57.944334+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.02574`
- secondary_mean_absolute_error: `0.020677`
- primary_error_advantage: `-0.005063`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.025825`
- secondary_mean_absolute_error: `0.02385`
- primary_error_advantage: `-0.001975`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.03195`
- secondary_mean_absolute_error: `0.030161`
- primary_error_advantage: `-0.001789`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.060954`
- secondary_mean_absolute_error: `0.042366`
- primary_error_advantage: `-0.018588`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.077646`
- secondary_mean_absolute_error: `0.07088`
- primary_error_advantage: `-0.006766`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.021027`, as_primary `0`, as_primary_hit `None`, avg `0.002783`, median `0.001912`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.025056`, as_primary `0`, as_primary_hit `None`, avg `0.007633`, median `0.003908`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.032916`, as_primary `0`, as_primary_hit `None`, avg `0.019184`, median `0.012538`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.048612`, as_primary `0`, as_primary_hit `None`, avg `0.018671`, median `0.013663`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.071521`, as_primary `0`, as_primary_hit `None`, avg `0.052464`, median `0.066728`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.025065`, as_primary `0`, as_primary_hit `None`, avg `0.002783`, median `0.001912`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.029439`, as_primary `0`, as_primary_hit `None`, avg `0.007633`, median `0.003908`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.040262`, as_primary `0`, as_primary_hit `None`, avg `0.019184`, median `0.012538`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.072551`, as_primary `0`, as_primary_hit `None`, avg `0.018671`, median `0.013663`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.08911`, as_primary `0`, as_primary_hit `None`, avg `0.052464`, median `0.066728`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.02574`, as_primary `80`, as_primary_hit `0.5`, avg `0.002783`, median `0.001912`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.025825`, as_primary `80`, as_primary_hit `0.575`, avg `0.007633`, median `0.003908`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.03195`, as_primary `80`, as_primary_hit `0.675`, avg `0.019184`, median `0.012538`
- 20d: sample `80`, direction_hit `0.4375`, path_mae `0.060954`, as_primary `80`, as_primary_hit `0.5625`, avg `0.018671`, median `0.013663`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.077646`, as_primary `80`, as_primary_hit `0.675`, avg `0.052464`, median `0.066728`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.020677`, as_primary `0`, as_primary_hit `None`, avg `0.002783`, median `0.001912`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.02385`, as_primary `0`, as_primary_hit `None`, avg `0.007633`, median `0.003908`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.030161`, as_primary `0`, as_primary_hit `None`, avg `0.019184`, median `0.012538`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.042366`, as_primary `0`, as_primary_hit `None`, avg `0.018671`, median `0.013663`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.07088`, as_primary `0`, as_primary_hit `None`, avg `0.052464`, median `0.066728`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.02574`, avg `0.002783`, median `0.001912`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4375`, primary_mae `0.025825`, avg `0.007633`, median `0.003908`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.03195`, avg `0.019184`, median `0.012538`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.060954`, avg `0.018671`, median `0.013663`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.077646`, avg `0.052464`, median `0.066728`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.021861`, avg `0.000489`, median `-0.001806`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.4167`, primary_mae `0.022409`, avg `0.004554`, median `0.002343`
- 10d: sample `60`, primary_hit `0.3333`, primary_closer `0.3833`, primary_mae `0.026856`, avg `0.015517`, median `0.011643`
- 20d: sample `60`, primary_hit `0.4833`, primary_closer `0.35`, primary_mae `0.054322`, avg `0.013137`, median `0.002171`
- 60d: sample `60`, primary_hit `0.3667`, primary_closer `0.4333`, primary_mae `0.06835`, avg `0.037497`, median `0.062362`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.037377`, avg `0.009664`, median `0.010315`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.036071`, avg `0.016872`, median `0.013397`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.047229`, avg `0.030184`, median `0.032397`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.080851`, avg `0.035272`, median `0.029816`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.105536`, avg `0.097366`, median `0.106229`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.021861, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.022409, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.026856, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.054322, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.06835, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020677, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02574, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.021861, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02385, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029439, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.022409, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030161, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040262, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.026856, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042366, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072551, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.054322, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07088, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.08911, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.06835, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.028616`, avg `0.004212`, median `0.008886`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.021678`, avg `0.002741`, median `-0.006088`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.032078`, avg `0.004312`, median `-0.001976`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.067078`, avg `0.026908`, median `0.030587`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.095616`, avg `0.086299`, median `0.124079`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.040335`, avg `0.016226`, median `0.019095`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.03757`, avg `0.024376`, median `0.02645`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.4375`, primary_mae `0.047228`, avg `0.040418`, median `0.047828`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.091237`, avg `0.04823`, median `0.03457`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.117717`, avg `0.109883`, median `0.118517`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.024314`, avg `-0.00158`, median `-0.00313`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.020783`, avg `-0.005915`, median `-0.005337`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.02513`, avg `-3.5e-05`, median `-0.002556`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.047349`, avg `0.01068`, median `-0.0039`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.069626`, avg `0.023594`, median `0.020882`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.02574`, avg `0.002783`, median `0.001912`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4375`, primary_mae `0.025825`, avg `0.007633`, median `0.003908`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.03195`, avg `0.019184`, median `0.012538`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.060954`, avg `0.018671`, median `0.013663`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.077646`, avg `0.052464`, median `0.066728`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.02574`, avg `0.002783`, median `0.001912`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4375`, primary_mae `0.025825`, avg `0.007633`, median `0.003908`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.03195`, avg `0.019184`, median `0.012538`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.060954`, avg `0.018671`, median `0.013663`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.077646`, avg `0.052464`, median `0.066728`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.037377`, avg `0.009664`, median `0.010315`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.036071`, avg `0.016872`, median `0.013397`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.047229`, avg `0.030184`, median `0.032397`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.080851`, avg `0.035272`, median `0.029816`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.105536`, avg `0.097366`, median `0.106229`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.021861`, avg `0.000489`, median `-0.001806`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.4167`, primary_mae `0.022409`, avg `0.004554`, median `0.002343`
- 10d: sample `60`, primary_hit `0.3333`, primary_closer `0.3833`, primary_mae `0.026856`, avg `0.015517`, median `0.011643`
- 20d: sample `60`, primary_hit `0.4833`, primary_closer `0.35`, primary_mae `0.054322`, avg `0.013137`, median `0.002171`
- 60d: sample `60`, primary_hit `0.3667`, primary_closer `0.4333`, primary_mae `0.06835`, avg `0.037497`, median `0.062362`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.02574`, avg `0.002783`, median `0.001912`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4375`, primary_mae `0.025825`, avg `0.007633`, median `0.003908`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.03195`, avg `0.019184`, median `0.012538`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.060954`, avg `0.018671`, median `0.013663`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.077646`, avg `0.052464`, median `0.066728`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.02574`, avg `0.002783`, median `0.001912`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4375`, primary_mae `0.025825`, avg `0.007633`, median `0.003908`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.03195`, avg `0.019184`, median `0.012538`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.060954`, avg `0.018671`, median `0.013663`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.077646`, avg `0.052464`, median `0.066728`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
