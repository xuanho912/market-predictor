# Historical Replay Benchmark

Generated at: `2026-08-25T21:57:50.798866+00:00`
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
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.015594`
- secondary_mean_absolute_error: `0.015136`
- primary_error_advantage: `-0.000458`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.020765`
- secondary_mean_absolute_error: `0.019328`
- primary_error_advantage: `-0.001437`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.03563`
- secondary_mean_absolute_error: `0.033519`
- primary_error_advantage: `-0.002111`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.052454`
- secondary_mean_absolute_error: `0.053862`
- primary_error_advantage: `0.001408`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.074331`
- secondary_mean_absolute_error: `0.065248`
- primary_error_advantage: `-0.009083`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.013864`, as_primary `0`, as_primary_hit `None`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.018048`, as_primary `0`, as_primary_hit `None`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.025525`, as_primary `0`, as_primary_hit `None`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.036707`, as_primary `0`, as_primary_hit `None`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.060878`, as_primary `0`, as_primary_hit `None`, avg `0.01801`, median `0.028684`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014923`, as_primary `60`, as_primary_hit `0.6167`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.019895`, as_primary `60`, as_primary_hit `0.55`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.037186`, as_primary `60`, as_primary_hit `0.5667`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.049712`, as_primary `60`, as_primary_hit `0.6833`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.074744`, as_primary `60`, as_primary_hit `0.6667`, avg `0.01801`, median `0.028684`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.017149`, as_primary `20`, as_primary_hit `0.5`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.021759`, as_primary `20`, as_primary_hit `0.6`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.040702`, as_primary `20`, as_primary_hit `0.25`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.074468`, as_primary `20`, as_primary_hit `0.4`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, direction_hit `0.4`, path_mae `0.074851`, as_primary `20`, as_primary_hit `0.4`, avg `0.01801`, median `0.028684`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.01388`, as_primary `0`, as_primary_hit `None`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017744`, as_primary `0`, as_primary_hit `None`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.025014`, as_primary `0`, as_primary_hit `None`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.037453`, as_primary `0`, as_primary_hit `None`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.056717`, as_primary `0`, as_primary_hit `None`, avg `0.01801`, median `0.028684`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.015594`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.020765`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4875`, primary_mae `0.03563`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.052454`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, primary_hit `0.65`, primary_closer `0.4625`, primary_mae `0.074331`, avg `0.01801`, median `0.028684`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.5167`, primary_mae `0.016891`, avg `0.002664`, median `0.00509`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.4833`, primary_mae `0.023332`, avg `0.002362`, median `0.003417`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.4333`, primary_mae `0.039569`, avg `0.005656`, median `0.006195`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.4667`, primary_mae `0.047926`, avg `0.008017`, median `0.024066`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.4333`, primary_mae `0.074823`, avg `0.025339`, median `0.029874`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.011702`, avg `-0.001171`, median `-0.000413`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.013065`, avg `-0.002599`, median `0.000781`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.023815`, avg `-0.01227`, median `-0.016966`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.066036`, avg `-0.020576`, median `-0.011784`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.072856`, avg `-0.003977`, median `-0.018485`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.011702, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013065, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.023815, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.047926, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.072856, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013864, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017149, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.011702, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017744, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021759, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013065, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025014, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040702, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.023815, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036707, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074468, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.047926, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056717, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074851, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.072856, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.016742`, avg `-0.008017`, median `0.001949`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.024323`, avg `-0.008603`, median `-0.006309`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.029901`, avg `-0.001747`, median `-0.00518`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.05324`, avg `-0.000917`, median `0.006586`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.081364`, avg `0.002785`, median `0.004851`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.015007`, avg `-0.002252`, median `0.001949`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.019308`, avg `-0.002461`, median `0.00171`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.026133`, avg `0.006015`, median `0.013177`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.043274`, avg `0.01168`, median `0.023299`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.071627`, avg `0.021661`, median `0.029874`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.012765`, avg `0.000141`, median `0.000684`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.012923`, avg `-0.00307`, median `0.000633`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.024496`, avg `-0.011944`, median `-0.016467`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.067051`, avg `-0.020369`, median `-0.011784`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.075705`, avg `-0.003036`, median `-0.018485`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.015594`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.020765`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4875`, primary_mae `0.03563`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.052454`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, primary_hit `0.65`, primary_closer `0.4625`, primary_mae `0.074331`, avg `0.01801`, median `0.028684`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.015594`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.020765`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4875`, primary_mae `0.03563`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.052454`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, primary_hit `0.65`, primary_closer `0.4625`, primary_mae `0.074331`, avg `0.01801`, median `0.028684`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.015603`, avg `-0.00385`, median `-0.000127`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.019661`, avg `-0.004014`, median `-0.002011`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.024422`, avg `0.007073`, median `0.010282`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.039228`, avg `0.0152`, median `0.027848`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.070691`, avg `0.022341`, median `0.031374`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.015269`, avg `0.002849`, median `0.003955`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.019829`, avg `0.000706`, median `0.000781`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.475`, primary_mae `0.03722`, avg `-0.003605`, median `-0.007787`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.060676`, avg `-0.005839`, median `0.009671`
- 60d: sample `40`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.088642`, avg `0.024621`, median `0.030984`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.015594`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.020765`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4875`, primary_mae `0.03563`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.052454`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, primary_hit `0.65`, primary_closer `0.4625`, primary_mae `0.074331`, avg `0.01801`, median `0.028684`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.015594`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.020765`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4875`, primary_mae `0.03563`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.052454`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, primary_hit `0.65`, primary_closer `0.4625`, primary_mae `0.074331`, avg `0.01801`, median `0.028684`

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
