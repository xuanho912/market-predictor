# Historical Replay Benchmark

Generated at: `2026-07-06T14:44:32.122805+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.014709`
- secondary_mean_absolute_error: `0.01297`
- primary_error_advantage: `-0.001739`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.018144`
- secondary_mean_absolute_error: `0.016371`
- primary_error_advantage: `-0.001773`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.025636`
- secondary_mean_absolute_error: `0.018705`
- primary_error_advantage: `-0.006931`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.044154`
- secondary_mean_absolute_error: `0.044823`
- primary_error_advantage: `0.000669`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.070543`
- secondary_mean_absolute_error: `0.054345`
- primary_error_advantage: `-0.016198`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.013576`, as_primary `0`, as_primary_hit `None`, avg `-0.001157`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.016041`, as_primary `0`, as_primary_hit `None`, avg `-0.001785`, median `0.002195`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.019005`, as_primary `0`, as_primary_hit `None`, avg `0.002683`, median `1.4e-05`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.029209`, as_primary `0`, as_primary_hit `None`, avg `0.005851`, median `0.01072`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.053127`, as_primary `0`, as_primary_hit `None`, avg `0.00419`, median `-0.007739`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.014709`, as_primary `80`, as_primary_hit `0.5`, avg `-0.001157`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.018144`, as_primary `80`, as_primary_hit `0.5375`, avg `-0.001785`, median `0.002195`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.025636`, as_primary `80`, as_primary_hit `0.5`, avg `0.002683`, median `1.4e-05`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.044154`, as_primary `80`, as_primary_hit `0.675`, avg `0.005851`, median `0.01072`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.070543`, as_primary `80`, as_primary_hit `0.4625`, avg `0.00419`, median `-0.007739`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.013723`, as_primary `0`, as_primary_hit `None`, avg `-0.001157`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.017084`, as_primary `0`, as_primary_hit `None`, avg `-0.001785`, median `0.002195`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.020323`, as_primary `0`, as_primary_hit `None`, avg `0.002683`, median `1.4e-05`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.055074`, as_primary `0`, as_primary_hit `None`, avg `0.005851`, median `0.01072`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.065894`, as_primary `0`, as_primary_hit `None`, avg `0.00419`, median `-0.007739`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.012909`, as_primary `0`, as_primary_hit `None`, avg `-0.001157`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.015819`, as_primary `0`, as_primary_hit `None`, avg `-0.001785`, median `0.002195`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.01796`, as_primary `0`, as_primary_hit `None`, avg `0.002683`, median `1.4e-05`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.028277`, as_primary `0`, as_primary_hit `None`, avg `0.005851`, median `0.01072`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.050546`, as_primary `0`, as_primary_hit `None`, avg `0.00419`, median `-0.007739`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.009982`, avg `-0.002489`, median `-0.00191`
- 5d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.011281`, avg `0.002442`, median `0.003801`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.011765`, avg `0.003657`, median `0.002926`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.028366`, avg `0.00558`, median `0.01201`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.058062`, avg `-0.038559`, median `-0.038871`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.015292`, avg `-0.002275`, median `-0.00052`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.01751`, avg `-0.004258`, median `-0.001663`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.275`, primary_mae `0.026016`, avg `0.003442`, median `-0.004481`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.225`, primary_mae `0.053711`, avg `0.011208`, median `0.011873`
- 60d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.076542`, avg `0.03519`, median `0.051612`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.018269`, avg `0.002412`, median `0.003542`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.026275`, avg `-0.001068`, median `-0.004072`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.038748`, avg `0.00019`, median `0.004339`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.85`, primary_mae `0.040831`, avg `-0.004591`, median `0.005514`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.071026`, avg `-0.015059`, median `-0.012825`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.009982`, avg `-0.002489`, median `-0.00191`
- 5d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.011281`, avg `0.002442`, median `0.003801`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.011765`, avg `0.003657`, median `0.002926`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.028366`, avg `0.00558`, median `0.01201`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.058062`, avg `-0.038559`, median `-0.038871`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.4`, primary_mae `0.016284`, avg `-0.000713`, median `0.000388`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.4667`, primary_mae `0.020431`, avg `-0.003194`, median `-0.001663`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.3333`, primary_mae `0.03026`, avg `0.002358`, median `-0.001735`
- 20d: sample `60`, primary_hit `0.6667`, primary_closer `0.4333`, primary_mae `0.049417`, avg `0.005942`, median `0.008744`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.074704`, avg `0.01844`, median `0.015994`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.009982, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.011281, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.011765, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.028366, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.058062, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012909, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014709, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.009982, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015819, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018144, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.011281, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01796, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025636, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.011765, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028277, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055074, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.028366, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050546, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070543, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.058062, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.013847`, avg `-0.013768`, median `-0.010064`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.014854`, avg `-0.011794`, median `-0.013366`
- 10d: sample `8`, primary_hit `0.0`, primary_closer `0.125`, primary_mae `0.01521`, avg `-0.01387`, median `-0.012789`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.04812`, avg `0.016823`, median `0.024617`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.102514`, avg `0.026683`, median `0.029112`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.015824`, avg `-0.011437`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.018848`, avg `-0.010644`, median `-0.012995`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.017041`, avg `-0.004877`, median `-0.008733`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.047445`, avg `0.016618`, median `0.020913`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.095941`, avg `0.030848`, median `0.037982`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.015184`, avg `0.001913`, median `0.003542`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.025256`, avg `-0.000529`, median `-0.004072`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.040086`, avg `-0.002581`, median `-0.002915`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.8125`, primary_mae `0.044784`, avg `-0.008432`, median `0.007521`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.075809`, avg `-0.02226`, median `-0.014079`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.014709`, avg `-0.001157`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.018144`, avg `-0.001785`, median `0.002195`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.025636`, avg `0.002683`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.044154`, avg `0.005851`, median `0.01072`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.3625`, primary_mae `0.070543`, avg `0.00419`, median `-0.007739`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.014709`, avg `-0.001157`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.018144`, avg `-0.001785`, median `0.002195`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.025636`, avg `0.002683`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.044154`, avg `0.005851`, median `0.01072`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.3625`, primary_mae `0.070543`, avg `0.00419`, median `-0.007739`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.014709`, avg `-0.001157`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.018144`, avg `-0.001785`, median `0.002195`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.025636`, avg `0.002683`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.044154`, avg `0.005851`, median `0.01072`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.3625`, primary_mae `0.070543`, avg `0.00419`, median `-0.007739`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.014709`, avg `-0.001157`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.018144`, avg `-0.001785`, median `0.002195`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.025636`, avg `0.002683`, median `1.4e-05`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.044154`, avg `0.005851`, median `0.01072`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.3625`, primary_mae `0.070543`, avg `0.00419`, median `-0.007739`

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
