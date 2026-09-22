# Historical Replay Benchmark

Generated at: `2026-09-22T00:26:13.007548+00:00`
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
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.020568`
- secondary_mean_absolute_error: `0.021155`
- primary_error_advantage: `0.000587`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.525`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.025292`
- secondary_mean_absolute_error: `0.023263`
- primary_error_advantage: `-0.002029`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.041304`
- secondary_mean_absolute_error: `0.037254`
- primary_error_advantage: `-0.00405`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.053221`
- secondary_mean_absolute_error: `0.05537`
- primary_error_advantage: `0.002149`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.067329`
- secondary_mean_absolute_error: `0.059885`
- primary_error_advantage: `-0.007444`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.01733`, as_primary `0`, as_primary_hit `None`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.021313`, as_primary `0`, as_primary_hit `None`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.031932`, as_primary `0`, as_primary_hit `None`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.040336`, as_primary `0`, as_primary_hit `None`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.052612`, as_primary `0`, as_primary_hit `None`, avg `0.066044`, median `0.079292`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.019432`, as_primary `40`, as_primary_hit `0.65`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.024549`, as_primary `40`, as_primary_hit `0.625`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.036164`, as_primary `40`, as_primary_hit `0.65`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.057691`, as_primary `40`, as_primary_hit `0.8`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.059683`, as_primary `40`, as_primary_hit `0.85`, avg `0.066044`, median `0.079292`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.023215`, as_primary `40`, as_primary_hit `0.6`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.026388`, as_primary `40`, as_primary_hit `0.6`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.044611`, as_primary `40`, as_primary_hit `0.575`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, direction_hit `0.2125`, path_mae `0.061416`, as_primary `40`, as_primary_hit `0.775`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, direction_hit `0.175`, path_mae `0.071006`, as_primary `40`, as_primary_hit `0.8`, avg `0.066044`, median `0.079292`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.017514`, as_primary `0`, as_primary_hit `None`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.020699`, as_primary `0`, as_primary_hit `None`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.032269`, as_primary `0`, as_primary_hit `None`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.037231`, as_primary `0`, as_primary_hit `None`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.054203`, as_primary `0`, as_primary_hit `None`, avg `0.066044`, median `0.079292`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.020568`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.025292`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.5`, primary_mae `0.041304`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.053221`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.067329`, avg `0.066044`, median `0.079292`

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
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.035088`, avg `-0.004311`, median `-0.000629`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.034353`, avg `-0.006185`, median `-0.011716`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.071132`, avg `-0.006789`, median `-0.00147`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.066834`, avg `0.007523`, median `0.017154`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.108515`, avg `0.042411`, median `0.06708`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.55`, primary_mae `0.015728`, avg `0.008535`, median `0.012563`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.022271`, avg `0.009878`, median `0.012751`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.5167`, primary_mae `0.031361`, avg `0.013835`, median `0.014007`
- 20d: sample `60`, primary_hit `0.5667`, primary_closer `0.5333`, primary_mae `0.048683`, avg `0.039283`, median `0.033877`
- 60d: sample `60`, primary_hit `0.6167`, primary_closer `0.5667`, primary_mae `0.0536`, avg `0.073921`, median `0.082331`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.015728, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.022271, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.031361, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.048683, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.0536, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01733, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023215, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.015728, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020699, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026388, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.022271, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031932, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044611, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.031361, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037231, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061416, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.048683, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052612, 'direction_hit_rate': 0.825}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071006, 'direction_hit_rate': 0.175}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.0536, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.012253`, avg `0.010261`, median `0.018969`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.01755`, avg `0.011464`, median `0.011781`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.024499`, avg `0.014702`, median `0.017921`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.875`, primary_mae `0.02051`, avg `0.059682`, median `0.060676`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.032522`, avg `0.089216`, median `0.099778`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.012401`, avg `0.011069`, median `0.017922`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.017239`, avg `0.01426`, median `0.014527`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.5625`, primary_mae `0.021077`, avg `0.020542`, median `0.024318`
- 20d: sample `16`, primary_hit `1.0`, primary_closer `0.625`, primary_mae `0.02813`, avg `0.053405`, median `0.058396`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.039723`, avg `0.080457`, median `0.096338`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.035404`, avg `-0.00515`, median `0.00075`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.032182`, avg `-0.008263`, median `-0.011716`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.066171`, avg `-0.013982`, median `-0.015492`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.061712`, avg `0.00145`, median `0.005403`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.107342`, avg `0.034447`, median `0.064205`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.020568`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.025292`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.5`, primary_mae `0.041304`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.053221`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.067329`, avg `0.066044`, median `0.079292`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.020568`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.025292`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.5`, primary_mae `0.041304`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.053221`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.067329`, avg `0.066044`, median `0.079292`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.013547`, avg `0.000998`, median `0.002973`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.016454`, avg `-0.000165`, median `0.001407`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.65`, primary_mae `0.023246`, avg `-0.004112`, median `0.004006`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.042735`, avg `0.01599`, median `0.030823`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.55`, primary_mae `0.038033`, avg `0.058882`, median `0.064839`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.020568`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.025292`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.5`, primary_mae `0.041304`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.053221`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.067329`, avg `0.066044`, median `0.079292`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.020568`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.025292`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.5`, primary_mae `0.041304`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.053221`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.067329`, avg `0.066044`, median `0.079292`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.525`, primary_mae `0.016818`, avg `0.012304`, median `0.017848`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.02518`, avg `0.014899`, median `0.016307`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.035418`, avg `0.022809`, median `0.024318`
- 20d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.051657`, avg `0.05093`, median `0.040733`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.061383`, avg `0.081441`, median `0.088751`

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
