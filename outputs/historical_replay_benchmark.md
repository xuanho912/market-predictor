# Historical Replay Benchmark

Generated at: `2026-08-02T13:57:58.570042+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `PROMISING`
Overfit warning: `{'level': 'medium', 'reasons': ['high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_mixed_or_not_better_keep_confidence_capped`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.019398`
- secondary_mean_absolute_error: `0.019546`
- primary_error_advantage: `0.000148`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.025393`
- secondary_mean_absolute_error: `0.025981`
- primary_error_advantage: `0.000588`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.030382`
- secondary_mean_absolute_error: `0.032802`
- primary_error_advantage: `0.00242`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.062446`
- secondary_mean_absolute_error: `0.063876`
- primary_error_advantage: `0.00143`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5125`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.093993`
- secondary_mean_absolute_error: `0.095113`
- primary_error_advantage: `0.00112`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5375`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.016804`, as_primary `0`, as_primary_hit `None`, avg `-0.000453`, median `0.000402`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.020308`, as_primary `0`, as_primary_hit `None`, avg `-0.002527`, median `0.000725`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.022665`, as_primary `0`, as_primary_hit `None`, avg `-0.00267`, median `-0.009041`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.041362`, as_primary `0`, as_primary_hit `None`, avg `0.002884`, median `0.005712`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.071954`, as_primary `0`, as_primary_hit `None`, avg `-0.0018`, median `0.003669`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.020103`, as_primary `60`, as_primary_hit `0.5333`, avg `-0.000453`, median `0.000402`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.027389`, as_primary `60`, as_primary_hit `0.5333`, avg `-0.002527`, median `0.000725`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.033401`, as_primary `60`, as_primary_hit `0.35`, avg `-0.00267`, median `-0.009041`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.065609`, as_primary `60`, as_primary_hit `0.5667`, avg `0.002884`, median `0.005712`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.091309`, as_primary `60`, as_primary_hit `0.5667`, avg `-0.0018`, median `0.003669`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.019732`, as_primary `20`, as_primary_hit `0.45`, avg `-0.000453`, median `0.000402`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.025198`, as_primary `20`, as_primary_hit `0.5`, avg `-0.002527`, median `0.000725`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.031099`, as_primary `20`, as_primary_hit `0.4`, avg `-0.00267`, median `-0.009041`
- 20d: sample `80`, direction_hit `0.45`, path_mae `0.068393`, as_primary `20`, as_primary_hit `0.5`, avg `0.002884`, median `0.005712`
- 60d: sample `80`, direction_hit `0.4875`, path_mae `0.106743`, as_primary `20`, as_primary_hit `0.35`, avg `-0.0018`, median `0.003669`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.016585`, as_primary `0`, as_primary_hit `None`, avg `-0.000453`, median `0.000402`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.019524`, as_primary `0`, as_primary_hit `None`, avg `-0.002527`, median `0.000725`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.022208`, as_primary `0`, as_primary_hit `None`, avg `-0.00267`, median `-0.009041`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.040038`, as_primary `0`, as_primary_hit `None`, avg `0.002884`, median `0.005712`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.072804`, as_primary `0`, as_primary_hit `None`, avg `-0.0018`, median `0.003669`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.5167`, primary_mae `0.018933`, avg `-0.000726`, median `0.000684`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.4667`, primary_mae `0.023263`, avg `-0.002453`, median `0.000725`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.4167`, primary_mae `0.023397`, avg `2.6e-05`, median `-0.007436`
- 20d: sample `60`, primary_hit `0.5667`, primary_closer `0.5333`, primary_mae `0.052794`, avg `0.010724`, median `0.007983`
- 60d: sample `60`, primary_hit `0.5667`, primary_closer `0.5667`, primary_mae `0.075902`, avg `0.018554`, median `0.025527`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.02079`, avg `0.000366`, median `-0.000629`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.031783`, avg `-0.002746`, median `-0.004155`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.051337`, avg `-0.010756`, median `-0.015175`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.091403`, avg `-0.020638`, median `0.002187`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.148266`, avg `-0.062863`, median `-0.045068`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.017905`, avg `-0.004086`, median `-0.000971`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.018802`, avg `-0.007051`, median `0.000552`
- 10d: sample `40`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.015802`, avg `-0.012814`, median `-0.013575`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.050129`, avg `-0.007537`, median `-0.005975`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.070534`, avg `0.001769`, median `-0.004291`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.02079`, avg `0.000366`, median `-0.000629`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.031783`, avg `-0.002746`, median `-0.004155`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.051337`, avg `-0.010756`, median `-0.015175`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.091403`, avg `-0.020638`, median `0.002187`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.148266`, avg `-0.062863`, median `-0.045068`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.02099`, avg `0.005996`, median `0.008962`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.032184`, avg `0.006743`, median `0.009055`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.038586`, avg `0.025705`, median `0.027966`
- 20d: sample `20`, primary_hit `0.9`, primary_closer `0.65`, primary_mae `0.058124`, avg `0.047246`, median `0.049277`
- 60d: sample `20`, primary_hit `0.75`, primary_closer `0.7`, primary_mae `0.086639`, avg `0.052124`, median `0.072959`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.017905, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018802, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.015802, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.050129, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.070534, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016585, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020103, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.017905, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019524, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027389, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018802, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022208, 'direction_hit_rate': 0.3625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033401, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.015802, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040038, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.068393, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.050129, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071954, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.106743, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.070534, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.022101`, avg `-0.020886`, median `-0.02628`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.028185`, avg `-0.026523`, median `-0.023845`
- 10d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.02066`, avg `-0.014898`, median `-0.016542`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.087546`, avg `-0.02428`, median `-0.028005`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.133199`, avg `-0.027753`, median `-0.042188`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.01989`, avg `-0.007704`, median `-0.004092`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.019033`, avg `-0.014416`, median `-0.002934`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.017916`, avg `-0.013294`, median `-0.014477`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.067321`, avg `-0.002426`, median `0.00081`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.09884`, avg `0.011429`, median `0.024759`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.6875`, primary_mae `0.019017`, avg `-0.002607`, median `-0.003306`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.030455`, avg `-0.006138`, median `-0.004155`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.050846`, avg `-0.010511`, median `-0.013139`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.089147`, avg `-0.022523`, median `0.007755`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.146423`, avg `-0.065471`, median `-0.057799`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5375`, primary_mae `0.019398`, avg `-0.000453`, median `0.000402`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4875`, primary_mae `0.025393`, avg `-0.002527`, median `0.000725`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.4625`, primary_mae `0.030382`, avg `-0.00267`, median `-0.009041`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.062446`, avg `0.002884`, median `0.005712`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5375`, primary_mae `0.093993`, avg `-0.0018`, median `0.003669`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5375`, primary_mae `0.019398`, avg `-0.000453`, median `0.000402`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4875`, primary_mae `0.025393`, avg `-0.002527`, median `0.000725`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.4625`, primary_mae `0.030382`, avg `-0.00267`, median `-0.009041`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.062446`, avg `0.002884`, median `0.005712`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5375`, primary_mae `0.093993`, avg `-0.0018`, median `0.003669`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.017905`, avg `-0.004086`, median `-0.000971`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.018802`, avg `-0.007051`, median `0.000552`
- 10d: sample `40`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.015802`, avg `-0.012814`, median `-0.013575`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.050129`, avg `-0.007537`, median `-0.005975`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.070534`, avg `0.001769`, median `-0.004291`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.02089`, avg `0.003181`, median `0.00559`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.55`, primary_mae `0.031984`, avg `0.001998`, median `0.001845`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.55`, primary_mae `0.044961`, avg `0.007475`, median `0.010988`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.074763`, avg `0.013304`, median `0.022472`
- 60d: sample `40`, primary_hit `0.7`, primary_closer `0.575`, primary_mae `0.117453`, avg `-0.005369`, median `0.035626`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5375`, primary_mae `0.019398`, avg `-0.000453`, median `0.000402`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4875`, primary_mae `0.025393`, avg `-0.002527`, median `0.000725`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.4625`, primary_mae `0.030382`, avg `-0.00267`, median `-0.009041`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.062446`, avg `0.002884`, median `0.005712`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5375`, primary_mae `0.093993`, avg `-0.0018`, median `0.003669`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5667`, primary_closer `0.5833`, primary_mae `0.020286`, avg `0.000691`, median `0.00177`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.028019`, avg `-0.002265`, median `-0.000357`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.036237`, avg `0.001444`, median `-0.006487`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.4667`, primary_mae `0.071669`, avg `0.009353`, median `0.016991`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.5`, primary_mae `0.110948`, avg `0.000755`, median `0.032531`

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
