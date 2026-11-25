# Historical Replay Benchmark

Generated at: `2026-11-25T04:34:29.087561+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.026137`
- secondary_mean_absolute_error: `0.024261`
- primary_error_advantage: `-0.001876`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.028822`
- secondary_mean_absolute_error: `0.027739`
- primary_error_advantage: `-0.001083`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2125`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.028349`
- secondary_mean_absolute_error: `0.034082`
- primary_error_advantage: `0.005733`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.7`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.053229`
- secondary_mean_absolute_error: `0.044481`
- primary_error_advantage: `-0.008748`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.068834`
- secondary_mean_absolute_error: `0.070267`
- primary_error_advantage: `0.001433`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.022767`, as_primary `0`, as_primary_hit `None`, avg `0.001871`, median `0.001684`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.027133`, as_primary `0`, as_primary_hit `None`, avg `0.005122`, median `0.002949`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.031017`, as_primary `0`, as_primary_hit `None`, avg `0.011755`, median `0.005498`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.038001`, as_primary `0`, as_primary_hit `None`, avg `0.008501`, median `0.005051`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.069725`, as_primary `0`, as_primary_hit `None`, avg `0.05066`, median `0.061523`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.025935`, as_primary `0`, as_primary_hit `None`, avg `0.001871`, median `0.001684`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.028881`, as_primary `0`, as_primary_hit `None`, avg `0.005122`, median `0.002949`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.036962`, as_primary `0`, as_primary_hit `None`, avg `0.011755`, median `0.005498`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.063572`, as_primary `0`, as_primary_hit `None`, avg `0.008501`, median `0.005051`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.094521`, as_primary `0`, as_primary_hit `None`, avg `0.05066`, median `0.061523`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.026137`, as_primary `80`, as_primary_hit `0.5`, avg `0.001871`, median `0.001684`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.028822`, as_primary `80`, as_primary_hit `0.5625`, avg `0.005122`, median `0.002949`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.028349`, as_primary `80`, as_primary_hit `0.6`, avg `0.011755`, median `0.005498`
- 20d: sample `80`, direction_hit `0.45`, path_mae `0.053229`, as_primary `80`, as_primary_hit `0.55`, avg `0.008501`, median `0.005051`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.068834`, as_primary `80`, as_primary_hit `0.725`, avg `0.05066`, median `0.061523`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.022419`, as_primary `0`, as_primary_hit `None`, avg `0.001871`, median `0.001684`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.025405`, as_primary `0`, as_primary_hit `None`, avg `0.005122`, median `0.002949`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.026406`, as_primary `0`, as_primary_hit `None`, avg `0.011755`, median `0.005498`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.034044`, as_primary `0`, as_primary_hit `None`, avg `0.008501`, median `0.005051`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.065386`, as_primary `0`, as_primary_hit `None`, avg `0.05066`, median `0.061523`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.026137`, avg `0.001871`, median `0.001684`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4625`, primary_mae `0.028822`, avg `0.005122`, median `0.002949`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.028349`, avg `0.011755`, median `0.005498`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.053229`, avg `0.008501`, median `0.005051`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.475`, primary_mae `0.068834`, avg `0.05066`, median `0.061523`

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
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.45`, primary_mae `0.024046`, avg `0.000249`, median `-0.00118`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4167`, primary_mae `0.026821`, avg `0.002139`, median `0.001655`
- 10d: sample `60`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.025284`, avg `0.008977`, median `0.005438`
- 20d: sample `60`, primary_hit `0.5`, primary_closer `0.3167`, primary_mae `0.046379`, avg `0.004791`, median `0.000359`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.45`, primary_mae `0.066367`, avg `0.039371`, median `0.061523`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.032407`, avg `0.006734`, median `0.010315`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.6`, primary_mae `0.034825`, avg `0.014071`, median `0.008916`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.7`, primary_mae `0.037544`, avg `0.02009`, median `0.008659`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.55`, primary_mae `0.07378`, avg `0.019633`, median `0.016179`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.55`, primary_mae `0.076236`, avg `0.084524`, median `0.054706`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.024046, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.026821, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.025284, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.046379, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.066367, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022419, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026137, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.024046, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025405, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028881, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.026821, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2125, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026406, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036962, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.025284, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034044, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.063572, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.046379, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065386, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.094521, 'direction_hit_rate': 0.725}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.066367, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.030006`, avg `0.004061`, median `0.010315`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.028293`, avg `0.013582`, median `0.004783`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.75`, primary_mae `0.030044`, avg `0.023553`, median `0.002799`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.086197`, avg `0.037298`, median `0.032046`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.104334`, avg `0.08833`, median `0.059641`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.029155`, avg `0.005542`, median `0.010315`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.625`, primary_mae `0.027431`, avg `0.01389`, median `0.008916`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.75`, primary_mae `0.028252`, avg `0.018559`, median `0.008659`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.5625`, primary_mae `0.068846`, avg `0.018023`, median `0.016179`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.5625`, primary_mae `0.078078`, avg `0.08466`, median `0.054706`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.025535`, avg `-0.00135`, median `-0.00313`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.022122`, avg `-0.008507`, median `-0.007072`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.020818`, avg `0.001966`, median `-0.001481`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.043792`, avg `0.01191`, median `-0.0039`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.077265`, avg `0.034284`, median `0.054701`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.026137`, avg `0.001871`, median `0.001684`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4625`, primary_mae `0.028822`, avg `0.005122`, median `0.002949`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.028349`, avg `0.011755`, median `0.005498`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.053229`, avg `0.008501`, median `0.005051`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.475`, primary_mae `0.068834`, avg `0.05066`, median `0.061523`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.026137`, avg `0.001871`, median `0.001684`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4625`, primary_mae `0.028822`, avg `0.005122`, median `0.002949`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.028349`, avg `0.011755`, median `0.005498`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.053229`, avg `0.008501`, median `0.005051`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.475`, primary_mae `0.068834`, avg `0.05066`, median `0.061523`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.032407`, avg `0.006734`, median `0.010315`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.6`, primary_mae `0.034825`, avg `0.014071`, median `0.008916`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.7`, primary_mae `0.037544`, avg `0.02009`, median `0.008659`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.55`, primary_mae `0.07378`, avg `0.019633`, median `0.016179`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.55`, primary_mae `0.076236`, avg `0.084524`, median `0.054706`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.45`, primary_mae `0.024046`, avg `0.000249`, median `-0.00118`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4167`, primary_mae `0.026821`, avg `0.002139`, median `0.001655`
- 10d: sample `60`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.025284`, avg `0.008977`, median `0.005438`
- 20d: sample `60`, primary_hit `0.5`, primary_closer `0.3167`, primary_mae `0.046379`, avg `0.004791`, median `0.000359`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.45`, primary_mae `0.066367`, avg `0.039371`, median `0.061523`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.026137`, avg `0.001871`, median `0.001684`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4625`, primary_mae `0.028822`, avg `0.005122`, median `0.002949`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.028349`, avg `0.011755`, median `0.005498`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.053229`, avg `0.008501`, median `0.005051`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.475`, primary_mae `0.068834`, avg `0.05066`, median `0.061523`

### flow_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.032407`, avg `0.006734`, median `0.010315`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.6`, primary_mae `0.034825`, avg `0.014071`, median `0.008916`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.7`, primary_mae `0.037544`, avg `0.02009`, median `0.008659`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.55`, primary_mae `0.07378`, avg `0.019633`, median `0.016179`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.55`, primary_mae `0.076236`, avg `0.084524`, median `0.054706`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.026137`, avg `0.001871`, median `0.001684`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4625`, primary_mae `0.028822`, avg `0.005122`, median `0.002949`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.028349`, avg `0.011755`, median `0.005498`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.053229`, avg `0.008501`, median `0.005051`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.475`, primary_mae `0.068834`, avg `0.05066`, median `0.061523`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
