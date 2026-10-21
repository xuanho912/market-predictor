# Historical Replay Benchmark

Generated at: `2026-10-21T06:06:05.243200+00:00`
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
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.016474`
- secondary_mean_absolute_error: `0.014474`
- primary_error_advantage: `-0.002`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.020542`
- secondary_mean_absolute_error: `0.018007`
- primary_error_advantage: `-0.002535`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.024258`
- secondary_mean_absolute_error: `0.021826`
- primary_error_advantage: `-0.002432`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.0472`
- secondary_mean_absolute_error: `0.030928`
- primary_error_advantage: `-0.016272`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.087998`
- secondary_mean_absolute_error: `0.067021`
- primary_error_advantage: `-0.020977`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.014551`, as_primary `0`, as_primary_hit `None`, avg `-0.000977`, median `0.000823`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.019029`, as_primary `0`, as_primary_hit `None`, avg `-0.002505`, median `0.00133`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.02381`, as_primary `0`, as_primary_hit `None`, avg `-0.002243`, median `-0.001038`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.030681`, as_primary `0`, as_primary_hit `None`, avg `0.014385`, median `0.012168`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.065328`, as_primary `0`, as_primary_hit `None`, avg `0.034655`, median `0.046203`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.015988`, as_primary `0`, as_primary_hit `None`, avg `-0.000977`, median `0.000823`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.023836`, as_primary `0`, as_primary_hit `None`, avg `-0.002505`, median `0.00133`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.031855`, as_primary `0`, as_primary_hit `None`, avg `-0.002243`, median `-0.001038`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.046425`, as_primary `0`, as_primary_hit `None`, avg `0.014385`, median `0.012168`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.083701`, as_primary `0`, as_primary_hit `None`, avg `0.034655`, median `0.046203`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.016474`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.000977`, median `0.000823`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.020542`, as_primary `80`, as_primary_hit `0.525`, avg `-0.002505`, median `0.00133`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.024258`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.002243`, median `-0.001038`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.0472`, as_primary `80`, as_primary_hit `0.65`, avg `0.014385`, median `0.012168`
- 60d: sample `80`, direction_hit `0.3125`, path_mae `0.087998`, as_primary `80`, as_primary_hit `0.6875`, avg `0.034655`, median `0.046203`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.014459`, as_primary `0`, as_primary_hit `None`, avg `-0.000977`, median `0.000823`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.017756`, as_primary `0`, as_primary_hit `None`, avg `-0.002505`, median `0.00133`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.021005`, as_primary `0`, as_primary_hit `None`, avg `-0.002243`, median `-0.001038`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.028772`, as_primary `0`, as_primary_hit `None`, avg `0.014385`, median `0.012168`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.064268`, as_primary `0`, as_primary_hit `None`, avg `0.034655`, median `0.046203`

## Edge Status Performance

### NO_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017858`, avg `-0.0`, median `0.000371`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022799`, avg `0.001017`, median `-0.000601`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.030644`, avg `0.00778`, median `0.007808`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.043668`, avg `0.024637`, median `0.013284`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.062104`, avg `0.060023`, median `0.054719`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.016695`, avg `4.2e-05`, median `-0.00065`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.021654`, avg `-0.005327`, median `-0.012082`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.03215`, avg `-0.016779`, median `-0.024199`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.055034`, avg `-0.001306`, median `-0.000315`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.103056`, avg `0.050935`, median `0.061971`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.015671`, avg `-0.001975`, median `0.001174`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.018857`, avg `-0.002855`, median `0.002614`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.017119`, avg `1.4e-05`, median `-0.000315`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.3`, primary_mae `0.045049`, avg `0.017104`, median `0.020913`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.093417`, avg `0.013832`, median `0.028478`

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
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.017277`, avg `2.1e-05`, median `-0.00065`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.022226`, avg `-0.002155`, median `-0.00735`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.031397`, avg `-0.0045`, median `-0.011642`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.325`, primary_mae `0.049351`, avg `0.011666`, median `0.008277`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.08258`, avg `0.055479`, median `0.057087`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.015671`, avg `-0.001975`, median `0.001174`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.018857`, avg `-0.002855`, median `0.002614`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.017119`, avg `1.4e-05`, median `-0.000315`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.3`, primary_mae `0.045049`, avg `0.017104`, median `0.020913`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.093417`, avg `0.013832`, median `0.028478`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.015671, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018857, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.017119, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.045049, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.08258, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014459, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016474, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.015671, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017756, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023836, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018857, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021005, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031855, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.017119, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028772, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0472, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.045049, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064268, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.087998, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.08258, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.011255`, avg `0.00592`, median `0.00607`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.010298`, avg `0.006419`, median `0.009732`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.009349`, avg `0.008099`, median `0.007771`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.037895`, avg `0.017643`, median `0.021414`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.103065`, avg `-0.009263`, median `0.035301`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.012054`, avg `0.002668`, median `0.005444`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.014339`, avg `0.005368`, median `0.009672`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.01488`, avg `0.010743`, median `0.011607`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.039437`, avg `0.017162`, median `0.024588`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.09764`, avg `-0.000961`, median `0.023396`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017582`, avg `-0.000904`, median `0.000371`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.022389`, avg `-0.001139`, median `-0.007393`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.030316`, avg `0.00503`, median `0.004511`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.041508`, avg `0.021716`, median `0.011663`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.062868`, avg `0.066332`, median `0.061264`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.016474`, avg `-0.000977`, median `0.000823`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.020542`, avg `-0.002505`, median `0.00133`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.425`, primary_mae `0.024258`, avg `-0.002243`, median `-0.001038`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.3125`, primary_mae `0.0472`, avg `0.014385`, median `0.012168`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3625`, primary_mae `0.087998`, avg `0.034655`, median `0.046203`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.016474`, avg `-0.000977`, median `0.000823`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.020542`, avg `-0.002505`, median `0.00133`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.425`, primary_mae `0.024258`, avg `-0.002243`, median `-0.001038`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.3125`, primary_mae `0.0472`, avg `0.014385`, median `0.012168`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3625`, primary_mae `0.087998`, avg `0.034655`, median `0.046203`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.015671`, avg `-0.001975`, median `0.001174`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.018857`, avg `-0.002855`, median `0.002614`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.017119`, avg `1.4e-05`, median `-0.000315`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.3`, primary_mae `0.045049`, avg `0.017104`, median `0.020913`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.093417`, avg `0.013832`, median `0.028478`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.017277`, avg `2.1e-05`, median `-0.00065`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.022226`, avg `-0.002155`, median `-0.00735`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.031397`, avg `-0.0045`, median `-0.011642`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.325`, primary_mae `0.049351`, avg `0.011666`, median `0.008277`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.08258`, avg `0.055479`, median `0.057087`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.016474`, avg `-0.000977`, median `0.000823`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.020542`, avg `-0.002505`, median `0.00133`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.425`, primary_mae `0.024258`, avg `-0.002243`, median `-0.001038`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.3125`, primary_mae `0.0472`, avg `0.014385`, median `0.012168`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3625`, primary_mae `0.087998`, avg `0.034655`, median `0.046203`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.016474`, avg `-0.000977`, median `0.000823`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.020542`, avg `-0.002505`, median `0.00133`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.425`, primary_mae `0.024258`, avg `-0.002243`, median `-0.001038`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.3125`, primary_mae `0.0472`, avg `0.014385`, median `0.012168`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3625`, primary_mae `0.087998`, avg `0.034655`, median `0.046203`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
