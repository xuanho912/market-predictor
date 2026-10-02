# Historical Replay Benchmark

Generated at: `2026-10-02T17:54:56.868987+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.017104`
- secondary_mean_absolute_error: `0.015128`
- primary_error_advantage: `-0.001976`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.02235`
- secondary_mean_absolute_error: `0.016924`
- primary_error_advantage: `-0.005426`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.037924`
- secondary_mean_absolute_error: `0.028301`
- primary_error_advantage: `-0.009623`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.067912`
- secondary_mean_absolute_error: `0.039995`
- primary_error_advantage: `-0.027917`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.175`
- secondary_hit_rate: `0.825`
- primary_vs_secondary_accuracy_spread: `-0.65`
- primary_closer_than_secondary_rate: `0.2375`
- primary_mean_absolute_error: `0.080639`
- secondary_mean_absolute_error: `0.050764`
- primary_error_advantage: `-0.029875`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.015224`, as_primary `0`, as_primary_hit `None`, avg `-0.003838`, median `-0.003098`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.017077`, as_primary `0`, as_primary_hit `None`, avg `-0.00503`, median `-0.002309`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.029383`, as_primary `0`, as_primary_hit `None`, avg `-0.007779`, median `-0.002583`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.040131`, as_primary `0`, as_primary_hit `None`, avg `0.003459`, median `0.013951`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.051153`, as_primary `0`, as_primary_hit `None`, avg `0.048533`, median `0.056634`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.015293`, as_primary `0`, as_primary_hit `None`, avg `-0.003838`, median `-0.003098`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.017266`, as_primary `0`, as_primary_hit `None`, avg `-0.00503`, median `-0.002309`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.033879`, as_primary `0`, as_primary_hit `None`, avg `-0.007779`, median `-0.002583`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.058856`, as_primary `0`, as_primary_hit `None`, avg `0.003459`, median `0.013951`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.052397`, as_primary `0`, as_primary_hit `None`, avg `0.048533`, median `0.056634`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.017104`, as_primary `80`, as_primary_hit `0.45`, avg `-0.003838`, median `-0.003098`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.02235`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.00503`, median `-0.002309`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.037924`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.007779`, median `-0.002583`
- 20d: sample `80`, direction_hit `0.425`, path_mae `0.067912`, as_primary `80`, as_primary_hit `0.575`, avg `0.003459`, median `0.013951`
- 60d: sample `80`, direction_hit `0.175`, path_mae `0.080639`, as_primary `80`, as_primary_hit `0.825`, avg `0.048533`, median `0.056634`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.015128`, as_primary `0`, as_primary_hit `None`, avg `-0.003838`, median `-0.003098`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.016924`, as_primary `0`, as_primary_hit `None`, avg `-0.00503`, median `-0.002309`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.028301`, as_primary `0`, as_primary_hit `None`, avg `-0.007779`, median `-0.002583`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.039995`, as_primary `0`, as_primary_hit `None`, avg `0.003459`, median `0.013951`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.050764`, as_primary `0`, as_primary_hit `None`, avg `0.048533`, median `0.056634`

## Edge Status Performance

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.016838`, avg `-0.004079`, median `-0.003098`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.02146`, avg `-0.00324`, median `-0.004042`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.044884`, avg `-0.009427`, median `0.002106`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.275`, primary_mae `0.070258`, avg `0.004458`, median `0.010261`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.275`, primary_mae `0.073368`, avg `0.064892`, median `0.084406`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.01737`, avg `-0.003596`, median `-0.002653`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.25`, primary_mae `0.023241`, avg `-0.00682`, median `-0.000992`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.325`, primary_mae `0.030964`, avg `-0.00613`, median `-0.005578`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.25`, primary_mae `0.065566`, avg `0.00246`, median `0.013951`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.2`, primary_mae `0.08791`, avg `0.032175`, median `0.043219`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.020143`, avg `-0.008545`, median `-0.010058`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.026572`, avg `-0.008385`, median `-0.007022`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.044543`, avg `-0.0143`, median `-0.017516`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.325`, primary_mae `0.081583`, avg `-0.003192`, median `-0.00102`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.225`, primary_mae `0.113464`, avg `0.054642`, median `0.084656`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.014065`, avg `0.000869`, median `0.003`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.018129`, avg `-0.001675`, median `0.003783`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.325`, primary_mae `0.031304`, avg `-0.001258`, median `0.004865`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.2`, primary_mae `0.054242`, avg `0.010111`, median `0.015722`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.047814`, avg `0.042425`, median `0.044525`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.014065, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.018129, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.031304, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.054242, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.125, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.047814, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015128, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017104, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.014065, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016924, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02235, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.018129, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028301, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037924, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.031304, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039995, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067912, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.054242, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.175, 'secondary_hit_rate': 0.825, 'primary_vs_secondary_accuracy_spread': -0.65, 'primary_closer_than_secondary_rate': 0.2375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050764, 'direction_hit_rate': 0.825}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.080639, 'direction_hit_rate': 0.175}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.125, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.047814, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.009681`, avg `-0.000163`, median `0.003983`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.010859`, avg `0.001297`, median `0.005524`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.022454`, avg `0.003735`, median `0.010165`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.061666`, avg `0.012634`, median `0.032633`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.046761`, avg `0.050604`, median `0.047436`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.01005`, avg `-0.000287`, median `0.000437`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.011954`, avg `-0.00194`, median `0.001171`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.021258`, avg `0.004906`, median `0.007434`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.059779`, avg `0.016468`, median `0.025964`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.039061`, avg `0.029612`, median `0.036672`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.026087`, avg `-0.006736`, median `-0.002898`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.1875`, primary_mae `0.035727`, avg `-0.012944`, median `-0.009034`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.041524`, avg `-0.017906`, median `-0.015452`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.077684`, avg `-0.007401`, median `-0.001627`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.139932`, avg `0.038785`, median `0.057834`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4125`, primary_mae `0.017104`, avg `-0.003838`, median `-0.003098`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3625`, primary_mae `0.02235`, avg `-0.00503`, median `-0.002309`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.35`, primary_mae `0.037924`, avg `-0.007779`, median `-0.002583`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2625`, primary_mae `0.067912`, avg `0.003459`, median `0.013951`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.2375`, primary_mae `0.080639`, avg `0.048533`, median `0.056634`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4125`, primary_mae `0.017104`, avg `-0.003838`, median `-0.003098`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3625`, primary_mae `0.02235`, avg `-0.00503`, median `-0.002309`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.35`, primary_mae `0.037924`, avg `-0.007779`, median `-0.002583`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2625`, primary_mae `0.067912`, avg `0.003459`, median `0.013951`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.2375`, primary_mae `0.080639`, avg `0.048533`, median `0.056634`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4125`, primary_mae `0.017104`, avg `-0.003838`, median `-0.003098`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3625`, primary_mae `0.02235`, avg `-0.00503`, median `-0.002309`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.35`, primary_mae `0.037924`, avg `-0.007779`, median `-0.002583`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2625`, primary_mae `0.067912`, avg `0.003459`, median `0.013951`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.2375`, primary_mae `0.080639`, avg `0.048533`, median `0.056634`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4125`, primary_mae `0.017104`, avg `-0.003838`, median `-0.003098`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3625`, primary_mae `0.02235`, avg `-0.00503`, median `-0.002309`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.35`, primary_mae `0.037924`, avg `-0.007779`, median `-0.002583`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2625`, primary_mae `0.067912`, avg `0.003459`, median `0.013951`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.2375`, primary_mae `0.080639`, avg `0.048533`, median `0.056634`

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
