# Historical Replay Benchmark

Generated at: `2026-10-16T16:42:44.423594+00:00`
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
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.017836`
- secondary_mean_absolute_error: `0.01472`
- primary_error_advantage: `-0.003116`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.020248`
- secondary_mean_absolute_error: `0.017873`
- primary_error_advantage: `-0.002375`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.023335`
- secondary_mean_absolute_error: `0.022549`
- primary_error_advantage: `-0.000786`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.048241`
- secondary_mean_absolute_error: `0.03451`
- primary_error_advantage: `-0.013731`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2625`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.475`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.077716`
- secondary_mean_absolute_error: `0.057974`
- primary_error_advantage: `-0.019742`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.01432`, as_primary `0`, as_primary_hit `None`, avg `-0.005914`, median `-0.006355`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018147`, as_primary `0`, as_primary_hit `None`, avg `-0.006515`, median `-0.010108`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.024415`, as_primary `0`, as_primary_hit `None`, avg `-0.005611`, median `-0.008477`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.033581`, as_primary `0`, as_primary_hit `None`, avg `0.015172`, median `0.013035`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.059161`, as_primary `0`, as_primary_hit `None`, avg `0.049002`, median `0.059299`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.015153`, as_primary `0`, as_primary_hit `None`, avg `-0.005914`, median `-0.006355`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.021352`, as_primary `0`, as_primary_hit `None`, avg `-0.006515`, median `-0.010108`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.03207`, as_primary `0`, as_primary_hit `None`, avg `-0.005611`, median `-0.008477`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.049819`, as_primary `0`, as_primary_hit `None`, avg `0.015172`, median `0.013035`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.071299`, as_primary `0`, as_primary_hit `None`, avg `0.049002`, median `0.059299`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.017836`, as_primary `80`, as_primary_hit `0.425`, avg `-0.005914`, median `-0.006355`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.020248`, as_primary `80`, as_primary_hit `0.45`, avg `-0.006515`, median `-0.010108`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.023335`, as_primary `80`, as_primary_hit `0.425`, avg `-0.005611`, median `-0.008477`
- 20d: sample `80`, direction_hit `0.4125`, path_mae `0.048241`, as_primary `80`, as_primary_hit `0.5875`, avg `0.015172`, median `0.013035`
- 60d: sample `80`, direction_hit `0.2625`, path_mae `0.077716`, as_primary `80`, as_primary_hit `0.7375`, avg `0.049002`, median `0.059299`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.014492`, as_primary `0`, as_primary_hit `None`, avg `-0.005914`, median `-0.006355`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.017318`, as_primary `0`, as_primary_hit `None`, avg `-0.006515`, median `-0.010108`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.021762`, as_primary `0`, as_primary_hit `None`, avg `-0.005611`, median `-0.008477`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.030972`, as_primary `0`, as_primary_hit `None`, avg `0.015172`, median `0.013035`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.057085`, as_primary `0`, as_primary_hit `None`, avg `0.049002`, median `0.059299`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.017836`, avg `-0.005914`, median `-0.006355`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.020248`, avg `-0.006515`, median `-0.010108`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.023335`, avg `-0.005611`, median `-0.008477`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.3875`, primary_mae `0.048241`, avg `0.015172`, median `0.013035`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.35`, primary_mae `0.077716`, avg `0.049002`, median `0.059299`

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
- 3d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.014688`, avg `-0.011216`, median `-0.00934`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.35`, primary_mae `0.019678`, avg `-0.015954`, median `-0.021206`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.5`, primary_mae `0.027578`, avg `-0.024966`, median `-0.036035`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.064744`, avg `0.008082`, median `-0.000315`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.2`, primary_mae `0.075264`, avg `0.075267`, median `0.086161`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.014924`, avg `-0.003971`, median `0.001086`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.014601`, avg `-0.003412`, median `0.000995`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.65`, primary_mae `0.016686`, avg `-0.000366`, median `0.000297`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.034695`, avg `0.010308`, median `0.009052`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.061563`, avg `0.007545`, median `0.017729`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.020867`, avg `-0.004234`, median `-0.004083`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.023357`, avg `-0.003347`, median `-0.000844`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.024537`, avg `0.001444`, median `-0.003145`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.046763`, avg `0.021149`, median `0.019681`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.087018`, avg `0.056597`, median `0.064103`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.014688, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014601, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.016686, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.034695, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.061563, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01432, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017836, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.014688, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017318, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021352, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014601, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021762, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03207, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.016686, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030972, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049819, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.034695, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.475, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057085, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.077716, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.061563, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.014112`, avg `-0.002903`, median `0.001086`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.014981`, avg `-0.006121`, median `-0.002888`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.875`, primary_mae `0.012124`, avg `-0.006253`, median `-0.003647`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.035725`, avg `0.014079`, median `0.008728`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.056594`, avg `0.021077`, median `0.041509`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.016243`, avg `-0.004164`, median `0.001086`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.015539`, avg `-0.004701`, median `-0.002888`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.625`, primary_mae `0.01705`, avg `0.001681`, median `0.000297`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.038135`, avg `0.015634`, median `0.017343`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.05958`, avg `0.022522`, median `0.037786`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.01696`, avg `-0.000691`, median `0.007921`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.017577`, avg `0.004778`, median `0.00265`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.027114`, avg `0.013548`, median `0.011751`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.04898`, avg `0.031035`, median `0.034268`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.3125`, primary_mae `0.071833`, avg `0.092064`, median `0.079433`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.017836`, avg `-0.005914`, median `-0.006355`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.020248`, avg `-0.006515`, median `-0.010108`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.023335`, avg `-0.005611`, median `-0.008477`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.3875`, primary_mae `0.048241`, avg `0.015172`, median `0.013035`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.35`, primary_mae `0.077716`, avg `0.049002`, median `0.059299`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.017836`, avg `-0.005914`, median `-0.006355`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.020248`, avg `-0.006515`, median `-0.010108`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.023335`, avg `-0.005611`, median `-0.008477`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.3875`, primary_mae `0.048241`, avg `0.015172`, median `0.013035`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.35`, primary_mae `0.077716`, avg `0.049002`, median `0.059299`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.019459`, avg `-0.005464`, median `-0.000494`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.020757`, avg `-0.006479`, median `0.000888`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.019564`, avg `-0.002737`, median `-0.005954`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.042603`, avg `0.014311`, median `0.013035`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.081682`, avg `0.023778`, median `0.041779`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.016213`, avg `-0.006363`, median `-0.00934`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.01974`, avg `-0.006551`, median `-0.012577`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.027105`, avg `-0.008484`, median `-0.01401`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.05388`, avg `0.016034`, median `0.011539`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.275`, primary_mae `0.07375`, avg `0.074225`, median `0.078416`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.017836`, avg `-0.005914`, median `-0.006355`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.020248`, avg `-0.006515`, median `-0.010108`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.023335`, avg `-0.005611`, median `-0.008477`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.3875`, primary_mae `0.048241`, avg `0.015172`, median `0.013035`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.35`, primary_mae `0.077716`, avg `0.049002`, median `0.059299`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.017836`, avg `-0.005914`, median `-0.006355`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.020248`, avg `-0.006515`, median `-0.010108`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.023335`, avg `-0.005611`, median `-0.008477`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.3875`, primary_mae `0.048241`, avg `0.015172`, median `0.013035`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.35`, primary_mae `0.077716`, avg `0.049002`, median `0.059299`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
