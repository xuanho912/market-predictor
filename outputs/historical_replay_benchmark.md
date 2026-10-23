# Historical Replay Benchmark

Generated at: `2026-10-23T17:12:19.659418+00:00`
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
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.01976`
- secondary_mean_absolute_error: `0.017754`
- primary_error_advantage: `-0.002006`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.018198`
- secondary_mean_absolute_error: `0.0177`
- primary_error_advantage: `-0.000498`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.1375`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.026083`
- secondary_mean_absolute_error: `0.02694`
- primary_error_advantage: `0.000857`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.046589`
- secondary_mean_absolute_error: `0.037935`
- primary_error_advantage: `-0.008654`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.048123`
- secondary_mean_absolute_error: `0.040197`
- primary_error_advantage: `-0.007926`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.016484`, as_primary `0`, as_primary_hit `None`, avg `0.002737`, median `0.001927`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.01686`, as_primary `0`, as_primary_hit `None`, avg `0.002477`, median `0.003558`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.022689`, as_primary `0`, as_primary_hit `None`, avg `0.007053`, median `0.007019`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.02957`, as_primary `0`, as_primary_hit `None`, avg `0.016545`, median `0.018688`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.039732`, as_primary `0`, as_primary_hit `None`, avg `0.035706`, median `0.040496`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.016739`, as_primary `20`, as_primary_hit `0.65`, avg `0.002737`, median `0.001927`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.017605`, as_primary `20`, as_primary_hit `0.6`, avg `0.002477`, median `0.003558`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.028815`, as_primary `20`, as_primary_hit `0.55`, avg `0.007053`, median `0.007019`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.045932`, as_primary `20`, as_primary_hit `0.7`, avg `0.016545`, median `0.018688`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.044113`, as_primary `20`, as_primary_hit `0.7`, avg `0.035706`, median `0.040496`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.020635`, as_primary `60`, as_primary_hit `0.5`, avg `0.002737`, median `0.001927`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.017943`, as_primary `60`, as_primary_hit `0.5333`, avg `0.002477`, median `0.003558`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.027863`, as_primary `60`, as_primary_hit `0.6167`, avg `0.007053`, median `0.007019`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.048831`, as_primary `60`, as_primary_hit `0.7167`, avg `0.016545`, median `0.018688`
- 60d: sample `80`, direction_hit `0.2`, path_mae `0.048319`, as_primary `60`, as_primary_hit `0.8333`, avg `0.035706`, median `0.040496`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.016346`, as_primary `0`, as_primary_hit `None`, avg `0.002737`, median `0.001927`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.016696`, as_primary `0`, as_primary_hit `None`, avg `0.002477`, median `0.003558`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.021294`, as_primary `0`, as_primary_hit `None`, avg `0.007053`, median `0.007019`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.028297`, as_primary `0`, as_primary_hit `None`, avg `0.016545`, median `0.018688`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.038639`, as_primary `0`, as_primary_hit `None`, avg `0.035706`, median `0.040496`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.01976`, avg `0.002737`, median `0.001927`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.018198`, avg `0.002477`, median `0.003558`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.026083`, avg `0.007053`, median `0.007019`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.4125`, primary_mae `0.046589`, avg `0.016545`, median `0.018688`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4125`, primary_mae `0.048123`, avg `0.035706`, median `0.040496`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.011829`, avg `0.00436`, median `0.006323`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.015576`, avg `0.002843`, median `0.003558`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.030069`, avg `0.00012`, median `0.005184`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.65`, primary_mae `0.041515`, avg `0.014805`, median `0.02184`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.047439`, avg `0.017746`, median `0.029617`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.021174`, avg `1e-06`, median `-0.00786`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.021312`, avg `-0.001944`, median `-0.004807`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.028249`, avg `0.006293`, median `0.006365`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.053441`, avg `0.013585`, median `0.014604`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.069362`, avg `0.04604`, median `0.037911`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.02785`, avg `0.003995`, median `0.002901`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.019565`, avg `-0.000286`, median `-0.005132`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.023764`, avg `0.006417`, median `0.002415`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.041324`, avg `0.02117`, median `0.027803`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.35`, primary_mae `0.040755`, avg `0.060119`, median `0.073238`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.018185`, avg `0.002593`, median `0.003229`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.65`, primary_mae `0.016337`, avg `0.009295`, median `0.01723`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.02225`, avg `0.015382`, median `0.016753`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.050077`, avg `0.016622`, median `0.010237`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.034936`, avg `0.018919`, median `0.021062`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.011829, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.015576, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.02225, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.041324, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.034936, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016346, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020635, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.011829, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016696, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017943, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.015576, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.1375, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021294, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028815, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.02225, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028297, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048831, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.041324, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038639, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048319, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.034936, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.007833`, avg `0.008415`, median `0.006547`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.012982`, avg `0.006168`, median `0.007486`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.027512`, avg `0.007932`, median `0.010794`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.028131`, avg `0.030828`, median `0.0272`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.047246`, avg `0.023923`, median `0.016646`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.012527`, avg `0.003402`, median `0.006323`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.014817`, avg `0.002938`, median `0.003558`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.028788`, avg `0.001135`, median `0.005326`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.04453`, avg `0.011179`, median `0.016771`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.052671`, avg `0.012339`, median `0.023593`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.020882`, avg `0.001137`, median `-0.005904`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.019689`, avg `0.002119`, median `0.002887`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.029615`, avg `0.013525`, median `0.013105`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.057108`, avg `0.018968`, median `0.031443`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.077482`, avg `0.052049`, median `0.046105`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.01976`, avg `0.002737`, median `0.001927`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.018198`, avg `0.002477`, median `0.003558`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.026083`, avg `0.007053`, median `0.007019`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.4125`, primary_mae `0.046589`, avg `0.016545`, median `0.018688`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4125`, primary_mae `0.048123`, avg `0.035706`, median `0.040496`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.01976`, avg `0.002737`, median `0.001927`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.018198`, avg `0.002477`, median `0.003558`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.026083`, avg `0.007053`, median `0.007019`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.4125`, primary_mae `0.046589`, avg `0.016545`, median `0.018688`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4125`, primary_mae `0.048123`, avg `0.035706`, median `0.040496`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.5333`, primary_mae `0.019288`, avg `0.003649`, median `0.004985`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.5667`, primary_mae `0.017159`, avg `0.003951`, median `0.005191`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.5167`, primary_mae `0.025361`, avg `0.007306`, median `0.007019`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.45`, primary_mae `0.044305`, avg `0.017532`, median `0.021475`
- 60d: sample `60`, primary_hit `0.35`, primary_closer `0.4667`, primary_mae `0.041043`, avg `0.032261`, median `0.040496`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.021174`, avg `1e-06`, median `-0.00786`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.021312`, avg `-0.001944`, median `-0.004807`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.028249`, avg `0.006293`, median `0.006365`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.053441`, avg `0.013585`, median `0.014604`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.069362`, avg `0.04604`, median `0.037911`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.01976`, avg `0.002737`, median `0.001927`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.018198`, avg `0.002477`, median `0.003558`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.026083`, avg `0.007053`, median `0.007019`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.4125`, primary_mae `0.046589`, avg `0.016545`, median `0.018688`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4125`, primary_mae `0.048123`, avg `0.035706`, median `0.040496`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.01976`, avg `0.002737`, median `0.001927`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.018198`, avg `0.002477`, median `0.003558`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.026083`, avg `0.007053`, median `0.007019`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.4125`, primary_mae `0.046589`, avg `0.016545`, median `0.018688`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4125`, primary_mae `0.048123`, avg `0.035706`, median `0.040496`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
