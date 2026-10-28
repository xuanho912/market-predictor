# Historical Replay Benchmark

Generated at: `2026-10-28T00:59:14.165692+00:00`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.018358`
- secondary_mean_absolute_error: `0.020779`
- primary_error_advantage: `0.002421`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.027471`
- secondary_mean_absolute_error: `0.028357`
- primary_error_advantage: `0.000886`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.042696`
- secondary_mean_absolute_error: `0.044953`
- primary_error_advantage: `0.002257`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.55`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.064008`
- secondary_mean_absolute_error: `0.058689`
- primary_error_advantage: `-0.005319`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.054005`
- secondary_mean_absolute_error: `0.048015`
- primary_error_advantage: `-0.00599`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.018119`, as_primary `0`, as_primary_hit `None`, avg `0.003206`, median `0.007812`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.024515`, as_primary `0`, as_primary_hit `None`, avg `0.001098`, median `0.004099`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.03527`, as_primary `0`, as_primary_hit `None`, avg `-0.003306`, median `0.000938`
- 20d: sample `80`, direction_hit `0.4875`, path_mae `0.041776`, as_primary `0`, as_primary_hit `None`, avg `-0.007112`, median `-0.002679`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.045634`, as_primary `0`, as_primary_hit `None`, avg `0.067`, median `0.069096`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.019707`, as_primary `20`, as_primary_hit `0.65`, avg `0.003206`, median `0.007812`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.027618`, as_primary `20`, as_primary_hit `0.65`, avg `0.001098`, median `0.004099`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.043265`, as_primary `20`, as_primary_hit `0.55`, avg `-0.003306`, median `0.000938`
- 20d: sample `80`, direction_hit `0.4875`, path_mae `0.060792`, as_primary `20`, as_primary_hit `0.5`, avg `-0.007112`, median `-0.002679`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.049981`, as_primary `20`, as_primary_hit `0.95`, avg `0.067`, median `0.069096`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.019575`, as_primary `60`, as_primary_hit `0.5833`, avg `0.003206`, median `0.007812`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.02778`, as_primary `60`, as_primary_hit `0.5333`, avg `0.001098`, median `0.004099`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.046288`, as_primary `60`, as_primary_hit `0.5`, avg `-0.003306`, median `0.000938`
- 20d: sample `80`, direction_hit `0.5125`, path_mae `0.067192`, as_primary `60`, as_primary_hit `0.4833`, avg `-0.007112`, median `-0.002679`
- 60d: sample `80`, direction_hit `0.1375`, path_mae `0.052094`, as_primary `60`, as_primary_hit `0.8333`, avg `0.067`, median `0.069096`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.018263`, as_primary `0`, as_primary_hit `None`, avg `0.003206`, median `0.007812`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.024149`, as_primary `0`, as_primary_hit `None`, avg `0.001098`, median `0.004099`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.034657`, as_primary `0`, as_primary_hit `None`, avg `-0.003306`, median `0.000938`
- 20d: sample `80`, direction_hit `0.4875`, path_mae `0.041222`, as_primary `0`, as_primary_hit `None`, avg `-0.007112`, median `-0.002679`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.044813`, as_primary `0`, as_primary_hit `None`, avg `0.067`, median `0.069096`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.018149`, avg `0.005634`, median `0.018118`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.02886`, avg `0.004608`, median `0.004099`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.040594`, avg `0.006705`, median `0.02112`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.071981`, avg `-0.003088`, median `0.007553`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.4`, primary_mae `0.039538`, avg `0.061751`, median `0.062686`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.5`, primary_mae `0.018428`, avg `0.002397`, median `0.006198`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.027008`, avg `-7.2e-05`, median `0.003462`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.043396`, avg `-0.006644`, median `-0.001287`
- 20d: sample `60`, primary_hit `0.5167`, primary_closer `0.4333`, primary_mae `0.061351`, avg `-0.008454`, median `-0.002679`
- 60d: sample `60`, primary_hit `0.1667`, primary_closer `0.45`, primary_mae `0.058827`, avg `0.06875`, median `0.075016`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.018149`, avg `0.005634`, median `0.018118`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.02886`, avg `0.004608`, median `0.004099`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.040594`, avg `0.006705`, median `0.02112`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.071981`, avg `-0.003088`, median `0.007553`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.4`, primary_mae `0.039538`, avg `0.061751`, median `0.062686`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.019069`, avg `0.001213`, median `0.006198`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.027501`, avg `-0.001195`, median `0.006365`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.036305`, avg `-0.005468`, median `0.001125`
- 20d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.051578`, avg `-0.007868`, median `-0.014419`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.475`, primary_mae `0.054014`, avg `0.07054`, median `0.070782`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.017145`, avg `0.004766`, median `0.005949`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.026023`, avg `0.002174`, median `-0.000823`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.057579`, avg `-0.008994`, median `-0.005818`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.080895`, avg `-0.009624`, median `0.007176`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.068454`, avg `0.065169`, median `0.091555`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.017145, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.026023, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.036305, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.051578, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.039538, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018119, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019707, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.017145, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024149, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02778, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.026023, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034657, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.046288, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.036305, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041222, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067192, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.051578, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044813, 'direction_hit_rate': 0.8625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052094, 'direction_hit_rate': 0.1375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.039538, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016475`, avg `0.011129`, median `0.018909`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.031813`, avg `0.008236`, median `0.016774`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.045823`, avg `0.003698`, median `0.004277`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.070879`, avg `-0.003955`, median `-0.002353`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.047285`, avg `0.055409`, median `0.067424`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.020595`, avg `0.001653`, median `0.010214`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.032947`, avg `-0.001018`, median `0.001372`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.047209`, avg `-0.002354`, median `-0.008604`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.083344`, avg `-0.01642`, median `-0.02913`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.045966`, avg `0.054329`, median `0.057737`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.022887`, avg `0.00189`, median `0.007933`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.032938`, avg `0.000792`, median `0.010244`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.040049`, avg `0.010355`, median `0.010405`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.053325`, avg `0.011629`, median `0.002641`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.074755`, avg `0.123403`, median `0.125416`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.5375`, primary_mae `0.018358`, avg `0.003206`, median `0.007812`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.027471`, avg `0.001098`, median `0.004099`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.042696`, avg `-0.003306`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.064008`, avg `-0.007112`, median `-0.002679`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.4375`, primary_mae `0.054005`, avg `0.067`, median `0.069096`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.5375`, primary_mae `0.018358`, avg `0.003206`, median `0.007812`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.027471`, avg `0.001098`, median `0.004099`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.042696`, avg `-0.003306`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.064008`, avg `-0.007112`, median `-0.002679`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.4375`, primary_mae `0.054005`, avg `0.067`, median `0.069096`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.5833`, primary_mae `0.016047`, avg `0.003982`, median `0.007812`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.5333`, primary_mae `0.025137`, avg `0.001842`, median `0.001561`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.55`, primary_mae `0.044527`, avg `-0.006531`, median `-0.010602`
- 20d: sample `60`, primary_hit `0.5333`, primary_closer `0.5333`, primary_mae `0.069785`, avg `-0.01032`, median `-0.014269`
- 60d: sample `60`, primary_hit `0.4833`, primary_closer `0.4667`, primary_mae `0.050167`, avg `0.053421`, median `0.059547`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.025291`, avg `0.000881`, median `0.007933`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.034474`, avg `-0.001134`, median `0.010244`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.037201`, avg `0.006366`, median `0.009633`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.25`, primary_mae `0.046679`, avg `0.002511`, median `0.001267`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.35`, primary_mae `0.065519`, avg `0.107739`, median `0.104383`

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
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.025291`, avg `0.000881`, median `0.007933`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.034474`, avg `-0.001134`, median `0.010244`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.037201`, avg `0.006366`, median `0.009633`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.25`, primary_mae `0.046679`, avg `0.002511`, median `0.001267`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.35`, primary_mae `0.065519`, avg `0.107739`, median `0.104383`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.5375`, primary_mae `0.018358`, avg `0.003206`, median `0.007812`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.027471`, avg `0.001098`, median `0.004099`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.042696`, avg `-0.003306`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.064008`, avg `-0.007112`, median `-0.002679`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.4375`, primary_mae `0.054005`, avg `0.067`, median `0.069096`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
