# Historical Replay Benchmark

Generated at: `2026-10-13T19:21:46.744159+00:00`
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
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.018282`
- secondary_mean_absolute_error: `0.01565`
- primary_error_advantage: `-0.002632`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.021457`
- secondary_mean_absolute_error: `0.019824`
- primary_error_advantage: `-0.001633`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.025959`
- secondary_mean_absolute_error: `0.023674`
- primary_error_advantage: `-0.002285`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.059686`
- secondary_mean_absolute_error: `0.041884`
- primary_error_advantage: `-0.017802`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.25`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.5`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.076289`
- secondary_mean_absolute_error: `0.059289`
- primary_error_advantage: `-0.017`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.016448`, as_primary `0`, as_primary_hit `None`, avg `-0.00623`, median `-0.005438`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.018867`, as_primary `0`, as_primary_hit `None`, avg `-0.00985`, median `-0.015005`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.024001`, as_primary `0`, as_primary_hit `None`, avg `-0.010944`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.03455`, as_primary `0`, as_primary_hit `None`, avg `0.014118`, median `0.015565`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.053355`, as_primary `0`, as_primary_hit `None`, avg `0.037524`, median `0.052147`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.016328`, as_primary `0`, as_primary_hit `None`, avg `-0.00623`, median `-0.005438`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.019806`, as_primary `0`, as_primary_hit `None`, avg `-0.00985`, median `-0.015005`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.027773`, as_primary `0`, as_primary_hit `None`, avg `-0.010944`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.050151`, as_primary `0`, as_primary_hit `None`, avg `0.014118`, median `0.015565`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.063969`, as_primary `0`, as_primary_hit `None`, avg `0.037524`, median `0.052147`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.018282`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.00623`, median `-0.005438`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.021457`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.00985`, median `-0.015005`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.025959`, as_primary `80`, as_primary_hit `0.375`, avg `-0.010944`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.059686`, as_primary `80`, as_primary_hit `0.6125`, avg `0.014118`, median `0.015565`
- 60d: sample `80`, direction_hit `0.25`, path_mae `0.076289`, as_primary `80`, as_primary_hit `0.75`, avg `0.037524`, median `0.052147`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.015608`, as_primary `0`, as_primary_hit `None`, avg `-0.00623`, median `-0.005438`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.018907`, as_primary `0`, as_primary_hit `None`, avg `-0.00985`, median `-0.015005`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.022707`, as_primary `0`, as_primary_hit `None`, avg `-0.010944`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.034274`, as_primary `0`, as_primary_hit `None`, avg `0.014118`, median `0.015565`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.055053`, as_primary `0`, as_primary_hit `None`, avg `0.037524`, median `0.052147`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.018282`, avg `-0.00623`, median `-0.005438`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.021457`, avg `-0.00985`, median `-0.015005`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.025959`, avg `-0.010944`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.059686`, avg `0.014118`, median `0.015565`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.076289`, avg `0.037524`, median `0.052147`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.019406`, avg `-0.007474`, median `-0.005583`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.023641`, avg `-0.010743`, median `-0.016241`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.027082`, avg `-0.012662`, median `-0.010944`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.063233`, avg `0.00677`, median `0.009546`
- 60d: sample `40`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.093106`, avg `0.017781`, median `0.048423`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.017158`, avg `-0.004987`, median `-0.005438`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.019273`, avg `-0.008957`, median `-0.013338`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.024835`, avg `-0.009226`, median `-0.014057`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.056139`, avg `0.021466`, median `0.015719`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.325`, primary_mae `0.059473`, avg `0.057268`, median `0.056639`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.017158, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.019273, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.024835, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.056139, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.059473, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015608, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018282, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.017158, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018867, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021457, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.019273, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022707, 'direction_hit_rate': 0.375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027773, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.024835, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034274, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059686, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.056139, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.5, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053355, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076289, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.059473, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.019372`, avg `-0.016625`, median `-0.030767`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.022505`, avg `-0.014933`, median `-0.020293`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.020689`, avg `-0.010376`, median `-0.014252`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.082794`, avg `0.007481`, median `0.023936`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.146577`, avg `0.018653`, median `0.052632`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.020006`, avg `-0.008905`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.021979`, avg `-0.013151`, median `-0.019358`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.025346`, avg `-0.012472`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.076633`, avg `0.003999`, median `0.019252`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.137228`, avg `0.00823`, median `0.048285`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.018648`, avg `-0.01041`, median `-0.010671`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.018952`, avg `-0.014954`, median `-0.021882`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.5625`, primary_mae `0.032381`, avg `-0.018503`, median `-0.035238`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.084001`, avg `0.027599`, median `0.019624`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.1875`, primary_mae `0.07904`, avg `0.082436`, median `0.086109`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.018282`, avg `-0.00623`, median `-0.005438`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.021457`, avg `-0.00985`, median `-0.015005`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.025959`, avg `-0.010944`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.059686`, avg `0.014118`, median `0.015565`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.076289`, avg `0.037524`, median `0.052147`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.018282`, avg `-0.00623`, median `-0.005438`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.021457`, avg `-0.00985`, median `-0.015005`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.025959`, avg `-0.010944`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.059686`, avg `0.014118`, median `0.015565`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.076289`, avg `0.037524`, median `0.052147`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.019406`, avg `-0.007474`, median `-0.005583`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.023641`, avg `-0.010743`, median `-0.016241`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.027082`, avg `-0.012662`, median `-0.010944`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.063233`, avg `0.00677`, median `0.009546`
- 60d: sample `40`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.093106`, avg `0.017781`, median `0.048423`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.017158`, avg `-0.004987`, median `-0.005438`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.019273`, avg `-0.008957`, median `-0.013338`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.024835`, avg `-0.009226`, median `-0.014057`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.056139`, avg `0.021466`, median `0.015719`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.325`, primary_mae `0.059473`, avg `0.057268`, median `0.056639`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.018282`, avg `-0.00623`, median `-0.005438`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.021457`, avg `-0.00985`, median `-0.015005`
- 10d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.025959`, avg `-0.010944`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.059686`, avg `0.014118`, median `0.015565`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.076289`, avg `0.037524`, median `0.052147`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.7`, primary_closer `0.375`, primary_mae `0.019106`, avg `-0.009935`, median `-0.010058`
- 5d: sample `40`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.020765`, avg `-0.014566`, median `-0.017873`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.475`, primary_mae `0.031137`, avg `-0.0145`, median `-0.018361`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.067866`, avg `0.018346`, median `0.009546`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.35`, primary_mae `0.063723`, avg `0.052208`, median `0.059055`

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
