# Historical Replay Benchmark

Generated at: `2026-06-15T14:29:14.648819+00:00`
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
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.014707`
- secondary_mean_absolute_error: `0.013541`
- primary_error_advantage: `-0.001166`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.019961`
- secondary_mean_absolute_error: `0.017782`
- primary_error_advantage: `-0.002179`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.028524`
- secondary_mean_absolute_error: `0.026302`
- primary_error_advantage: `-0.002222`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.7`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.052272`
- secondary_mean_absolute_error: `0.045929`
- primary_error_advantage: `-0.006343`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.07492`
- secondary_mean_absolute_error: `0.061282`
- primary_error_advantage: `-0.013638`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.013933`, as_primary `0`, as_primary_hit `None`, avg `0.004936`, median `0.005843`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.01842`, as_primary `0`, as_primary_hit `None`, avg `0.005659`, median `0.005601`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.023148`, as_primary `0`, as_primary_hit `None`, avg `0.007758`, median `0.007534`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.034935`, as_primary `0`, as_primary_hit `None`, avg `0.010917`, median `0.017745`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.05777`, as_primary `0`, as_primary_hit `None`, avg `0.029015`, median `0.033835`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.014707`, as_primary `80`, as_primary_hit `0.6375`, avg `0.004936`, median `0.005843`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.019961`, as_primary `80`, as_primary_hit `0.6375`, avg `0.005659`, median `0.005601`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.028524`, as_primary `80`, as_primary_hit `0.6`, avg `0.007758`, median `0.007534`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.052272`, as_primary `80`, as_primary_hit `0.7`, avg `0.010917`, median `0.017745`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.07492`, as_primary `80`, as_primary_hit `0.5875`, avg `0.029015`, median `0.033835`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.01405`, as_primary `0`, as_primary_hit `None`, avg `0.004936`, median `0.005843`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.018533`, as_primary `0`, as_primary_hit `None`, avg `0.005659`, median `0.005601`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.028923`, as_primary `0`, as_primary_hit `None`, avg `0.007758`, median `0.007534`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.06343`, as_primary `0`, as_primary_hit `None`, avg `0.010917`, median `0.017745`
- 60d: sample `80`, direction_hit `0.4125`, path_mae `0.071882`, as_primary `0`, as_primary_hit `None`, avg `0.029015`, median `0.033835`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.012982`, as_primary `0`, as_primary_hit `None`, avg `0.004936`, median `0.005843`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.016953`, as_primary `0`, as_primary_hit `None`, avg `0.005659`, median `0.005601`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.02233`, as_primary `0`, as_primary_hit `None`, avg `0.007758`, median `0.007534`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.032984`, as_primary `0`, as_primary_hit `None`, avg `0.010917`, median `0.017745`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.054331`, as_primary `0`, as_primary_hit `None`, avg `0.029015`, median `0.033835`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.475`, primary_mae `0.014707`, avg `0.004936`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.019961`, avg `0.005659`, median `0.005601`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.028524`, avg `0.007758`, median `0.007534`
- 20d: sample `80`, primary_hit `0.7`, primary_closer `0.3625`, primary_mae `0.052272`, avg `0.010917`, median `0.017745`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.07492`, avg `0.029015`, median `0.033835`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.55`, primary_mae `0.014822`, avg `0.006685`, median `0.00609`
- 5d: sample `40`, primary_hit `0.75`, primary_closer `0.525`, primary_mae `0.017862`, avg `0.008257`, median `0.008615`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.525`, primary_mae `0.026032`, avg `0.005138`, median `0.00719`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.054626`, avg `0.002509`, median `0.01201`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.080115`, avg `0.010788`, median `-0.00576`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.014593`, avg `0.003186`, median `0.00509`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.022059`, avg `0.003061`, median `0.001516`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.031017`, avg `0.010377`, median `0.008315`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.225`, primary_mae `0.049918`, avg `0.019324`, median `0.021541`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.375`, primary_mae `0.069726`, avg `0.047242`, median `0.053882`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014593, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.017862, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.026032, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.049918, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.069726, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012982, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014707, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014593, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016953, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019961, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.017862, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02233, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028923, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.026032, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032984, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06343, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.049918, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054331, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07492, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.069726, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.01568`, avg `-0.007791`, median `-0.007158`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.023023`, avg `-0.011833`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.01504`, avg `0.008706`, median `0.006918`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.0`, primary_mae `0.022072`, avg `0.028852`, median `0.030181`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.032369`, avg `0.054535`, median `0.055714`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.015095`, avg `-0.003602`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.019535`, avg `-0.006022`, median `-0.008992`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.014823`, avg `0.009391`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.1875`, primary_mae `0.029008`, avg `0.022579`, median `0.028979`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.051161`, avg `0.036809`, median `0.04041`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.015095`, avg `-0.003602`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.019535`, avg `-0.006022`, median `-0.008992`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.014823`, avg `0.009391`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.1875`, primary_mae `0.029008`, avg `0.022579`, median `0.028979`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.051161`, avg `0.036809`, median `0.04041`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.475`, primary_mae `0.014707`, avg `0.004936`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.019961`, avg `0.005659`, median `0.005601`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.028524`, avg `0.007758`, median `0.007534`
- 20d: sample `80`, primary_hit `0.7`, primary_closer `0.3625`, primary_mae `0.052272`, avg `0.010917`, median `0.017745`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.07492`, avg `0.029015`, median `0.033835`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.475`, primary_mae `0.014707`, avg `0.004936`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.019961`, avg `0.005659`, median `0.005601`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.028524`, avg `0.007758`, median `0.007534`
- 20d: sample `80`, primary_hit `0.7`, primary_closer `0.3625`, primary_mae `0.052272`, avg `0.010917`, median `0.017745`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.07492`, avg `0.029015`, median `0.033835`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.475`, primary_mae `0.014707`, avg `0.004936`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.019961`, avg `0.005659`, median `0.005601`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.028524`, avg `0.007758`, median `0.007534`
- 20d: sample `80`, primary_hit `0.7`, primary_closer `0.3625`, primary_mae `0.052272`, avg `0.010917`, median `0.017745`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.07492`, avg `0.029015`, median `0.033835`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.475`, primary_mae `0.014707`, avg `0.004936`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.019961`, avg `0.005659`, median `0.005601`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.028524`, avg `0.007758`, median `0.007534`
- 20d: sample `80`, primary_hit `0.7`, primary_closer `0.3625`, primary_mae `0.052272`, avg `0.010917`, median `0.017745`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.07492`, avg `0.029015`, median `0.033835`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.475`, primary_mae `0.014707`, avg `0.004936`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.019961`, avg `0.005659`, median `0.005601`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.028524`, avg `0.007758`, median `0.007534`
- 20d: sample `80`, primary_hit `0.7`, primary_closer `0.3625`, primary_mae `0.052272`, avg `0.010917`, median `0.017745`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.07492`, avg `0.029015`, median `0.033835`

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
