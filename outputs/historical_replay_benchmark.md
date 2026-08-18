# Historical Replay Benchmark

Generated at: `2026-08-18T23:34:00.852839+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `40`
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
- sample_size: `40`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.2`
- primary_mean_absolute_error: `0.023607`
- secondary_mean_absolute_error: `0.013744`
- primary_error_advantage: `-0.009863`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `40`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.225`
- primary_mean_absolute_error: `0.022568`
- secondary_mean_absolute_error: `0.014071`
- primary_error_advantage: `-0.008497`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `40`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.325`
- primary_vs_secondary_accuracy_spread: `0.35`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.02716`
- secondary_mean_absolute_error: `0.022247`
- primary_error_advantage: `-0.004913`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `40`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.071261`
- secondary_mean_absolute_error: `0.049313`
- primary_error_advantage: `-0.021948`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `40`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.075183`
- secondary_mean_absolute_error: `0.062064`
- primary_error_advantage: `-0.013119`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `40`
- 3d: sample `40`, direction_hit `0.5`, path_mae `0.016368`, as_primary `0`, as_primary_hit `None`, avg `-0.004602`, median `-0.000614`
- 5d: sample `40`, direction_hit `0.55`, path_mae `0.016272`, as_primary `0`, as_primary_hit `None`, avg `-0.004471`, median `0.000725`
- 10d: sample `40`, direction_hit `0.325`, path_mae `0.017646`, as_primary `0`, as_primary_hit `None`, avg `-0.009387`, median `-0.011447`
- 20d: sample `40`, direction_hit `0.425`, path_mae `0.036093`, as_primary `0`, as_primary_hit `None`, avg `-0.013936`, median `-0.005975`
- 60d: sample `40`, direction_hit `0.425`, path_mae `0.054777`, as_primary `0`, as_primary_hit `None`, avg `-0.007601`, median `-0.011995`

### bounce_path
- sample_size: `40`
- 3d: sample `40`, direction_hit `0.5`, path_mae `0.013744`, as_primary `0`, as_primary_hit `None`, avg `-0.004602`, median `-0.000614`
- 5d: sample `40`, direction_hit `0.55`, path_mae `0.014071`, as_primary `0`, as_primary_hit `None`, avg `-0.004471`, median `0.000725`
- 10d: sample `40`, direction_hit `0.325`, path_mae `0.022247`, as_primary `0`, as_primary_hit `None`, avg `-0.009387`, median `-0.011447`
- 20d: sample `40`, direction_hit `0.425`, path_mae `0.049313`, as_primary `0`, as_primary_hit `None`, avg `-0.013936`, median `-0.005975`
- 60d: sample `40`, direction_hit `0.425`, path_mae `0.062064`, as_primary `0`, as_primary_hit `None`, avg `-0.007601`, median `-0.011995`

### failed_bounce_path
- sample_size: `40`
- 3d: sample `40`, direction_hit `0.5`, path_mae `0.023607`, as_primary `40`, as_primary_hit `0.5`, avg `-0.004602`, median `-0.000614`
- 5d: sample `40`, direction_hit `0.45`, path_mae `0.022568`, as_primary `40`, as_primary_hit `0.55`, avg `-0.004471`, median `0.000725`
- 10d: sample `40`, direction_hit `0.675`, path_mae `0.02716`, as_primary `40`, as_primary_hit `0.325`, avg `-0.009387`, median `-0.011447`
- 20d: sample `40`, direction_hit `0.575`, path_mae `0.071261`, as_primary `40`, as_primary_hit `0.425`, avg `-0.013936`, median `-0.005975`
- 60d: sample `40`, direction_hit `0.575`, path_mae `0.075183`, as_primary `40`, as_primary_hit `0.425`, avg `-0.007601`, median `-0.011995`

### analog_average_path
- sample_size: `40`
- 3d: sample `40`, direction_hit `0.5`, path_mae `0.013662`, as_primary `0`, as_primary_hit `None`, avg `-0.004602`, median `-0.000614`
- 5d: sample `40`, direction_hit `0.55`, path_mae `0.01371`, as_primary `0`, as_primary_hit `None`, avg `-0.004471`, median `0.000725`
- 10d: sample `40`, direction_hit `0.325`, path_mae `0.017571`, as_primary `0`, as_primary_hit `None`, avg `-0.009387`, median `-0.011447`
- 20d: sample `40`, direction_hit `0.425`, path_mae `0.035998`, as_primary `0`, as_primary_hit `None`, avg `-0.013936`, median `-0.005975`
- 60d: sample `40`, direction_hit `0.425`, path_mae `0.054777`, as_primary `0`, as_primary_hit `None`, avg `-0.007601`, median `-0.011995`

## Edge Status Performance

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.2`, primary_mae `0.023607`, avg `-0.004602`, median `-0.000614`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.225`, primary_mae `0.022568`, avg `-0.004471`, median `0.000725`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.02716`, avg `-0.009387`, median `-0.011447`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.3`, primary_mae `0.071261`, avg `-0.013936`, median `-0.005975`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.075183`, avg `-0.007601`, median `-0.011995`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.25`, primary_mae `0.029962`, avg `-0.008136`, median `-0.005666`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.028845`, avg `-0.008622`, median `-0.003481`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.031167`, avg `-0.00779`, median `-0.011067`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.08041`, avg `-0.008311`, median `0.00675`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.083635`, avg `-0.006407`, median `-0.017896`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.15`, primary_mae `0.017252`, avg `-0.001069`, median `0.000402`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.016292`, avg `-0.000319`, median `0.001088`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.023153`, avg `-0.010985`, median `-0.011447`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.062112`, avg `-0.01956`, median `-0.012145`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.06673`, avg `-0.008795`, median `-0.011995`

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

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.15, 'primary_mean_absolute_error': 0.017252, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.016292, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.023153, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.062112, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.06673, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 40, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.2, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 40, 'path_mean_absolute_error': 0.013662, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 40, 'path_mean_absolute_error': 0.023607, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.15, 'primary_mean_absolute_error': 0.017252, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 40, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.225, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 40, 'path_mean_absolute_error': 0.01371, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 40, 'path_mean_absolute_error': 0.022568, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.016292, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 40, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.325, 'primary_vs_secondary_accuracy_spread': 0.35, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 40, 'path_mean_absolute_error': 0.017571, 'direction_hit_rate': 0.325}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 40, 'path_mean_absolute_error': 0.02716, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.023153, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 40, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 40, 'path_mean_absolute_error': 0.035998, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 40, 'path_mean_absolute_error': 0.071261, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.062112, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 40, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 40, 'path_mean_absolute_error': 0.054777, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 40, 'path_mean_absolute_error': 0.075183, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.06673, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `4`
- 3d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.037022`, avg `0.000689`, median `0.005338`
- 5d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.03329`, avg `0.000861`, median `0.008933`
- 10d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.050272`, avg `0.013584`, median `0.023382`
- 20d: sample `4`, primary_hit `0.5`, primary_closer `0.0`, primary_mae `0.099837`, avg `0.017351`, median `0.010792`
- 60d: sample `4`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.08515`, avg `0.012383`, median `0.003915`

