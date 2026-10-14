# Historical Replay Benchmark

Generated at: `2026-10-14T06:13:56.234549+00:00`
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
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.01828`
- secondary_mean_absolute_error: `0.01564`
- primary_error_advantage: `-0.00264`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.021334`
- secondary_mean_absolute_error: `0.019655`
- primary_error_advantage: `-0.001679`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.026082`
- secondary_mean_absolute_error: `0.023772`
- primary_error_advantage: `-0.00231`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.060675`
- secondary_mean_absolute_error: `0.042386`
- primary_error_advantage: `-0.018289`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2625`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.475`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.077766`
- secondary_mean_absolute_error: `0.060293`
- primary_error_advantage: `-0.017473`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.016427`, as_primary `0`, as_primary_hit `None`, avg `-0.006241`, median `-0.005438`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.018722`, as_primary `0`, as_primary_hit `None`, avg `-0.01033`, median `-0.015005`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.024075`, as_primary `0`, as_primary_hit `None`, avg `-0.010846`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.034938`, as_primary `0`, as_primary_hit `None`, avg `0.013442`, median `0.014286`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.054034`, as_primary `0`, as_primary_hit `None`, avg `0.036238`, median `0.052147`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.016318`, as_primary `0`, as_primary_hit `None`, avg `-0.006241`, median `-0.005438`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.019548`, as_primary `0`, as_primary_hit `None`, avg `-0.01033`, median `-0.015005`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.027871`, as_primary `0`, as_primary_hit `None`, avg `-0.010846`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.050828`, as_primary `0`, as_primary_hit `None`, avg `0.013442`, median `0.014286`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.065256`, as_primary `0`, as_primary_hit `None`, avg `0.036238`, median `0.052147`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.01828`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.006241`, median `-0.005438`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.021334`, as_primary `80`, as_primary_hit `0.4`, avg `-0.01033`, median `-0.015005`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.026082`, as_primary `80`, as_primary_hit `0.375`, avg `-0.010846`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.4`, path_mae `0.060675`, as_primary `80`, as_primary_hit `0.6`, avg `0.013442`, median `0.014286`
- 60d: sample `80`, direction_hit `0.2625`, path_mae `0.077766`, as_primary `80`, as_primary_hit `0.7375`, avg `0.036238`, median `0.052147`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.015599`, as_primary `0`, as_primary_hit `None`, avg `-0.006241`, median `-0.005438`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.018738`, as_primary `0`, as_primary_hit `None`, avg `-0.01033`, median `-0.015005`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.022805`, as_primary `0`, as_primary_hit `None`, avg `-0.010846`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.034776`, as_primary `0`, as_primary_hit `None`, avg `0.013442`, median `0.014286`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.056058`, as_primary `0`, as_primary_hit `None`, avg `0.036238`, median `0.052147`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.01828`, avg `-0.006241`, median `-0.005438`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4875`, primary_mae `0.021334`, avg `-0.01033`, median `-0.015005`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.026082`, avg `-0.010846`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060675`, avg `0.013442`, median `0.014286`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.3625`, primary_mae `0.077766`, avg `0.036238`, median `0.052147`

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
- 3d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.020003`, avg `-0.011667`, median `-0.010671`
- 5d: sample `20`, primary_hit `0.8`, primary_closer `0.45`, primary_mae `0.018887`, avg `-0.016754`, median `-0.021882`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.035644`, avg `-0.014864`, median `-0.032528`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.087368`, avg `0.030987`, median `0.044315`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.2`, primary_mae `0.083584`, avg `0.080919`, median `0.092349`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.019406`, avg `-0.007474`, median `-0.005583`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.023641`, avg `-0.010743`, median `-0.016241`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.027082`, avg `-0.012662`, median `-0.010944`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.063233`, avg `0.00677`, median `0.009546`
- 60d: sample `40`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.093106`, avg `0.017781`, median `0.048423`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.014304`, avg `0.00165`, median `0.007125`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.019169`, avg `-0.00308`, median `0.00102`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.014518`, avg `-0.003197`, median `-0.001758`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.028867`, avg `0.00924`, median `0.012218`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.041267`, avg `0.02847`, median `0.029695`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.014304, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.018887, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014518, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.028867, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.041267, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015599, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01828, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.014304, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018722, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021334, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.018887, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022805, 'direction_hit_rate': 0.375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027871, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014518, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034776, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060675, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.028867, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.475, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054034, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.077766, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.041267, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.019372`, avg `-0.016625`, median `-0.030767`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.022505`, avg `-0.014933`, median `-0.020293`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.020689`, avg `-0.010376`, median `-0.014252`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.082794`, avg `0.007481`, median `0.023936`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.146577`, avg `0.018653`, median `0.052632`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.020006`, avg `-0.008905`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.021979`, avg `-0.013151`, median `-0.019358`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.025346`, avg `-0.012472`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.076633`, avg `0.003999`, median `0.019252`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.137228`, avg `0.00823`, median `0.048285`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.9375`, primary_closer `0.25`, primary_mae `0.018146`, avg `-0.010913`, median `-0.010671`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.017306`, avg `-0.0166`, median `-0.021882`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.035326`, avg `-0.015558`, median `-0.035238`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.082265`, avg `0.025863`, median `0.019624`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.1875`, primary_mae `0.076493`, avg `0.079889`, median `0.085768`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.01828`, avg `-0.006241`, median `-0.005438`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4875`, primary_mae `0.021334`, avg `-0.01033`, median `-0.015005`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.026082`, avg `-0.010846`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060675`, avg `0.013442`, median `0.014286`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.3625`, primary_mae `0.077766`, avg `0.036238`, median `0.052147`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.01828`, avg `-0.006241`, median `-0.005438`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4875`, primary_mae `0.021334`, avg `-0.01033`, median `-0.015005`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.026082`, avg `-0.010846`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060675`, avg `0.013442`, median `0.014286`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.3625`, primary_mae `0.077766`, avg `0.036238`, median `0.052147`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.019406`, avg `-0.007474`, median `-0.005583`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.023641`, avg `-0.010743`, median `-0.016241`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.027082`, avg `-0.012662`, median `-0.010944`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.063233`, avg `0.00677`, median `0.009546`
- 60d: sample `40`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.093106`, avg `0.017781`, median `0.048423`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.017153`, avg `-0.005008`, median `-0.005438`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.019028`, avg `-0.009917`, median `-0.013338`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.525`, primary_mae `0.025081`, avg `-0.00903`, median `-0.014057`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.275`, primary_mae `0.058118`, avg `0.020114`, median `0.014434`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.062426`, avg `0.054695`, median `0.056639`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.01828`, avg `-0.006241`, median `-0.005438`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4875`, primary_mae `0.021334`, avg `-0.01033`, median `-0.015005`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.026082`, avg `-0.010846`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060675`, avg `0.013442`, median `0.014286`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.3625`, primary_mae `0.077766`, avg `0.036238`, median `0.052147`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4333`, primary_mae `0.017505`, avg `-0.006074`, median `-0.005438`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.4667`, primary_mae `0.020233`, avg `-0.010738`, median `-0.014021`
- 10d: sample `60`, primary_hit `0.6167`, primary_closer `0.4833`, primary_mae `0.025597`, avg `-0.010732`, median `-0.013709`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.35`, primary_mae `0.054866`, avg `0.01531`, median `0.012218`
- 60d: sample `60`, primary_hit `0.2333`, primary_closer `0.3667`, primary_mae `0.056237`, avg `0.044295`, median `0.051945`

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
