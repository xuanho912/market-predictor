# Historical Replay Benchmark

Generated at: `2026-09-15T17:03:03.708180+00:00`
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
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.021507`
- secondary_mean_absolute_error: `0.014747`
- primary_error_advantage: `-0.00676`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.021927`
- secondary_mean_absolute_error: `0.01693`
- primary_error_advantage: `-0.004997`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.030058`
- secondary_mean_absolute_error: `0.024327`
- primary_error_advantage: `-0.005731`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.057726`
- secondary_mean_absolute_error: `0.03215`
- primary_error_advantage: `-0.025576`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.108055`
- secondary_mean_absolute_error: `0.067147`
- primary_error_advantage: `-0.040908`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.015208`, as_primary `0`, as_primary_hit `None`, avg `0.000536`, median `0.000878`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.016996`, as_primary `0`, as_primary_hit `None`, avg `-0.003565`, median `0.000448`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.025908`, as_primary `0`, as_primary_hit `None`, avg `-0.006742`, median `-0.011449`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.032734`, as_primary `0`, as_primary_hit `None`, avg `0.00757`, median `0.007561`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.071666`, as_primary `0`, as_primary_hit `None`, avg `0.03895`, median `0.059722`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.016393`, as_primary `0`, as_primary_hit `None`, avg `0.000536`, median `0.000878`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.020202`, as_primary `0`, as_primary_hit `None`, avg `-0.003565`, median `0.000448`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.037016`, as_primary `0`, as_primary_hit `None`, avg `-0.006742`, median `-0.011449`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.051157`, as_primary `0`, as_primary_hit `None`, avg `0.00757`, median `0.007561`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.074525`, as_primary `0`, as_primary_hit `None`, avg `0.03895`, median `0.059722`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.021507`, as_primary `80`, as_primary_hit `0.525`, avg `0.000536`, median `0.000878`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.021927`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.003565`, median `0.000448`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.030058`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.006742`, median `-0.011449`
- 20d: sample `80`, direction_hit `0.4375`, path_mae `0.057726`, as_primary `80`, as_primary_hit `0.5625`, avg `0.00757`, median `0.007561`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.108055`, as_primary `80`, as_primary_hit `0.725`, avg `0.03895`, median `0.059722`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014747`, as_primary `0`, as_primary_hit `None`, avg `0.000536`, median `0.000878`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.01693`, as_primary `0`, as_primary_hit `None`, avg `-0.003565`, median `0.000448`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.024327`, as_primary `0`, as_primary_hit `None`, avg `-0.006742`, median `-0.011449`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.03215`, as_primary `0`, as_primary_hit `None`, avg `0.00757`, median `0.007561`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.067147`, as_primary `0`, as_primary_hit `None`, avg `0.03895`, median `0.059722`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3125`, primary_mae `0.021507`, avg `0.000536`, median `0.000878`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.021927`, avg `-0.003565`, median `0.000448`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.375`, primary_mae `0.030058`, avg `-0.006742`, median `-0.011449`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.057726`, avg `0.00757`, median `0.007561`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.108055`, avg `0.03895`, median `0.059722`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.3167`, primary_mae `0.021195`, avg `-0.000702`, median `-0.000512`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.021681`, avg `-0.005512`, median `4.2e-05`
- 10d: sample `60`, primary_hit `0.6667`, primary_closer `0.3667`, primary_mae `0.025735`, avg `-0.009898`, median `-0.013782`
- 20d: sample `60`, primary_hit `0.4667`, primary_closer `0.2333`, primary_mae `0.061014`, avg `0.004227`, median `0.004327`
- 60d: sample `60`, primary_hit `0.3333`, primary_closer `0.3333`, primary_mae `0.116369`, avg `0.029144`, median `0.059251`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.022443`, avg `0.004249`, median `0.009116`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.022664`, avg `0.002275`, median `0.003973`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.043027`, avg `0.002728`, median `0.011331`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.047861`, avg `0.0176`, median `0.014651`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.35`, primary_mae `0.083114`, avg `0.068368`, median `0.064505`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.021195, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.021681, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6667, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.025735, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047861, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.083114, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014747, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021507, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.021195, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01693, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021927, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.021681, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024327, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037016, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6667, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.025735, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03215, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057726, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047861, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067147, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.108055, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.083114, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.030227`, avg `0.003659`, median `0.004814`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.030376`, avg `-4.4e-05`, median `0.003026`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.02236`, avg `-0.001978`, median `-0.00362`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.06499`, avg `0.040213`, median `0.047524`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.132139`, avg `0.080765`, median `0.103033`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.025734`, avg `-0.001967`, median `0.000341`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.024742`, avg `-0.007982`, median `-0.002115`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.021079`, avg `-0.003149`, median `-0.005954`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.049321`, avg `0.023485`, median `0.030181`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.098458`, avg `0.044907`, median `0.072376`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.1875`, primary_mae `0.027129`, avg `0.004207`, median `0.003143`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.031637`, avg `0.003088`, median `0.005514`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.036043`, avg `-0.016098`, median `-0.024778`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.1875`, primary_mae `0.067964`, avg `-0.009611`, median `-0.011353`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.189133`, avg `0.023945`, median `0.069017`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3125`, primary_mae `0.021507`, avg `0.000536`, median `0.000878`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.021927`, avg `-0.003565`, median `0.000448`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.375`, primary_mae `0.030058`, avg `-0.006742`, median `-0.011449`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.057726`, avg `0.00757`, median `0.007561`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.108055`, avg `0.03895`, median `0.059722`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3125`, primary_mae `0.021507`, avg `0.000536`, median `0.000878`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.021927`, avg `-0.003565`, median `0.000448`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.375`, primary_mae `0.030058`, avg `-0.006742`, median `-0.011449`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.057726`, avg `0.00757`, median `0.007561`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.108055`, avg `0.03895`, median `0.059722`

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
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3125`, primary_mae `0.021507`, avg `0.000536`, median `0.000878`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.3625`, primary_mae `0.021927`, avg `-0.003565`, median `0.000448`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.375`, primary_mae `0.030058`, avg `-0.006742`, median `-0.011449`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.057726`, avg `0.00757`, median `0.007561`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.108055`, avg `0.03895`, median `0.059722`

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
