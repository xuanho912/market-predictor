# Historical Replay Benchmark

Generated at: `2026-10-31T07:03:08.647469+00:00`
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
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.018737`
- secondary_mean_absolute_error: `0.019589`
- primary_error_advantage: `0.000852`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.024479`
- secondary_mean_absolute_error: `0.019854`
- primary_error_advantage: `-0.004625`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.034677`
- secondary_mean_absolute_error: `0.030281`
- primary_error_advantage: `-0.004396`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.042789`
- secondary_mean_absolute_error: `0.046327`
- primary_error_advantage: `0.003538`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.3625`
- primary_vs_secondary_accuracy_spread: `0.275`
- primary_closer_than_secondary_rate: `0.5875`
- primary_mean_absolute_error: `0.034274`
- secondary_mean_absolute_error: `0.041768`
- primary_error_advantage: `0.007494`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5875`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.016759`, as_primary `0`, as_primary_hit `None`, avg `0.004475`, median `0.004564`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.020341`, as_primary `0`, as_primary_hit `None`, avg `0.009407`, median `0.00829`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.027917`, as_primary `0`, as_primary_hit `None`, avg `0.019762`, median `0.019847`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.031442`, as_primary `0`, as_primary_hit `None`, avg `0.033163`, median `0.041386`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.031555`, as_primary `0`, as_primary_hit `None`, avg `0.049616`, median `0.057725`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.01948`, as_primary `60`, as_primary_hit `0.55`, avg `0.004475`, median `0.004564`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.0266`, as_primary `60`, as_primary_hit `0.5833`, avg `0.009407`, median `0.00829`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.038036`, as_primary `60`, as_primary_hit `0.65`, avg `0.019762`, median `0.019847`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.044249`, as_primary `60`, as_primary_hit `0.7167`, avg `0.033163`, median `0.041386`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.037468`, as_primary `60`, as_primary_hit `0.8167`, avg `0.049616`, median `0.057725`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.020523`, as_primary `20`, as_primary_hit `0.55`, avg `0.004475`, median `0.004564`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.020259`, as_primary `20`, as_primary_hit `0.65`, avg `0.009407`, median `0.00829`
- 10d: sample `80`, direction_hit `0.2875`, path_mae `0.030214`, as_primary `20`, as_primary_hit `0.9`, avg `0.019762`, median `0.019847`
- 20d: sample `80`, direction_hit `0.2125`, path_mae `0.049125`, as_primary `20`, as_primary_hit `1.0`, avg `0.033163`, median `0.041386`
- 60d: sample `80`, direction_hit `0.1625`, path_mae `0.04179`, as_primary `20`, as_primary_hit `0.9`, avg `0.049616`, median `0.057725`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.016459`, as_primary `0`, as_primary_hit `None`, avg `0.004475`, median `0.004564`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.019051`, as_primary `0`, as_primary_hit `None`, avg `0.009407`, median `0.00829`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.023954`, as_primary `0`, as_primary_hit `None`, avg `0.019762`, median `0.019847`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.028915`, as_primary `0`, as_primary_hit `None`, avg `0.033163`, median `0.041386`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.029509`, as_primary `0`, as_primary_hit `None`, avg `0.049616`, median `0.057725`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.018737`, avg `0.004475`, median `0.004564`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.024479`, avg `0.009407`, median `0.00829`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.034677`, avg `0.019762`, median `0.019847`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.042789`, avg `0.033163`, median `0.041386`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.5875`, primary_mae `0.034274`, avg `0.049616`, median `0.057725`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.01463`, avg `0.006388`, median `0.006451`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.01692`, avg `0.014102`, median `0.018469`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.043176`, avg `0.015621`, median `0.01117`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.059265`, avg `0.011344`, median `0.00392`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.049813`, avg `0.017038`, median `0.021062`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.017512`, avg `0.002552`, median `0.002021`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.026246`, avg `0.004981`, median `0.001501`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.037793`, avg `0.011863`, median `0.011777`
- 20d: sample `40`, primary_hit `0.825`, primary_closer `0.55`, primary_mae `0.040424`, avg `0.028995`, median `0.028608`
- 60d: sample `40`, primary_hit `0.9`, primary_closer `0.725`, primary_mae `0.031026`, avg `0.057649`, median `0.064174`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.025294`, avg `0.006408`, median `0.005492`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.028502`, avg `0.013565`, median `0.023423`
- 10d: sample `20`, primary_hit `0.1`, primary_closer `0.55`, primary_mae `0.019945`, avg `0.0397`, median `0.036023`
- 20d: sample `20`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.031042`, avg `0.063319`, median `0.057013`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.5`, primary_mae `0.025229`, avg `0.066127`, median `0.068874`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.01463, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01692, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.019945, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.0, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.031042, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.025229, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016459, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020523, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.01463, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019051, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0266, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01692, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023954, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038036, 'direction_hit_rate': 0.7125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.019945, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028915, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049125, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.0, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.031042, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_vs_secondary_accuracy_spread': 0.275, 'primary_closer_than_secondary_rate': 0.5875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029509, 'direction_hit_rate': 0.8375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04179, 'direction_hit_rate': 0.1625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.025229, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022217`, avg `0.005912`, median `0.001744`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.028658`, avg `0.009411`, median `0.00489`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.033109`, avg `0.021811`, median `0.022448`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.032783`, avg `0.039468`, median `0.031427`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.875`, primary_mae `0.015487`, avg `0.08304`, median `0.08335`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.018724`, avg `0.008362`, median `0.007527`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.028903`, avg `0.008686`, median `0.003837`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.033017`, avg `0.022019`, median `0.022448`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.5`, primary_mae `0.034948`, avg `0.037261`, median `0.029911`
- 60d: sample `16`, primary_hit `1.0`, primary_closer `0.625`, primary_mae `0.022652`, avg `0.072669`, median `0.07382`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.026706`, avg `0.006349`, median `0.006768`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.029279`, avg `0.013491`, median `0.016372`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.625`, primary_mae `0.019249`, avg `0.037845`, median `0.034572`
- 20d: sample `16`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.031638`, avg `0.06351`, median `0.055787`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.026553`, avg `0.063597`, median `0.068874`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.018737`, avg `0.004475`, median `0.004564`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.024479`, avg `0.009407`, median `0.00829`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.034677`, avg `0.019762`, median `0.019847`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.042789`, avg `0.033163`, median `0.041386`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.5875`, primary_mae `0.034274`, avg `0.049616`, median `0.057725`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.018737`, avg `0.004475`, median `0.004564`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.024479`, avg `0.009407`, median `0.00829`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.034677`, avg `0.019762`, median `0.019847`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.042789`, avg `0.033163`, median `0.041386`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.5875`, primary_mae `0.034274`, avg `0.049616`, median `0.057725`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.016551`, avg `0.003831`, median `0.004564`
- 5d: sample `60`, primary_hit `0.5833`, primary_closer `0.4333`, primary_mae `0.023137`, avg `0.008021`, median `0.007096`
- 10d: sample `60`, primary_hit `0.65`, primary_closer `0.4333`, primary_mae `0.039587`, avg `0.013115`, median `0.01117`
- 20d: sample `60`, primary_hit `0.7167`, primary_closer `0.5333`, primary_mae `0.046705`, avg `0.023111`, median `0.028426`
- 60d: sample `60`, primary_hit `0.8167`, primary_closer `0.6167`, primary_mae `0.037288`, avg `0.044112`, median `0.055122`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.025294`, avg `0.006408`, median `0.005492`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.028502`, avg `0.013565`, median `0.023423`
- 10d: sample `20`, primary_hit `0.1`, primary_closer `0.55`, primary_mae `0.019945`, avg `0.0397`, median `0.036023`
- 20d: sample `20`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.031042`, avg `0.063319`, median `0.057013`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.5`, primary_mae `0.025229`, avg `0.066127`, median `0.068874`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.018737`, avg `0.004475`, median `0.004564`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.024479`, avg `0.009407`, median `0.00829`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.034677`, avg `0.019762`, median `0.019847`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.042789`, avg `0.033163`, median `0.041386`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.5875`, primary_mae `0.034274`, avg `0.049616`, median `0.057725`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.018737`, avg `0.004475`, median `0.004564`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.024479`, avg `0.009407`, median `0.00829`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.034677`, avg `0.019762`, median `0.019847`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.042789`, avg `0.033163`, median `0.041386`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.5875`, primary_mae `0.034274`, avg `0.049616`, median `0.057725`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.018737`, avg `0.004475`, median `0.004564`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.024479`, avg `0.009407`, median `0.00829`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.034677`, avg `0.019762`, median `0.019847`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.042789`, avg `0.033163`, median `0.041386`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.5875`, primary_mae `0.034274`, avg `0.049616`, median `0.057725`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
