# Historical Replay Benchmark

Generated at: `2026-10-17T01:25:38.180561+00:00`
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
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.019145`
- secondary_mean_absolute_error: `0.017109`
- primary_error_advantage: `-0.002036`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.021062`
- secondary_mean_absolute_error: `0.020603`
- primary_error_advantage: `-0.000459`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.031859`
- secondary_mean_absolute_error: `0.029198`
- primary_error_advantage: `-0.002661`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.054633`
- secondary_mean_absolute_error: `0.035501`
- primary_error_advantage: `-0.019132`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.225`
- secondary_hit_rate: `0.775`
- primary_vs_secondary_accuracy_spread: `-0.55`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.060955`
- secondary_mean_absolute_error: `0.057547`
- primary_error_advantage: `-0.003408`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.016507`, as_primary `0`, as_primary_hit `None`, avg `0.000622`, median `0.001376`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.021296`, as_primary `0`, as_primary_hit `None`, avg `-0.001656`, median `-0.002902`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.028946`, as_primary `0`, as_primary_hit `None`, avg `-0.006295`, median `-0.000139`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.036477`, as_primary `0`, as_primary_hit `None`, avg `0.010975`, median `0.016607`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.056444`, as_primary `0`, as_primary_hit `None`, avg `0.075278`, median `0.07817`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.018775`, as_primary `0`, as_primary_hit `None`, avg `0.000622`, median `0.001376`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.025761`, as_primary `0`, as_primary_hit `None`, avg `-0.001656`, median `-0.002902`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.034211`, as_primary `0`, as_primary_hit `None`, avg `-0.006295`, median `-0.000139`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.053877`, as_primary `0`, as_primary_hit `None`, avg `0.010975`, median `0.016607`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.065246`, as_primary `0`, as_primary_hit `None`, avg `0.075278`, median `0.07817`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.019145`, as_primary `80`, as_primary_hit `0.5125`, avg `0.000622`, median `0.001376`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.021062`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.001656`, median `-0.002902`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.031859`, as_primary `80`, as_primary_hit `0.5`, avg `-0.006295`, median `-0.000139`
- 20d: sample `80`, direction_hit `0.4`, path_mae `0.054633`, as_primary `80`, as_primary_hit `0.6`, avg `0.010975`, median `0.016607`
- 60d: sample `80`, direction_hit `0.225`, path_mae `0.060955`, as_primary `80`, as_primary_hit `0.775`, avg `0.075278`, median `0.07817`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.016396`, as_primary `0`, as_primary_hit `None`, avg `0.000622`, median `0.001376`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.019844`, as_primary `0`, as_primary_hit `None`, avg `-0.001656`, median `-0.002902`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.02827`, as_primary `0`, as_primary_hit `None`, avg `-0.006295`, median `-0.000139`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.033875`, as_primary `0`, as_primary_hit `None`, avg `0.010975`, median `0.016607`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.05583`, as_primary `0`, as_primary_hit `None`, avg `0.075278`, median `0.07817`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.019145`, avg `0.000622`, median `0.001376`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.021062`, avg `-0.001656`, median `-0.002902`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.031859`, avg `-0.006295`, median `-0.000139`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.054633`, avg `0.010975`, median `0.016607`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.5125`, primary_mae `0.060955`, avg `0.075278`, median `0.07817`

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
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.019284`, avg `-0.000578`, median `-0.005379`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.021567`, avg `-0.004953`, median `-0.012483`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.035743`, avg `-0.009682`, median `-0.001976`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.053537`, avg `0.008089`, median `0.003949`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.077125`, avg `0.100351`, median `0.130651`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.019007`, avg `0.001822`, median `0.004149`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.020556`, avg `0.001642`, median `0.004992`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.027976`, avg `-0.002908`, median `-1e-06`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.05573`, avg `0.01386`, median `0.028838`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.575`, primary_mae `0.044786`, avg `0.050206`, median `0.052475`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.019007, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.020556, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.027976, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.053537, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.044786, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016396, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019145, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.019007, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019844, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025761, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.020556, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02827, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034211, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.027976, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033875, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054633, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.053537, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.225, 'secondary_hit_rate': 0.775, 'primary_vs_secondary_accuracy_spread': -0.55, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05583, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065246, 'direction_hit_rate': 0.775}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.044786, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.018715`, avg `0.003888`, median `0.005341`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.02252`, avg `0.006352`, median `0.012456`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.020998`, avg `0.01196`, median `0.013415`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.066034`, avg `0.048142`, median `0.050926`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.062902`, avg `0.084573`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.019577`, avg `0.005794`, median `0.009687`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.021299`, avg `0.007388`, median `0.008828`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.024513`, avg `0.007171`, median `0.010351`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.0625`, primary_mae `0.056833`, avg `0.037338`, median `0.036926`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.055888`, avg `0.058645`, median `0.052475`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.01386`, avg `-0.005066`, median `-0.008185`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.015751`, avg `-0.005693`, median `0.002015`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.017426`, avg `-0.002199`, median `0.006054`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.036138`, avg `0.012732`, median `0.003949`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.6875`, primary_mae `0.045709`, avg `0.139827`, median `0.165792`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.019145`, avg `0.000622`, median `0.001376`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.021062`, avg `-0.001656`, median `-0.002902`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.031859`, avg `-0.006295`, median `-0.000139`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.054633`, avg `0.010975`, median `0.016607`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.5125`, primary_mae `0.060955`, avg `0.075278`, median `0.07817`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.019145`, avg `0.000622`, median `0.001376`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.021062`, avg `-0.001656`, median `-0.002902`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.031859`, avg `-0.006295`, median `-0.000139`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.054633`, avg `0.010975`, median `0.016607`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.5125`, primary_mae `0.060955`, avg `0.075278`, median `0.07817`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.019007`, avg `0.001822`, median `0.004149`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.020556`, avg `0.001642`, median `0.004992`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.027976`, avg `-0.002908`, median `-1e-06`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.05573`, avg `0.01386`, median `0.028838`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.575`, primary_mae `0.044786`, avg `0.050206`, median `0.052475`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.019284`, avg `-0.000578`, median `-0.005379`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.021567`, avg `-0.004953`, median `-0.012483`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.035743`, avg `-0.009682`, median `-0.001976`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.053537`, avg `0.008089`, median `0.003949`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.077125`, avg `0.100351`, median `0.130651`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.019145`, avg `0.000622`, median `0.001376`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.021062`, avg `-0.001656`, median `-0.002902`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.031859`, avg `-0.006295`, median `-0.000139`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.054633`, avg `0.010975`, median `0.016607`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.5125`, primary_mae `0.060955`, avg `0.075278`, median `0.07817`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.019145`, avg `0.000622`, median `0.001376`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.021062`, avg `-0.001656`, median `-0.002902`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.031859`, avg `-0.006295`, median `-0.000139`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.054633`, avg `0.010975`, median `0.016607`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.5125`, primary_mae `0.060955`, avg `0.075278`, median `0.07817`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
