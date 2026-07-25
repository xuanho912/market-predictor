# Historical Replay Benchmark

Generated at: `2026-07-25T04:32:41.179442+00:00`
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
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.01584`
- secondary_mean_absolute_error: `0.015932`
- primary_error_advantage: `9.2e-05`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5125`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.019921`
- secondary_mean_absolute_error: `0.019645`
- primary_error_advantage: `-0.000276`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.022812`
- secondary_mean_absolute_error: `0.018903`
- primary_error_advantage: `-0.003909`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.041707`
- secondary_mean_absolute_error: `0.038472`
- primary_error_advantage: `-0.003235`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.3375`
- primary_vs_secondary_accuracy_spread: `0.325`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.070415`
- secondary_mean_absolute_error: `0.068202`
- primary_error_advantage: `-0.002213`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.575`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.015812`, as_primary `0`, as_primary_hit `None`, avg `0.004561`, median `0.005108`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.019007`, as_primary `0`, as_primary_hit `None`, avg `0.008785`, median `0.00893`
- 10d: sample `80`, direction_hit `0.775`, path_mae `0.019104`, as_primary `0`, as_primary_hit `None`, avg `0.016591`, median `0.020959`
- 20d: sample `80`, direction_hit `0.8375`, path_mae `0.026161`, as_primary `0`, as_primary_hit `None`, avg `0.030276`, median `0.033589`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.061908`, as_primary `0`, as_primary_hit `None`, avg `0.04647`, median `0.07415`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.016011`, as_primary `40`, as_primary_hit `0.675`, avg `0.004561`, median `0.005108`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.019232`, as_primary `40`, as_primary_hit `0.7`, avg `0.008785`, median `0.00893`
- 10d: sample `80`, direction_hit `0.775`, path_mae `0.020219`, as_primary `40`, as_primary_hit `0.775`, avg `0.016591`, median `0.020959`
- 20d: sample `80`, direction_hit `0.8375`, path_mae `0.038329`, as_primary `40`, as_primary_hit `0.825`, avg `0.030276`, median `0.033589`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.0681`, as_primary `40`, as_primary_hit `0.95`, avg `0.04647`, median `0.07415`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.015761`, as_primary `40`, as_primary_hit `0.55`, avg `0.004561`, median `0.005108`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.020211`, as_primary `40`, as_primary_hit `0.575`, avg `0.008785`, median `0.00893`
- 10d: sample `80`, direction_hit `0.225`, path_mae `0.022845`, as_primary `40`, as_primary_hit `0.775`, avg `0.016591`, median `0.020959`
- 20d: sample `80`, direction_hit `0.1625`, path_mae `0.044897`, as_primary `40`, as_primary_hit `0.85`, avg `0.030276`, median `0.033589`
- 60d: sample `80`, direction_hit `0.2125`, path_mae `0.073744`, as_primary `40`, as_primary_hit `0.625`, avg `0.04647`, median `0.07415`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.015654`, as_primary `0`, as_primary_hit `None`, avg `0.004561`, median `0.005108`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.019073`, as_primary `0`, as_primary_hit `None`, avg `0.008785`, median `0.00893`
- 10d: sample `80`, direction_hit `0.775`, path_mae `0.018944`, as_primary `0`, as_primary_hit `None`, avg `0.016591`, median `0.020959`
- 20d: sample `80`, direction_hit `0.8375`, path_mae `0.02536`, as_primary `0`, as_primary_hit `None`, avg `0.030276`, median `0.033589`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.063942`, as_primary `0`, as_primary_hit `None`, avg `0.04647`, median `0.07415`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5125`, primary_mae `0.01584`, avg `0.004561`, median `0.005108`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4875`, primary_mae `0.019921`, avg `0.008785`, median `0.00893`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.022812`, avg `0.016591`, median `0.020959`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.041707`, avg `0.030276`, median `0.033589`
- 60d: sample `80`, primary_hit `0.6625`, primary_closer `0.575`, primary_mae `0.070415`, avg `0.04647`, median `0.07415`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5125`, primary_mae `0.01584`, avg `0.004561`, median `0.005108`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4875`, primary_mae `0.019921`, avg `0.008785`, median `0.00893`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.022812`, avg `0.016591`, median `0.020959`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.041707`, avg `0.030276`, median `0.033589`
- 60d: sample `80`, primary_hit `0.6625`, primary_closer `0.575`, primary_mae `0.070415`, avg `0.04647`, median `0.07415`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5625, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.01584, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5625, 'primary_closer_than_secondary_rate': 0.4875, 'primary_mean_absolute_error': 0.019921, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4875, 'primary_mean_absolute_error': 0.022812, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4875, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.041707, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6625, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.070415, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015654, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016011, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5625, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.01584, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019007, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020211, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5625, 'primary_closer_than_secondary_rate': 0.4875, 'primary_mean_absolute_error': 0.019921, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018944, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022845, 'direction_hit_rate': 0.225}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4875, 'primary_mean_absolute_error': 0.022812, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02536, 'direction_hit_rate': 0.8375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044897, 'direction_hit_rate': 0.1625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4875, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.041707, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.3375, 'primary_vs_secondary_accuracy_spread': 0.325, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061908, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073744, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6625, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.070415, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

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
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.02104`, avg `0.008403`, median `0.005731`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.023443`, avg `0.014116`, median `0.008083`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.6875`, primary_mae `0.015464`, avg `0.024595`, median `0.031223`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.3125`, primary_mae `0.036796`, avg `0.035637`, median `0.03528`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.086943`, avg `0.011901`, median `0.060674`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5125`, primary_mae `0.01584`, avg `0.004561`, median `0.005108`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4875`, primary_mae `0.019921`, avg `0.008785`, median `0.00893`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.022812`, avg `0.016591`, median `0.020959`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.041707`, avg `0.030276`, median `0.033589`
- 60d: sample `80`, primary_hit `0.6625`, primary_closer `0.575`, primary_mae `0.070415`, avg `0.04647`, median `0.07415`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5125`, primary_mae `0.01584`, avg `0.004561`, median `0.005108`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4875`, primary_mae `0.019921`, avg `0.008785`, median `0.00893`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.022812`, avg `0.016591`, median `0.020959`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.041707`, avg `0.030276`, median `0.033589`
- 60d: sample `80`, primary_hit `0.6625`, primary_closer `0.575`, primary_mae `0.070415`, avg `0.04647`, median `0.07415`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.475`, primary_mae `0.012862`, avg `0.004881`, median `0.005602`
- 5d: sample `40`, primary_hit `0.7`, primary_closer `0.525`, primary_mae `0.015853`, avg `0.010233`, median `0.014405`
- 10d: sample `40`, primary_hit `0.775`, primary_closer `0.525`, primary_mae `0.017222`, avg `0.013995`, median `0.015658`
- 20d: sample `40`, primary_hit `0.825`, primary_closer `0.6`, primary_mae `0.032371`, avg `0.031002`, median `0.033589`
- 60d: sample `40`, primary_hit `0.95`, primary_closer `0.65`, primary_mae `0.035357`, avg `0.081442`, median `0.084258`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.018818`, avg `0.004241`, median `0.001442`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.023989`, avg `0.007336`, median `0.006091`
- 10d: sample `40`, primary_hit `0.225`, primary_closer `0.45`, primary_mae `0.028402`, avg `0.019187`, median `0.026765`
- 20d: sample `40`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.051043`, avg `0.029551`, median `0.031544`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.105473`, avg `0.011499`, median `0.059517`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5125`, primary_mae `0.01584`, avg `0.004561`, median `0.005108`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4875`, primary_mae `0.019921`, avg `0.008785`, median `0.00893`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.022812`, avg `0.016591`, median `0.020959`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.041707`, avg `0.030276`, median `0.033589`
- 60d: sample `80`, primary_hit `0.6625`, primary_closer `0.575`, primary_mae `0.070415`, avg `0.04647`, median `0.07415`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5125`, primary_mae `0.01584`, avg `0.004561`, median `0.005108`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4875`, primary_mae `0.019921`, avg `0.008785`, median `0.00893`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.022812`, avg `0.016591`, median `0.020959`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.041707`, avg `0.030276`, median `0.033589`
- 60d: sample `80`, primary_hit `0.6625`, primary_closer `0.575`, primary_mae `0.070415`, avg `0.04647`, median `0.07415`

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
