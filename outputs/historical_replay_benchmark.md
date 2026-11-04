# Historical Replay Benchmark

Generated at: `2026-11-04T07:32:48.735241+00:00`
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
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.026968`
- secondary_mean_absolute_error: `0.02077`
- primary_error_advantage: `-0.006198`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.029918`
- secondary_mean_absolute_error: `0.028241`
- primary_error_advantage: `-0.001677`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.6`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.3375`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.044468`
- secondary_mean_absolute_error: `0.034595`
- primary_error_advantage: `-0.009873`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.059962`
- secondary_mean_absolute_error: `0.041085`
- primary_error_advantage: `-0.018877`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.055671`
- secondary_mean_absolute_error: `0.036334`
- primary_error_advantage: `-0.019337`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.020056`, as_primary `0`, as_primary_hit `None`, avg `0.000532`, median `0.001007`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.026151`, as_primary `0`, as_primary_hit `None`, avg `0.00422`, median `0.003698`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.029734`, as_primary `0`, as_primary_hit `None`, avg `0.014454`, median `0.018569`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.034915`, as_primary `0`, as_primary_hit `None`, avg `0.02856`, median `0.030717`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.033008`, as_primary `0`, as_primary_hit `None`, avg `0.048645`, median `0.062627`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.023056`, as_primary `0`, as_primary_hit `None`, avg `0.000532`, median `0.001007`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.031675`, as_primary `0`, as_primary_hit `None`, avg `0.00422`, median `0.003698`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.042728`, as_primary `0`, as_primary_hit `None`, avg `0.014454`, median `0.018569`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.051551`, as_primary `0`, as_primary_hit `None`, avg `0.02856`, median `0.030717`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.037897`, as_primary `0`, as_primary_hit `None`, avg `0.048645`, median `0.062627`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.026968`, as_primary `80`, as_primary_hit `0.5125`, avg `0.000532`, median `0.001007`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.029918`, as_primary `80`, as_primary_hit `0.525`, avg `0.00422`, median `0.003698`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.044468`, as_primary `80`, as_primary_hit `0.6625`, avg `0.014454`, median `0.018569`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.059962`, as_primary `80`, as_primary_hit `0.725`, avg `0.02856`, median `0.030717`
- 60d: sample `80`, direction_hit `0.1875`, path_mae `0.055671`, as_primary `80`, as_primary_hit `0.8125`, avg `0.048645`, median `0.062627`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.019538`, as_primary `0`, as_primary_hit `None`, avg `0.000532`, median `0.001007`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.023999`, as_primary `0`, as_primary_hit `None`, avg `0.00422`, median `0.003698`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.028372`, as_primary `0`, as_primary_hit `None`, avg `0.014454`, median `0.018569`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.034114`, as_primary `0`, as_primary_hit `None`, avg `0.02856`, median `0.030717`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.034069`, as_primary `0`, as_primary_hit `None`, avg `0.048645`, median `0.062627`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.026968`, avg `0.000532`, median `0.001007`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.029918`, avg `0.00422`, median `0.003698`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.044468`, avg `0.014454`, median `0.018569`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.059962`, avg `0.02856`, median `0.030717`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.055671`, avg `0.048645`, median `0.062627`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.031436`, avg `-0.004762`, median `-0.008464`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.027057`, avg `0.006643`, median `-0.001204`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.052581`, avg `0.020986`, median `0.029242`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.065546`, avg `0.043052`, median `0.053281`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.052065`, avg `0.055319`, median `0.069033`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.4`, primary_mae `0.025479`, avg `0.002296`, median `0.005306`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4833`, primary_mae `0.030872`, avg `0.003412`, median `0.007025`
- 10d: sample `60`, primary_hit `0.3333`, primary_closer `0.3833`, primary_mae `0.041763`, avg `0.012276`, median `0.013286`
- 20d: sample `60`, primary_hit `0.3`, primary_closer `0.3833`, primary_mae `0.0581`, avg `0.02373`, median `0.028608`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.3167`, primary_mae `0.056873`, avg `0.04642`, median `0.056753`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.025479, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.027057, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.041763, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.0581, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.052065, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019538, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026968, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.025479, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023999, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031675, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.027057, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.3375, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028372, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044468, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.041763, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034114, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059962, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.0581, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033008, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055671, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.052065, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.01279`, avg `-0.00054`, median `-0.004204`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.015358`, avg `0.000936`, median `-0.009913`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.037499`, avg `-0.002318`, median `-0.003361`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.044312`, avg `0.018122`, median `0.017025`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.057133`, avg `0.027743`, median `0.040761`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.014451`, avg `-0.00025`, median `-0.004204`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.018393`, avg `0.005943`, median `0.007025`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.042445`, avg `0.007934`, median `0.003439`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.055408`, avg `0.026743`, median `0.029737`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.07293`, avg `0.047041`, median `0.048488`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.035365`, avg `-0.000824`, median `-0.002931`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.030354`, avg `0.014105`, median `0.00445`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.055818`, avg `0.026595`, median `0.029836`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.069076`, avg `0.050242`, median `0.054498`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.0552`, avg `0.052694`, median `0.068874`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.026968`, avg `0.000532`, median `0.001007`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.029918`, avg `0.00422`, median `0.003698`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.044468`, avg `0.014454`, median `0.018569`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.059962`, avg `0.02856`, median `0.030717`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.055671`, avg `0.048645`, median `0.062627`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.026968`, avg `0.000532`, median `0.001007`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.029918`, avg `0.00422`, median `0.003698`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.044468`, avg `0.014454`, median `0.018569`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.059962`, avg `0.02856`, median `0.030717`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.055671`, avg `0.048645`, median `0.062627`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.4`, primary_mae `0.025479`, avg `0.002296`, median `0.005306`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4833`, primary_mae `0.030872`, avg `0.003412`, median `0.007025`
- 10d: sample `60`, primary_hit `0.3333`, primary_closer `0.3833`, primary_mae `0.041763`, avg `0.012276`, median `0.013286`
- 20d: sample `60`, primary_hit `0.3`, primary_closer `0.3833`, primary_mae `0.0581`, avg `0.02373`, median `0.028608`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.3167`, primary_mae `0.056873`, avg `0.04642`, median `0.056753`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.031436`, avg `-0.004762`, median `-0.008464`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.027057`, avg `0.006643`, median `-0.001204`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.052581`, avg `0.020986`, median `0.029242`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.065546`, avg `0.043052`, median `0.053281`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.052065`, avg `0.055319`, median `0.069033`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.026968`, avg `0.000532`, median `0.001007`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.029918`, avg `0.00422`, median `0.003698`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.044468`, avg `0.014454`, median `0.018569`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.059962`, avg `0.02856`, median `0.030717`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.055671`, avg `0.048645`, median `0.062627`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.026968`, avg `0.000532`, median `0.001007`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.029918`, avg `0.00422`, median `0.003698`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.044468`, avg `0.014454`, median `0.018569`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.059962`, avg `0.02856`, median `0.030717`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.055671`, avg `0.048645`, median `0.062627`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.026968`, avg `0.000532`, median `0.001007`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.029918`, avg `0.00422`, median `0.003698`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.044468`, avg `0.014454`, median `0.018569`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.059962`, avg `0.02856`, median `0.030717`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.055671`, avg `0.048645`, median `0.062627`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
