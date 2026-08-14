# Historical Replay Benchmark

Generated at: `2026-08-14T21:55:11.722165+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.019014`
- secondary_mean_absolute_error: `0.015562`
- primary_error_advantage: `-0.003452`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `20`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.025747`
- secondary_mean_absolute_error: `0.016652`
- primary_error_advantage: `-0.009095`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `20`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.03112`
- secondary_mean_absolute_error: `0.022193`
- primary_error_advantage: `-0.008927`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `20`
- primary_hit_rate: `0.75`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.2`
- primary_mean_absolute_error: `0.058667`
- secondary_mean_absolute_error: `0.036778`
- primary_error_advantage: `-0.021889`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `20`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.076456`
- secondary_mean_absolute_error: `0.069144`
- primary_error_advantage: `-0.007312`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.5`, path_mae `0.016063`, as_primary `0`, as_primary_hit `None`, avg `-1.1e-05`, median `-0.000883`
- 5d: sample `20`, direction_hit `0.5`, path_mae `0.018871`, as_primary `0`, as_primary_hit `None`, avg `0.002265`, median `0.000744`
- 10d: sample `20`, direction_hit `0.65`, path_mae `0.023257`, as_primary `0`, as_primary_hit `None`, avg `0.004346`, median `0.007439`
- 20d: sample `20`, direction_hit `0.75`, path_mae `0.0361`, as_primary `0`, as_primary_hit `None`, avg `0.012746`, median `0.023697`
- 60d: sample `20`, direction_hit `0.5`, path_mae `0.069162`, as_primary `0`, as_primary_hit `None`, avg `0.01137`, median `0.012785`

### bounce_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.5`, path_mae `0.019014`, as_primary `20`, as_primary_hit `0.5`, avg `-1.1e-05`, median `-0.000883`
- 5d: sample `20`, direction_hit `0.5`, path_mae `0.025747`, as_primary `20`, as_primary_hit `0.5`, avg `0.002265`, median `0.000744`
- 10d: sample `20`, direction_hit `0.65`, path_mae `0.03112`, as_primary `20`, as_primary_hit `0.65`, avg `0.004346`, median `0.007439`
- 20d: sample `20`, direction_hit `0.75`, path_mae `0.058667`, as_primary `20`, as_primary_hit `0.75`, avg `0.012746`, median `0.023697`
- 60d: sample `20`, direction_hit `0.5`, path_mae `0.076456`, as_primary `20`, as_primary_hit `0.5`, avg `0.01137`, median `0.012785`

### failed_bounce_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.5`, path_mae `0.018398`, as_primary `0`, as_primary_hit `None`, avg `-1.1e-05`, median `-0.000883`
- 5d: sample `20`, direction_hit `0.5`, path_mae `0.019133`, as_primary `0`, as_primary_hit `None`, avg `0.002265`, median `0.000744`
- 10d: sample `20`, direction_hit `0.35`, path_mae `0.029045`, as_primary `0`, as_primary_hit `None`, avg `0.004346`, median `0.007439`
- 20d: sample `20`, direction_hit `0.25`, path_mae `0.077921`, as_primary `0`, as_primary_hit `None`, avg `0.012746`, median `0.023697`
- 60d: sample `20`, direction_hit `0.5`, path_mae `0.09146`, as_primary `0`, as_primary_hit `None`, avg `0.01137`, median `0.012785`

### analog_average_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.5`, path_mae `0.015562`, as_primary `0`, as_primary_hit `None`, avg `-1.1e-05`, median `-0.000883`
- 5d: sample `20`, direction_hit `0.5`, path_mae `0.016652`, as_primary `0`, as_primary_hit `None`, avg `0.002265`, median `0.000744`
- 10d: sample `20`, direction_hit `0.65`, path_mae `0.022193`, as_primary `0`, as_primary_hit `None`, avg `0.004346`, median `0.007439`
- 20d: sample `20`, direction_hit `0.75`, path_mae `0.036778`, as_primary `0`, as_primary_hit `None`, avg `0.012746`, median `0.023697`
- 60d: sample `20`, direction_hit `0.5`, path_mae `0.069144`, as_primary `0`, as_primary_hit `None`, avg `0.01137`, median `0.012785`

