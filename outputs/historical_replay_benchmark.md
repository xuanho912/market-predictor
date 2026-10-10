# Historical Replay Benchmark

Generated at: `2026-10-10T01:23:02.295861+00:00`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.015419`
- secondary_mean_absolute_error: `0.015273`
- primary_error_advantage: `-0.000146`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.017628`
- secondary_mean_absolute_error: `0.019679`
- primary_error_advantage: `0.002051`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.6`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.6`
- primary_mean_absolute_error: `0.02064`
- secondary_mean_absolute_error: `0.024964`
- primary_error_advantage: `0.004324`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.725`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2375`
- secondary_hit_rate: `0.7625`
- primary_vs_secondary_accuracy_spread: `-0.525`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.042527`
- secondary_mean_absolute_error: `0.037643`
- primary_error_advantage: `-0.004884`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1625`
- secondary_hit_rate: `0.8375`
- primary_vs_secondary_accuracy_spread: `-0.675`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.046978`
- secondary_mean_absolute_error: `0.040204`
- primary_error_advantage: `-0.006774`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.015064`, as_primary `0`, as_primary_hit `None`, avg `-0.000109`, median `0.00104`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.018475`, as_primary `0`, as_primary_hit `None`, avg `-0.000577`, median `-0.003529`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.022504`, as_primary `0`, as_primary_hit `None`, avg `0.000915`, median `0.003868`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.028344`, as_primary `0`, as_primary_hit `None`, avg `0.022234`, median `0.027693`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.044172`, as_primary `0`, as_primary_hit `None`, avg `0.071383`, median `0.089556`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.015342`, as_primary `0`, as_primary_hit `None`, avg `-0.000109`, median `0.00104`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.020053`, as_primary `0`, as_primary_hit `None`, avg `-0.000577`, median `-0.003529`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.025461`, as_primary `0`, as_primary_hit `None`, avg `0.000915`, median `0.003868`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.040753`, as_primary `0`, as_primary_hit `None`, avg `0.022234`, median `0.027693`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.045486`, as_primary `0`, as_primary_hit `None`, avg `0.071383`, median `0.089556`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.015419`, as_primary `80`, as_primary_hit `0.525`, avg `-0.000109`, median `0.00104`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.017628`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.000577`, median `-0.003529`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.02064`, as_primary `80`, as_primary_hit `0.55`, avg `0.000915`, median `0.003868`
- 20d: sample `80`, direction_hit `0.2375`, path_mae `0.042527`, as_primary `80`, as_primary_hit `0.7625`, avg `0.022234`, median `0.027693`
- 60d: sample `80`, direction_hit `0.1625`, path_mae `0.046978`, as_primary `80`, as_primary_hit `0.8375`, avg `0.071383`, median `0.089556`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.015129`, as_primary `0`, as_primary_hit `None`, avg `-0.000109`, median `0.00104`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.017277`, as_primary `0`, as_primary_hit `None`, avg `-0.000577`, median `-0.003529`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.020654`, as_primary `0`, as_primary_hit `None`, avg `0.000915`, median `0.003868`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.02708`, as_primary `0`, as_primary_hit `None`, avg `0.022234`, median `0.027693`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.04213`, as_primary `0`, as_primary_hit `None`, avg `0.071383`, median `0.089556`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.4833`, primary_mae `0.014642`, avg `0.001786`, median `0.004149`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.5167`, primary_mae `0.017236`, avg `0.001277`, median `0.001139`
- 10d: sample `60`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.017178`, avg `0.004346`, median `0.004191`
- 20d: sample `60`, primary_hit `0.1333`, primary_closer `0.3833`, primary_mae `0.035797`, avg `0.030662`, median `0.031783`
- 60d: sample `60`, primary_hit `0.15`, primary_closer `0.5`, primary_mae `0.041332`, avg `0.069489`, median `0.084258`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.01775`, avg `-0.005797`, median `-0.00545`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.018805`, avg `-0.00614`, median `-0.006363`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.031026`, avg `-0.009378`, median `-0.022914`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.062719`, avg `-0.00305`, median `-0.016989`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.063915`, avg `0.077065`, median `0.103937`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.65`, primary_mae `0.010852`, avg `0.000453`, median `0.000822`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.013914`, avg `0.000542`, median `0.001139`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.7`, primary_mae `0.013036`, avg `0.002063`, median `0.00589`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.041337`, avg `0.029415`, median `0.03365`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.3`, primary_mae `0.04391`, avg `0.082236`, median `0.084406`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.01775`, avg `-0.005797`, median `-0.00545`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.018805`, avg `-0.00614`, median `-0.006363`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.031026`, avg `-0.009378`, median `-0.022914`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.062719`, avg `-0.00305`, median `-0.016989`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.063915`, avg `0.077065`, median `0.103937`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.014586`, avg `0.009137`, median `0.013734`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.65`, primary_mae `0.016832`, avg `0.009363`, median `0.009975`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.75`, primary_mae `0.019679`, avg `0.01332`, median `0.014434`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.5`, primary_mae `0.045069`, avg `0.042723`, median `0.040733`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.6`, primary_mae `0.03126`, avg `0.087459`, median `0.099615`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.018488`, avg `-0.004231`, median `-0.006849`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.020962`, avg `-0.006074`, median `-0.014292`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.018818`, avg `-0.002343`, median `-0.008356`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.35`, primary_mae `0.020984`, avg `0.019849`, median `0.015844`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.6`, primary_mae `0.048827`, avg `0.038771`, median `0.029695`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.010852, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.013914, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.013036, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.020984, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.03126, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015064, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015419, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.010852, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017277, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020053, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.013914, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.6, 'best_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02064, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025461, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.013036, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_vs_secondary_accuracy_spread': -0.525, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02708, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042527, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.020984, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1625, 'secondary_hit_rate': 0.8375, 'primary_vs_secondary_accuracy_spread': -0.675, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04213, 'direction_hit_rate': 0.8375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.046978, 'direction_hit_rate': 0.1625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.03126, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017638`, avg `0.000559`, median `0.005307`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.875`, primary_mae `0.013151`, avg `0.001369`, median `0.006272`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.875`, primary_mae `0.024385`, avg `0.000212`, median `0.005316`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.375`, primary_mae `0.046793`, avg `0.04772`, median `0.050926`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.625`, primary_mae `0.040955`, avg `0.078355`, median `0.093471`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.014373`, avg `0.006133`, median `0.012407`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.6875`, primary_mae `0.017185`, avg `0.007848`, median `0.008828`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.75`, primary_mae `0.021337`, avg `0.012469`, median `0.016702`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.4375`, primary_mae `0.046912`, avg `0.043749`, median `0.050926`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.5625`, primary_mae `0.028953`, avg `0.093315`, median `0.099778`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.017578`, avg `-0.006735`, median `-0.011531`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.018338`, avg `-0.006338`, median `-0.006363`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.034757`, avg `-0.009438`, median `-0.028333`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.066638`, avg `0.001163`, median `0.003968`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.054677`, avg `0.089349`, median `0.103937`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.015419`, avg `-0.000109`, median `0.00104`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.55`, primary_mae `0.017628`, avg `-0.000577`, median `-0.003529`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.6`, primary_mae `0.02064`, avg `0.000915`, median `0.003868`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.425`, primary_mae `0.042527`, avg `0.022234`, median `0.027693`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.45`, primary_mae `0.046978`, avg `0.071383`, median `0.089556`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.015419`, avg `-0.000109`, median `0.00104`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.55`, primary_mae `0.017628`, avg `-0.000577`, median `-0.003529`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.6`, primary_mae `0.02064`, avg `0.000915`, median `0.003868`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.425`, primary_mae `0.042527`, avg `0.022234`, median `0.027693`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.45`, primary_mae `0.046978`, avg `0.071383`, median `0.089556`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.014586`, avg `0.009137`, median `0.013734`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.65`, primary_mae `0.016832`, avg `0.009363`, median `0.009975`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.75`, primary_mae `0.019679`, avg `0.01332`, median `0.014434`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.5`, primary_mae `0.045069`, avg `0.042723`, median `0.040733`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.6`, primary_mae `0.03126`, avg `0.087459`, median `0.099615`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.018119`, avg `-0.005014`, median `-0.00676`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.019884`, avg `-0.006107`, median `-0.012028`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.024922`, avg `-0.00586`, median `-0.010218`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.45`, primary_mae `0.041852`, avg `0.008399`, median `0.014408`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.056371`, avg `0.057918`, median `0.072409`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.015419`, avg `-0.000109`, median `0.00104`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.55`, primary_mae `0.017628`, avg `-0.000577`, median `-0.003529`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.6`, primary_mae `0.02064`, avg `0.000915`, median `0.003868`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.425`, primary_mae `0.042527`, avg `0.022234`, median `0.027693`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.45`, primary_mae `0.046978`, avg `0.071383`, median `0.089556`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.5333`, primary_mae `0.015697`, avg `-0.003192`, median `-0.001726`
- 5d: sample `60`, primary_hit `0.6`, primary_closer `0.5167`, primary_mae `0.017894`, avg `-0.00389`, median `-0.006697`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.55`, primary_mae `0.02096`, avg `-0.003219`, median `-0.002708`
- 20d: sample `60`, primary_hit `0.2667`, primary_closer `0.4`, primary_mae `0.04168`, avg `0.015404`, median `0.023201`
- 60d: sample `60`, primary_hit `0.1833`, primary_closer `0.4`, primary_mae `0.052217`, avg `0.066024`, median `0.079087`

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
