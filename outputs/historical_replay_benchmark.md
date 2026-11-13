# Historical Replay Benchmark

Generated at: `2026-11-13T03:24:15.769987+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
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
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.020635`
- secondary_mean_absolute_error: `0.016664`
- primary_error_advantage: `-0.003971`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.022914`
- secondary_mean_absolute_error: `0.017532`
- primary_error_advantage: `-0.005382`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.044851`
- secondary_mean_absolute_error: `0.02894`
- primary_error_advantage: `-0.015911`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.055659`
- secondary_mean_absolute_error: `0.053057`
- primary_error_advantage: `-0.002602`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.089045`
- secondary_mean_absolute_error: `0.076576`
- primary_error_advantage: `-0.012469`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.01606`, as_primary `0`, as_primary_hit `None`, avg `0.001435`, median `0.000879`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.01835`, as_primary `0`, as_primary_hit `None`, avg `0.003778`, median `0.003558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.028055`, as_primary `0`, as_primary_hit `None`, avg `0.003328`, median `-0.003995`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.035504`, as_primary `0`, as_primary_hit `None`, avg `0.013771`, median `0.014195`
- 60d: sample `80`, direction_hit `0.425`, path_mae `0.077151`, as_primary `0`, as_primary_hit `None`, avg `-0.001791`, median `-0.009482`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.019388`, as_primary `60`, as_primary_hit `0.4333`, avg `0.001435`, median `0.000879`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.022606`, as_primary `60`, as_primary_hit `0.5333`, avg `0.003778`, median `0.003558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.04115`, as_primary `60`, as_primary_hit `0.4333`, avg `0.003328`, median `-0.003995`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.05848`, as_primary `60`, as_primary_hit `0.6167`, avg `0.013771`, median `0.014195`
- 60d: sample `80`, direction_hit `0.425`, path_mae `0.106566`, as_primary `60`, as_primary_hit `0.35`, avg `-0.001791`, median `-0.009482`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.018697`, as_primary `20`, as_primary_hit `0.75`, avg `0.001435`, median `0.000879`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.019857`, as_primary `20`, as_primary_hit `0.8`, avg `0.003778`, median `0.003558`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.038675`, as_primary `20`, as_primary_hit `0.6`, avg `0.003328`, median `-0.003995`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.059606`, as_primary `20`, as_primary_hit `0.75`, avg `0.013771`, median `0.014195`
- 60d: sample `80`, direction_hit `0.575`, path_mae `0.076576`, as_primary `20`, as_primary_hit `0.65`, avg `-0.001791`, median `-0.009482`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.015801`, as_primary `0`, as_primary_hit `None`, avg `0.001435`, median `0.000879`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.016602`, as_primary `0`, as_primary_hit `None`, avg `0.003778`, median `0.003558`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.026334`, as_primary `0`, as_primary_hit `None`, avg `0.003328`, median `-0.003995`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.032909`, as_primary `0`, as_primary_hit `None`, avg `0.013771`, median `0.014195`
- 60d: sample `80`, direction_hit `0.425`, path_mae `0.066062`, as_primary `0`, as_primary_hit `None`, avg `-0.001791`, median `-0.009482`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3875`, primary_mae `0.020635`, avg `0.001435`, median `0.000879`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.3125`, primary_mae `0.022914`, avg `0.003778`, median `0.003558`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.044851`, avg `0.003328`, median `-0.003995`
- 20d: sample `80`, primary_hit `0.525`, primary_closer `0.5125`, primary_mae `0.055659`, avg `0.013771`, median `0.014195`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.089045`, avg `-0.001791`, median `-0.009482`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.4333`, primary_mae `0.019129`, avg `-0.001375`, median `-0.004035`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.35`, primary_mae `0.022178`, avg `0.000813`, median `0.000641`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.4`, primary_mae `0.033298`, avg `0.002029`, median `-0.005954`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.6`, primary_mae `0.05236`, avg `0.007727`, median `0.01201`
- 60d: sample `60`, primary_hit `0.35`, primary_closer `0.4167`, primary_mae `0.088286`, avg `-0.010501`, median `-0.021901`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.025153`, avg `0.009868`, median `0.011763`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.02512`, avg `0.012674`, median `0.01257`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.15`, primary_mae `0.079509`, avg `0.007226`, median `0.01657`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.065554`, avg `0.031904`, median `0.030573`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.091322`, avg `0.024342`, median `0.024981`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.019129, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022178, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.033298, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.05236, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.088286, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015801, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019388, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.019129, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016602, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022606, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022178, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026334, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04115, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.033298, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032909, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059606, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.05236, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066062, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.106566, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.088286, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.029587`, avg `-0.003671`, median `-0.000347`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.039025`, avg `-0.007346`, median `-0.010408`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.070247`, avg `-0.011852`, median `-0.012286`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.068294`, avg `-0.000917`, median `0.011966`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.110881`, avg `-0.011402`, median `-0.030406`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.025283`, avg `0.001751`, median `0.005515`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.031599`, avg `0.001878`, median `-0.002514`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.05867`, avg `0.004803`, median `-0.003044`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.062722`, avg `0.011518`, median `0.009961`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.104562`, avg `0.01024`, median `-0.023919`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.025092`, avg `0.009749`, median `0.011763`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.023805`, avg `0.009843`, median `0.01257`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.1875`, primary_mae `0.075119`, avg `0.000419`, median `0.009595`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.060948`, avg `0.026042`, median `0.021059`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.07739`, avg `0.031786`, median `0.024981`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3875`, primary_mae `0.020635`, avg `0.001435`, median `0.000879`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.3125`, primary_mae `0.022914`, avg `0.003778`, median `0.003558`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.044851`, avg `0.003328`, median `-0.003995`
- 20d: sample `80`, primary_hit `0.525`, primary_closer `0.5125`, primary_mae `0.055659`, avg `0.013771`, median `0.014195`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.089045`, avg `-0.001791`, median `-0.009482`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3875`, primary_mae `0.020635`, avg `0.001435`, median `0.000879`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.3125`, primary_mae `0.022914`, avg `0.003778`, median `0.003558`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.044851`, avg `0.003328`, median `-0.003995`
- 20d: sample `80`, primary_hit `0.525`, primary_closer `0.5125`, primary_mae `0.055659`, avg `0.013771`, median `0.014195`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.089045`, avg `-0.001791`, median `-0.009482`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.4333`, primary_mae `0.019129`, avg `-0.001375`, median `-0.004035`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.35`, primary_mae `0.022178`, avg `0.000813`, median `0.000641`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.4`, primary_mae `0.033298`, avg `0.002029`, median `-0.005954`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.6`, primary_mae `0.05236`, avg `0.007727`, median `0.01201`
- 60d: sample `60`, primary_hit `0.35`, primary_closer `0.4167`, primary_mae `0.088286`, avg `-0.010501`, median `-0.021901`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.025153`, avg `0.009868`, median `0.011763`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.02512`, avg `0.012674`, median `0.01257`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.15`, primary_mae `0.079509`, avg `0.007226`, median `0.01657`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.065554`, avg `0.031904`, median `0.030573`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.091322`, avg `0.024342`, median `0.024981`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3875`, primary_mae `0.020635`, avg `0.001435`, median `0.000879`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.3125`, primary_mae `0.022914`, avg `0.003778`, median `0.003558`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.044851`, avg `0.003328`, median `-0.003995`
- 20d: sample `80`, primary_hit `0.525`, primary_closer `0.5125`, primary_mae `0.055659`, avg `0.013771`, median `0.014195`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.089045`, avg `-0.001791`, median `-0.009482`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3875`, primary_mae `0.020635`, avg `0.001435`, median `0.000879`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.3125`, primary_mae `0.022914`, avg `0.003778`, median `0.003558`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.044851`, avg `0.003328`, median `-0.003995`
- 20d: sample `80`, primary_hit `0.525`, primary_closer `0.5125`, primary_mae `0.055659`, avg `0.013771`, median `0.014195`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.089045`, avg `-0.001791`, median `-0.009482`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3875`, primary_mae `0.020635`, avg `0.001435`, median `0.000879`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.3125`, primary_mae `0.022914`, avg `0.003778`, median `0.003558`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.044851`, avg `0.003328`, median `-0.003995`
- 20d: sample `80`, primary_hit `0.525`, primary_closer `0.5125`, primary_mae `0.055659`, avg `0.013771`, median `0.014195`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.089045`, avg `-0.001791`, median `-0.009482`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
