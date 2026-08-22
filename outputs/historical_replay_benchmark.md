# Historical Replay Benchmark

Generated at: `2026-08-22T04:18:41.661904+00:00`
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
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.016946`
- secondary_mean_absolute_error: `0.013534`
- primary_error_advantage: `-0.003412`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.02297`
- secondary_mean_absolute_error: `0.019738`
- primary_error_advantage: `-0.003232`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.037979`
- secondary_mean_absolute_error: `0.027537`
- primary_error_advantage: `-0.010442`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.066559`
- secondary_mean_absolute_error: `0.045871`
- primary_error_advantage: `-0.020688`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.25`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.075973`
- secondary_mean_absolute_error: `0.062102`
- primary_error_advantage: `-0.013871`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.013899`, as_primary `0`, as_primary_hit `None`, avg `0.003808`, median `0.005506`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.019296`, as_primary `0`, as_primary_hit `None`, avg `0.002807`, median `0.001478`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.026436`, as_primary `0`, as_primary_hit `None`, avg `0.003161`, median `0.00312`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.042592`, as_primary `0`, as_primary_hit `None`, avg `0.0036`, median `0.010234`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.063034`, as_primary `0`, as_primary_hit `None`, avg `0.014634`, median `0.022458`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.016946`, as_primary `80`, as_primary_hit `0.675`, avg `0.003808`, median `0.005506`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.02297`, as_primary `80`, as_primary_hit `0.575`, avg `0.002807`, median `0.001478`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.037979`, as_primary `80`, as_primary_hit `0.5125`, avg `0.003161`, median `0.00312`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.066559`, as_primary `80`, as_primary_hit `0.575`, avg `0.0036`, median `0.010234`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.075973`, as_primary `80`, as_primary_hit `0.5625`, avg `0.014634`, median `0.022458`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.325`, path_mae `0.017834`, as_primary `0`, as_primary_hit `None`, avg `0.003808`, median `0.005506`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.023866`, as_primary `0`, as_primary_hit `None`, avg `0.002807`, median `0.001478`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.039845`, as_primary `0`, as_primary_hit `None`, avg `0.003161`, median `0.00312`
- 20d: sample `80`, direction_hit `0.425`, path_mae `0.076988`, as_primary `0`, as_primary_hit `None`, avg `0.0036`, median `0.010234`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.081565`, as_primary `0`, as_primary_hit `None`, avg `0.014634`, median `0.022458`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.013217`, as_primary `0`, as_primary_hit `None`, avg `0.003808`, median `0.005506`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.018244`, as_primary `0`, as_primary_hit `None`, avg `0.002807`, median `0.001478`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.025921`, as_primary `0`, as_primary_hit `None`, avg `0.003161`, median `0.00312`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.039925`, as_primary `0`, as_primary_hit `None`, avg `0.0036`, median `0.010234`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.06053`, as_primary `0`, as_primary_hit `None`, avg `0.014634`, median `0.022458`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.018151`, avg `0.00465`, median `0.005581`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.025561`, avg `0.001504`, median `0.001088`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.039221`, avg `0.001497`, median `-0.007304`
- 20d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.07766`, avg `0.003531`, median `0.002895`
- 60d: sample `40`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.083555`, avg `0.021977`, median `0.021115`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.015741`, avg `0.002965`, median `0.004608`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.020379`, avg `0.004111`, median `0.003101`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.3`, primary_mae `0.036737`, avg `0.004825`, median `0.007209`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.275`, primary_mae `0.055458`, avg `0.003669`, median `0.013942`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.068392`, avg `0.007291`, median `0.028313`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.008853`, avg `0.001768`, median `0.001417`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.7`, primary_mae `0.009427`, avg `-0.000112`, median `0.001088`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.023581`, avg `-0.012428`, median `-0.01559`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.6`, primary_mae `0.050171`, avg `-0.025462`, median `-0.018797`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.063914`, avg `-0.014869`, median `-0.02584`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6667`, primary_closer `0.4`, primary_mae `0.019643`, avg `0.004488`, median `0.006568`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.3833`, primary_mae `0.027485`, avg `0.003781`, median `0.002329`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.042778`, avg `0.008358`, median `0.01093`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.25`, primary_mae `0.072022`, avg `0.013287`, median `0.015268`
- 60d: sample `60`, primary_hit `0.6333`, primary_closer `0.3833`, primary_mae `0.079993`, avg `0.024468`, median `0.030192`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.008853, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.009427, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.023581, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.050171, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.063914, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013217, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017834, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.008853, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018244, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023866, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.009427, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025921, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039845, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.023581, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039925, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076988, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.050171, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06053, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.081565, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.063914, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.014942`, avg `-0.002548`, median `0.002672`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.021665`, avg `-0.0069`, median `-0.00451`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.015841`, avg `0.010019`, median `0.020593`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.043388`, avg `0.010949`, median `0.019745`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.068505`, avg `0.012955`, median `0.004851`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.013642`, avg `-0.003387`, median `0.001503`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.013051`, avg `-0.003312`, median `0.00171`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.024187`, avg `-0.000134`, median `0.000295`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.1875`, primary_mae `0.050678`, avg `0.002223`, median `0.008959`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.083593`, avg `-0.008499`, median `-0.025539`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.013642`, avg `-0.003387`, median `0.001503`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.013051`, avg `-0.003312`, median `0.00171`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.024187`, avg `-0.000134`, median `0.000295`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.1875`, primary_mae `0.050678`, avg `0.002223`, median `0.008959`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.083593`, avg `-0.008499`, median `-0.025539`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.675`, primary_closer `0.425`, primary_mae `0.016946`, avg `0.003808`, median `0.005506`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.02297`, avg `0.002807`, median `0.001478`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3375`, primary_mae `0.037979`, avg `0.003161`, median `0.00312`
- 20d: sample `80`, primary_hit `0.575`, primary_closer `0.3375`, primary_mae `0.066559`, avg `0.0036`, median `0.010234`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.3875`, primary_mae `0.075973`, avg `0.014634`, median `0.022458`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.675`, primary_closer `0.425`, primary_mae `0.016946`, avg `0.003808`, median `0.005506`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.02297`, avg `0.002807`, median `0.001478`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3375`, primary_mae `0.037979`, avg `0.003161`, median `0.00312`
- 20d: sample `80`, primary_hit `0.575`, primary_closer `0.3375`, primary_mae `0.066559`, avg `0.0036`, median `0.010234`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.3875`, primary_mae `0.075973`, avg `0.014634`, median `0.022458`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.012396`, avg `-0.00147`, median `0.001416`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.575`, primary_mae `0.011718`, avg `-0.001336`, median `0.000818`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.023854`, avg `-0.005425`, median `-0.012812`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.050187`, avg `-0.010221`, median `-0.005516`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.325`, primary_mae `0.068967`, avg `-0.006189`, median `-0.020199`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.021694`, avg `0.001412`, median `0.003063`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.027853`, avg `0.00028`, median `-0.001001`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.039494`, avg `0.0085`, median `0.01093`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.077676`, avg `0.018772`, median `0.017664`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.3`, primary_mae `0.088608`, avg `0.030657`, median `0.024813`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.675`, primary_closer `0.425`, primary_mae `0.016946`, avg `0.003808`, median `0.005506`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.02297`, avg `0.002807`, median `0.001478`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3375`, primary_mae `0.037979`, avg `0.003161`, median `0.00312`
- 20d: sample `80`, primary_hit `0.575`, primary_closer `0.3375`, primary_mae `0.066559`, avg `0.0036`, median `0.010234`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.3875`, primary_mae `0.075973`, avg `0.014634`, median `0.022458`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.675`, primary_closer `0.425`, primary_mae `0.016946`, avg `0.003808`, median `0.005506`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.02297`, avg `0.002807`, median `0.001478`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3375`, primary_mae `0.037979`, avg `0.003161`, median `0.00312`
- 20d: sample `80`, primary_hit `0.575`, primary_closer `0.3375`, primary_mae `0.066559`, avg `0.0036`, median `0.010234`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.3875`, primary_mae `0.075973`, avg `0.014634`, median `0.022458`

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
