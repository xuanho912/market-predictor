# Historical Replay Benchmark

Generated at: `2026-07-23T14:42:27.726275+00:00`
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
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.028224`
- secondary_mean_absolute_error: `0.018695`
- primary_error_advantage: `-0.009529`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.032001`
- secondary_mean_absolute_error: `0.022389`
- primary_error_advantage: `-0.009612`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.034678`
- secondary_mean_absolute_error: `0.026942`
- primary_error_advantage: `-0.007736`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.073399`
- secondary_mean_absolute_error: `0.044235`
- primary_error_advantage: `-0.029164`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.115618`
- secondary_mean_absolute_error: `0.084628`
- primary_error_advantage: `-0.03099`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.018412`, as_primary `0`, as_primary_hit `None`, avg `-0.002849`, median `0.001302`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.021192`, as_primary `0`, as_primary_hit `None`, avg `-0.00272`, median `0.000995`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.024363`, as_primary `0`, as_primary_hit `None`, avg `0.00444`, median `0.006527`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.036781`, as_primary `0`, as_primary_hit `None`, avg `0.017063`, median `0.02387`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.073842`, as_primary `0`, as_primary_hit `None`, avg `0.025003`, median `0.049921`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.018676`, as_primary `0`, as_primary_hit `None`, avg `-0.002849`, median `0.001302`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.026364`, as_primary `0`, as_primary_hit `None`, avg `-0.00272`, median `0.000995`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.02855`, as_primary `0`, as_primary_hit `None`, avg `0.00444`, median `0.006527`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.056115`, as_primary `0`, as_primary_hit `None`, avg `0.017063`, median `0.02387`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.087624`, as_primary `0`, as_primary_hit `None`, avg `0.025003`, median `0.049921`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.028224`, as_primary `80`, as_primary_hit `0.5625`, avg `-0.002849`, median `0.001302`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.032001`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.00272`, median `0.000995`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.034678`, as_primary `80`, as_primary_hit `0.575`, avg `0.00444`, median `0.006527`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.073399`, as_primary `80`, as_primary_hit `0.6875`, avg `0.017063`, median `0.02387`
- 60d: sample `80`, direction_hit `0.35`, path_mae `0.115618`, as_primary `80`, as_primary_hit `0.65`, avg `0.025003`, median `0.049921`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.018499`, as_primary `0`, as_primary_hit `None`, avg `-0.002849`, median `0.001302`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.020954`, as_primary `0`, as_primary_hit `None`, avg `-0.00272`, median `0.000995`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.024098`, as_primary `0`, as_primary_hit `None`, avg `0.00444`, median `0.006527`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.037887`, as_primary `0`, as_primary_hit `None`, avg `0.017063`, median `0.02387`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.075154`, as_primary `0`, as_primary_hit `None`, avg `0.025003`, median `0.049921`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.028224`, avg `-0.002849`, median `0.001302`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.032001`, avg `-0.00272`, median `0.000995`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.034678`, avg `0.00444`, median `0.006527`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.073399`, avg `0.017063`, median `0.02387`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.115618`, avg `0.025003`, median `0.049921`

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
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.275`, primary_mae `0.031745`, avg `-0.001274`, median `0.004508`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.035027`, avg `0.001728`, median `0.001164`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.25`, primary_mae `0.045184`, avg `0.012818`, median `0.022187`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.077671`, avg `0.022973`, median `0.042225`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.137462`, avg `0.021129`, median `0.060071`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.024704`, avg `-0.004423`, median `0.001169`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.028974`, avg `-0.007167`, median `0.000995`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.024171`, avg `-0.003938`, median `-0.006514`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.069127`, avg `0.011153`, median `0.020147`
- 60d: sample `40`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.093774`, avg `0.028878`, median `0.04627`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.024704, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.028974, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.024171, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.069127, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.093774, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018412, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028224, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.024704, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020954, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032001, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.028974, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024098, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034678, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.024171, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036781, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073399, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.069127, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073842, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.115618, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.093774, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.027298`, avg `-0.01363`, median `-0.018199`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.030668`, avg `-0.025133`, median `-0.031479`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.017684`, avg `-0.011762`, median `-0.009593`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.066016`, avg `-0.007317`, median `-0.006533`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.106133`, avg `0.011993`, median `0.004276`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.033396`, avg `-0.007531`, median `-0.00023`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.040317`, avg `-0.0145`, median `-0.008746`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.022898`, avg `-0.005148`, median `-0.007383`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.081042`, avg `0.015295`, median `0.024617`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.132477`, avg `0.046168`, median `0.054967`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.034215`, avg `-0.000521`, median `0.008116`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.035151`, avg `0.012216`, median `0.010722`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.038471`, avg `0.029525`, median `0.031352`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.062685`, avg `0.044262`, median `0.051197`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.136288`, avg `0.047786`, median `0.073766`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.028224`, avg `-0.002849`, median `0.001302`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.032001`, avg `-0.00272`, median `0.000995`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.034678`, avg `0.00444`, median `0.006527`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.073399`, avg `0.017063`, median `0.02387`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.115618`, avg `0.025003`, median `0.049921`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.028224`, avg `-0.002849`, median `0.001302`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.032001`, avg `-0.00272`, median `0.000995`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.034678`, avg `0.00444`, median `0.006527`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.073399`, avg `0.017063`, median `0.02387`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.115618`, avg `0.025003`, median `0.049921`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.024704`, avg `-0.004423`, median `0.001169`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.028974`, avg `-0.007167`, median `0.000995`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.024171`, avg `-0.003938`, median `-0.006514`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.069127`, avg `0.011153`, median `0.020147`
- 60d: sample `40`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.093774`, avg `0.028878`, median `0.04627`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.275`, primary_mae `0.031745`, avg `-0.001274`, median `0.004508`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.035027`, avg `0.001728`, median `0.001164`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.25`, primary_mae `0.045184`, avg `0.012818`, median `0.022187`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.077671`, avg `0.022973`, median `0.042225`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.137462`, avg `0.021129`, median `0.060071`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.028224`, avg `-0.002849`, median `0.001302`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.032001`, avg `-0.00272`, median `0.000995`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.034678`, avg `0.00444`, median `0.006527`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.073399`, avg `0.017063`, median `0.02387`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.115618`, avg `0.025003`, median `0.049921`

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
