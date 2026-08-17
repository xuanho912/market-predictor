# Historical Replay Benchmark

Generated at: `2026-08-17T23:11:03.633634+00:00`
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
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.017582`
- secondary_mean_absolute_error: `0.013646`
- primary_error_advantage: `-0.003936`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.026032`
- secondary_mean_absolute_error: `0.016196`
- primary_error_advantage: `-0.009836`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.037855`
- secondary_mean_absolute_error: `0.029945`
- primary_error_advantage: `-0.00791`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.071415`
- secondary_mean_absolute_error: `0.060781`
- primary_error_advantage: `-0.010634`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.086513`
- secondary_mean_absolute_error: `0.070909`
- primary_error_advantage: `-0.015604`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014845`, as_primary `0`, as_primary_hit `None`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.019113`, as_primary `0`, as_primary_hit `None`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.02645`, as_primary `0`, as_primary_hit `None`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.046191`, as_primary `0`, as_primary_hit `None`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.066696`, as_primary `0`, as_primary_hit `None`, avg `0.021566`, median `0.030669`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.017582`, as_primary `80`, as_primary_hit `0.5875`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.026032`, as_primary `80`, as_primary_hit `0.625`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.037855`, as_primary `80`, as_primary_hit `0.5375`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.071415`, as_primary `80`, as_primary_hit `0.6125`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.086513`, as_primary `80`, as_primary_hit `0.6`, avg `0.021566`, median `0.030669`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.0152`, as_primary `0`, as_primary_hit `None`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.019562`, as_primary `0`, as_primary_hit `None`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.03791`, as_primary `0`, as_primary_hit `None`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.083512`, as_primary `0`, as_primary_hit `None`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, direction_hit `0.4`, path_mae `0.087649`, as_primary `0`, as_primary_hit `None`, avg `0.021566`, median `0.030669`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.012831`, as_primary `0`, as_primary_hit `None`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.0159`, as_primary `0`, as_primary_hit `None`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.025194`, as_primary `0`, as_primary_hit `None`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.044173`, as_primary `0`, as_primary_hit `None`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.066111`, as_primary `0`, as_primary_hit `None`, avg `0.021566`, median `0.030669`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.015724`, avg `0.003001`, median `0.001417`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.475`, primary_mae `0.023547`, avg `0.003311`, median `0.001674`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.035683`, avg `0.003429`, median `-0.004033`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.072341`, avg `0.010272`, median `0.007491`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.071589`, avg `0.023867`, median `0.019108`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.019441`, avg `0.002084`, median `0.004264`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.275`, primary_mae `0.028517`, avg `0.00187`, median `0.003203`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.040028`, avg `0.006032`, median `0.00986`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.225`, primary_mae `0.070489`, avg `0.010277`, median `0.024063`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.101436`, avg `0.019265`, median `0.044817`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.65`, primary_mae `0.0094`, avg `-0.003738`, median `-0.000642`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.009462`, avg `0.001256`, median `0.001659`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.018723`, avg `-0.008287`, median `-0.011447`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.037117`, avg `-0.009248`, median `-0.005516`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.056287`, avg `-0.005354`, median `-0.015624`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.3167`, primary_mae `0.02031`, avg `0.004636`, median `0.006579`
- 5d: sample `60`, primary_hit `0.5833`, primary_closer `0.25`, primary_mae `0.031556`, avg `0.003035`, median `0.003203`
- 10d: sample `60`, primary_hit `0.6167`, primary_closer `0.3667`, primary_mae `0.044233`, avg `0.00907`, median `0.011852`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.2667`, primary_mae `0.082848`, avg `0.016782`, median `0.024063`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.3333`, primary_mae `0.096588`, avg `0.030539`, median `0.044817`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.0094, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.009462, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.018723, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.037117, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.056287, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012831, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017582, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.0094, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0159, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026032, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.009462, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025194, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03791, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.018723, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044173, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.083512, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.037117, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066111, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.087649, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.056287, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.024068`, avg `-0.00677`, median `-0.002198`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.024849`, avg `-0.000561`, median `0.004667`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.029286`, avg `0.002081`, median `0.006471`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.064043`, avg `0.003814`, median `0.015956`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.067986`, avg `0.012687`, median `-0.000129`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017322`, avg `0.002547`, median `0.007972`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.023101`, avg `0.005843`, median `0.004667`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.026543`, avg `0.009948`, median `0.011059`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.049783`, avg `0.022519`, median `0.023697`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.062476`, avg `0.027381`, median `0.038342`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017322`, avg `0.002547`, median `0.007972`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.023101`, avg `0.005843`, median `0.004667`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.026543`, avg `0.009948`, median `0.011059`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.049783`, avg `0.022519`, median `0.023697`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.062476`, avg `0.027381`, median `0.038342`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.017582`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.026032`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.037855`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, primary_hit `0.6125`, primary_closer `0.35`, primary_mae `0.071415`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.086513`, avg `0.021566`, median `0.030669`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.017582`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.026032`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.037855`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, primary_hit `0.6125`, primary_closer `0.35`, primary_mae `0.071415`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.086513`, avg `0.021566`, median `0.030669`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.016094`, avg `0.000143`, median `0.000473`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.4333`, primary_mae `0.022165`, avg `0.001665`, median `0.003101`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.3833`, primary_mae `0.032926`, avg `0.001259`, median `-8e-05`
- 20d: sample `60`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.059365`, avg `0.003769`, median `0.014475`
- 60d: sample `60`, primary_hit `0.5333`, primary_closer `0.3833`, primary_mae `0.086387`, avg `0.011059`, median `0.024312`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.022048`, avg `0.00974`, median `0.010408`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.037632`, avg `0.005366`, median `0.002669`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.052643`, avg `0.015145`, median `0.016311`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.107565`, avg `0.029792`, median `0.02188`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.08689`, avg `0.053087`, median `0.047537`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.017582`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.026032`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.037855`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, primary_hit `0.6125`, primary_closer `0.35`, primary_mae `0.071415`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.086513`, avg `0.021566`, median `0.030669`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.017582`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.026032`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.037855`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, primary_hit `0.6125`, primary_closer `0.35`, primary_mae `0.071415`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.086513`, avg `0.021566`, median `0.030669`

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
