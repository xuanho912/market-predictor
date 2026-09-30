# Historical Replay Benchmark

Generated at: `2026-09-30T00:55:45.730009+00:00`
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
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.018004`
- secondary_mean_absolute_error: `0.015946`
- primary_error_advantage: `-0.002058`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.019458`
- secondary_mean_absolute_error: `0.017027`
- primary_error_advantage: `-0.002431`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.021828`
- secondary_mean_absolute_error: `0.021238`
- primary_error_advantage: `-0.00059`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.050907`
- secondary_mean_absolute_error: `0.036996`
- primary_error_advantage: `-0.013911`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.0875`
- secondary_hit_rate: `0.9125`
- primary_vs_secondary_accuracy_spread: `-0.825`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.040973`
- secondary_mean_absolute_error: `0.038268`
- primary_error_advantage: `-0.002705`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.016259`, as_primary `0`, as_primary_hit `None`, avg `-0.001695`, median `-0.001624`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.01821`, as_primary `0`, as_primary_hit `None`, avg `-0.000155`, median `-0.00179`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.022273`, as_primary `0`, as_primary_hit `None`, avg `0.004249`, median `0.006554`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.032628`, as_primary `0`, as_primary_hit `None`, avg `0.023764`, median `0.0322`
- 60d: sample `80`, direction_hit `0.9125`, path_mae `0.038606`, as_primary `0`, as_primary_hit `None`, avg `0.092583`, median `0.109973`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.017089`, as_primary `0`, as_primary_hit `None`, avg `-0.001695`, median `-0.001624`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.019612`, as_primary `0`, as_primary_hit `None`, avg `-0.000155`, median `-0.00179`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.024013`, as_primary `0`, as_primary_hit `None`, avg `0.004249`, median `0.006554`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.045422`, as_primary `0`, as_primary_hit `None`, avg `0.023764`, median `0.0322`
- 60d: sample `80`, direction_hit `0.9125`, path_mae `0.041192`, as_primary `0`, as_primary_hit `None`, avg `0.092583`, median `0.109973`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.018004`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.001695`, median `-0.001624`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.019458`, as_primary `80`, as_primary_hit `0.475`, avg `-0.000155`, median `-0.00179`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.021828`, as_primary `80`, as_primary_hit `0.6`, avg `0.004249`, median `0.006554`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.050907`, as_primary `80`, as_primary_hit `0.725`, avg `0.023764`, median `0.0322`
- 60d: sample `80`, direction_hit `0.0875`, path_mae `0.040973`, as_primary `80`, as_primary_hit `0.9125`, avg `0.092583`, median `0.109973`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.01575`, as_primary `0`, as_primary_hit `None`, avg `-0.001695`, median `-0.001624`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.016851`, as_primary `0`, as_primary_hit `None`, avg `-0.000155`, median `-0.00179`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.02094`, as_primary `0`, as_primary_hit `None`, avg `0.004249`, median `0.006554`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.031464`, as_primary `0`, as_primary_hit `None`, avg `0.023764`, median `0.0322`
- 60d: sample `80`, direction_hit `0.9125`, path_mae `0.038629`, as_primary `0`, as_primary_hit `None`, avg `0.092583`, median `0.109973`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.018004`, avg `-0.001695`, median `-0.001624`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.019458`, avg `-0.000155`, median `-0.00179`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.021828`, avg `0.004249`, median `0.006554`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.050907`, avg `0.023764`, median `0.0322`
- 60d: sample `80`, primary_hit `0.0875`, primary_closer `0.475`, primary_mae `0.040973`, avg `0.092583`, median `0.109973`

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
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.022572`, avg `-0.004632`, median `-0.006398`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.021499`, avg `-0.004042`, median `-0.005714`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.034126`, avg `-0.00253`, median `-0.003925`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.075881`, avg `0.002391`, median `0.005418`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.4`, primary_mae `0.033272`, avg `0.118903`, median `0.127413`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.014146`, avg `0.001227`, median `0.002181`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.5`, primary_mae `0.014807`, avg `0.003134`, median `0.005292`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.6`, primary_mae `0.015718`, avg `0.008464`, median `0.009969`
- 20d: sample `40`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.044055`, avg `0.033205`, median `0.036357`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.525`, primary_mae `0.035311`, avg `0.091424`, median `0.10703`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.021151`, avg `-0.004604`, median `-0.008568`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.026721`, avg `-0.002847`, median `-0.010572`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.021753`, avg `0.002598`, median `-0.000753`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.039638`, avg `0.026254`, median `0.026541`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.45`, primary_mae `0.059999`, avg `0.068582`, median `0.070115`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014146, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014807, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.015718, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.039638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.033272, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01575, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018004, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014146, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016851, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019612, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014807, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02094, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024013, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.015718, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031464, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050907, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.039638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.0875, 'secondary_hit_rate': 0.9125, 'primary_vs_secondary_accuracy_spread': -0.825, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038606, 'direction_hit_rate': 0.9125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041192, 'direction_hit_rate': 0.9125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.033272, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.012832`, avg `0.005815`, median `0.008014`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.015499`, avg `0.006695`, median `0.008828`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.014721`, avg `0.009347`, median `0.01205`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.035436`, avg `0.026788`, median `0.029102`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.625`, primary_mae `0.0093`, avg `0.114868`, median `0.11635`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.014345`, avg `0.002888`, median `0.003357`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.016459`, avg `0.006423`, median `0.008828`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.018731`, avg `0.009173`, median `0.014434`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.036694`, avg `0.029622`, median `0.027795`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.625`, primary_mae `0.034752`, avg `0.091162`, median `0.111461`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.020141`, avg `-0.006554`, median `-0.010376`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.019853`, avg `-0.003422`, median `-0.005714`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.034537`, avg `-0.001776`, median `-0.003925`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.065928`, avg `-0.007903`, median `-0.016989`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.375`, primary_mae `0.029647`, avg `0.12167`, median `0.122732`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.018004`, avg `-0.001695`, median `-0.001624`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.019458`, avg `-0.000155`, median `-0.00179`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.021828`, avg `0.004249`, median `0.006554`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.050907`, avg `0.023764`, median `0.0322`
- 60d: sample `80`, primary_hit `0.0875`, primary_closer `0.475`, primary_mae `0.040973`, avg `0.092583`, median `0.109973`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.018004`, avg `-0.001695`, median `-0.001624`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.019458`, avg `-0.000155`, median `-0.00179`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.021828`, avg `0.004249`, median `0.006554`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.050907`, avg `0.023764`, median `0.0322`
- 60d: sample `80`, primary_hit `0.0875`, primary_closer `0.475`, primary_mae `0.040973`, avg `0.092583`, median `0.109973`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.014146`, avg `0.001227`, median `0.002181`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.5`, primary_mae `0.014807`, avg `0.003134`, median `0.005292`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.6`, primary_mae `0.015718`, avg `0.008464`, median `0.009969`
- 20d: sample `40`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.044055`, avg `0.033205`, median `0.036357`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.525`, primary_mae `0.035311`, avg `0.091424`, median `0.10703`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.021861`, avg `-0.004618`, median `-0.008479`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.35`, primary_mae `0.02411`, avg `-0.003444`, median `-0.006363`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.027939`, avg `3.4e-05`, median `-0.003293`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.057759`, avg `0.014323`, median `0.021423`
- 60d: sample `40`, primary_hit `0.1`, primary_closer `0.425`, primary_mae `0.046636`, avg `0.093743`, median `0.114142`

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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.4333`, primary_mae `0.019424`, avg `-0.002006`, median `-0.001624`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.4167`, primary_mae `0.021193`, avg `-0.000163`, median `-0.002857`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.024608`, avg `0.003956`, median `0.004426`
- 20d: sample `60`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.052667`, avg `0.021514`, median `0.029674`
- 60d: sample `60`, primary_hit `0.1`, primary_closer `0.5`, primary_mae `0.044109`, avg `0.091644`, median `0.113104`

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
