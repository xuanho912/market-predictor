# Historical Replay Benchmark

Generated at: `2026-09-15T01:02:24.323843+00:00`
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
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.021758`
- secondary_mean_absolute_error: `0.017268`
- primary_error_advantage: `-0.00449`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.022565`
- secondary_mean_absolute_error: `0.019717`
- primary_error_advantage: `-0.002848`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.036604`
- secondary_mean_absolute_error: `0.026182`
- primary_error_advantage: `-0.010422`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.225`
- secondary_hit_rate: `0.775`
- primary_vs_secondary_accuracy_spread: `-0.55`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.054519`
- secondary_mean_absolute_error: `0.031428`
- primary_error_advantage: `-0.023091`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `-0.6`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.065052`
- secondary_mean_absolute_error: `0.057115`
- primary_error_advantage: `-0.007937`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.016611`, as_primary `0`, as_primary_hit `None`, avg `0.004929`, median `0.011557`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.020061`, as_primary `0`, as_primary_hit `None`, avg `0.006833`, median `0.010615`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.026938`, as_primary `0`, as_primary_hit `None`, avg `0.012263`, median `0.01642`
- 20d: sample `80`, direction_hit `0.775`, path_mae `0.03293`, as_primary `0`, as_primary_hit `None`, avg `0.033075`, median `0.03523`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.056598`, as_primary `0`, as_primary_hit `None`, avg `0.067791`, median `0.085394`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.017809`, as_primary `0`, as_primary_hit `None`, avg `0.004929`, median `0.011557`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.022735`, as_primary `0`, as_primary_hit `None`, avg `0.006833`, median `0.010615`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.034505`, as_primary `0`, as_primary_hit `None`, avg `0.012263`, median `0.01642`
- 20d: sample `80`, direction_hit `0.775`, path_mae `0.048153`, as_primary `0`, as_primary_hit `None`, avg `0.033075`, median `0.03523`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.059171`, as_primary `0`, as_primary_hit `None`, avg `0.067791`, median `0.085394`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.021758`, as_primary `80`, as_primary_hit `0.6375`, avg `0.004929`, median `0.011557`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.022565`, as_primary `80`, as_primary_hit `0.5875`, avg `0.006833`, median `0.010615`
- 10d: sample `80`, direction_hit `0.3125`, path_mae `0.036604`, as_primary `80`, as_primary_hit `0.6875`, avg `0.012263`, median `0.01642`
- 20d: sample `80`, direction_hit `0.225`, path_mae `0.054519`, as_primary `80`, as_primary_hit `0.775`, avg `0.033075`, median `0.03523`
- 60d: sample `80`, direction_hit `0.2`, path_mae `0.065052`, as_primary `80`, as_primary_hit `0.8`, avg `0.067791`, median `0.085394`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.017268`, as_primary `0`, as_primary_hit `None`, avg `0.004929`, median `0.011557`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.019717`, as_primary `0`, as_primary_hit `None`, avg `0.006833`, median `0.010615`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.026182`, as_primary `0`, as_primary_hit `None`, avg `0.012263`, median `0.01642`
- 20d: sample `80`, direction_hit `0.775`, path_mae `0.031428`, as_primary `0`, as_primary_hit `None`, avg `0.033075`, median `0.03523`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.057115`, as_primary `0`, as_primary_hit `None`, avg `0.067791`, median `0.085394`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.35`, primary_mae `0.021758`, avg `0.004929`, median `0.011557`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.022565`, avg `0.006833`, median `0.010615`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.036604`, avg `0.012263`, median `0.01642`
- 20d: sample `80`, primary_hit `0.225`, primary_closer `0.2875`, primary_mae `0.054519`, avg `0.033075`, median `0.03523`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.065052`, avg `0.067791`, median `0.085394`

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
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.032408`, avg `-0.006006`, median `-0.009681`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.034049`, avg `-0.006159`, median `-0.009536`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.054284`, avg `0.003165`, median `0.002203`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.062722`, avg `0.014596`, median `0.030478`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.09331`, avg `0.034027`, median `0.070115`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.014269`, avg `0.006489`, median `0.011557`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.014855`, avg `0.008052`, median `0.011297`
- 10d: sample `40`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.015085`, avg `0.011989`, median `0.012344`
- 20d: sample `40`, primary_hit `0.175`, primary_closer `0.25`, primary_mae `0.040424`, avg `0.033756`, median `0.035107`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.525`, primary_mae `0.042509`, avg `0.075645`, median `0.08585`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.026087`, avg `0.012744`, median `0.018551`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.026502`, avg `0.017387`, median `0.019955`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.061962`, avg `0.02191`, median `0.026309`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.074504`, avg `0.050192`, median `0.048916`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.081879`, avg `0.085844`, median `0.1123`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014269, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014855, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.015085, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.040424, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.042509, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016611, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021758, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014269, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019717, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022735, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014855, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026182, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036604, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.015085, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.225, 'secondary_hit_rate': 0.775, 'primary_vs_secondary_accuracy_spread': -0.55, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031428, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054519, 'direction_hit_rate': 0.225}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.040424, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': -0.6, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056598, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065052, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.042509, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.017523`, avg `-0.001324`, median `-0.001624`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.014475`, avg `0.004581`, median `0.008828`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.017894`, avg `0.011426`, median `0.017428`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.055364`, avg `0.050716`, median `0.058396`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.625`, primary_mae `0.034479`, avg `0.095878`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.625`, primary_mae `0.01503`, avg `0.009542`, median `0.017602`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.5625`, primary_mae `0.015746`, avg `0.012241`, median `0.014527`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.016335`, avg `0.016745`, median `0.018067`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.041884`, avg `0.036725`, median `0.038853`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.625`, primary_mae `0.043952`, avg `0.081093`, median `0.099778`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.033528`, avg `-0.005977`, median `-0.005289`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.034338`, avg `-0.005674`, median `-0.009536`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.048013`, avg `-0.003653`, median `-0.00147`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.054982`, avg `0.006354`, median `0.0135`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.099492`, avg `0.032283`, median `0.075157`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.35`, primary_mae `0.021758`, avg `0.004929`, median `0.011557`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.022565`, avg `0.006833`, median `0.010615`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.036604`, avg `0.012263`, median `0.01642`
- 20d: sample `80`, primary_hit `0.225`, primary_closer `0.2875`, primary_mae `0.054519`, avg `0.033075`, median `0.03523`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.065052`, avg `0.067791`, median `0.085394`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.35`, primary_mae `0.021758`, avg `0.004929`, median `0.011557`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.022565`, avg `0.006833`, median `0.010615`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.036604`, avg `0.012263`, median `0.01642`
- 20d: sample `80`, primary_hit `0.225`, primary_closer `0.2875`, primary_mae `0.054519`, avg `0.033075`, median `0.03523`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.065052`, avg `0.067791`, median `0.085394`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.35`, primary_mae `0.021758`, avg `0.004929`, median `0.011557`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.022565`, avg `0.006833`, median `0.010615`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.036604`, avg `0.012263`, median `0.01642`
- 20d: sample `80`, primary_hit `0.225`, primary_closer `0.2875`, primary_mae `0.054519`, avg `0.033075`, median `0.03523`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.065052`, avg `0.067791`, median `0.085394`

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
