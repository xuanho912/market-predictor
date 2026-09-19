# Historical Replay Benchmark

Generated at: `2026-09-19T00:45:46.031567+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `PROMISING`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_supportive_but_not_forward_validated`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.017647`
- secondary_mean_absolute_error: `0.018126`
- primary_error_advantage: `0.000479`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5125`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.022508`
- secondary_mean_absolute_error: `0.023604`
- primary_error_advantage: `0.001096`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.029992`
- secondary_mean_absolute_error: `0.03016`
- primary_error_advantage: `0.000168`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.046952`
- secondary_mean_absolute_error: `0.057949`
- primary_error_advantage: `0.010997`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.575`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.066599`
- secondary_mean_absolute_error: `0.061915`
- primary_error_advantage: `-0.004684`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.016115`, as_primary `0`, as_primary_hit `None`, avg `0.002804`, median `0.005428`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.019909`, as_primary `0`, as_primary_hit `None`, avg `0.004408`, median `0.00805`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.025575`, as_primary `0`, as_primary_hit `None`, avg `0.011601`, median `0.011325`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.038376`, as_primary `0`, as_primary_hit `None`, avg `0.033731`, median `0.034279`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.055749`, as_primary `0`, as_primary_hit `None`, avg `0.070213`, median `0.092349`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.017895`, as_primary `40`, as_primary_hit `0.65`, avg `0.002804`, median `0.005428`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.023551`, as_primary `40`, as_primary_hit `0.625`, avg `0.004408`, median `0.00805`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.03082`, as_primary `40`, as_primary_hit `0.75`, avg `0.011601`, median `0.011325`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.053694`, as_primary `40`, as_primary_hit `0.8`, avg `0.033731`, median `0.034279`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.062017`, as_primary `40`, as_primary_hit `0.875`, avg `0.070213`, median `0.092349`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.017878`, as_primary `40`, as_primary_hit `0.525`, avg `0.002804`, median `0.005428`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.022561`, as_primary `40`, as_primary_hit `0.525`, avg `0.004408`, median `0.00805`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.029331`, as_primary `40`, as_primary_hit `0.575`, avg `0.011601`, median `0.011325`
- 20d: sample `80`, direction_hit `0.2`, path_mae `0.051207`, as_primary `40`, as_primary_hit `0.8`, avg `0.033731`, median `0.034279`
- 60d: sample `80`, direction_hit `0.2`, path_mae `0.066497`, as_primary `40`, as_primary_hit `0.725`, avg `0.070213`, median `0.092349`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.015987`, as_primary `0`, as_primary_hit `None`, avg `0.002804`, median `0.005428`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.019222`, as_primary `0`, as_primary_hit `None`, avg `0.004408`, median `0.00805`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.024746`, as_primary `0`, as_primary_hit `None`, avg `0.011601`, median `0.011325`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.034275`, as_primary `0`, as_primary_hit `None`, avg `0.033731`, median `0.034279`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.056081`, as_primary `0`, as_primary_hit `None`, avg `0.070213`, median `0.092349`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5125`, primary_mae `0.017647`, avg `0.002804`, median `0.005428`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.022508`, avg `0.004408`, median `0.00805`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.029992`, avg `0.011601`, median `0.011325`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.046952`, avg `0.033731`, median `0.034279`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.066599`, avg `0.070213`, median `0.092349`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.011966`, avg `0.001803`, median `0.002973`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.012664`, avg `0.002833`, median `0.004536`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.6`, primary_mae `0.01234`, avg `0.003099`, median `0.006274`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.65`, primary_mae `0.030721`, avg `0.028375`, median `0.036446`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.4`, primary_mae `0.041752`, avg `0.073829`, median `0.082944`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.5167`, primary_mae `0.019541`, avg `0.003137`, median `0.008122`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.4833`, primary_mae `0.02579`, avg `0.004934`, median `0.009885`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.035876`, avg `0.014435`, median `0.017781`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.052362`, avg `0.035517`, median `0.034279`
- 60d: sample `60`, primary_hit `0.4833`, primary_closer `0.5`, primary_mae `0.074882`, avg `0.069008`, median `0.09426`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.011966, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.012664, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.01234, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.030721, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.041752, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015987, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017895, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.011966, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019222, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023551, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.012664, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024746, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03082, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.01234, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034275, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053694, 'direction_hit_rate': 0.8}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.030721, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055749, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066497, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.041752, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.018056`, avg `0.001029`, median `0.005307`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.023964`, avg `0.001132`, median `0.006272`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.029845`, avg `0.006385`, median `0.005316`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.75`, primary_mae `0.027687`, avg `0.052505`, median `0.058396`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.044536`, avg `0.08582`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.014733`, avg `0.007312`, median `0.014755`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.02134`, avg `0.008404`, median `0.008828`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.027478`, avg `0.012052`, median `0.016702`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.625`, primary_mae `0.038243`, avg `0.042624`, median `0.050926`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.625`, primary_mae `0.027594`, avg `0.09406`, median `0.099778`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.021875`, avg `-0.012679`, median `-0.011593`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.022872`, avg `-0.015624`, median `-0.012861`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.042278`, avg `-0.00477`, median `-0.00147`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.063059`, avg `0.01043`, median `0.021827`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.114227`, avg `0.035962`, median `0.078066`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5125`, primary_mae `0.017647`, avg `0.002804`, median `0.005428`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.022508`, avg `0.004408`, median `0.00805`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.029992`, avg `0.011601`, median `0.011325`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.046952`, avg `0.033731`, median `0.034279`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.066599`, avg `0.070213`, median `0.092349`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5125`, primary_mae `0.017647`, avg `0.002804`, median `0.005428`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.022508`, avg `0.004408`, median `0.00805`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.029992`, avg `0.011601`, median `0.011325`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.046952`, avg `0.033731`, median `0.034279`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.066599`, avg `0.070213`, median `0.092349`

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
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5125`, primary_mae `0.017647`, avg `0.002804`, median `0.005428`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.022508`, avg `0.004408`, median `0.00805`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.029992`, avg `0.011601`, median `0.011325`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.046952`, avg `0.033731`, median `0.034279`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.066599`, avg `0.070213`, median `0.092349`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5125`, primary_mae `0.017647`, avg `0.002804`, median `0.005428`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.022508`, avg `0.004408`, median `0.00805`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.029992`, avg `0.011601`, median `0.011325`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.046952`, avg `0.033731`, median `0.034279`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.066599`, avg `0.070213`, median `0.092349`

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
