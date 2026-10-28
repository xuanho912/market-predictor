# Historical Replay Benchmark

Generated at: `2026-10-28T01:51:42.682044+00:00`
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
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.01599`
- secondary_mean_absolute_error: `0.014132`
- primary_error_advantage: `-0.001858`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.020051`
- secondary_mean_absolute_error: `0.018757`
- primary_error_advantage: `-0.001294`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.028899`
- secondary_mean_absolute_error: `0.027343`
- primary_error_advantage: `-0.001556`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.040579`
- secondary_mean_absolute_error: `0.041573`
- primary_error_advantage: `0.000994`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.065283`
- secondary_mean_absolute_error: `0.062737`
- primary_error_advantage: `-0.002546`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.014413`, as_primary `0`, as_primary_hit `None`, avg `0.005696`, median `0.006029`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.018805`, as_primary `0`, as_primary_hit `None`, avg `0.008783`, median `0.009948`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.026255`, as_primary `0`, as_primary_hit `None`, avg `0.012161`, median `0.010117`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.032561`, as_primary `0`, as_primary_hit `None`, avg `0.019025`, median `0.026036`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.048889`, as_primary `0`, as_primary_hit `None`, avg `0.033859`, median `0.047453`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.015173`, as_primary `60`, as_primary_hit `0.65`, avg `0.005696`, median `0.006029`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.020017`, as_primary `60`, as_primary_hit `0.6667`, avg `0.008783`, median `0.009948`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.032318`, as_primary `60`, as_primary_hit `0.7333`, avg `0.012161`, median `0.010117`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.043861`, as_primary `60`, as_primary_hit `0.7667`, avg `0.019025`, median `0.026036`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.054282`, as_primary `60`, as_primary_hit `0.75`, avg `0.033859`, median `0.047453`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.015738`, as_primary `20`, as_primary_hit `0.55`, avg `0.005696`, median `0.006029`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.019341`, as_primary `20`, as_primary_hit `0.6`, avg `0.008783`, median `0.009948`
- 10d: sample `80`, direction_hit `0.3125`, path_mae `0.032416`, as_primary `20`, as_primary_hit `0.55`, avg `0.012161`, median `0.010117`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.051522`, as_primary `20`, as_primary_hit `0.55`, avg `0.019025`, median `0.026036`
- 60d: sample `80`, direction_hit `0.25`, path_mae `0.079425`, as_primary `20`, as_primary_hit `0.75`, avg `0.033859`, median `0.047453`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.013956`, as_primary `0`, as_primary_hit `None`, avg `0.005696`, median `0.006029`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.017786`, as_primary `0`, as_primary_hit `None`, avg `0.008783`, median `0.009948`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.023882`, as_primary `0`, as_primary_hit `None`, avg `0.012161`, median `0.010117`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.030176`, as_primary `0`, as_primary_hit `None`, avg `0.019025`, median `0.026036`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.049294`, as_primary `0`, as_primary_hit `None`, avg `0.033859`, median `0.047453`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.65`, primary_closer `0.4667`, primary_mae `0.013978`, avg `0.006058`, median `0.006029`
- 5d: sample `60`, primary_hit `0.6667`, primary_closer `0.5167`, primary_mae `0.019098`, avg `0.009745`, median `0.010594`
- 10d: sample `60`, primary_hit `0.7333`, primary_closer `0.45`, primary_mae `0.028446`, avg `0.014975`, median `0.014115`
- 20d: sample `60`, primary_hit `0.7667`, primary_closer `0.4167`, primary_mae `0.039094`, avg `0.022037`, median `0.028445`
- 60d: sample `60`, primary_hit `0.75`, primary_closer `0.6`, primary_mae `0.052316`, avg `0.032402`, median `0.050858`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022029`, avg `0.004608`, median `0.005578`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.02291`, avg `0.005896`, median `0.009377`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.030258`, avg `0.003721`, median `0.005647`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.045034`, avg `0.00999`, median `0.001221`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.2`, primary_mae `0.104185`, avg `0.03823`, median `0.031522`

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
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022029`, avg `0.004608`, median `0.005578`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.02291`, avg `0.005896`, median `0.009377`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.030258`, avg `0.003721`, median `0.005647`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.045034`, avg `0.00999`, median `0.001221`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.2`, primary_mae `0.104185`, avg `0.03823`, median `0.031522`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.65`, primary_closer `0.4667`, primary_mae `0.013978`, avg `0.006058`, median `0.006029`
- 5d: sample `60`, primary_hit `0.6667`, primary_closer `0.5167`, primary_mae `0.019098`, avg `0.009745`, median `0.010594`
- 10d: sample `60`, primary_hit `0.7333`, primary_closer `0.45`, primary_mae `0.028446`, avg `0.014975`, median `0.014115`
- 20d: sample `60`, primary_hit `0.7667`, primary_closer `0.4167`, primary_mae `0.039094`, avg `0.022037`, median `0.028445`
- 60d: sample `60`, primary_hit `0.75`, primary_closer `0.6`, primary_mae `0.052316`, avg `0.032402`, median `0.050858`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.013978, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6667, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.019098, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7333, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.028446, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7667, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.039094, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.052316, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013956, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015738, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.013978, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017786, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020017, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6667, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.019098, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023882, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032416, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7333, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.028446, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030176, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051522, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7667, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.039094, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048889, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.079425, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.052316, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.021698`, avg `0.005635`, median `0.002901`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.031684`, avg `0.006385`, median `0.001226`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.037944`, avg `0.015161`, median `0.014259`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.038836`, avg `0.033414`, median `0.029911`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.024843`, avg `0.067525`, median `0.070816`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.020912`, avg `0.005554`, median `0.002901`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.032153`, avg `0.005335`, median `0.003191`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.1875`, primary_mae `0.036537`, avg `0.017332`, median `0.014259`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.1875`, primary_mae `0.038412`, avg `0.033797`, median `0.028709`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.5625`, primary_mae `0.033242`, avg `0.061012`, median `0.07382`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.021086`, avg `0.004812`, median `0.005578`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.020415`, avg `0.007649`, median `0.009377`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.025209`, avg `0.003323`, median `0.005647`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.037528`, avg `0.002283`, median `-0.008338`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.107421`, avg `0.03882`, median `0.031522`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.01599`, avg `0.005696`, median `0.006029`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4875`, primary_mae `0.020051`, avg `0.008783`, median `0.009948`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.028899`, avg `0.012161`, median `0.010117`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.425`, primary_mae `0.040579`, avg `0.019025`, median `0.026036`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.065283`, avg `0.033859`, median `0.047453`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.01599`, avg `0.005696`, median `0.006029`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4875`, primary_mae `0.020051`, avg `0.008783`, median `0.009948`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.028899`, avg `0.012161`, median `0.010117`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.425`, primary_mae `0.040579`, avg `0.019025`, median `0.026036`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.065283`, avg `0.033859`, median `0.047453`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.65`, primary_closer `0.4667`, primary_mae `0.013978`, avg `0.006058`, median `0.006029`
- 5d: sample `60`, primary_hit `0.6667`, primary_closer `0.5167`, primary_mae `0.019098`, avg `0.009745`, median `0.010594`
- 10d: sample `60`, primary_hit `0.7333`, primary_closer `0.45`, primary_mae `0.028446`, avg `0.014975`, median `0.014115`
- 20d: sample `60`, primary_hit `0.7667`, primary_closer `0.4167`, primary_mae `0.039094`, avg `0.022037`, median `0.028445`
- 60d: sample `60`, primary_hit `0.75`, primary_closer `0.6`, primary_mae `0.052316`, avg `0.032402`, median `0.050858`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022029`, avg `0.004608`, median `0.005578`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.02291`, avg `0.005896`, median `0.009377`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.030258`, avg `0.003721`, median `0.005647`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.045034`, avg `0.00999`, median `0.001221`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.2`, primary_mae `0.104185`, avg `0.03823`, median `0.031522`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.01599`, avg `0.005696`, median `0.006029`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4875`, primary_mae `0.020051`, avg `0.008783`, median `0.009948`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.028899`, avg `0.012161`, median `0.010117`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.425`, primary_mae `0.040579`, avg `0.019025`, median `0.026036`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.065283`, avg `0.033859`, median `0.047453`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
