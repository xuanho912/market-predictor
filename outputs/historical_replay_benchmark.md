# Historical Replay Benchmark

Generated at: `2026-07-09T21:56:01.620473+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.013394`
- secondary_mean_absolute_error: `0.011657`
- primary_error_advantage: `-0.001737`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.017318`
- secondary_mean_absolute_error: `0.015111`
- primary_error_advantage: `-0.002207`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.025353`
- secondary_mean_absolute_error: `0.02093`
- primary_error_advantage: `-0.004423`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.045143`
- secondary_mean_absolute_error: `0.046558`
- primary_error_advantage: `0.001415`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.062699`
- secondary_mean_absolute_error: `0.057732`
- primary_error_advantage: `-0.004967`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.012031`, as_primary `0`, as_primary_hit `None`, avg `-0.001885`, median `-0.000199`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.015497`, as_primary `0`, as_primary_hit `None`, avg `-0.003664`, median `-0.00156`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.019994`, as_primary `0`, as_primary_hit `None`, avg `-0.001263`, median `-0.006389`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.031093`, as_primary `0`, as_primary_hit `None`, avg `0.000554`, median `0.008744`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.053659`, as_primary `0`, as_primary_hit `None`, avg `0.009363`, median `0.011163`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.013394`, as_primary `80`, as_primary_hit `0.5`, avg `-0.001885`, median `-0.000199`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.017318`, as_primary `80`, as_primary_hit `0.475`, avg `-0.003664`, median `-0.00156`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.025353`, as_primary `80`, as_primary_hit `0.45`, avg `-0.001263`, median `-0.006389`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.045143`, as_primary `80`, as_primary_hit `0.65`, avg `0.000554`, median `0.008744`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.062699`, as_primary `80`, as_primary_hit `0.525`, avg `0.009363`, median `0.011163`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.012388`, as_primary `0`, as_primary_hit `None`, avg `-0.001885`, median `-0.000199`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.015985`, as_primary `0`, as_primary_hit `None`, avg `-0.003664`, median `-0.00156`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.021541`, as_primary `0`, as_primary_hit `None`, avg `-0.001263`, median `-0.006389`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.065413`, as_primary `0`, as_primary_hit `None`, avg `0.000554`, median `0.008744`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.069403`, as_primary `0`, as_primary_hit `None`, avg `0.009363`, median `0.011163`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.011632`, as_primary `0`, as_primary_hit `None`, avg `-0.001885`, median `-0.000199`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.015127`, as_primary `0`, as_primary_hit `None`, avg `-0.003664`, median `-0.00156`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.019538`, as_primary `0`, as_primary_hit `None`, avg `-0.001263`, median `-0.006389`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.03154`, as_primary `0`, as_primary_hit `None`, avg `0.000554`, median `0.008744`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.053289`, as_primary `0`, as_primary_hit `None`, avg `0.009363`, median `0.011163`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.013392`, avg `-0.000546`, median `-0.000421`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.018982`, avg `-0.00251`, median `-0.000554`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.030807`, avg `-0.003669`, median `-0.007304`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.6`, primary_mae `0.050292`, avg `-0.006787`, median `0.007185`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.061343`, avg `-0.007877`, median `-0.011052`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.013396`, avg `-0.003224`, median `0.000418`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.015654`, avg `-0.004818`, median `-0.002881`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.019899`, avg `0.001143`, median `-0.00464`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.225`, primary_mae `0.039994`, avg `0.007894`, median `0.011873`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.064055`, avg `0.026604`, median `0.045588`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.013392`, avg `-0.000546`, median `-0.000421`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.018982`, avg `-0.00251`, median `-0.000554`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.030807`, avg `-0.003669`, median `-0.007304`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.6`, primary_mae `0.050292`, avg `-0.006787`, median `0.007185`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.061343`, avg `-0.007877`, median `-0.011052`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.013396`, avg `-0.003224`, median `0.000418`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.015654`, avg `-0.004818`, median `-0.002881`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.019899`, avg `0.001143`, median `-0.00464`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.225`, primary_mae `0.039994`, avg `0.007894`, median `0.011873`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.064055`, avg `0.026604`, median `0.045588`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.013392, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.015654, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.019899, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.039994, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.061343, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011632, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013394, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.013392, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015127, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017318, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.015654, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019538, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025353, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.019899, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031093, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065413, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.039994, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053289, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069403, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.061343, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.013502`, avg `-0.007945`, median `-5e-05`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.014048`, avg `-0.007801`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.019588`, avg `0.001184`, median `0.0036`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.375`, primary_mae `0.021916`, avg `0.029489`, median `0.030181`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.043932`, avg `0.066365`, median `0.076071`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.014235`, avg `-0.010758`, median `-0.009708`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.013979`, avg `-0.011013`, median `-0.010372`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.015131`, avg `-0.007188`, median `-0.011067`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.036515`, avg `0.017128`, median `0.024592`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.076654`, avg `0.036418`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.014235`, avg `-0.010758`, median `-0.009708`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.013979`, avg `-0.011013`, median `-0.010372`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.015131`, avg `-0.007188`, median `-0.011067`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.036515`, avg `0.017128`, median `0.024592`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.076654`, avg `0.036418`, median `0.052814`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.013394`, avg `-0.001885`, median `-0.000199`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.017318`, avg `-0.003664`, median `-0.00156`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.025353`, avg `-0.001263`, median `-0.006389`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.045143`, avg `0.000554`, median `0.008744`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.062699`, avg `0.009363`, median `0.011163`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.013394`, avg `-0.001885`, median `-0.000199`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.017318`, avg `-0.003664`, median `-0.00156`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.025353`, avg `-0.001263`, median `-0.006389`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.045143`, avg `0.000554`, median `0.008744`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.062699`, avg `0.009363`, median `0.011163`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.013394`, avg `-0.001885`, median `-0.000199`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.017318`, avg `-0.003664`, median `-0.00156`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.025353`, avg `-0.001263`, median `-0.006389`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.045143`, avg `0.000554`, median `0.008744`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.062699`, avg `0.009363`, median `0.011163`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.017728`, avg `-0.000379`, median `-0.001059`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.026502`, avg `-0.002495`, median `-0.005921`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.045203`, avg `-0.000924`, median `0.004339`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.8`, primary_mae `0.063495`, avg `-0.007559`, median `0.007521`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.071296`, avg `-0.004079`, median `-0.007976`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.013394`, avg `-0.001885`, median `-0.000199`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.017318`, avg `-0.003664`, median `-0.00156`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.025353`, avg `-0.001263`, median `-0.006389`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.045143`, avg `0.000554`, median `0.008744`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.062699`, avg `0.009363`, median `0.011163`

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
