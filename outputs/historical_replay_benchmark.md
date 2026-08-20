# Historical Replay Benchmark

Generated at: `2026-08-20T13:14:37.103296+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.021266`
- secondary_mean_absolute_error: `0.015929`
- primary_error_advantage: `-0.005337`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `20`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.026593`
- secondary_mean_absolute_error: `0.015836`
- primary_error_advantage: `-0.010757`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 10d
- sample_size: `20`
- primary_hit_rate: `0.7`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.032136`
- secondary_mean_absolute_error: `0.021605`
- primary_error_advantage: `-0.010531`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `20`
- primary_hit_rate: `0.8`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.051205`
- secondary_mean_absolute_error: `0.029122`
- primary_error_advantage: `-0.022083`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 60d
- sample_size: `20`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.068697`
- secondary_mean_absolute_error: `0.059118`
- primary_error_advantage: `-0.009579`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.55`, path_mae `0.015739`, as_primary `0`, as_primary_hit `None`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, direction_hit `0.55`, path_mae `0.019022`, as_primary `0`, as_primary_hit `None`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, direction_hit `0.7`, path_mae `0.022425`, as_primary `0`, as_primary_hit `None`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, direction_hit `0.8`, path_mae `0.032772`, as_primary `0`, as_primary_hit `None`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, direction_hit `0.55`, path_mae `0.060905`, as_primary `0`, as_primary_hit `None`, avg `0.028804`, median `0.038342`

### bounce_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.55`, path_mae `0.021266`, as_primary `20`, as_primary_hit `0.55`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, direction_hit `0.55`, path_mae `0.026593`, as_primary `20`, as_primary_hit `0.55`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, direction_hit `0.7`, path_mae `0.032136`, as_primary `20`, as_primary_hit `0.7`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, direction_hit `0.8`, path_mae `0.051205`, as_primary `20`, as_primary_hit `0.8`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, direction_hit `0.55`, path_mae `0.068697`, as_primary `20`, as_primary_hit `0.55`, avg `0.028804`, median `0.038342`

### failed_bounce_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.45`, path_mae `0.01957`, as_primary `0`, as_primary_hit `None`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, direction_hit `0.45`, path_mae `0.017275`, as_primary `0`, as_primary_hit `None`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, direction_hit `0.3`, path_mae `0.031382`, as_primary `0`, as_primary_hit `None`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, direction_hit `0.2`, path_mae `0.056313`, as_primary `0`, as_primary_hit `None`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, direction_hit `0.45`, path_mae `0.061219`, as_primary `0`, as_primary_hit `None`, avg `0.028804`, median `0.038342`

### analog_average_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.55`, path_mae `0.015929`, as_primary `0`, as_primary_hit `None`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, direction_hit `0.55`, path_mae `0.015836`, as_primary `0`, as_primary_hit `None`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, direction_hit `0.7`, path_mae `0.021605`, as_primary `0`, as_primary_hit `None`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, direction_hit `0.8`, path_mae `0.029122`, as_primary `0`, as_primary_hit `None`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, direction_hit `0.55`, path_mae `0.059118`, as_primary `0`, as_primary_hit `None`, avg `0.028804`, median `0.038342`

## Edge Status Performance

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.021266`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.026593`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.032136`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.051205`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068697`, avg `0.028804`, median `0.038342`

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
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.021266`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.026593`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.032136`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.051205`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068697`, avg `0.028804`, median `0.038342`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.021266, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.026593, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.032136, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.051205, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.068697, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 20, 'path_mean_absolute_error': 0.015739, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.021266, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.021266, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.015836, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.026593, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.026593, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.021605, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.032136, 'direction_hit_rate': 0.7}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.032136, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.8, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.029122, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.056313, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.051205, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.059118, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.068697, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.068697, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `2`
- 3d: sample `2`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.006675`, avg `0.015904`, median `0.015904`
- 5d: sample `2`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.013799`, avg `0.015529`, median `0.015529`
- 10d: sample `2`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.011552`, avg `0.023382`, median `0.023382`
- 20d: sample `2`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.043543`, avg `0.027687`, median `0.027687`
- 60d: sample `2`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.072078`, avg `0.024401`, median `0.024401`

### top_20
- sample_size: `4`
- 3d: sample `4`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.015331`, avg `0.006853`, median `0.005338`
- 5d: sample `4`, primary_hit `1.0`, primary_closer `0.25`, primary_mae `0.01923`, avg `0.010098`, median `0.009586`
- 10d: sample `4`, primary_hit `1.0`, primary_closer `0.75`, primary_mae `0.014003`, avg `0.02093`, median `0.023382`
- 20d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.058855`, avg `0.012375`, median `0.000839`
- 60d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.104018`, avg `-0.00754`, median `-0.035929`

### bottom_20
- sample_size: `4`
- 3d: sample `4`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.015331`, avg `0.006853`, median `0.005338`
- 5d: sample `4`, primary_hit `1.0`, primary_closer `0.25`, primary_mae `0.01923`, avg `0.010098`, median `0.009586`
- 10d: sample `4`, primary_hit `1.0`, primary_closer `0.75`, primary_mae `0.014003`, avg `0.02093`, median `0.023382`
- 20d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.058855`, avg `0.012375`, median `0.000839`
- 60d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.104018`, avg `-0.00754`, median `-0.035929`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.021266`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.026593`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.032136`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.051205`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068697`, avg `0.028804`, median `0.038342`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.021266`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.026593`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.032136`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.051205`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068697`, avg `0.028804`, median `0.038342`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.021266`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.026593`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.032136`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.051205`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068697`, avg `0.028804`, median `0.038342`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.021266`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.026593`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.032136`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.051205`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068697`, avg `0.028804`, median `0.038342`

### options_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.021266`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.026593`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.032136`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.051205`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068697`, avg `0.028804`, median `0.038342`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.021266`, avg `0.001527`, median `0.005338`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.026593`, avg `0.004948`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.032136`, avg `0.005827`, median `0.011059`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.051205`, avg `0.022569`, median `0.026122`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068697`, avg `0.028804`, median `0.038342`

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
