# Historical Replay Benchmark

Generated at: `2026-09-15T06:13:15.614414+00:00`
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
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.022193`
- secondary_mean_absolute_error: `0.013572`
- primary_error_advantage: `-0.008621`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.02285`
- secondary_mean_absolute_error: `0.01599`
- primary_error_advantage: `-0.00686`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.031561`
- secondary_mean_absolute_error: `0.024335`
- primary_error_advantage: `-0.007226`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.068741`
- secondary_mean_absolute_error: `0.038044`
- primary_error_advantage: `-0.030697`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.116658`
- secondary_mean_absolute_error: `0.07185`
- primary_error_advantage: `-0.044808`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.013979`, as_primary `0`, as_primary_hit `None`, avg `0.001928`, median `0.005303`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.015855`, as_primary `0`, as_primary_hit `None`, avg `0.00023`, median `0.002338`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.027416`, as_primary `0`, as_primary_hit `None`, avg `-0.000843`, median `-0.00478`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.038137`, as_primary `0`, as_primary_hit `None`, avg `0.01372`, median `0.020147`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.07451`, as_primary `0`, as_primary_hit `None`, avg `0.039718`, median `0.06505`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.013652`, as_primary `0`, as_primary_hit `None`, avg `0.001928`, median `0.005303`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.019998`, as_primary `0`, as_primary_hit `None`, avg `0.00023`, median `0.002338`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.036558`, as_primary `0`, as_primary_hit `None`, avg `-0.000843`, median `-0.00478`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.053934`, as_primary `0`, as_primary_hit `None`, avg `0.01372`, median `0.020147`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.080352`, as_primary `0`, as_primary_hit `None`, avg `0.039718`, median `0.06505`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.022193`, as_primary `80`, as_primary_hit `0.6375`, avg `0.001928`, median `0.005303`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.02285`, as_primary `80`, as_primary_hit `0.5875`, avg `0.00023`, median `0.002338`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.031561`, as_primary `80`, as_primary_hit `0.45`, avg `-0.000843`, median `-0.00478`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.068741`, as_primary `80`, as_primary_hit `0.6375`, avg `0.01372`, median `0.020147`
- 60d: sample `80`, direction_hit `0.3`, path_mae `0.116658`, as_primary `80`, as_primary_hit `0.7`, avg `0.039718`, median `0.06505`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.013572`, as_primary `0`, as_primary_hit `None`, avg `0.001928`, median `0.005303`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.01599`, as_primary `0`, as_primary_hit `None`, avg `0.00023`, median `0.002338`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.024335`, as_primary `0`, as_primary_hit `None`, avg `-0.000843`, median `-0.00478`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.038044`, as_primary `0`, as_primary_hit `None`, avg `0.01372`, median `0.020147`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.07185`, as_primary `0`, as_primary_hit `None`, avg `0.039718`, median `0.06505`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.2625`, primary_mae `0.022193`, avg `0.001928`, median `0.005303`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.3125`, primary_mae `0.02285`, avg `0.00023`, median `0.002338`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.031561`, avg `-0.000843`, median `-0.00478`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.25`, primary_mae `0.068741`, avg `0.01372`, median `0.020147`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3125`, primary_mae `0.116658`, avg `0.039718`, median `0.06505`

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
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.25`, primary_mae `0.021796`, avg `0.000809`, median `0.001736`
- 5d: sample `60`, primary_hit `0.4333`, primary_closer `0.3167`, primary_mae `0.021969`, avg `-0.001716`, median `0.001763`
- 10d: sample `60`, primary_hit `0.6333`, primary_closer `0.3833`, primary_mae `0.02989`, avg `-0.006827`, median `-0.008973`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.2333`, primary_mae `0.074189`, avg `0.006756`, median `0.010694`
- 60d: sample `60`, primary_hit `0.35`, primary_closer `0.3333`, primary_mae `0.127772`, avg `0.030068`, median `0.060495`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.023382`, avg `0.005287`, median `0.010341`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.025491`, avg `0.00607`, median `0.00764`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.036575`, avg `0.017107`, median `0.017018`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.052395`, avg `0.034611`, median `0.044001`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.083318`, avg `0.068667`, median `0.082481`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.021796, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.021969, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.02989, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.052395, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.083318, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013572, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022193, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.021796, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015855, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02285, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.021969, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024335, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036558, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.02989, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038044, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.068741, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.052395, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07185, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.116658, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.083318, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.03279`, avg `0.004786`, median `0.009324`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.031997`, avg `-0.000186`, median `0.002458`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.021151`, avg `-0.001987`, median `-0.00362`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.068144`, avg `0.041866`, median `0.047524`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.132626`, avg `0.080057`, median `0.103033`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.028205`, avg `-0.002369`, median `0.003063`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.026762`, avg `-0.010053`, median `0.000647`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.018369`, avg `-0.005941`, median `-0.006514`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.051318`, avg `0.021411`, median `0.024617`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.093362`, avg `0.039786`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.016363`, avg `0.002828`, median `0.001417`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.012376`, avg `-0.001789`, median `0.002038`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.02234`, avg `-0.007983`, median `-0.01363`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.1875`, primary_mae `0.077722`, avg `-0.000233`, median `0.013838`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.077518`, avg `0.019038`, median `0.045303`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.2625`, primary_mae `0.022193`, avg `0.001928`, median `0.005303`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.3125`, primary_mae `0.02285`, avg `0.00023`, median `0.002338`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.031561`, avg `-0.000843`, median `-0.00478`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.25`, primary_mae `0.068741`, avg `0.01372`, median `0.020147`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3125`, primary_mae `0.116658`, avg `0.039718`, median `0.06505`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.2625`, primary_mae `0.022193`, avg `0.001928`, median `0.005303`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.3125`, primary_mae `0.02285`, avg `0.00023`, median `0.002338`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.031561`, avg `-0.000843`, median `-0.00478`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.25`, primary_mae `0.068741`, avg `0.01372`, median `0.020147`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3125`, primary_mae `0.116658`, avg `0.039718`, median `0.06505`

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
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.2625`, primary_mae `0.022193`, avg `0.001928`, median `0.005303`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.3125`, primary_mae `0.02285`, avg `0.00023`, median `0.002338`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.031561`, avg `-0.000843`, median `-0.00478`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.25`, primary_mae `0.068741`, avg `0.01372`, median `0.020147`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3125`, primary_mae `0.116658`, avg `0.039718`, median `0.06505`

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
