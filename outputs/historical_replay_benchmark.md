# Historical Replay Benchmark

Generated at: `2026-07-24T21:35:59.208054+00:00`
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
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.023473`
- secondary_mean_absolute_error: `0.020778`
- primary_error_advantage: `-0.002695`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.032891`
- secondary_mean_absolute_error: `0.024618`
- primary_error_advantage: `-0.008273`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.03761`
- secondary_mean_absolute_error: `0.028934`
- primary_error_advantage: `-0.008676`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.079921`
- secondary_mean_absolute_error: `0.055724`
- primary_error_advantage: `-0.024197`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.118764`
- secondary_mean_absolute_error: `0.085367`
- primary_error_advantage: `-0.033397`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.019182`, as_primary `0`, as_primary_hit `None`, avg `-0.004114`, median `0.000402`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.022128`, as_primary `0`, as_primary_hit `None`, avg `-0.005433`, median `-0.001279`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.024522`, as_primary `0`, as_primary_hit `None`, avg `0.004266`, median `0.005949`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.041936`, as_primary `0`, as_primary_hit `None`, avg `0.013789`, median `0.020543`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.074524`, as_primary `0`, as_primary_hit `None`, avg `0.02243`, median `0.054511`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.02052`, as_primary `0`, as_primary_hit `None`, avg `-0.004114`, median `0.000402`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.025553`, as_primary `0`, as_primary_hit `None`, avg `-0.005433`, median `-0.001279`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.030356`, as_primary `0`, as_primary_hit `None`, avg `0.004266`, median `0.005949`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.05962`, as_primary `0`, as_primary_hit `None`, avg `0.013789`, median `0.020543`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.085516`, as_primary `0`, as_primary_hit `None`, avg `0.02243`, median `0.054511`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.023473`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.004114`, median `0.000402`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.032891`, as_primary `80`, as_primary_hit `0.475`, avg `-0.005433`, median `-0.001279`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.03761`, as_primary `80`, as_primary_hit `0.575`, avg `0.004266`, median `0.005949`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.079921`, as_primary `80`, as_primary_hit `0.6375`, avg `0.013789`, median `0.020543`
- 60d: sample `80`, direction_hit `0.3375`, path_mae `0.118764`, as_primary `80`, as_primary_hit `0.6625`, avg `0.02243`, median `0.054511`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.019128`, as_primary `0`, as_primary_hit `None`, avg `-0.004114`, median `0.000402`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.02211`, as_primary `0`, as_primary_hit `None`, avg `-0.005433`, median `-0.001279`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.024548`, as_primary `0`, as_primary_hit `None`, avg `0.004266`, median `0.005949`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.04346`, as_primary `0`, as_primary_hit `None`, avg `0.013789`, median `0.020543`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.076517`, as_primary `0`, as_primary_hit `None`, avg `0.02243`, median `0.054511`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.022442`, avg `-0.005026`, median `0.000952`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.030031`, avg `-0.008456`, median `-0.000371`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.023242`, avg `-0.004364`, median `-0.006514`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.068775`, avg `0.010637`, median `0.019669`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.09705`, avg `0.033692`, median `0.048423`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.024504`, avg `-0.003201`, median `-0.003306`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.035751`, avg `-0.002409`, median `-0.00269`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.051978`, avg `0.012896`, median `0.025887`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.325`, primary_mae `0.091067`, avg `0.01694`, median `0.030849`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.140479`, avg `0.011168`, median `0.063592`

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
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.024504`, avg `-0.003201`, median `-0.003306`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.035751`, avg `-0.002409`, median `-0.00269`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.051978`, avg `0.012896`, median `0.025887`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.325`, primary_mae `0.091067`, avg `0.01694`, median `0.030849`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.140479`, avg `0.011168`, median `0.063592`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.022442`, avg `-0.005026`, median `0.000952`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.030031`, avg `-0.008456`, median `-0.000371`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.023242`, avg `-0.004364`, median `-0.006514`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.068775`, avg `0.010637`, median `0.019669`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.09705`, avg `0.033692`, median `0.048423`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.022442, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.030031, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.023242, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.068775, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.09705, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019128, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023473, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.022442, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02211, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032891, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.030031, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024522, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03761, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.023242, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041936, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.079921, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.068775, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074524, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.118764, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.09705, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.024645`, avg `-0.01363`, median `-0.018199`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.030668`, avg `-0.025133`, median `-0.031479`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.017684`, avg `-0.011762`, median `-0.009593`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.066016`, avg `-0.007317`, median `-0.006533`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.106133`, avg `0.011993`, median `0.004276`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.030697`, avg `-0.00691`, median `-0.00023`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.040575`, avg `-0.014243`, median `-0.008746`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.024855`, avg `-0.003191`, median `-0.006514`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.084679`, avg `0.018931`, median `0.031583`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.136934`, avg `0.050625`, median `0.06438`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.022434`, avg `-0.00694`, median `-0.007873`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.036043`, avg `-0.016389`, median `-0.011498`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.055797`, avg `0.003858`, median `0.022725`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.105668`, avg `0.000178`, median `0.021621`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.177209`, avg `-0.012115`, median `0.011899`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.023473`, avg `-0.004114`, median `0.000402`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.032891`, avg `-0.005433`, median `-0.001279`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.03761`, avg `0.004266`, median `0.005949`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.079921`, avg `0.013789`, median `0.020543`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.375`, primary_mae `0.118764`, avg `0.02243`, median `0.054511`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.023473`, avg `-0.004114`, median `0.000402`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.032891`, avg `-0.005433`, median `-0.001279`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.03761`, avg `0.004266`, median `0.005949`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.079921`, avg `0.013789`, median `0.020543`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.375`, primary_mae `0.118764`, avg `0.02243`, median `0.054511`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.022442`, avg `-0.005026`, median `0.000952`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.030031`, avg `-0.008456`, median `-0.000371`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.023242`, avg `-0.004364`, median `-0.006514`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.068775`, avg `0.010637`, median `0.019669`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.09705`, avg `0.033692`, median `0.048423`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.024504`, avg `-0.003201`, median `-0.003306`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.035751`, avg `-0.002409`, median `-0.00269`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.051978`, avg `0.012896`, median `0.025887`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.325`, primary_mae `0.091067`, avg `0.01694`, median `0.030849`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.140479`, avg `0.011168`, median `0.063592`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.023473`, avg `-0.004114`, median `0.000402`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.032891`, avg `-0.005433`, median `-0.001279`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.03761`, avg `0.004266`, median `0.005949`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.079921`, avg `0.013789`, median `0.020543`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.375`, primary_mae `0.118764`, avg `0.02243`, median `0.054511`

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
