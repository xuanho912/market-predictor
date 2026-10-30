# Historical Replay Benchmark

Generated at: `2026-10-30T07:13:50.941406+00:00`
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
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.017354`
- secondary_mean_absolute_error: `0.01578`
- primary_error_advantage: `-0.001574`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.024365`
- secondary_mean_absolute_error: `0.020469`
- primary_error_advantage: `-0.003896`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.031471`
- secondary_mean_absolute_error: `0.029735`
- primary_error_advantage: `-0.001736`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.044477`
- secondary_mean_absolute_error: `0.034946`
- primary_error_advantage: `-0.009531`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.04768`
- secondary_mean_absolute_error: `0.046876`
- primary_error_advantage: `-0.000804`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.016929`, as_primary `0`, as_primary_hit `None`, avg `0.003897`, median `0.005557`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.022096`, as_primary `0`, as_primary_hit `None`, avg `0.005386`, median `0.006294`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.028078`, as_primary `0`, as_primary_hit `None`, avg `0.013168`, median `0.011387`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.030885`, as_primary `0`, as_primary_hit `None`, avg `0.023171`, median `0.028445`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.047235`, as_primary `0`, as_primary_hit `None`, avg `0.045772`, median `0.054182`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.018557`, as_primary `60`, as_primary_hit `0.65`, avg `0.003897`, median `0.005557`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.02445`, as_primary `60`, as_primary_hit `0.5833`, avg `0.005386`, median `0.006294`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.035231`, as_primary `60`, as_primary_hit `0.6667`, avg `0.013168`, median `0.011387`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.044188`, as_primary `60`, as_primary_hit `0.7667`, avg `0.023171`, median `0.028445`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.049442`, as_primary `60`, as_primary_hit `0.7333`, avg `0.045772`, median `0.054182`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.018233`, as_primary `20`, as_primary_hit `0.5`, avg `0.003897`, median `0.005557`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.022148`, as_primary `20`, as_primary_hit `0.55`, avg `0.005386`, median `0.006294`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.039592`, as_primary `20`, as_primary_hit `0.6`, avg `0.013168`, median `0.011387`
- 20d: sample `80`, direction_hit `0.2625`, path_mae `0.053279`, as_primary `20`, as_primary_hit `0.65`, avg `0.023171`, median `0.028445`
- 60d: sample `80`, direction_hit `0.225`, path_mae `0.059243`, as_primary `20`, as_primary_hit `0.9`, avg `0.045772`, median `0.054182`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.015885`, as_primary `0`, as_primary_hit `None`, avg `0.003897`, median `0.005557`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.020432`, as_primary `0`, as_primary_hit `None`, avg `0.005386`, median `0.006294`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.026365`, as_primary `0`, as_primary_hit `None`, avg `0.013168`, median `0.011387`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.029829`, as_primary `0`, as_primary_hit `None`, avg `0.023171`, median `0.028445`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.045771`, as_primary `0`, as_primary_hit `None`, avg `0.045772`, median `0.054182`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.017354`, avg `0.003897`, median `0.005557`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.024365`, avg `0.005386`, median `0.006294`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.031471`, avg `0.013168`, median `0.011387`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.375`, primary_mae `0.044477`, avg `0.023171`, median `0.028445`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.04768`, avg `0.045772`, median `0.054182`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.019514`, avg `0.006051`, median `0.005236`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.032207`, avg `0.005312`, median `-0.000258`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.040245`, avg `0.014335`, median `0.015525`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.043879`, avg `0.028204`, median `0.028445`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.55`, primary_mae `0.042295`, avg `0.048299`, median `0.066906`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.023094`, avg `-3.5e-05`, median `-0.001791`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.024683`, avg `-0.000596`, median `0.005385`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.02758`, avg `0.01282`, median `0.008601`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.057043`, avg `0.019802`, median `0.015793`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.55`, primary_mae `0.052339`, avg `0.066658`, median `0.054679`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.013403`, avg `0.004785`, median `0.006323`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.020284`, avg `0.008414`, median `0.008893`
- 10d: sample `40`, primary_hit `0.7`, primary_closer `0.575`, primary_mae `0.02903`, avg `0.012759`, median `0.013221`
- 20d: sample `40`, primary_hit `0.75`, primary_closer `0.425`, primary_mae `0.038493`, avg `0.02234`, median `0.0272`
- 60d: sample `40`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.048043`, avg `0.034066`, median `0.046908`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013403, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.020284, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.02758, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.038493, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.042295, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015885, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018557, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013403, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020432, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02445, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.020284, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026365, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039592, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.02758, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029829, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053279, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.038493, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045771, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059243, 'direction_hit_rate': 0.225}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.042295, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.022824`, avg `0.003864`, median `0.002901`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.030061`, avg `0.008008`, median `0.00228`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.033772`, avg `0.019334`, median `0.022448`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.039098`, avg `0.033152`, median `0.02973`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.030523`, avg `0.061844`, median `0.070816`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.020322`, avg `0.005647`, median `0.005236`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.031638`, avg `0.005952`, median `0.003837`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.034193`, avg `0.020844`, median `0.016941`
- 20d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.036041`, avg `0.036168`, median `0.029911`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.5625`, primary_mae `0.037066`, avg `0.056034`, median `0.070816`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.026506`, avg `-0.000395`, median `-0.007516`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.026825`, avg `-0.000255`, median `0.00793`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.029215`, avg `0.01557`, median `0.009373`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.061754`, avg `0.026603`, median `0.035478`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.5625`, primary_mae `0.045931`, avg `0.066784`, median `0.052482`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.017354`, avg `0.003897`, median `0.005557`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.024365`, avg `0.005386`, median `0.006294`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.031471`, avg `0.013168`, median `0.011387`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.375`, primary_mae `0.044477`, avg `0.023171`, median `0.028445`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.04768`, avg `0.045772`, median `0.054182`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.017354`, avg `0.003897`, median `0.005557`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.024365`, avg `0.005386`, median `0.006294`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.031471`, avg `0.013168`, median `0.011387`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.375`, primary_mae `0.044477`, avg `0.023171`, median `0.028445`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.04768`, avg `0.045772`, median `0.054182`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.65`, primary_closer `0.3667`, primary_mae `0.01544`, avg `0.005207`, median `0.006251`
- 5d: sample `60`, primary_hit `0.5833`, primary_closer `0.3667`, primary_mae `0.024258`, avg `0.00738`, median `0.006642`
- 10d: sample `60`, primary_hit `0.6667`, primary_closer `0.4833`, primary_mae `0.032768`, avg `0.013284`, median `0.013595`
- 20d: sample `60`, primary_hit `0.7667`, primary_closer `0.3833`, primary_mae `0.040289`, avg `0.024294`, median `0.028445`
- 60d: sample `60`, primary_hit `0.7333`, primary_closer `0.4833`, primary_mae `0.046127`, avg `0.03881`, median `0.053577`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.023094`, avg `-3.5e-05`, median `-0.001791`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.024683`, avg `-0.000596`, median `0.005385`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.02758`, avg `0.01282`, median `0.008601`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.057043`, avg `0.019802`, median `0.015793`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.55`, primary_mae `0.052339`, avg `0.066658`, median `0.054679`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.017354`, avg `0.003897`, median `0.005557`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.024365`, avg `0.005386`, median `0.006294`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.031471`, avg `0.013168`, median `0.011387`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.375`, primary_mae `0.044477`, avg `0.023171`, median `0.028445`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.04768`, avg `0.045772`, median `0.054182`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.017354`, avg `0.003897`, median `0.005557`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.024365`, avg `0.005386`, median `0.006294`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.031471`, avg `0.013168`, median `0.011387`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.375`, primary_mae `0.044477`, avg `0.023171`, median `0.028445`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.04768`, avg `0.045772`, median `0.054182`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.017354`, avg `0.003897`, median `0.005557`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.024365`, avg `0.005386`, median `0.006294`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.031471`, avg `0.013168`, median `0.011387`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.375`, primary_mae `0.044477`, avg `0.023171`, median `0.028445`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.04768`, avg `0.045772`, median `0.054182`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
