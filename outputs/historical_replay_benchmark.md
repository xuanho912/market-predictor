# Historical Replay Benchmark

Generated at: `2026-08-20T04:22:23.027650+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `40`
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
- sample_size: `40`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.01582`
- secondary_mean_absolute_error: `0.011958`
- primary_error_advantage: `-0.003862`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 5d
- sample_size: `40`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.020129`
- secondary_mean_absolute_error: `0.013215`
- primary_error_advantage: `-0.006914`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 10d
- sample_size: `40`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.024991`
- secondary_mean_absolute_error: `0.022472`
- primary_error_advantage: `-0.002519`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `40`
- primary_hit_rate: `0.725`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.04176`
- secondary_mean_absolute_error: `0.041405`
- primary_error_advantage: `-0.000355`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 60d
- sample_size: `40`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.07207`
- secondary_mean_absolute_error: `0.057816`
- primary_error_advantage: `-0.014254`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `40`
- 3d: sample `40`, direction_hit `0.55`, path_mae `0.012423`, as_primary `0`, as_primary_hit `None`, avg `0.001546`, median `0.001491`
- 5d: sample `40`, direction_hit `0.65`, path_mae `0.015178`, as_primary `0`, as_primary_hit `None`, avg `0.005035`, median `0.004963`
- 10d: sample `40`, direction_hit `0.65`, path_mae `0.020009`, as_primary `0`, as_primary_hit `None`, avg `0.003137`, median `0.010085`
- 20d: sample `40`, direction_hit `0.725`, path_mae `0.028895`, as_primary `0`, as_primary_hit `None`, avg `0.010455`, median `0.012453`
- 60d: sample `40`, direction_hit `0.5`, path_mae `0.058845`, as_primary `0`, as_primary_hit `None`, avg `0.014207`, median `0.000206`

### bounce_path
- sample_size: `40`
- 3d: sample `40`, direction_hit `0.55`, path_mae `0.01582`, as_primary `40`, as_primary_hit `0.55`, avg `0.001546`, median `0.001491`
- 5d: sample `40`, direction_hit `0.65`, path_mae `0.020129`, as_primary `40`, as_primary_hit `0.65`, avg `0.005035`, median `0.004963`
- 10d: sample `40`, direction_hit `0.65`, path_mae `0.024991`, as_primary `40`, as_primary_hit `0.65`, avg `0.003137`, median `0.010085`
- 20d: sample `40`, direction_hit `0.725`, path_mae `0.04176`, as_primary `40`, as_primary_hit `0.725`, avg `0.010455`, median `0.012453`
- 60d: sample `40`, direction_hit `0.5`, path_mae `0.07207`, as_primary `40`, as_primary_hit `0.5`, avg `0.014207`, median `0.000206`

### failed_bounce_path
- sample_size: `40`
- 3d: sample `40`, direction_hit `0.45`, path_mae `0.01283`, as_primary `0`, as_primary_hit `None`, avg `0.001546`, median `0.001491`
- 5d: sample `40`, direction_hit `0.35`, path_mae `0.013934`, as_primary `0`, as_primary_hit `None`, avg `0.005035`, median `0.004963`
- 10d: sample `40`, direction_hit `0.35`, path_mae `0.02736`, as_primary `0`, as_primary_hit `None`, avg `0.003137`, median `0.010085`
- 20d: sample `40`, direction_hit `0.275`, path_mae `0.055`, as_primary `0`, as_primary_hit `None`, avg `0.010455`, median `0.012453`
- 60d: sample `40`, direction_hit `0.5`, path_mae `0.058866`, as_primary `0`, as_primary_hit `None`, avg `0.014207`, median `0.000206`

