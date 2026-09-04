# Historical Replay Benchmark

Generated at: `2026-09-04T00:31:26.596701+00:00`
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
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.021967`
- secondary_mean_absolute_error: `0.016799`
- primary_error_advantage: `-0.005168`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.027683`
- secondary_mean_absolute_error: `0.020993`
- primary_error_advantage: `-0.00669`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.039993`
- secondary_mean_absolute_error: `0.032192`
- primary_error_advantage: `-0.007801`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `-0.6`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.051541`
- secondary_mean_absolute_error: `0.038021`
- primary_error_advantage: `-0.01352`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.072404`
- secondary_mean_absolute_error: `0.055708`
- primary_error_advantage: `-0.016696`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6625`, path_mae `0.015592`, as_primary `0`, as_primary_hit `None`, avg `0.005226`, median `0.009276`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.01998`, as_primary `0`, as_primary_hit `None`, avg `0.008839`, median `0.011847`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.030353`, as_primary `0`, as_primary_hit `None`, avg `0.012478`, median `0.018382`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.03251`, as_primary `0`, as_primary_hit `None`, avg `0.025116`, median `0.029088`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.061965`, as_primary `0`, as_primary_hit `None`, avg `0.044394`, median `0.063114`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6625`, path_mae `0.017318`, as_primary `0`, as_primary_hit `None`, avg `0.005226`, median `0.009276`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.021984`, as_primary `0`, as_primary_hit `None`, avg `0.008839`, median `0.011847`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.03654`, as_primary `0`, as_primary_hit `None`, avg `0.012478`, median `0.018382`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.044885`, as_primary `0`, as_primary_hit `None`, avg `0.025116`, median `0.029088`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.066805`, as_primary `0`, as_primary_hit `None`, avg `0.044394`, median `0.063114`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3375`, path_mae `0.021967`, as_primary `80`, as_primary_hit `0.6625`, avg `0.005226`, median `0.009276`
- 5d: sample `80`, direction_hit `0.325`, path_mae `0.027683`, as_primary `80`, as_primary_hit `0.675`, avg `0.008839`, median `0.011847`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.039993`, as_primary `80`, as_primary_hit `0.65`, avg `0.012478`, median `0.018382`
- 20d: sample `80`, direction_hit `0.2`, path_mae `0.051541`, as_primary `80`, as_primary_hit `0.8`, avg `0.025116`, median `0.029088`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.072404`, as_primary `80`, as_primary_hit `0.725`, avg `0.044394`, median `0.063114`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6625`, path_mae `0.01573`, as_primary `0`, as_primary_hit `None`, avg `0.005226`, median `0.009276`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.019838`, as_primary `0`, as_primary_hit `None`, avg `0.008839`, median `0.011847`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.028748`, as_primary `0`, as_primary_hit `None`, avg `0.012478`, median `0.018382`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.030374`, as_primary `0`, as_primary_hit `None`, avg `0.025116`, median `0.029088`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.055977`, as_primary `0`, as_primary_hit `None`, avg `0.044394`, median `0.063114`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.3375`, primary_mae `0.021967`, avg `0.005226`, median `0.009276`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.027683`, avg `0.008839`, median `0.011847`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.039993`, avg `0.012478`, median `0.018382`
- 20d: sample `80`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.051541`, avg `0.025116`, median `0.029088`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.072404`, avg `0.044394`, median `0.063114`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.01989`, avg `0.001989`, median `0.006729`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.025969`, avg `0.004981`, median `0.00873`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.0438`, avg `0.004958`, median `0.017789`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.067276`, avg `0.012083`, median `0.030071`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.35`, primary_mae `0.054564`, avg `0.04923`, median `0.060028`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.022659`, avg `0.006306`, median `0.012398`
- 5d: sample `60`, primary_hit `0.3167`, primary_closer `0.4167`, primary_mae `0.028255`, avg `0.010126`, median `0.013983`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.4333`, primary_mae `0.038724`, avg `0.014985`, median `0.019457`
- 20d: sample `60`, primary_hit `0.1667`, primary_closer `0.45`, primary_mae `0.046296`, avg `0.02946`, median `0.028576`
- 60d: sample `60`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.078351`, avg `0.042783`, median `0.064205`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.01989, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.025969, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.038724, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1667, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.046296, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.054564, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015592, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021967, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.01989, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019838, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027683, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.025969, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028748, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039993, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.038724, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': -0.6, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030374, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051541, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1667, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.046296, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055977, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072404, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.054564, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.01981`, avg `0.011441`, median `0.019319`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.017808`, avg `0.013802`, median `0.011781`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.023886`, avg `0.016973`, median `0.017921`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.125`, primary_mae `0.059448`, avg `0.061725`, median `0.060676`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.075695`, avg `0.085751`, median `0.098383`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.017456`, avg `0.007601`, median `0.01606`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.019233`, avg `0.01333`, median `0.018243`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.026425`, avg `0.016905`, median `0.024318`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.375`, primary_mae `0.049774`, avg `0.047927`, median `0.058396`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.3125`, primary_mae `0.063576`, avg `0.077536`, median `0.096338`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.017967`, avg `0.013639`, median `0.01634`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.024606`, avg `0.016317`, median `0.019955`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.03501`, avg `0.02309`, median `0.01979`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.375`, primary_mae `0.040498`, avg `0.040463`, median `0.034442`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.088037`, avg `0.039035`, median `0.004377`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.3375`, primary_mae `0.021967`, avg `0.005226`, median `0.009276`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.027683`, avg `0.008839`, median `0.011847`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.039993`, avg `0.012478`, median `0.018382`
- 20d: sample `80`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.051541`, avg `0.025116`, median `0.029088`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.072404`, avg `0.044394`, median `0.063114`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.3375`, primary_mae `0.021967`, avg `0.005226`, median `0.009276`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.027683`, avg `0.008839`, median `0.011847`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.039993`, avg `0.012478`, median `0.018382`
- 20d: sample `80`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.051541`, avg `0.025116`, median `0.029088`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.072404`, avg `0.044394`, median `0.063114`

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
- 3d: sample `60`, primary_hit `0.2833`, primary_closer `0.3`, primary_mae `0.01854`, avg `0.007972`, median `0.012244`
- 5d: sample `60`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.023183`, avg `0.01108`, median `0.011847`
- 10d: sample `60`, primary_hit `0.3333`, primary_closer `0.3833`, primary_mae `0.033877`, avg `0.014231`, median `0.018151`
- 20d: sample `60`, primary_hit `0.1667`, primary_closer `0.4`, primary_mae `0.048678`, avg `0.029487`, median `0.031267`
- 60d: sample `60`, primary_hit `0.2667`, primary_closer `0.3667`, primary_mae `0.067093`, avg `0.049507`, median `0.064049`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.3375`, primary_mae `0.021967`, avg `0.005226`, median `0.009276`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.027683`, avg `0.008839`, median `0.011847`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.039993`, avg `0.012478`, median `0.018382`
- 20d: sample `80`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.051541`, avg `0.025116`, median `0.029088`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.072404`, avg `0.044394`, median `0.063114`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.026069`, avg `-0.000511`, median `0.00404`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.033576`, avg `0.003549`, median `0.00892`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.05107`, avg `0.006089`, median `0.018762`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.063703`, avg `0.012044`, median `0.027432`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.325`, primary_mae `0.071451`, avg `0.039143`, median `0.061051`

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
