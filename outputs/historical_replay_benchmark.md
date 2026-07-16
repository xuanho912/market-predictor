# Historical Replay Benchmark

Generated at: `2026-07-16T14:26:45.194326+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.018218`
- secondary_mean_absolute_error: `0.014804`
- primary_error_advantage: `-0.003414`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.0219`
- secondary_mean_absolute_error: `0.016155`
- primary_error_advantage: `-0.005745`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.023561`
- secondary_mean_absolute_error: `0.020577`
- primary_error_advantage: `-0.002984`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.054754`
- secondary_mean_absolute_error: `0.041035`
- primary_error_advantage: `-0.013719`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.7`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.090343`
- secondary_mean_absolute_error: `0.075862`
- primary_error_advantage: `-0.014481`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.75`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.014978`, as_primary `0`, as_primary_hit `None`, avg `-0.002924`, median `0.0`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.016153`, as_primary `0`, as_primary_hit `None`, avg `-0.001635`, median `0.001204`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.0188`, as_primary `0`, as_primary_hit `None`, avg `-0.003197`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.031725`, as_primary `0`, as_primary_hit `None`, avg `0.004251`, median `0.003958`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.072089`, as_primary `0`, as_primary_hit `None`, avg `0.006164`, median `0.00973`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015441`, as_primary `0`, as_primary_hit `None`, avg `-0.002924`, median `0.0`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.016168`, as_primary `0`, as_primary_hit `None`, avg `-0.001635`, median `0.001204`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.021469`, as_primary `0`, as_primary_hit `None`, avg `-0.003197`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.046595`, as_primary `0`, as_primary_hit `None`, avg `0.004251`, median `0.003958`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.084162`, as_primary `0`, as_primary_hit `None`, avg `0.006164`, median `0.00973`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.018218`, as_primary `80`, as_primary_hit `0.5`, avg `-0.002924`, median `0.0`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.0219`, as_primary `80`, as_primary_hit `0.55`, avg `-0.001635`, median `0.001204`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.023561`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.003197`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.4`, path_mae `0.054754`, as_primary `80`, as_primary_hit `0.6`, avg `0.004251`, median `0.003958`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.090343`, as_primary `80`, as_primary_hit `0.5625`, avg `0.006164`, median `0.00973`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.014331`, as_primary `0`, as_primary_hit `None`, avg `-0.002924`, median `0.0`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.015901`, as_primary `0`, as_primary_hit `None`, avg `-0.001635`, median `0.001204`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.018336`, as_primary `0`, as_primary_hit `None`, avg `-0.003197`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.03001`, as_primary `0`, as_primary_hit `None`, avg `0.004251`, median `0.003958`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.065568`, as_primary `0`, as_primary_hit `None`, avg `0.006164`, median `0.00973`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.018218`, avg `-0.002924`, median `0.0`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.0219`, avg `-0.001635`, median `0.001204`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.023561`, avg `-0.003197`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.054754`, avg `0.004251`, median `0.003958`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.45`, primary_mae `0.090343`, avg `0.006164`, median `0.00973`

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
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.3833`, primary_mae `0.018432`, avg `-0.004738`, median `-0.001391`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.3833`, primary_mae `0.022341`, avg `-0.004472`, median `2.2e-05`
- 10d: sample `60`, primary_hit `0.6667`, primary_closer `0.3333`, primary_mae `0.023843`, avg `-0.009393`, median `-0.010905`
- 20d: sample `60`, primary_hit `0.4333`, primary_closer `0.2667`, primary_mae `0.062067`, avg `-0.000715`, median `0.003247`
- 60d: sample `60`, primary_hit `0.4667`, primary_closer `0.35`, primary_mae `0.100179`, avg `-0.004521`, median `0.006776`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.017579`, avg `0.002518`, median `0.007125`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.020575`, avg `0.006879`, median `0.006624`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.6`, primary_mae `0.022716`, avg `0.015394`, median `0.0181`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.7`, primary_mae `0.032814`, avg `0.019147`, median `0.007521`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.75`, primary_mae `0.060833`, avg `0.038217`, median `0.044193`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.017579, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.020575, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.022716, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.032814, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.060833, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014331, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018218, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.017579, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015901, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0219, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.020575, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018336, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023561, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.022716, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03001, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054754, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.032814, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065568, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.090343, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.060833, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019651`, avg `-0.00328`, median `-0.004067`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.024741`, avg `-0.000619`, median `-0.004712`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.030498`, avg `0.020756`, median `0.029419`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.5`, primary_mae `0.046549`, avg `0.034681`, median `0.032972`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.074607`, avg `0.041882`, median `0.032175`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020308`, avg `0.000894`, median `0.002096`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.023463`, avg `0.004988`, median `0.003601`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.025552`, avg `0.01756`, median `0.026575`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.036796`, avg `0.024898`, median `0.009478`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.6875`, primary_mae `0.061428`, avg `0.052531`, median `0.056741`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.009806`, avg `-0.007497`, median `-0.005289`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.014215`, avg `-0.003165`, median `0.001499`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.01735`, avg `-0.002623`, median `-0.004397`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.125`, primary_mae `0.040399`, avg `0.002688`, median `0.002615`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.047414`, avg `-0.019762`, median `-0.016937`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.018218`, avg `-0.002924`, median `0.0`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.0219`, avg `-0.001635`, median `0.001204`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.023561`, avg `-0.003197`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.054754`, avg `0.004251`, median `0.003958`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.45`, primary_mae `0.090343`, avg `0.006164`, median `0.00973`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.018218`, avg `-0.002924`, median `0.0`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.0219`, avg `-0.001635`, median `0.001204`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.023561`, avg `-0.003197`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.054754`, avg `0.004251`, median `0.003958`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.45`, primary_mae `0.090343`, avg `0.006164`, median `0.00973`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.018633`, avg `0.001219`, median `0.003732`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.023469`, avg `0.004215`, median `0.005394`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.025027`, avg `0.001973`, median `0.000849`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.575`, primary_mae `0.050519`, avg `0.009564`, median `0.006184`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.55`, primary_mae `0.103581`, avg `0.018082`, median `0.024439`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.5`, primary_mae `0.017729`, avg `-0.003871`, median `-0.00205`
- 5d: sample `60`, primary_hit `0.4333`, primary_closer `0.4167`, primary_mae `0.020412`, avg `-0.002696`, median `0.001204`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.4167`, primary_mae `0.022302`, avg `-0.000446`, median `-0.001038`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.35`, primary_mae `0.050264`, avg `0.005673`, median `0.003958`
- 60d: sample `60`, primary_hit `0.45`, primary_closer `0.4833`, primary_mae `0.07168`, avg `0.008903`, median `0.006776`

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
