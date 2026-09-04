# Historical Replay Benchmark

Generated at: `2026-09-04T08:17:16.231322+00:00`
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
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.021185`
- secondary_mean_absolute_error: `0.017605`
- primary_error_advantage: `-0.00358`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3875`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.023247`
- secondary_mean_absolute_error: `0.020265`
- primary_error_advantage: `-0.002982`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.030669`
- secondary_mean_absolute_error: `0.027158`
- primary_error_advantage: `-0.003511`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2375`
- secondary_hit_rate: `0.7625`
- primary_vs_secondary_accuracy_spread: `-0.525`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.046095`
- secondary_mean_absolute_error: `0.036523`
- primary_error_advantage: `-0.009572`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.072874`
- secondary_mean_absolute_error: `0.059862`
- primary_error_advantage: `-0.013012`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3875`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.017239`, as_primary `0`, as_primary_hit `None`, avg `0.004762`, median `0.008399`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.019364`, as_primary `0`, as_primary_hit `None`, avg `0.006319`, median `0.00893`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.026581`, as_primary `0`, as_primary_hit `None`, avg `0.013032`, median `0.013781`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.02869`, as_primary `0`, as_primary_hit `None`, avg `0.027055`, median `0.031193`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.064154`, as_primary `0`, as_primary_hit `None`, avg `0.05099`, median `0.071639`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.018166`, as_primary `0`, as_primary_hit `None`, avg `0.004762`, median `0.008399`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.020396`, as_primary `0`, as_primary_hit `None`, avg `0.006319`, median `0.00893`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.031677`, as_primary `0`, as_primary_hit `None`, avg `0.013032`, median `0.013781`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.041291`, as_primary `0`, as_primary_hit `None`, avg `0.027055`, median `0.031193`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.067304`, as_primary `0`, as_primary_hit `None`, avg `0.05099`, median `0.071639`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.021185`, as_primary `80`, as_primary_hit `0.6125`, avg `0.004762`, median `0.008399`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.023247`, as_primary `80`, as_primary_hit `0.6125`, avg `0.006319`, median `0.00893`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.030669`, as_primary `80`, as_primary_hit `0.6625`, avg `0.013032`, median `0.013781`
- 20d: sample `80`, direction_hit `0.2375`, path_mae `0.046095`, as_primary `80`, as_primary_hit `0.7625`, avg `0.027055`, median `0.031193`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.072874`, as_primary `80`, as_primary_hit `0.725`, avg `0.05099`, median `0.071639`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.017446`, as_primary `0`, as_primary_hit `None`, avg `0.004762`, median `0.008399`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.019596`, as_primary `0`, as_primary_hit `None`, avg `0.006319`, median `0.00893`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.024744`, as_primary `0`, as_primary_hit `None`, avg `0.013032`, median `0.013781`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.027447`, as_primary `0`, as_primary_hit `None`, avg `0.027055`, median `0.031193`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.062471`, as_primary `0`, as_primary_hit `None`, avg `0.05099`, median `0.071639`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3875`, primary_mae `0.021185`, avg `0.004762`, median `0.008399`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.425`, primary_mae `0.023247`, avg `0.006319`, median `0.00893`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.475`, primary_mae `0.030669`, avg `0.013032`, median `0.013781`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.375`, primary_mae `0.046095`, avg `0.027055`, median `0.031193`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.3875`, primary_mae `0.072874`, avg `0.05099`, median `0.071639`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.016388`, avg `0.000382`, median `0.004678`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.015655`, avg `0.001026`, median `0.007174`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.01854`, avg `0.003876`, median `0.00833`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.037681`, avg `0.025325`, median `0.031151`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.35`, primary_mae `0.049042`, avg `0.053513`, median `0.064049`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.3833`, primary_mae `0.022784`, avg `0.006222`, median `0.012398`
- 5d: sample `60`, primary_hit `0.3667`, primary_closer `0.4167`, primary_mae `0.025778`, avg `0.008084`, median `0.012062`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.5167`, primary_mae `0.034712`, avg `0.016084`, median `0.019142`
- 20d: sample `60`, primary_hit `0.2333`, primary_closer `0.4167`, primary_mae `0.048899`, avg `0.027632`, median `0.031193`
- 60d: sample `60`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.080818`, avg `0.05015`, median `0.073824`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016388, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.015655, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.01854, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.037681, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.049042, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017239, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021185, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016388, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019364, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023247, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.015655, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024744, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031677, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.01854, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_vs_secondary_accuracy_spread': -0.525, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027447, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.046095, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.037681, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062471, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072874, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.049042, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016305`, avg `-0.001901`, median `-0.001624`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.015369`, avg `0.006282`, median `0.008828`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.017644`, avg `0.009959`, median `0.01205`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.054144`, avg `0.042258`, median `0.050926`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.625`, primary_mae `0.032501`, avg `0.099899`, median `0.120549`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.013912`, avg `0.005213`, median `0.008014`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.01512`, avg `0.007436`, median `0.008828`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.625`, primary_mae `0.014781`, avg `0.012923`, median `0.015353`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.044676`, avg `0.030588`, median `0.025647`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.375`, primary_mae `0.034882`, avg `0.08716`, median `0.099778`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.4375`, primary_mae `0.018154`, avg `0.015373`, median `0.019675`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.024017`, avg `0.014528`, median `0.019955`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.03379`, avg `0.029055`, median `0.028523`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.3125`, primary_mae `0.048649`, avg `0.043557`, median `0.041794`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.093315`, avg `0.04701`, median `0.040665`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3875`, primary_mae `0.021185`, avg `0.004762`, median `0.008399`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.425`, primary_mae `0.023247`, avg `0.006319`, median `0.00893`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.475`, primary_mae `0.030669`, avg `0.013032`, median `0.013781`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.375`, primary_mae `0.046095`, avg `0.027055`, median `0.031193`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.3875`, primary_mae `0.072874`, avg `0.05099`, median `0.071639`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3875`, primary_mae `0.021185`, avg `0.004762`, median `0.008399`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.425`, primary_mae `0.023247`, avg `0.006319`, median `0.00893`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.475`, primary_mae `0.030669`, avg `0.013032`, median `0.013781`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.375`, primary_mae `0.046095`, avg `0.027055`, median `0.031193`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.3875`, primary_mae `0.072874`, avg `0.05099`, median `0.071639`

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
- 3d: sample `60`, primary_hit `0.3333`, primary_closer `0.4167`, primary_mae `0.016638`, avg `0.007791`, median `0.012244`
- 5d: sample `60`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.018276`, avg `0.009577`, median `0.011806`
- 10d: sample `60`, primary_hit `0.3`, primary_closer `0.4833`, primary_mae `0.021559`, avg `0.014847`, median `0.013781`
- 20d: sample `60`, primary_hit `0.2333`, primary_closer `0.3833`, primary_mae `0.041518`, avg `0.030783`, median `0.033268`
- 60d: sample `60`, primary_hit `0.2333`, primary_closer `0.4167`, primary_mae `0.058498`, avg `0.062029`, median `0.079408`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3875`, primary_mae `0.021185`, avg `0.004762`, median `0.008399`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.425`, primary_mae `0.023247`, avg `0.006319`, median `0.00893`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.475`, primary_mae `0.030669`, avg `0.013032`, median `0.013781`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.375`, primary_mae `0.046095`, avg `0.027055`, median `0.031193`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.3875`, primary_mae `0.072874`, avg `0.05099`, median `0.071639`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.025607`, avg `-0.001971`, median `0.001552`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.026908`, avg `-0.001214`, median `0.002581`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.038269`, avg `0.005732`, median `0.00833`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.048753`, avg `0.020599`, median `0.02921`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.082522`, avg `0.035694`, median `0.063114`

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
