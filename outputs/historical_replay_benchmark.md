# Historical Replay Benchmark

Generated at: `2026-07-06T15:57:44.945739+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.013657`
- secondary_mean_absolute_error: `0.012446`
- primary_error_advantage: `-0.001211`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.017544`
- secondary_mean_absolute_error: `0.015762`
- primary_error_advantage: `-0.001782`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.024629`
- secondary_mean_absolute_error: `0.018919`
- primary_error_advantage: `-0.00571`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.041538`
- secondary_mean_absolute_error: `0.047698`
- primary_error_advantage: `0.00616`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.675`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.065027`
- secondary_mean_absolute_error: `0.057792`
- primary_error_advantage: `-0.007235`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.012756`, as_primary `0`, as_primary_hit `None`, avg `-0.001467`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.015501`, as_primary `0`, as_primary_hit `None`, avg `-0.00206`, median `-0.000454`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.018804`, as_primary `0`, as_primary_hit `None`, avg `0.001058`, median `-0.000307`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.027005`, as_primary `0`, as_primary_hit `None`, avg `0.004932`, median `0.01072`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.053448`, as_primary `0`, as_primary_hit `None`, avg `0.001553`, median `-0.007739`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.013657`, as_primary `80`, as_primary_hit `0.5`, avg `-0.001467`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.017544`, as_primary `80`, as_primary_hit `0.5`, avg `-0.00206`, median `-0.000454`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.024629`, as_primary `80`, as_primary_hit `0.4875`, avg `0.001058`, median `-0.000307`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.041538`, as_primary `80`, as_primary_hit `0.675`, avg `0.004932`, median `0.01072`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.065027`, as_primary `80`, as_primary_hit `0.4625`, avg `0.001553`, median `-0.007739`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.013027`, as_primary `0`, as_primary_hit `None`, avg `-0.001467`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.016499`, as_primary `0`, as_primary_hit `None`, avg `-0.00206`, median `-0.000454`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.01897`, as_primary `0`, as_primary_hit `None`, avg `0.001058`, median `-0.000307`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.052367`, as_primary `0`, as_primary_hit `None`, avg `0.004932`, median `0.01072`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.065046`, as_primary `0`, as_primary_hit `None`, avg `0.001553`, median `-0.007739`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.012153`, as_primary `0`, as_primary_hit `None`, avg `-0.001467`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.015178`, as_primary `0`, as_primary_hit `None`, avg `-0.00206`, median `-0.000454`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.017535`, as_primary `0`, as_primary_hit `None`, avg `0.001058`, median `-0.000307`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.026364`, as_primary `0`, as_primary_hit `None`, avg `0.004932`, median `0.01072`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.052091`, as_primary `0`, as_primary_hit `None`, avg `0.001553`, median `-0.007739`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.011254`, avg `0.000532`, median `0.001072`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.014175`, avg `0.000686`, median `0.003111`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.021759`, avg `0.005593`, median `0.003193`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.6`, primary_mae `0.04101`, avg `0.003691`, median `0.010232`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.5`, primary_mae `0.055908`, avg `-0.004385`, median `-0.018714`

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.014089`, avg `-0.009582`, median `-0.010064`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.015749`, avg `-0.008741`, median `-0.006575`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.014863`, avg `-0.005755`, median `-0.008733`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.043822`, avg `0.016416`, median `0.020913`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.079438`, avg `0.027865`, median `0.020962`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.018032`, avg `0.002649`, median `0.003542`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.026076`, avg `-0.000869`, median `-0.004072`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.040136`, avg `-0.001198`, median `-0.002915`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.85`, primary_mae `0.040311`, avg `-0.004071`, median `0.007521`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.068852`, avg `-0.012884`, median `-0.011052`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.011254`, avg `0.000532`, median `0.001072`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.014175`, avg `0.000686`, median `0.003111`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.021759`, avg `0.005593`, median `0.003193`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.6`, primary_mae `0.04101`, avg `0.003691`, median `0.010232`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.5`, primary_mae `0.055908`, avg `-0.004385`, median `-0.018714`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.01606`, avg `-0.003467`, median `-0.004257`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.020912`, avg `-0.004805`, median `-0.006575`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.0275`, avg `-0.003476`, median `-0.008051`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.55`, primary_mae `0.042066`, avg `0.006172`, median `0.012119`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.074145`, avg `0.00749`, median `0.00071`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.011254, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.014175, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.021759, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.04101, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.055908, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012153, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013657, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.011254, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015178, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017544, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.014175, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017535, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024629, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.021759, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026364, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052367, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.04101, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052091, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065046, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.055908, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.010709`, avg `-0.013768`, median `-0.010064`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.014331`, avg `-0.011794`, median `-0.013366`
- 10d: sample `8`, primary_hit `0.0`, primary_closer `0.125`, primary_mae `0.01266`, avg `-0.01387`, median `-0.012789`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.045309`, avg `0.016823`, median `0.024617`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.089014`, avg `0.026683`, median `0.029112`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.012073`, avg `-0.010552`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.014054`, avg `-0.009997`, median `-0.006575`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.013723`, avg `-0.009892`, median `-0.012789`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.04461`, avg `0.014916`, median `0.020913`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.08234`, avg `0.024056`, median `0.020962`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.015184`, avg `0.001913`, median `0.003542`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.025256`, avg `-0.000529`, median `-0.004072`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.040086`, avg `-0.002581`, median `-0.002915`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.8125`, primary_mae `0.044784`, avg `-0.008432`, median `0.007521`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.075809`, avg `-0.02226`, median `-0.014079`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.013657`, avg `-0.001467`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.017544`, avg `-0.00206`, median `-0.000454`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.3875`, primary_mae `0.024629`, avg `0.001058`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.575`, primary_mae `0.041538`, avg `0.004932`, median `0.01072`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.065027`, avg `0.001553`, median `-0.007739`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.013657`, avg `-0.001467`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.017544`, avg `-0.00206`, median `-0.000454`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.3875`, primary_mae `0.024629`, avg `0.001058`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.575`, primary_mae `0.041538`, avg `0.004932`, median `0.01072`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.065027`, avg `0.001553`, median `-0.007739`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.013657`, avg `-0.001467`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.017544`, avg `-0.00206`, median `-0.000454`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.3875`, primary_mae `0.024629`, avg `0.001058`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.575`, primary_mae `0.041538`, avg `0.004932`, median `0.01072`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.065027`, avg `0.001553`, median `-0.007739`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.013657`, avg `-0.001467`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.017544`, avg `-0.00206`, median `-0.000454`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.3875`, primary_mae `0.024629`, avg `0.001058`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.575`, primary_mae `0.041538`, avg `0.004932`, median `0.01072`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.065027`, avg `0.001553`, median `-0.007739`

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
