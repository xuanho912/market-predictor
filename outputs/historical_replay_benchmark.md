# Historical Replay Benchmark

Generated at: `2026-10-06T18:25:57.414726+00:00`
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
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.325`
- primary_vs_secondary_accuracy_spread: `0.35`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.015699`
- secondary_mean_absolute_error: `0.015221`
- primary_error_advantage: `-0.000478`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.024165`
- secondary_mean_absolute_error: `0.021924`
- primary_error_advantage: `-0.002241`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.040377`
- secondary_mean_absolute_error: `0.035647`
- primary_error_advantage: `-0.00473`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.069827`
- secondary_mean_absolute_error: `0.06078`
- primary_error_advantage: `-0.009047`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.076961`
- secondary_mean_absolute_error: `0.06812`
- primary_error_advantage: `-0.008841`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.325`, path_mae `0.015101`, as_primary `0`, as_primary_hit `None`, avg `-0.009204`, median `-0.008645`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.020746`, as_primary `0`, as_primary_hit `None`, avg `-0.013363`, median `-0.01246`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.029654`, as_primary `0`, as_primary_hit `None`, avg `-0.012125`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.5375`, path_mae `0.042096`, as_primary `0`, as_primary_hit `None`, avg `-0.004353`, median `0.00206`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.064712`, as_primary `0`, as_primary_hit `None`, avg `0.017659`, median `0.039666`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.325`, path_mae `0.015221`, as_primary `0`, as_primary_hit `None`, avg `-0.009204`, median `-0.008645`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.021924`, as_primary `0`, as_primary_hit `None`, avg `-0.013363`, median `-0.01246`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.035647`, as_primary `0`, as_primary_hit `None`, avg `-0.012125`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.5375`, path_mae `0.06078`, as_primary `0`, as_primary_hit `None`, avg `-0.004353`, median `0.00206`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.06812`, as_primary `0`, as_primary_hit `None`, avg `0.017659`, median `0.039666`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.015699`, as_primary `80`, as_primary_hit `0.325`, avg `-0.009204`, median `-0.008645`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.024165`, as_primary `80`, as_primary_hit `0.375`, avg `-0.013363`, median `-0.01246`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.040377`, as_primary `80`, as_primary_hit `0.425`, avg `-0.012125`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.4625`, path_mae `0.069827`, as_primary `80`, as_primary_hit `0.5375`, avg `-0.004353`, median `0.00206`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.076961`, as_primary `80`, as_primary_hit `0.675`, avg `0.017659`, median `0.039666`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.325`, path_mae `0.015093`, as_primary `0`, as_primary_hit `None`, avg `-0.009204`, median `-0.008645`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.020751`, as_primary `0`, as_primary_hit `None`, avg `-0.013363`, median `-0.01246`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.028609`, as_primary `0`, as_primary_hit `None`, avg `-0.012125`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.5375`, path_mae `0.041486`, as_primary `0`, as_primary_hit `None`, avg `-0.004353`, median `0.00206`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.067546`, as_primary `0`, as_primary_hit `None`, avg `0.017659`, median `0.039666`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.7`, primary_closer `0.4833`, primary_mae `0.015285`, avg `-0.010518`, median `-0.009933`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.023724`, avg `-0.014409`, median `-0.009552`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.5167`, primary_mae `0.037555`, avg `-0.010682`, median `-0.012632`
- 20d: sample `60`, primary_hit `0.4333`, primary_closer `0.4`, primary_mae `0.074964`, avg `-0.003345`, median `0.011992`
- 60d: sample `60`, primary_hit `0.35`, primary_closer `0.3667`, primary_mae `0.085642`, avg `0.012429`, median `0.039666`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.016939`, avg `-0.005261`, median `-0.003704`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.025489`, avg `-0.010225`, median `-0.014456`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.048843`, avg `-0.016454`, median `-0.011647`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.054414`, avg `-0.007376`, median `-0.005132`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.050916`, avg `0.033348`, median `0.037786`

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
- 3d: sample `60`, primary_hit `0.7333`, primary_closer `0.4667`, primary_mae `0.017629`, avg `-0.012316`, median `-0.011995`
- 5d: sample `60`, primary_hit `0.6833`, primary_closer `0.5`, primary_mae `0.028212`, avg `-0.016844`, median `-0.017227`
- 10d: sample `60`, primary_hit `0.6167`, primary_closer `0.4167`, primary_mae `0.04632`, avg `-0.018489`, median `-0.020336`
- 20d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.074803`, avg `-0.010048`, median `-0.005132`
- 60d: sample `60`, primary_hit `0.3667`, primary_closer `0.4333`, primary_mae `0.088237`, avg `0.015797`, median `0.041125`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.009908`, avg `0.000133`, median `0.001336`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.012025`, avg `-0.00292`, median `0.001171`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.6`, primary_mae `0.022546`, avg `0.006968`, median `0.009716`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.054898`, avg `0.012731`, median `0.020612`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.043133`, avg `0.023246`, median `0.039666`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.009908, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.012025, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.022546, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.054898, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.043133, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.325, 'primary_vs_secondary_accuracy_spread': 0.35, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015093, 'direction_hit_rate': 0.325}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015699, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.009908, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020746, 'direction_hit_rate': 0.375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024165, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.012025, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028609, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040377, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.022546, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041486, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069827, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.054898, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064712, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076961, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.043133, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.011468`, avg `-0.000663`, median `0.005794`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.009956`, avg `0.000394`, median `0.002359`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.029311`, avg `0.010591`, median `0.016769`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.068387`, avg `0.019356`, median `0.033594`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.047449`, avg `0.03672`, median `0.043377`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.010033`, avg `8.4e-05`, median `0.001336`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.011565`, avg `-0.002329`, median `0.001171`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.024085`, avg `0.007733`, median `0.010165`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.063011`, avg `0.0197`, median `0.029416`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.040011`, avg `0.030562`, median `0.041986`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.017589`, avg `-0.006457`, median `-0.003619`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.026168`, avg `-0.010877`, median `-0.015635`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.0534`, avg `-0.011864`, median `-0.004743`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.060526`, avg `-0.002111`, median `0.00088`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.4375`, primary_mae `0.050935`, avg `0.041016`, median `0.050131`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.675`, primary_closer `0.475`, primary_mae `0.015699`, avg `-0.009204`, median `-0.008645`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.024165`, avg `-0.013363`, median `-0.01246`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.040377`, avg `-0.012125`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.069827`, avg `-0.004353`, median `0.00206`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.076961`, avg `0.017659`, median `0.039666`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.675`, primary_closer `0.475`, primary_mae `0.015699`, avg `-0.009204`, median `-0.008645`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.024165`, avg `-0.013363`, median `-0.01246`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.040377`, avg `-0.012125`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.069827`, avg `-0.004353`, median `0.00206`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.076961`, avg `0.017659`, median `0.039666`

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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.65`, primary_closer `0.4833`, primary_mae `0.014976`, avg `-0.00774`, median `-0.004602`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.5167`, primary_mae `0.023288`, avg `-0.012254`, median `-0.010672`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4833`, primary_mae `0.041172`, avg `-0.008521`, median `-0.006704`
- 20d: sample `60`, primary_hit `0.4333`, primary_closer `0.4333`, primary_mae `0.066495`, avg `0.002089`, median `0.003271`
- 60d: sample `60`, primary_hit `0.2667`, primary_closer `0.3833`, primary_mae `0.06724`, avg `0.036177`, median `0.044525`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.675`, primary_closer `0.475`, primary_mae `0.015699`, avg `-0.009204`, median `-0.008645`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.024165`, avg `-0.013363`, median `-0.01246`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.040377`, avg `-0.012125`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.069827`, avg `-0.004353`, median `0.00206`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.076961`, avg `0.017659`, median `0.039666`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.675`, primary_closer `0.475`, primary_mae `0.015699`, avg `-0.009204`, median `-0.008645`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.024165`, avg `-0.013363`, median `-0.01246`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.040377`, avg `-0.012125`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.069827`, avg `-0.004353`, median `0.00206`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.076961`, avg `0.017659`, median `0.039666`

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
