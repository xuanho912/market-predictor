# Historical Replay Benchmark

Generated at: `2026-06-29T23:38:20.605091+00:00`
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
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.01309`
- secondary_mean_absolute_error: `0.013255`
- primary_error_advantage: `0.000165`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.017975`
- secondary_mean_absolute_error: `0.016777`
- primary_error_advantage: `-0.001198`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.028445`
- secondary_mean_absolute_error: `0.021891`
- primary_error_advantage: `-0.006554`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.052521`
- secondary_mean_absolute_error: `0.034465`
- primary_error_advantage: `-0.018056`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.08603`
- secondary_mean_absolute_error: `0.062693`
- primary_error_advantage: `-0.023337`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.012839`, as_primary `0`, as_primary_hit `None`, avg `-0.001581`, median `-0.002402`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.016626`, as_primary `0`, as_primary_hit `None`, avg `-0.004774`, median `-0.006441`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.021498`, as_primary `0`, as_primary_hit `None`, avg `0.000219`, median `-0.001153`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.030251`, as_primary `0`, as_primary_hit `None`, avg `0.011734`, median `0.015533`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.063234`, as_primary `0`, as_primary_hit `None`, avg `0.036402`, median `0.044937`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.012787`, as_primary `60`, as_primary_hit `0.4167`, avg `-0.001581`, median `-0.002402`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.017484`, as_primary `60`, as_primary_hit `0.4167`, avg `-0.004774`, median `-0.006441`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.025463`, as_primary `60`, as_primary_hit `0.5`, avg `0.000219`, median `-0.001153`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.045298`, as_primary `60`, as_primary_hit `0.6833`, avg `0.011734`, median `0.015533`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.08738`, as_primary `60`, as_primary_hit `0.7167`, avg `0.036402`, median `0.044937`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.01376`, as_primary `20`, as_primary_hit `0.4`, avg `-0.001581`, median `-0.002402`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017909`, as_primary `20`, as_primary_hit `0.5`, avg `-0.004774`, median `-0.006441`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.027205`, as_primary `20`, as_primary_hit `0.4`, avg `0.000219`, median `-0.001153`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.054696`, as_primary `20`, as_primary_hit `0.65`, avg `0.011734`, median `0.015533`
- 60d: sample `80`, direction_hit `0.35`, path_mae `0.074319`, as_primary `20`, as_primary_hit `0.45`, avg `0.036402`, median `0.044937`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.012627`, as_primary `0`, as_primary_hit `None`, avg `-0.001581`, median `-0.002402`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.016356`, as_primary `0`, as_primary_hit `None`, avg `-0.004774`, median `-0.006441`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.020784`, as_primary `0`, as_primary_hit `None`, avg `0.000219`, median `-0.001153`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.028274`, as_primary `0`, as_primary_hit `None`, avg `0.011734`, median `0.015533`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.057305`, as_primary `0`, as_primary_hit `None`, avg `0.036402`, median `0.044937`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.7`, primary_mae `0.010237`, avg `-0.00318`, median `-0.002593`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.6`, primary_mae `0.015377`, avg `-0.005388`, median `-0.005247`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.02611`, avg `0.003389`, median `0.001486`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.065408`, avg `0.007844`, median `-0.002157`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.165321`, avg `0.06252`, median `0.069591`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.01546`, avg `-0.000119`, median `-0.001735`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.019664`, avg `-0.004472`, median `-0.008169`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.325`, primary_mae `0.027164`, avg `0.00227`, median `-0.000741`
- 20d: sample `40`, primary_hit `0.8`, primary_closer `0.275`, primary_mae `0.039778`, avg `0.021217`, median `0.028709`
- 60d: sample `40`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.06391`, avg `0.045822`, median `0.061862`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.011203`, avg `-0.002904`, median `-0.003287`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.017194`, avg `-0.004766`, median `-0.000801`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.033345`, avg `-0.007054`, median `-0.006018`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.065122`, avg `-0.003342`, median `0.01201`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.050979`, avg `-0.008556`, median `-0.005354`

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
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.011203`, avg `-0.002904`, median `-0.003287`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.017194`, avg `-0.004766`, median `-0.000801`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.033345`, avg `-0.007054`, median `-0.006018`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.065122`, avg `-0.003342`, median `0.01201`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.050979`, avg `-0.008556`, median `-0.005354`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.5667`, primary_mae `0.013719`, avg `-0.001139`, median `-0.001981`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.45`, primary_mae `0.018235`, avg `-0.004777`, median `-0.006654`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.026812`, avg `0.002643`, median `-7.9e-05`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.3`, primary_mae `0.048321`, avg `0.01676`, median `0.016418`
- 60d: sample `60`, primary_hit `0.7167`, primary_closer `0.35`, primary_mae `0.097714`, avg `0.051388`, median `0.063825`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.011203, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017194, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.026812, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.048321, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.050979, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012627, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01376, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.011203, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016356, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017909, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017194, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020784, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027205, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.026812, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028274, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054696, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.048321, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057305, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.08738, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.050979, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.016192`, avg `-0.004068`, median `-0.006094`
- 5d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.018457`, avg `-0.018992`, median `-0.018285`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.010986`, avg `0.00331`, median `0.00206`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.0`, primary_mae `0.029357`, avg `0.029013`, median `0.030181`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.25`, primary_mae `0.032229`, avg `0.086977`, median `0.093637`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.016603`, avg `-0.004545`, median `-0.005953`
- 5d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.017422`, avg `-0.015141`, median `-0.014993`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.011859`, avg `-0.001797`, median `-0.00223`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.125`, primary_mae `0.035153`, avg `0.02322`, median `0.028979`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.055438`, avg `0.064095`, median `0.083174`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.011167`, avg `-0.004003`, median `-0.003287`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.017708`, avg `-0.005404`, median `-0.000801`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.033445`, avg `-0.007511`, median `-0.006414`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.062242`, avg `-0.007799`, median `0.009366`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.049622`, avg `-0.018596`, median `-0.020937`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.525`, primary_mae `0.01309`, avg `-0.001581`, median `-0.002402`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.45`, primary_mae `0.017975`, avg `-0.004774`, median `-0.006441`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.3375`, primary_mae `0.028445`, avg `0.000219`, median `-0.001153`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.2875`, primary_mae `0.052521`, avg `0.011734`, median `0.015533`
- 60d: sample `80`, primary_hit `0.675`, primary_closer `0.4`, primary_mae `0.08603`, avg `0.036402`, median `0.044937`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.525`, primary_mae `0.01309`, avg `-0.001581`, median `-0.002402`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.45`, primary_mae `0.017975`, avg `-0.004774`, median `-0.006441`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.3375`, primary_mae `0.028445`, avg `0.000219`, median `-0.001153`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.2875`, primary_mae `0.052521`, avg `0.011734`, median `0.015533`
- 60d: sample `80`, primary_hit `0.675`, primary_closer `0.4`, primary_mae `0.08603`, avg `0.036402`, median `0.044937`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.5667`, primary_mae `0.013719`, avg `-0.001139`, median `-0.001981`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.45`, primary_mae `0.018235`, avg `-0.004777`, median `-0.006654`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.026812`, avg `0.002643`, median `-7.9e-05`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.3`, primary_mae `0.048321`, avg `0.01676`, median `0.016418`
- 60d: sample `60`, primary_hit `0.7167`, primary_closer `0.35`, primary_mae `0.097714`, avg `0.051388`, median `0.063825`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.011203`, avg `-0.002904`, median `-0.003287`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.017194`, avg `-0.004766`, median `-0.000801`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.033345`, avg `-0.007054`, median `-0.006018`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.065122`, avg `-0.003342`, median `0.01201`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.050979`, avg `-0.008556`, median `-0.005354`

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
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.01072`, avg `-0.003042`, median `-0.002845`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.016286`, avg `-0.005077`, median `-0.004256`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.029727`, avg `-0.001833`, median `-0.003297`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.065265`, avg `0.002251`, median `0.005773`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.10815`, avg `0.026982`, median `0.032181`

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
