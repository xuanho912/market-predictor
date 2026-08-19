# Historical Replay Benchmark

Generated at: `2026-08-19T02:35:32.540469+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `20`
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
- sample_size: `20`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.012564`
- secondary_mean_absolute_error: `0.012178`
- primary_error_advantage: `-0.000386`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `20`
- primary_hit_rate: `0.2`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `-0.6`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.022628`
- secondary_mean_absolute_error: `0.015494`
- primary_error_advantage: `-0.007134`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `20`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.053832`
- secondary_mean_absolute_error: `0.039616`
- primary_error_advantage: `-0.014216`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `20`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.105033`
- secondary_mean_absolute_error: `0.075483`
- primary_error_advantage: `-0.02955`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 60d
- sample_size: `20`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.131695`
- secondary_mean_absolute_error: `0.122816`
- primary_error_advantage: `-0.008879`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.7`, path_mae `0.011547`, as_primary `0`, as_primary_hit `None`, avg `0.008118`, median `0.009894`
- 5d: sample `20`, direction_hit `0.8`, path_mae `0.013939`, as_primary `0`, as_primary_hit `None`, avg `0.008722`, median `0.01032`
- 10d: sample `20`, direction_hit `0.7`, path_mae `0.027942`, as_primary `0`, as_primary_hit `None`, avg `0.010894`, median `0.01607`
- 20d: sample `20`, direction_hit `0.7`, path_mae `0.047535`, as_primary `0`, as_primary_hit `None`, avg `0.007486`, median `0.021222`
- 60d: sample `20`, direction_hit `0.65`, path_mae `0.087254`, as_primary `0`, as_primary_hit `None`, avg `0.023778`, median `0.055727`

### bounce_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.7`, path_mae `0.012178`, as_primary `0`, as_primary_hit `None`, avg `0.008118`, median `0.009894`
- 5d: sample `20`, direction_hit `0.8`, path_mae `0.015494`, as_primary `0`, as_primary_hit `None`, avg `0.008722`, median `0.01032`
- 10d: sample `20`, direction_hit `0.7`, path_mae `0.039616`, as_primary `0`, as_primary_hit `None`, avg `0.010894`, median `0.01607`
- 20d: sample `20`, direction_hit `0.7`, path_mae `0.075483`, as_primary `0`, as_primary_hit `None`, avg `0.007486`, median `0.021222`
- 60d: sample `20`, direction_hit `0.65`, path_mae `0.122816`, as_primary `0`, as_primary_hit `None`, avg `0.023778`, median `0.055727`

### failed_bounce_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.3`, path_mae `0.012564`, as_primary `20`, as_primary_hit `0.7`, avg `0.008118`, median `0.009894`
- 5d: sample `20`, direction_hit `0.2`, path_mae `0.022628`, as_primary `20`, as_primary_hit `0.8`, avg `0.008722`, median `0.01032`
- 10d: sample `20`, direction_hit `0.3`, path_mae `0.053832`, as_primary `20`, as_primary_hit `0.7`, avg `0.010894`, median `0.01607`
- 20d: sample `20`, direction_hit `0.3`, path_mae `0.105033`, as_primary `20`, as_primary_hit `0.7`, avg `0.007486`, median `0.021222`
- 60d: sample `20`, direction_hit `0.35`, path_mae `0.131695`, as_primary `20`, as_primary_hit `0.65`, avg `0.023778`, median `0.055727`

### analog_average_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.7`, path_mae `0.011617`, as_primary `0`, as_primary_hit `None`, avg `0.008118`, median `0.009894`
- 5d: sample `20`, direction_hit `0.8`, path_mae `0.014054`, as_primary `0`, as_primary_hit `None`, avg `0.008722`, median `0.01032`
- 10d: sample `20`, direction_hit `0.7`, path_mae `0.028081`, as_primary `0`, as_primary_hit `None`, avg `0.010894`, median `0.01607`
- 20d: sample `20`, direction_hit `0.7`, path_mae `0.048975`, as_primary `0`, as_primary_hit `None`, avg `0.007486`, median `0.021222`
- 60d: sample `20`, direction_hit `0.65`, path_mae `0.095275`, as_primary `0`, as_primary_hit `None`, avg `0.023778`, median `0.055727`

