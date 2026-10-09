# Historical Replay Benchmark

Generated at: `2026-10-09T18:24:20.412233+00:00`
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
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.3375`
- primary_vs_secondary_accuracy_spread: `0.325`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.01936`
- secondary_mean_absolute_error: `0.017158`
- primary_error_advantage: `-0.002202`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.021874`
- secondary_mean_absolute_error: `0.020051`
- primary_error_advantage: `-0.001823`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.02811`
- secondary_mean_absolute_error: `0.025011`
- primary_error_advantage: `-0.003099`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.062401`
- secondary_mean_absolute_error: `0.043313`
- primary_error_advantage: `-0.019088`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2125`
- secondary_hit_rate: `0.7875`
- primary_vs_secondary_accuracy_spread: `-0.575`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.075413`
- secondary_mean_absolute_error: `0.055634`
- primary_error_advantage: `-0.019779`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3333`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3375`, path_mae `0.016095`, as_primary `0`, as_primary_hit `None`, avg `-0.007702`, median `-0.005896`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.017236`, as_primary `0`, as_primary_hit `None`, avg `-0.012053`, median `-0.013341`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.023219`, as_primary `0`, as_primary_hit `None`, avg `-0.009048`, median `-0.006976`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.036577`, as_primary `0`, as_primary_hit `None`, avg `0.014208`, median `0.016024`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.047091`, as_primary `0`, as_primary_hit `None`, avg `0.039494`, median `0.04627`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3375`, path_mae `0.01758`, as_primary `0`, as_primary_hit `None`, avg `-0.007702`, median `-0.005896`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.019975`, as_primary `0`, as_primary_hit `None`, avg `-0.012053`, median `-0.013341`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.028882`, as_primary `0`, as_primary_hit `None`, avg `-0.009048`, median `-0.006976`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.054184`, as_primary `0`, as_primary_hit `None`, avg `0.014208`, median `0.016024`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.059479`, as_primary `0`, as_primary_hit `None`, avg `0.039494`, median `0.04627`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6625`, path_mae `0.01936`, as_primary `80`, as_primary_hit `0.3375`, avg `-0.007702`, median `-0.005896`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.021874`, as_primary `80`, as_primary_hit `0.4`, avg `-0.012053`, median `-0.013341`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.02811`, as_primary `80`, as_primary_hit `0.4`, avg `-0.009048`, median `-0.006976`
- 20d: sample `80`, direction_hit `0.4`, path_mae `0.062401`, as_primary `80`, as_primary_hit `0.6`, avg `0.014208`, median `0.016024`
- 60d: sample `80`, direction_hit `0.2125`, path_mae `0.075413`, as_primary `80`, as_primary_hit `0.7875`, avg `0.039494`, median `0.04627`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3375`, path_mae `0.015207`, as_primary `0`, as_primary_hit `None`, avg `-0.007702`, median `-0.005896`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.016613`, as_primary `0`, as_primary_hit `None`, avg `-0.012053`, median `-0.013341`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.022734`, as_primary `0`, as_primary_hit `None`, avg `-0.009048`, median `-0.006976`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.036202`, as_primary `0`, as_primary_hit `None`, avg `0.014208`, median `0.016024`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.048682`, as_primary `0`, as_primary_hit `None`, avg `0.039494`, median `0.04627`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.4375`, primary_mae `0.01936`, avg `-0.007702`, median `-0.005896`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5125`, primary_mae `0.021874`, avg `-0.012053`, median `-0.013341`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.02811`, avg `-0.009048`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.062401`, avg `0.014208`, median `0.016024`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.325`, primary_mae `0.075413`, avg `0.039494`, median `0.04627`

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
- 3d: sample `40`, primary_hit `0.725`, primary_closer `0.425`, primary_mae `0.02191`, avg `-0.009904`, median `-0.00934`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.425`, primary_mae `0.024965`, avg `-0.013668`, median `-0.017704`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.034883`, avg `-0.010669`, median `-0.008598`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.070265`, avg `0.017918`, median `0.017343`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.4`, primary_mae `0.06726`, avg `0.053022`, median `0.059055`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.01889`, avg `-0.014318`, median `-0.015861`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.027079`, avg `-0.021377`, median `-0.02258`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.027934`, avg `-0.016472`, median `-0.014807`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.077033`, avg `0.008013`, median `0.019252`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.121503`, avg `0.031662`, median `0.048285`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.014728`, avg `0.003318`, median `0.003`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.7`, primary_mae `0.010486`, avg `0.000498`, median `0.001901`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.014738`, avg `0.001619`, median `0.003334`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.03204`, avg `0.012984`, median `0.01444`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.04563`, avg `0.02027`, median `0.029695`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014728, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.010486, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014738, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.03204, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.04563, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.3375, 'primary_vs_secondary_accuracy_spread': 0.325, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015207, 'direction_hit_rate': 0.3375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01936, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014728, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016613, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021874, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.010486, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022734, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028882, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014738, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036202, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062401, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.03204, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2125, 'secondary_hit_rate': 0.7875, 'primary_vs_secondary_accuracy_spread': -0.575, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.047091, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075413, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.04563, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.01786`, avg `-0.016807`, median `-0.030767`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.031311`, avg `-0.01718`, median `-0.020293`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.025217`, avg `-0.012488`, median `-0.014252`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.089956`, avg `0.014597`, median `0.027639`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.143914`, avg `0.053341`, median `0.065914`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.019595`, avg `-0.01298`, median `-0.015861`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.029304`, avg `-0.019849`, median `-0.02258`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.028353`, avg `-0.017728`, median `-0.012632`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.079687`, avg `0.008629`, median `0.023936`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.125255`, avg `0.031385`, median `0.054785`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.125`, primary_mae `0.02622`, avg `-0.007314`, median `-0.010058`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.021159`, avg `-0.016326`, median `-0.021882`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.039456`, avg `-0.012589`, median `-0.029899`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.093015`, avg `0.031454`, median `0.042225`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.1875`, primary_mae `0.097691`, avg `0.084365`, median `0.092349`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.4375`, primary_mae `0.01936`, avg `-0.007702`, median `-0.005896`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5125`, primary_mae `0.021874`, avg `-0.012053`, median `-0.013341`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.02811`, avg `-0.009048`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.062401`, avg `0.014208`, median `0.016024`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.325`, primary_mae `0.075413`, avg `0.039494`, median `0.04627`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.4375`, primary_mae `0.01936`, avg `-0.007702`, median `-0.005896`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5125`, primary_mae `0.021874`, avg `-0.012053`, median `-0.013341`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.02811`, avg `-0.009048`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.062401`, avg `0.014208`, median `0.016024`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.325`, primary_mae `0.075413`, avg `0.039494`, median `0.04627`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.01889`, avg `-0.014318`, median `-0.015861`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.027079`, avg `-0.021377`, median `-0.02258`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.027934`, avg `-0.016472`, median `-0.014807`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.077033`, avg `0.008013`, median `0.019252`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.121503`, avg `0.031662`, median `0.048285`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.325`, primary_mae `0.020329`, avg `-0.005121`, median `-0.003848`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.017271`, avg `-0.008875`, median `-0.008187`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.028701`, avg `-0.005328`, median `-0.005578`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.059266`, avg `0.018647`, median `0.01444`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.25`, primary_mae `0.06796`, avg `0.045811`, median `0.043421`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.4375`, primary_mae `0.01936`, avg `-0.007702`, median `-0.005896`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5125`, primary_mae `0.021874`, avg `-0.012053`, median `-0.013341`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.02811`, avg `-0.009048`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.062401`, avg `0.014208`, median `0.016024`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.325`, primary_mae `0.075413`, avg `0.039494`, median `0.04627`

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
