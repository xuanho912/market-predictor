# Historical Replay Benchmark

Generated at: `2026-06-23T23:39:21.420991+00:00`
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
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.020035`
- secondary_mean_absolute_error: `0.014945`
- primary_error_advantage: `-0.00509`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.2875`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.020321`
- secondary_mean_absolute_error: `0.018851`
- primary_error_advantage: `-0.00147`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.03411`
- secondary_mean_absolute_error: `0.029587`
- primary_error_advantage: `-0.004523`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2875`
- secondary_hit_rate: `0.7625`
- primary_vs_secondary_accuracy_spread: `-0.475`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.051464`
- secondary_mean_absolute_error: `0.0343`
- primary_error_advantage: `-0.017164`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.325`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.058511`
- secondary_mean_absolute_error: `0.053849`
- primary_error_advantage: `-0.004662`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.014718`, as_primary `0`, as_primary_hit `None`, avg `0.000988`, median `-0.001404`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.017478`, as_primary `0`, as_primary_hit `None`, avg `-0.000655`, median `-0.000848`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.024872`, as_primary `0`, as_primary_hit `None`, avg `0.000309`, median `-0.001836`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.027947`, as_primary `0`, as_primary_hit `None`, avg `0.015255`, median `0.020408`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.04578`, as_primary `0`, as_primary_hit `None`, avg `0.039858`, median `0.061862`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.016307`, as_primary `20`, as_primary_hit `0.6`, avg `0.000988`, median `-0.001404`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.019592`, as_primary `20`, as_primary_hit `0.6`, avg `-0.000655`, median `-0.000848`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.030375`, as_primary `20`, as_primary_hit `0.5`, avg `0.000309`, median `-0.001836`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.040064`, as_primary `20`, as_primary_hit `0.6`, avg `0.015255`, median `0.020408`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.05379`, as_primary `20`, as_primary_hit `0.75`, avg `0.039858`, median `0.061862`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.01906`, as_primary `60`, as_primary_hit `0.4167`, avg `0.000988`, median `-0.001404`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.020012`, as_primary `60`, as_primary_hit `0.45`, avg `-0.000655`, median `-0.000848`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.034162`, as_primary `60`, as_primary_hit `0.4333`, avg `0.000309`, median `-0.001836`
- 20d: sample `80`, direction_hit `0.2375`, path_mae `0.051843`, as_primary `60`, as_primary_hit `0.8167`, avg `0.015255`, median `0.020408`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.061383`, as_primary `60`, as_primary_hit `0.7167`, avg `0.039858`, median `0.061862`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.014351`, as_primary `0`, as_primary_hit `None`, avg `0.000988`, median `-0.001404`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.017021`, as_primary `0`, as_primary_hit `None`, avg `-0.000655`, median `-0.000848`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.023884`, as_primary `0`, as_primary_hit `None`, avg `0.000309`, median `-0.001836`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.02709`, as_primary `0`, as_primary_hit `None`, avg `0.015255`, median `0.020408`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.048156`, as_primary `0`, as_primary_hit `None`, avg `0.039858`, median `0.061862`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.2875`, primary_mae `0.020035`, avg `0.000988`, median `-0.001404`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.475`, primary_mae `0.020321`, avg `-0.000655`, median `-0.000848`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.03411`, avg `0.000309`, median `-0.001836`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.325`, primary_mae `0.051464`, avg `0.015255`, median `0.020408`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.058511`, avg `0.039858`, median `0.061862`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.016401`, avg `-0.002688`, median `-0.004669`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.01952`, avg `-0.005424`, median `-0.00869`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.03552`, avg `-0.00573`, median `-0.007304`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.069318`, avg `-0.003397`, median `0.013566`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.050683`, avg `0.010608`, median `0.032753`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5667`, primary_closer `0.3`, primary_mae `0.021246`, avg `0.002213`, median `0.000418`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.4667`, primary_mae `0.020588`, avg `0.000934`, median `-8.2e-05`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.03364`, avg `0.002321`, median `-0.001153`
- 20d: sample `60`, primary_hit `0.2833`, primary_closer `0.35`, primary_mae `0.045513`, avg `0.021472`, median `0.028445`
- 60d: sample `60`, primary_hit `0.4`, primary_closer `0.4833`, primary_mae `0.06112`, avg `0.049608`, median `0.070539`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.016401, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.01952, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.03364, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.045513, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.050683, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014351, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01906, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.016401, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017021, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020012, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.01952, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023884, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034162, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.03364, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7625, 'primary_vs_secondary_accuracy_spread': -0.475, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02709, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051843, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.045513, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04578, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061383, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.050683, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.0`, primary_mae `0.026323`, avg `-0.005153`, median `-0.004956`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.023262`, avg `-0.001032`, median `-0.004187`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.03362`, avg `-0.011333`, median `-0.017088`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.062979`, avg `-0.004369`, median `0.006992`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.031665`, avg `0.056387`, median `0.072319`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.021776`, avg `0.007619`, median `0.005019`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.019228`, avg `0.004624`, median `0.001122`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.032763`, avg `0.001778`, median `-0.005494`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.058968`, avg `0.00694`, median `0.009441`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.5625`, primary_mae `0.0541`, avg `0.046768`, median `0.070539`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.024584`, avg `0.004443`, median `0.002901`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.018182`, avg `-0.003249`, median `-0.007293`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.017442`, avg `0.003179`, median `-0.001481`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.3125`, primary_mae `0.035922`, avg `0.030642`, median `0.029544`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.375`, primary_mae `0.046101`, avg `0.078105`, median `0.077573`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.2875`, primary_mae `0.020035`, avg `0.000988`, median `-0.001404`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.475`, primary_mae `0.020321`, avg `-0.000655`, median `-0.000848`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.03411`, avg `0.000309`, median `-0.001836`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.325`, primary_mae `0.051464`, avg `0.015255`, median `0.020408`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.058511`, avg `0.039858`, median `0.061862`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.2875`, primary_mae `0.020035`, avg `0.000988`, median `-0.001404`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.475`, primary_mae `0.020321`, avg `-0.000655`, median `-0.000848`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.03411`, avg `0.000309`, median `-0.001836`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.325`, primary_mae `0.051464`, avg `0.015255`, median `0.020408`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.058511`, avg `0.039858`, median `0.061862`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.018529`, avg `0.002728`, median `-0.000944`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.018197`, avg `0.001093`, median `0.002701`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.032337`, avg `-0.000644`, median `-0.004681`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.275`, primary_mae `0.062376`, avg `0.002808`, median `0.014347`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.051967`, avg `0.028266`, median `0.04246`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.3`, primary_mae `0.019827`, avg `-0.001397`, median `-0.002866`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.02147`, avg `-0.003411`, median `-0.006631`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.45`, primary_mae `0.035762`, avg `-0.001069`, median `-0.001836`
- 20d: sample `60`, primary_hit `0.1833`, primary_closer `0.3333`, primary_mae `0.050141`, avg `0.017335`, median `0.022835`
- 60d: sample `60`, primary_hit `0.2833`, primary_closer `0.4167`, primary_mae `0.060264`, avg `0.037836`, median `0.058512`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.2875`, primary_mae `0.020035`, avg `0.000988`, median `-0.001404`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.475`, primary_mae `0.020321`, avg `-0.000655`, median `-0.000848`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.03411`, avg `0.000309`, median `-0.001836`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.325`, primary_mae `0.051464`, avg `0.015255`, median `0.020408`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.058511`, avg `0.039858`, median `0.061862`

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
