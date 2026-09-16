# Historical Replay Benchmark

Generated at: `2026-09-16T16:59:36.827404+00:00`
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
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.019265`
- secondary_mean_absolute_error: `0.014218`
- primary_error_advantage: `-0.005047`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.023478`
- secondary_mean_absolute_error: `0.01785`
- primary_error_advantage: `-0.005628`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.030106`
- secondary_mean_absolute_error: `0.023474`
- primary_error_advantage: `-0.006632`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.058579`
- secondary_mean_absolute_error: `0.03348`
- primary_error_advantage: `-0.025099`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.225`
- secondary_hit_rate: `0.775`
- primary_vs_secondary_accuracy_spread: `-0.55`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.102713`
- secondary_mean_absolute_error: `0.062313`
- primary_error_advantage: `-0.0404`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.014772`, as_primary `0`, as_primary_hit `None`, avg `0.000826`, median `0.001274`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.018299`, as_primary `0`, as_primary_hit `None`, avg `-0.001858`, median `0.000995`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.025062`, as_primary `0`, as_primary_hit `None`, avg `-0.000549`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.035661`, as_primary `0`, as_primary_hit `None`, avg `0.012298`, median `0.012243`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.069484`, as_primary `0`, as_primary_hit `None`, avg `0.042236`, median `0.055948`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.017192`, as_primary `0`, as_primary_hit `None`, avg `0.000826`, median `0.001274`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.02175`, as_primary `0`, as_primary_hit `None`, avg `-0.001858`, median `0.000995`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.035604`, as_primary `0`, as_primary_hit `None`, avg `-0.000549`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.057253`, as_primary `0`, as_primary_hit `None`, avg `0.012298`, median `0.012243`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.074456`, as_primary `0`, as_primary_hit `None`, avg `0.042236`, median `0.055948`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.019265`, as_primary `80`, as_primary_hit `0.55`, avg `0.000826`, median `0.001274`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.023478`, as_primary `80`, as_primary_hit `0.5375`, avg `-0.001858`, median `0.000995`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.030106`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.000549`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.058579`, as_primary `80`, as_primary_hit `0.6125`, avg `0.012298`, median `0.012243`
- 60d: sample `80`, direction_hit `0.225`, path_mae `0.102713`, as_primary `80`, as_primary_hit `0.775`, avg `0.042236`, median `0.055948`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.014218`, as_primary `0`, as_primary_hit `None`, avg `0.000826`, median `0.001274`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.01785`, as_primary `0`, as_primary_hit `None`, avg `-0.001858`, median `0.000995`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.023474`, as_primary `0`, as_primary_hit `None`, avg `-0.000549`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.03348`, as_primary `0`, as_primary_hit `None`, avg `0.012298`, median `0.012243`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.062313`, as_primary `0`, as_primary_hit `None`, avg `0.042236`, median `0.055948`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.019265`, avg `0.000826`, median `0.001274`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.325`, primary_mae `0.023478`, avg `-0.001858`, median `0.000995`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.030106`, avg `-0.000549`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.2625`, primary_mae `0.058579`, avg `0.012298`, median `0.012243`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.102713`, avg `0.042236`, median `0.055948`

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
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.3833`, primary_mae `0.016939`, avg `-0.001973`, median `-0.00165`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.35`, primary_mae `0.021263`, avg `-0.006691`, median `-0.00331`
- 10d: sample `60`, primary_hit `0.65`, primary_closer `0.3833`, primary_mae `0.02476`, avg `-0.007677`, median `-0.009483`
- 20d: sample `60`, primary_hit `0.4667`, primary_closer `0.2167`, primary_mae `0.062438`, avg `0.003108`, median `0.004773`
- 60d: sample `60`, primary_hit `0.2833`, primary_closer `0.2833`, primary_mae `0.11746`, avg `0.028477`, median `0.048084`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.02624`, avg `0.009223`, median `0.011608`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.030123`, avg `0.01264`, median `0.015279`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.046145`, avg `0.020834`, median `0.021201`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.047001`, avg `0.039871`, median `0.033704`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.5`, primary_mae `0.058472`, avg `0.083513`, median `0.079814`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.016939, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.021263, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.02476, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.047001, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.058472, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014218, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019265, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.016939, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01785, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023478, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.021263, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023474, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035604, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.02476, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03348, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058579, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.047001, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.225, 'secondary_hit_rate': 0.775, 'primary_vs_secondary_accuracy_spread': -0.55, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062313, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.102713, 'direction_hit_rate': 0.225}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.058472, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.017302`, avg `-0.005043`, median `-0.005521`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.017355`, avg `-0.008697`, median `-0.008736`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.014902`, avg `-0.003343`, median `-0.008236`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.057339`, avg `0.023422`, median `0.021062`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.111036`, avg `0.051354`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.019403`, avg `-0.005762`, median `-0.005521`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.018388`, avg `-0.010953`, median `-0.012995`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.018546`, avg `-0.0009`, median `-0.005954`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.058539`, avg `0.024622`, median `0.030181`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.112652`, avg `0.05297`, median `0.072376`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.023362`, avg `0.005578`, median `0.008408`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.03298`, avg `0.003843`, median `0.005514`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.03683`, avg `-0.014411`, median `-0.021871`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.1875`, primary_mae `0.072161`, avg `-0.012272`, median `-0.010228`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.183491`, avg `0.016986`, median `0.038915`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.019265`, avg `0.000826`, median `0.001274`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.325`, primary_mae `0.023478`, avg `-0.001858`, median `0.000995`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.030106`, avg `-0.000549`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.2625`, primary_mae `0.058579`, avg `0.012298`, median `0.012243`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.102713`, avg `0.042236`, median `0.055948`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.019265`, avg `0.000826`, median `0.001274`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.325`, primary_mae `0.023478`, avg `-0.001858`, median `0.000995`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.030106`, avg `-0.000549`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.2625`, primary_mae `0.058579`, avg `0.012298`, median `0.012243`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.102713`, avg `0.042236`, median `0.055948`

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
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.019265`, avg `0.000826`, median `0.001274`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.325`, primary_mae `0.023478`, avg `-0.001858`, median `0.000995`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.030106`, avg `-0.000549`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.2625`, primary_mae `0.058579`, avg `0.012298`, median `0.012243`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.102713`, avg `0.042236`, median `0.055948`

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
