# Historical Replay Benchmark

Generated at: `2026-08-17T13:08:50.681815+00:00`
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
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.021677`
- secondary_mean_absolute_error: `0.015618`
- primary_error_advantage: `-0.006059`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `20`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.025223`
- secondary_mean_absolute_error: `0.014566`
- primary_error_advantage: `-0.010657`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `20`
- primary_hit_rate: `0.7`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.028583`
- secondary_mean_absolute_error: `0.017697`
- primary_error_advantage: `-0.010886`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `20`
- primary_hit_rate: `0.85`
- secondary_hit_rate: `0.85`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.049183`
- secondary_mean_absolute_error: `0.02689`
- primary_error_advantage: `-0.022293`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `20`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.067878`
- secondary_mean_absolute_error: `0.058218`
- primary_error_advantage: `-0.00966`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.6`, path_mae `0.015705`, as_primary `0`, as_primary_hit `None`, avg `0.002108`, median `0.007972`
- 5d: sample `20`, direction_hit `0.6`, path_mae `0.018183`, as_primary `0`, as_primary_hit `None`, avg `0.006318`, median `0.004667`
- 10d: sample `20`, direction_hit `0.7`, path_mae `0.020467`, as_primary `0`, as_primary_hit `None`, avg `0.009379`, median `0.011059`
- 20d: sample `20`, direction_hit `0.85`, path_mae `0.031574`, as_primary `0`, as_primary_hit `None`, avg `0.024591`, median `0.026122`
- 60d: sample `20`, direction_hit `0.6`, path_mae `0.059959`, as_primary `0`, as_primary_hit `None`, avg `0.029623`, median `0.038342`

### bounce_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.6`, path_mae `0.021677`, as_primary `20`, as_primary_hit `0.6`, avg `0.002108`, median `0.007972`
- 5d: sample `20`, direction_hit `0.6`, path_mae `0.025223`, as_primary `20`, as_primary_hit `0.6`, avg `0.006318`, median `0.004667`
- 10d: sample `20`, direction_hit `0.7`, path_mae `0.028583`, as_primary `20`, as_primary_hit `0.7`, avg `0.009379`, median `0.011059`
- 20d: sample `20`, direction_hit `0.85`, path_mae `0.049183`, as_primary `20`, as_primary_hit `0.85`, avg `0.024591`, median `0.026122`
- 60d: sample `20`, direction_hit `0.6`, path_mae `0.067878`, as_primary `20`, as_primary_hit `0.6`, avg `0.029623`, median `0.038342`

### failed_bounce_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.4`, path_mae `0.018662`, as_primary `0`, as_primary_hit `None`, avg `0.002108`, median `0.007972`
- 5d: sample `20`, direction_hit `0.4`, path_mae `0.0157`, as_primary `0`, as_primary_hit `None`, avg `0.006318`, median `0.004667`
- 10d: sample `20`, direction_hit `0.3`, path_mae `0.019928`, as_primary `0`, as_primary_hit `None`, avg `0.009379`, median `0.011059`
- 20d: sample `20`, direction_hit `0.15`, path_mae `0.053625`, as_primary `0`, as_primary_hit `None`, avg `0.024591`, median `0.026122`
- 60d: sample `20`, direction_hit `0.4`, path_mae `0.06178`, as_primary `0`, as_primary_hit `None`, avg `0.029623`, median `0.038342`

### analog_average_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.6`, path_mae `0.015618`, as_primary `0`, as_primary_hit `None`, avg `0.002108`, median `0.007972`
- 5d: sample `20`, direction_hit `0.6`, path_mae `0.014566`, as_primary `0`, as_primary_hit `None`, avg `0.006318`, median `0.004667`
- 10d: sample `20`, direction_hit `0.7`, path_mae `0.017697`, as_primary `0`, as_primary_hit `None`, avg `0.009379`, median `0.011059`
- 20d: sample `20`, direction_hit `0.85`, path_mae `0.02689`, as_primary `0`, as_primary_hit `None`, avg `0.024591`, median `0.026122`
- 60d: sample `20`, direction_hit `0.6`, path_mae `0.058218`, as_primary `0`, as_primary_hit `None`, avg `0.029623`, median `0.038342`

