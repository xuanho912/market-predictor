# Historical Replay Benchmark

Generated at: `2026-09-17T00:58:54.062518+00:00`
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
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.022188`
- secondary_mean_absolute_error: `0.017999`
- primary_error_advantage: `-0.004189`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.022753`
- secondary_mean_absolute_error: `0.020352`
- primary_error_advantage: `-0.002401`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.03495`
- secondary_mean_absolute_error: `0.027092`
- primary_error_advantage: `-0.007858`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2375`
- secondary_hit_rate: `0.7625`
- primary_vs_secondary_accuracy_spread: `-0.525`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.057001`
- secondary_mean_absolute_error: `0.033593`
- primary_error_advantage: `-0.023408`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1625`
- secondary_hit_rate: `0.8375`
- primary_vs_secondary_accuracy_spread: `-0.675`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.06666`
- secondary_mean_absolute_error: `0.052293`
- primary_error_advantage: `-0.014367`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.017678`, as_primary `0`, as_primary_hit `None`, avg `0.003279`, median `0.006065`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.021002`, as_primary `0`, as_primary_hit `None`, avg `0.003574`, median `0.002459`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.02704`, as_primary `0`, as_primary_hit `None`, avg `0.006045`, median `0.007341`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.034976`, as_primary `0`, as_primary_hit `None`, avg `0.031885`, median `0.034838`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.050705`, as_primary `0`, as_primary_hit `None`, avg `0.082576`, median `0.098023`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.018122`, as_primary `0`, as_primary_hit `None`, avg `0.003279`, median `0.006065`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.023855`, as_primary `0`, as_primary_hit `None`, avg `0.003574`, median `0.002459`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.031791`, as_primary `0`, as_primary_hit `None`, avg `0.006045`, median `0.007341`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.053173`, as_primary `0`, as_primary_hit `None`, avg `0.031885`, median `0.034838`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.057048`, as_primary `0`, as_primary_hit `None`, avg `0.082576`, median `0.098023`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.022188`, as_primary `80`, as_primary_hit `0.5875`, avg `0.003279`, median `0.006065`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.022753`, as_primary `80`, as_primary_hit `0.55`, avg `0.003574`, median `0.002459`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.03495`, as_primary `80`, as_primary_hit `0.625`, avg `0.006045`, median `0.007341`
- 20d: sample `80`, direction_hit `0.2375`, path_mae `0.057001`, as_primary `80`, as_primary_hit `0.7625`, avg `0.031885`, median `0.034838`
- 60d: sample `80`, direction_hit `0.1625`, path_mae `0.06666`, as_primary `80`, as_primary_hit `0.8375`, avg `0.082576`, median `0.098023`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.017999`, as_primary `0`, as_primary_hit `None`, avg `0.003279`, median `0.006065`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.020352`, as_primary `0`, as_primary_hit `None`, avg `0.003574`, median `0.002459`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.027092`, as_primary `0`, as_primary_hit `None`, avg `0.006045`, median `0.007341`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.033593`, as_primary `0`, as_primary_hit `None`, avg `0.031885`, median `0.034838`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.052293`, as_primary `0`, as_primary_hit `None`, avg `0.082576`, median `0.098023`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.022188`, avg `0.003279`, median `0.006065`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.022753`, avg `0.003574`, median `0.002459`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.03495`, avg `0.006045`, median `0.007341`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.2875`, primary_mae `0.057001`, avg `0.031885`, median `0.034838`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.3875`, primary_mae `0.06666`, avg `0.082576`, median `0.098023`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.3`, primary_mae `0.022139`, avg `-0.001303`, median `0.000822`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.021692`, avg `-0.002929`, median `-0.0017`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.525`, primary_mae `0.026817`, avg `-0.002731`, median `0.004006`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.049366`, avg `0.02013`, median `0.030823`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.073641`, avg `0.060163`, median `0.084406`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.022238`, avg `0.007861`, median `0.013335`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.023815`, avg `0.010077`, median `0.006997`
- 10d: sample `40`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.043082`, avg `0.01482`, median `0.017852`
- 20d: sample `40`, primary_hit `0.225`, primary_closer `0.275`, primary_mae `0.064635`, avg `0.043639`, median `0.043229`
- 60d: sample `40`, primary_hit `0.1`, primary_closer `0.45`, primary_mae `0.05968`, avg `0.104989`, median `0.11865`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.022139, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.021692, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.026817, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.049366, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.05968, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017678, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022188, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.022139, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020352, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023855, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.021692, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02704, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03495, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.026817, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_vs_secondary_accuracy_spread': -0.525, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033593, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057001, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.049366, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1625, 'secondary_hit_rate': 0.8375, 'primary_vs_secondary_accuracy_spread': -0.675, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050705, 'direction_hit_rate': 0.8375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06666, 'direction_hit_rate': 0.1625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.05968, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.015456`, avg `-0.001232`, median `0.001049`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.017376`, avg `0.002193`, median `0.006272`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.01626`, avg `0.007992`, median `0.01205`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.056541`, avg `0.039454`, median `0.050926`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.875`, primary_mae `0.038074`, avg `0.108026`, median `0.120549`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.017341`, avg `0.006407`, median `0.008014`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.01849`, avg `0.008736`, median `0.008828`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.018372`, avg `0.013492`, median `0.014434`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.04804`, avg `0.030596`, median `0.033084`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.6875`, primary_mae `0.048582`, avg `0.083849`, median `0.111461`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.030761`, avg `-0.00579`, median `-0.00486`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.029144`, avg `-0.006544`, median `-0.006752`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.039381`, avg `-0.008636`, median `-0.00147`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.059452`, avg `0.007323`, median `0.0135`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.099562`, avg `0.029456`, median `0.075157`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.022188`, avg `0.003279`, median `0.006065`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.022753`, avg `0.003574`, median `0.002459`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.03495`, avg `0.006045`, median `0.007341`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.2875`, primary_mae `0.057001`, avg `0.031885`, median `0.034838`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.3875`, primary_mae `0.06666`, avg `0.082576`, median `0.098023`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.022188`, avg `0.003279`, median `0.006065`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.022753`, avg `0.003574`, median `0.002459`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.03495`, avg `0.006045`, median `0.007341`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.2875`, primary_mae `0.057001`, avg `0.031885`, median `0.034838`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.3875`, primary_mae `0.06666`, avg `0.082576`, median `0.098023`

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
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.022188`, avg `0.003279`, median `0.006065`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.022753`, avg `0.003574`, median `0.002459`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.03495`, avg `0.006045`, median `0.007341`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.2875`, primary_mae `0.057001`, avg `0.031885`, median `0.034838`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.3875`, primary_mae `0.06666`, avg `0.082576`, median `0.098023`

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
