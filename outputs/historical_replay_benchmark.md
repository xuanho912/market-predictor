# Historical Replay Benchmark

Generated at: `2026-06-25T23:56:31.721701+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
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
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.016394`
- secondary_mean_absolute_error: `0.016682`
- primary_error_advantage: `0.000288`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.020033`
- secondary_mean_absolute_error: `0.019413`
- primary_error_advantage: `-0.00062`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.031248`
- secondary_mean_absolute_error: `0.025543`
- primary_error_advantage: `-0.005705`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3333`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.050867`
- secondary_mean_absolute_error: `0.034041`
- primary_error_advantage: `-0.016826`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.7125`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.063469`
- secondary_mean_absolute_error: `0.046891`
- primary_error_advantage: `-0.016578`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.2667`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.015445`, as_primary `0`, as_primary_hit `None`, avg `0.001868`, median `-0.000961`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.018368`, as_primary `0`, as_primary_hit `None`, avg `-0.002222`, median `-0.005851`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.023702`, as_primary `0`, as_primary_hit `None`, avg `0.000108`, median `-0.001702`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.030264`, as_primary `0`, as_primary_hit `None`, avg `0.012661`, median `0.019288`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.045986`, as_primary `0`, as_primary_hit `None`, avg `0.0453`, median `0.063468`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.016715`, as_primary `60`, as_primary_hit `0.5333`, avg `0.001868`, median `-0.000961`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.020179`, as_primary `60`, as_primary_hit `0.45`, avg `-0.002222`, median `-0.005851`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.031325`, as_primary `60`, as_primary_hit `0.4667`, avg `0.000108`, median `-0.001702`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.043341`, as_primary `60`, as_primary_hit `0.7667`, avg `0.012661`, median `0.019288`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.062979`, as_primary `60`, as_primary_hit `0.8167`, avg `0.0453`, median `0.063468`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.016516`, as_primary `20`, as_primary_hit `0.35`, avg `0.001868`, median `-0.000961`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.019559`, as_primary `20`, as_primary_hit `0.35`, avg `-0.002222`, median `-0.005851`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.029406`, as_primary `20`, as_primary_hit `0.45`, avg `0.000108`, median `-0.001702`
- 20d: sample `80`, direction_hit `0.2625`, path_mae `0.060279`, as_primary `20`, as_primary_hit `0.65`, avg `0.012661`, median `0.019288`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.066322`, as_primary `20`, as_primary_hit `0.6`, avg `0.0453`, median `0.063468`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.015166`, as_primary `0`, as_primary_hit `None`, avg `0.001868`, median `-0.000961`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.017821`, as_primary `0`, as_primary_hit `None`, avg `-0.002222`, median `-0.005851`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.022497`, as_primary `0`, as_primary_hit `None`, avg `0.000108`, median `-0.001702`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.030354`, as_primary `0`, as_primary_hit `None`, avg `0.012661`, median `0.019288`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.048021`, as_primary `0`, as_primary_hit `None`, avg `0.0453`, median `0.063468`

## Edge Status Performance

