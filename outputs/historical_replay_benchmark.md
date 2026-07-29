# Historical Replay Benchmark

Generated at: `2026-07-29T00:10:54.672067+00:00`
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
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.022222`
- secondary_mean_absolute_error: `0.019834`
- primary_error_advantage: `-0.002388`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.028834`
- secondary_mean_absolute_error: `0.025632`
- primary_error_advantage: `-0.003202`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.035085`
- secondary_mean_absolute_error: `0.024376`
- primary_error_advantage: `-0.010709`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.25`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.067189`
- secondary_mean_absolute_error: `0.061324`
- primary_error_advantage: `-0.005865`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.099009`
- secondary_mean_absolute_error: `0.086281`
- primary_error_advantage: `-0.012728`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.018486`, as_primary `0`, as_primary_hit `None`, avg `-0.002002`, median `0.000655`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.022`, as_primary `0`, as_primary_hit `None`, avg `-0.001875`, median `0.001499`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.024357`, as_primary `0`, as_primary_hit `None`, avg `0.005263`, median `0.001591`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.03981`, as_primary `0`, as_primary_hit `None`, avg `0.016144`, median `0.021309`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.065426`, as_primary `0`, as_primary_hit `None`, avg `0.028793`, median `0.052147`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.019843`, as_primary `40`, as_primary_hit `0.475`, avg `-0.002002`, median `0.000655`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.024686`, as_primary `40`, as_primary_hit `0.45`, avg `-0.001875`, median `0.001499`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.02909`, as_primary `40`, as_primary_hit `0.325`, avg `0.005263`, median `0.001591`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.059466`, as_primary `40`, as_primary_hit `0.575`, avg `0.016144`, median `0.021309`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.079028`, as_primary `40`, as_primary_hit `0.65`, avg `0.028793`, median `0.052147`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.022383`, as_primary `40`, as_primary_hit `0.575`, avg `-0.002002`, median `0.000655`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.030365`, as_primary `40`, as_primary_hit `0.625`, avg `-0.001875`, median `0.001499`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.031864`, as_primary `40`, as_primary_hit `0.725`, avg `0.005263`, median `0.001591`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.074181`, as_primary `40`, as_primary_hit `0.675`, avg `0.016144`, median `0.021309`
- 60d: sample `80`, direction_hit `0.35`, path_mae `0.107964`, as_primary `40`, as_primary_hit `0.65`, avg `0.028793`, median `0.052147`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.018613`, as_primary `0`, as_primary_hit `None`, avg `-0.002002`, median `0.000655`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.021536`, as_primary `0`, as_primary_hit `None`, avg `-0.001875`, median `0.001499`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.023084`, as_primary `0`, as_primary_hit `None`, avg `0.005263`, median `0.001591`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.040226`, as_primary `0`, as_primary_hit `None`, avg `0.016144`, median `0.021309`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.065798`, as_primary `0`, as_primary_hit `None`, avg `0.028793`, median `0.052147`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.4667`, primary_mae `0.021997`, avg `-0.001325`, median `0.000983`
- 5d: sample `60`, primary_hit `0.3667`, primary_closer `0.35`, primary_mae `0.024928`, avg `-0.000159`, median `0.00235`
- 10d: sample `60`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.031595`, avg `0.008086`, median `0.000914`
- 20d: sample `60`, primary_hit `0.45`, primary_closer `0.4667`, primary_mae `0.058046`, avg `0.023888`, median `0.023936`
- 60d: sample `60`, primary_hit `0.4833`, primary_closer `0.4333`, primary_mae `0.078565`, avg `0.047853`, median `0.058802`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.022897`, avg `-0.004033`, median `-0.000629`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.040552`, avg `-0.007026`, median `-0.004165`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.045556`, avg `-0.003205`, median `0.009806`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.094617`, avg `-0.007088`, median `0.012493`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.160344`, avg `-0.028388`, median `-0.028749`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.014659`, avg `-0.005092`, median `-4.2e-05`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.2`, primary_mae `0.018343`, avg `-0.004676`, median `8.8e-05`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.023413`, avg `-0.007334`, median `-0.010196`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.039568`, avg `0.000436`, median `-0.001572`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.043258`, avg `0.013159`, median `0.003188`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.025843`, avg `0.003126`, median `0.003333`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.036368`, avg `0.005775`, median `0.0098`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.046532`, avg `0.016625`, median `0.025887`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.090333`, avg `0.023602`, median `0.04668`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.275`, primary_mae `0.134908`, avg `0.027368`, median `0.07049`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.6`, primary_mae `0.022544`, avg `-0.009167`, median `-0.005846`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.024256`, avg `-0.014375`, median `-0.016241`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.023865`, avg `-0.004863`, median `-0.007383`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.65`, primary_mae `0.048522`, avg `0.016938`, median `0.023936`
- 60d: sample `20`, primary_hit `0.75`, primary_closer `0.7`, primary_mae `0.082965`, avg `0.047276`, median `0.059313`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014659, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.018343, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.023413, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.039568, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.043258, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018486, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022383, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014659, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021536, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030365, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.018343, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023084, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031864, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.023413, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03981, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074181, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.039568, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065426, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.107964, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.043258, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.032178`, avg `-0.021369`, median `-0.031812`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.035981`, avg `-0.028609`, median `-0.028941`
- 10d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.032256`, avg `-0.017639`, median `-0.014696`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.065705`, avg `0.001093`, median `0.01375`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.104545`, avg `0.027797`, median `0.041779`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.02175`, avg `-0.007531`, median `-0.00023`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.025034`, avg `-0.0145`, median `-0.008746`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.025246`, avg `-0.005148`, median `-0.007383`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.050622`, avg `0.015295`, median `0.024617`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.084227`, avg `0.046168`, median `0.054967`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.025499`, avg `-0.002781`, median `-0.000629`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.04237`, avg `-0.005682`, median `-0.002733`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.050469`, avg `0.001595`, median `0.012861`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.099357`, avg `-0.002962`, median `0.012493`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.164469`, avg `-0.022681`, median `-0.028749`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022222`, avg `-0.002002`, median `0.000655`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.3375`, primary_mae `0.028834`, avg `-0.001875`, median `0.001499`
- 10d: sample `80`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.035085`, avg `0.005263`, median `0.001591`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.067189`, avg `0.016144`, median `0.021309`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.099009`, avg `0.028793`, median `0.052147`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022222`, avg `-0.002002`, median `0.000655`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.3375`, primary_mae `0.028834`, avg `-0.001875`, median `0.001499`
- 10d: sample `80`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.035085`, avg `0.005263`, median `0.001591`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.067189`, avg `0.016144`, median `0.021309`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.099009`, avg `0.028793`, median `0.052147`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.018602`, avg `-0.00713`, median `-0.000971`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.0213`, avg `-0.009525`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.023639`, avg `-0.006099`, median `-0.008819`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.6`, primary_mae `0.044045`, avg `0.008687`, median `0.016081`
- 60d: sample `40`, primary_hit `0.65`, primary_closer `0.575`, primary_mae `0.063111`, avg `0.030218`, median `0.041779`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.025843`, avg `0.003126`, median `0.003333`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.036368`, avg `0.005775`, median `0.0098`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.046532`, avg `0.016625`, median `0.025887`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.090333`, avg `0.023602`, median `0.04668`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.275`, primary_mae `0.134908`, avg `0.027368`, median `0.07049`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022222`, avg `-0.002002`, median `0.000655`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.3375`, primary_mae `0.028834`, avg `-0.001875`, median `0.001499`
- 10d: sample `80`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.035085`, avg `0.005263`, median `0.001591`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.067189`, avg `0.016144`, median `0.021309`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.099009`, avg `0.028793`, median `0.052147`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.021724`, avg `0.002597`, median `0.001736`
- 5d: sample `40`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.025264`, avg `0.00695`, median `0.005089`
- 10d: sample `40`, primary_hit `0.225`, primary_closer `0.225`, primary_mae `0.03546`, avg `0.01456`, median `0.017629`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.062808`, avg `0.027364`, median `0.024755`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.076364`, avg `0.048142`, median `0.058049`

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
