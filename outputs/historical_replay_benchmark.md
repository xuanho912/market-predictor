# Historical Replay Benchmark

Generated at: `2026-08-15T02:22:35.410090+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `60`
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
- sample_size: `60`
- primary_hit_rate: `0.5833`
- secondary_hit_rate: `0.5833`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3167`
- primary_mean_absolute_error: `0.0186`
- secondary_mean_absolute_error: `0.013114`
- primary_error_advantage: `-0.005486`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 5d
- sample_size: `60`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3167`
- primary_mean_absolute_error: `0.026125`
- secondary_mean_absolute_error: `0.016208`
- primary_error_advantage: `-0.009917`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.2`

### 10d
- sample_size: `60`
- primary_hit_rate: `0.5667`
- secondary_hit_rate: `0.5667`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3333`
- primary_mean_absolute_error: `0.033555`
- secondary_mean_absolute_error: `0.022587`
- primary_error_advantage: `-0.010968`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `60`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.2833`
- primary_mean_absolute_error: `0.06664`
- secondary_mean_absolute_error: `0.037999`
- primary_error_advantage: `-0.028641`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 60d
- sample_size: `60`
- primary_hit_rate: `0.5833`
- secondary_hit_rate: `0.5833`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3667`
- primary_mean_absolute_error: `0.075059`
- secondary_mean_absolute_error: `0.055357`
- primary_error_advantage: `-0.019702`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.5833`, path_mae `0.015084`, as_primary `0`, as_primary_hit `None`, avg `0.002573`, median `0.001889`
- 5d: sample `60`, direction_hit `0.65`, path_mae `0.020365`, as_primary `0`, as_primary_hit `None`, avg `0.004968`, median `0.00431`
- 10d: sample `60`, direction_hit `0.5667`, path_mae `0.024487`, as_primary `0`, as_primary_hit `None`, avg `0.007585`, median `0.009079`
- 20d: sample `60`, direction_hit `0.65`, path_mae `0.044258`, as_primary `0`, as_primary_hit `None`, avg `0.016938`, median `0.013776`
- 60d: sample `60`, direction_hit `0.5833`, path_mae `0.059485`, as_primary `0`, as_primary_hit `None`, avg `0.029398`, median `0.023142`

### bounce_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.5833`, path_mae `0.0186`, as_primary `60`, as_primary_hit `0.5833`, avg `0.002573`, median `0.001889`
- 5d: sample `60`, direction_hit `0.65`, path_mae `0.026125`, as_primary `60`, as_primary_hit `0.65`, avg `0.004968`, median `0.00431`
- 10d: sample `60`, direction_hit `0.5667`, path_mae `0.033555`, as_primary `60`, as_primary_hit `0.5667`, avg `0.007585`, median `0.009079`
- 20d: sample `60`, direction_hit `0.65`, path_mae `0.06664`, as_primary `60`, as_primary_hit `0.65`, avg `0.016938`, median `0.013776`
- 60d: sample `60`, direction_hit `0.5833`, path_mae `0.075059`, as_primary `60`, as_primary_hit `0.5833`, avg `0.029398`, median `0.023142`

### failed_bounce_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.4167`, path_mae `0.015111`, as_primary `0`, as_primary_hit `None`, avg `0.002573`, median `0.001889`
- 5d: sample `60`, direction_hit `0.35`, path_mae `0.017083`, as_primary `0`, as_primary_hit `None`, avg `0.004968`, median `0.00431`
- 10d: sample `60`, direction_hit `0.4333`, path_mae `0.030237`, as_primary `0`, as_primary_hit `None`, avg `0.007585`, median `0.009079`
- 20d: sample `60`, direction_hit `0.35`, path_mae `0.069205`, as_primary `0`, as_primary_hit `None`, avg `0.016938`, median `0.013776`
- 60d: sample `60`, direction_hit `0.4167`, path_mae `0.064725`, as_primary `0`, as_primary_hit `None`, avg `0.029398`, median `0.023142`