### STRONG_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.4833`, primary_mae `0.017227`, avg `0.003585`, median `0.001998`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.020804`, avg `-0.000663`, median `-0.003772`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.3333`, primary_mae `0.030421`, avg `0.002651`, median `-0.001443`
- 20d: sample `60`, primary_hit `0.7667`, primary_closer `0.4`, primary_mae `0.045378`, avg `0.018674`, median `0.027925`
- 60d: sample `60`, primary_hit `0.8167`, primary_closer `0.2667`, primary_mae `0.067165`, avg `0.05822`, median `0.072046`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.013896`, avg `-0.003283`, median `-0.004669`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.017722`, avg `-0.006899`, median `-0.011189`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.03373`, avg `-0.00752`, median `-0.009328`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.067336`, avg `-0.005379`, median `0.012119`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.052382`, avg `0.006539`, median `0.034354`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.013896`, avg `-0.003283`, median `-0.004669`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.017722`, avg `-0.006899`, median `-0.011189`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.03373`, avg `-0.00752`, median `-0.009328`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.067336`, avg `-0.005379`, median `0.012119`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.052382`, avg `0.006539`, median `0.034354`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.4833`, primary_mae `0.017227`, avg `0.003585`, median `0.001998`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.020804`, avg `-0.000663`, median `-0.003772`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.3333`, primary_mae `0.030421`, avg `0.002651`, median `-0.001443`
- 20d: sample `60`, primary_hit `0.7667`, primary_closer `0.4`, primary_mae `0.045378`, avg `0.018674`, median `0.027925`
- 60d: sample `60`, primary_hit `0.8167`, primary_closer `0.2667`, primary_mae `0.067165`, avg `0.05822`, median `0.072046`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.013896, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.017722, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.3333, 'primary_mean_absolute_error': 0.030421, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7667, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.045378, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.052382, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015166, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016715, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.013896, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017821, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020179, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.017722, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022497, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031325, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.3333, 'primary_mean_absolute_error': 0.030421, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030264, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060279, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7667, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.045378, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7125, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045986, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066322, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.052382, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.020843`, avg `-0.000748`, median `-0.001284`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.014743`, avg `-0.010783`, median `-0.010753`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.0139`, avg `0.004627`, median `0.002156`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.019377`, avg `0.024681`, median `0.028709`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.625`, primary_mae `0.022553`, avg `0.082149`, median `0.093637`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.018166`, avg `0.002456`, median `0.000401`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.016255`, avg `-0.00731`, median `-0.007674`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.017184`, avg `0.003929`, median `-0.001443`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.5625`, primary_mae `0.023993`, avg `0.023842`, median `0.026537`
- 60d: sample `16`, primary_hit `1.0`, primary_closer `0.4375`, primary_mae `0.019497`, avg `0.075195`, median `0.074488`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.01427`, avg `-0.003535`, median `-0.004669`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.018582`, avg `-0.00625`, median `-0.011189`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.032789`, avg `-0.008952`, median `-0.009328`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.065045`, avg `-0.005384`, median `0.009366`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.049833`, avg `0.009257`, median `0.034354`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.016394`, avg `0.001868`, median `-0.000961`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.020033`, avg `-0.002222`, median `-0.005851`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.031248`, avg `0.000108`, median `-0.001702`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.3625`, primary_mae `0.050867`, avg `0.012661`, median `0.019288`
- 60d: sample `80`, primary_hit `0.7125`, primary_closer `0.3`, primary_mae `0.063469`, avg `0.0453`, median `0.063468`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.016394`, avg `0.001868`, median `-0.000961`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.020033`, avg `-0.002222`, median `-0.005851`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.031248`, avg `0.000108`, median `-0.001702`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.3625`, primary_mae `0.050867`, avg `0.012661`, median `0.019288`
- 60d: sample `80`, primary_hit `0.7125`, primary_closer `0.3`, primary_mae `0.063469`, avg `0.0453`, median `0.063468`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.01765`, avg `0.002461`, median `-0.000668`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.0187`, avg `-0.00079`, median `-0.001187`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.25`, primary_mae `0.03948`, avg `0.001691`, median `-0.004104`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.069809`, avg `0.006173`, median `0.016362`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.2`, primary_mae `0.101667`, avg `0.057092`, median `0.073914`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.015976`, avg `0.00167`, median `-0.000961`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.5`, primary_mae `0.020478`, avg `-0.002699`, median `-0.006423`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.4167`, primary_mae `0.028504`, avg `-0.000419`, median `-0.001443`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.3833`, primary_mae `0.044553`, avg `0.014823`, median `0.020408`
- 60d: sample `60`, primary_hit `0.6833`, primary_closer `0.3333`, primary_mae `0.050736`, avg `0.041369`, median `0.058512`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.016394`, avg `0.001868`, median `-0.000961`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.020033`, avg `-0.002222`, median `-0.005851`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.031248`, avg `0.000108`, median `-0.001702`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.3625`, primary_mae `0.050867`, avg `0.012661`, median `0.019288`
- 60d: sample `80`, primary_hit `0.7125`, primary_closer `0.3`, primary_mae `0.063469`, avg `0.0453`, median `0.063468`

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