## Edge Status Performance

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.019014`, avg `-1.1e-05`, median `-0.000883`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.025747`, avg `0.002265`, median `0.000744`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.03112`, avg `0.004346`, median `0.007439`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.058667`, avg `0.012746`, median `0.023697`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.076456`, avg `0.01137`, median `0.012785`

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
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.019014`, avg `-1.1e-05`, median `-0.000883`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.025747`, avg `0.002265`, median `0.000744`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.03112`, avg `0.004346`, median `0.007439`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.058667`, avg `0.012746`, median `0.023697`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.076456`, avg `0.01137`, median `0.012785`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019014, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.025747, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.03112, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.058667, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.076456, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.015562, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.019014, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019014, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.016652, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.025747, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.025747, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.022193, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.03112, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.03112, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.2, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 20, 'path_mean_absolute_error': 0.0361, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.077921, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.058667, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.069144, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.09146, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.076456, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `2`
- 3d: sample `2`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.006675`, avg `0.015904`, median `0.015904`
- 5d: sample `2`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.008758`, avg `0.015529`, median `0.015529`
- 10d: sample `2`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.007985`, avg `0.023382`, median `0.023382`
- 20d: sample `2`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.04017`, avg `0.027687`, median `0.027687`
- 60d: sample `2`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.062703`, avg `0.024401`, median `0.024401`

### top_20
- sample_size: `4`
- 3d: sample `4`, primary_hit `1.0`, primary_closer `0.75`, primary_mae `0.007609`, avg `0.011449`, median `0.010886`
- 5d: sample `4`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.012959`, avg `0.011328`, median `0.012047`
- 10d: sample `4`, primary_hit `1.0`, primary_closer `0.75`, primary_mae `0.012914`, avg `0.018453`, median `0.023382`
- 20d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.051611`, avg `0.016246`, median `0.008581`
- 60d: sample `4`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.064148`, avg `0.022295`, median `0.02374`

### bottom_20
- sample_size: `4`
- 3d: sample `4`, primary_hit `1.0`, primary_closer `0.75`, primary_mae `0.007609`, avg `0.011449`, median `0.010886`
- 5d: sample `4`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.012959`, avg `0.011328`, median `0.012047`
- 10d: sample `4`, primary_hit `1.0`, primary_closer `0.75`, primary_mae `0.012914`, avg `0.018453`, median `0.023382`
- 20d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.051611`, avg `0.016246`, median `0.008581`
- 60d: sample `4`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.064148`, avg `0.022295`, median `0.02374`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.019014`, avg `-1.1e-05`, median `-0.000883`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.025747`, avg `0.002265`, median `0.000744`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.03112`, avg `0.004346`, median `0.007439`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.058667`, avg `0.012746`, median `0.023697`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.076456`, avg `0.01137`, median `0.012785`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.019014`, avg `-1.1e-05`, median `-0.000883`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.025747`, avg `0.002265`, median `0.000744`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.03112`, avg `0.004346`, median `0.007439`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.058667`, avg `0.012746`, median `0.023697`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.076456`, avg `0.01137`, median `0.012785`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.019014`, avg `-1.1e-05`, median `-0.000883`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.025747`, avg `0.002265`, median `0.000744`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.03112`, avg `0.004346`, median `0.007439`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.058667`, avg `0.012746`, median `0.023697`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.076456`, avg `0.01137`, median `0.012785`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.019014`, avg `-1.1e-05`, median `-0.000883`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.025747`, avg `0.002265`, median `0.000744`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.03112`, avg `0.004346`, median `0.007439`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.058667`, avg `0.012746`, median `0.023697`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.076456`, avg `0.01137`, median `0.012785`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.019014`, avg `-1.1e-05`, median `-0.000883`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.025747`, avg `0.002265`, median `0.000744`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.03112`, avg `0.004346`, median `0.007439`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.058667`, avg `0.012746`, median `0.023697`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.076456`, avg `0.01137`, median `0.012785`

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
