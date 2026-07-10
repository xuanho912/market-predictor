# Historical Replay Benchmark

Generated at: `2026-07-10T15:04:45.078437+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.012482`
- secondary_mean_absolute_error: `0.011627`
- primary_error_advantage: `-0.000855`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.016352`
- secondary_mean_absolute_error: `0.015324`
- primary_error_advantage: `-0.001028`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.026961`
- secondary_mean_absolute_error: `0.02138`
- primary_error_advantage: `-0.005581`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.049282`
- secondary_mean_absolute_error: `0.047233`
- primary_error_advantage: `-0.002049`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.070146`
- secondary_mean_absolute_error: `0.060482`
- primary_error_advantage: `-0.009664`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.012322`, as_primary `0`, as_primary_hit `None`, avg `-0.002031`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.015574`, as_primary `0`, as_primary_hit `None`, avg `-0.002878`, median `0.000837`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.020191`, as_primary `0`, as_primary_hit `None`, avg `3.6e-05`, median `0.001302`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.035892`, as_primary `0`, as_primary_hit `None`, avg `0.001253`, median `0.010449`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.054`, as_primary `0`, as_primary_hit `None`, avg `0.007096`, median `0.012182`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.012482`, as_primary `80`, as_primary_hit `0.5`, avg `-0.002031`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.016352`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.002878`, median `0.000837`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.026961`, as_primary `80`, as_primary_hit `0.5125`, avg `3.6e-05`, median `0.001302`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.049282`, as_primary `80`, as_primary_hit `0.675`, avg `0.001253`, median `0.010449`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.070146`, as_primary `80`, as_primary_hit `0.525`, avg `0.007096`, median `0.012182`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.012487`, as_primary `0`, as_primary_hit `None`, avg `-0.002031`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.016798`, as_primary `0`, as_primary_hit `None`, avg `-0.002878`, median `0.000837`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.024089`, as_primary `0`, as_primary_hit `None`, avg `3.6e-05`, median `0.001302`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.067603`, as_primary `0`, as_primary_hit `None`, avg `0.001253`, median `0.010449`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.080208`, as_primary `0`, as_primary_hit `None`, avg `0.007096`, median `0.012182`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.011621`, as_primary `0`, as_primary_hit `None`, avg `-0.002031`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.015271`, as_primary `0`, as_primary_hit `None`, avg `-0.002878`, median `0.000837`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.01934`, as_primary `0`, as_primary_hit `None`, avg `3.6e-05`, median `0.001302`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.032986`, as_primary `0`, as_primary_hit `None`, avg `0.001253`, median `0.010449`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.054794`, as_primary `0`, as_primary_hit `None`, avg `0.007096`, median `0.012182`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.010858`, avg `-0.001284`, median `-0.00051`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.01501`, avg `-0.002672`, median `0.001977`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.026841`, avg `-0.00217`, median `0.003376`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.043614`, avg `-0.004007`, median `0.011504`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.061516`, avg `-0.010945`, median `-0.011052`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.014106`, avg `-0.002777`, median `0.000565`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.017694`, avg `-0.003085`, median `-0.000454`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.3`, primary_mae `0.027081`, avg `0.002241`, median `-0.001735`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.05495`, avg `0.006513`, median `0.009961`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.35`, primary_mae `0.078775`, avg `0.025137`, median `0.045588`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.010858`, avg `-0.001284`, median `-0.00051`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.01501`, avg `-0.002672`, median `0.001977`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.026841`, avg `-0.00217`, median `0.003376`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.043614`, avg `-0.004007`, median `0.011504`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.061516`, avg `-0.010945`, median `-0.011052`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.014106`, avg `-0.002777`, median `0.000565`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.017694`, avg `-0.003085`, median `-0.000454`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.3`, primary_mae `0.027081`, avg `0.002241`, median `-0.001735`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.05495`, avg `0.006513`, median `0.009961`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.35`, primary_mae `0.078775`, avg `0.025137`, median `0.045588`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.010858, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.01501, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.026841, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.043614, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.061516, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011621, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012487, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.010858, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015271, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016798, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.01501, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01934, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026961, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.026841, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032986, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067603, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.043614, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.080208, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.061516, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017505`, avg `-0.011085`, median `-0.004864`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.016921`, avg `-0.01495`, median `-0.012112`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.02058`, avg `-0.012357`, median `-0.019121`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.041013`, avg `0.008856`, median `0.013447`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.062837`, avg `0.034648`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.015569`, avg `-0.009929`, median `-0.005521`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.017887`, avg `-0.010261`, median `-0.004713`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.017528`, avg `-0.009044`, median `-0.016124`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.049273`, avg `0.001662`, median `0.016513`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.091118`, avg `0.007502`, median `0.003555`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.015569`, avg `-0.009929`, median `-0.005521`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.017887`, avg `-0.010261`, median `-0.004713`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.017528`, avg `-0.009044`, median `-0.016124`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.049273`, avg `0.001662`, median `0.016513`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.091118`, avg `0.007502`, median `0.003555`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.012482`, avg `-0.002031`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.016352`, avg `-0.002878`, median `0.000837`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3875`, primary_mae `0.026961`, avg `3.6e-05`, median `0.001302`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4`, primary_mae `0.049282`, avg `0.001253`, median `0.010449`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.070146`, avg `0.007096`, median `0.012182`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.012482`, avg `-0.002031`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.016352`, avg `-0.002878`, median `0.000837`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3875`, primary_mae `0.026961`, avg `3.6e-05`, median `0.001302`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4`, primary_mae `0.049282`, avg `0.001253`, median `0.010449`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.070146`, avg `0.007096`, median `0.012182`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.4333`, primary_mae `0.012548`, avg `-0.00388`, median `-0.001412`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.4833`, primary_mae `0.015702`, avg `-0.00514`, median `-0.002161`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.4333`, primary_mae `0.023431`, avg `-0.004008`, median `-0.002374`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.4667`, primary_mae `0.045067`, avg `-0.000874`, median `0.01201`
- 60d: sample `60`, primary_hit `0.4667`, primary_closer `0.4167`, primary_mae `0.069711`, avg `-0.001817`, median `-0.00576`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.013409`, avg `-0.001278`, median `-0.001059`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.019074`, avg `-0.004147`, median `-0.005921`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.04004`, avg `-0.008707`, median `-0.012374`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.75`, primary_mae `0.063019`, avg `-0.018299`, median `0.003211`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.065232`, avg `-0.006916`, median `-0.007976`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.012482`, avg `-0.002031`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.016352`, avg `-0.002878`, median `0.000837`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3875`, primary_mae `0.026961`, avg `3.6e-05`, median `0.001302`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4`, primary_mae `0.049282`, avg `0.001253`, median `0.010449`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.070146`, avg `0.007096`, median `0.012182`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.012482`, avg `-0.002031`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.016352`, avg `-0.002878`, median `0.000837`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3875`, primary_mae `0.026961`, avg `3.6e-05`, median `0.001302`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4`, primary_mae `0.049282`, avg `0.001253`, median `0.010449`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.070146`, avg `0.007096`, median `0.012182`

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
