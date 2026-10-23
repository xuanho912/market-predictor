# Historical Replay Benchmark

Generated at: `2026-10-23T23:18:14.152787+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.019532`
- secondary_mean_absolute_error: `0.017083`
- primary_error_advantage: `-0.002449`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.019032`
- secondary_mean_absolute_error: `0.018531`
- primary_error_advantage: `-0.000501`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.026156`
- secondary_mean_absolute_error: `0.026435`
- primary_error_advantage: `0.000279`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.043948`
- secondary_mean_absolute_error: `0.038424`
- primary_error_advantage: `-0.005524`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.425`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.056245`
- secondary_mean_absolute_error: `0.051126`
- primary_error_advantage: `-0.005119`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.016047`, as_primary `0`, as_primary_hit `None`, avg `0.001099`, median `-1.2e-05`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.0175`, as_primary `0`, as_primary_hit `None`, avg `0.001209`, median `0.003203`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.021543`, as_primary `0`, as_primary_hit `None`, avg `0.008074`, median `0.007534`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.026788`, as_primary `0`, as_primary_hit `None`, avg `0.015819`, median `0.016711`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.045679`, as_primary `0`, as_primary_hit `None`, avg `0.03864`, median `0.048873`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.016708`, as_primary `20`, as_primary_hit `0.6`, avg `0.001099`, median `-1.2e-05`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.018897`, as_primary `20`, as_primary_hit `0.55`, avg `0.001209`, median `0.003203`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.026425`, as_primary `20`, as_primary_hit `0.55`, avg `0.008074`, median `0.007534`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.04035`, as_primary `20`, as_primary_hit `0.7`, avg `0.015819`, median `0.016711`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.050478`, as_primary `20`, as_primary_hit `0.65`, avg `0.03864`, median `0.048873`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.019843`, as_primary `60`, as_primary_hit `0.4667`, avg `0.001099`, median `-1.2e-05`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018743`, as_primary `60`, as_primary_hit `0.55`, avg `0.001209`, median `0.003203`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.027415`, as_primary `60`, as_primary_hit `0.65`, avg `0.008074`, median `0.007534`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.04552`, as_primary `60`, as_primary_hit `0.7333`, avg `0.015819`, median `0.016711`
- 60d: sample `80`, direction_hit `0.2125`, path_mae `0.056893`, as_primary `60`, as_primary_hit `0.8333`, avg `0.03864`, median `0.048873`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015774`, as_primary `0`, as_primary_hit `None`, avg `0.001099`, median `-1.2e-05`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.017106`, as_primary `0`, as_primary_hit `None`, avg `0.001209`, median `0.003203`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.020889`, as_primary `0`, as_primary_hit `None`, avg `0.008074`, median `0.007534`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.025588`, as_primary `0`, as_primary_hit `None`, avg `0.015819`, median `0.016711`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.043025`, as_primary `0`, as_primary_hit `None`, avg `0.03864`, median `0.048873`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.019532`, avg `0.001099`, median `-1.2e-05`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.019032`, avg `0.001209`, median `0.003203`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.026156`, avg `0.008074`, median `0.007534`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.043948`, avg `0.015819`, median `0.016711`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.425`, primary_mae `0.056245`, avg `0.03864`, median `0.048873`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.021205`, avg `-0.002268`, median `-0.00786`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.024281`, avg `0.000535`, median `0.002202`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.031907`, avg `0.010001`, median `0.013105`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.049446`, avg `0.015729`, median `0.018476`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.2`, primary_mae `0.086111`, avg `0.047629`, median `0.046105`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.01876`, avg `0.002671`, median `0.002315`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.017064`, avg `-0.000818`, median `-0.003603`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.027046`, avg `0.003729`, median `0.004772`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.5`, primary_mae `0.040315`, avg `0.016034`, median `0.017488`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.425`, primary_mae `0.046888`, avg `0.037426`, median `0.05619`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.019402`, avg `0.001322`, median `-0.000648`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.017716`, avg `0.005938`, median `0.012556`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.018624`, avg `0.014838`, median `0.016753`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.045717`, avg `0.015479`, median `0.015638`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.65`, primary_mae `0.045091`, avg `0.03208`, median `0.02226`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.01876, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.017064, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.018624, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.040315, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.045091, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015774, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019843, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.01876, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017106, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018897, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.017064, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020889, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027415, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.018624, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025588, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04552, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.040315, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.425, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043025, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056893, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.045091, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.008626`, avg `0.006022`, median `0.006323`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.015505`, avg `0.002367`, median `0.003214`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.027167`, avg `0.007339`, median `0.00842`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.025904`, avg `0.027829`, median `0.023499`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.054033`, avg `0.004239`, median `-0.002378`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.011827`, avg `0.004624`, median `0.006323`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.014079`, avg `0.001952`, median `0.003214`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.027538`, avg `-0.000102`, median `-0.000714`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.039367`, avg `0.010246`, median `0.013566`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.057513`, avg `0.008595`, median `0.007715`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.019564`, avg `0.00131`, median `-0.005904`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.022547`, avg `0.003104`, median `0.004066`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.030907`, avg `0.01483`, median `0.013105`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.050939`, avg `0.01699`, median `0.020403`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.084331`, avg `0.047107`, median `0.046105`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.019532`, avg `0.001099`, median `-1.2e-05`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.019032`, avg `0.001209`, median `0.003203`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.026156`, avg `0.008074`, median `0.007534`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.043948`, avg `0.015819`, median `0.016711`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.425`, primary_mae `0.056245`, avg `0.03864`, median `0.048873`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.019532`, avg `0.001099`, median `-1.2e-05`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.019032`, avg `0.001209`, median `0.003203`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.026156`, avg `0.008074`, median `0.007534`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.043948`, avg `0.015819`, median `0.016711`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.425`, primary_mae `0.056245`, avg `0.03864`, median `0.048873`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.5`, primary_mae `0.018974`, avg `0.002221`, median `0.001546`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.4833`, primary_mae `0.017282`, avg `0.001434`, median `0.003214`
- 10d: sample `60`, primary_hit `0.4167`, primary_closer `0.5667`, primary_mae `0.024239`, avg `0.007432`, median `0.007314`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.4833`, primary_mae `0.042116`, avg `0.015849`, median `0.016711`
- 60d: sample `60`, primary_hit `0.3333`, primary_closer `0.5`, primary_mae `0.046289`, avg `0.035644`, median `0.050464`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.021205`, avg `-0.002268`, median `-0.00786`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.024281`, avg `0.000535`, median `0.002202`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.031907`, avg `0.010001`, median `0.013105`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.049446`, avg `0.015729`, median `0.018476`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.2`, primary_mae `0.086111`, avg `0.047629`, median `0.046105`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.019532`, avg `0.001099`, median `-1.2e-05`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.019032`, avg `0.001209`, median `0.003203`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.026156`, avg `0.008074`, median `0.007534`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.043948`, avg `0.015819`, median `0.016711`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.425`, primary_mae `0.056245`, avg `0.03864`, median `0.048873`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.019532`, avg `0.001099`, median `-1.2e-05`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.019032`, avg `0.001209`, median `0.003203`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.026156`, avg `0.008074`, median `0.007534`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.043948`, avg `0.015819`, median `0.016711`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.425`, primary_mae `0.056245`, avg `0.03864`, median `0.048873`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.015225`, avg `0.002023`, median `0.002303`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.016393`, avg `0.002546`, median `0.005191`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.023402`, avg `0.006865`, median `0.008249`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.042158`, avg `0.012834`, median `0.01321`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.575`, primary_mae `0.048106`, avg `0.022456`, median `0.017111`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.019532`, avg `0.001099`, median `-1.2e-05`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.019032`, avg `0.001209`, median `0.003203`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.026156`, avg `0.008074`, median `0.007534`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.043948`, avg `0.015819`, median `0.016711`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.425`, primary_mae `0.056245`, avg `0.03864`, median `0.048873`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
