# Historical Replay Benchmark

Generated at: `2026-07-24T14:15:41.271547+00:00`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.021552`
- secondary_mean_absolute_error: `0.020281`
- primary_error_advantage: `-0.001271`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.028958`
- secondary_mean_absolute_error: `0.02438`
- primary_error_advantage: `-0.004578`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.034684`
- secondary_mean_absolute_error: `0.02841`
- primary_error_advantage: `-0.006274`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.6`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.078385`
- secondary_mean_absolute_error: `0.054013`
- primary_error_advantage: `-0.024372`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.111974`
- secondary_mean_absolute_error: `0.087098`
- primary_error_advantage: `-0.024876`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.018426`, as_primary `0`, as_primary_hit `None`, avg `-0.0037`, median `0.000655`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.021544`, as_primary `0`, as_primary_hit `None`, avg `-0.005547`, median `-0.001935`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.023907`, as_primary `0`, as_primary_hit `None`, avg `0.004863`, median `0.005949`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.04047`, as_primary `0`, as_primary_hit `None`, avg `0.01552`, median `0.021747`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.072921`, as_primary `0`, as_primary_hit `None`, avg `0.022185`, median `0.054511`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.02001`, as_primary `0`, as_primary_hit `None`, avg `-0.0037`, median `0.000655`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.025322`, as_primary `0`, as_primary_hit `None`, avg `-0.005547`, median `-0.001935`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.029759`, as_primary `0`, as_primary_hit `None`, avg `0.004863`, median `0.005949`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.057889`, as_primary `0`, as_primary_hit `None`, avg `0.01552`, median `0.021747`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.086456`, as_primary `0`, as_primary_hit `None`, avg `0.022185`, median `0.054511`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.021552`, as_primary `80`, as_primary_hit `0.525`, avg `-0.0037`, median `0.000655`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.028958`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.005547`, median `-0.001935`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.034684`, as_primary `80`, as_primary_hit `0.5625`, avg `0.004863`, median `0.005949`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.078385`, as_primary `80`, as_primary_hit `0.65`, avg `0.01552`, median `0.021747`
- 60d: sample `80`, direction_hit `0.35`, path_mae `0.111974`, as_primary `80`, as_primary_hit `0.65`, avg `0.022185`, median `0.054511`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.018567`, as_primary `0`, as_primary_hit `None`, avg `-0.0037`, median `0.000655`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.021325`, as_primary `0`, as_primary_hit `None`, avg `-0.005547`, median `-0.001935`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.023477`, as_primary `0`, as_primary_hit `None`, avg `0.004863`, median `0.005949`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.041913`, as_primary `0`, as_primary_hit `None`, avg `0.01552`, median `0.021747`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.074513`, as_primary `0`, as_primary_hit `None`, avg `0.022185`, median `0.054511`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.01973`, avg `-0.005848`, median `0.000684`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.026966`, avg `-0.008988`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.018842`, avg `-0.003441`, median `-0.006514`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.064234`, avg `0.012338`, median `0.020147`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.086496`, avg `0.035262`, median `0.048423`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.023373`, avg `-0.001552`, median `0.000254`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.03095`, avg `-0.002107`, median `-0.00269`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.050527`, avg `0.013167`, median `0.025887`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.3`, primary_mae `0.092537`, avg `0.018702`, median `0.042225`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.137453`, avg `0.009107`, median `0.063592`

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
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.023373`, avg `-0.001552`, median `0.000254`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.03095`, avg `-0.002107`, median `-0.00269`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.050527`, avg `0.013167`, median `0.025887`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.3`, primary_mae `0.092537`, avg `0.018702`, median `0.042225`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.137453`, avg `0.009107`, median `0.063592`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.01973`, avg `-0.005848`, median `0.000684`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.026966`, avg `-0.008988`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.018842`, avg `-0.003441`, median `-0.006514`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.064234`, avg `0.012338`, median `0.020147`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.086496`, avg `0.035262`, median `0.048423`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.01973, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.026966, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.018842, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.064234, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.086496, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018426, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021552, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.01973, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021325, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028958, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.026966, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023477, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034684, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.018842, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04047, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.078385, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.064234, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072921, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.111974, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.086496, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.029309`, avg `-0.006489`, median `-0.005846`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.035974`, avg `-0.014113`, median `-0.008611`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.014965`, avg `-0.003292`, median `-0.006886`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.06449`, avg `0.016195`, median `0.00754`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.103002`, avg `0.04523`, median `0.043932`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.027751`, avg `-0.006839`, median `0.000341`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.037194`, avg `-0.013914`, median `-0.006529`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.017674`, avg `-0.004444`, median `-0.007383`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.071977`, avg `0.01574`, median `0.024617`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.11764`, avg `0.049448`, median `0.054967`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.022434`, avg `-0.00694`, median `-0.007873`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.036043`, avg `-0.016389`, median `-0.011498`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.055797`, avg `0.003858`, median `0.022725`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.105668`, avg `0.000178`, median `0.021621`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.177209`, avg `-0.012115`, median `0.011899`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.021552`, avg `-0.0037`, median `0.000655`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.425`, primary_mae `0.028958`, avg `-0.005547`, median `-0.001935`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.034684`, avg `0.004863`, median `0.005949`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.078385`, avg `0.01552`, median `0.021747`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.111974`, avg `0.022185`, median `0.054511`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.021552`, avg `-0.0037`, median `0.000655`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.425`, primary_mae `0.028958`, avg `-0.005547`, median `-0.001935`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.034684`, avg `0.004863`, median `0.005949`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.078385`, avg `0.01552`, median `0.021747`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.111974`, avg `0.022185`, median `0.054511`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.01973`, avg `-0.005848`, median `0.000684`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.026966`, avg `-0.008988`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.018842`, avg `-0.003441`, median `-0.006514`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.064234`, avg `0.012338`, median `0.020147`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.086496`, avg `0.035262`, median `0.048423`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.023373`, avg `-0.001552`, median `0.000254`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.03095`, avg `-0.002107`, median `-0.00269`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.050527`, avg `0.013167`, median `0.025887`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.3`, primary_mae `0.092537`, avg `0.018702`, median `0.042225`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.137453`, avg `0.009107`, median `0.063592`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.021552`, avg `-0.0037`, median `0.000655`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.425`, primary_mae `0.028958`, avg `-0.005547`, median `-0.001935`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.034684`, avg `0.004863`, median `0.005949`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.078385`, avg `0.01552`, median `0.021747`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.111974`, avg `0.022185`, median `0.054511`

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
