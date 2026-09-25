# Historical Replay Benchmark

Generated at: `2026-09-25T09:07:37.673695+00:00`
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
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.018164`
- secondary_mean_absolute_error: `0.016863`
- primary_error_advantage: `-0.001301`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.025669`
- secondary_mean_absolute_error: `0.020138`
- primary_error_advantage: `-0.005531`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.042066`
- secondary_mean_absolute_error: `0.030729`
- primary_error_advantage: `-0.011337`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.076304`
- secondary_mean_absolute_error: `0.047467`
- primary_error_advantage: `-0.028837`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.089342`
- secondary_mean_absolute_error: `0.062348`
- primary_error_advantage: `-0.026994`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.016178`, as_primary `0`, as_primary_hit `None`, avg `-0.006252`, median `-0.004146`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.019184`, as_primary `0`, as_primary_hit `None`, avg `-0.009449`, median `-0.007462`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.0278`, as_primary `0`, as_primary_hit `None`, avg `-0.00871`, median `-0.006203`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.042304`, as_primary `0`, as_primary_hit `None`, avg `0.006662`, median `0.016024`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.053228`, as_primary `0`, as_primary_hit `None`, avg `0.044065`, median `0.050314`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.017001`, as_primary `0`, as_primary_hit `None`, avg `-0.006252`, median `-0.004146`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.020164`, as_primary `0`, as_primary_hit `None`, avg `-0.009449`, median `-0.007462`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.033937`, as_primary `0`, as_primary_hit `None`, avg `-0.00871`, median `-0.006203`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.061488`, as_primary `0`, as_primary_hit `None`, avg `0.006662`, median `0.016024`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.060792`, as_primary `0`, as_primary_hit `None`, avg `0.044065`, median `0.050314`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.018164`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.006252`, median `-0.004146`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.025669`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.009449`, median `-0.007462`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.042066`, as_primary `80`, as_primary_hit `0.45`, avg `-0.00871`, median `-0.006203`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.076304`, as_primary `80`, as_primary_hit `0.625`, avg `0.006662`, median `0.016024`
- 60d: sample `80`, direction_hit `0.1875`, path_mae `0.089342`, as_primary `80`, as_primary_hit `0.8125`, avg `0.044065`, median `0.050314`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015899`, as_primary `0`, as_primary_hit `None`, avg `-0.006252`, median `-0.004146`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.018615`, as_primary `0`, as_primary_hit `None`, avg `-0.009449`, median `-0.007462`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.028263`, as_primary `0`, as_primary_hit `None`, avg `-0.00871`, median `-0.006203`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.043403`, as_primary `0`, as_primary_hit `None`, avg `0.006662`, median `0.016024`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.054902`, as_primary `0`, as_primary_hit `None`, avg `0.044065`, median `0.050314`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.022208`, avg `-0.010292`, median `-0.014138`
- 5d: sample `20`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.030288`, avg `-0.017705`, median `-0.020235`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.4`, primary_mae `0.037621`, avg `-0.021642`, median `-0.015452`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.085125`, avg `0.00108`, median `0.018406`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.125595`, avg `0.027605`, median `0.041779`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5667`, primary_closer `0.4167`, primary_mae `0.016816`, avg `-0.004905`, median `-0.003662`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.3667`, primary_mae `0.02413`, avg `-0.006697`, median `-0.003597`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.3167`, primary_mae `0.043548`, avg `-0.004399`, median `0.004921`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.25`, primary_mae `0.073364`, avg `0.008522`, median `0.015571`
- 60d: sample `60`, primary_hit `0.1667`, primary_closer `0.25`, primary_mae `0.077257`, avg `0.049552`, median `0.055681`

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
- 3d: sample `60`, primary_hit `0.5667`, primary_closer `0.4167`, primary_mae `0.016816`, avg `-0.004905`, median `-0.003662`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.3667`, primary_mae `0.02413`, avg `-0.006697`, median `-0.003597`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.3167`, primary_mae `0.043548`, avg `-0.004399`, median `0.004921`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.25`, primary_mae `0.073364`, avg `0.008522`, median `0.015571`
- 60d: sample `60`, primary_hit `0.1667`, primary_closer `0.25`, primary_mae `0.077257`, avg `0.049552`, median `0.055681`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.022208`, avg `-0.010292`, median `-0.014138`
- 5d: sample `20`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.030288`, avg `-0.017705`, median `-0.020235`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.4`, primary_mae `0.037621`, avg `-0.021642`, median `-0.015452`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.085125`, avg `0.00108`, median `0.018406`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.125595`, avg `0.027605`, median `0.041779`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.016816, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.02413, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.037621, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.073364, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1667, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.077257, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015899, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018164, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.016816, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018615, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025669, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.02413, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0278, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042066, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.037621, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042304, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076304, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.073364, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053228, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.089342, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1667, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.077257, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.020358`, avg `-0.016717`, median `-0.031812`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.030415`, avg `-0.022926`, median `-0.025209`
- 10d: sample `8`, primary_hit `1.0`, primary_closer `0.375`, primary_mae `0.035059`, avg `-0.023846`, median `-0.017516`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.086095`, avg `-0.004187`, median `0.019252`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.130694`, avg `0.019077`, median `0.048285`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.022347`, avg `-0.010734`, median `-0.01952`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.030823`, avg `-0.017848`, median `-0.020235`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.035521`, avg `-0.024289`, median `-0.017516`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.081738`, avg `-0.003346`, median `0.019252`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.131421`, avg `0.030275`, median `0.048285`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.021098`, avg `-0.018385`, median `-0.012143`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.02916`, avg `-0.018561`, median `-0.017304`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.053685`, avg `-0.005562`, median `-0.006323`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.088744`, avg `0.015243`, median `0.034922`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.10744`, avg `0.076472`, median `0.114142`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4375`, primary_mae `0.018164`, avg `-0.006252`, median `-0.004146`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.025669`, avg `-0.009449`, median `-0.007462`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.3375`, primary_mae `0.042066`, avg `-0.00871`, median `-0.006203`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.275`, primary_mae `0.076304`, avg `0.006662`, median `0.016024`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.089342`, avg `0.044065`, median `0.050314`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4375`, primary_mae `0.018164`, avg `-0.006252`, median `-0.004146`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.025669`, avg `-0.009449`, median `-0.007462`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.3375`, primary_mae `0.042066`, avg `-0.00871`, median `-0.006203`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.275`, primary_mae `0.076304`, avg `0.006662`, median `0.016024`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.089342`, avg `0.044065`, median `0.050314`

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
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4375`, primary_mae `0.018164`, avg `-0.006252`, median `-0.004146`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.025669`, avg `-0.009449`, median `-0.007462`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.3375`, primary_mae `0.042066`, avg `-0.00871`, median `-0.006203`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.275`, primary_mae `0.076304`, avg `0.006662`, median `0.016024`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.089342`, avg `0.044065`, median `0.050314`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4375`, primary_mae `0.018164`, avg `-0.006252`, median `-0.004146`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.025669`, avg `-0.009449`, median `-0.007462`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.3375`, primary_mae `0.042066`, avg `-0.00871`, median `-0.006203`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.275`, primary_mae `0.076304`, avg `0.006662`, median `0.016024`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.089342`, avg `0.044065`, median `0.050314`

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
