# Historical Replay Benchmark

Generated at: `2026-08-08T04:41:44.243763+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.01454`
- secondary_mean_absolute_error: `0.012175`
- primary_error_advantage: `-0.002365`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.018275`
- secondary_mean_absolute_error: `0.01702`
- primary_error_advantage: `-0.001255`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.030164`
- secondary_mean_absolute_error: `0.027754`
- primary_error_advantage: `-0.00241`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.062486`
- secondary_mean_absolute_error: `0.054584`
- primary_error_advantage: `-0.007902`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.077358`
- secondary_mean_absolute_error: `0.081513`
- primary_error_advantage: `0.004155`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.012388`, as_primary `0`, as_primary_hit `None`, avg `0.003576`, median `0.005105`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.016917`, as_primary `0`, as_primary_hit `None`, avg `0.005924`, median `0.00573`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.025064`, as_primary `0`, as_primary_hit `None`, avg `0.005937`, median `0.008249`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.039213`, as_primary `0`, as_primary_hit `None`, avg `0.010016`, median `0.013593`
- 60d: sample `80`, direction_hit `0.575`, path_mae `0.067646`, as_primary `0`, as_primary_hit `None`, avg `0.022271`, median `0.031767`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.015072`, as_primary `60`, as_primary_hit `0.5833`, avg `0.003576`, median `0.005105`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.021564`, as_primary `60`, as_primary_hit `0.7167`, avg `0.005924`, median `0.00573`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.034291`, as_primary `60`, as_primary_hit `0.5833`, avg `0.005937`, median `0.008249`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.063262`, as_primary `60`, as_primary_hit `0.6833`, avg `0.010016`, median `0.013593`
- 60d: sample `80`, direction_hit `0.575`, path_mae `0.085868`, as_primary `60`, as_primary_hit `0.55`, avg `0.022271`, median `0.031767`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.013475`, as_primary `20`, as_primary_hit `0.75`, avg `0.003576`, median `0.005105`
- 5d: sample `80`, direction_hit `0.3125`, path_mae `0.017368`, as_primary `20`, as_primary_hit `0.6`, avg `0.005924`, median `0.00573`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.031031`, as_primary `20`, as_primary_hit `0.6`, avg `0.005937`, median `0.008249`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.075079`, as_primary `20`, as_primary_hit `0.65`, avg `0.010016`, median `0.013593`
- 60d: sample `80`, direction_hit `0.425`, path_mae `0.085886`, as_primary `20`, as_primary_hit `0.65`, avg `0.022271`, median `0.031767`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.012118`, as_primary `0`, as_primary_hit `None`, avg `0.003576`, median `0.005105`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.014935`, as_primary `0`, as_primary_hit `None`, avg `0.005924`, median `0.00573`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.022698`, as_primary `0`, as_primary_hit `None`, avg `0.005937`, median `0.008249`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.037187`, as_primary `0`, as_primary_hit `None`, avg `0.010016`, median `0.013593`
- 60d: sample `80`, direction_hit `0.575`, path_mae `0.062615`, as_primary `0`, as_primary_hit `None`, avg `0.022271`, median `0.031767`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.01454`, avg `0.003576`, median `0.005105`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.018275`, avg `0.005924`, median `0.00573`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.030164`, avg `0.005937`, median `0.008249`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.062486`, avg `0.010016`, median `0.013593`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.077358`, avg `0.022271`, median `0.031767`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4`, primary_mae `0.015347`, avg `0.002009`, median `0.003213`
- 5d: sample `60`, primary_hit `0.7167`, primary_closer `0.5`, primary_mae `0.016965`, avg `0.006203`, median `0.00573`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.026701`, avg `0.004556`, median `0.006542`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.5167`, primary_mae `0.049754`, avg `0.007404`, median `0.013593`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.074811`, avg `0.015378`, median `0.031767`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.012117`, avg `0.008277`, median `0.010408`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.022208`, avg `0.005087`, median `0.005967`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.040552`, avg `0.010077`, median `0.011814`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.2`, primary_mae `0.100682`, avg `0.017854`, median `0.013042`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.084998`, avg `0.042947`, median `0.042337`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.012117, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7167, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.016965, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.026701, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.049754, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.074811, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012118, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015072, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.012117, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014935, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021564, 'direction_hit_rate': 0.6875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7167, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.016965, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022698, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034291, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.026701, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037187, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075079, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.049754, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062615, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.085886, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.074811, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.026891`, avg `-0.003813`, median `-0.002198`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.0`, primary_mae `0.028429`, avg `0.000899`, median `0.003509`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.032668`, avg `0.002265`, median `0.002208`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.061971`, avg `0.009259`, median `0.014663`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.109217`, avg `-0.012738`, median `-0.032183`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.024264`, avg `-0.001186`, median `0.004081`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.023803`, avg `0.006313`, median `0.004667`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.029011`, avg `0.007732`, median `0.011059`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.054911`, avg `0.017703`, median `0.023697`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.08098`, avg `0.016706`, median `0.003555`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.013498`, avg `0.008873`, median `0.010545`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.024336`, avg `0.005709`, median `0.005967`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.039363`, avg `0.014268`, median `0.006552`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.105379`, avg `0.027474`, median `0.013042`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.094484`, avg `0.044825`, median `0.066875`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.01454`, avg `0.003576`, median `0.005105`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.018275`, avg `0.005924`, median `0.00573`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.030164`, avg `0.005937`, median `0.008249`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.062486`, avg `0.010016`, median `0.013593`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.077358`, avg `0.022271`, median `0.031767`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.01454`, avg `0.003576`, median `0.005105`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.018275`, avg `0.005924`, median `0.00573`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.030164`, avg `0.005937`, median `0.008249`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.062486`, avg `0.010016`, median `0.013593`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.077358`, avg `0.022271`, median `0.031767`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4`, primary_mae `0.015347`, avg `0.002009`, median `0.003213`
- 5d: sample `60`, primary_hit `0.7167`, primary_closer `0.5`, primary_mae `0.016965`, avg `0.006203`, median `0.00573`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.026701`, avg `0.004556`, median `0.006542`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.5167`, primary_mae `0.049754`, avg `0.007404`, median `0.013593`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.074811`, avg `0.015378`, median `0.031767`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.012117`, avg `0.008277`, median `0.010408`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.022208`, avg `0.005087`, median `0.005967`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.040552`, avg `0.010077`, median `0.011814`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.2`, primary_mae `0.100682`, avg `0.017854`, median `0.013042`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.084998`, avg `0.042947`, median `0.042337`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.01454`, avg `0.003576`, median `0.005105`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.018275`, avg `0.005924`, median `0.00573`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.030164`, avg `0.005937`, median `0.008249`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.062486`, avg `0.010016`, median `0.013593`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.077358`, avg `0.022271`, median `0.031767`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.01454`, avg `0.003576`, median `0.005105`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.018275`, avg `0.005924`, median `0.00573`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.030164`, avg `0.005937`, median `0.008249`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.062486`, avg `0.010016`, median `0.013593`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.077358`, avg `0.022271`, median `0.031767`

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
