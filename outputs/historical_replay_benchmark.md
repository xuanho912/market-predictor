# Historical Replay Benchmark

Generated at: `2026-10-15T00:14:28.201106+00:00`
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
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.018399`
- secondary_mean_absolute_error: `0.015982`
- primary_error_advantage: `-0.002417`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.02135`
- secondary_mean_absolute_error: `0.020341`
- primary_error_advantage: `-0.001009`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.026966`
- secondary_mean_absolute_error: `0.026278`
- primary_error_advantage: `-0.000688`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.575`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.044426`
- secondary_mean_absolute_error: `0.033307`
- primary_error_advantage: `-0.011119`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1375`
- secondary_hit_rate: `0.8625`
- primary_vs_secondary_accuracy_spread: `-0.725`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.047605`
- secondary_mean_absolute_error: `0.044553`
- primary_error_advantage: `-0.003052`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.015828`, as_primary `0`, as_primary_hit `None`, avg `0.005662`, median `0.006946`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.02022`, as_primary `0`, as_primary_hit `None`, avg `0.006502`, median `0.00805`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.026465`, as_primary `0`, as_primary_hit `None`, avg `0.007902`, median `0.007997`
- 20d: sample `80`, direction_hit `0.8125`, path_mae `0.030734`, as_primary `0`, as_primary_hit `None`, avg `0.033253`, median `0.033877`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.049123`, as_primary `0`, as_primary_hit `None`, avg `0.086249`, median `0.096112`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.016987`, as_primary `0`, as_primary_hit `None`, avg `0.005662`, median `0.006946`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.023635`, as_primary `0`, as_primary_hit `None`, avg `0.006502`, median `0.00805`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.030439`, as_primary `0`, as_primary_hit `None`, avg `0.007902`, median `0.007997`
- 20d: sample `80`, direction_hit `0.8125`, path_mae `0.04118`, as_primary `0`, as_primary_hit `None`, avg `0.033253`, median `0.033877`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.05938`, as_primary `0`, as_primary_hit `None`, avg `0.086249`, median `0.096112`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.018399`, as_primary `80`, as_primary_hit `0.625`, avg `0.005662`, median `0.006946`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.02135`, as_primary `80`, as_primary_hit `0.6`, avg `0.006502`, median `0.00805`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.026966`, as_primary `80`, as_primary_hit `0.625`, avg `0.007902`, median `0.007997`
- 20d: sample `80`, direction_hit `0.1875`, path_mae `0.044426`, as_primary `80`, as_primary_hit `0.8125`, avg `0.033253`, median `0.033877`
- 60d: sample `80`, direction_hit `0.1375`, path_mae `0.047605`, as_primary `80`, as_primary_hit `0.8625`, avg `0.086249`, median `0.096112`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.016093`, as_primary `0`, as_primary_hit `None`, avg `0.005662`, median `0.006946`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.019368`, as_primary `0`, as_primary_hit `None`, avg `0.006502`, median `0.00805`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.025009`, as_primary `0`, as_primary_hit `None`, avg `0.007902`, median `0.007997`
- 20d: sample `80`, direction_hit `0.8125`, path_mae `0.028831`, as_primary `0`, as_primary_hit `None`, avg `0.033253`, median `0.033877`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.044958`, as_primary `0`, as_primary_hit `None`, avg `0.086249`, median `0.096112`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.018399`, avg `0.005662`, median `0.006946`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.02135`, avg `0.006502`, median `0.00805`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.5375`, primary_mae `0.026966`, avg `0.007902`, median `0.007997`
- 20d: sample `80`, primary_hit `0.1875`, primary_closer `0.4`, primary_mae `0.044426`, avg `0.033253`, median `0.033877`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.4375`, primary_mae `0.047605`, avg `0.086249`, median `0.096112`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.275`, primary_closer `0.45`, primary_mae `0.013788`, avg `0.007213`, median `0.011685`
- 5d: sample `40`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.0164`, avg `0.009037`, median `0.011847`
- 10d: sample `40`, primary_hit `0.25`, primary_closer `0.575`, primary_mae `0.018554`, avg `0.013403`, median `0.014434`
- 20d: sample `40`, primary_hit `0.1`, primary_closer `0.425`, primary_mae `0.034386`, avg `0.039746`, median `0.036616`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.425`, primary_mae `0.03296`, avg `0.078624`, median `0.086443`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.02301`, avg `0.004111`, median `0.001496`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.0263`, avg `0.003966`, median `-0.002596`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.035378`, avg `0.002401`, median `0.001307`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.054466`, avg `0.026761`, median `0.024105`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.062249`, avg `0.093874`, median `0.113344`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.013788, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.0164, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.018554, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.034386, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.075, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.03296, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015828, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018399, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.013788, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019368, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023635, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.0164, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025009, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030439, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.018554, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028831, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044426, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.034386, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1375, 'secondary_hit_rate': 0.8625, 'primary_vs_secondary_accuracy_spread': -0.725, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044958, 'direction_hit_rate': 0.8625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05938, 'direction_hit_rate': 0.8625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.075, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.03296, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.019547`, avg `0.005525`, median `0.014755`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.875`, primary_mae `0.010801`, avg `0.005819`, median `0.008828`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.875`, primary_mae `0.015932`, avg `0.009112`, median `0.013415`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.5`, primary_mae `0.036961`, avg `0.047306`, median `0.050926`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.059503`, avg `0.063421`, median `0.093471`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.018623`, avg `0.008242`, median `0.016082`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.6875`, primary_mae `0.01751`, avg `0.009794`, median `0.011781`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.625`, primary_mae `0.022351`, avg `0.016005`, median `0.02208`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.4375`, primary_mae `0.044084`, avg `0.052477`, median `0.058396`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.044735`, avg `0.080934`, median `0.09828`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.024249`, avg `0.004775`, median `0.001496`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.028024`, avg `0.007033`, median `0.001638`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.041128`, avg `-0.005673`, median `-0.020135`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.071575`, avg `0.016577`, median `-0.008263`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.4375`, primary_mae `0.039866`, avg `0.137809`, median `0.128796`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.018399`, avg `0.005662`, median `0.006946`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.02135`, avg `0.006502`, median `0.00805`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.5375`, primary_mae `0.026966`, avg `0.007902`, median `0.007997`
- 20d: sample `80`, primary_hit `0.1875`, primary_closer `0.4`, primary_mae `0.044426`, avg `0.033253`, median `0.033877`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.4375`, primary_mae `0.047605`, avg `0.086249`, median `0.096112`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.018399`, avg `0.005662`, median `0.006946`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.02135`, avg `0.006502`, median `0.00805`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.5375`, primary_mae `0.026966`, avg `0.007902`, median `0.007997`
- 20d: sample `80`, primary_hit `0.1875`, primary_closer `0.4`, primary_mae `0.044426`, avg `0.033253`, median `0.033877`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.4375`, primary_mae `0.047605`, avg `0.086249`, median `0.096112`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.275`, primary_closer `0.45`, primary_mae `0.013788`, avg `0.007213`, median `0.011685`
- 5d: sample `40`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.0164`, avg `0.009037`, median `0.011847`
- 10d: sample `40`, primary_hit `0.25`, primary_closer `0.575`, primary_mae `0.018554`, avg `0.013403`, median `0.014434`
- 20d: sample `40`, primary_hit `0.1`, primary_closer `0.425`, primary_mae `0.034386`, avg `0.039746`, median `0.036616`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.425`, primary_mae `0.03296`, avg `0.078624`, median `0.086443`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.02301`, avg `0.004111`, median `0.001496`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.0263`, avg `0.003966`, median `-0.002596`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.035378`, avg `0.002401`, median `0.001307`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.054466`, avg `0.026761`, median `0.024105`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.062249`, avg `0.093874`, median `0.113344`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.018399`, avg `0.005662`, median `0.006946`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.02135`, avg `0.006502`, median `0.00805`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.5375`, primary_mae `0.026966`, avg `0.007902`, median `0.007997`
- 20d: sample `80`, primary_hit `0.1875`, primary_closer `0.4`, primary_mae `0.044426`, avg `0.033253`, median `0.033877`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.4375`, primary_mae `0.047605`, avg `0.086249`, median `0.096112`

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
