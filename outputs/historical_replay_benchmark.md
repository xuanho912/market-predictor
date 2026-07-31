# Historical Replay Benchmark

Generated at: `2026-07-31T00:14:45.430998+00:00`
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
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.017081`
- secondary_mean_absolute_error: `0.017009`
- primary_error_advantage: `-7.2e-05`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5125`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.024503`
- secondary_mean_absolute_error: `0.021786`
- primary_error_advantage: `-0.002717`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.525`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.037381`
- secondary_mean_absolute_error: `0.02836`
- primary_error_advantage: `-0.009021`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.068177`
- secondary_mean_absolute_error: `0.053813`
- primary_error_advantage: `-0.014364`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.105393`
- secondary_mean_absolute_error: `0.083251`
- primary_error_advantage: `-0.022142`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3875`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014653`, as_primary `0`, as_primary_hit `None`, avg `0.002084`, median `0.001378`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.018626`, as_primary `0`, as_primary_hit `None`, avg `0.002137`, median `0.001659`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.02475`, as_primary `0`, as_primary_hit `None`, avg `0.001763`, median `-0.002063`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.037249`, as_primary `0`, as_primary_hit `None`, avg `0.011983`, median `0.016341`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.069981`, as_primary `0`, as_primary_hit `None`, avg `0.014024`, median `0.026861`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.01803`, as_primary `20`, as_primary_hit `0.55`, avg `0.002084`, median `0.001378`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.025233`, as_primary `20`, as_primary_hit `0.5`, avg `0.002137`, median `0.001659`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.034974`, as_primary `20`, as_primary_hit `0.35`, avg `0.001763`, median `-0.002063`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.058874`, as_primary `20`, as_primary_hit `0.65`, avg `0.011983`, median `0.016341`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.087599`, as_primary `20`, as_primary_hit `0.7`, avg `0.014024`, median `0.026861`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.017807`, as_primary `60`, as_primary_hit `0.6`, avg `0.002084`, median `0.001378`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.024108`, as_primary `60`, as_primary_hit `0.6167`, avg `0.002137`, median `0.001659`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.036037`, as_primary `60`, as_primary_hit `0.5`, avg `0.001763`, median `-0.002063`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.069652`, as_primary `60`, as_primary_hit `0.6167`, avg `0.011983`, median `0.016341`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.109999`, as_primary `60`, as_primary_hit `0.5167`, avg `0.014024`, median `0.026861`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014533`, as_primary `0`, as_primary_hit `None`, avg `0.002084`, median `0.001378`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.01783`, as_primary `0`, as_primary_hit `None`, avg `0.002137`, median `0.001659`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.023409`, as_primary `0`, as_primary_hit `None`, avg `0.001763`, median `-0.002063`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.036463`, as_primary `0`, as_primary_hit `None`, avg `0.011983`, median `0.016341`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.069058`, as_primary `0`, as_primary_hit `None`, avg `0.014024`, median `0.026861`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.020667`, avg `-0.003632`, median `0.001378`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.025306`, avg `-0.006515`, median `-0.000507`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.027036`, avg `-0.00105`, median `-0.006514`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.053349`, avg `0.018438`, median `0.024617`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.085577`, avg `0.036923`, median `0.041779`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4`, primary_closer `0.4833`, primary_mae `0.015885`, avg `0.00399`, median `0.001595`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.5167`, primary_mae `0.024236`, avg `0.005022`, median `0.001797`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.040829`, avg `0.0027`, median `-0.000896`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.2833`, primary_mae `0.073119`, avg `0.009831`, median `0.015359`
- 60d: sample `60`, primary_hit `0.4833`, primary_closer `0.3167`, primary_mae `0.111998`, avg `0.00639`, median `0.008129`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.014021`, avg `0.006576`, median `0.003846`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.55`, primary_mae `0.022857`, avg `0.011039`, median `0.006165`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.054465`, avg `0.009535`, median `0.014043`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.110652`, avg `0.009096`, median `0.018088`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.164877`, avg `-0.033982`, median `-0.003084`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.016817`, avg `0.002697`, median `0.000944`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.5`, primary_mae `0.024925`, avg `0.002013`, median `0.001088`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.034011`, avg `-0.000717`, median `-0.007037`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.054353`, avg `0.010198`, median `0.011226`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.275`, primary_mae `0.085559`, avg `0.026577`, median `0.029534`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.020667`, avg `-0.003632`, median `0.001378`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.025306`, avg `-0.006515`, median `-0.000507`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.027036`, avg `-0.00105`, median `-0.006514`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.053349`, avg `0.018438`, median `0.024617`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.085577`, avg `0.036923`, median `0.041779`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.014021, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.022857, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.027036, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.053349, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.085559, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014533, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01803, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.014021, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01783, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025233, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.022857, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023409, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036037, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.027036, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036463, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069652, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.053349, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069058, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.109999, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.085559, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.025728`, avg `-0.014537`, median `-0.009708`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.035441`, avg `-0.02117`, median `-0.019178`
- 10d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.031957`, avg `-0.010848`, median `-0.011439`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.065021`, avg `0.006054`, median `0.01014`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.097481`, avg `0.027723`, median `0.029112`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.021243`, avg `-0.003936`, median `0.000341`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.025651`, avg `-0.007252`, median `0.00171`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.027675`, avg `-0.001903`, median `-0.007383`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.060412`, avg `0.011989`, median `0.01014`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.097307`, avg `0.025357`, median `0.030028`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.625`, primary_mae `0.010501`, avg `0.000758`, median `0.000402`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.875`, primary_mae `0.010096`, avg `0.002291`, median `0.001463`
- 10d: sample `16`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.015799`, avg `-0.01543`, median `-0.01559`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.053143`, avg `-0.016838`, median `-0.011244`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.064931`, avg `-0.005542`, median `-0.009163`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.017081`, avg `0.002084`, median `0.001378`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.525`, primary_mae `0.024503`, avg `0.002137`, median `0.001659`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.35`, primary_mae `0.037381`, avg `0.001763`, median `-0.002063`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.068177`, avg `0.011983`, median `0.016341`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.105393`, avg `0.014024`, median `0.026861`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.017081`, avg `0.002084`, median `0.001378`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.525`, primary_mae `0.024503`, avg `0.002137`, median `0.001659`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.35`, primary_mae `0.037381`, avg `0.001763`, median `-0.002063`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.068177`, avg `0.011983`, median `0.016341`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.105393`, avg `0.014024`, median `0.026861`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.575`, primary_mae `0.016349`, avg `-0.002515`, median `0.000402`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.625`, primary_mae `0.018326`, avg `-0.004593`, median `0.000725`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.425`, primary_mae `0.021724`, avg `-0.007728`, median `-0.010971`
- 20d: sample `40`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.051881`, avg `-0.001804`, median `-0.003981`
- 60d: sample `40`, primary_hit `0.7`, primary_closer `0.475`, primary_mae `0.071663`, avg `0.01246`, median `-0.001484`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.017812`, avg `0.006684`, median `0.008855`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.425`, primary_mae `0.030681`, avg `0.008868`, median `0.006165`
- 10d: sample `40`, primary_hit `0.35`, primary_closer `0.275`, primary_mae `0.053038`, avg `0.011253`, median `0.016131`
- 20d: sample `40`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.084472`, avg `0.025769`, median `0.036112`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.139122`, avg `0.015588`, median `0.046049`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.017081`, avg `0.002084`, median `0.001378`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.525`, primary_mae `0.024503`, avg `0.002137`, median `0.001659`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.35`, primary_mae `0.037381`, avg `0.001763`, median `-0.002063`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.068177`, avg `0.011983`, median `0.016341`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.105393`, avg `0.014024`, median `0.026861`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.5`, primary_mae `0.018764`, avg `0.003245`, median `0.003405`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.4667`, primary_mae `0.028889`, avg `0.00374`, median `0.003417`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.04437`, avg `0.007152`, median `0.007901`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.35`, primary_mae `0.074098`, avg `0.023326`, median `0.033856`
- 60d: sample `60`, primary_hit `0.4833`, primary_closer `0.4`, primary_mae `0.121274`, avg `0.0227`, median `0.044873`

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
