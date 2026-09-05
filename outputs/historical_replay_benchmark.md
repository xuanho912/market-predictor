# Historical Replay Benchmark

Generated at: `2026-09-05T15:19:39.627769+00:00`
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
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.019304`
- secondary_mean_absolute_error: `0.013286`
- primary_error_advantage: `-0.006018`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.15`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.019213`
- secondary_mean_absolute_error: `0.015448`
- primary_error_advantage: `-0.003765`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.032361`
- secondary_mean_absolute_error: `0.023494`
- primary_error_advantage: `-0.008867`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.06262`
- secondary_mean_absolute_error: `0.033174`
- primary_error_advantage: `-0.029446`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.2`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.097066`
- secondary_mean_absolute_error: `0.063261`
- primary_error_advantage: `-0.033805`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.01371`, as_primary `0`, as_primary_hit `None`, avg `-0.001891`, median `0.000402`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.015811`, as_primary `0`, as_primary_hit `None`, avg `-1e-06`, median `0.000725`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.02419`, as_primary `0`, as_primary_hit `None`, avg `0.001741`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.033704`, as_primary `0`, as_primary_hit `None`, avg `0.008537`, median `0.022074`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.063677`, as_primary `0`, as_primary_hit `None`, avg `0.029108`, median `0.055734`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.013868`, as_primary `0`, as_primary_hit `None`, avg `-0.001891`, median `0.000402`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.017427`, as_primary `0`, as_primary_hit `None`, avg `-1e-06`, median `0.000725`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.032796`, as_primary `0`, as_primary_hit `None`, avg `0.001741`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.046067`, as_primary `0`, as_primary_hit `None`, avg `0.008537`, median `0.022074`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.076028`, as_primary `0`, as_primary_hit `None`, avg `0.029108`, median `0.055734`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.019304`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.001891`, median `0.000402`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.019213`, as_primary `80`, as_primary_hit `0.5375`, avg `-1e-06`, median `0.000725`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.032361`, as_primary `80`, as_primary_hit `0.4125`, avg `0.001741`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.06262`, as_primary `80`, as_primary_hit `0.6625`, avg `0.008537`, median `0.022074`
- 60d: sample `80`, direction_hit `0.3375`, path_mae `0.097066`, as_primary `80`, as_primary_hit `0.6625`, avg `0.029108`, median `0.055734`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.013286`, as_primary `0`, as_primary_hit `None`, avg `-0.001891`, median `0.000402`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.015448`, as_primary `0`, as_primary_hit `None`, avg `-1e-06`, median `0.000725`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.023494`, as_primary `0`, as_primary_hit `None`, avg `0.001741`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.033174`, as_primary `0`, as_primary_hit `None`, avg `0.008537`, median `0.022074`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.063261`, as_primary `0`, as_primary_hit `None`, avg `0.029108`, median `0.055734`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.25`, primary_mae `0.019304`, avg `-0.001891`, median `0.000402`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.3875`, primary_mae `0.019213`, avg `-1e-06`, median `0.000725`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.325`, primary_mae `0.032361`, avg `0.001741`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.2625`, primary_mae `0.06262`, avg `0.008537`, median `0.022074`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.3125`, primary_mae `0.097066`, avg `0.029108`, median `0.055734`

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
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.013437`, avg `-0.004953`, median `-0.004974`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.014281`, avg `-0.00385`, median `0.000725`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.020773`, avg `-0.013157`, median `-0.015308`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.065038`, avg `-0.021743`, median `-0.011784`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.071212`, avg `-0.005932`, median `-0.01182`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.2667`, primary_mae `0.021259`, avg `-0.000871`, median `0.001274`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4167`, primary_mae `0.020857`, avg `0.001283`, median `0.000827`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.036224`, avg `0.006706`, median `0.000269`
- 20d: sample `60`, primary_hit `0.2333`, primary_closer `0.25`, primary_mae `0.061814`, avg `0.018631`, median `0.028985`
- 60d: sample `60`, primary_hit `0.25`, primary_closer `0.2833`, primary_mae `0.105685`, avg `0.040788`, median `0.069999`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.013437, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.014281, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.020773, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2333, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.061814, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.071212, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013286, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019304, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.013437, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015448, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019213, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.014281, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023494, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032796, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.020773, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033174, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06262, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2333, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.061814, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.063261, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.097066, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.071212, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.026853`, avg `0.005498`, median `0.01185`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.02904`, avg `0.015418`, median `0.016895`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.04528`, avg `0.006302`, median `0.001395`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.087611`, avg `0.011006`, median `0.02705`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.16216`, avg `0.025361`, median `0.041664`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.125`, primary_mae `0.024395`, avg `0.003243`, median `0.003489`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.025162`, avg `0.011539`, median `0.009264`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.049271`, avg `0.006632`, median `0.002658`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.125`, primary_mae `0.09345`, avg `0.011764`, median `0.034463`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.164723`, avg `0.016658`, median `0.041664`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.012514`, avg `-0.004753`, median `-0.004974`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.014383`, avg `-0.003476`, median `0.000725`
- 10d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.018823`, avg `-0.015692`, median `-0.015308`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.063029`, avg `-0.024549`, median `-0.011784`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.071447`, avg `-0.004385`, median `-0.01182`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.25`, primary_mae `0.019304`, avg `-0.001891`, median `0.000402`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.3875`, primary_mae `0.019213`, avg `-1e-06`, median `0.000725`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.325`, primary_mae `0.032361`, avg `0.001741`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.2625`, primary_mae `0.06262`, avg `0.008537`, median `0.022074`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.3125`, primary_mae `0.097066`, avg `0.029108`, median `0.055734`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.25`, primary_mae `0.019304`, avg `-0.001891`, median `0.000402`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.3875`, primary_mae `0.019213`, avg `-1e-06`, median `0.000725`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.325`, primary_mae `0.032361`, avg `0.001741`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.2625`, primary_mae `0.06262`, avg `0.008537`, median `0.022074`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.3125`, primary_mae `0.097066`, avg `0.029108`, median `0.055734`

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
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.2833`, primary_mae `0.017183`, avg `-0.002666`, median `-0.001735`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.4333`, primary_mae `0.016905`, avg `-0.002773`, median `-0.003439`
- 10d: sample `60`, primary_hit `0.6167`, primary_closer `0.3333`, primary_mae `0.026798`, avg `0.000557`, median `-0.007304`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.2833`, primary_mae `0.053596`, avg `0.00806`, median `0.020543`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.3167`, primary_mae `0.07661`, avg `0.035648`, median `0.055734`

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