## Edge Status Performance

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.012564`, avg `0.008118`, median `0.009894`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.022628`, avg `0.008722`, median `0.01032`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.053832`, avg `0.010894`, median `0.01607`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.105033`, avg `0.007486`, median `0.021222`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.131695`, avg `0.023778`, median `0.055727`

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
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.012564`, avg `0.008118`, median `0.009894`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.022628`, avg `0.008722`, median `0.01032`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.053832`, avg `0.010894`, median `0.01607`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.105033`, avg `0.007486`, median `0.021222`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.131695`, avg `0.023778`, median `0.055727`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.012564, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.022628, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.053832, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.105033, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.131695, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 20, 'path_mean_absolute_error': 0.011547, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.012564, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.012564, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': -0.6, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 20, 'path_mean_absolute_error': 0.013939, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.022628, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.022628, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 20, 'path_mean_absolute_error': 0.027942, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.053832, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.053832, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 20, 'path_mean_absolute_error': 0.047535, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.105033, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.105033, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 20, 'path_mean_absolute_error': 0.087254, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.131695, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.131695, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `2`
- 3d: sample `2`, primary_hit `0.5`, primary_closer `1.0`, primary_mae `0.003182`, avg `0.00246`, median `0.00246`
- 5d: sample `2`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.012129`, avg `0.004634`, median `0.004634`
- 10d: sample `2`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.049591`, avg `0.016892`, median `0.016892`
- 20d: sample `2`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.084157`, avg `-0.000888`, median `-0.000888`
- 60d: sample `2`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.070955`, avg `-0.014766`, median `-0.014766`

### top_20
- sample_size: `4`
- 3d: sample `4`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.009294`, avg `0.006148`, median `0.00246`
- 5d: sample `4`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.016689`, avg `0.009194`, median `0.008363`
- 10d: sample `4`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.047628`, avg `0.014929`, median `0.016892`
- 20d: sample `4`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.082152`, avg `-0.002893`, median `-0.004899`
- 60d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.112173`, avg `0.032878`, median `0.060238`

### bottom_20
- sample_size: `4`
- 3d: sample `4`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.009294`, avg `0.006148`, median `0.00246`
- 5d: sample `4`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.016689`, avg `0.009194`, median `0.008363`
- 10d: sample `4`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.047628`, avg `0.014929`, median `0.016892`
- 20d: sample `4`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.082152`, avg `-0.002893`, median `-0.004899`
- 60d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.112173`, avg `0.032878`, median `0.060238`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.012564`, avg `0.008118`, median `0.009894`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.022628`, avg `0.008722`, median `0.01032`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.053832`, avg `0.010894`, median `0.01607`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.105033`, avg `0.007486`, median `0.021222`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.131695`, avg `0.023778`, median `0.055727`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.012564`, avg `0.008118`, median `0.009894`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.022628`, avg `0.008722`, median `0.01032`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.053832`, avg `0.010894`, median `0.01607`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.105033`, avg `0.007486`, median `0.021222`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.131695`, avg `0.023778`, median `0.055727`

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
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.012564`, avg `0.008118`, median `0.009894`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.022628`, avg `0.008722`, median `0.01032`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.053832`, avg `0.010894`, median `0.01607`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.105033`, avg `0.007486`, median `0.021222`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.131695`, avg `0.023778`, median `0.055727`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.012564`, avg `0.008118`, median `0.009894`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.022628`, avg `0.008722`, median `0.01032`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.053832`, avg `0.010894`, median `0.01607`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.105033`, avg `0.007486`, median `0.021222`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.131695`, avg `0.023778`, median `0.055727`

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
