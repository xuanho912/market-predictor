# Historical Replay Benchmark

Generated at: `2026-09-02T08:10:01.531909+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_mixed_or_not_better_keep_confidence_capped`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.020028`
- secondary_mean_absolute_error: `0.014665`
- primary_error_advantage: `-0.005363`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.020897`
- secondary_mean_absolute_error: `0.01675`
- primary_error_advantage: `-0.004147`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.026008`
- secondary_mean_absolute_error: `0.027107`
- primary_error_advantage: `0.001099`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5125`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.045687`
- secondary_mean_absolute_error: `0.046877`
- primary_error_advantage: `0.00119`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.525`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.074094`
- secondary_mean_absolute_error: `0.068565`
- primary_error_advantage: `-0.005529`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.015686`, as_primary `0`, as_primary_hit `None`, avg `0.001048`, median `0.000878`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.016664`, as_primary `0`, as_primary_hit `None`, avg `-0.00011`, median `0.001499`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.023127`, as_primary `0`, as_primary_hit `None`, avg `-0.001293`, median `-0.007787`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.032541`, as_primary `0`, as_primary_hit `None`, avg `0.01296`, median `0.01374`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.057466`, as_primary `0`, as_primary_hit `None`, avg `0.04386`, median `0.05856`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.016409`, as_primary `20`, as_primary_hit `0.45`, avg `0.001048`, median `0.000878`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017645`, as_primary `20`, as_primary_hit `0.55`, avg `-0.00011`, median `0.001499`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.029853`, as_primary `20`, as_primary_hit `0.45`, avg `-0.001293`, median `-0.007787`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.046192`, as_primary `20`, as_primary_hit `0.6`, avg `0.01296`, median `0.01374`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.067766`, as_primary `20`, as_primary_hit `0.65`, avg `0.04386`, median `0.05856`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.018414`, as_primary `60`, as_primary_hit `0.5833`, avg `0.001048`, median `0.000878`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.020366`, as_primary `60`, as_primary_hit `0.5667`, avg `-0.00011`, median `0.001499`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.026966`, as_primary `60`, as_primary_hit `0.3833`, avg `-0.001293`, median `-0.007787`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.051212`, as_primary `60`, as_primary_hit `0.6167`, avg `0.01296`, median `0.01374`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.08214`, as_primary `60`, as_primary_hit `0.8`, avg `0.04386`, median `0.05856`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.014523`, as_primary `0`, as_primary_hit `None`, avg `0.001048`, median `0.000878`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.016488`, as_primary `0`, as_primary_hit `None`, avg `-0.00011`, median `0.001499`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.022075`, as_primary `0`, as_primary_hit `None`, avg `-0.001293`, median `-0.007787`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.031267`, as_primary `0`, as_primary_hit `None`, avg `0.01296`, median `0.01374`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.05485`, as_primary `0`, as_primary_hit `None`, avg `0.04386`, median `0.05856`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3`, primary_mae `0.020028`, avg `0.001048`, median `0.000878`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.375`, primary_mae `0.020897`, avg `-0.00011`, median `0.001499`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.5125`, primary_mae `0.026008`, avg `-0.001293`, median `-0.007787`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.525`, primary_mae `0.045687`, avg `0.01296`, median `0.01374`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.074094`, avg `0.04386`, median `0.05856`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3`, primary_mae `0.020028`, avg `0.001048`, median `0.000878`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.375`, primary_mae `0.020897`, avg `-0.00011`, median `0.001499`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.5125`, primary_mae `0.026008`, avg `-0.001293`, median `-0.007787`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.525`, primary_mae `0.045687`, avg `0.01296`, median `0.01374`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.074094`, avg `0.04386`, median `0.05856`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.020028, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4625, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.020897, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.026008, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.045687, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3125, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.074094, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014523, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018414, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.020028, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016488, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020366, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4625, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.020897, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022075, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029853, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.026008, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031267, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051212, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.045687, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05485, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.08214, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3125, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.074094, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.022308`, avg `-0.004172`, median `-0.000127`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.019939`, avg `-0.012244`, median `-0.014548`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.025393`, avg `0.007921`, median `0.013417`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.060192`, avg `0.033913`, median `0.031427`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.125`, primary_mae `0.135631`, avg `0.086159`, median `0.093846`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.020559`, avg `-0.007939`, median `-0.007945`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.021775`, avg `-0.014123`, median `-0.014548`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.020388`, avg `-9.8e-05`, median `-0.003556`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.051688`, avg `0.020911`, median `0.031427`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.108348`, avg `0.056407`, median `0.088952`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.021657`, avg `0.005645`, median `0.009121`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.023513`, avg `0.005222`, median `0.000837`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.034544`, avg `0.006252`, median `-0.006998`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.031807`, avg `0.021423`, median `0.018905`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.625`, primary_mae `0.046509`, avg `0.068224`, median `0.058973`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3`, primary_mae `0.020028`, avg `0.001048`, median `0.000878`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.375`, primary_mae `0.020897`, avg `-0.00011`, median `0.001499`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.5125`, primary_mae `0.026008`, avg `-0.001293`, median `-0.007787`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.525`, primary_mae `0.045687`, avg `0.01296`, median `0.01374`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.074094`, avg `0.04386`, median `0.05856`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3`, primary_mae `0.020028`, avg `0.001048`, median `0.000878`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.375`, primary_mae `0.020897`, avg `-0.00011`, median `0.001499`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.5125`, primary_mae `0.026008`, avg `-0.001293`, median `-0.007787`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.525`, primary_mae `0.045687`, avg `0.01296`, median `0.01374`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.074094`, avg `0.04386`, median `0.05856`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.275`, primary_mae `0.019751`, avg `-0.003028`, median `-0.001735`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.019085`, avg `-0.008062`, median `-0.003439`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.019756`, avg `-0.003768`, median `-0.007304`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.046353`, avg `0.010519`, median `0.020543`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.072301`, avg `0.038885`, median `0.060495`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.021631`, avg `-0.000925`, median `-0.001735`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.023636`, avg `-0.003528`, median `-0.005336`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.026197`, avg `0.00157`, median `-0.005954`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.040194`, avg `0.020198`, median `0.024365`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.45`, primary_mae `0.071833`, avg `0.060041`, median `0.064505`

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