### analog_average_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.5833`, path_mae `0.013114`, as_primary `0`, as_primary_hit `None`, avg `0.002573`, median `0.001889`
- 5d: sample `60`, direction_hit `0.65`, path_mae `0.016208`, as_primary `0`, as_primary_hit `None`, avg `0.004968`, median `0.00431`
- 10d: sample `60`, direction_hit `0.5667`, path_mae `0.022587`, as_primary `0`, as_primary_hit `None`, avg `0.007585`, median `0.009079`
- 20d: sample `60`, direction_hit `0.65`, path_mae `0.037999`, as_primary `0`, as_primary_hit `None`, avg `0.016938`, median `0.013776`
- 60d: sample `60`, direction_hit `0.5833`, path_mae `0.055357`, as_primary `0`, as_primary_hit `None`, avg `0.029398`, median `0.023142`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.017062`, avg `0.002806`, median `0.000684`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.35`, primary_mae `0.026576`, avg `0.004293`, median `0.003151`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.036041`, avg `0.006688`, median `0.002896`
- 20d: sample `40`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.075368`, avg `0.013111`, median `0.009322`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.078649`, avg `0.029286`, median `0.019108`

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.021677`, avg `0.002108`, median `0.007972`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.25`, primary_mae `0.025223`, avg `0.006318`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.028583`, avg `0.009379`, median `0.011059`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.049183`, avg `0.024591`, median `0.026122`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.067878`, avg `0.029623`, median `0.038342`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.015585`, avg `-0.000768`, median `0.000173`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.017926`, avg `0.004032`, median `0.00431`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.022444`, avg `0.002132`, median `0.002128`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.042847`, avg `0.007974`, median `0.010775`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.063884`, avg `0.006984`, median `-0.005258`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.02463`, avg `0.009257`, median `0.01087`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.042524`, avg `0.006839`, median `0.005687`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.055777`, avg `0.018491`, median `0.016311`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.114224`, avg `0.034864`, median `0.022139`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.35`, primary_mae `0.097409`, avg `0.074228`, median `0.0687`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.015585, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.017926, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022444, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.042847, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.063884, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5833, 'secondary_hit_rate': 0.5833, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3167, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.013114, 'direction_hit_rate': 0.5833}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.0186, 'direction_hit_rate': 0.5833}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.015585, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3167, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.016208, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.026125, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.017926, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5667, 'secondary_hit_rate': 0.5667, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3333, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.022587, 'direction_hit_rate': 0.5667}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.033555, 'direction_hit_rate': 0.5667}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022444, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.2833, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.037999, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.069205, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.042847, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5833, 'secondary_hit_rate': 0.5833, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3667, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.055357, 'direction_hit_rate': 0.5833}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.075059, 'direction_hit_rate': 0.5833}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.063884, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `6`
- 3d: sample `6`, primary_hit `0.6667`, primary_closer `0.1667`, primary_mae `0.018431`, avg `0.004648`, median `0.005338`
- 5d: sample `6`, primary_hit `0.8333`, primary_closer `0.0`, primary_mae `0.021721`, avg `0.007607`, median `0.00778`
- 10d: sample `6`, primary_hit `0.8333`, primary_closer `0.3333`, primary_mae `0.023581`, avg `0.011352`, median `0.01669`
- 20d: sample `6`, primary_hit `0.6667`, primary_closer `0.1667`, primary_mae `0.055081`, avg `0.016149`, median `0.015956`
- 60d: sample `6`, primary_hit `0.3333`, primary_closer `0.3333`, primary_mae `0.092343`, avg `0.004136`, median `-0.032183`

