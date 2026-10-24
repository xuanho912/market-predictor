# Historical Replay Benchmark

Generated at: `2026-10-24T01:22:37.297710+00:00`
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
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.022642`
- secondary_mean_absolute_error: `0.022648`
- primary_error_advantage: `6e-06`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.029271`
- secondary_mean_absolute_error: `0.030656`
- primary_error_advantage: `0.001385`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.047524`
- secondary_mean_absolute_error: `0.047241`
- primary_error_advantage: `-0.000283`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.7`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.064773`
- secondary_mean_absolute_error: `0.054755`
- primary_error_advantage: `-0.010018`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.75`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1625`
- secondary_hit_rate: `0.8375`
- primary_vs_secondary_accuracy_spread: `-0.675`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.055894`
- secondary_mean_absolute_error: `0.060038`
- primary_error_advantage: `0.004144`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.019552`, as_primary `0`, as_primary_hit `None`, avg `0.001628`, median `0.00282`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.026135`, as_primary `0`, as_primary_hit `None`, avg `-0.000572`, median `0.001372`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.038137`, as_primary `0`, as_primary_hit `None`, avg `-0.005028`, median `-0.007307`
- 20d: sample `80`, direction_hit `0.45`, path_mae `0.041137`, as_primary `0`, as_primary_hit `None`, avg `-0.009621`, median `-0.014419`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.050365`, as_primary `0`, as_primary_hit `None`, avg `0.066698`, median `0.065811`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.023593`, as_primary `0`, as_primary_hit `None`, avg `0.001628`, median `0.00282`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.030666`, as_primary `0`, as_primary_hit `None`, avg `-0.000572`, median `0.001372`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.049902`, as_primary `0`, as_primary_hit `None`, avg `-0.005028`, median `-0.007307`
- 20d: sample `80`, direction_hit `0.45`, path_mae `0.061639`, as_primary `0`, as_primary_hit `None`, avg `-0.009621`, median `-0.014419`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.060021`, as_primary `0`, as_primary_hit `None`, avg `0.066698`, median `0.065811`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.022642`, as_primary `80`, as_primary_hit `0.55`, avg `0.001628`, median `0.00282`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.029271`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.000572`, median `0.001372`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.047524`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.005028`, median `-0.007307`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.064773`, as_primary `80`, as_primary_hit `0.45`, avg `-0.009621`, median `-0.014419`
- 60d: sample `80`, direction_hit `0.1625`, path_mae `0.055894`, as_primary `80`, as_primary_hit `0.8375`, avg `0.066698`, median `0.065811`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.019364`, as_primary `0`, as_primary_hit `None`, avg `0.001628`, median `0.00282`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.025622`, as_primary `0`, as_primary_hit `None`, avg `-0.000572`, median `0.001372`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.036694`, as_primary `0`, as_primary_hit `None`, avg `-0.005028`, median `-0.007307`
- 20d: sample `80`, direction_hit `0.45`, path_mae `0.039027`, as_primary `0`, as_primary_hit `None`, avg `-0.009621`, median `-0.014419`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.048857`, as_primary `0`, as_primary_hit `None`, avg `0.066698`, median `0.065811`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.022642`, avg `0.001628`, median `0.00282`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4875`, primary_mae `0.029271`, avg `-0.000572`, median `0.001372`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.5`, primary_mae `0.047524`, avg `-0.005028`, median `-0.007307`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.064773`, avg `-0.009621`, median `-0.014419`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.55`, primary_mae `0.055894`, avg `0.066698`, median `0.065811`

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
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.023341`, avg `0.001502`, median `0.003856`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.029946`, avg `-0.001013`, median `0.002693`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.5`, primary_mae `0.044679`, avg `-0.001689`, median `-0.002501`
- 20d: sample `60`, primary_hit `0.5667`, primary_closer `0.4833`, primary_mae `0.061174`, avg `-0.008121`, median `-0.017646`
- 60d: sample `60`, primary_hit `0.1167`, primary_closer `0.5667`, primary_mae `0.045267`, avg `0.068819`, median `0.064669`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.020543`, avg `0.002005`, median `0.002066`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.027246`, avg `0.00075`, median `-0.002987`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.056058`, avg `-0.015047`, median `-0.018027`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.075569`, avg `-0.014121`, median `0.000884`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.087774`, avg `0.060337`, median `0.084728`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.020543, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.027246, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.044679, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.061174, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1167, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.045267, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019364, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023593, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.020543, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025622, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030666, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.027246, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036694, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049902, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.044679, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039027, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064773, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.061174, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1625, 'secondary_hit_rate': 0.8375, 'primary_vs_secondary_accuracy_spread': -0.675, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048857, 'direction_hit_rate': 0.8375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060021, 'direction_hit_rate': 0.8375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1167, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.045267, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.012894`, avg `-0.006152`, median `-0.010431`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.013298`, avg `-0.010653`, median `-0.015512`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.016915`, avg `-0.033235`, median `-0.04277`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.033126`, avg `-0.041288`, median `-0.045815`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.875`, primary_mae `0.032842`, avg `0.025079`, median `0.034011`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.6875`, primary_mae `0.013899`, avg `-0.000435`, median `-0.00419`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.018856`, avg `-0.004799`, median `-0.011914`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.030111`, avg `-0.018975`, median `-0.035039`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.050465`, avg `-0.022647`, median `-0.025949`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.6875`, primary_mae `0.03951`, avg `0.023626`, median `0.034011`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.030882`, avg `-0.003919`, median `0.004933`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.040075`, avg `-0.005634`, median `0.00779`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.046073`, avg `0.007866`, median `0.009633`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.04711`, avg `0.001527`, median `-0.000982`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.4375`, primary_mae `0.06614`, avg `0.11494`, median `0.125416`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.022642`, avg `0.001628`, median `0.00282`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4875`, primary_mae `0.029271`, avg `-0.000572`, median `0.001372`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.5`, primary_mae `0.047524`, avg `-0.005028`, median `-0.007307`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.064773`, avg `-0.009621`, median `-0.014419`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.55`, primary_mae `0.055894`, avg `0.066698`, median `0.065811`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.022642`, avg `0.001628`, median `0.00282`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4875`, primary_mae `0.029271`, avg `-0.000572`, median `0.001372`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.5`, primary_mae `0.047524`, avg `-0.005028`, median `-0.007307`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.064773`, avg `-0.009621`, median `-0.014419`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.55`, primary_mae `0.055894`, avg `0.066698`, median `0.065811`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.5167`, primary_mae `0.019148`, avg `0.00175`, median `0.001618`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.5333`, primary_mae `0.02474`, avg `-0.000183`, median `-0.002987`
- 10d: sample `60`, primary_hit `0.6167`, primary_closer `0.5667`, primary_mae `0.047169`, avg `-0.010189`, median `-0.018027`
- 20d: sample `60`, primary_hit `0.5833`, primary_closer `0.55`, primary_mae `0.069879`, avg `-0.014195`, median `-0.023458`
- 60d: sample `60`, primary_hit `0.2167`, primary_closer `0.6`, primary_mae `0.053645`, avg `0.05132`, median `0.056969`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.2`, primary_mae `0.033122`, avg `0.001261`, median `0.007933`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.042865`, avg `-0.001741`, median `0.007804`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.048588`, avg `0.010453`, median `0.010405`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.25`, primary_mae `0.049454`, avg `0.004101`, median `0.001969`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.4`, primary_mae `0.062641`, avg `0.112833`, median `0.120274`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.022642`, avg `0.001628`, median `0.00282`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4875`, primary_mae `0.029271`, avg `-0.000572`, median `0.001372`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.5`, primary_mae `0.047524`, avg `-0.005028`, median `-0.007307`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.064773`, avg `-0.009621`, median `-0.014419`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.55`, primary_mae `0.055894`, avg `0.066698`, median `0.065811`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.022642`, avg `0.001628`, median `0.00282`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4875`, primary_mae `0.029271`, avg `-0.000572`, median `0.001372`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.5`, primary_mae `0.047524`, avg `-0.005028`, median `-0.007307`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.064773`, avg `-0.009621`, median `-0.014419`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.55`, primary_mae `0.055894`, avg `0.066698`, median `0.065811`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.022642`, avg `0.001628`, median `0.00282`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4875`, primary_mae `0.029271`, avg `-0.000572`, median `0.001372`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.5`, primary_mae `0.047524`, avg `-0.005028`, median `-0.007307`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.064773`, avg `-0.009621`, median `-0.014419`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.55`, primary_mae `0.055894`, avg `0.066698`, median `0.065811`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.022642`, avg `0.001628`, median `0.00282`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4875`, primary_mae `0.029271`, avg `-0.000572`, median `0.001372`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.5`, primary_mae `0.047524`, avg `-0.005028`, median `-0.007307`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.064773`, avg `-0.009621`, median `-0.014419`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.55`, primary_mae `0.055894`, avg `0.066698`, median `0.065811`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
