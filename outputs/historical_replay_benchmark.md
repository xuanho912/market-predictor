# Historical Replay Benchmark

Generated at: `2026-10-01T02:04:38.308746+00:00`
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
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.02188`
- secondary_mean_absolute_error: `0.016025`
- primary_error_advantage: `-0.005855`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.027394`
- secondary_mean_absolute_error: `0.01821`
- primary_error_advantage: `-0.009184`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.038369`
- secondary_mean_absolute_error: `0.027869`
- primary_error_advantage: `-0.0105`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.072823`
- secondary_mean_absolute_error: `0.041027`
- primary_error_advantage: `-0.031796`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `-0.6`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.09451`
- secondary_mean_absolute_error: `0.058646`
- primary_error_advantage: `-0.035864`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.016271`, as_primary `0`, as_primary_hit `None`, avg `-0.006249`, median `-0.003446`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.0179`, as_primary `0`, as_primary_hit `None`, avg `-0.009919`, median `-0.006363`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.027966`, as_primary `0`, as_primary_hit `None`, avg `-0.007588`, median `-0.002583`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.040924`, as_primary `0`, as_primary_hit `None`, avg `0.007414`, median `0.015571`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.058205`, as_primary `0`, as_primary_hit `None`, avg `0.044742`, median `0.059055`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.015854`, as_primary `0`, as_primary_hit `None`, avg `-0.006249`, median `-0.003446`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.020034`, as_primary `0`, as_primary_hit `None`, avg `-0.009919`, median `-0.006363`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.035915`, as_primary `0`, as_primary_hit `None`, avg `-0.007588`, median `-0.002583`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.061139`, as_primary `0`, as_primary_hit `None`, avg `0.007414`, median `0.015571`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.059401`, as_primary `0`, as_primary_hit `None`, avg `0.044742`, median `0.059055`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.02188`, as_primary `80`, as_primary_hit `0.425`, avg `-0.006249`, median `-0.003446`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.027394`, as_primary `80`, as_primary_hit `0.425`, avg `-0.009919`, median `-0.006363`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.038369`, as_primary `80`, as_primary_hit `0.475`, avg `-0.007588`, median `-0.002583`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.072823`, as_primary `80`, as_primary_hit `0.6125`, avg `0.007414`, median `0.015571`
- 60d: sample `80`, direction_hit `0.2`, path_mae `0.09451`, as_primary `80`, as_primary_hit `0.8`, avg `0.044742`, median `0.059055`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.016025`, as_primary `0`, as_primary_hit `None`, avg `-0.006249`, median `-0.003446`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.01821`, as_primary `0`, as_primary_hit `None`, avg `-0.009919`, median `-0.006363`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.027869`, as_primary `0`, as_primary_hit `None`, avg `-0.007588`, median `-0.002583`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.041027`, as_primary `0`, as_primary_hit `None`, avg `0.007414`, median `0.015571`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.058646`, as_primary `0`, as_primary_hit `None`, avg `0.044742`, median `0.059055`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.3625`, primary_mae `0.02188`, avg `-0.006249`, median `-0.003446`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.027394`, avg `-0.009919`, median `-0.006363`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.325`, primary_mae `0.038369`, avg `-0.007588`, median `-0.002583`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.25`, primary_mae `0.072823`, avg `0.007414`, median `0.015571`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.2625`, primary_mae `0.09451`, avg `0.044742`, median `0.059055`

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
- 3d: sample `40`, primary_hit `0.7`, primary_closer `0.3`, primary_mae `0.029717`, avg `-0.013611`, median `-0.012143`
- 5d: sample `40`, primary_hit `0.75`, primary_closer `0.275`, primary_mae `0.034678`, avg `-0.017783`, median `-0.014934`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.042201`, avg `-0.012537`, median `-0.015452`
- 20d: sample `40`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.081413`, avg `0.004562`, median `0.007148`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.225`, primary_mae `0.129794`, avg `0.055232`, median `0.092349`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.014042`, avg `0.001112`, median `0.002549`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.02011`, avg `-0.002055`, median `0.001566`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.275`, primary_mae `0.034536`, avg `-0.002638`, median `0.004865`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.2`, primary_mae `0.064234`, avg `0.010266`, median `0.015876`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.3`, primary_mae `0.059226`, avg `0.034252`, median `0.041232`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.014042, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.02011, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.034536, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.064234, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.059226, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015854, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02188, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.014042, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0179, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027394, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.02011, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027869, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038369, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.034536, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040924, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072823, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.064234, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': -0.6, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058205, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.09451, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.059226, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.013033`, avg `0.000424`, median `0.00021`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.015054`, avg `-0.001497`, median `0.001171`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.033695`, avg `0.009167`, median `0.005013`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.0`, primary_mae `0.0895`, avg `0.032707`, median `0.033594`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.069183`, avg `0.030837`, median `0.03603`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.008974`, avg `0.000782`, median `0.000437`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.014246`, avg `-0.002946`, median `0.001171`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.031964`, avg `0.004486`, median `0.006069`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.078464`, avg `0.018351`, median `0.025964`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.064261`, avg `0.021498`, median `0.030631`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.1875`, primary_mae `0.029629`, avg `-0.017353`, median `-0.014095`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.034288`, avg `-0.016818`, median `-0.013338`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.05363`, avg `0.000851`, median `0.012828`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.09154`, avg `0.019414`, median `0.039587`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.118715`, avg `0.069934`, median `0.114142`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.3625`, primary_mae `0.02188`, avg `-0.006249`, median `-0.003446`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.027394`, avg `-0.009919`, median `-0.006363`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.325`, primary_mae `0.038369`, avg `-0.007588`, median `-0.002583`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.25`, primary_mae `0.072823`, avg `0.007414`, median `0.015571`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.2625`, primary_mae `0.09451`, avg `0.044742`, median `0.059055`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.3625`, primary_mae `0.02188`, avg `-0.006249`, median `-0.003446`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.027394`, avg `-0.009919`, median `-0.006363`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.325`, primary_mae `0.038369`, avg `-0.007588`, median `-0.002583`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.25`, primary_mae `0.072823`, avg `0.007414`, median `0.015571`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.2625`, primary_mae `0.09451`, avg `0.044742`, median `0.059055`

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
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.3625`, primary_mae `0.02188`, avg `-0.006249`, median `-0.003446`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.027394`, avg `-0.009919`, median `-0.006363`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.325`, primary_mae `0.038369`, avg `-0.007588`, median `-0.002583`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.25`, primary_mae `0.072823`, avg `0.007414`, median `0.015571`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.2625`, primary_mae `0.09451`, avg `0.044742`, median `0.059055`

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
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.3625`, primary_mae `0.02188`, avg `-0.006249`, median `-0.003446`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.027394`, avg `-0.009919`, median `-0.006363`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.325`, primary_mae `0.038369`, avg `-0.007588`, median `-0.002583`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.25`, primary_mae `0.072823`, avg `0.007414`, median `0.015571`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.2625`, primary_mae `0.09451`, avg `0.044742`, median `0.059055`

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