### top_20
- sample_size: `12`
- 3d: sample `12`, primary_hit `0.5`, primary_closer `0.1667`, primary_mae `0.025397`, avg `-0.002319`, median `-0.000883`
- 5d: sample `12`, primary_hit `0.5833`, primary_closer `0.0833`, primary_mae `0.028143`, avg `0.001792`, median `0.004667`
- 10d: sample `12`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.028192`, avg `0.007981`, median `0.011059`
- 20d: sample `12`, primary_hit `0.75`, primary_closer `0.1667`, primary_mae `0.057748`, avg `0.014533`, median `0.023697`
- 60d: sample `12`, primary_hit `0.5`, primary_closer `0.3333`, primary_mae `0.085411`, avg `0.011067`, median `0.005143`

### bottom_20
- sample_size: `12`
- 3d: sample `12`, primary_hit `0.5`, primary_closer `0.1667`, primary_mae `0.025397`, avg `-0.002319`, median `-0.000883`
- 5d: sample `12`, primary_hit `0.5833`, primary_closer `0.0833`, primary_mae `0.028143`, avg `0.001792`, median `0.004667`
- 10d: sample `12`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.028192`, avg `0.007981`, median `0.011059`
- 20d: sample `12`, primary_hit `0.75`, primary_closer `0.1667`, primary_mae `0.057748`, avg `0.014533`, median `0.023697`
- 60d: sample `12`, primary_hit `0.5`, primary_closer `0.3333`, primary_mae `0.085411`, avg `0.011067`, median `0.005143`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.3167`, primary_mae `0.0186`, avg `0.002573`, median `0.001889`
- 5d: sample `60`, primary_hit `0.65`, primary_closer `0.3167`, primary_mae `0.026125`, avg `0.004968`, median `0.00431`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.3333`, primary_mae `0.033555`, avg `0.007585`, median `0.009079`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.2833`, primary_mae `0.06664`, avg `0.016938`, median `0.013776`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.3667`, primary_mae `0.075059`, avg `0.029398`, median `0.023142`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.3167`, primary_mae `0.0186`, avg `0.002573`, median `0.001889`
- 5d: sample `60`, primary_hit `0.65`, primary_closer `0.3167`, primary_mae `0.026125`, avg `0.004968`, median `0.00431`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.3333`, primary_mae `0.033555`, avg `0.007585`, median `0.009079`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.2833`, primary_mae `0.06664`, avg `0.016938`, median `0.013776`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.3667`, primary_mae `0.075059`, avg `0.029398`, median `0.023142`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.015585`, avg `-0.000768`, median `0.000173`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.017926`, avg `0.004032`, median `0.00431`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.022444`, avg `0.002132`, median `0.002128`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.042847`, avg `0.007974`, median `0.010775`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.063884`, avg `0.006984`, median `-0.005258`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.02463`, avg `0.009257`, median `0.01087`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.042524`, avg `0.006839`, median `0.005687`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.055777`, avg `0.018491`, median `0.016311`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.114224`, avg `0.034864`, median `0.022139`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.35`, primary_mae `0.097409`, avg `0.074228`, median `0.0687`

### options_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.3167`, primary_mae `0.0186`, avg `0.002573`, median `0.001889`
- 5d: sample `60`, primary_hit `0.65`, primary_closer `0.3167`, primary_mae `0.026125`, avg `0.004968`, median `0.00431`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.3333`, primary_mae `0.033555`, avg `0.007585`, median `0.009079`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.2833`, primary_mae `0.06664`, avg `0.016938`, median `0.013776`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.3667`, primary_mae `0.075059`, avg `0.029398`, median `0.023142`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.3167`, primary_mae `0.0186`, avg `0.002573`, median `0.001889`
- 5d: sample `60`, primary_hit `0.65`, primary_closer `0.3167`, primary_mae `0.026125`, avg `0.004968`, median `0.00431`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.3333`, primary_mae `0.033555`, avg `0.007585`, median `0.009079`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.2833`, primary_mae `0.06664`, avg `0.016938`, median `0.013776`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.3667`, primary_mae `0.075059`, avg `0.029398`, median `0.023142`

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