### top_20
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.031028`, avg `-0.005889`, median `-0.002198`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.031861`, avg `-0.005845`, median `0.003509`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.037908`, avg `0.00122`, median `0.002208`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.090746`, avg `0.00826`, median `0.014663`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.065315`, avg `-0.007452`, median `-0.032183`

### bottom_20
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.0`, primary_mae `0.016318`, avg `0.000239`, median `0.000402`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.016767`, avg `0.004647`, median `0.001088`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.023512`, avg `-0.008376`, median `-0.01285`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.125`, primary_mae `0.066622`, avg `-0.010587`, median `-0.011388`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.086785`, avg `0.010198`, median `0.014967`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.2`, primary_mae `0.023607`, avg `-0.004602`, median `-0.000614`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.225`, primary_mae `0.022568`, avg `-0.004471`, median `0.000725`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.02716`, avg `-0.009387`, median `-0.011447`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.3`, primary_mae `0.071261`, avg `-0.013936`, median `-0.005975`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.075183`, avg `-0.007601`, median `-0.011995`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.2`, primary_mae `0.023607`, avg `-0.004602`, median `-0.000614`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.225`, primary_mae `0.022568`, avg `-0.004471`, median `0.000725`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.02716`, avg `-0.009387`, median `-0.011447`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.3`, primary_mae `0.071261`, avg `-0.013936`, median `-0.005975`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.075183`, avg `-0.007601`, median `-0.011995`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.2`, primary_mae `0.023607`, avg `-0.004602`, median `-0.000614`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.225`, primary_mae `0.022568`, avg `-0.004471`, median `0.000725`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.02716`, avg `-0.009387`, median `-0.011447`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.3`, primary_mae `0.071261`, avg `-0.013936`, median `-0.005975`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.075183`, avg `-0.007601`, median `-0.011995`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.2`, primary_mae `0.023607`, avg `-0.004602`, median `-0.000614`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.225`, primary_mae `0.022568`, avg `-0.004471`, median `0.000725`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.02716`, avg `-0.009387`, median `-0.011447`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.3`, primary_mae `0.071261`, avg `-0.013936`, median `-0.005975`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.075183`, avg `-0.007601`, median `-0.011995`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.2`, primary_mae `0.023607`, avg `-0.004602`, median `-0.000614`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.225`, primary_mae `0.022568`, avg `-0.004471`, median `0.000725`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.02716`, avg `-0.009387`, median `-0.011447`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.3`, primary_mae `0.071261`, avg `-0.013936`, median `-0.005975`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.075183`, avg `-0.007601`, median `-0.011995`

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
