# Historical Replay Benchmark

Generated at: `2026-07-14T14:17:04.307155+00:00`
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
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.012943`
- secondary_mean_absolute_error: `0.011582`
- primary_error_advantage: `-0.001361`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.018193`
- secondary_mean_absolute_error: `0.015768`
- primary_error_advantage: `-0.002425`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.026046`
- secondary_mean_absolute_error: `0.025993`
- primary_error_advantage: `-5.3e-05`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.2375`
- primary_mean_absolute_error: `0.065354`
- secondary_mean_absolute_error: `0.041088`
- primary_error_advantage: `-0.024266`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.2167`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.073861`
- secondary_mean_absolute_error: `0.071813`
- primary_error_advantage: `-0.002048`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5667`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.011493`, as_primary `0`, as_primary_hit `None`, avg `-0.001192`, median `0.000673`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.01585`, as_primary `0`, as_primary_hit `None`, avg `-0.000353`, median `0.003772`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.022027`, as_primary `0`, as_primary_hit `None`, avg `-0.001668`, median `-0.001038`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.030828`, as_primary `0`, as_primary_hit `None`, avg `0.003218`, median `0.011504`
- 60d: sample `80`, direction_hit `0.5`, path_mae `0.064757`, as_primary `0`, as_primary_hit `None`, avg `0.004252`, median `-0.000292`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.012125`, as_primary `20`, as_primary_hit `0.65`, avg `-0.001192`, median `0.000673`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.016276`, as_primary `20`, as_primary_hit `0.55`, avg `-0.000353`, median `0.003772`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.026012`, as_primary `20`, as_primary_hit `0.5`, avg `-0.001668`, median `-0.001038`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.045347`, as_primary `20`, as_primary_hit `0.75`, avg `0.003218`, median `0.011504`
- 60d: sample `80`, direction_hit `0.5`, path_mae `0.07286`, as_primary `20`, as_primary_hit `0.55`, avg `0.004252`, median `-0.000292`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.012449`, as_primary `60`, as_primary_hit `0.5`, avg `-0.001192`, median `0.000673`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018335`, as_primary `60`, as_primary_hit `0.55`, avg `-0.000353`, median `0.003772`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.027031`, as_primary `60`, as_primary_hit `0.4667`, avg `-0.001668`, median `-0.001038`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.068099`, as_primary `60`, as_primary_hit `0.65`, avg `0.003218`, median `0.011504`
- 60d: sample `80`, direction_hit `0.5`, path_mae `0.076224`, as_primary `60`, as_primary_hit `0.4833`, avg `0.004252`, median `-0.000292`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.011388`, as_primary `0`, as_primary_hit `None`, avg `-0.001192`, median `0.000673`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.015509`, as_primary `0`, as_primary_hit `None`, avg `-0.000353`, median `0.003772`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.020989`, as_primary `0`, as_primary_hit `None`, avg `-0.001668`, median `-0.001038`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.031328`, as_primary `0`, as_primary_hit `None`, avg `0.003218`, median `0.011504`
- 60d: sample `80`, direction_hit `0.5`, path_mae `0.061757`, as_primary `0`, as_primary_hit `None`, avg `0.004252`, median `-0.000292`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.009198`, avg `0.00105`, median `0.000673`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.013772`, avg `0.003822`, median `0.005522`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.024622`, avg `1.6e-05`, median `0.001302`
- 20d: sample `40`, primary_hit `0.55`, primary_closer `0.25`, primary_mae `0.050704`, avg `0.00618`, median `0.012791`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.067829`, avg `-0.001415`, median `-0.013302`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.016689`, avg `-0.003435`, median `0.000886`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.022613`, avg `-0.004527`, median `-0.001055`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.575`, primary_mae `0.027469`, avg `-0.003352`, median `-0.008877`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.225`, primary_mae `0.080004`, avg `0.000256`, median `0.007521`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.079894`, avg `0.009919`, median `0.008008`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.007575`, avg `-0.002018`, median `-0.00191`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.65`, primary_mae `0.012341`, avg `0.001007`, median `0.004486`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.025753`, avg `-0.002355`, median `0.002926`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.05504`, avg `-4.6e-05`, median `0.011191`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.05847`, avg `-0.020507`, median `-0.030547`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.021171`, avg `-0.008048`, median `-0.005521`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.025671`, avg `-0.009747`, median `-0.003481`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.024907`, avg `-0.010959`, median `-0.016097`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.076664`, avg `-0.000783`, median `0.012154`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.109272`, avg `0.012535`, median `0.024759`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.011514`, avg `0.002648`, median `0.00544`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.017379`, avg `0.003664`, median `0.006047`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.026761`, avg `0.003321`, median `0.002358`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.2`, primary_mae `0.064855`, avg `0.006851`, median `0.012285`
- 60d: sample `40`, primary_hit `0.525`, primary_closer `0.55`, primary_mae `0.063852`, avg `0.01249`, median `0.002507`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.007575, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.012341, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.024907, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.05504, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.05847, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011388, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012449, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.007575, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015509, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018335, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.012341, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020989, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027031, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.024907, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.2375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030828, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.068099, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.05504, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061757, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076224, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.05847, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.00825`, avg `0.004856`, median `0.003333`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.014257`, avg `0.003711`, median `0.002881`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.021057`, avg `-0.004766`, median `-0.00151`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.055623`, avg `0.003316`, median `0.005283`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.069305`, avg `0.014702`, median `0.029359`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.008918`, avg `0.004444`, median `0.00431`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.013488`, avg `0.007348`, median `0.006047`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.022929`, avg `-0.002499`, median `-0.007236`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.049981`, avg `0.009736`, median `0.012815`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.07719`, avg `0.022863`, median `0.029359`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.019421`, avg `-0.009866`, median `-0.010725`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.024631`, avg `-0.012237`, median `-0.004713`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.5625`, primary_mae `0.024592`, avg `-0.011987`, median `-0.017542`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.071872`, avg `-0.007431`, median `0.002227`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.094237`, avg `-0.004189`, median `-0.017896`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.012943`, avg `-0.001192`, median `0.000673`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4625`, primary_mae `0.018193`, avg `-0.000353`, median `0.003772`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.026046`, avg `-0.001668`, median `-0.001038`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.2375`, primary_mae `0.065354`, avg `0.003218`, median `0.011504`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.5375`, primary_mae `0.073861`, avg `0.004252`, median `-0.000292`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.012943`, avg `-0.001192`, median `0.000673`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4625`, primary_mae `0.018193`, avg `-0.000353`, median `0.003772`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.026046`, avg `-0.001668`, median `-0.001038`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.2375`, primary_mae `0.065354`, avg `0.003218`, median `0.011504`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.5375`, primary_mae `0.073861`, avg `0.004252`, median `-0.000292`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.575`, primary_mae `0.009891`, avg `-0.00042`, median `0.000235`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.575`, primary_mae `0.015948`, avg `0.000849`, median `0.00487`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.027892`, avg `0.000951`, median `0.003376`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.2`, primary_mae `0.069192`, avg `0.000624`, median `0.009321`
- 60d: sample `40`, primary_hit `0.55`, primary_closer `0.625`, primary_mae `0.054493`, avg `-0.006603`, median `-0.011052`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.013651`, avg `-0.002963`, median `-0.00051`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.4833`, primary_mae `0.019189`, avg `-0.002683`, median `0.003359`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4833`, primary_mae `0.026897`, avg `-0.003019`, median `-0.001038`
- 20d: sample `60`, primary_hit `0.35`, primary_closer `0.2333`, primary_mae `0.071682`, avg `0.000155`, median `0.009321`
- 60d: sample `60`, primary_hit `0.5167`, primary_closer `0.5667`, primary_mae `0.072753`, avg `-0.000223`, median `-0.003329`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.012943`, avg `-0.001192`, median `0.000673`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4625`, primary_mae `0.018193`, avg `-0.000353`, median `0.003772`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.026046`, avg `-0.001668`, median `-0.001038`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.2375`, primary_mae `0.065354`, avg `0.003218`, median `0.011504`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.5375`, primary_mae `0.073861`, avg `0.004252`, median `-0.000292`

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
