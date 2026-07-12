# Historical Replay Benchmark

Generated at: `2026-07-12T13:59:12.130832+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.012062`
- secondary_mean_absolute_error: `0.012074`
- primary_error_advantage: `1.2e-05`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.01601`
- secondary_mean_absolute_error: `0.015234`
- primary_error_advantage: `-0.000776`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.022249`
- secondary_mean_absolute_error: `0.022865`
- primary_error_advantage: `0.000616`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.056952`
- secondary_mean_absolute_error: `0.03982`
- primary_error_advantage: `-0.017132`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.225`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.073168`
- secondary_mean_absolute_error: `0.069641`
- primary_error_advantage: `-0.003527`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.012147`, as_primary `0`, as_primary_hit `None`, avg `-0.000956`, median `0.000886`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.015181`, as_primary `0`, as_primary_hit `None`, avg `-0.000938`, median `0.003101`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.019356`, as_primary `0`, as_primary_hit `None`, avg `-0.002566`, median `0.001302`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.034584`, as_primary `0`, as_primary_hit `None`, avg `-0.002328`, median `0.0089`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.063024`, as_primary `0`, as_primary_hit `None`, avg `0.003881`, median `0.009134`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.012179`, as_primary `60`, as_primary_hit `0.55`, avg `-0.000956`, median `0.000886`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.016214`, as_primary `60`, as_primary_hit `0.5667`, avg `-0.000938`, median `0.003101`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.023797`, as_primary `60`, as_primary_hit `0.5333`, avg `-0.002566`, median `0.001302`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.048278`, as_primary `60`, as_primary_hit `0.7`, avg `-0.002328`, median `0.0089`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.076785`, as_primary `60`, as_primary_hit `0.5333`, avg `0.003881`, median `0.009134`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.012983`, as_primary `20`, as_primary_hit `0.45`, avg `-0.000956`, median `0.000886`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.017525`, as_primary `20`, as_primary_hit `0.5`, avg `-0.000938`, median `0.003101`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.026958`, as_primary `20`, as_primary_hit `0.45`, avg `-0.002566`, median `0.001302`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.072546`, as_primary `20`, as_primary_hit `0.55`, avg `-0.002328`, median `0.0089`
- 60d: sample `80`, direction_hit `0.4875`, path_mae `0.082545`, as_primary `20`, as_primary_hit `0.45`, avg `0.003881`, median `0.009134`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.011879`, as_primary `0`, as_primary_hit `None`, avg `-0.000956`, median `0.000886`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.014835`, as_primary `0`, as_primary_hit `None`, avg `-0.000938`, median `0.003101`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.019315`, as_primary `0`, as_primary_hit `None`, avg `-0.002566`, median `0.001302`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.034477`, as_primary `0`, as_primary_hit `None`, avg `-0.002328`, median `0.0089`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.061697`, as_primary `0`, as_primary_hit `None`, avg `0.003881`, median `0.009134`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.012062`, avg `-0.000956`, median `0.000886`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.01601`, avg `-0.000938`, median `0.003101`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.022249`, avg `-0.002566`, median `0.001302`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.056952`, avg `-0.002328`, median `0.0089`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.073168`, avg `0.003881`, median `0.009134`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.010312`, avg `-0.000195`, median `-0.00051`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.01627`, avg `0.000555`, median `0.004272`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.525`, primary_mae `0.025896`, avg `-0.002085`, median `0.004979`
- 20d: sample `40`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.068192`, avg `-0.007012`, median `0.007521`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.078179`, avg `-0.004007`, median `-0.011728`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.013812`, avg `-0.001717`, median `0.001949`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.01575`, avg `-0.002432`, median `0.00014`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.018601`, avg `-0.003047`, median `-0.003167`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.275`, primary_mae `0.045711`, avg `0.002356`, median `0.010449`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.425`, primary_mae `0.068157`, avg `0.011769`, median `0.020962`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.010312, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.01575, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018601, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.045711, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.068157, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011879, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012983, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.010312, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014835, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017525, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.01575, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019315, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026958, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018601, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034477, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072546, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.045711, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061697, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.082545, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.068157, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.01785`, avg `-0.002449`, median `0.006507`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.016703`, avg `-0.004006`, median `-0.006575`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.023093`, avg `0.001119`, median `0.001055`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.024212`, avg `0.026927`, median `0.027848`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.053469`, avg `0.042692`, median `0.066618`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.015852`, avg `-0.00769`, median `-0.000105`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.019109`, avg `-0.010882`, median `-0.006575`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.023508`, avg `-0.006756`, median `-0.010098`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.048102`, avg `0.002468`, median `0.017805`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.080747`, avg `0.012942`, median `0.012424`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.6875`, primary_mae `0.01375`, avg `-0.003934`, median `-0.007307`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016871`, avg `-0.005953`, median `-0.01009`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.03297`, avg `-0.009809`, median `-0.018589`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.106981`, avg `-0.020545`, median `0.002411`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.075289`, avg `-0.006755`, median `0.001159`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.012062`, avg `-0.000956`, median `0.000886`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.01601`, avg `-0.000938`, median `0.003101`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.022249`, avg `-0.002566`, median `0.001302`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.056952`, avg `-0.002328`, median `0.0089`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.073168`, avg `0.003881`, median `0.009134`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.012062`, avg `-0.000956`, median `0.000886`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.01601`, avg `-0.000938`, median `0.003101`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.022249`, avg `-0.002566`, median `0.001302`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.056952`, avg `-0.002328`, median `0.0089`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.073168`, avg `0.003881`, median `0.009134`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.55`, primary_mae `0.012482`, avg `-0.00267`, median `-0.00051`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.4667`, primary_mae `0.016629`, avg `-0.002793`, median `0.002849`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.4833`, primary_mae `0.024651`, avg `-0.004175`, median `-0.000307`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.3333`, primary_mae `0.061555`, avg `-0.004136`, median `0.007832`
- 60d: sample `60`, primary_hit `0.5167`, primary_closer `0.45`, primary_mae `0.078668`, avg `0.001164`, median `-0.00549`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.01254`, avg `-0.002278`, median `-0.004648`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017332`, avg `-0.002894`, median `-0.001601`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.035121`, avg `-0.007194`, median `-0.012374`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.25`, primary_mae `0.107753`, avg `-0.017588`, median `0.002411`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.08091`, avg `-0.002908`, median `-0.007976`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.012062`, avg `-0.000956`, median `0.000886`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.01601`, avg `-0.000938`, median `0.003101`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.022249`, avg `-0.002566`, median `0.001302`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.056952`, avg `-0.002328`, median `0.0089`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.073168`, avg `0.003881`, median `0.009134`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.012062`, avg `-0.000956`, median `0.000886`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.01601`, avg `-0.000938`, median `0.003101`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.022249`, avg `-0.002566`, median `0.001302`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.056952`, avg `-0.002328`, median `0.0089`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.073168`, avg `0.003881`, median `0.009134`

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
