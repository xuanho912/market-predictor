# Historical Replay Benchmark

Generated at: `2026-07-17T04:28:55.078920+00:00`
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
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.018936`
- secondary_mean_absolute_error: `0.014308`
- primary_error_advantage: `-0.004628`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.024557`
- secondary_mean_absolute_error: `0.017364`
- primary_error_advantage: `-0.007193`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.023137`
- secondary_mean_absolute_error: `0.021496`
- primary_error_advantage: `-0.001641`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.052515`
- secondary_mean_absolute_error: `0.043222`
- primary_error_advantage: `-0.009293`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.090602`
- secondary_mean_absolute_error: `0.077071`
- primary_error_advantage: `-0.013531`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.015036`, as_primary `0`, as_primary_hit `None`, avg `-0.004782`, median `-0.000908`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.01811`, as_primary `0`, as_primary_hit `None`, avg `-0.003333`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.019741`, as_primary `0`, as_primary_hit `None`, avg `-0.003671`, median `-0.009151`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.031293`, as_primary `0`, as_primary_hit `None`, avg `0.010518`, median `0.013604`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.066511`, as_primary `0`, as_primary_hit `None`, avg `0.020385`, median `0.035204`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.014464`, as_primary `0`, as_primary_hit `None`, avg `-0.004782`, median `-0.000908`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.018433`, as_primary `0`, as_primary_hit `None`, avg `-0.003333`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.023154`, as_primary `0`, as_primary_hit `None`, avg `-0.003671`, median `-0.009151`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.045833`, as_primary `0`, as_primary_hit `None`, avg `0.010518`, median `0.013604`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.07722`, as_primary `0`, as_primary_hit `None`, avg `0.020385`, median `0.035204`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.018936`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.004782`, median `-0.000908`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.024557`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.003333`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.023137`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.003671`, median `-0.009151`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.052515`, as_primary `80`, as_primary_hit `0.65`, avg `0.010518`, median `0.013604`
- 60d: sample `80`, direction_hit `0.4`, path_mae `0.090602`, as_primary `80`, as_primary_hit `0.6`, avg `0.020385`, median `0.035204`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.014649`, as_primary `0`, as_primary_hit `None`, avg `-0.004782`, median `-0.000908`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.017071`, as_primary `0`, as_primary_hit `None`, avg `-0.003333`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.019268`, as_primary `0`, as_primary_hit `None`, avg `-0.003671`, median `-0.009151`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.030754`, as_primary `0`, as_primary_hit `None`, avg `0.010518`, median `0.013604`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.065195`, as_primary `0`, as_primary_hit `None`, avg `0.020385`, median `0.035204`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.4125`, primary_mae `0.018936`, avg `-0.004782`, median `-0.000908`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.024557`, avg `-0.003333`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.023137`, avg `-0.003671`, median `-0.009151`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.052515`, avg `0.010518`, median `0.013604`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.090602`, avg `0.020385`, median `0.035204`

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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.4667`, primary_mae `0.016539`, avg `-0.005754`, median `-0.005289`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.4333`, primary_mae `0.019907`, avg `-0.00347`, median `-0.001055`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.4667`, primary_mae `0.021903`, avg `-0.000792`, median `-0.006514`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.4167`, primary_mae `0.04806`, avg `0.013528`, median `0.015167`
- 60d: sample `60`, primary_hit `0.3833`, primary_closer `0.4833`, primary_mae `0.075247`, avg `0.028409`, median `0.043678`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.026126`, avg `-0.001866`, median `0.00177`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.038507`, avg `-0.002923`, median `-0.000392`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.026842`, avg `-0.012307`, median `-0.016462`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.065881`, avg `0.001485`, median `0.006376`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.136668`, avg `-0.003687`, median `0.005662`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.016539, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.019907, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.021903, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.04806, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.075247, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014464, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018936, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.016539, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017071, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024557, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.019907, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019268, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023154, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.021903, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030754, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052515, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.04806, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065195, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.090602, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.075247, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.018635`, avg `-0.014876`, median `-0.020266`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.019013`, avg `-0.018532`, median `-0.02323`
- 10d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.012338`, avg `-0.015696`, median `-0.014252`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.08583`, avg `0.016079`, median `0.025462`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.145663`, avg `0.049114`, median `0.059414`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.019573`, avg `-0.012738`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.019193`, avg `-0.016931`, median `-0.016241`
- 10d: sample `16`, primary_hit `0.875`, primary_closer `0.5625`, primary_mae `0.012842`, avg `-0.013869`, median `-0.016097`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.069001`, avg `0.007192`, median `0.020913`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.121011`, avg `0.031892`, median `0.052632`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.016711`, avg `0.002109`, median `0.007125`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.019973`, avg `0.00715`, median `0.003601`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.4375`, primary_mae `0.035965`, avg `0.01365`, median `0.026575`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.041703`, avg `0.021632`, median `0.009478`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.6875`, primary_mae `0.067697`, avg `0.046456`, median `0.061492`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.4125`, primary_mae `0.018936`, avg `-0.004782`, median `-0.000908`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.024557`, avg `-0.003333`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.023137`, avg `-0.003671`, median `-0.009151`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.052515`, avg `0.010518`, median `0.013604`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.090602`, avg `0.020385`, median `0.035204`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.4125`, primary_mae `0.018936`, avg `-0.004782`, median `-0.000908`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.024557`, avg `-0.003333`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.023137`, avg `-0.003671`, median `-0.009151`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.052515`, avg `0.010518`, median `0.013604`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.090602`, avg `0.020385`, median `0.035204`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.3667`, primary_mae `0.021398`, avg `-0.004353`, median `-0.000908`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.3167`, primary_mae `0.027085`, avg `-0.003405`, median `-0.000813`
- 10d: sample `60`, primary_hit `0.6167`, primary_closer `0.4667`, primary_mae `0.025741`, avg `-0.00353`, median `-0.010392`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.45`, primary_mae `0.058807`, avg `0.01089`, median `0.013099`
- 60d: sample `60`, primary_hit `0.4`, primary_closer `0.4833`, primary_mae `0.106073`, avg `0.022754`, median `0.044193`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.014734`, avg `-0.003044`, median `-0.000919`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.018764`, avg `0.000991`, median `0.001499`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.02522`, avg `0.0042`, median `0.000926`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.038133`, avg `0.016398`, median `0.013604`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.525`, primary_mae `0.055715`, avg `0.030148`, median `0.043678`

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
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.018837`, avg `-0.003968`, median `0.000673`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.02774`, avg `-0.003021`, median `0.000159`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.021084`, avg `-0.0082`, median `-0.010461`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.04976`, avg `0.005442`, median `0.01002`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.090429`, avg `0.004795`, median `0.014153`

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
