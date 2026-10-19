# Historical Replay Benchmark

Generated at: `2026-10-19T18:47:03.556955+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
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
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.017374`
- secondary_mean_absolute_error: `0.015929`
- primary_error_advantage: `-0.001445`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.022902`
- secondary_mean_absolute_error: `0.01933`
- primary_error_advantage: `-0.003572`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.030107`
- secondary_mean_absolute_error: `0.025299`
- primary_error_advantage: `-0.004808`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.051621`
- secondary_mean_absolute_error: `0.032044`
- primary_error_advantage: `-0.019577`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.095814`
- secondary_mean_absolute_error: `0.062893`
- primary_error_advantage: `-0.032921`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.015874`, as_primary `0`, as_primary_hit `None`, avg `-0.006434`, median `-0.007503`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.019459`, as_primary `0`, as_primary_hit `None`, avg `-0.00524`, median `-0.002614`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.026924`, as_primary `0`, as_primary_hit `None`, avg `-0.001401`, median `-0.002237`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.03456`, as_primary `0`, as_primary_hit `None`, avg `0.018832`, median `0.014409`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.064938`, as_primary `0`, as_primary_hit `None`, avg `0.048108`, median `0.059055`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.017858`, as_primary `0`, as_primary_hit `None`, avg `-0.006434`, median `-0.007503`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.02195`, as_primary `0`, as_primary_hit `None`, avg `-0.00524`, median `-0.002614`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.032834`, as_primary `0`, as_primary_hit `None`, avg `-0.001401`, median `-0.002237`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.050766`, as_primary `0`, as_primary_hit `None`, avg `0.018832`, median `0.014409`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.084152`, as_primary `0`, as_primary_hit `None`, avg `0.048108`, median `0.059055`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.017374`, as_primary `80`, as_primary_hit `0.4`, avg `-0.006434`, median `-0.007503`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.022902`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.00524`, median `-0.002614`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.030107`, as_primary `80`, as_primary_hit `0.475`, avg `-0.001401`, median `-0.002237`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.051621`, as_primary `80`, as_primary_hit `0.6125`, avg `0.018832`, median `0.014409`
- 60d: sample `80`, direction_hit `0.3`, path_mae `0.095814`, as_primary `80`, as_primary_hit `0.7`, avg `0.048108`, median `0.059055`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.015929`, as_primary `0`, as_primary_hit `None`, avg `-0.006434`, median `-0.007503`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.01933`, as_primary `0`, as_primary_hit `None`, avg `-0.00524`, median `-0.002614`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.025299`, as_primary `0`, as_primary_hit `None`, avg `-0.001401`, median `-0.002237`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.032044`, as_primary `0`, as_primary_hit `None`, avg `0.018832`, median `0.014409`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.062893`, as_primary `0`, as_primary_hit `None`, avg `0.048108`, median `0.059055`

## Edge Status Performance

### RISK_WARNING
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6667`, primary_closer `0.4833`, primary_mae `0.018476`, avg `-0.00811`, median `-0.011656`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.4333`, primary_mae `0.024928`, avg `-0.00605`, median `-0.007502`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.3833`, primary_mae `0.03476`, avg `-0.001357`, median `-0.002237`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.3`, primary_mae `0.056442`, avg `0.021872`, median `0.016431`
- 60d: sample `60`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.110558`, avg `0.061207`, median `0.075201`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.01407`, avg `-0.001409`, median `0.003047`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.016823`, avg `-0.00281`, median `0.000995`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.016151`, avg `-0.001531`, median `-0.003558`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.037158`, avg `0.00971`, median `0.009052`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.051581`, avg `0.008812`, median `0.005352`

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
- 3d: sample `40`, primary_hit `0.7`, primary_closer `0.525`, primary_mae `0.017122`, avg `-0.00829`, median `-0.014891`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.023698`, avg `-0.004539`, median `-0.010588`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.041572`, avg `0.001172`, median `0.003591`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.059591`, avg `0.023835`, median `0.014557`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.117546`, avg `0.074414`, median `0.079581`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.017627`, avg `-0.004579`, median `0.000241`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.022106`, avg `-0.00594`, median `0.000888`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.018643`, avg `-0.003973`, median `-0.006665`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.043651`, avg `0.013828`, median `0.013035`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.074082`, avg `0.021802`, median `0.03183`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.017122, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.022106, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.018643, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.043651, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.074082, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015874, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017858, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.017122, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01933, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022902, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.022106, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025299, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032834, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.018643, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032044, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051621, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.043651, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062893, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.095814, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.074082, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.019298`, avg `-0.008796`, median `-0.010064`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.023252`, avg `-0.012434`, median `-0.02258`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.017356`, avg `-0.00345`, median `-0.005954`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.065718`, avg `0.037655`, median `0.050926`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.128741`, avg `0.072565`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.023821`, avg `-0.005514`, median `-0.001624`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.028007`, avg `-0.007552`, median `-0.000171`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.018413`, avg `-0.003682`, median `-0.008236`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.055765`, avg `0.027702`, median `0.025462`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.111499`, avg `0.054612`, median `0.066096`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.017709`, avg `-0.01126`, median `-0.016441`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.020231`, avg `-0.004381`, median `-0.008382`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.036198`, avg `0.007137`, median `0.004841`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.125`, primary_mae `0.062266`, avg `0.021256`, median `0.014557`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.125`, primary_mae `0.160255`, avg `0.068585`, median `0.068484`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.017374`, avg `-0.006434`, median `-0.007503`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.022902`, avg `-0.00524`, median `-0.002614`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.030107`, avg `-0.001401`, median `-0.002237`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.051621`, avg `0.018832`, median `0.014409`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.095814`, avg `0.048108`, median `0.059055`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.017374`, avg `-0.006434`, median `-0.007503`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.022902`, avg `-0.00524`, median `-0.002614`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.030107`, avg `-0.001401`, median `-0.002237`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.051621`, avg `0.018832`, median `0.014409`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.095814`, avg `0.048108`, median `0.059055`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.017627`, avg `-0.004579`, median `0.000241`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.022106`, avg `-0.00594`, median `0.000888`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.018643`, avg `-0.003973`, median `-0.006665`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.043651`, avg `0.013828`, median `0.013035`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.074082`, avg `0.021802`, median `0.03183`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.7`, primary_closer `0.525`, primary_mae `0.017122`, avg `-0.00829`, median `-0.014891`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.023698`, avg `-0.004539`, median `-0.010588`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.041572`, avg `0.001172`, median `0.003591`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.059591`, avg `0.023835`, median `0.014557`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.117546`, avg `0.074414`, median `0.079581`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.017374`, avg `-0.006434`, median `-0.007503`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.022902`, avg `-0.00524`, median `-0.002614`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.030107`, avg `-0.001401`, median `-0.002237`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.051621`, avg `0.018832`, median `0.014409`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.095814`, avg `0.048108`, median `0.059055`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.017374`, avg `-0.006434`, median `-0.007503`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.022902`, avg `-0.00524`, median `-0.002614`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.030107`, avg `-0.001401`, median `-0.002237`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.051621`, avg `0.018832`, median `0.014409`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.095814`, avg `0.048108`, median `0.059055`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
