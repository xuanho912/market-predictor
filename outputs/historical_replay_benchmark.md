# Historical Replay Benchmark

Generated at: `2026-09-03T16:28:30.087692+00:00`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.017723`
- secondary_mean_absolute_error: `0.014457`
- primary_error_advantage: `-0.003266`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.020407`
- secondary_mean_absolute_error: `0.016614`
- primary_error_advantage: `-0.003793`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.027019`
- secondary_mean_absolute_error: `0.02076`
- primary_error_advantage: `-0.006259`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.049972`
- secondary_mean_absolute_error: `0.028276`
- primary_error_advantage: `-0.021696`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.067506`
- secondary_mean_absolute_error: `0.048562`
- primary_error_advantage: `-0.018944`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014681`, as_primary `0`, as_primary_hit `None`, avg `-0.00011`, median `0.000609`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.017065`, as_primary `0`, as_primary_hit `None`, avg `0.001808`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.022008`, as_primary `0`, as_primary_hit `None`, avg `-0.001015`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.028677`, as_primary `0`, as_primary_hit `None`, avg `0.005439`, median `0.013418`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.048472`, as_primary `0`, as_primary_hit `None`, avg `0.029985`, median `0.044873`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.015099`, as_primary `0`, as_primary_hit `None`, avg `-0.00011`, median `0.000609`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.017834`, as_primary `0`, as_primary_hit `None`, avg `0.001808`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.030405`, as_primary `0`, as_primary_hit `None`, avg `-0.001015`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.043224`, as_primary `0`, as_primary_hit `None`, avg `0.005439`, median `0.013418`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.056521`, as_primary `0`, as_primary_hit `None`, avg `0.029985`, median `0.044873`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.017723`, as_primary `80`, as_primary_hit `0.525`, avg `-0.00011`, median `0.000609`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.020407`, as_primary `80`, as_primary_hit `0.575`, avg `0.001808`, median `0.001271`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.027019`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.001015`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.049972`, as_primary `80`, as_primary_hit `0.6125`, avg `0.005439`, median `0.013418`
- 60d: sample `80`, direction_hit `0.3`, path_mae `0.067506`, as_primary `80`, as_primary_hit `0.7`, avg `0.029985`, median `0.044873`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014457`, as_primary `0`, as_primary_hit `None`, avg `-0.00011`, median `0.000609`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.016614`, as_primary `0`, as_primary_hit `None`, avg `0.001808`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.02076`, as_primary `0`, as_primary_hit `None`, avg `-0.001015`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.028276`, as_primary `0`, as_primary_hit `None`, avg `0.005439`, median `0.013418`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.048562`, as_primary `0`, as_primary_hit `None`, avg `0.029985`, median `0.044873`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.017723`, avg `-0.00011`, median `0.000609`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.020407`, avg `0.001808`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.027019`, avg `-0.001015`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.049972`, avg `0.005439`, median `0.013418`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.067506`, avg `0.029985`, median `0.044873`

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
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.010713`, avg `-0.003162`, median `-0.001535`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.015238`, avg `-0.001804`, median `0.000818`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.019444`, avg `-0.014486`, median `-0.01712`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.058812`, avg `-0.027969`, median `-0.020035`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.060696`, avg `-0.016448`, median `-0.028583`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.3833`, primary_mae `0.020059`, avg `0.000908`, median `0.002082`
- 5d: sample `60`, primary_hit `0.4333`, primary_closer `0.4`, primary_mae `0.02213`, avg `0.003012`, median `0.003417`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.3833`, primary_mae `0.029544`, avg `0.003476`, median `0.000128`
- 20d: sample `60`, primary_hit `0.2667`, primary_closer `0.3`, primary_mae `0.047026`, avg `0.016575`, median `0.024711`
- 60d: sample `60`, primary_hit `0.1667`, primary_closer `0.3`, primary_mae `0.069776`, avg `0.045463`, median `0.060651`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.010713, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.015238, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.019444, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2667, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047026, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.060696, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014457, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017723, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.010713, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016614, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020407, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.015238, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02076, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030405, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.019444, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028276, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049972, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2667, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047026, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048472, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067506, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.060696, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.015981`, avg `-0.008657`, median `-0.000127`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.015001`, avg `-0.014544`, median `-0.014548`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.025745`, avg `0.004059`, median `0.013417`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.046032`, avg `0.013802`, median `0.027848`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.075978`, avg `0.043429`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.016349`, avg `-0.003694`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.015223`, avg `-0.006225`, median `-0.002115`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.02402`, avg `0.004`, median `0.003189`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.049434`, avg `0.017114`, median `0.030181`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.07995`, avg `0.038232`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.010984`, avg `-0.002995`, median `-0.001535`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.015933`, avg `-0.001926`, median `0.001088`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.021159`, avg `-0.012598`, median `-0.016051`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.0651`, avg `-0.022478`, median `-0.015662`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.069902`, avg `-0.008461`, median `-0.019635`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.017723`, avg `-0.00011`, median `0.000609`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.020407`, avg `0.001808`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.027019`, avg `-0.001015`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.049972`, avg `0.005439`, median `0.013418`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.067506`, avg `0.029985`, median `0.044873`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.017723`, avg `-0.00011`, median `0.000609`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.020407`, avg `0.001808`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.027019`, avg `-0.001015`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.049972`, avg `0.005439`, median `0.013418`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.067506`, avg `0.029985`, median `0.044873`

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
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.4167`, primary_mae `0.016062`, avg `3.2e-05`, median `-0.000614`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.3833`, primary_mae `0.018771`, avg `0.000259`, median `0.000725`
- 10d: sample `60`, primary_hit `0.6333`, primary_closer `0.35`, primary_mae `0.02639`, avg `-0.001376`, median `-0.007787`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.3`, primary_mae `0.047936`, avg `0.005215`, median `0.01374`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.35`, primary_mae `0.061143`, avg `0.032472`, median `0.051777`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.017723`, avg `-0.00011`, median `0.000609`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.020407`, avg `0.001808`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.027019`, avg `-0.001015`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.049972`, avg `0.005439`, median `0.013418`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.067506`, avg `0.029985`, median `0.044873`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.010713`, avg `-0.003162`, median `-0.001535`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.015238`, avg `-0.001804`, median `0.000818`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.019444`, avg `-0.014486`, median `-0.01712`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.058812`, avg `-0.027969`, median `-0.020035`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.060696`, avg `-0.016448`, median `-0.028583`

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
