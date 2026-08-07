# Historical Replay Benchmark

Generated at: `2026-08-07T00:59:04.950628+00:00`
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
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.015501`
- secondary_mean_absolute_error: `0.015965`
- primary_error_advantage: `0.000464`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.020599`
- secondary_mean_absolute_error: `0.01838`
- primary_error_advantage: `-0.002219`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.03318`
- secondary_mean_absolute_error: `0.028053`
- primary_error_advantage: `-0.005127`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.062216`
- secondary_mean_absolute_error: `0.053488`
- primary_error_advantage: `-0.008728`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.08765`
- secondary_mean_absolute_error: `0.073239`
- primary_error_advantage: `-0.014411`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.013501`, as_primary `0`, as_primary_hit `None`, avg `0.002543`, median `0.004555`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.017295`, as_primary `0`, as_primary_hit `None`, avg `0.0048`, median `0.005948`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.026917`, as_primary `0`, as_primary_hit `None`, avg `0.005329`, median `0.003976`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.038693`, as_primary `0`, as_primary_hit `None`, avg `0.012039`, median `0.014542`
- 60d: sample `80`, direction_hit `0.55`, path_mae `0.069346`, as_primary `0`, as_primary_hit `None`, avg `0.019304`, median `0.02343`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.015648`, as_primary `40`, as_primary_hit `0.525`, avg `0.002543`, median `0.004555`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.022338`, as_primary `40`, as_primary_hit `0.7`, avg `0.0048`, median `0.005948`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.034861`, as_primary `40`, as_primary_hit `0.5`, avg `0.005329`, median `0.003976`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.059573`, as_primary `40`, as_primary_hit `0.625`, avg `0.012039`, median `0.014542`
- 60d: sample `80`, direction_hit `0.55`, path_mae `0.086437`, as_primary `40`, as_primary_hit `0.425`, avg `0.019304`, median `0.02343`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.017301`, as_primary `40`, as_primary_hit `0.75`, avg `0.002543`, median `0.004555`
- 5d: sample `80`, direction_hit `0.3`, path_mae `0.021205`, as_primary `40`, as_primary_hit `0.7`, avg `0.0048`, median `0.005948`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.033151`, as_primary `40`, as_primary_hit `0.6`, avg `0.005329`, median `0.003976`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.067996`, as_primary `40`, as_primary_hit `0.725`, avg `0.012039`, median `0.014542`
- 60d: sample `80`, direction_hit `0.45`, path_mae `0.083497`, as_primary `40`, as_primary_hit `0.675`, avg `0.019304`, median `0.02343`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.013343`, as_primary `0`, as_primary_hit `None`, avg `0.002543`, median `0.004555`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.015609`, as_primary `0`, as_primary_hit `None`, avg `0.0048`, median `0.005948`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.024352`, as_primary `0`, as_primary_hit `None`, avg `0.005329`, median `0.003976`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.036054`, as_primary `0`, as_primary_hit `None`, avg `0.012039`, median `0.014542`
- 60d: sample `80`, direction_hit `0.55`, path_mae `0.067098`, as_primary `0`, as_primary_hit `None`, avg `0.019304`, median `0.02343`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.015501`, avg `0.002543`, median `0.004555`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4625`, primary_mae `0.020599`, avg `0.0048`, median `0.005948`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.03318`, avg `0.005329`, median `0.003976`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.062216`, avg `0.012039`, median `0.014542`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.08765`, avg `0.019304`, median `0.02343`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3333`, primary_closer `0.45`, primary_mae `0.014261`, avg `0.004311`, median `0.005105`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4333`, primary_mae `0.020351`, avg `0.005835`, median `0.006888`
- 10d: sample `60`, primary_hit `0.4167`, primary_closer `0.4167`, primary_mae `0.036107`, avg `0.005691`, median `0.003976`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.3667`, primary_mae `0.065618`, avg `0.011811`, median `0.01201`
- 60d: sample `60`, primary_hit `0.3333`, primary_closer `0.3667`, primary_mae `0.091075`, avg `0.021629`, median `0.029849`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.019221`, avg `-0.00276`, median `0.002617`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.021341`, avg `0.001696`, median `0.003509`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.024398`, avg `0.004241`, median `0.006471`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.65`, primary_mae `0.052011`, avg `0.012723`, median `0.023697`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.077375`, avg `0.01233`, median `0.003555`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014261, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.020351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.024398, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.052011, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.077375, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013343, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017301, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014261, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015609, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022338, 'direction_hit_rate': 0.7}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.020351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024352, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034861, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.024398, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036054, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067996, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.052011, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067098, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.086437, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.077375, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019821`, avg `-0.004255`, median `-0.003968`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.020113`, avg `-0.00032`, median `0.00171`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.025724`, avg `-0.001054`, median `-0.011067`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.057956`, avg `0.003945`, median `0.006243`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.094311`, avg `-0.015481`, median `-0.034556`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.021165`, avg `-0.006098`, median `-0.002198`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.022119`, avg `-0.001442`, median `0.00171`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.027795`, avg `-0.00254`, median `-0.005041`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.059429`, avg `0.002296`, median `0.014663`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.079795`, avg `0.004766`, median `-0.012556`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.019082`, avg `0.005689`, median `0.010545`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.026612`, avg `0.000592`, median `0.007609`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.033763`, avg `0.00581`, median `0.003199`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.05865`, avg `0.022379`, median `0.013042`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.076803`, avg `0.036602`, median `0.02343`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.015501`, avg `0.002543`, median `0.004555`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4625`, primary_mae `0.020599`, avg `0.0048`, median `0.005948`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.03318`, avg `0.005329`, median `0.003976`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.062216`, avg `0.012039`, median `0.014542`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.08765`, avg `0.019304`, median `0.02343`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.015501`, avg `0.002543`, median `0.004555`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4625`, primary_mae `0.020599`, avg `0.0048`, median `0.005948`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.03318`, avg `0.005329`, median `0.003976`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.062216`, avg `0.012039`, median `0.014542`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.08765`, avg `0.019304`, median `0.02343`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.55`, primary_mae `0.013828`, avg `-0.002491`, median `0.000173`
- 5d: sample `40`, primary_hit `0.7`, primary_closer `0.575`, primary_mae `0.015189`, avg `0.002874`, median `0.00431`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.019585`, avg `0.002086`, median `-8e-05`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.6`, primary_mae `0.039788`, avg `0.007193`, median `0.01201`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.070456`, avg `0.002874`, median `-0.009163`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.020623`, avg `0.009738`, median `0.012358`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.029371`, avg `0.006547`, median `0.009868`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.040957`, avg `0.015025`, median `0.005533`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.070383`, avg `0.035495`, median `0.022345`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.090155`, avg `0.056092`, median `0.070486`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.015501`, avg `0.002543`, median `0.004555`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4625`, primary_mae `0.020599`, avg `0.0048`, median `0.005948`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.03318`, avg `0.005329`, median `0.003976`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.062216`, avg `0.012039`, median `0.014542`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.08765`, avg `0.019304`, median `0.02343`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3333`, primary_closer `0.45`, primary_mae `0.014261`, avg `0.004311`, median `0.005105`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4333`, primary_mae `0.020351`, avg `0.005835`, median `0.006888`
- 10d: sample `60`, primary_hit `0.4167`, primary_closer `0.4167`, primary_mae `0.036107`, avg `0.005691`, median `0.003976`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.3667`, primary_mae `0.065618`, avg `0.011811`, median `0.01201`
- 60d: sample `60`, primary_hit `0.3333`, primary_closer `0.3667`, primary_mae `0.091075`, avg `0.021629`, median `0.029849`

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
