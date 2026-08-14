# Historical Replay Benchmark

Generated at: `2026-08-14T23:34:05.537539+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `20`
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
- sample_size: `20`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.6`
- primary_mean_absolute_error: `0.009615`
- secondary_mean_absolute_error: `0.010073`
- primary_error_advantage: `0.000458`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `20`
- primary_hit_rate: `0.75`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.009528`
- secondary_mean_absolute_error: `0.009402`
- primary_error_advantage: `-0.000126`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `20`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.01566`
- secondary_mean_absolute_error: `0.015108`
- primary_error_advantage: `-0.000552`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `20`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.032139`
- secondary_mean_absolute_error: `0.027503`
- primary_error_advantage: `-0.004636`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `20`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.060988`
- secondary_mean_absolute_error: `0.048413`
- primary_error_advantage: `-0.012575`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.5`, path_mae `0.010957`, as_primary `0`, as_primary_hit `None`, avg `-0.003311`, median `-0.00051`
- 5d: sample `20`, direction_hit `0.75`, path_mae `0.009493`, as_primary `0`, as_primary_hit `None`, avg `0.002904`, median `0.004845`
- 10d: sample `20`, direction_hit `0.45`, path_mae `0.015152`, as_primary `0`, as_primary_hit `None`, avg `0.000463`, median `-0.000945`
- 20d: sample `20`, direction_hit `0.6`, path_mae `0.026841`, as_primary `0`, as_primary_hit `None`, avg `-0.00291`, median `0.01014`
- 60d: sample `20`, direction_hit `0.4`, path_mae `0.051704`, as_primary `0`, as_primary_hit `None`, avg `-0.004822`, median `-0.017782`

### bounce_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.5`, path_mae `0.009615`, as_primary `20`, as_primary_hit `0.5`, avg `-0.003311`, median `-0.00051`
- 5d: sample `20`, direction_hit `0.75`, path_mae `0.009528`, as_primary `20`, as_primary_hit `0.75`, avg `0.002904`, median `0.004845`
- 10d: sample `20`, direction_hit `0.45`, path_mae `0.01566`, as_primary `20`, as_primary_hit `0.45`, avg `0.000463`, median `-0.000945`
- 20d: sample `20`, direction_hit `0.6`, path_mae `0.032139`, as_primary `20`, as_primary_hit `0.6`, avg `-0.00291`, median `0.01014`
- 60d: sample `20`, direction_hit `0.4`, path_mae `0.060988`, as_primary `20`, as_primary_hit `0.4`, avg `-0.004822`, median `-0.017782`

### failed_bounce_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.5`, path_mae `0.016995`, as_primary `0`, as_primary_hit `None`, avg `-0.003311`, median `-0.00051`
- 5d: sample `20`, direction_hit `0.25`, path_mae `0.009461`, as_primary `0`, as_primary_hit `None`, avg `0.002904`, median `0.004845`
- 10d: sample `20`, direction_hit `0.55`, path_mae `0.021534`, as_primary `0`, as_primary_hit `None`, avg `0.000463`, median `-0.000945`
- 20d: sample `20`, direction_hit `0.4`, path_mae `0.052676`, as_primary `0`, as_primary_hit `None`, avg `-0.00291`, median `0.01014`
- 60d: sample `20`, direction_hit `0.6`, path_mae `0.04996`, as_primary `0`, as_primary_hit `None`, avg `-0.004822`, median `-0.017782`

