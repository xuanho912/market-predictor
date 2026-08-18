# Historical Replay Benchmark

Generated at: `2026-08-18T02:32:11.762197+00:00`
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
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.015388`
- secondary_mean_absolute_error: `0.01584`
- primary_error_advantage: `0.000452`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.021344`
- secondary_mean_absolute_error: `0.020884`
- primary_error_advantage: `-0.00046`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.036234`
- secondary_mean_absolute_error: `0.031566`
- primary_error_advantage: `-0.004668`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.06851`
- secondary_mean_absolute_error: `0.063687`
- primary_error_advantage: `-0.004823`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.080767`
- secondary_mean_absolute_error: `0.076655`
- primary_error_advantage: `-0.004112`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

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
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.017582`, as_primary `60`, as_primary_hit `0.55`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.026032`, as_primary `60`, as_primary_hit `0.6333`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.037855`, as_primary `60`, as_primary_hit `0.5`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.071415`, as_primary `60`, as_primary_hit `0.6`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.086513`, as_primary `60`, as_primary_hit `0.5333`, avg `0.021566`, median `0.030669`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.0152`, as_primary `20`, as_primary_hit `0.7`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.019562`, as_primary `20`, as_primary_hit `0.6`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.03791`, as_primary `20`, as_primary_hit `0.65`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.083512`, as_primary `20`, as_primary_hit `0.65`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, direction_hit `0.4`, path_mae `0.087649`, as_primary `20`, as_primary_hit `0.8`, avg `0.021566`, median `0.030669`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.012831`, as_primary `0`, as_primary_hit `None`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.0159`, as_primary `0`, as_primary_hit `None`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.025194`, as_primary `0`, as_primary_hit `None`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.044173`, as_primary `0`, as_primary_hit `None`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.066111`, as_primary `0`, as_primary_hit `None`, avg `0.021566`, median `0.030669`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.525`, primary_mae `0.015388`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.021344`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.036234`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.425`, primary_mae `0.06851`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.080767`, avg `0.021566`, median `0.030669`

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
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.4833`, primary_mae `0.017384`, avg `0.004636`, median `0.006579`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.45`, primary_mae `0.025304`, avg `0.003035`, median `0.003203`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.4`, primary_mae `0.042071`, avg `0.00907`, median `0.011852`
- 20d: sample `60`, primary_hit `0.5833`, primary_closer `0.3667`, primary_mae `0.078974`, avg `0.016782`, median `0.024063`
- 60d: sample `60`, primary_hit `0.4667`, primary_closer `0.4333`, primary_mae `0.088927`, avg `0.030539`, median `0.044817`

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

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012831, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017582, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.0094, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0159, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026032, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.009462, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025194, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03791, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.018723, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044173, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.083512, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.037117, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066111, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.087649, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.056287, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

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
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.525`, primary_mae `0.015388`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.021344`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.036234`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.425`, primary_mae `0.06851`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.080767`, avg `0.021566`, median `0.030669`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.525`, primary_mae `0.015388`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.021344`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.036234`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.425`, primary_mae `0.06851`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.080767`, avg `0.021566`, median `0.030669`

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
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.75`, primary_mae `0.013271`, avg `0.00974`, median `0.010408`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.8`, primary_mae `0.018879`, avg `0.005366`, median `0.002669`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.046159`, avg `0.015145`, median `0.016311`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.65`, primary_mae `0.095943`, avg `0.029792`, median `0.02188`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.65`, primary_mae `0.063908`, avg `0.053087`, median `0.047537`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.525`, primary_mae `0.015388`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.021344`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.036234`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.425`, primary_mae `0.06851`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.080767`, avg `0.021566`, median `0.030669`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.525`, primary_mae `0.015388`, avg `0.002542`, median `0.002477`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.021344`, avg `0.00259`, median `0.003101`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.036234`, avg `0.00473`, median `0.006608`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.425`, primary_mae `0.06851`, avg `0.010275`, median `0.01596`
- 60d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.080767`, avg `0.021566`, median `0.030669`

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
