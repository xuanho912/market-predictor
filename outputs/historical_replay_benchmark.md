# Historical Replay Benchmark

Generated at: `2026-09-24T06:14:47.884276+00:00`
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
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.019919`
- secondary_mean_absolute_error: `0.016343`
- primary_error_advantage: `-0.003576`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.021478`
- secondary_mean_absolute_error: `0.019064`
- primary_error_advantage: `-0.002414`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.030464`
- secondary_mean_absolute_error: `0.026656`
- primary_error_advantage: `-0.003808`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.065651`
- secondary_mean_absolute_error: `0.054919`
- primary_error_advantage: `-0.010732`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.090532`
- secondary_mean_absolute_error: `0.070328`
- primary_error_advantage: `-0.020204`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.01641`, as_primary `0`, as_primary_hit `None`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.017339`, as_primary `0`, as_primary_hit `None`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.022668`, as_primary `0`, as_primary_hit `None`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.038399`, as_primary `0`, as_primary_hit `None`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.058651`, as_primary `0`, as_primary_hit `None`, avg `0.024955`, median `0.041986`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016532`, as_primary `0`, as_primary_hit `None`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.01901`, as_primary `0`, as_primary_hit `None`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.029352`, as_primary `0`, as_primary_hit `None`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.058024`, as_primary `0`, as_primary_hit `None`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.070187`, as_primary `0`, as_primary_hit `None`, avg `0.024955`, median `0.041986`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.019919`, as_primary `80`, as_primary_hit `0.4`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.021478`, as_primary `80`, as_primary_hit `0.4`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.030464`, as_primary `80`, as_primary_hit `0.375`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.4375`, path_mae `0.065651`, as_primary `80`, as_primary_hit `0.5625`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, direction_hit `0.3`, path_mae `0.090532`, as_primary `80`, as_primary_hit `0.7`, avg `0.024955`, median `0.041986`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.015748`, as_primary `0`, as_primary_hit `None`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.01682`, as_primary `0`, as_primary_hit `None`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.022545`, as_primary `0`, as_primary_hit `None`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.038069`, as_primary `0`, as_primary_hit `None`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.057423`, as_primary `0`, as_primary_hit `None`, avg `0.024955`, median `0.041986`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.019919`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.021478`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4125`, primary_mae `0.030464`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.065651`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.090532`, avg `0.024955`, median `0.041986`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.020227`, avg `-0.005058`, median `-0.002723`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.020469`, avg `-0.010773`, median `-0.011804`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.031655`, avg `-0.007266`, median `-0.006704`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.071278`, avg `0.007995`, median `0.011992`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.325`, primary_mae `0.098249`, avg `0.030371`, median `0.043377`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.019612`, avg `-0.007573`, median `-0.009708`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.022487`, avg `-0.011758`, median `-0.015917`
- 10d: sample `40`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.029274`, avg `-0.012603`, median `-0.010944`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.060024`, avg `0.007924`, median `0.016081`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.475`, primary_mae `0.082815`, avg `0.019539`, median `0.033294`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.019612, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.020469, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.029274, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.060024, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.082815, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015748, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019919, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.019612, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01682, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021478, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.020469, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022545, 'direction_hit_rate': 0.375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030464, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.029274, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038069, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065651, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.060024, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057423, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.090532, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.082815, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.01758`, avg `-0.015931`, median `-0.027264`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.024445`, avg `-0.020884`, median `-0.025209`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.025247`, avg `-0.02023`, median `-0.017516`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.083834`, avg `0.003485`, median `0.025462`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.136646`, avg `0.032624`, median `0.059414`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.02205`, avg `-0.009799`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.027854`, avg `-0.013201`, median `-0.017298`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.030437`, avg `-0.015013`, median `-0.012632`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.08165`, avg `0.007716`, median `0.020913`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.124061`, avg `0.029961`, median `0.048285`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.031836`, avg `-0.012758`, median `-0.009555`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.02957`, avg `-0.022185`, median `-0.023937`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.04121`, avg `-0.021101`, median `-0.038715`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.087011`, avg `0.001283`, median `-0.003773`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.151565`, avg `0.045378`, median `0.068156`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.019919`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.021478`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4125`, primary_mae `0.030464`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.065651`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.090532`, avg `0.024955`, median `0.041986`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.019919`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.021478`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4125`, primary_mae `0.030464`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.065651`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.090532`, avg `0.024955`, median `0.041986`

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
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.019919`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.021478`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4125`, primary_mae `0.030464`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.065651`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.090532`, avg `0.024955`, median `0.041986`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.019919`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.021478`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4125`, primary_mae `0.030464`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.065651`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.090532`, avg `0.024955`, median `0.041986`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.019919`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.021478`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.4125`, primary_mae `0.030464`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.065651`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.090532`, avg `0.024955`, median `0.041986`

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
