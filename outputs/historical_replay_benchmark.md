# Historical Replay Benchmark

Generated at: `2026-08-14T20:53:51.218325+00:00`
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
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.014919`
- secondary_mean_absolute_error: `0.011983`
- primary_error_advantage: `-0.002936`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.022603`
- secondary_mean_absolute_error: `0.01505`
- primary_error_advantage: `-0.007553`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.034632`
- secondary_mean_absolute_error: `0.023006`
- primary_error_advantage: `-0.011626`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.06755`
- secondary_mean_absolute_error: `0.041754`
- primary_error_advantage: `-0.025796`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.2`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.091662`
- secondary_mean_absolute_error: `0.068404`
- primary_error_advantage: `-0.023258`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.013512`, as_primary `0`, as_primary_hit `None`, avg `0.002496`, median `0.002167`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.017391`, as_primary `0`, as_primary_hit `None`, avg `0.001209`, median `0.002945`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.02445`, as_primary `0`, as_primary_hit `None`, avg `0.004814`, median `0.005827`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.043006`, as_primary `0`, as_primary_hit `None`, avg `0.009223`, median `0.014602`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.069919`, as_primary `0`, as_primary_hit `None`, avg `0.018985`, median `0.028065`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.014919`, as_primary `80`, as_primary_hit `0.575`, avg `0.002496`, median `0.002167`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.022603`, as_primary `80`, as_primary_hit `0.5875`, avg `0.001209`, median `0.002945`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.034632`, as_primary `80`, as_primary_hit `0.5625`, avg `0.004814`, median `0.005827`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.06755`, as_primary `80`, as_primary_hit `0.6375`, avg `0.009223`, median `0.014602`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.091662`, as_primary `80`, as_primary_hit `0.5875`, avg `0.018985`, median `0.028065`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.014593`, as_primary `0`, as_primary_hit `None`, avg `0.002496`, median `0.002167`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.016688`, as_primary `0`, as_primary_hit `None`, avg `0.001209`, median `0.002945`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.031509`, as_primary `0`, as_primary_hit `None`, avg `0.004814`, median `0.005827`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.080908`, as_primary `0`, as_primary_hit `None`, avg `0.009223`, median `0.014602`
- 60d: sample `80`, direction_hit `0.4125`, path_mae `0.091394`, as_primary `0`, as_primary_hit `None`, avg `0.018985`, median `0.028065`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.011983`, as_primary `0`, as_primary_hit `None`, avg `0.002496`, median `0.002167`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.01505`, as_primary `0`, as_primary_hit `None`, avg `0.001209`, median `0.002945`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.023006`, as_primary `0`, as_primary_hit `None`, avg `0.004814`, median `0.005827`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.041754`, as_primary `0`, as_primary_hit `None`, avg `0.009223`, median `0.014602`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.068404`, as_primary `0`, as_primary_hit `None`, avg `0.018985`, median `0.028065`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.013902`, avg `0.002829`, median `0.001882`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.35`, primary_mae `0.022059`, avg `0.001797`, median `0.002174`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.036046`, avg `0.003219`, median `0.003627`
- 20d: sample `40`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.071079`, avg `0.005894`, median `0.012723`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.070617`, avg `0.016682`, median `0.017574`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.015936`, avg `0.002163`, median `0.002167`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.325`, primary_mae `0.023147`, avg `0.000621`, median `0.003203`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.033219`, avg `0.006408`, median `0.006608`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.2`, primary_mae `0.064022`, avg `0.012552`, median `0.024063`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.112707`, avg `0.021288`, median `0.044817`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.013902`, avg `0.002829`, median `0.001882`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.35`, primary_mae `0.022059`, avg `0.001797`, median `0.002174`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.036046`, avg `0.003219`, median `0.003627`
- 20d: sample `40`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.071079`, avg `0.005894`, median `0.012723`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.070617`, avg `0.016682`, median `0.017574`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.015936`, avg `0.002163`, median `0.002167`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.325`, primary_mae `0.023147`, avg `0.000621`, median `0.003203`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.033219`, avg `0.006408`, median `0.006608`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.2`, primary_mae `0.064022`, avg `0.012552`, median `0.024063`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.112707`, avg `0.021288`, median `0.044817`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.013902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022059, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.033219, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.064022, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.070617, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011983, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014919, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.013902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01505, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022603, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022059, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023006, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034632, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.033219, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041754, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.080908, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.064022, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.068404, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.091662, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.070617, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.018711`, avg `-0.001413`, median `0.005338`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.021901`, avg `0.002386`, median `0.004667`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.026517`, avg `0.004849`, median `0.007806`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.064251`, avg `0.003606`, median `0.015956`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.065308`, avg `0.017202`, median `-0.000129`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.019875`, avg `-7e-06`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.025056`, avg `0.003888`, median `0.004667`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.028249`, avg `0.008241`, median `0.011059`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.056904`, avg `0.015398`, median `0.023697`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.074398`, avg `0.012769`, median `0.005143`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.019875`, avg `-7e-06`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.025056`, avg `0.003888`, median `0.004667`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.028249`, avg `0.008241`, median `0.011059`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.056904`, avg `0.015398`, median `0.023697`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.074398`, avg `0.012769`, median `0.005143`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.014919`, avg `0.002496`, median `0.002167`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.3375`, primary_mae `0.022603`, avg `0.001209`, median `0.002945`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.35`, primary_mae `0.034632`, avg `0.004814`, median `0.005827`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.2625`, primary_mae `0.06755`, avg `0.009223`, median `0.014602`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.091662`, avg `0.018985`, median `0.028065`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.014919`, avg `0.002496`, median `0.002167`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.3375`, primary_mae `0.022603`, avg `0.001209`, median `0.002945`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.35`, primary_mae `0.034632`, avg `0.004814`, median `0.005827`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.2625`, primary_mae `0.06755`, avg `0.009223`, median `0.014602`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.091662`, avg `0.018985`, median `0.028065`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.55`, primary_mae `0.014445`, avg `-0.001689`, median `0.000173`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.018529`, avg `0.001572`, median `0.003354`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.024261`, avg `0.001533`, median `0.003463`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.045867`, avg `0.004453`, median `0.012734`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.06728`, avg `0.005486`, median `-0.004015`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.2`, primary_mae `0.017927`, avg `0.009026`, median `0.009151`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.15`, primary_mae `0.032807`, avg `0.002715`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.054689`, avg `0.007718`, median `0.011814`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.10909`, avg `0.015628`, median `0.014591`
- 60d: sample `20`, primary_hit `0.75`, primary_closer `0.35`, primary_mae `0.083129`, avg `0.033762`, median `0.023142`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.014919`, avg `0.002496`, median `0.002167`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.3375`, primary_mae `0.022603`, avg `0.001209`, median `0.002945`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.35`, primary_mae `0.034632`, avg `0.004814`, median `0.005827`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.2625`, primary_mae `0.06755`, avg `0.009223`, median `0.014602`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.091662`, avg `0.018985`, median `0.028065`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.014919`, avg `0.002496`, median `0.002167`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.3375`, primary_mae `0.022603`, avg `0.001209`, median `0.002945`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.35`, primary_mae `0.034632`, avg `0.004814`, median `0.005827`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.2625`, primary_mae `0.06755`, avg `0.009223`, median `0.014602`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.091662`, avg `0.018985`, median `0.028065`

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
