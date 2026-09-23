# Historical Replay Benchmark

Generated at: `2026-09-23T23:03:34.588781+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `PROMISING`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_supportive_but_not_forward_validated`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.019525`
- secondary_mean_absolute_error: `0.016136`
- primary_error_advantage: `-0.003389`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.021775`
- secondary_mean_absolute_error: `0.018712`
- primary_error_advantage: `-0.003063`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.6125`
- primary_mean_absolute_error: `0.027313`
- secondary_mean_absolute_error: `0.032504`
- primary_error_advantage: `0.005191`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.6125`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.060815`
- secondary_mean_absolute_error: `0.06286`
- primary_error_advantage: `0.002045`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.525`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.089523`
- secondary_mean_absolute_error: `0.071196`
- primary_error_advantage: `-0.018327`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.015893`, as_primary `0`, as_primary_hit `None`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.017339`, as_primary `0`, as_primary_hit `None`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.022668`, as_primary `0`, as_primary_hit `None`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.038399`, as_primary `0`, as_primary_hit `None`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.058651`, as_primary `0`, as_primary_hit `None`, avg `0.024955`, median `0.041986`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.0167`, as_primary `40`, as_primary_hit `0.425`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.01901`, as_primary `40`, as_primary_hit `0.425`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.029352`, as_primary `40`, as_primary_hit `0.3`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.058024`, as_primary `40`, as_primary_hit `0.575`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.070187`, as_primary `40`, as_primary_hit `0.65`, avg `0.024955`, median `0.041986`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.018961`, as_primary `40`, as_primary_hit `0.375`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.021478`, as_primary `40`, as_primary_hit `0.375`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.030464`, as_primary `40`, as_primary_hit `0.45`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.4375`, path_mae `0.065651`, as_primary `40`, as_primary_hit `0.55`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, direction_hit `0.3`, path_mae `0.090532`, as_primary `40`, as_primary_hit `0.75`, avg `0.024955`, median `0.041986`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.015567`, as_primary `0`, as_primary_hit `None`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.01682`, as_primary `0`, as_primary_hit `None`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.022545`, as_primary `0`, as_primary_hit `None`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.038069`, as_primary `0`, as_primary_hit `None`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.057423`, as_primary `0`, as_primary_hit `None`, avg `0.024955`, median `0.041986`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.4667`, primary_mae `0.016951`, avg `-0.00412`, median `-0.001442`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.5`, primary_mae `0.018963`, avg `-0.008167`, median `-0.000992`
- 10d: sample `60`, primary_hit `0.3333`, primary_closer `0.6333`, primary_mae `0.022699`, avg `-0.005897`, median `-0.007015`
- 20d: sample `60`, primary_hit `0.5`, primary_closer `0.5167`, primary_mae `0.050228`, avg `0.009363`, median `0.015722`
- 60d: sample `60`, primary_hit `0.5167`, primary_closer `0.5`, primary_mae `0.067104`, avg `0.019239`, median `0.030631`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.027246`, avg `-0.012903`, median `-0.010671`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.030211`, avg `-0.02056`, median `-0.023937`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.041156`, avg `-0.022048`, median `-0.038715`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.092576`, avg `0.003748`, median `-0.000315`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.15678`, avg `0.042104`, median `0.078416`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018194`, avg `-0.003953`, median `0.001086`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022614`, avg `-0.006572`, median `-0.002888`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.025422`, avg `-0.011024`, median `-0.008686`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.03917`, avg `0.0139`, median `0.017343`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.052186`, avg `0.02155`, median `0.037786`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.027246`, avg `-0.012903`, median `-0.010671`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.030211`, avg `-0.02056`, median `-0.023937`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.041156`, avg `-0.022048`, median `-0.038715`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.092576`, avg `0.003748`, median `-0.000315`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.15678`, avg `0.042104`, median `0.078416`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.35`, primary_closer `0.475`, primary_mae `0.01633`, avg `-0.004204`, median `-0.002653`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.017138`, avg `-0.008965`, median `-0.000992`
- 10d: sample `40`, primary_hit `0.3`, primary_closer `0.675`, primary_mae `0.021337`, avg `-0.003333`, median `-0.006203`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.055757`, avg `0.007095`, median `0.014591`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.074563`, avg `0.018083`, median `0.030631`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.01633, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.017138, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.675, 'primary_mean_absolute_error': 0.021337, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.03917, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.052186, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015567, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018961, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.01633, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01682, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021478, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.017138, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.6125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022545, 'direction_hit_rate': 0.375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030464, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.675, 'primary_mean_absolute_error': 0.021337, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038069, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065651, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.03917, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057423, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.090532, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.052186, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.022995`, avg `-0.015931`, median `-0.027264`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.026344`, avg `-0.020884`, median `-0.025209`
- 10d: sample `8`, primary_hit `0.125`, primary_closer `0.625`, primary_mae `0.023994`, avg `-0.02023`, median `-0.017516`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.75`, primary_mae `0.057674`, avg `0.003485`, median `0.025462`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.093267`, avg `0.032624`, median `0.059414`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.019543`, avg `-0.009799`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.020827`, avg `-0.013201`, median `-0.017298`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.75`, primary_mae `0.021503`, avg `-0.015013`, median `-0.012632`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.6875`, primary_mae `0.056346`, avg `0.007716`, median `0.020913`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.097648`, avg `0.029961`, median `0.048285`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.028838`, avg `-0.012758`, median `-0.009555`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.02957`, avg `-0.022185`, median `-0.023937`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.04121`, avg `-0.021101`, median `-0.038715`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.087011`, avg `0.001283`, median `-0.003773`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.151565`, avg `0.045378`, median `0.068156`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.019525`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.021775`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.6125`, primary_mae `0.027313`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.525`, primary_mae `0.060815`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.089523`, avg `0.024955`, median `0.041986`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.019525`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.021775`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.6125`, primary_mae `0.027313`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.525`, primary_mae `0.060815`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.089523`, avg `0.024955`, median `0.041986`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018194`, avg `-0.003953`, median `0.001086`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022614`, avg `-0.006572`, median `-0.002888`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.025422`, avg `-0.011024`, median `-0.008686`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.03917`, avg `0.0139`, median `0.017343`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.052186`, avg `0.02155`, median `0.037786`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.019525`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.021775`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.6125`, primary_mae `0.027313`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.525`, primary_mae `0.060815`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.089523`, avg `0.024955`, median `0.041986`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.019525`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.021775`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.6125`, primary_mae `0.027313`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.525`, primary_mae `0.060815`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.089523`, avg `0.024955`, median `0.041986`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4125`, primary_mae `0.019525`, avg `-0.006316`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.021775`, avg `-0.011265`, median `-0.012577`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.6125`, primary_mae `0.027313`, avg `-0.009935`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.525`, primary_mae `0.060815`, avg `0.007959`, median `0.014286`
- 60d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.089523`, avg `0.024955`, median `0.041986`

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
