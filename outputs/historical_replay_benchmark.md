# Historical Replay Benchmark

Generated at: `2026-09-18T08:31:31.286534+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.018705`
- secondary_mean_absolute_error: `0.016293`
- primary_error_advantage: `-0.002412`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.019971`
- secondary_mean_absolute_error: `0.016847`
- primary_error_advantage: `-0.003124`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.029318`
- secondary_mean_absolute_error: `0.02244`
- primary_error_advantage: `-0.006878`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.062349`
- secondary_mean_absolute_error: `0.038298`
- primary_error_advantage: `-0.024051`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.425`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.108518`
- secondary_mean_absolute_error: `0.069033`
- primary_error_advantage: `-0.039485`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.016592`, as_primary `0`, as_primary_hit `None`, avg `-0.005773`, median `-0.001727`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.017652`, as_primary `0`, as_primary_hit `None`, avg `-0.008498`, median `-0.005451`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.023239`, as_primary `0`, as_primary_hit `None`, avg `-0.007962`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.038436`, as_primary `0`, as_primary_hit `None`, avg `0.012585`, median `0.015571`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.069095`, as_primary `0`, as_primary_hit `None`, avg `0.039128`, median `0.059055`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.01818`, as_primary `0`, as_primary_hit `None`, avg `-0.005773`, median `-0.001727`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.019431`, as_primary `0`, as_primary_hit `None`, avg `-0.008498`, median `-0.005451`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.031014`, as_primary `0`, as_primary_hit `None`, avg `-0.007962`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.059047`, as_primary `0`, as_primary_hit `None`, avg `0.012585`, median `0.015571`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.084829`, as_primary `0`, as_primary_hit `None`, avg `0.039128`, median `0.059055`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.018705`, as_primary `80`, as_primary_hit `0.45`, avg `-0.005773`, median `-0.001727`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.019971`, as_primary `80`, as_primary_hit `0.45`, avg `-0.008498`, median `-0.005451`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.029318`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.007962`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.425`, path_mae `0.062349`, as_primary `80`, as_primary_hit `0.575`, avg `0.012585`, median `0.015571`
- 60d: sample `80`, direction_hit `0.2875`, path_mae `0.108518`, as_primary `80`, as_primary_hit `0.7125`, avg `0.039128`, median `0.059055`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.016293`, as_primary `0`, as_primary_hit `None`, avg `-0.005773`, median `-0.001727`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.016847`, as_primary `0`, as_primary_hit `None`, avg `-0.008498`, median `-0.005451`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.02244`, as_primary `0`, as_primary_hit `None`, avg `-0.007962`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.038298`, as_primary `0`, as_primary_hit `None`, avg `0.012585`, median `0.015571`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.069033`, as_primary `0`, as_primary_hit `None`, avg `0.039128`, median `0.059055`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018705`, avg `-0.005773`, median `-0.001727`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.019971`, avg `-0.008498`, median `-0.005451`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3125`, primary_mae `0.029318`, avg `-0.007962`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2875`, primary_mae `0.062349`, avg `0.012585`, median `0.015571`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.3125`, primary_mae `0.108518`, avg `0.039128`, median `0.059055`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4`, primary_mae `0.019111`, avg `-0.007908`, median `-0.008756`
- 5d: sample `60`, primary_hit `0.65`, primary_closer `0.3667`, primary_mae `0.021877`, avg `-0.01303`, median `-0.015737`
- 10d: sample `60`, primary_hit `0.7333`, primary_closer `0.3167`, primary_mae `0.026854`, avg `-0.01651`, median `-0.015453`
- 20d: sample `60`, primary_hit `0.5`, primary_closer `0.2667`, primary_mae `0.067667`, avg `0.004859`, median `-0.000119`
- 60d: sample `60`, primary_hit `0.3333`, primary_closer `0.3333`, primary_mae `0.110991`, avg `0.02463`, median `0.052147`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.6`, primary_mae `0.017488`, avg `0.000631`, median `0.008116`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.014253`, avg `0.005097`, median `0.00616`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.03671`, avg `0.017679`, median `0.019802`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.35`, primary_mae `0.046396`, avg `0.035765`, median `0.046433`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.101098`, avg `0.082621`, median `0.1008`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.017488, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014253, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7333, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.026854, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.046396, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.101098, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016293, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018705, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.017488, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016847, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019971, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014253, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02244, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031014, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7333, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.026854, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038298, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062349, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.046396, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.425, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069033, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.108518, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.101098, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.020303`, avg `0.003571`, median `0.011398`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.016641`, avg `0.009276`, median `0.011486`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.041207`, avg `0.021851`, median `0.019234`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.043025`, avg `0.034503`, median `0.035195`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.094513`, avg `0.085544`, median `0.085373`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.75`, primary_mae `0.013848`, avg `0.00523`, median `0.010341`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.014864`, avg `0.00699`, median `0.006622`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.035796`, avg `0.018279`, median `0.01895`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.375`, primary_mae `0.040684`, avg `0.032162`, median `0.03088`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.088919`, avg `0.080476`, median `0.085373`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.022152`, avg `-0.012498`, median `-0.010671`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.023625`, avg `-0.022573`, median `-0.023989`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.03399`, avg `-0.026967`, median `-0.037662`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.088417`, avg `-0.003438`, median `-0.017251`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.16717`, avg `0.016334`, median `0.061566`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018705`, avg `-0.005773`, median `-0.001727`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.019971`, avg `-0.008498`, median `-0.005451`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3125`, primary_mae `0.029318`, avg `-0.007962`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2875`, primary_mae `0.062349`, avg `0.012585`, median `0.015571`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.3125`, primary_mae `0.108518`, avg `0.039128`, median `0.059055`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018705`, avg `-0.005773`, median `-0.001727`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.019971`, avg `-0.008498`, median `-0.005451`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3125`, primary_mae `0.029318`, avg `-0.007962`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2875`, primary_mae `0.062349`, avg `0.012585`, median `0.015571`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.3125`, primary_mae `0.108518`, avg `0.039128`, median `0.059055`

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
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018705`, avg `-0.005773`, median `-0.001727`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.019971`, avg `-0.008498`, median `-0.005451`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3125`, primary_mae `0.029318`, avg `-0.007962`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2875`, primary_mae `0.062349`, avg `0.012585`, median `0.015571`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.3125`, primary_mae `0.108518`, avg `0.039128`, median `0.059055`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018705`, avg `-0.005773`, median `-0.001727`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.019971`, avg `-0.008498`, median `-0.005451`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3125`, primary_mae `0.029318`, avg `-0.007962`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2875`, primary_mae `0.062349`, avg `0.012585`, median `0.015571`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.3125`, primary_mae `0.108518`, avg `0.039128`, median `0.059055`

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