### analog_average_path
- sample_size: `40`
- 3d: sample `40`, direction_hit `0.55`, path_mae `0.011934`, as_primary `0`, as_primary_hit `None`, avg `0.001546`, median `0.001491`
- 5d: sample `40`, direction_hit `0.65`, path_mae `0.013124`, as_primary `0`, as_primary_hit `None`, avg `0.005035`, median `0.004963`
- 10d: sample `40`, direction_hit `0.65`, path_mae `0.01987`, as_primary `0`, as_primary_hit `None`, avg `0.003137`, median `0.010085`
- 20d: sample `40`, direction_hit `0.725`, path_mae `0.027506`, as_primary `0`, as_primary_hit `None`, avg `0.010455`, median `0.012453`
- 60d: sample `40`, direction_hit `0.5`, path_mae `0.055564`, as_primary `0`, as_primary_hit `None`, avg `0.014207`, median `0.000206`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.01582`, avg `0.001546`, median `0.001491`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.325`, primary_mae `0.020129`, avg `0.005035`, median `0.004963`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.024991`, avg `0.003137`, median `0.010085`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.475`, primary_mae `0.04176`, avg `0.010455`, median `0.012453`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.07207`, avg `0.014207`, median `0.000206`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.009382`, avg `0.001566`, median `0.00084`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.35`, primary_mae `0.013666`, avg `0.005123`, median `0.005529`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.65`, primary_mae `0.017846`, avg `0.000446`, median `0.008571`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.7`, primary_mae `0.032315`, avg `-0.001659`, median `0.007613`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.075442`, avg `-0.00039`, median `-0.017782`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.022258`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.026593`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.032136`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.051205`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068697`, avg `0.028804`, median `0.038342`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.009382, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013666, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.017846, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.032315, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.068697, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 40, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 40, 'path_mean_absolute_error': 0.011934, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 40, 'path_mean_absolute_error': 0.01582, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.009382, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 40, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 40, 'path_mean_absolute_error': 0.013124, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 40, 'path_mean_absolute_error': 0.020129, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013666, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 40, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 40, 'path_mean_absolute_error': 0.01987, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 40, 'path_mean_absolute_error': 0.02736, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.017846, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 40, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 40, 'path_mean_absolute_error': 0.027506, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 40, 'path_mean_absolute_error': 0.055, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.032315, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 40, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 40, 'path_mean_absolute_error': 0.055564, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 40, 'path_mean_absolute_error': 0.07207, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.068697, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `4`
- 3d: sample `4`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.016225`, avg `0.006853`, median `0.005338`
- 5d: sample `4`, primary_hit `1.0`, primary_closer `0.25`, primary_mae `0.01923`, avg `0.010098`, median `0.009586`
- 10d: sample `4`, primary_hit `1.0`, primary_closer `0.75`, primary_mae `0.014003`, avg `0.02093`, median `0.023382`
- 20d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.058855`, avg `0.012375`, median `0.000839`
- 60d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.104018`, avg `-0.00754`, median `-0.035929`

### top_20
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.022094`, avg `0.000984`, median `0.005338`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.022978`, avg `0.00726`, median `0.00778`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.023694`, avg `0.013099`, median `0.01669`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.064696`, avg `0.008112`, median `0.008959`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.076287`, avg `0.020192`, median `0.005143`

### bottom_20
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.022094`, avg `0.000984`, median `0.005338`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.022978`, avg `0.00726`, median `0.00778`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.023694`, avg `0.013099`, median `0.01669`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.064696`, avg `0.008112`, median `0.008959`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.076287`, avg `0.020192`, median `0.005143`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.01582`, avg `0.001546`, median `0.001491`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.325`, primary_mae `0.020129`, avg `0.005035`, median `0.004963`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.024991`, avg `0.003137`, median `0.010085`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.475`, primary_mae `0.04176`, avg `0.010455`, median `0.012453`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.07207`, avg `0.014207`, median `0.000206`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.01582`, avg `0.001546`, median `0.001491`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.325`, primary_mae `0.020129`, avg `0.005035`, median `0.004963`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.024991`, avg `0.003137`, median `0.010085`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.475`, primary_mae `0.04176`, avg `0.010455`, median `0.012453`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.07207`, avg `0.014207`, median `0.000206`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.01582`, avg `0.001546`, median `0.001491`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.325`, primary_mae `0.020129`, avg `0.005035`, median `0.004963`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.024991`, avg `0.003137`, median `0.010085`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.475`, primary_mae `0.04176`, avg `0.010455`, median `0.012453`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.07207`, avg `0.014207`, median `0.000206`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.022258`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.026593`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.032136`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.051205`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068697`, avg `0.028804`, median `0.038342`

### options_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.01582`, avg `0.001546`, median `0.001491`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.325`, primary_mae `0.020129`, avg `0.005035`, median `0.004963`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.024991`, avg `0.003137`, median `0.010085`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.475`, primary_mae `0.04176`, avg `0.010455`, median `0.012453`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.07207`, avg `0.014207`, median `0.000206`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.01582`, avg `0.001546`, median `0.001491`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.325`, primary_mae `0.020129`, avg `0.005035`, median `0.004963`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.024991`, avg `0.003137`, median `0.010085`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.475`, primary_mae `0.04176`, avg `0.010455`, median `0.012453`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.07207`, avg `0.014207`, median `0.000206`

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
