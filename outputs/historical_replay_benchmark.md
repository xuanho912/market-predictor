# Historical Replay Benchmark

Generated at: `2026-09-03T00:49:40.362633+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.3833`, primary_mae `0.021973`, avg `0.00091`, median `0.003357`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.4333`, primary_mae `0.023022`, avg `0.002498`, median `0.007174`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.4667`, primary_mae `0.030827`, avg `0.008449`, median `0.011443`
- 20d: sample `60`, primary_hit `0.25`, primary_closer `0.3667`, primary_mae `0.047135`, avg `0.023816`, median `0.02921`
- 60d: sample `60`, primary_hit `0.25`, primary_closer `0.3333`, primary_mae `0.069973`, avg `0.049442`, median `0.07206`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.01882`, avg `0.016319`, median `0.021894`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.023923`, avg `0.017783`, median `0.023997`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.030195`, avg `0.026784`, median `0.026309`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.042974`, avg `0.036772`, median `0.034442`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.081578`, avg `0.055634`, median `0.071057`

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
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.3875`, primary_mae `0.021185`, avg `0.004762`, median `0.008399`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.425`, primary_mae `0.023247`, avg `0.006319`, median `0.00893`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.475`, primary_mae `0.030669`, avg `0.013032`, median `0.013781`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.375`, primary_mae `0.046095`, avg `0.027055`, median `0.031193`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.3875`, primary_mae `0.072874`, avg `0.05099`, median `0.071639`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3875, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.021185, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3875, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.023247, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3375, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.030669, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.2375, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.046095, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.072874, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017239, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021185, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3875, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.021185, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019364, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023247, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3875, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.023247, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024744, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031677, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3375, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.030669, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_vs_secondary_accuracy_spread': -0.525, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027447, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.046095, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.2375, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.046095, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062471, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072874, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.072874, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.039546`, avg `-0.005912`, median `0.000899`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.045002`, avg `0.000337`, median `0.005221`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.063399`, avg `0.011776`, median `0.029091`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.055727`, avg `0.008107`, median `0.028464`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.110831`, avg `0.01122`, median `0.035555`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.035091`, avg `-0.005452`, median `-0.000629`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.036043`, avg `-0.006571`, median `-0.011716`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.06051`, avg `0.009477`, median `0.024797`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.057566`, avg `0.013002`, median `0.021827`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.113128`, avg `0.021008`, median `0.061361`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.4375`, primary_mae `0.018154`, avg `0.015373`, median `0.019675`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.024017`, avg `0.014528`, median `0.019955`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.03379`, avg `0.029055`, median `0.028523`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.3125`, primary_mae `0.048649`, avg `0.043557`, median `0.041794`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.093315`, avg `0.04701`, median `0.040665`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

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
