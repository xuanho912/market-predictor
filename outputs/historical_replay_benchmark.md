# Historical Replay Benchmark

Generated at: `2026-09-10T16:27:38.505712+00:00`
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
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.018498`
- secondary_mean_absolute_error: `0.013824`
- primary_error_advantage: `-0.004674`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.020555`
- secondary_mean_absolute_error: `0.015824`
- primary_error_advantage: `-0.004731`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.031122`
- secondary_mean_absolute_error: `0.023391`
- primary_error_advantage: `-0.007731`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.0638`
- secondary_mean_absolute_error: `0.03643`
- primary_error_advantage: `-0.02737`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.103711`
- secondary_mean_absolute_error: `0.069166`
- primary_error_advantage: `-0.034545`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.014092`, as_primary `0`, as_primary_hit `None`, avg `0.002593`, median `0.005303`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.015903`, as_primary `0`, as_primary_hit `None`, avg `0.001489`, median `0.003417`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.025999`, as_primary `0`, as_primary_hit `None`, avg `-0.000248`, median `-0.00478`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.037814`, as_primary `0`, as_primary_hit `None`, avg `0.011049`, median `0.017249`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.073563`, as_primary `0`, as_primary_hit `None`, avg `0.036506`, median `0.05856`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.01498`, as_primary `0`, as_primary_hit `None`, avg `0.002593`, median `0.005303`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.019294`, as_primary `0`, as_primary_hit `None`, avg `0.001489`, median `0.003417`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.035374`, as_primary `0`, as_primary_hit `None`, avg `-0.000248`, median `-0.00478`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.054151`, as_primary `0`, as_primary_hit `None`, avg `0.011049`, median `0.017249`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.078455`, as_primary `0`, as_primary_hit `None`, avg `0.036506`, median `0.05856`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.018498`, as_primary `80`, as_primary_hit `0.6125`, avg `0.002593`, median `0.005303`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.020555`, as_primary `80`, as_primary_hit `0.6375`, avg `0.001489`, median `0.003417`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.031122`, as_primary `80`, as_primary_hit `0.45`, avg `-0.000248`, median `-0.00478`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.0638`, as_primary `80`, as_primary_hit `0.6125`, avg `0.011049`, median `0.017249`
- 60d: sample `80`, direction_hit `0.3125`, path_mae `0.103711`, as_primary `80`, as_primary_hit `0.6875`, avg `0.036506`, median `0.05856`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013824`, as_primary `0`, as_primary_hit `None`, avg `0.002593`, median `0.005303`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.015824`, as_primary `0`, as_primary_hit `None`, avg `0.001489`, median `0.003417`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.023391`, as_primary `0`, as_primary_hit `None`, avg `-0.000248`, median `-0.00478`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.03643`, as_primary `0`, as_primary_hit `None`, avg `0.011049`, median `0.017249`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.069166`, as_primary `0`, as_primary_hit `None`, avg `0.036506`, median `0.05856`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.018498`, avg `0.002593`, median `0.005303`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.020555`, avg `0.001489`, median `0.003417`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.031122`, avg `-0.000248`, median `-0.00478`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.275`, primary_mae `0.0638`, avg `0.011049`, median `0.017249`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.103711`, avg `0.036506`, median `0.05856`

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
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.018498`, avg `0.002593`, median `0.005303`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.020555`, avg `0.001489`, median `0.003417`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.031122`, avg `-0.000248`, median `-0.00478`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.275`, primary_mae `0.0638`, avg `0.011049`, median `0.017249`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.103711`, avg `0.036506`, median `0.05856`

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

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3875, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.018498, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3625, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.020555, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.031122, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3875, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.0638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3125, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.103711, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013824, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018498, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3875, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.018498, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015824, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020555, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3625, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.020555, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023391, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035374, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.031122, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03643, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0638, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3875, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.0638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069166, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.103711, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3125, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.103711, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.027486`, avg `-0.001516`, median `0.004814`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.024237`, avg `-0.011121`, median `0.000647`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.017858`, avg `-0.014794`, median `-0.019121`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.056756`, avg `0.018164`, median `0.017863`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.091044`, avg `0.035099`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.023993`, avg `-0.004605`, median `0.000341`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.024106`, avg `-0.010631`, median `-0.002115`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.017241`, avg `-0.007285`, median `-0.009726`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.052429`, avg `0.016593`, median `0.024617`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.087085`, avg `0.033855`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.017689`, avg `0.003238`, median `0.004891`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.023756`, avg `0.006181`, median `0.009983`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.046915`, avg `-0.004207`, median `-0.016628`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.1875`, primary_mae `0.092344`, avg `0.000732`, median `-0.008413`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.191894`, avg `0.026546`, median `0.086526`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.018498`, avg `0.002593`, median `0.005303`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.020555`, avg `0.001489`, median `0.003417`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.031122`, avg `-0.000248`, median `-0.00478`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.275`, primary_mae `0.0638`, avg `0.011049`, median `0.017249`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.103711`, avg `0.036506`, median `0.05856`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.018498`, avg `0.002593`, median `0.005303`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.020555`, avg `0.001489`, median `0.003417`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.031122`, avg `-0.000248`, median `-0.00478`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.275`, primary_mae `0.0638`, avg `0.011049`, median `0.017249`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.103711`, avg `0.036506`, median `0.05856`

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
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.018498`, avg `0.002593`, median `0.005303`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.020555`, avg `0.001489`, median `0.003417`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.031122`, avg `-0.000248`, median `-0.00478`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.275`, primary_mae `0.0638`, avg `0.011049`, median `0.017249`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.103711`, avg `0.036506`, median `0.05856`

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
