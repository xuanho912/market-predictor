# Historical Replay Benchmark

Generated at: `2026-09-11T16:31:57.638715+00:00`
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
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.017863`
- secondary_mean_absolute_error: `0.01331`
- primary_error_advantage: `-0.004553`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.022694`
- secondary_mean_absolute_error: `0.01704`
- primary_error_advantage: `-0.005654`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.030412`
- secondary_mean_absolute_error: `0.022125`
- primary_error_advantage: `-0.008287`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.066378`
- secondary_mean_absolute_error: `0.039818`
- primary_error_advantage: `-0.02656`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.112829`
- secondary_mean_absolute_error: `0.083347`
- primary_error_advantage: `-0.029482`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.013441`, as_primary `0`, as_primary_hit `None`, avg `-0.001145`, median `0.000878`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.01691`, as_primary `0`, as_primary_hit `None`, avg `-0.003085`, median `0.000904`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.024584`, as_primary `0`, as_primary_hit `None`, avg `-0.002398`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.040701`, as_primary `0`, as_primary_hit `None`, avg `0.004722`, median `0.008518`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.083772`, as_primary `0`, as_primary_hit `None`, avg `0.01569`, median `0.038067`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.014891`, as_primary `0`, as_primary_hit `None`, avg `-0.001145`, median `0.000878`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.021481`, as_primary `0`, as_primary_hit `None`, avg `-0.003085`, median `0.000904`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.036097`, as_primary `0`, as_primary_hit `None`, avg `-0.002398`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.058972`, as_primary `0`, as_primary_hit `None`, avg `0.004722`, median `0.008518`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.099247`, as_primary `0`, as_primary_hit `None`, avg `0.01569`, median `0.038067`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.017863`, as_primary `80`, as_primary_hit `0.5625`, avg `-0.001145`, median `0.000878`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.022694`, as_primary `80`, as_primary_hit `0.55`, avg `-0.003085`, median `0.000904`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.030412`, as_primary `80`, as_primary_hit `0.4`, avg `-0.002398`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.4375`, path_mae `0.066378`, as_primary `80`, as_primary_hit `0.5625`, avg `0.004722`, median `0.008518`
- 60d: sample `80`, direction_hit `0.4125`, path_mae `0.112829`, as_primary `80`, as_primary_hit `0.5875`, avg `0.01569`, median `0.038067`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.01331`, as_primary `0`, as_primary_hit `None`, avg `-0.001145`, median `0.000878`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.01704`, as_primary `0`, as_primary_hit `None`, avg `-0.003085`, median `0.000904`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.022125`, as_primary `0`, as_primary_hit `None`, avg `-0.002398`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.039818`, as_primary `0`, as_primary_hit `None`, avg `0.004722`, median `0.008518`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.083347`, as_primary `0`, as_primary_hit `None`, avg `0.01569`, median `0.038067`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.017863`, avg `-0.001145`, median `0.000878`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.022694`, avg `-0.003085`, median `0.000904`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.030412`, avg `-0.002398`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.066378`, avg `0.004722`, median `0.008518`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.3375`, primary_mae `0.112829`, avg `0.01569`, median `0.038067`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.017863`, avg `-0.001145`, median `0.000878`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.022694`, avg `-0.003085`, median `0.000904`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.030412`, avg `-0.002398`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.066378`, avg `0.004722`, median `0.008518`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.3375`, primary_mae `0.112829`, avg `0.01569`, median `0.038067`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.017863, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.022694, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.030412, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.3125, 'primary_mean_absolute_error': 0.066378, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4125, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.112829, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01331, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017863, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.017863, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01691, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022694, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.022694, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022125, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036097, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.030412, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039818, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066378, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.3125, 'primary_mean_absolute_error': 0.066378, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.083347, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.112829, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4125, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.112829, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.022861`, avg `-0.00729`, median `-0.003521`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.022178`, avg `-0.013748`, median `-0.01025`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.016343`, avg `-0.005391`, median `-0.011067`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.05672`, avg `0.015877`, median `0.024617`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.101676`, avg `0.046433`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.022154`, avg `-0.010291`, median `-0.009708`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.023425`, avg `-0.012826`, median `-0.01025`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.5`, primary_mae `0.014925`, avg `-0.006898`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.052659`, avg `0.012814`, median `0.01014`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.093277`, avg `0.032712`, median `0.041779`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.016144`, avg `0.002734`, median `0.003143`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.025578`, avg `-0.002163`, median `-0.002624`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.040083`, avg `-0.015914`, median `-0.022053`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.086364`, avg `-0.025089`, median `-0.008413`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.174184`, avg `-0.030767`, median `0.063169`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.017863`, avg `-0.001145`, median `0.000878`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.022694`, avg `-0.003085`, median `0.000904`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.030412`, avg `-0.002398`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.066378`, avg `0.004722`, median `0.008518`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.3375`, primary_mae `0.112829`, avg `0.01569`, median `0.038067`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.017863`, avg `-0.001145`, median `0.000878`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.022694`, avg `-0.003085`, median `0.000904`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.030412`, avg `-0.002398`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.066378`, avg `0.004722`, median `0.008518`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.3375`, primary_mae `0.112829`, avg `0.01569`, median `0.038067`

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
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.017863`, avg `-0.001145`, median `0.000878`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.022694`, avg `-0.003085`, median `0.000904`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.030412`, avg `-0.002398`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.066378`, avg `0.004722`, median `0.008518`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.3375`, primary_mae `0.112829`, avg `0.01569`, median `0.038067`

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
