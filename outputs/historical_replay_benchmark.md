# Historical Replay Benchmark

Generated at: `2026-10-16T05:55:22.502315+00:00`
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
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.016888`
- secondary_mean_absolute_error: `0.016045`
- primary_error_advantage: `-0.000843`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.020595`
- secondary_mean_absolute_error: `0.018656`
- primary_error_advantage: `-0.001939`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.023723`
- secondary_mean_absolute_error: `0.023277`
- primary_error_advantage: `-0.000446`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.053348`
- secondary_mean_absolute_error: `0.041271`
- primary_error_advantage: `-0.012077`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.08077`
- secondary_mean_absolute_error: `0.062044`
- primary_error_advantage: `-0.018726`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.015102`, as_primary `0`, as_primary_hit `None`, avg `-0.007207`, median `-0.008299`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.017756`, as_primary `0`, as_primary_hit `None`, avg `-0.009576`, median `-0.011865`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.022513`, as_primary `0`, as_primary_hit `None`, avg `-0.008346`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.034733`, as_primary `0`, as_primary_hit `None`, avg `0.017347`, median `0.017588`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.055704`, as_primary `0`, as_primary_hit `None`, avg `0.053071`, median `0.059313`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016396`, as_primary `20`, as_primary_hit `0.55`, avg `-0.007207`, median `-0.008299`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.019814`, as_primary `20`, as_primary_hit `0.45`, avg `-0.009576`, median `-0.011865`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.028327`, as_primary `20`, as_primary_hit `0.45`, avg `-0.008346`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.049704`, as_primary `20`, as_primary_hit `0.5`, avg `0.017347`, median `0.017588`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.069255`, as_primary `20`, as_primary_hit `0.65`, avg `0.053071`, median `0.059313`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.01647`, as_primary `60`, as_primary_hit `0.35`, avg `-0.007207`, median `-0.008299`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.019796`, as_primary `60`, as_primary_hit `0.35`, avg `-0.009576`, median `-0.011865`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.022481`, as_primary `60`, as_primary_hit `0.3333`, avg `-0.008346`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.05438`, as_primary `60`, as_primary_hit `0.6667`, avg `0.017347`, median `0.017588`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.082828`, as_primary `60`, as_primary_hit `0.8`, avg `0.053071`, median `0.059313`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.014856`, as_primary `0`, as_primary_hit `None`, avg `-0.007207`, median `-0.008299`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.017502`, as_primary `0`, as_primary_hit `None`, avg `-0.009576`, median `-0.011865`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.020563`, as_primary `0`, as_primary_hit `None`, avg `-0.008346`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.033691`, as_primary `0`, as_primary_hit `None`, avg `0.017347`, median `0.017588`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.054554`, as_primary `0`, as_primary_hit `None`, avg `0.053071`, median `0.059313`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.017655`, avg `-0.006261`, median `-0.000971`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.021657`, avg `-0.009411`, median `-0.0084`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.022298`, avg `-0.005415`, median `-0.008686`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.054881`, avg `0.011282`, median `0.018008`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.086372`, avg `0.031497`, median `0.052147`

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.4`, primary_mae `0.016122`, avg `-0.008152`, median `-0.010058`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.475`, primary_mae `0.019533`, avg `-0.009741`, median `-0.013608`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.025148`, avg `-0.011277`, median `-0.015501`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.051816`, avg `0.023412`, median `0.017072`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.075167`, avg `0.074646`, median `0.078416`

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
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.017655`, avg `-0.006261`, median `-0.000971`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.021657`, avg `-0.009411`, median `-0.0084`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.022298`, avg `-0.005415`, median `-0.008686`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.054881`, avg `0.011282`, median `0.018008`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.086372`, avg `0.031497`, median `0.052147`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.4`, primary_mae `0.016122`, avg `-0.008152`, median `-0.010058`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.475`, primary_mae `0.019533`, avg `-0.009741`, median `-0.013608`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.025148`, avg `-0.011277`, median `-0.015501`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.051816`, avg `0.023412`, median `0.017072`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.075167`, avg `0.074646`, median `0.078416`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016122, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.019533, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.022298, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.051816, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.075167, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014856, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01647, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016122, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017502, 'direction_hit_rate': 0.375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019814, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.019533, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020563, 'direction_hit_rate': 0.3625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028327, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.022298, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033691, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05438, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.051816, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054554, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.082828, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.075167, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.011897`, avg `-0.002404`, median `0.002791`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020647`, avg `-0.003861`, median `-0.002888`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.022451`, avg `-0.00401`, median `-0.003647`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.033657`, avg `0.011979`, median `0.008728`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.037772`, avg `0.020146`, median `0.037786`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.014544`, avg `-0.002299`, median `0.001086`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.017087`, avg `-0.00359`, median `0.000995`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.019372`, avg `0.001002`, median `-0.003558`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.03268`, avg `0.013783`, median `0.017343`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.043164`, avg `0.025202`, median `0.037786`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.4375`, primary_mae `0.014556`, avg `-0.01067`, median `-0.00934`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.023111`, avg `-0.012572`, median `-0.015463`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.032236`, avg `-0.019672`, median `-0.0349`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.063598`, avg `0.008522`, median `-0.000315`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.080933`, avg `0.063985`, median `0.078416`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.016888`, avg `-0.007207`, median `-0.008299`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4875`, primary_mae `0.020595`, avg `-0.009576`, median `-0.011865`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4875`, primary_mae `0.023723`, avg `-0.008346`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.053348`, avg `0.017347`, median `0.017588`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3875`, primary_mae `0.08077`, avg `0.053071`, median `0.059313`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.016888`, avg `-0.007207`, median `-0.008299`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4875`, primary_mae `0.020595`, avg `-0.009576`, median `-0.011865`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4875`, primary_mae `0.023723`, avg `-0.008346`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.053348`, avg `0.017347`, median `0.017588`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3875`, primary_mae `0.08077`, avg `0.053071`, median `0.059313`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.017655`, avg `-0.006261`, median `-0.000971`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.021657`, avg `-0.009411`, median `-0.0084`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.022298`, avg `-0.005415`, median `-0.008686`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.054881`, avg `0.011282`, median `0.018008`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.086372`, avg `0.031497`, median `0.052147`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.4`, primary_mae `0.016122`, avg `-0.008152`, median `-0.010058`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.475`, primary_mae `0.019533`, avg `-0.009741`, median `-0.013608`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.025148`, avg `-0.011277`, median `-0.015501`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.051816`, avg `0.023412`, median `0.017072`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.075167`, avg `0.074646`, median `0.078416`

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
