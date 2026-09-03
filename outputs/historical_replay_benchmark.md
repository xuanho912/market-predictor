# Historical Replay Benchmark

Generated at: `2026-09-03T08:19:41.479561+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
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
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.015971`
- secondary_mean_absolute_error: `0.013059`
- primary_error_advantage: `-0.002912`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.023189`
- secondary_mean_absolute_error: `0.017263`
- primary_error_advantage: `-0.005926`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.032524`
- secondary_mean_absolute_error: `0.023611`
- primary_error_advantage: `-0.008913`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.061436`
- secondary_mean_absolute_error: `0.035246`
- primary_error_advantage: `-0.02619`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.101465`
- secondary_mean_absolute_error: `0.066903`
- primary_error_advantage: `-0.034562`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.013044`, as_primary `0`, as_primary_hit `None`, avg `0.000908`, median `0.000755`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017229`, as_primary `0`, as_primary_hit `None`, avg `-0.000322`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.025145`, as_primary `0`, as_primary_hit `None`, avg `-0.001232`, median `-0.007955`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.03591`, as_primary `0`, as_primary_hit `None`, avg `0.008985`, median `0.017853`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.068919`, as_primary `0`, as_primary_hit `None`, avg `0.030986`, median `0.059722`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.014685`, as_primary `0`, as_primary_hit `None`, avg `0.000908`, median `0.000755`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.018693`, as_primary `0`, as_primary_hit `None`, avg `-0.000322`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.034051`, as_primary `0`, as_primary_hit `None`, avg `-0.001232`, median `-0.007955`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.048719`, as_primary `0`, as_primary_hit `None`, avg `0.008985`, median `0.017853`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.080989`, as_primary `0`, as_primary_hit `None`, avg `0.030986`, median `0.059722`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.015971`, as_primary `80`, as_primary_hit `0.5625`, avg `0.000908`, median `0.000755`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.023189`, as_primary `80`, as_primary_hit `0.5625`, avg `-0.000322`, median `0.001271`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.032524`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.001232`, median `-0.007955`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.061436`, as_primary `80`, as_primary_hit `0.65`, avg `0.008985`, median `0.017853`
- 60d: sample `80`, direction_hit `0.3125`, path_mae `0.101465`, as_primary `80`, as_primary_hit `0.6875`, avg `0.030986`, median `0.059722`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.013059`, as_primary `0`, as_primary_hit `None`, avg `0.000908`, median `0.000755`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017263`, as_primary `0`, as_primary_hit `None`, avg `-0.000322`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.023611`, as_primary `0`, as_primary_hit `None`, avg `-0.001232`, median `-0.007955`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.035246`, as_primary `0`, as_primary_hit `None`, avg `0.008985`, median `0.017853`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.066903`, as_primary `0`, as_primary_hit `None`, avg `0.030986`, median `0.059722`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.015971`, avg `0.000908`, median `0.000755`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.023189`, avg `-0.000322`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.032524`, avg `-0.001232`, median `-0.007955`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.3125`, primary_mae `0.061436`, avg `0.008985`, median `0.017853`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.101465`, avg `0.030986`, median `0.059722`

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
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.012796`, avg `0.000329`, median `0.000609`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.021566`, avg `-7e-05`, median `0.001056`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.325`, primary_mae `0.033657`, avg `-0.007927`, median `-0.011952`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.25`, primary_mae `0.082095`, avg `-0.005687`, median `0.008468`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.325`, primary_mae `0.127799`, avg `-0.002695`, median `0.020967`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.019146`, avg `0.001488`, median `0.003423`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.024813`, avg `-0.000574`, median `0.003026`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.031391`, avg `0.005462`, median `-0.000811`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.040776`, avg `0.023657`, median `0.027304`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.425`, primary_mae `0.075132`, avg `0.064666`, median `0.068732`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.012796, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.021566, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.031391, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.040776, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.075132, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013044, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015971, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.012796, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017229, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023189, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.021566, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023611, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034051, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.031391, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035246, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061436, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.040776, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066903, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.101465, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.075132, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.018008`, avg `-0.009181`, median `-0.005846`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.022742`, avg `-0.013975`, median `-0.014509`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.023269`, avg `-6e-05`, median `-0.003208`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.05827`, avg `0.028723`, median `0.032598`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.130095`, avg `0.078668`, median `0.096964`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.021385`, avg `-0.006244`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.022557`, avg `-0.013523`, median `-0.014548`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.023085`, avg `-7.1e-05`, median `-0.003556`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.049949`, avg `0.024629`, median `0.031427`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.114413`, avg `0.063894`, median `0.088952`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.009988`, avg `-0.003003`, median `-0.001535`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.011027`, avg `-0.006094`, median `-0.000876`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.022627`, avg `-0.006509`, median `-0.009`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.062773`, avg `-0.003557`, median `0.007874`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.083008`, avg `0.024409`, median `0.045303`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.015971`, avg `0.000908`, median `0.000755`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.023189`, avg `-0.000322`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.032524`, avg `-0.001232`, median `-0.007955`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.3125`, primary_mae `0.061436`, avg `0.008985`, median `0.017853`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.101465`, avg `0.030986`, median `0.059722`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.015971`, avg `0.000908`, median `0.000755`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.023189`, avg `-0.000322`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.032524`, avg `-0.001232`, median `-0.007955`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.3125`, primary_mae `0.061436`, avg `0.008985`, median `0.017853`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.101465`, avg `0.030986`, median `0.059722`

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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.4`, primary_mae `0.01566`, avg `-0.000295`, median `0.000402`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.4333`, primary_mae `0.020346`, avg `-0.002071`, median `0.000818`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.3833`, primary_mae `0.027767`, avg `0.001098`, median `-0.006567`
- 20d: sample `60`, primary_hit `0.35`, primary_closer `0.3167`, primary_mae `0.047791`, avg `0.014711`, median `0.019748`
- 60d: sample `60`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.07661`, avg `0.050483`, median `0.062955`

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