## Edge Status Performance

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.021677`, avg `0.002108`, median `0.007972`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.25`, primary_mae `0.025223`, avg `0.006318`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.028583`, avg `0.009379`, median `0.011059`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.049183`, avg `0.024591`, median `0.026122`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.067878`, avg `0.029623`, median `0.038342`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.021677`, avg `0.002108`, median `0.007972`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.25`, primary_mae `0.025223`, avg `0.006318`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.028583`, avg `0.009379`, median `0.011059`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.049183`, avg `0.024591`, median `0.026122`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.067878`, avg `0.029623`, median `0.038342`

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

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.021677, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.025223, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.028583, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.049183, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.067878, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.015618, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.021677, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.021677, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.014566, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.025223, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.025223, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.017697, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.028583, 'direction_hit_rate': 0.7}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.028583, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.85, 'secondary_hit_rate': 0.85, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.02689, 'direction_hit_rate': 0.85}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.053625, 'direction_hit_rate': 0.15}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.049183, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.058218, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.067878, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.067878, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `2`
- 3d: sample `2`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.007174`, avg `0.015904`, median `0.015904`
- 5d: sample `2`, primary_hit `1.0`, primary_closer `0.0`, primary_mae `0.013799`, avg `0.015529`, median `0.015529`
- 10d: sample `2`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.011552`, avg `0.023382`, median `0.023382`
- 20d: sample `2`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.043543`, avg `0.027687`, median `0.027687`
- 60d: sample `2`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.072078`, avg `0.024401`, median `0.024401`

### top_20
- sample_size: `4`
- 3d: sample `4`, primary_hit `1.0`, primary_closer `0.25`, primary_mae `0.011629`, avg `0.011449`, median `0.010886`
- 5d: sample `4`, primary_hit `1.0`, primary_closer `0.0`, primary_mae `0.018`, avg `0.011328`, median `0.012047`
- 10d: sample `4`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.016481`, avg `0.018453`, median `0.023382`
- 20d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.054984`, avg `0.016246`, median `0.008581`
- 60d: sample `4`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.074184`, avg `0.022295`, median `0.02374`

### bottom_20
- sample_size: `4`
- 3d: sample `4`, primary_hit `1.0`, primary_closer `0.25`, primary_mae `0.011629`, avg `0.011449`, median `0.010886`
- 5d: sample `4`, primary_hit `1.0`, primary_closer `0.0`, primary_mae `0.018`, avg `0.011328`, median `0.012047`
- 10d: sample `4`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.016481`, avg `0.018453`, median `0.023382`
- 20d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.054984`, avg `0.016246`, median `0.008581`
- 60d: sample `4`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.074184`, avg `0.022295`, median `0.02374`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.021677`, avg `0.002108`, median `0.007972`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.25`, primary_mae `0.025223`, avg `0.006318`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.028583`, avg `0.009379`, median `0.011059`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.049183`, avg `0.024591`, median `0.026122`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.067878`, avg `0.029623`, median `0.038342`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.021677`, avg `0.002108`, median `0.007972`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.25`, primary_mae `0.025223`, avg `0.006318`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.028583`, avg `0.009379`, median `0.011059`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.049183`, avg `0.024591`, median `0.026122`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.067878`, avg `0.029623`, median `0.038342`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.021677`, avg `0.002108`, median `0.007972`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.25`, primary_mae `0.025223`, avg `0.006318`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.028583`, avg `0.009379`, median `0.011059`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.049183`, avg `0.024591`, median `0.026122`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.067878`, avg `0.029623`, median `0.038342`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.021677`, avg `0.002108`, median `0.007972`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.25`, primary_mae `0.025223`, avg `0.006318`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.028583`, avg `0.009379`, median `0.011059`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.049183`, avg `0.024591`, median `0.026122`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.067878`, avg `0.029623`, median `0.038342`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.021677`, avg `0.002108`, median `0.007972`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.25`, primary_mae `0.025223`, avg `0.006318`, median `0.004667`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.028583`, avg `0.009379`, median `0.011059`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.049183`, avg `0.024591`, median `0.026122`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.067878`, avg `0.029623`, median `0.038342`

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
