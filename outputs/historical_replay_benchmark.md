# Historical Replay Benchmark

Generated at: `2026-10-29T07:11:01.715052+00:00`
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
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.015428`
- secondary_mean_absolute_error: `0.013918`
- primary_error_advantage: `-0.00151`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.022287`
- secondary_mean_absolute_error: `0.019141`
- primary_error_advantage: `-0.003146`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.7`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.028015`
- secondary_mean_absolute_error: `0.022735`
- primary_error_advantage: `-0.00528`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.042493`
- secondary_mean_absolute_error: `0.029789`
- primary_error_advantage: `-0.012704`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3167`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.068325`
- secondary_mean_absolute_error: `0.056915`
- primary_error_advantage: `-0.01141`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.014288`, as_primary `0`, as_primary_hit `None`, avg `0.003702`, median `0.00448`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.02014`, as_primary `0`, as_primary_hit `None`, avg `0.004878`, median `0.007532`
- 10d: sample `80`, direction_hit `0.725`, path_mae `0.024874`, as_primary `0`, as_primary_hit `None`, avg `0.011981`, median `0.011387`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.032705`, as_primary `0`, as_primary_hit `None`, avg `0.018295`, median `0.025176`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.056752`, as_primary `0`, as_primary_hit `None`, avg `0.035066`, median `0.055033`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.015339`, as_primary `60`, as_primary_hit `0.6333`, avg `0.003702`, median `0.00448`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.022329`, as_primary `60`, as_primary_hit `0.6167`, avg `0.004878`, median `0.007532`
- 10d: sample `80`, direction_hit `0.725`, path_mae `0.031342`, as_primary `60`, as_primary_hit `0.7833`, avg `0.011981`, median `0.011387`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.045833`, as_primary `60`, as_primary_hit `0.75`, avg `0.018295`, median `0.025176`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.059881`, as_primary `60`, as_primary_hit `0.7167`, avg `0.035066`, median `0.055033`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.015697`, as_primary `20`, as_primary_hit `0.55`, avg `0.003702`, median `0.00448`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.021725`, as_primary `20`, as_primary_hit `0.45`, avg `0.004878`, median `0.007532`
- 10d: sample `80`, direction_hit `0.275`, path_mae `0.032837`, as_primary `20`, as_primary_hit `0.55`, avg `0.011981`, median `0.011387`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.053057`, as_primary `20`, as_primary_hit `0.6`, avg `0.018295`, median `0.025176`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.087556`, as_primary `20`, as_primary_hit `0.75`, avg `0.035066`, median `0.055033`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013918`, as_primary `0`, as_primary_hit `None`, avg `0.003702`, median `0.00448`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.019141`, as_primary `0`, as_primary_hit `None`, avg `0.004878`, median `0.007532`
- 10d: sample `80`, direction_hit `0.725`, path_mae `0.022735`, as_primary `0`, as_primary_hit `None`, avg `0.011981`, median `0.011387`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.029789`, as_primary `0`, as_primary_hit `None`, avg `0.018295`, median `0.025176`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.056915`, as_primary `0`, as_primary_hit `None`, avg `0.035066`, median `0.055033`

## Edge Status Performance

### STRONG_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.014765`, avg `0.004511`, median `0.004727`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.4167`, primary_mae `0.022279`, avg `0.007134`, median `0.008725`
- 10d: sample `60`, primary_hit `0.7833`, primary_closer `0.3667`, primary_mae `0.02813`, avg `0.015998`, median `0.019584`
- 20d: sample `60`, primary_hit `0.75`, primary_closer `0.3167`, primary_mae `0.040747`, avg `0.02093`, median `0.028445`
- 60d: sample `60`, primary_hit `0.7167`, primary_closer `0.5`, primary_mae `0.057286`, avg `0.031908`, median `0.055172`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.017418`, avg `0.001275`, median `0.003757`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.02231`, avg `-0.001891`, median `-0.006476`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.027671`, avg `-6.9e-05`, median `0.003986`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.047729`, avg `0.010388`, median `0.002175`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.101443`, avg `0.044542`, median `0.055033`

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
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.017418`, avg `0.001275`, median `0.003757`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.02231`, avg `-0.001891`, median `-0.006476`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.027671`, avg `-6.9e-05`, median `0.003986`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.047729`, avg `0.010388`, median `0.002175`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.101443`, avg `0.044542`, median `0.055033`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.014765`, avg `0.004511`, median `0.004727`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.4167`, primary_mae `0.022279`, avg `0.007134`, median `0.008725`
- 10d: sample `60`, primary_hit `0.7833`, primary_closer `0.3667`, primary_mae `0.02813`, avg `0.015998`, median `0.019584`
- 20d: sample `60`, primary_hit `0.75`, primary_closer `0.3167`, primary_mae `0.040747`, avg `0.02093`, median `0.028445`
- 60d: sample `60`, primary_hit `0.7167`, primary_closer `0.5`, primary_mae `0.057286`, avg `0.031908`, median `0.055172`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.014765, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.022279, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.027671, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.040747, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7167, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.057286, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013918, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015697, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.014765, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019141, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022329, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.022279, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022735, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032837, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.027671, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029789, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053057, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.040747, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056752, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.087556, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7167, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.057286, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.024861`, avg `0.003864`, median `0.002901`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.02884`, avg `0.008008`, median `0.00228`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.034548`, avg `0.019334`, median `0.022448`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.038478`, avg `0.033152`, median `0.02973`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.030361`, avg `0.061844`, median `0.070816`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.021811`, avg `0.006565`, median `0.002901`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.028011`, avg `0.007852`, median `0.010356`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.038701`, avg `0.016721`, median `0.022448`
- 20d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.040054`, avg `0.031534`, median `0.028445`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.5625`, primary_mae `0.037992`, avg `0.054584`, median `0.070816`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.019437`, avg `-0.002899`, median `-0.009133`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.023537`, avg `-0.003945`, median `-0.009834`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.027887`, avg `-0.003641`, median `-0.002529`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.048021`, avg `0.010117`, median `0.002175`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.095427`, avg `0.041293`, median `0.041889`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4625`, primary_mae `0.015428`, avg `0.003702`, median `0.00448`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.022287`, avg `0.004878`, median `0.007532`
- 10d: sample `80`, primary_hit `0.7`, primary_closer `0.3875`, primary_mae `0.028015`, avg `0.011981`, median `0.011387`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.3375`, primary_mae `0.042493`, avg `0.018295`, median `0.025176`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.068325`, avg `0.035066`, median `0.055033`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4625`, primary_mae `0.015428`, avg `0.003702`, median `0.00448`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.022287`, avg `0.004878`, median `0.007532`
- 10d: sample `80`, primary_hit `0.7`, primary_closer `0.3875`, primary_mae `0.028015`, avg `0.011981`, median `0.011387`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.3375`, primary_mae `0.042493`, avg `0.018295`, median `0.025176`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.068325`, avg `0.035066`, median `0.055033`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.014765`, avg `0.004511`, median `0.004727`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.4167`, primary_mae `0.022279`, avg `0.007134`, median `0.008725`
- 10d: sample `60`, primary_hit `0.7833`, primary_closer `0.3667`, primary_mae `0.02813`, avg `0.015998`, median `0.019584`
- 20d: sample `60`, primary_hit `0.75`, primary_closer `0.3167`, primary_mae `0.040747`, avg `0.02093`, median `0.028445`
- 60d: sample `60`, primary_hit `0.7167`, primary_closer `0.5`, primary_mae `0.057286`, avg `0.031908`, median `0.055172`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.017418`, avg `0.001275`, median `0.003757`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.02231`, avg `-0.001891`, median `-0.006476`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.027671`, avg `-6.9e-05`, median `0.003986`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.047729`, avg `0.010388`, median `0.002175`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.101443`, avg `0.044542`, median `0.055033`

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
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.015515`, avg `0.002195`, median `0.004375`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.0203`, avg `0.004414`, median `0.009377`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.425`, primary_mae `0.026719`, avg `0.0117`, median `0.009787`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.04905`, avg `0.012281`, median `0.017223`
- 60d: sample `40`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.087912`, avg `0.037063`, median `0.055914`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4625`, primary_mae `0.015428`, avg `0.003702`, median `0.00448`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.022287`, avg `0.004878`, median `0.007532`
- 10d: sample `80`, primary_hit `0.7`, primary_closer `0.3875`, primary_mae `0.028015`, avg `0.011981`, median `0.011387`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.3375`, primary_mae `0.042493`, avg `0.018295`, median `0.025176`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.068325`, avg `0.035066`, median `0.055033`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
