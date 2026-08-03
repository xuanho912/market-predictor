# Historical Replay Benchmark

Generated at: `2026-08-03T23:57:21.988390+00:00`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.017412`
- secondary_mean_absolute_error: `0.016814`
- primary_error_advantage: `-0.000598`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.023549`
- secondary_mean_absolute_error: `0.019388`
- primary_error_advantage: `-0.004161`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.2875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.425`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.036231`
- secondary_mean_absolute_error: `0.027716`
- primary_error_advantage: `-0.008515`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.068433`
- secondary_mean_absolute_error: `0.055352`
- primary_error_advantage: `-0.013081`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.102915`
- secondary_mean_absolute_error: `0.076834`
- primary_error_advantage: `-0.026081`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.01581`, as_primary `0`, as_primary_hit `None`, avg `0.000415`, median `0.000983`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.017927`, as_primary `0`, as_primary_hit `None`, avg `-1.5e-05`, median `0.002728`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.022729`, as_primary `0`, as_primary_hit `None`, avg `0.001177`, median `-0.006487`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.037228`, as_primary `0`, as_primary_hit `None`, avg `0.003883`, median `0.005719`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.066996`, as_primary `0`, as_primary_hit `None`, avg `0.00449`, median `0.008242`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.017768`, as_primary `40`, as_primary_hit `0.525`, avg `0.000415`, median `0.000983`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.021431`, as_primary `40`, as_primary_hit `0.575`, avg `-1.5e-05`, median `0.002728`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.030169`, as_primary `40`, as_primary_hit `0.225`, avg `0.001177`, median `-0.006487`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.059042`, as_primary `40`, as_primary_hit `0.375`, avg `0.003883`, median `0.005719`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.081911`, as_primary `40`, as_primary_hit `0.425`, avg `0.00449`, median `0.008242`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.017328`, as_primary `40`, as_primary_hit `0.575`, avg `0.000415`, median `0.000983`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.024126`, as_primary `40`, as_primary_hit `0.625`, avg `-1.5e-05`, median `0.002728`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.0363`, as_primary `40`, as_primary_hit `0.65`, avg `0.001177`, median `-0.006487`
- 20d: sample `80`, direction_hit `0.45`, path_mae `0.07101`, as_primary `40`, as_primary_hit `0.725`, avg `0.003883`, median `0.005719`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.100239`, as_primary `40`, as_primary_hit `0.65`, avg `0.00449`, median `0.008242`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.015226`, as_primary `0`, as_primary_hit `None`, avg `0.000415`, median `0.000983`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.016939`, as_primary `0`, as_primary_hit `None`, avg `-1.5e-05`, median `0.002728`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.022659`, as_primary `0`, as_primary_hit `None`, avg `0.001177`, median `-0.006487`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.036926`, as_primary `0`, as_primary_hit `None`, avg `0.003883`, median `0.005719`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.066782`, as_primary `0`, as_primary_hit `None`, avg `0.00449`, median `0.008242`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.55`, primary_mae `0.015878`, avg `-0.001485`, median `0.000402`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.4333`, primary_mae `0.019858`, avg `-0.001963`, median `0.002073`
- 10d: sample `60`, primary_hit `0.2833`, primary_closer `0.4667`, primary_mae `0.032067`, avg `-0.006072`, median `-0.009821`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.5`, primary_mae `0.067602`, avg `-0.010217`, median `-0.003053`
- 60d: sample `60`, primary_hit `0.45`, primary_closer `0.4667`, primary_mae `0.101134`, avg `-0.013683`, median `-0.009163`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.022014`, avg `0.006116`, median `0.009444`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.034623`, avg `0.005832`, median `0.009055`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.048721`, avg `0.022924`, median `0.027594`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.2`, primary_mae `0.070926`, avg `0.046183`, median `0.049277`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.108257`, avg `0.059007`, median `0.072959`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.55`, primary_mae `0.015878`, avg `-0.001485`, median `0.000402`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.4333`, primary_mae `0.019858`, avg `-0.001963`, median `0.002073`
- 10d: sample `60`, primary_hit `0.2833`, primary_closer `0.4667`, primary_mae `0.032067`, avg `-0.006072`, median `-0.009821`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.5`, primary_mae `0.067602`, avg `-0.010217`, median `-0.003053`
- 60d: sample `60`, primary_hit `0.45`, primary_closer `0.4667`, primary_mae `0.101134`, avg `-0.013683`, median `-0.009163`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.022014`, avg `0.006116`, median `0.009444`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.034623`, avg `0.005832`, median `0.009055`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.048721`, avg `0.022924`, median `0.027594`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.2`, primary_mae `0.070926`, avg `0.046183`, median `0.049277`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.108257`, avg `0.059007`, median `0.072959`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.015878, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.019858, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2833, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.032067, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.067602, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.101134, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015226, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017768, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.015878, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016939, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024126, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.019858, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.425, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022659, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0363, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2833, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.032067, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036926, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07101, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.067602, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066782, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.100239, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.101134, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.016804`, avg `-0.019958`, median `-0.02628`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.019505`, avg `-0.023775`, median `-0.021157`
- 10d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.017249`, avg `-0.017739`, median `-0.020733`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.062841`, avg `-0.016002`, median `-0.006591`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.108905`, avg `-0.011664`, median `-0.021705`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.02062`, avg `-0.00798`, median `-0.003521`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.6875`, primary_mae `0.022125`, avg `-0.013215`, median `-0.002011`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.5625`, primary_mae `0.014395`, avg `-0.010703`, median `-0.013277`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.625`, primary_mae `0.057776`, avg `-0.007255`, median `-0.001662`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.100663`, avg `0.001181`, median `0.005177`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.020746`, avg `0.007474`, median `0.009444`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.031287`, avg `0.006926`, median `0.009055`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.047302`, avg `0.026059`, median `0.027594`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.063343`, avg `0.044679`, median `0.047846`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.108213`, avg `0.059784`, median `0.084587`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.017412`, avg `0.000415`, median `0.000983`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.023549`, avg `-1.5e-05`, median `0.002728`
- 10d: sample `80`, primary_hit `0.2875`, primary_closer `0.4375`, primary_mae `0.036231`, avg `0.001177`, median `-0.006487`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.068433`, avg `0.003883`, median `0.005719`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.102915`, avg `0.00449`, median `0.008242`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.017412`, avg `0.000415`, median `0.000983`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.023549`, avg `-1.5e-05`, median `0.002728`
- 10d: sample `80`, primary_hit `0.2875`, primary_closer `0.4375`, primary_mae `0.036231`, avg `0.001177`, median `-0.006487`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.068433`, avg `0.003883`, median `0.005719`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.102915`, avg `0.00449`, median `0.008242`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.016538`, avg `-0.003619`, median `0.000402`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.015863`, avg `-0.00587`, median `0.001032`
- 10d: sample `40`, primary_hit `0.225`, primary_closer `0.5`, primary_mae `0.016172`, avg `-0.009891`, median `-0.011907`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.575`, primary_mae `0.046199`, avg `-0.009114`, median `-0.007545`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.074942`, avg `-0.006731`, median `-0.014105`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.022014`, avg `0.006116`, median `0.009444`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.034623`, avg `0.005832`, median `0.009055`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.048721`, avg `0.022924`, median `0.027594`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.2`, primary_mae `0.070926`, avg `0.046183`, median `0.049277`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.108257`, avg `0.059007`, median `0.072959`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.017412`, avg `0.000415`, median `0.000983`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.023549`, avg `-1.5e-05`, median `0.002728`
- 10d: sample `80`, primary_hit `0.2875`, primary_closer `0.4375`, primary_mae `0.036231`, avg `0.001177`, median `-0.006487`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.068433`, avg `0.003883`, median `0.005719`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.102915`, avg `0.00449`, median `0.008242`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.017412`, avg `0.000415`, median `0.000983`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.023549`, avg `-1.5e-05`, median `0.002728`
- 10d: sample `80`, primary_hit `0.2875`, primary_closer `0.4375`, primary_mae `0.036231`, avg `0.001177`, median `-0.006487`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.068433`, avg `0.003883`, median `0.005719`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.102915`, avg `0.00449`, median `0.008242`

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
