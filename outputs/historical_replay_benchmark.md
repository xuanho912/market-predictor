# Historical Replay Benchmark

Generated at: `2026-08-20T20:54:20.669906+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
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
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.018972`
- secondary_mean_absolute_error: `0.0152`
- primary_error_advantage: `-0.003772`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.022463`
- secondary_mean_absolute_error: `0.020434`
- primary_error_advantage: `-0.002029`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.0413`
- secondary_mean_absolute_error: `0.029278`
- primary_error_advantage: `-0.012022`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.075026`
- secondary_mean_absolute_error: `0.052914`
- primary_error_advantage: `-0.022112`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.087413`
- secondary_mean_absolute_error: `0.079271`
- primary_error_advantage: `-0.008142`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.015029`, as_primary `0`, as_primary_hit `None`, avg `0.002742`, median `0.00448`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.020384`, as_primary `0`, as_primary_hit `None`, avg `0.001266`, median `0.000776`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.026344`, as_primary `0`, as_primary_hit `None`, avg `0.001994`, median `0.006139`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.041657`, as_primary `0`, as_primary_hit `None`, avg `0.008154`, median `0.012779`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.064732`, as_primary `0`, as_primary_hit `None`, avg `0.018753`, median `0.031582`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.017682`, as_primary `0`, as_primary_hit `None`, avg `0.002742`, median `0.00448`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.026022`, as_primary `0`, as_primary_hit `None`, avg `0.001266`, median `0.000776`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.035531`, as_primary `0`, as_primary_hit `None`, avg `0.001994`, median `0.006139`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.065953`, as_primary `0`, as_primary_hit `None`, avg `0.008154`, median `0.012779`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.086219`, as_primary `0`, as_primary_hit `None`, avg `0.018753`, median `0.031582`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.018972`, as_primary `80`, as_primary_hit `0.6375`, avg `0.002742`, median `0.00448`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.022463`, as_primary `80`, as_primary_hit `0.5375`, avg `0.001266`, median `0.000776`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.0413`, as_primary `80`, as_primary_hit `0.55`, avg `0.001994`, median `0.006139`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.075026`, as_primary `80`, as_primary_hit `0.6375`, avg `0.008154`, median `0.012779`
- 60d: sample `80`, direction_hit `0.4125`, path_mae `0.087413`, as_primary `80`, as_primary_hit `0.5875`, avg `0.018753`, median `0.031582`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.01448`, as_primary `0`, as_primary_hit `None`, avg `0.002742`, median `0.00448`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.018108`, as_primary `0`, as_primary_hit `None`, avg `0.001266`, median `0.000776`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.025405`, as_primary `0`, as_primary_hit `None`, avg `0.001994`, median `0.006139`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.037562`, as_primary `0`, as_primary_hit `None`, avg `0.008154`, median `0.012779`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.064987`, as_primary `0`, as_primary_hit `None`, avg `0.018753`, median `0.031582`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.018972`, avg `0.002742`, median `0.00448`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.022463`, avg `0.001266`, median `0.000776`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.0413`, avg `0.001994`, median `0.006139`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.2875`, primary_mae `0.075026`, avg `0.008154`, median `0.012779`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.087413`, avg `0.018753`, median `0.031582`

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
- 3d: sample `40`, primary_hit `0.35`, primary_closer `0.275`, primary_mae `0.018303`, avg `0.000238`, median `0.002204`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.018282`, avg `-0.000919`, median `0.000781`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.031459`, avg `-0.004685`, median `-0.007304`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.061555`, avg `-0.005228`, median `0.003008`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.06083`, avg `-0.002358`, median `-0.019322`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.019641`, avg `0.005246`, median `0.006073`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.026644`, avg `0.003451`, median `0.000271`
- 10d: sample `40`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.051141`, avg `0.008672`, median `0.010562`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.2`, primary_mae `0.088497`, avg `0.021537`, median `0.017642`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.113996`, avg `0.039864`, median `0.063703`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.018303, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018282, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.031459, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.061555, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.06083, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01448, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018972, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.018303, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018108, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026022, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018282, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025405, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0413, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.031459, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037562, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075026, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.061555, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064732, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.087413, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.06083, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.01492`, avg `0.004174`, median `0.004727`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.022797`, avg `-0.000584`, median `0.002503`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.044431`, avg `-0.012003`, median `-0.011879`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.08622`, avg `-0.007642`, median `0.017926`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.102756`, avg `0.02301`, median `0.054898`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.018859`, avg `0.008212`, median `0.015726`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.024503`, avg `0.008494`, median `0.00786`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.045287`, avg `0.001963`, median `0.005114`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.085025`, avg `0.010246`, median `0.01836`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.128153`, avg `0.018362`, median `0.063703`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.020618`, avg `0.004447`, median `0.003955`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.030184`, avg `0.000942`, median `-0.009564`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.059396`, avg `0.019212`, median `0.020266`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.125`, primary_mae `0.103269`, avg `0.041125`, median `0.030431`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.11324`, avg `0.090602`, median `0.086025`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.018972`, avg `0.002742`, median `0.00448`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.022463`, avg `0.001266`, median `0.000776`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.0413`, avg `0.001994`, median `0.006139`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.2875`, primary_mae `0.075026`, avg `0.008154`, median `0.012779`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.087413`, avg `0.018753`, median `0.031582`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.018972`, avg `0.002742`, median `0.00448`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.022463`, avg `0.001266`, median `0.000776`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.0413`, avg `0.001994`, median `0.006139`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.2875`, primary_mae `0.075026`, avg `0.008154`, median `0.012779`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.087413`, avg `0.018753`, median `0.031582`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.35`, primary_closer `0.275`, primary_mae `0.018303`, avg `0.000238`, median `0.002204`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.018282`, avg `-0.000919`, median `0.000781`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.031459`, avg `-0.004685`, median `-0.007304`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.061555`, avg `-0.005228`, median `0.003008`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.06083`, avg `-0.002358`, median `-0.019322`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.024116`, avg `-0.000361`, median `0.001944`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.025768`, avg `-0.001806`, median `-0.003704`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.048631`, avg `0.005662`, median `0.008948`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.275`, primary_mae `0.077465`, avg `0.018377`, median `0.012779`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.425`, primary_mae `0.078113`, avg `0.039637`, median `0.033928`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.018972`, avg `0.002742`, median `0.00448`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.022463`, avg `0.001266`, median `0.000776`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.0413`, avg `0.001994`, median `0.006139`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.2875`, primary_mae `0.075026`, avg `0.008154`, median `0.012779`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.087413`, avg `0.018753`, median `0.031582`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.018972`, avg `0.002742`, median `0.00448`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.022463`, avg `0.001266`, median `0.000776`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.0413`, avg `0.001994`, median `0.006139`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.2875`, primary_mae `0.075026`, avg `0.008154`, median `0.012779`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.087413`, avg `0.018753`, median `0.031582`

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
