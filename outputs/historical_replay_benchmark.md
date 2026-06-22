# Historical Replay Benchmark

Generated at: `2026-06-22T17:42:45.683560+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'high', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay', 'forward validation completed samples are below the minimum gate'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.015307`
- secondary_mean_absolute_error: `0.013195`
- primary_error_advantage: `-0.002112`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.01698`
- secondary_mean_absolute_error: `0.015694`
- primary_error_advantage: `-0.001286`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.024367`
- secondary_mean_absolute_error: `0.019028`
- primary_error_advantage: `-0.005339`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.03751`
- secondary_mean_absolute_error: `0.025294`
- primary_error_advantage: `-0.012216`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.0599`
- secondary_mean_absolute_error: `0.052169`
- primary_error_advantage: `-0.007731`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.013696`, as_primary `0`, as_primary_hit `None`, avg `-0.000973`, median `-0.001404`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.015777`, as_primary `0`, as_primary_hit `None`, avg `-0.00398`, median `-0.003858`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.019401`, as_primary `0`, as_primary_hit `None`, avg `-0.002625`, median `-0.003658`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.025073`, as_primary `0`, as_primary_hit `None`, avg `0.007815`, median `0.015161`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.053007`, as_primary `0`, as_primary_hit `None`, avg `0.023634`, median `0.039962`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.015307`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.000973`, median `-0.001404`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.01698`, as_primary `80`, as_primary_hit `0.45`, avg `-0.00398`, median `-0.003858`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.024367`, as_primary `80`, as_primary_hit `0.4`, avg `-0.002625`, median `-0.003658`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.03751`, as_primary `80`, as_primary_hit `0.6875`, avg `0.007815`, median `0.015161`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.0599`, as_primary `80`, as_primary_hit `0.6125`, avg `0.023634`, median `0.039962`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.013728`, as_primary `0`, as_primary_hit `None`, avg `-0.000973`, median `-0.001404`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.017449`, as_primary `0`, as_primary_hit `None`, avg `-0.00398`, median `-0.003858`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.024928`, as_primary `0`, as_primary_hit `None`, avg `-0.002625`, median `-0.003658`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.052888`, as_primary `0`, as_primary_hit `None`, avg `0.007815`, median `0.015161`
- 60d: sample `80`, direction_hit `0.3875`, path_mae `0.06277`, as_primary `0`, as_primary_hit `None`, avg `0.023634`, median `0.039962`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.013195`, as_primary `0`, as_primary_hit `None`, avg `-0.000973`, median `-0.001404`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.015694`, as_primary `0`, as_primary_hit `None`, avg `-0.00398`, median `-0.003858`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.019028`, as_primary `0`, as_primary_hit `None`, avg `-0.002625`, median `-0.003658`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.025294`, as_primary `0`, as_primary_hit `None`, avg `0.007815`, median `0.015161`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.052169`, as_primary `0`, as_primary_hit `None`, avg `0.023634`, median `0.039962`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3875`, primary_mae `0.015307`, avg `-0.000973`, median `-0.001404`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.01698`, avg `-0.00398`, median `-0.003858`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.024367`, avg `-0.002625`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.03751`, avg `0.007815`, median `0.015161`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.0599`, avg `0.023634`, median `0.039962`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.013438`, avg `-0.001717`, median `-0.001404`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.016355`, avg `-0.005372`, median `-0.003195`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.024831`, avg `-0.00552`, median `-0.007701`
- 20d: sample `40`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.038571`, avg `-0.001098`, median `0.008896`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.058981`, avg `0.00648`, median `0.002524`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.017176`, avg `-0.000229`, median `-0.001207`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.017606`, avg `-0.002589`, median `-0.005063`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.325`, primary_mae `0.023902`, avg `0.00027`, median `-0.001481`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.3`, primary_mae `0.03645`, avg `0.016728`, median `0.028346`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.45`, primary_mae `0.060818`, avg `0.040788`, median `0.061862`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.013438, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.016355, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.023902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.03645, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.058981, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013195, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015307, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.013438, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015694, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017449, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.016355, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019028, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024928, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.023902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025073, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052888, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.03645, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052169, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06277, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.058981, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.016952`, avg `-0.005957`, median `-0.006094`
- 5d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.015484`, avg `-0.018169`, median `-0.014993`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.011207`, avg `0.004766`, median `0.006144`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.125`, primary_mae `0.017352`, avg `0.028135`, median `0.030181`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.027189`, avg `0.075992`, median `0.086868`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.01729`, avg `-0.003055`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.013632`, avg `-0.010332`, median `-0.010753`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.01227`, avg `-0.000136`, median `-0.001577`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.018981`, avg `0.028119`, median `0.030181`
- 60d: sample `16`, primary_hit `1.0`, primary_closer `0.5625`, primary_mae `0.027781`, avg `0.079842`, median `0.088952`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.01729`, avg `-0.003055`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.013632`, avg `-0.010332`, median `-0.010753`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.01227`, avg `-0.000136`, median `-0.001577`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.018981`, avg `0.028119`, median `0.030181`
- 60d: sample `16`, primary_hit `1.0`, primary_closer `0.5625`, primary_mae `0.027781`, avg `0.079842`, median `0.088952`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3875`, primary_mae `0.015307`, avg `-0.000973`, median `-0.001404`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.01698`, avg `-0.00398`, median `-0.003858`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.024367`, avg `-0.002625`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.03751`, avg `0.007815`, median `0.015161`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.0599`, avg `0.023634`, median `0.039962`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3875`, primary_mae `0.015307`, avg `-0.000973`, median `-0.001404`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.01698`, avg `-0.00398`, median `-0.003858`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.024367`, avg `-0.002625`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.03751`, avg `0.007815`, median `0.015161`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.0599`, avg `0.023634`, median `0.039962`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.013438`, avg `-0.001717`, median `-0.001404`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.016355`, avg `-0.005372`, median `-0.003195`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.024831`, avg `-0.00552`, median `-0.007701`
- 20d: sample `40`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.038571`, avg `-0.001098`, median `0.008896`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.058981`, avg `0.00648`, median `0.002524`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.017176`, avg `-0.000229`, median `-0.001207`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.017606`, avg `-0.002589`, median `-0.005063`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.325`, primary_mae `0.023902`, avg `0.00027`, median `-0.001481`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.3`, primary_mae `0.03645`, avg `0.016728`, median `0.028346`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.45`, primary_mae `0.060818`, avg `0.040788`, median `0.061862`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3875`, primary_mae `0.015307`, avg `-0.000973`, median `-0.001404`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.01698`, avg `-0.00398`, median `-0.003858`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.024367`, avg `-0.002625`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.03751`, avg `0.007815`, median `0.015161`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.0599`, avg `0.023634`, median `0.039962`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3875`, primary_mae `0.015307`, avg `-0.000973`, median `-0.001404`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.01698`, avg `-0.00398`, median `-0.003858`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.024367`, avg `-0.002625`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.03751`, avg `0.007815`, median `0.015161`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.0599`, avg `0.023634`, median `0.039962`

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
