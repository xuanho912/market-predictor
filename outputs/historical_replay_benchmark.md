# Historical Replay Benchmark

Generated at: `2026-07-21T14:26:10.252393+00:00`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.014752`
- secondary_mean_absolute_error: `0.013808`
- primary_error_advantage: `-0.000944`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.019306`
- secondary_mean_absolute_error: `0.016626`
- primary_error_advantage: `-0.00268`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.026614`
- secondary_mean_absolute_error: `0.025078`
- primary_error_advantage: `-0.001536`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.064307`
- secondary_mean_absolute_error: `0.043693`
- primary_error_advantage: `-0.020614`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.111918`
- secondary_mean_absolute_error: `0.085332`
- primary_error_advantage: `-0.026586`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.012375`, as_primary `0`, as_primary_hit `None`, avg `-0.003447`, median `0.000609`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.015525`, as_primary `0`, as_primary_hit `None`, avg `-0.004528`, median `-0.000869`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.021899`, as_primary `0`, as_primary_hit `None`, avg `-0.002859`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.035313`, as_primary `0`, as_primary_hit `None`, avg `0.009487`, median `0.01543`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.075278`, as_primary `0`, as_primary_hit `None`, avg `0.01931`, median `0.044873`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.013982`, as_primary `0`, as_primary_hit `None`, avg `-0.003447`, median `0.000609`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.017672`, as_primary `0`, as_primary_hit `None`, avg `-0.004528`, median `-0.000869`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.028415`, as_primary `0`, as_primary_hit `None`, avg `-0.002859`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.049143`, as_primary `0`, as_primary_hit `None`, avg `0.009487`, median `0.01543`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.087907`, as_primary `0`, as_primary_hit `None`, avg `0.01931`, median `0.044873`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.014752`, as_primary `80`, as_primary_hit `0.525`, avg `-0.003447`, median `0.000609`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.019306`, as_primary `80`, as_primary_hit `0.475`, avg `-0.004528`, median `-0.000869`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.026614`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.002859`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.064307`, as_primary `80`, as_primary_hit `0.6375`, avg `0.009487`, median `0.01543`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.111918`, as_primary `80`, as_primary_hit `0.5625`, avg `0.01931`, median `0.044873`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.012143`, as_primary `0`, as_primary_hit `None`, avg `-0.003447`, median `0.000609`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.015026`, as_primary `0`, as_primary_hit `None`, avg `-0.004528`, median `-0.000869`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.020863`, as_primary `0`, as_primary_hit `None`, avg `-0.002859`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.035247`, as_primary `0`, as_primary_hit `None`, avg `0.009487`, median `0.01543`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.076035`, as_primary `0`, as_primary_hit `None`, avg `0.01931`, median `0.044873`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.022828`, avg `-0.010492`, median `-0.009708`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.028431`, avg `-0.017101`, median `-0.019178`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.018045`, avg `-0.005238`, median `-0.007383`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.068191`, avg `0.010514`, median `0.01014`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.101964`, avg `0.031428`, median `0.041779`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.3667`, primary_mae `0.01206`, avg `-0.001098`, median `0.000726`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.45`, primary_mae `0.016264`, avg `-0.000337`, median `0.000725`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.029471`, avg `-0.002065`, median `-0.005393`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.3333`, primary_mae `0.063013`, avg `0.009144`, median `0.01543`
- 60d: sample `60`, primary_hit `0.45`, primary_closer `0.3833`, primary_mae `0.115236`, avg `0.015271`, median `0.046049`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.3667`, primary_mae `0.01206`, avg `-0.001098`, median `0.000726`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.45`, primary_mae `0.016264`, avg `-0.000337`, median `0.000725`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.029471`, avg `-0.002065`, median `-0.005393`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.3333`, primary_mae `0.063013`, avg `0.009144`, median `0.01543`
- 60d: sample `60`, primary_hit `0.45`, primary_closer `0.3833`, primary_mae `0.115236`, avg `0.015271`, median `0.046049`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.022828`, avg `-0.010492`, median `-0.009708`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.028431`, avg `-0.017101`, median `-0.019178`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.018045`, avg `-0.005238`, median `-0.007383`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.068191`, avg `0.010514`, median `0.01014`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.101964`, avg `0.031428`, median `0.041779`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.01206, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016264, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.018045, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.3333, 'primary_mean_absolute_error': 0.063013, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.101964, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012143, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014752, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.01206, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015026, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019306, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016264, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020863, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028415, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.018045, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035247, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064307, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.3333, 'primary_mean_absolute_error': 0.063013, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075278, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.111918, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.101964, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.020078`, avg `-0.012643`, median `-0.005846`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.027999`, avg `-0.016654`, median `-0.019178`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.013602`, avg `-0.011849`, median `-0.012486`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.077358`, avg `0.025786`, median `0.031583`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.12867`, avg `0.065978`, median `0.079666`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.024489`, avg `-0.008641`, median `-0.005521`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.032165`, avg `-0.014327`, median `-0.01025`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.6875`, primary_mae `0.017655`, avg `-0.006657`, median `-0.009105`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.071633`, avg `0.012118`, median `0.024617`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.110488`, avg `0.037991`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.011394`, avg `0.003759`, median `0.002829`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.016988`, avg `0.005169`, median `0.001846`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.038655`, avg `-0.006359`, median `-0.016185`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.10238`, avg `0.000177`, median `0.016877`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.207467`, avg `0.007522`, median `0.090445`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.014752`, avg `-0.003447`, median `0.000609`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.019306`, avg `-0.004528`, median `-0.000869`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.026614`, avg `-0.002859`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.375`, primary_mae `0.064307`, avg `0.009487`, median `0.01543`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.111918`, avg `0.01931`, median `0.044873`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.014752`, avg `-0.003447`, median `0.000609`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.019306`, avg `-0.004528`, median `-0.000869`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.026614`, avg `-0.002859`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.375`, primary_mae `0.064307`, avg `0.009487`, median `0.01543`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.111918`, avg `0.01931`, median `0.044873`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.016684`, avg `-0.007294`, median `-0.004983`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.020072`, avg `-0.011136`, median `-0.003439`
- 10d: sample `40`, primary_hit `0.7`, primary_closer `0.65`, primary_mae `0.019481`, avg `-0.006529`, median `-0.008819`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.06391`, avg `0.00257`, median `-0.001434`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.083099`, avg `0.019105`, median `0.009193`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.014278`, avg `-0.002586`, median `-0.003808`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.020269`, avg `-0.001075`, median `-0.006669`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.031153`, avg `0.010213`, median `0.015799`
- 20d: sample `20`, primary_hit `0.0`, primary_closer `0.35`, primary_mae `0.02866`, avg `0.033613`, median `0.037591`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.087878`, avg `0.044293`, median `0.071478`

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
