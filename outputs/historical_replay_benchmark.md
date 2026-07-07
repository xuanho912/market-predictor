# Historical Replay Benchmark

Generated at: `2026-07-07T15:18:00.652149+00:00`
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
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.014205`
- secondary_mean_absolute_error: `0.013387`
- primary_error_advantage: `-0.000818`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.016944`
- secondary_mean_absolute_error: `0.016193`
- primary_error_advantage: `-0.000751`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.022972`
- secondary_mean_absolute_error: `0.018772`
- primary_error_advantage: `-0.0042`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.041289`
- secondary_mean_absolute_error: `0.036596`
- primary_error_advantage: `-0.004693`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.074404`
- secondary_mean_absolute_error: `0.056871`
- primary_error_advantage: `-0.017533`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.013951`, as_primary `0`, as_primary_hit `None`, avg `-0.002818`, median `-0.00205`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.015766`, as_primary `0`, as_primary_hit `None`, avg `-0.0031`, median `0.001055`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.018652`, as_primary `0`, as_primary_hit `None`, avg `0.001685`, median `1.4e-05`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.026837`, as_primary `0`, as_primary_hit `None`, avg `0.006662`, median `0.011034`
- 60d: sample `80`, direction_hit `0.4875`, path_mae `0.057609`, as_primary `0`, as_primary_hit `None`, avg `0.005631`, median `-0.003484`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.014205`, as_primary `80`, as_primary_hit `0.45`, avg `-0.002818`, median `-0.00205`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.016944`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.0031`, median `0.001055`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.022972`, as_primary `80`, as_primary_hit `0.5`, avg `0.001685`, median `1.4e-05`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.041289`, as_primary `80`, as_primary_hit `0.6875`, avg `0.006662`, median `0.011034`
- 60d: sample `80`, direction_hit `0.4875`, path_mae `0.074404`, as_primary `80`, as_primary_hit `0.4875`, avg `0.005631`, median `-0.003484`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.014759`, as_primary `0`, as_primary_hit `None`, avg `-0.002818`, median `-0.00205`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.01742`, as_primary `0`, as_primary_hit `None`, avg `-0.0031`, median `0.001055`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.020829`, as_primary `0`, as_primary_hit `None`, avg `0.001685`, median `1.4e-05`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.051812`, as_primary `0`, as_primary_hit `None`, avg `0.006662`, median `0.011034`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.069314`, as_primary `0`, as_primary_hit `None`, avg `0.005631`, median `-0.003484`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.013224`, as_primary `0`, as_primary_hit `None`, avg `-0.002818`, median `-0.00205`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.015709`, as_primary `0`, as_primary_hit `None`, avg `-0.0031`, median `0.001055`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.01776`, as_primary `0`, as_primary_hit `None`, avg `0.001685`, median `1.4e-05`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.026908`, as_primary `0`, as_primary_hit `None`, avg `0.006662`, median `0.011034`
- 60d: sample `80`, direction_hit `0.4875`, path_mae `0.053406`, as_primary `0`, as_primary_hit `None`, avg `0.005631`, median `-0.003484`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.014205`, avg `-0.002818`, median `-0.00205`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.016944`, avg `-0.0031`, median `0.001055`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.022972`, avg `0.001685`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.45`, primary_mae `0.041289`, avg `0.006662`, median `0.011034`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.074404`, avg `0.005631`, median `-0.003484`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.325`, primary_mae `0.010977`, avg `-0.001107`, median `-0.00052`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.014444`, avg `-0.001287`, median `0.00286`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.021585`, avg `0.001315`, median `1.4e-05`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.65`, primary_mae `0.034387`, avg `-0.000154`, median `0.009961`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.058144`, avg `-0.014785`, median `-0.026294`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.017434`, avg `-0.004529`, median `-0.008109`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.019444`, avg `-0.004913`, median `-0.005909`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.02436`, avg `0.002056`, median `0.000604`
- 20d: sample `40`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.04819`, avg `0.013478`, median `0.015289`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.35`, primary_mae `0.090663`, avg `0.026047`, median `0.024773`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.010977, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014444, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.021585, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.034387, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.058144, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013224, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014759, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.010977, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015709, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01742, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014444, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01776, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022972, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.021585, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026837, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051812, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.034387, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053406, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074404, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.058144, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.013219`, avg `-0.013768`, median `-0.010064`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.014854`, avg `-0.011794`, median `-0.013366`
- 10d: sample `8`, primary_hit `0.0`, primary_closer `0.125`, primary_mae `0.01521`, avg `-0.01387`, median `-0.012789`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.04812`, avg `0.016823`, median `0.024617`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.102514`, avg `0.026683`, median `0.029112`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.016794`, avg `-0.010153`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.017458`, avg `-0.010515`, median `-0.008697`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.016209`, avg `-0.007306`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.046367`, avg `0.017695`, median `0.020913`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.086852`, avg `0.040757`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.016794`, avg `-0.010153`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.017458`, avg `-0.010515`, median `-0.008697`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.016209`, avg `-0.007306`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.046367`, avg `0.017695`, median `0.020913`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.086852`, avg `0.040757`, median `0.052814`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.014205`, avg `-0.002818`, median `-0.00205`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.016944`, avg `-0.0031`, median `0.001055`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.022972`, avg `0.001685`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.45`, primary_mae `0.041289`, avg `0.006662`, median `0.011034`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.074404`, avg `0.005631`, median `-0.003484`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.014205`, avg `-0.002818`, median `-0.00205`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.016944`, avg `-0.0031`, median `0.001055`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.022972`, avg `0.001685`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.45`, primary_mae `0.041289`, avg `0.006662`, median `0.011034`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.074404`, avg `0.005631`, median `-0.003484`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.014205`, avg `-0.002818`, median `-0.00205`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.016944`, avg `-0.0031`, median `0.001055`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.022972`, avg `0.001685`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.45`, primary_mae `0.041289`, avg `0.006662`, median `0.011034`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.074404`, avg `0.005631`, median `-0.003484`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.3875`, primary_mae `0.014205`, avg `-0.002818`, median `-0.00205`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.016944`, avg `-0.0031`, median `0.001055`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.022972`, avg `0.001685`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.45`, primary_mae `0.041289`, avg `0.006662`, median `0.011034`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.074404`, avg `0.005631`, median `-0.003484`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.014518`, avg `-0.006226`, median `-0.004103`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.015007`, avg `-0.005116`, median `0.002195`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.013662`, avg `-0.001491`, median `-0.003297`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.475`, primary_mae `0.040805`, avg `0.007909`, median `0.012625`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.275`, primary_mae `0.07732`, avg `-0.0041`, median `-0.017782`

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
