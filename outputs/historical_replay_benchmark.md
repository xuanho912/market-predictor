# Historical Replay Benchmark

Generated at: `2026-07-06T21:54:12.922766+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.015155`
- secondary_mean_absolute_error: `0.012478`
- primary_error_advantage: `-0.002677`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.018482`
- secondary_mean_absolute_error: `0.016924`
- primary_error_advantage: `-0.001558`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.025542`
- secondary_mean_absolute_error: `0.019067`
- primary_error_advantage: `-0.006475`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.039885`
- secondary_mean_absolute_error: `0.037076`
- primary_error_advantage: `-0.002809`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.85`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.063389`
- secondary_mean_absolute_error: `0.054918`
- primary_error_advantage: `-0.008471`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.013595`, as_primary `0`, as_primary_hit `None`, avg `-0.001333`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.016458`, as_primary `0`, as_primary_hit `None`, avg `-0.002401`, median `-0.000454`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.018554`, as_primary `0`, as_primary_hit `None`, avg `0.00129`, median `-0.000307`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.025908`, as_primary `0`, as_primary_hit `None`, avg `0.004595`, median `0.0103`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.051543`, as_primary `0`, as_primary_hit `None`, avg `0.003583`, median `-0.004059`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015155`, as_primary `80`, as_primary_hit `0.5`, avg `-0.001333`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.018482`, as_primary `80`, as_primary_hit `0.5`, avg `-0.002401`, median `-0.000454`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.025542`, as_primary `80`, as_primary_hit `0.4875`, avg `0.00129`, median `-0.000307`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.039885`, as_primary `80`, as_primary_hit `0.6625`, avg `0.004595`, median `0.0103`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.063389`, as_primary `80`, as_primary_hit `0.475`, avg `0.003583`, median `-0.004059`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.013204`, as_primary `0`, as_primary_hit `None`, avg `-0.001333`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.017725`, as_primary `0`, as_primary_hit `None`, avg `-0.002401`, median `-0.000454`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.020291`, as_primary `0`, as_primary_hit `None`, avg `0.00129`, median `-0.000307`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.049673`, as_primary `0`, as_primary_hit `None`, avg `0.004595`, median `0.0103`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.06483`, as_primary `0`, as_primary_hit `None`, avg `0.003583`, median `-0.004059`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.01235`, as_primary `0`, as_primary_hit `None`, avg `-0.001333`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.016106`, as_primary `0`, as_primary_hit `None`, avg `-0.002401`, median `-0.000454`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.017818`, as_primary `0`, as_primary_hit `None`, avg `0.00129`, median `-0.000307`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.025285`, as_primary `0`, as_primary_hit `None`, avg `0.004595`, median `0.0103`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.050754`, as_primary `0`, as_primary_hit `None`, avg `0.003583`, median `-0.004059`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.010928`, avg `-0.001431`, median `-0.001467`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.01147`, avg `0.000844`, median `0.00337`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.010417`, avg `0.005192`, median `0.004016`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.022187`, avg `0.011759`, median `0.01293`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.050333`, avg `-0.020667`, median `-0.024343`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015662`, avg `-0.003107`, median `-0.00052`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.01796`, avg `-0.004559`, median `-0.002264`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.3`, primary_mae `0.024676`, avg `0.001714`, median `-0.005954`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.25`, primary_mae `0.047883`, avg `0.005984`, median `0.007177`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.066358`, avg `0.024769`, median `0.045588`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.018369`, avg `0.002312`, median `0.003542`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.026538`, avg `-0.001331`, median `-0.004072`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.042399`, avg `-0.003461`, median `-0.002915`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.85`, primary_mae `0.041588`, avg `-0.005348`, median `0.005514`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.070508`, avg `-0.01454`, median `-0.011052`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.325`, primary_mae `0.013982`, avg `0.001255`, median `0.001072`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.01609`, avg `0.000465`, median `0.003455`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.023147`, avg `0.007453`, median `0.003193`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.275`, primary_mae `0.038805`, avg `0.005577`, median `0.011258`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.050974`, avg `0.00458`, median `0.006274`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.016329`, avg `-0.003922`, median `-0.004257`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.020874`, avg `-0.005267`, median `-0.006575`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.027936`, avg `-0.004874`, median `-0.008051`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.55`, primary_mae `0.040965`, avg `0.003613`, median `0.007521`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.075804`, avg `0.002586`, median `-0.004059`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.013982, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.01609, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.023147, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.038805, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.050974, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01235, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015155, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.013982, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016106, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018482, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.01609, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017818, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025542, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.023147, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025285, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049673, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.038805, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050754, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06483, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.050974, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.014586`, avg `-0.010839`, median `-0.009739`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.014594`, avg `-0.008852`, median `-0.008736`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.015968`, avg `-0.008261`, median `-0.012789`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.044385`, avg `0.004923`, median `0.016513`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.098299`, avg `-0.005336`, median `-0.004019`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.01304`, avg `-0.010552`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.013959`, avg `-0.009997`, median `-0.006575`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.012359`, avg `-0.009892`, median `-0.012789`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.038902`, avg `0.014916`, median `0.020913`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.079044`, avg `0.024056`, median `0.020962`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.015603`, avg `0.004231`, median `0.006764`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.021958`, avg `0.004214`, median `0.007358`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.036731`, avg `0.00297`, median `0.004339`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.875`, primary_mae `0.033364`, avg `0.00329`, median `0.009478`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.06933`, avg `-0.010192`, median `-0.011052`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.015155`, avg `-0.001333`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.018482`, avg `-0.002401`, median `-0.000454`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.025542`, avg `0.00129`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.4125`, primary_mae `0.039885`, avg `0.004595`, median `0.0103`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.063389`, avg `0.003583`, median `-0.004059`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.015155`, avg `-0.001333`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.018482`, avg `-0.002401`, median `-0.000454`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.025542`, avg `0.00129`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.4125`, primary_mae `0.039885`, avg `0.004595`, median `0.0103`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.063389`, avg `0.003583`, median `-0.004059`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.015155`, avg `-0.001333`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.018482`, avg `-0.002401`, median `-0.000454`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.025542`, avg `0.00129`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.4125`, primary_mae `0.039885`, avg `0.004595`, median `0.0103`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.063389`, avg `0.003583`, median `-0.004059`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.015155`, avg `-0.001333`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.018482`, avg `-0.002401`, median `-0.000454`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.025542`, avg `0.00129`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.4125`, primary_mae `0.039885`, avg `0.004595`, median `0.0103`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.063389`, avg `0.003583`, median `-0.004059`

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
