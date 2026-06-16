# Historical Replay Benchmark

Generated at: `2026-06-16T14:42:24.997340+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'high', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay', 'forward validation completed samples are below the minimum gate'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.015083`
- secondary_mean_absolute_error: `0.013663`
- primary_error_advantage: `-0.00142`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.020807`
- secondary_mean_absolute_error: `0.017431`
- primary_error_advantage: `-0.003376`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.029747`
- secondary_mean_absolute_error: `0.02659`
- primary_error_advantage: `-0.003157`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.050432`
- secondary_mean_absolute_error: `0.044184`
- primary_error_advantage: `-0.006248`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.073082`
- secondary_mean_absolute_error: `0.060013`
- primary_error_advantage: `-0.013069`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.014184`, as_primary `0`, as_primary_hit `None`, avg `0.004683`, median `0.005077`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.017673`, as_primary `0`, as_primary_hit `None`, avg `0.00603`, median `0.005601`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.02291`, as_primary `0`, as_primary_hit `None`, avg `0.007406`, median `0.008315`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.033998`, as_primary `0`, as_primary_hit `None`, avg `0.009061`, median `0.017134`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.055977`, as_primary `0`, as_primary_hit `None`, avg `0.02811`, median `0.032906`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.015083`, as_primary `80`, as_primary_hit `0.625`, avg `0.004683`, median `0.005077`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.020807`, as_primary `80`, as_primary_hit `0.6375`, avg `0.00603`, median `0.005601`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.029747`, as_primary `80`, as_primary_hit `0.6`, avg `0.007406`, median `0.008315`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.050432`, as_primary `80`, as_primary_hit `0.6875`, avg `0.009061`, median `0.017134`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.073082`, as_primary `80`, as_primary_hit `0.6125`, avg `0.02811`, median `0.032906`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.014357`, as_primary `0`, as_primary_hit `None`, avg `0.004683`, median `0.005077`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.01822`, as_primary `0`, as_primary_hit `None`, avg `0.00603`, median `0.005601`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.029091`, as_primary `0`, as_primary_hit `None`, avg `0.007406`, median `0.008315`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.061575`, as_primary `0`, as_primary_hit `None`, avg `0.009061`, median `0.017134`
- 60d: sample `80`, direction_hit `0.3875`, path_mae `0.070977`, as_primary `0`, as_primary_hit `None`, avg `0.02811`, median `0.032906`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.013064`, as_primary `0`, as_primary_hit `None`, avg `0.004683`, median `0.005077`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.016393`, as_primary `0`, as_primary_hit `None`, avg `0.00603`, median `0.005601`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.021974`, as_primary `0`, as_primary_hit `None`, avg `0.007406`, median `0.008315`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.031491`, as_primary `0`, as_primary_hit `None`, avg `0.009061`, median `0.017134`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.052699`, as_primary `0`, as_primary_hit `None`, avg `0.02811`, median `0.032906`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4125`, primary_mae `0.015083`, avg `0.004683`, median `0.005077`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.375`, primary_mae `0.020807`, avg `0.00603`, median `0.005601`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.029747`, avg `0.007406`, median `0.008315`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.050432`, avg `0.009061`, median `0.017134`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.073082`, avg `0.02811`, median `0.032906`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.014114`, avg `0.006082`, median `0.005077`
- 5d: sample `40`, primary_hit `0.75`, primary_closer `0.425`, primary_mae `0.018406`, avg `0.009155`, median `0.008615`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.55`, primary_mae `0.028876`, avg `0.005751`, median `0.008571`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.053453`, avg `0.001044`, median `0.01201`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.072387`, avg `0.008442`, median `0.000394`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.016052`, avg `0.003283`, median `0.005335`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.325`, primary_mae `0.023208`, avg `0.002905`, median `0.001516`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.030618`, avg `0.009061`, median `0.008315`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.25`, primary_mae `0.047411`, avg `0.017079`, median `0.020209`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.35`, primary_mae `0.073777`, avg `0.047778`, median `0.059526`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014114, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018406, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.028876, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.047411, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.072387, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013064, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015083, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014114, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016393, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020807, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018406, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021974, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029747, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.028876, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031491, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061575, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.047411, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052699, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073082, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.072387, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.015062`, avg `-0.007736`, median `-0.006939`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.020282`, avg `-0.011553`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.015164`, avg `0.005967`, median `0.006918`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.0`, primary_mae `0.020335`, avg `0.027023`, median `0.028979`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.042038`, avg `0.04658`, median `0.055714`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.015814`, avg `-0.004727`, median `-0.006094`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.019545`, avg `-0.007672`, median `-0.010372`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.014904`, avg `0.007218`, median `0.006918`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.125`, primary_mae `0.029148`, avg `0.019289`, median `0.024685`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.055827`, avg `0.035914`, median `0.055714`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.015814`, avg `-0.004727`, median `-0.006094`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.019545`, avg `-0.007672`, median `-0.010372`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.014904`, avg `0.007218`, median `0.006918`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.125`, primary_mae `0.029148`, avg `0.019289`, median `0.024685`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.055827`, avg `0.035914`, median `0.055714`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4125`, primary_mae `0.015083`, avg `0.004683`, median `0.005077`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.375`, primary_mae `0.020807`, avg `0.00603`, median `0.005601`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.029747`, avg `0.007406`, median `0.008315`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.050432`, avg `0.009061`, median `0.017134`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.073082`, avg `0.02811`, median `0.032906`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4125`, primary_mae `0.015083`, avg `0.004683`, median `0.005077`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.375`, primary_mae `0.020807`, avg `0.00603`, median `0.005601`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.029747`, avg `0.007406`, median `0.008315`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.050432`, avg `0.009061`, median `0.017134`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.073082`, avg `0.02811`, median `0.032906`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4125`, primary_mae `0.015083`, avg `0.004683`, median `0.005077`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.375`, primary_mae `0.020807`, avg `0.00603`, median `0.005601`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.029747`, avg `0.007406`, median `0.008315`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.050432`, avg `0.009061`, median `0.017134`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.073082`, avg `0.02811`, median `0.032906`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4125`, primary_mae `0.015083`, avg `0.004683`, median `0.005077`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.375`, primary_mae `0.020807`, avg `0.00603`, median `0.005601`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.029747`, avg `0.007406`, median `0.008315`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.050432`, avg `0.009061`, median `0.017134`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.073082`, avg `0.02811`, median `0.032906`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4125`, primary_mae `0.015083`, avg `0.004683`, median `0.005077`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.375`, primary_mae `0.020807`, avg `0.00603`, median `0.005601`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.029747`, avg `0.007406`, median `0.008315`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.050432`, avg `0.009061`, median `0.017134`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.073082`, avg `0.02811`, median `0.032906`

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
