# Historical Replay Benchmark

Generated at: `2026-07-20T14:37:00.908046+00:00`
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
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.015371`
- secondary_mean_absolute_error: `0.01508`
- primary_error_advantage: `-0.000291`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.019214`
- secondary_mean_absolute_error: `0.017882`
- primary_error_advantage: `-0.001332`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.029281`
- secondary_mean_absolute_error: `0.0282`
- primary_error_advantage: `-0.001081`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5375`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.068558`
- secondary_mean_absolute_error: `0.048374`
- primary_error_advantage: `-0.020184`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.113983`
- secondary_mean_absolute_error: `0.081148`
- primary_error_advantage: `-0.032835`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.013482`, as_primary `0`, as_primary_hit `None`, avg `-0.001292`, median `0.001056`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.016783`, as_primary `0`, as_primary_hit `None`, avg `-0.000722`, median `0.001499`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.023784`, as_primary `0`, as_primary_hit `None`, avg `-0.000576`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.037071`, as_primary `0`, as_primary_hit `None`, avg `0.01245`, median `0.017756`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.078429`, as_primary `0`, as_primary_hit `None`, avg `0.028751`, median `0.054511`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.01508`, as_primary `0`, as_primary_hit `None`, avg `-0.001292`, median `0.001056`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.018856`, as_primary `0`, as_primary_hit `None`, avg `-0.000722`, median `0.001499`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.029467`, as_primary `0`, as_primary_hit `None`, avg `-0.000576`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.051413`, as_primary `0`, as_primary_hit `None`, avg `0.01245`, median `0.017756`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.089884`, as_primary `0`, as_primary_hit `None`, avg `0.028751`, median `0.054511`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015371`, as_primary `80`, as_primary_hit `0.5875`, avg `-0.001292`, median `0.001056`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.019214`, as_primary `80`, as_primary_hit `0.5625`, avg `-0.000722`, median `0.001499`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.029281`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.000576`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.068558`, as_primary `80`, as_primary_hit `0.6375`, avg `0.01245`, median `0.017756`
- 60d: sample `80`, direction_hit `0.4`, path_mae `0.113983`, as_primary `80`, as_primary_hit `0.6`, avg `0.028751`, median `0.054511`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.013188`, as_primary `0`, as_primary_hit `None`, avg `-0.001292`, median `0.001056`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.016614`, as_primary `0`, as_primary_hit `None`, avg `-0.000722`, median `0.001499`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.02274`, as_primary `0`, as_primary_hit `None`, avg `-0.000576`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.03714`, as_primary `0`, as_primary_hit `None`, avg `0.01245`, median `0.017756`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.076037`, as_primary `0`, as_primary_hit `None`, avg `0.028751`, median `0.054511`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.023374`, avg `-0.010277`, median `-0.009708`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.026058`, avg `-0.015047`, median `-0.01025`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.7`, primary_mae `0.018686`, avg `-0.007033`, median `-0.009105`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.070547`, avg `0.008718`, median `0.01014`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.113089`, avg `0.028015`, median `0.041779`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.35`, primary_closer `0.4833`, primary_mae `0.012704`, avg `0.001703`, median `0.001736`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.4833`, primary_mae `0.016933`, avg `0.004053`, median `0.003125`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.4833`, primary_mae `0.032813`, avg `0.001576`, median `0.000326`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.3667`, primary_mae `0.067895`, avg `0.013694`, median `0.017835`
- 60d: sample `60`, primary_hit `0.4`, primary_closer `0.3833`, primary_mae `0.114281`, avg `0.028996`, median `0.056396`

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
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.010544`, avg `-0.001671`, median `0.000684`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.65`, primary_mae `0.011871`, avg `-0.003065`, median `0.001032`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.020221`, avg `-0.007095`, median `-0.009`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.058099`, avg `0.000611`, median `-0.001572`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.048777`, avg `0.011226`, median `-0.010173`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.4167`, primary_mae `0.01698`, avg `-0.001166`, median `0.001161`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.4333`, primary_mae `0.021662`, avg `5.9e-05`, median `0.002729`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.5167`, primary_mae `0.032301`, avg `0.001596`, median `-0.00478`
- 20d: sample `60`, primary_hit `0.3`, primary_closer `0.3833`, primary_mae `0.072044`, avg `0.016397`, median `0.027586`
- 60d: sample `60`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.135719`, avg `0.034592`, median `0.064428`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.010544, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.011871, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.020221, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.058099, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.048777, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013188, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015371, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.010544, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016614, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019214, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.011871, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02274, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029467, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.020221, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037071, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.068558, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.058099, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076037, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.113983, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.048777, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.020285`, avg `-0.012643`, median `-0.005846`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.021856`, avg `-0.016654`, median `-0.019178`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.015084`, avg `-0.011849`, median `-0.012486`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.08128`, avg `0.025786`, median `0.031583`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.142284`, avg `0.065978`, median `0.079666`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.024799`, avg `-0.008641`, median `-0.005521`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.027045`, avg `-0.014327`, median `-0.01025`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.6875`, primary_mae `0.019717`, avg `-0.006657`, median `-0.009105`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.075531`, avg `0.012118`, median `0.024617`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.1224`, avg `0.037991`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.019198`, avg `0.002544`, median `0.007321`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.022628`, avg `0.008616`, median `0.010161`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.043115`, avg `0.018181`, median `0.025214`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.3125`, primary_mae `0.048856`, avg `0.034172`, median `0.045062`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.097923`, avg `0.05724`, median `0.069075`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4625`, primary_mae `0.015371`, avg `-0.001292`, median `0.001056`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.019214`, avg `-0.000722`, median `0.001499`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.029281`, avg `-0.000576`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.068558`, avg `0.01245`, median `0.017756`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.113983`, avg `0.028751`, median `0.054511`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4625`, primary_mae `0.015371`, avg `-0.001292`, median `0.001056`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.019214`, avg `-0.000722`, median `0.001499`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.029281`, avg `-0.000576`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.068558`, avg `0.01245`, median `0.017756`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.113983`, avg `0.028751`, median `0.054511`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.016959`, avg `-0.005974`, median `-0.000729`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.018965`, avg `-0.009056`, median `-0.000507`
- 10d: sample `40`, primary_hit `0.7`, primary_closer `0.65`, primary_mae `0.019453`, avg `-0.007064`, median `-0.009105`
- 20d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.064323`, avg `0.004665`, median `-0.000495`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.080933`, avg `0.01962`, median `0.022537`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.018691`, avg `0.001454`, median `0.003877`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.022744`, avg `0.007364`, median `0.006622`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.041721`, avg `0.015053`, median `0.022187`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.35`, primary_mae `0.048177`, avg `0.03449`, median `0.043649`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.091791`, avg `0.054457`, median `0.064428`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4625`, primary_mae `0.015371`, avg `-0.001292`, median `0.001056`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.019214`, avg `-0.000722`, median `0.001499`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.029281`, avg `-0.000576`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.068558`, avg `0.01245`, median `0.017756`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.113983`, avg `0.028751`, median `0.054511`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
