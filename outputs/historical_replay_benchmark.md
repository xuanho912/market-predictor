# Historical Replay Benchmark

Generated at: `2026-09-24T17:17:16.125022+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
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
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.020513`
- secondary_mean_absolute_error: `0.016778`
- primary_error_advantage: `-0.003735`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.026709`
- secondary_mean_absolute_error: `0.020858`
- primary_error_advantage: `-0.005851`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.037547`
- secondary_mean_absolute_error: `0.029013`
- primary_error_advantage: `-0.008534`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.075168`
- secondary_mean_absolute_error: `0.049574`
- primary_error_advantage: `-0.025594`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.095244`
- secondary_mean_absolute_error: `0.064113`
- primary_error_advantage: `-0.031131`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016518`, as_primary `0`, as_primary_hit `None`, avg `-0.006435`, median `-0.004602`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.019277`, as_primary `0`, as_primary_hit `None`, avg `-0.010557`, median `-0.010564`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.025912`, as_primary `0`, as_primary_hit `None`, avg `-0.009388`, median `-0.0067`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.041214`, as_primary `0`, as_primary_hit `None`, avg `0.006009`, median `0.016024`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.055861`, as_primary `0`, as_primary_hit `None`, avg `0.041386`, median `0.050314`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016942`, as_primary `0`, as_primary_hit `None`, avg `-0.006435`, median `-0.004602`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.020768`, as_primary `0`, as_primary_hit `None`, avg `-0.010557`, median `-0.010564`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.031326`, as_primary `0`, as_primary_hit `None`, avg `-0.009388`, median `-0.0067`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.060225`, as_primary `0`, as_primary_hit `None`, avg `0.006009`, median `0.016024`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.062441`, as_primary `0`, as_primary_hit `None`, avg `0.041386`, median `0.050314`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.020513`, as_primary `80`, as_primary_hit `0.4`, avg `-0.006435`, median `-0.004602`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.026709`, as_primary `80`, as_primary_hit `0.425`, avg `-0.010557`, median `-0.010564`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.037547`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.009388`, median `-0.0067`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.075168`, as_primary `80`, as_primary_hit `0.625`, avg `0.006009`, median `0.016024`
- 60d: sample `80`, direction_hit `0.1875`, path_mae `0.095244`, as_primary `80`, as_primary_hit `0.8125`, avg `0.041386`, median `0.050314`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016081`, as_primary `0`, as_primary_hit `None`, avg `-0.006435`, median `-0.004602`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.019074`, as_primary `0`, as_primary_hit `None`, avg `-0.010557`, median `-0.010564`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.026367`, as_primary `0`, as_primary_hit `None`, avg `-0.009388`, median `-0.0067`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.042105`, as_primary `0`, as_primary_hit `None`, avg `0.006009`, median `0.016024`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.056641`, as_primary `0`, as_primary_hit `None`, avg `0.041386`, median `0.050314`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.020513`, avg `-0.006435`, median `-0.004602`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4125`, primary_mae `0.026709`, avg `-0.010557`, median `-0.010564`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.037547`, avg `-0.009388`, median `-0.0067`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.075168`, avg `0.006009`, median `0.016024`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.095244`, avg `0.041386`, median `0.050314`

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
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4`, primary_mae `0.019415`, avg `-0.00515`, median `-0.003835`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.3833`, primary_mae `0.025517`, avg `-0.008174`, median `-0.006281`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.3667`, primary_mae `0.037523`, avg `-0.005303`, median `0.004061`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.3167`, primary_mae `0.07185`, avg `0.007653`, median `0.015571`
- 60d: sample `60`, primary_hit `0.1667`, primary_closer `0.25`, primary_mae `0.085127`, avg `0.04598`, median `0.055681`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.023808`, avg `-0.010292`, median `-0.014138`
- 5d: sample `20`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.030288`, avg `-0.017705`, median `-0.020235`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.4`, primary_mae `0.037621`, avg `-0.021642`, median `-0.015452`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.085125`, avg `0.00108`, median `0.018406`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.125595`, avg `0.027605`, median `0.041779`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.019415, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.025517, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.037523, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.07185, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1667, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.085127, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016081, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020513, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.019415, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019074, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026709, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.025517, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025912, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037547, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.037523, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041214, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075168, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.07185, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055861, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.095244, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1667, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.085127, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.024155`, avg `-0.009846`, median `-0.016078`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.034109`, avg `-0.013804`, median `-0.009546`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.042657`, avg `-0.014418`, median `-0.015452`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.103052`, avg `0.013426`, median `0.025462`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.151559`, avg `0.052254`, median `0.061567`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.022629`, avg `-0.011881`, median `-0.015475`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.031683`, avg `-0.016988`, median `-0.020235`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.040684`, avg `-0.018093`, median `-0.012632`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.089722`, avg `0.004637`, median `0.020913`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.126163`, avg `0.025016`, median `0.048285`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.027254`, avg `-0.01837`, median `-0.010701`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.03612`, avg `-0.015891`, median `-0.013338`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.048853`, avg `-0.006493`, median `-0.01146`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.088549`, avg `0.010815`, median `0.016851`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.114476`, avg `0.088308`, median `0.106082`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.020513`, avg `-0.006435`, median `-0.004602`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4125`, primary_mae `0.026709`, avg `-0.010557`, median `-0.010564`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.037547`, avg `-0.009388`, median `-0.0067`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.075168`, avg `0.006009`, median `0.016024`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.095244`, avg `0.041386`, median `0.050314`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.020513`, avg `-0.006435`, median `-0.004602`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4125`, primary_mae `0.026709`, avg `-0.010557`, median `-0.010564`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.037547`, avg `-0.009388`, median `-0.0067`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.075168`, avg `0.006009`, median `0.016024`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.095244`, avg `0.041386`, median `0.050314`

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
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.020513`, avg `-0.006435`, median `-0.004602`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4125`, primary_mae `0.026709`, avg `-0.010557`, median `-0.010564`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.037547`, avg `-0.009388`, median `-0.0067`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.075168`, avg `0.006009`, median `0.016024`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.095244`, avg `0.041386`, median `0.050314`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.020513`, avg `-0.006435`, median `-0.004602`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4125`, primary_mae `0.026709`, avg `-0.010557`, median `-0.010564`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.037547`, avg `-0.009388`, median `-0.0067`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.075168`, avg `0.006009`, median `0.016024`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.095244`, avg `0.041386`, median `0.050314`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.016888`, avg `-0.005245`, median `-0.003662`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.02244`, avg `-0.010742`, median `-0.004778`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.034786`, avg `-0.011225`, median `-0.0067`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.275`, primary_mae `0.081811`, avg `0.002143`, median `0.016024`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.097397`, avg `0.024232`, median `0.03292`

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
