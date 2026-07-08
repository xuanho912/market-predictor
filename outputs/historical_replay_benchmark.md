# Historical Replay Benchmark

Generated at: `2026-07-08T04:36:28.060571+00:00`
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
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.01438`
- secondary_mean_absolute_error: `0.013785`
- primary_error_advantage: `-0.000595`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.01779`
- secondary_mean_absolute_error: `0.01637`
- primary_error_advantage: `-0.00142`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.023558`
- secondary_mean_absolute_error: `0.020673`
- primary_error_advantage: `-0.002885`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.043084`
- secondary_mean_absolute_error: `0.035702`
- primary_error_advantage: `-0.007382`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.07554`
- secondary_mean_absolute_error: `0.058064`
- primary_error_advantage: `-0.017476`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.014318`, as_primary `0`, as_primary_hit `None`, avg `-0.002482`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.017079`, as_primary `0`, as_primary_hit `None`, avg `-0.003895`, median `0.00076`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.018803`, as_primary `0`, as_primary_hit `None`, avg `-0.000336`, median `1.4e-05`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.027396`, as_primary `0`, as_primary_hit `None`, avg `0.003479`, median `0.007832`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.060092`, as_primary `0`, as_primary_hit `None`, avg `0.002097`, median `-0.005408`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.01438`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.002482`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.01779`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.003895`, median `0.00076`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.023558`, as_primary `80`, as_primary_hit `0.5`, avg `-0.000336`, median `1.4e-05`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.043084`, as_primary `80`, as_primary_hit `0.625`, avg `0.003479`, median `0.007832`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.07554`, as_primary `80`, as_primary_hit `0.475`, avg `0.002097`, median `-0.005408`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.014605`, as_primary `0`, as_primary_hit `None`, avg `-0.002482`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.017421`, as_primary `0`, as_primary_hit `None`, avg `-0.003895`, median `0.00076`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.021569`, as_primary `0`, as_primary_hit `None`, avg `-0.000336`, median `1.4e-05`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.05042`, as_primary `0`, as_primary_hit `None`, avg `0.003479`, median `0.007832`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.069879`, as_primary `0`, as_primary_hit `None`, avg `0.002097`, median `-0.005408`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.013404`, as_primary `0`, as_primary_hit `None`, avg `-0.002482`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.016662`, as_primary `0`, as_primary_hit `None`, avg `-0.003895`, median `0.00076`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.017921`, as_primary `0`, as_primary_hit `None`, avg `-0.000336`, median `1.4e-05`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.026359`, as_primary `0`, as_primary_hit `None`, avg `0.003479`, median `0.007832`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.056484`, as_primary `0`, as_primary_hit `None`, avg `0.002097`, median `-0.005408`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.01438`, avg `-0.002482`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.01779`, avg `-0.003895`, median `0.00076`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4625`, primary_mae `0.023558`, avg `-0.000336`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.043084`, avg `0.003479`, median `0.007832`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.3625`, primary_mae `0.07554`, avg `0.002097`, median `-0.005408`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.011375`, avg `-0.001013`, median `-0.00052`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.015739`, avg `-0.003092`, median `0.00286`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.022141`, avg `0.000918`, median `0.002546`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.6`, primary_mae `0.036715`, avg `-0.002482`, median `0.008863`
- 60d: sample `40`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.064956`, avg `-0.02045`, median `-0.030547`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.017386`, avg `-0.003951`, median `-0.004648`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.019842`, avg `-0.004698`, median `-0.002011`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.024975`, avg `-0.00159`, median `-0.005954`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.25`, primary_mae `0.049454`, avg `0.009439`, median `0.007521`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.086123`, avg `0.024643`, median `0.015994`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.011375, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015739, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.022141, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.036715, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.064956, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013404, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014605, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.011375, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016662, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01779, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015739, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017921, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023558, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.022141, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026359, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05042, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.036715, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056484, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07554, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.064956, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.01471`, avg `-0.015259`, median `-0.010064`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.017601`, avg `-0.014866`, median `-0.02258`
- 10d: sample `8`, primary_hit `0.0`, primary_closer `0.125`, primary_mae `0.014406`, avg `-0.013065`, median `-0.012789`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.039485`, avg `0.025458`, median `0.025462`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.081032`, avg `0.048165`, median `0.059414`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.018062`, avg `-0.011421`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.020505`, avg `-0.013562`, median `-0.013366`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.017269`, avg `-0.010813`, median `-0.013277`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.055745`, avg `0.008318`, median `0.01014`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.101463`, avg `0.026146`, median `0.041779`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.018062`, avg `-0.011421`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.020505`, avg `-0.013562`, median `-0.013366`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.017269`, avg `-0.010813`, median `-0.013277`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.055745`, avg `0.008318`, median `0.01014`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.101463`, avg `0.026146`, median `0.041779`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.01438`, avg `-0.002482`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.01779`, avg `-0.003895`, median `0.00076`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4625`, primary_mae `0.023558`, avg `-0.000336`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.043084`, avg `0.003479`, median `0.007832`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.3625`, primary_mae `0.07554`, avg `0.002097`, median `-0.005408`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.01438`, avg `-0.002482`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.01779`, avg `-0.003895`, median `0.00076`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4625`, primary_mae `0.023558`, avg `-0.000336`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.043084`, avg `0.003479`, median `0.007832`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.3625`, primary_mae `0.07554`, avg `0.002097`, median `-0.005408`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.01438`, avg `-0.002482`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.01779`, avg `-0.003895`, median `0.00076`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4625`, primary_mae `0.023558`, avg `-0.000336`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.043084`, avg `0.003479`, median `0.007832`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.3625`, primary_mae `0.07554`, avg `0.002097`, median `-0.005408`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.01438`, avg `-0.002482`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.01779`, avg `-0.003895`, median `0.00076`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4625`, primary_mae `0.023558`, avg `-0.000336`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.043084`, avg `0.003479`, median `0.007832`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.3625`, primary_mae `0.07554`, avg `0.002097`, median `-0.005408`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.4`, primary_mae `0.015495`, avg `-0.003113`, median `-0.00205`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.4167`, primary_mae `0.017605`, avg `-0.002766`, median `0.002849`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.021112`, avg `-0.000275`, median `0.000697`
- 20d: sample `60`, primary_hit `0.7`, primary_closer `0.4167`, primary_mae `0.042086`, avg `0.008491`, median `0.010966`
- 60d: sample `60`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.077829`, avg `0.003723`, median `0.00071`

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