### analog_average_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.5`, path_mae `0.010073`, as_primary `0`, as_primary_hit `None`, avg `-0.003311`, median `-0.00051`
- 5d: sample `20`, direction_hit `0.75`, path_mae `0.009402`, as_primary `0`, as_primary_hit `None`, avg `0.002904`, median `0.004845`
- 10d: sample `20`, direction_hit `0.45`, path_mae `0.015108`, as_primary `0`, as_primary_hit `None`, avg `0.000463`, median `-0.000945`
- 20d: sample `20`, direction_hit `0.6`, path_mae `0.027503`, as_primary `0`, as_primary_hit `None`, avg `-0.00291`, median `0.01014`
- 60d: sample `20`, direction_hit `0.4`, path_mae `0.048413`, as_primary `0`, as_primary_hit `None`, avg `-0.004822`, median `-0.017782`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.009615`, avg `-0.003311`, median `-0.00051`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.009528`, avg `0.002904`, median `0.004845`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.01566`, avg `0.000463`, median `-0.000945`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.032139`, avg `-0.00291`, median `0.01014`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060988`, avg `-0.004822`, median `-0.017782`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.009615`, avg `-0.003311`, median `-0.00051`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.009528`, avg `0.002904`, median `0.004845`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.01566`, avg `0.000463`, median `-0.000945`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.032139`, avg `-0.00291`, median `0.01014`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060988`, avg `-0.004822`, median `-0.017782`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

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

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.009615, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.009528, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01566, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.032139, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.060988, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.6, 'best_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.009615, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.016995, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.009615, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.009402, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.009528, 'direction_hit_rate': 0.75}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.009528, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.015108, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.021534, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01566, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 20, 'path_mean_absolute_error': 0.026841, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.052676, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.032139, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.048413, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.060988, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.060988, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `2`
- 3d: sample `2`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.009301`, avg `0.008028`, median `0.008028`
- 5d: sample `2`, primary_hit `1.0`, primary_closer `0.0`, primary_mae `0.012582`, avg `0.014749`, median `0.014749`
- 10d: sample `2`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.013954`, avg `0.019931`, median `0.019931`
- 20d: sample `2`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.047025`, avg `-0.018402`, median `-0.018402`
- 60d: sample `2`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.082055`, avg `-0.039821`, median `-0.039821`

### top_20
- sample_size: `4`
- 3d: sample `4`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.009819`, avg `0.008546`, median `0.008028`
- 5d: sample `4`, primary_hit `1.0`, primary_closer `0.0`, primary_mae `0.010827`, avg `0.012993`, median `0.011238`
- 10d: sample `4`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.010329`, avg `0.016305`, median `0.016423`
- 20d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.029441`, avg `-0.000819`, median `-0.003639`
- 60d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.069491`, avg `-0.00688`, median `-0.033607`

### bottom_20
- sample_size: `4`
- 3d: sample `4`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.009819`, avg `0.008546`, median `0.008028`
- 5d: sample `4`, primary_hit `1.0`, primary_closer `0.0`, primary_mae `0.010827`, avg `0.012993`, median `0.011238`
- 10d: sample `4`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.010329`, avg `0.016305`, median `0.016423`
- 20d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.029441`, avg `-0.000819`, median `-0.003639`
- 60d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.069491`, avg `-0.00688`, median `-0.033607`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.009615`, avg `-0.003311`, median `-0.00051`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.009528`, avg `0.002904`, median `0.004845`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.01566`, avg `0.000463`, median `-0.000945`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.032139`, avg `-0.00291`, median `0.01014`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060988`, avg `-0.004822`, median `-0.017782`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.009615`, avg `-0.003311`, median `-0.00051`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.009528`, avg `0.002904`, median `0.004845`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.01566`, avg `0.000463`, median `-0.000945`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.032139`, avg `-0.00291`, median `0.01014`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060988`, avg `-0.004822`, median `-0.017782`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.009615`, avg `-0.003311`, median `-0.00051`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.009528`, avg `0.002904`, median `0.004845`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.01566`, avg `0.000463`, median `-0.000945`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.032139`, avg `-0.00291`, median `0.01014`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060988`, avg `-0.004822`, median `-0.017782`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.009615`, avg `-0.003311`, median `-0.00051`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.009528`, avg `0.002904`, median `0.004845`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.01566`, avg `0.000463`, median `-0.000945`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.032139`, avg `-0.00291`, median `0.01014`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060988`, avg `-0.004822`, median `-0.017782`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.009615`, avg `-0.003311`, median `-0.00051`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.009528`, avg `0.002904`, median `0.004845`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.01566`, avg `0.000463`, median `-0.000945`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.032139`, avg `-0.00291`, median `0.01014`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.060988`, avg `-0.004822`, median `-0.017782`

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
