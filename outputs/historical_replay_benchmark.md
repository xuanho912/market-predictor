# Historical Replay Benchmark

Generated at: `2026-10-04T16:53:22.151445+00:00`
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
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.01787`
- secondary_mean_absolute_error: `0.015375`
- primary_error_advantage: `-0.002495`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.023461`
- secondary_mean_absolute_error: `0.01743`
- primary_error_advantage: `-0.006031`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.039901`
- secondary_mean_absolute_error: `0.028328`
- primary_error_advantage: `-0.011573`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.070463`
- secondary_mean_absolute_error: `0.043253`
- primary_error_advantage: `-0.02721`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.15`
- secondary_hit_rate: `0.85`
- primary_vs_secondary_accuracy_spread: `-0.7`
- primary_closer_than_secondary_rate: `0.225`
- primary_mean_absolute_error: `0.081388`
- secondary_mean_absolute_error: `0.046116`
- primary_error_advantage: `-0.035272`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.015622`, as_primary `0`, as_primary_hit `None`, avg `-0.00448`, median `-0.003446`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.017744`, as_primary `0`, as_primary_hit `None`, avg `-0.005432`, median `-0.002857`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.029146`, as_primary `0`, as_primary_hit `None`, avg `-0.005318`, median `-1e-06`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.038928`, as_primary `0`, as_primary_hit `None`, avg `0.008373`, median `0.015722`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.047328`, as_primary `0`, as_primary_hit `None`, avg `0.053333`, median `0.058305`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.015424`, as_primary `0`, as_primary_hit `None`, avg `-0.00448`, median `-0.003446`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.017827`, as_primary `0`, as_primary_hit `None`, avg `-0.005432`, median `-0.002857`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.033938`, as_primary `0`, as_primary_hit `None`, avg `-0.005318`, median `-1e-06`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.058359`, as_primary `0`, as_primary_hit `None`, avg `0.008373`, median `0.015722`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.049228`, as_primary `0`, as_primary_hit `None`, avg `0.053333`, median `0.058305`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.01787`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.00448`, median `-0.003446`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.023461`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.005432`, median `-0.002857`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.039901`, as_primary `80`, as_primary_hit `0.5`, avg `-0.005318`, median `-1e-06`
- 20d: sample `80`, direction_hit `0.4`, path_mae `0.070463`, as_primary `80`, as_primary_hit `0.6`, avg `0.008373`, median `0.015722`
- 60d: sample `80`, direction_hit `0.15`, path_mae `0.081388`, as_primary `80`, as_primary_hit `0.85`, avg `0.053333`, median `0.058305`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.015338`, as_primary `0`, as_primary_hit `None`, avg `-0.00448`, median `-0.003446`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.017155`, as_primary `0`, as_primary_hit `None`, avg `-0.005432`, median `-0.002857`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.028162`, as_primary `0`, as_primary_hit `None`, avg `-0.005318`, median `-1e-06`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.039408`, as_primary `0`, as_primary_hit `None`, avg `0.008373`, median `0.015722`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.046161`, as_primary `0`, as_primary_hit `None`, avg `0.053333`, median `0.058305`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.01822`, avg `0.001608`, median `0.005108`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.025253`, avg `-0.00183`, median `0.005583`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.040806`, avg `-0.009391`, median `0.002106`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.053367`, avg `0.007271`, median `0.010261`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.35`, primary_mae `0.056006`, avg `0.058708`, median `0.064839`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4167`, primary_mae `0.017754`, avg `-0.00651`, median `-0.004217`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.3`, primary_mae `0.022864`, avg `-0.006632`, median `-0.004447`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.35`, primary_mae `0.039599`, avg `-0.00396`, median `-0.002583`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.25`, primary_mae `0.076162`, avg `0.00874`, median `0.016386`
- 60d: sample `60`, primary_hit `0.1667`, primary_closer `0.1833`, primary_mae `0.089849`, avg `0.051542`, median `0.056634`

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
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.01787`, avg `-0.00448`, median `-0.003446`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3375`, primary_mae `0.023461`, avg `-0.005432`, median `-0.002857`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.039901`, avg `-0.005318`, median `-1e-06`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.070463`, avg `0.008373`, median `0.015722`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.225`, primary_mae `0.081388`, avg `0.053333`, median `0.058305`

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

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5625, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.01787, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5375, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.023461, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.039901, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.070463, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.081388, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015338, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01787, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5625, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.01787, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017155, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023461, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5375, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.023461, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028162, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039901, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.039901, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038928, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070463, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.070463, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.15, 'secondary_hit_rate': 0.85, 'primary_vs_secondary_accuracy_spread': -0.7, 'primary_closer_than_secondary_rate': 0.225, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.046161, 'direction_hit_rate': 0.85}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.081388, 'direction_hit_rate': 0.15}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.081388, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.019066`, avg `0.011601`, median `0.012351`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.032678`, avg `0.008475`, median `0.007597`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.051108`, avg `0.006179`, median `0.009685`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.065716`, avg `0.022474`, median `0.023484`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.05145`, avg `0.068211`, median `0.07166`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.019702`, avg `0.00695`, median `0.012351`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.029295`, avg `0.004711`, median `0.007597`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.047392`, avg `0.002341`, median `0.005974`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.060203`, avg `0.016961`, median `0.017343`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.3125`, primary_mae `0.052334`, avg `0.072689`, median `0.075105`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.024697`, avg `-0.008383`, median `-0.00992`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.032518`, avg `-0.016152`, median `-0.013247`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.042052`, avg `-0.017378`, median `-0.015452`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.079606`, avg `-0.005479`, median `0.00754`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.139281`, avg `0.038135`, median `0.054785`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.01787`, avg `-0.00448`, median `-0.003446`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3375`, primary_mae `0.023461`, avg `-0.005432`, median `-0.002857`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.039901`, avg `-0.005318`, median `-1e-06`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.070463`, avg `0.008373`, median `0.015722`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.225`, primary_mae `0.081388`, avg `0.053333`, median `0.058305`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.01787`, avg `-0.00448`, median `-0.003446`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3375`, primary_mae `0.023461`, avg `-0.005432`, median `-0.002857`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.039901`, avg `-0.005318`, median `-1e-06`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.070463`, avg `0.008373`, median `0.015722`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.225`, primary_mae `0.081388`, avg `0.053333`, median `0.058305`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.01822`, avg `0.001608`, median `0.005108`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.025253`, avg `-0.00183`, median `0.005583`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.040806`, avg `-0.009391`, median `0.002106`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.053367`, avg `0.007271`, median `0.010261`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.35`, primary_mae `0.056006`, avg `0.058708`, median `0.064839`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4167`, primary_mae `0.017754`, avg `-0.00651`, median `-0.004217`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.3`, primary_mae `0.022864`, avg `-0.006632`, median `-0.004447`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.35`, primary_mae `0.039599`, avg `-0.00396`, median `-0.002583`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.25`, primary_mae `0.076162`, avg `0.00874`, median `0.016386`
- 60d: sample `60`, primary_hit `0.1667`, primary_closer `0.1833`, primary_mae `0.089849`, avg `0.051542`, median `0.056634`

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
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.01787`, avg `-0.00448`, median `-0.003446`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3375`, primary_mae `0.023461`, avg `-0.005432`, median `-0.002857`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.039901`, avg `-0.005318`, median `-1e-06`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.070463`, avg `0.008373`, median `0.015722`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.225`, primary_mae `0.081388`, avg `0.053333`, median `0.058305`

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
