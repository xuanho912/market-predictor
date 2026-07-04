# Historical Replay Benchmark

Generated at: `2026-07-04T04:56:22.560428+00:00`
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
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.017279`
- secondary_mean_absolute_error: `0.015066`
- primary_error_advantage: `-0.002213`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.021864`
- secondary_mean_absolute_error: `0.018689`
- primary_error_advantage: `-0.003175`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.029338`
- secondary_mean_absolute_error: `0.022775`
- primary_error_advantage: `-0.006563`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.051893`
- secondary_mean_absolute_error: `0.035372`
- primary_error_advantage: `-0.016521`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.073559`
- secondary_mean_absolute_error: `0.065231`
- primary_error_advantage: `-0.008328`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.014862`, as_primary `0`, as_primary_hit `None`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.018416`, as_primary `0`, as_primary_hit `None`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.022127`, as_primary `0`, as_primary_hit `None`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.030581`, as_primary `0`, as_primary_hit `None`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.058801`, as_primary `0`, as_primary_hit `None`, avg `0.038839`, median `0.048732`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.016546`, as_primary `60`, as_primary_hit `0.3833`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.021306`, as_primary `60`, as_primary_hit `0.3667`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.027131`, as_primary `60`, as_primary_hit `0.4833`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.043936`, as_primary `60`, as_primary_hit `0.7`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.073559`, as_primary `60`, as_primary_hit `0.7333`, avg `0.038839`, median `0.048732`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.016769`, as_primary `20`, as_primary_hit `0.4`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.020368`, as_primary `20`, as_primary_hit `0.45`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.029667`, as_primary `20`, as_primary_hit `0.4`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.053345`, as_primary `20`, as_primary_hit `0.7`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.084175`, as_primary `20`, as_primary_hit `0.5`, avg `0.038839`, median `0.048732`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.014481`, as_primary `0`, as_primary_hit `None`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.017637`, as_primary `0`, as_primary_hit `None`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.021166`, as_primary `0`, as_primary_hit `None`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.029755`, as_primary `0`, as_primary_hit `None`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.059052`, as_primary `0`, as_primary_hit `None`, avg `0.038839`, median `0.048732`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.018706`, avg `-0.000949`, median `-0.00397`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.025347`, avg `-0.003689`, median `-0.005247`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.035483`, avg `0.002999`, median `0.001486`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.070265`, avg `0.015748`, median `-0.002157`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.110715`, avg `0.072127`, median `0.072903`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.018052`, avg `-0.001898`, median `-0.001735`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.021716`, avg `-0.006335`, median `-0.012995`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.024101`, avg `0.000976`, median `-0.001153`
- 20d: sample `40`, primary_hit `0.825`, primary_closer `0.275`, primary_mae `0.034066`, avg `0.025005`, median `0.029102`
- 60d: sample `40`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.063994`, avg `0.043066`, median `0.063468`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.014306`, avg `-0.003795`, median `-0.003287`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018676`, avg `-0.005946`, median `-0.005426`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.03367`, avg `-0.00758`, median `-0.007304`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.069176`, avg `-0.003539`, median `0.013848`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.055533`, avg `-0.002904`, median `0.013327`

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
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.014306`, avg `-0.003795`, median `-0.003287`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018676`, avg `-0.005946`, median `-0.005426`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.03367`, avg `-0.00758`, median `-0.007304`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.069176`, avg `-0.003539`, median `0.013848`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.055533`, avg `-0.002904`, median `0.013327`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.3667`, primary_mae `0.01827`, avg `-0.001582`, median `-0.002593`
- 5d: sample `60`, primary_hit `0.3667`, primary_closer `0.3833`, primary_mae `0.022926`, avg `-0.005453`, median `-0.008169`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.35`, primary_mae `0.027895`, avg `0.001651`, median `-0.000741`
- 20d: sample `60`, primary_hit `0.7`, primary_closer `0.3167`, primary_mae `0.046132`, avg `0.02192`, median `0.028709`
- 60d: sample `60`, primary_hit `0.7333`, primary_closer `0.5`, primary_mae `0.079568`, avg `0.052753`, median `0.066423`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014306, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.018676, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.027895, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.046132, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.055533, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014481, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016769, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014306, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017637, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021306, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.018676, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021166, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029667, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.027895, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029755, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053345, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.046132, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058801, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.084175, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.055533, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017848`, avg `0.004016`, median `0.00743`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.013348`, avg `-0.010099`, median `-0.010753`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.009393`, avg `0.003671`, median `-0.001577`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.025541`, avg `0.024906`, median `0.029911`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.625`, primary_mae `0.027814`, avg `0.081857`, median `0.088952`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.015846`, avg `0.0007`, median `-0.001207`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.015974`, avg `-0.010493`, median `-0.010753`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.008243`, avg `0.000345`, median `-0.001836`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.1875`, primary_mae `0.029314`, avg `0.022126`, median `0.028709`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.4375`, primary_mae `0.046363`, avg `0.063823`, median `0.077573`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.014402`, avg `-0.002252`, median `-0.00191`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.018689`, avg `-0.005432`, median `-0.005426`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.034825`, avg `-0.005891`, median `-0.004583`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.06948`, avg `-0.003116`, median `0.01201`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.063997`, avg `-0.014263`, median `-0.037245`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.017279`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.021864`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3625`, primary_mae `0.029338`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.051893`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.073559`, avg `0.038839`, median `0.048732`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.017279`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.021864`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3625`, primary_mae `0.029338`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.051893`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.073559`, avg `0.038839`, median `0.048732`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.3667`, primary_mae `0.01827`, avg `-0.001582`, median `-0.002593`
- 5d: sample `60`, primary_hit `0.3667`, primary_closer `0.3833`, primary_mae `0.022926`, avg `-0.005453`, median `-0.008169`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.35`, primary_mae `0.027895`, avg `0.001651`, median `-0.000741`
- 20d: sample `60`, primary_hit `0.7`, primary_closer `0.3167`, primary_mae `0.046132`, avg `0.02192`, median `0.028709`
- 60d: sample `60`, primary_hit `0.7333`, primary_closer `0.5`, primary_mae `0.079568`, avg `0.052753`, median `0.066423`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.014306`, avg `-0.003795`, median `-0.003287`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018676`, avg `-0.005946`, median `-0.005426`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.03367`, avg `-0.00758`, median `-0.007304`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.069176`, avg `-0.003539`, median `0.013848`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.055533`, avg `-0.002904`, median `0.013327`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.017279`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.021864`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3625`, primary_mae `0.029338`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.051893`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.073559`, avg `0.038839`, median `0.048732`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.017279`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.021864`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3625`, primary_mae `0.029338`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.051893`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.073559`, avg `0.038839`, median `0.048732`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.017279`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.021864`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3625`, primary_mae `0.029338`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.051893`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.073559`, avg `0.038839`, median `0.048732`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
