# Historical Replay Benchmark

Generated at: `2026-09-23T17:03:15.243268+00:00`
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
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.019576`
- secondary_mean_absolute_error: `0.01609`
- primary_error_advantage: `-0.003486`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.021911`
- secondary_mean_absolute_error: `0.018273`
- primary_error_advantage: `-0.003638`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.029796`
- secondary_mean_absolute_error: `0.030248`
- primary_error_advantage: `0.000452`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.064488`
- secondary_mean_absolute_error: `0.059186`
- primary_error_advantage: `-0.005302`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.089993`
- secondary_mean_absolute_error: `0.069029`
- primary_error_advantage: `-0.020964`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016003`, as_primary `0`, as_primary_hit `None`, avg `-0.006587`, median `-0.003848`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.017048`, as_primary `0`, as_primary_hit `None`, avg `-0.011638`, median `-0.013338`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.022812`, as_primary `0`, as_primary_hit `None`, avg `-0.009892`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.038427`, as_primary `0`, as_primary_hit `None`, avg `0.008367`, median `0.015722`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.057829`, as_primary `0`, as_primary_hit `None`, avg `0.027063`, median `0.043377`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016292`, as_primary `20`, as_primary_hit `0.55`, avg `-0.006587`, median `-0.003848`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.019078`, as_primary `20`, as_primary_hit `0.5`, avg `-0.011638`, median `-0.013338`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.029538`, as_primary `20`, as_primary_hit `0.4`, avg `-0.009892`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.057616`, as_primary `20`, as_primary_hit `0.6`, avg `0.008367`, median `0.015722`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.068079`, as_primary `20`, as_primary_hit `0.7`, avg `0.027063`, median `0.043377`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.019375`, as_primary `60`, as_primary_hit `0.35`, avg `-0.006587`, median `-0.003848`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.021105`, as_primary `60`, as_primary_hit `0.35`, avg `-0.011638`, median `-0.013338`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.030507`, as_primary `60`, as_primary_hit `0.3667`, avg `-0.009892`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.4375`, path_mae `0.066058`, as_primary `60`, as_primary_hit `0.55`, avg `0.008367`, median `0.015722`
- 60d: sample `80`, direction_hit `0.2875`, path_mae `0.090943`, as_primary `60`, as_primary_hit `0.7167`, avg `0.027063`, median `0.043377`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.015419`, as_primary `0`, as_primary_hit `None`, avg `-0.006587`, median `-0.003848`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.016449`, as_primary `0`, as_primary_hit `None`, avg `-0.011638`, median `-0.013338`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.022579`, as_primary `0`, as_primary_hit `None`, avg `-0.009892`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.038423`, as_primary `0`, as_primary_hit `None`, avg `0.008367`, median `0.015722`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.057012`, as_primary `0`, as_primary_hit `None`, avg `0.027063`, median `0.043377`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.019576`, avg `-0.006587`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.45`, primary_mae `0.021911`, avg `-0.011638`, median `-0.013338`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.029796`, avg `-0.009892`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.064488`, avg `0.008367`, median `0.015722`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.089993`, avg `0.027063`, median `0.043377`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.017815`, avg `-0.003953`, median `0.001086`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022614`, avg `-0.006572`, median `-0.002888`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.025422`, avg `-0.011024`, median `-0.008686`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.03917`, avg `0.0139`, median `0.017343`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.052186`, avg `0.02155`, median `0.037786`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.029653`, avg `-0.012903`, median `-0.010671`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.030211`, avg `-0.02056`, median `-0.023937`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.041156`, avg `-0.022048`, median `-0.038715`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.092576`, avg `0.003748`, median `-0.000315`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.156779`, avg `0.042104`, median `0.078416`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.015419`, avg `-0.004746`, median `-0.002653`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.017409`, avg `-0.009711`, median `-0.003`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.026304`, avg `-0.003248`, median `-0.006203`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.063104`, avg `0.007909`, median `0.016386`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.075503`, avg `0.022299`, median `0.034349`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.015419, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.017409, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.025422, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.03917, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.052186, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015419, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019375, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.015419, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016449, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021105, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.017409, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022579, 'direction_hit_rate': 0.375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030507, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.025422, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038423, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066058, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.03917, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057012, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.090943, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.052186, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.017236`, avg `-0.016807`, median `-0.030767`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.025831`, avg `-0.01718`, median `-0.020293`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.028038`, avg `-0.012488`, median `-0.014252`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.094947`, avg `0.014597`, median `0.027639`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.151756`, avg `0.053341`, median `0.065914`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.021676`, avg `-0.009799`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.027854`, avg `-0.013201`, median `-0.017298`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.030437`, avg `-0.015013`, median `-0.012632`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.08165`, avg `0.007716`, median `0.020913`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.124061`, avg `0.029961`, median `0.048285`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.029708`, avg `-0.014145`, median `-0.010671`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.028671`, avg `-0.023084`, median `-0.025058`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.042621`, avg `-0.01969`, median `-0.035238`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.094018`, avg `0.00829`, median `0.012778`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.15619`, avg `0.050003`, median `0.084656`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.019576`, avg `-0.006587`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.45`, primary_mae `0.021911`, avg `-0.011638`, median `-0.013338`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.029796`, avg `-0.009892`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.064488`, avg `0.008367`, median `0.015722`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.089993`, avg `0.027063`, median `0.043377`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.019576`, avg `-0.006587`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.45`, primary_mae `0.021911`, avg `-0.011638`, median `-0.013338`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.029796`, avg `-0.009892`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.064488`, avg `0.008367`, median `0.015722`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.089993`, avg `0.027063`, median `0.043377`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.017815`, avg `-0.003953`, median `0.001086`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022614`, avg `-0.006572`, median `-0.002888`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.025422`, avg `-0.011024`, median `-0.008686`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.03917`, avg `0.0139`, median `0.017343`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.052186`, avg `0.02155`, median `0.037786`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.019576`, avg `-0.006587`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.45`, primary_mae `0.021911`, avg `-0.011638`, median `-0.013338`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.029796`, avg `-0.009892`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.064488`, avg `0.008367`, median `0.015722`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.089993`, avg `0.027063`, median `0.043377`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.019576`, avg `-0.006587`, median `-0.003848`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.45`, primary_mae `0.021911`, avg `-0.011638`, median `-0.013338`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.029796`, avg `-0.009892`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.064488`, avg `0.008367`, median `0.015722`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.089993`, avg `0.027063`, median `0.043377`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.015419`, avg `-0.004746`, median `-0.002653`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.017409`, avg `-0.009711`, median `-0.003`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.026304`, avg `-0.003248`, median `-0.006203`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.063104`, avg `0.007909`, median `0.016386`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.075503`, avg `0.022299`, median `0.034349`

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
