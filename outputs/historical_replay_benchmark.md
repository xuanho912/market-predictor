# Historical Replay Benchmark

Generated at: `2026-07-26T13:59:47.681427+00:00`
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
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.019847`
- secondary_mean_absolute_error: `0.018949`
- primary_error_advantage: `-0.000898`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.027227`
- secondary_mean_absolute_error: `0.022961`
- primary_error_advantage: `-0.004266`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.03699`
- secondary_mean_absolute_error: `0.028267`
- primary_error_advantage: `-0.008723`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.069641`
- secondary_mean_absolute_error: `0.053154`
- primary_error_advantage: `-0.016487`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.094761`
- secondary_mean_absolute_error: `0.074495`
- primary_error_advantage: `-0.020266`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.017647`, as_primary `0`, as_primary_hit `None`, avg `-0.000738`, median `0.000737`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.020853`, as_primary `0`, as_primary_hit `None`, avg `0.001178`, median `0.001032`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.025442`, as_primary `0`, as_primary_hit `None`, avg `0.009577`, median `0.017629`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.039562`, as_primary `0`, as_primary_hit `None`, avg `0.019284`, median `0.021311`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.067375`, as_primary `0`, as_primary_hit `None`, avg `0.033429`, median `0.058788`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.018706`, as_primary `20`, as_primary_hit `0.6`, avg `-0.000738`, median `0.000737`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.023881`, as_primary `20`, as_primary_hit `0.7`, avg `0.001178`, median `0.001032`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.029599`, as_primary `20`, as_primary_hit `0.7`, avg `0.009577`, median `0.017629`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.056178`, as_primary `20`, as_primary_hit `0.8`, avg `0.019284`, median `0.021311`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.074227`, as_primary `20`, as_primary_hit `0.95`, avg `0.033429`, median `0.058788`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.019831`, as_primary `60`, as_primary_hit `0.5167`, avg `-0.000738`, median `0.000737`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.027243`, as_primary `60`, as_primary_hit `0.4833`, avg `0.001178`, median `0.001032`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.03708`, as_primary `60`, as_primary_hit `0.65`, avg `0.009577`, median `0.017629`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.070513`, as_primary `60`, as_primary_hit `0.6167`, avg `0.019284`, median `0.021311`
- 60d: sample `80`, direction_hit `0.2875`, path_mae `0.095177`, as_primary `60`, as_primary_hit `0.6333`, avg `0.033429`, median `0.058788`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.017565`, as_primary `0`, as_primary_hit `None`, avg `-0.000738`, median `0.000737`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.020836`, as_primary `0`, as_primary_hit `None`, avg `0.001178`, median `0.001032`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.025848`, as_primary `0`, as_primary_hit `None`, avg `0.009577`, median `0.017629`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.040602`, as_primary `0`, as_primary_hit `None`, avg `0.019284`, median `0.021311`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.069781`, as_primary `0`, as_primary_hit `None`, avg `0.033429`, median `0.058788`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.4167`, primary_mae `0.019646`, avg `0.001791`, median `0.004286`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.024676`, avg `0.006454`, median `0.00653`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.031259`, avg `0.012552`, median `0.017629`
- 20d: sample `60`, primary_hit `0.5167`, primary_closer `0.4333`, primary_mae `0.058441`, avg `0.026775`, median `0.024768`
- 60d: sample `60`, primary_hit `0.5167`, primary_closer `0.4333`, primary_mae `0.06882`, avg `0.050485`, median `0.059526`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.02045`, avg `-0.008325`, median `-0.010263`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.034879`, avg `-0.01465`, median `-0.011498`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.054181`, avg `0.000649`, median `0.019179`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.103241`, avg `-0.003186`, median `0.019486`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.172582`, avg `-0.017738`, median `0.011899`

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
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.01519`, avg `0.001724`, median `0.002181`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.018703`, avg `0.004765`, median `0.005524`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.525`, primary_mae `0.022001`, avg `0.006258`, median `0.005119`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.048215`, avg `0.021629`, median `0.020543`
- 60d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.049043`, avg `0.055691`, median `0.058364`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.01519, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.018703, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.022001, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.048215, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.049043, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017565, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019831, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.01519, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020836, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027243, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.018703, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025442, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03708, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.022001, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039562, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070513, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.048215, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067375, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.095177, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.049043, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.016338`, avg `0.00231`, median `0.005341`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.012766`, avg `0.011766`, median `0.015644`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.018531`, avg `0.011279`, median `0.01205`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.036784`, avg `0.034564`, median `0.031643`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.625`, primary_mae `0.030819`, avg `0.096074`, median `0.11635`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.014577`, avg `0.003257`, median `0.003357`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.017903`, avg `0.00805`, median `0.008828`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.022987`, avg `0.012908`, median `0.016702`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.041199`, avg `0.033057`, median `0.029448`
- 60d: sample `16`, primary_hit `1.0`, primary_closer `0.625`, primary_mae `0.028362`, avg `0.101596`, median `0.11635`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.022434`, avg `-0.00694`, median `-0.007873`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.036043`, avg `-0.016389`, median `-0.011498`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.055797`, avg `0.003858`, median `0.022725`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.105668`, avg `0.000178`, median `0.021621`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.177209`, avg `-0.012115`, median `0.011899`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.019847`, avg `-0.000738`, median `0.000737`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.027227`, avg `0.001178`, median `0.001032`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.03699`, avg `0.009577`, median `0.017629`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.4125`, primary_mae `0.069641`, avg `0.019284`, median `0.021311`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.4375`, primary_mae `0.094761`, avg `0.033429`, median `0.058788`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.019847`, avg `-0.000738`, median `0.000737`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.027227`, avg `0.001178`, median `0.001032`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.03699`, avg `0.009577`, median `0.017629`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.4125`, primary_mae `0.069641`, avg `0.019284`, median `0.021311`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.4375`, primary_mae `0.094761`, avg `0.033429`, median `0.058788`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.01519`, avg `0.001724`, median `0.002181`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.018703`, avg `0.004765`, median `0.005524`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.525`, primary_mae `0.022001`, avg `0.006258`, median `0.005119`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.048215`, avg `0.021629`, median `0.020543`
- 60d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.049043`, avg `0.055691`, median `0.058364`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.024504`, avg `-0.003201`, median `-0.003306`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.035751`, avg `-0.002409`, median `-0.00269`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.051978`, avg `0.012896`, median `0.025887`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.325`, primary_mae `0.091067`, avg `0.01694`, median `0.030849`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.140479`, avg `0.011168`, median `0.063592`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.019847`, avg `-0.000738`, median `0.000737`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.027227`, avg `0.001178`, median `0.001032`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.03699`, avg `0.009577`, median `0.017629`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.4125`, primary_mae `0.069641`, avg `0.019284`, median `0.021311`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.4375`, primary_mae `0.094761`, avg `0.033429`, median `0.058788`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.028558`, avg `0.001924`, median `0.008855`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.036623`, avg `0.009831`, median `0.011005`
- 10d: sample `20`, primary_hit `0.15`, primary_closer `0.15`, primary_mae `0.049775`, avg `0.025142`, median `0.031485`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.078893`, avg `0.037066`, median `0.057289`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.108376`, avg `0.040074`, median `0.07049`

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
