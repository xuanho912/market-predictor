# Historical Replay Benchmark

Generated at: `2026-10-09T10:57:28.868706+00:00`
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
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.35`
- primary_vs_secondary_accuracy_spread: `0.3`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.019115`
- secondary_mean_absolute_error: `0.016494`
- primary_error_advantage: `-0.002621`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.024473`
- secondary_mean_absolute_error: `0.019629`
- primary_error_advantage: `-0.004844`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.035523`
- secondary_mean_absolute_error: `0.027552`
- primary_error_advantage: `-0.007971`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.076998`
- secondary_mean_absolute_error: `0.050446`
- primary_error_advantage: `-0.026552`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.25`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.5`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.077376`
- secondary_mean_absolute_error: `0.066193`
- primary_error_advantage: `-0.011183`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.35`, path_mae `0.015698`, as_primary `0`, as_primary_hit `None`, avg `-0.0068`, median `-0.004464`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.01788`, as_primary `0`, as_primary_hit `None`, avg `-0.010753`, median `-0.013233`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.027023`, as_primary `0`, as_primary_hit `None`, avg `-0.009802`, median `-0.006976`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.042297`, as_primary `0`, as_primary_hit `None`, avg `0.008729`, median `0.015722`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.055681`, as_primary `0`, as_primary_hit `None`, avg `0.030688`, median `0.04627`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.35`, path_mae `0.016549`, as_primary `0`, as_primary_hit `None`, avg `-0.0068`, median `-0.004464`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.019391`, as_primary `0`, as_primary_hit `None`, avg `-0.010753`, median `-0.013233`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.034142`, as_primary `0`, as_primary_hit `None`, avg `-0.009802`, median `-0.006976`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.060469`, as_primary `0`, as_primary_hit `None`, avg `0.008729`, median `0.015722`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.069163`, as_primary `0`, as_primary_hit `None`, avg `0.030688`, median `0.04627`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.019115`, as_primary `80`, as_primary_hit `0.35`, avg `-0.0068`, median `-0.004464`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.024473`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.010753`, median `-0.013233`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.035523`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.009802`, median `-0.006976`
- 20d: sample `80`, direction_hit `0.425`, path_mae `0.076998`, as_primary `80`, as_primary_hit `0.575`, avg `0.008729`, median `0.015722`
- 60d: sample `80`, direction_hit `0.25`, path_mae `0.077376`, as_primary `80`, as_primary_hit `0.75`, avg `0.030688`, median `0.04627`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.35`, path_mae `0.015039`, as_primary `0`, as_primary_hit `None`, avg `-0.0068`, median `-0.004464`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.017691`, as_primary `0`, as_primary_hit `None`, avg `-0.010753`, median `-0.013233`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.025946`, as_primary `0`, as_primary_hit `None`, avg `-0.009802`, median `-0.006976`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.042558`, as_primary `0`, as_primary_hit `None`, avg `0.008729`, median `0.015722`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.059083`, as_primary `0`, as_primary_hit `None`, avg `0.030688`, median `0.04627`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.019115`, avg `-0.0068`, median `-0.004464`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.024473`, avg `-0.010753`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.035523`, avg `-0.009802`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.076998`, avg `0.008729`, median `0.015722`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.077376`, avg `0.030688`, median `0.04627`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.019115`, avg `-0.0068`, median `-0.004464`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.024473`, avg `-0.010753`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.035523`, avg `-0.009802`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.076998`, avg `0.008729`, median `0.015722`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.077376`, avg `0.030688`, median `0.04627`

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

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.019115, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5875, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.024473, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5625, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.035523, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.076998, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.077376, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.35, 'primary_vs_secondary_accuracy_spread': 0.3, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015039, 'direction_hit_rate': 0.35}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019115, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.019115, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017691, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024473, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5875, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.024473, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025946, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035523, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5625, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.035523, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042297, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076998, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.076998, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.5, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055681, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.077376, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.077376, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.018292`, avg `-0.016625`, median `-0.030767`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.031799`, avg `-0.014933`, median `-0.020293`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.038026`, avg `-0.010376`, median `-0.014252`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.09393`, avg `0.007481`, median `0.023936`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.134084`, avg `0.018653`, median `0.052632`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.021221`, avg `-0.011103`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.034425`, avg `-0.013262`, median `-0.019358`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.039086`, avg `-0.012807`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.083668`, avg `0.00176`, median `0.009104`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.120425`, avg `-0.01037`, median `0.041779`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.125`, primary_mae `0.028451`, avg `-0.010673`, median `-0.010671`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.025279`, avg `-0.018244`, median `-0.022951`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.039665`, avg `-0.012731`, median `-0.029899`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.091779`, avg `0.022627`, median `0.019624`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.073587`, avg `0.074214`, median `0.085768`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.019115`, avg `-0.0068`, median `-0.004464`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.024473`, avg `-0.010753`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.035523`, avg `-0.009802`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.076998`, avg `0.008729`, median `0.015722`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.077376`, avg `0.030688`, median `0.04627`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.019115`, avg `-0.0068`, median `-0.004464`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.024473`, avg `-0.010753`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.035523`, avg `-0.009802`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.076998`, avg `0.008729`, median `0.015722`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.077376`, avg `0.030688`, median `0.04627`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.021209`, avg `-0.009733`, median `-0.010538`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.034394`, avg `-0.012103`, median `-0.018412`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.3`, primary_mae `0.0375`, avg `-0.015491`, median `-0.012632`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.083699`, avg `0.001066`, median `0.009104`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.122591`, avg `-0.000463`, median `0.045479`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.019006`, avg `-0.006047`, median `-0.003848`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.019512`, avg `-0.011173`, median `-0.011804`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.033644`, avg `-0.00581`, median `-0.005578`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.25`, primary_mae `0.082888`, avg `0.012421`, median `0.014591`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.070694`, avg `0.04438`, median `0.046053`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.019115`, avg `-0.0068`, median `-0.004464`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.024473`, avg `-0.010753`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.035523`, avg `-0.009802`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.076998`, avg `0.008729`, median `0.015722`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.077376`, avg `0.030688`, median `0.04627`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.019115`, avg `-0.0068`, median `-0.004464`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.024473`, avg `-0.010753`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.035523`, avg `-0.009802`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.076998`, avg `0.008729`, median `0.015722`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.077376`, avg `0.030688`, median `0.04627`

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
