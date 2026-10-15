# Historical Replay Benchmark

Generated at: `2026-10-15T17:05:08.455793+00:00`
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
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.016206`
- secondary_mean_absolute_error: `0.016421`
- primary_error_advantage: `0.000215`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.01971`
- secondary_mean_absolute_error: `0.018445`
- primary_error_advantage: `-0.001265`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.022511`
- secondary_mean_absolute_error: `0.024056`
- primary_error_advantage: `0.001545`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.047577`
- secondary_mean_absolute_error: `0.035858`
- primary_error_advantage: `-0.011719`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.225`
- secondary_hit_rate: `0.775`
- primary_vs_secondary_accuracy_spread: `-0.55`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.076622`
- secondary_mean_absolute_error: `0.058294`
- primary_error_advantage: `-0.018328`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015106`, as_primary `0`, as_primary_hit `None`, avg `-0.007324`, median `-0.006795`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.017429`, as_primary `0`, as_primary_hit `None`, avg `-0.008857`, median `-0.011865`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.023332`, as_primary `0`, as_primary_hit `None`, avg `-0.007669`, median `-0.010013`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.03156`, as_primary `0`, as_primary_hit `None`, avg `0.016844`, median `0.018851`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.054945`, as_primary `0`, as_primary_hit `None`, avg `0.055422`, median `0.061815`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.016365`, as_primary `0`, as_primary_hit `None`, avg `-0.007324`, median `-0.006795`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.020395`, as_primary `0`, as_primary_hit `None`, avg `-0.008857`, median `-0.011865`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.029962`, as_primary `0`, as_primary_hit `None`, avg `-0.007669`, median `-0.010013`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.045742`, as_primary `0`, as_primary_hit `None`, avg `0.016844`, median `0.018851`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.065854`, as_primary `0`, as_primary_hit `None`, avg `0.055422`, median `0.061815`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.016206`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.007324`, median `-0.006795`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.01971`, as_primary `80`, as_primary_hit `0.4`, avg `-0.008857`, median `-0.011865`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.022511`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.007669`, median `-0.010013`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.047577`, as_primary `80`, as_primary_hit `0.6125`, avg `0.016844`, median `0.018851`
- 60d: sample `80`, direction_hit `0.225`, path_mae `0.076622`, as_primary `80`, as_primary_hit `0.775`, avg `0.055422`, median `0.061815`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015005`, as_primary `0`, as_primary_hit `None`, avg `-0.007324`, median `-0.006795`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.016969`, as_primary `0`, as_primary_hit `None`, avg `-0.008857`, median `-0.011865`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.02137`, as_primary `0`, as_primary_hit `None`, avg `-0.007669`, median `-0.010013`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.030085`, as_primary `0`, as_primary_hit `None`, avg `0.016844`, median `0.018851`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.054195`, as_primary `0`, as_primary_hit `None`, avg `0.055422`, median `0.061815`

## Edge Status Performance

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.425`, primary_mae `0.016071`, avg `-0.008494`, median `-0.011593`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.019652`, avg `-0.009782`, median `-0.013608`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.475`, primary_mae `0.024963`, avg `-0.012118`, median `-0.015501`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.052914`, avg `0.01562`, median `0.015118`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.075272`, avg `0.072205`, median `0.078416`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.016341`, avg `-0.006154`, median `-0.000519`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.019769`, avg `-0.007931`, median `-0.0084`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.575`, primary_mae `0.020058`, avg `-0.00322`, median `-0.005954`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.425`, primary_mae `0.042241`, avg `0.018069`, median `0.020992`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.077972`, avg `0.038638`, median `0.058364`

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
- 3d: sample `20`, primary_hit `0.8`, primary_closer `0.4`, primary_mae `0.014002`, avg `-0.009627`, median `-0.00934`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.35`, primary_mae `0.020978`, avg `-0.014655`, median `-0.021206`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.5`, primary_mae `0.029823`, avg `-0.022722`, median `-0.036035`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.065752`, avg `0.00909`, median `-0.000315`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.2`, primary_mae `0.074084`, avg `0.074088`, median `0.086161`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.01227`, avg `-0.003122`, median `0.001086`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.014703`, avg `-0.004238`, median `-0.002888`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.019594`, avg `-0.001521`, median `-0.003558`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.031287`, avg `0.01514`, median `0.017343`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.04647`, avg `0.029024`, median `0.050131`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.019276`, avg `-0.008274`, median `-0.010064`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.021581`, avg `-0.008267`, median `-0.006883`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.020313`, avg `-0.003217`, median `-0.005954`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.046636`, avg `0.021573`, median `0.023936`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.092967`, avg `0.059287`, median `0.066096`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.01227, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014703, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.019594, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.031287, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.04647, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015005, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016365, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.01227, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016969, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020395, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014703, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02137, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029962, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.019594, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030085, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.047577, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.031287, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.225, 'secondary_hit_rate': 0.775, 'primary_vs_secondary_accuracy_spread': -0.55, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054195, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076622, 'direction_hit_rate': 0.225}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.04647, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.009668`, avg `-0.002903`, median `0.001086`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.014843`, avg `-0.006121`, median `-0.002888`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.012124`, avg `-0.006253`, median `-0.003647`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.029055`, avg `0.014079`, median `0.008728`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.040455`, avg `0.021077`, median `0.041509`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.013497`, avg `-0.002985`, median `0.001086`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.016106`, avg `-0.004803`, median `-0.002888`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.017098`, avg `-0.000765`, median `-0.003558`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.033235`, avg `0.01844`, median `0.019748`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.4375`, primary_mae `0.043595`, avg `0.031769`, median `0.050131`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.011759`, avg `-0.01301`, median `-0.011593`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.017763`, avg `-0.018879`, median `-0.021206`
- 10d: sample `16`, primary_hit `0.875`, primary_closer `0.5625`, primary_mae `0.023841`, avg `-0.029614`, median `-0.037567`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.060333`, avg `0.005967`, median `-0.003631`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.072757`, avg `0.069601`, median `0.079581`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.016206`, avg `-0.007324`, median `-0.006795`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.01971`, avg `-0.008857`, median `-0.011865`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.022511`, avg `-0.007669`, median `-0.010013`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.375`, primary_mae `0.047577`, avg `0.016844`, median `0.018851`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.076622`, avg `0.055422`, median `0.061815`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.016206`, avg `-0.007324`, median `-0.006795`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.01971`, avg `-0.008857`, median `-0.011865`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.022511`, avg `-0.007669`, median `-0.010013`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.375`, primary_mae `0.047577`, avg `0.016844`, median `0.018851`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.076622`, avg `0.055422`, median `0.061815`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.016341`, avg `-0.006154`, median `-0.000519`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.019769`, avg `-0.007931`, median `-0.0084`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.575`, primary_mae `0.020058`, avg `-0.00322`, median `-0.005954`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.425`, primary_mae `0.042241`, avg `0.018069`, median `0.020992`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.077972`, avg `0.038638`, median `0.058364`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.425`, primary_mae `0.016071`, avg `-0.008494`, median `-0.011593`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.019652`, avg `-0.009782`, median `-0.013608`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.475`, primary_mae `0.024963`, avg `-0.012118`, median `-0.015501`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.052914`, avg `0.01562`, median `0.015118`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.075272`, avg `0.072205`, median `0.078416`

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
