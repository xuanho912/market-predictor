# Historical Replay Benchmark

Generated at: `2026-08-05T00:14:48.150230+00:00`
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
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.012414`
- secondary_mean_absolute_error: `0.012738`
- primary_error_advantage: `0.000324`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.014316`
- secondary_mean_absolute_error: `0.015439`
- primary_error_advantage: `0.001123`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.024196`
- secondary_mean_absolute_error: `0.024768`
- primary_error_advantage: `0.000572`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.051897`
- secondary_mean_absolute_error: `0.050557`
- primary_error_advantage: `-0.00134`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.066652`
- secondary_mean_absolute_error: `0.07181`
- primary_error_advantage: `0.005158`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5375`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.012096`, as_primary `0`, as_primary_hit `None`, avg `0.001867`, median `0.004164`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.013381`, as_primary `0`, as_primary_hit `None`, avg `0.003809`, median `0.005323`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.021832`, as_primary `0`, as_primary_hit `None`, avg `0.002701`, median `0.002713`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.03062`, as_primary `0`, as_primary_hit `None`, avg `0.005498`, median `0.009961`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.057703`, as_primary `0`, as_primary_hit `None`, avg `0.016208`, median `0.019929`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.012233`, as_primary `40`, as_primary_hit `0.625`, avg `0.001867`, median `0.004164`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.01454`, as_primary `40`, as_primary_hit `0.65`, avg `0.003809`, median `0.005323`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.027522`, as_primary `40`, as_primary_hit `0.525`, avg `0.002701`, median `0.002713`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.049147`, as_primary `40`, as_primary_hit `0.675`, avg `0.005498`, median `0.009961`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.078137`, as_primary `40`, as_primary_hit `0.65`, avg `0.016208`, median `0.019929`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.012736`, as_primary `40`, as_primary_hit `0.65`, avg `0.001867`, median `0.004164`
- 5d: sample `80`, direction_hit `0.3`, path_mae `0.015724`, as_primary `40`, as_primary_hit `0.75`, avg `0.003809`, median `0.005323`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.025513`, as_primary `40`, as_primary_hit `0.525`, avg `0.002701`, median `0.002713`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.060561`, as_primary `40`, as_primary_hit `0.575`, avg `0.005498`, median `0.009961`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.072683`, as_primary `40`, as_primary_hit `0.475`, avg `0.016208`, median `0.019929`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.011913`, as_primary `0`, as_primary_hit `None`, avg `0.001867`, median `0.004164`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.013496`, as_primary `0`, as_primary_hit `None`, avg `0.003809`, median `0.005323`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.020436`, as_primary `0`, as_primary_hit `None`, avg `0.002701`, median `0.002713`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.030538`, as_primary `0`, as_primary_hit `None`, avg `0.005498`, median `0.009961`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.053726`, as_primary `0`, as_primary_hit `None`, avg `0.016208`, median `0.019929`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.55`, primary_mae `0.012719`, avg `-6.1e-05`, median `0.001723`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.5333`, primary_mae `0.013425`, avg `0.00292`, median `0.004845`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.5167`, primary_mae `0.024006`, avg `-0.000406`, median `-0.001861`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.5667`, primary_mae `0.046744`, avg `0.003837`, median `0.009961`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.6`, primary_mae `0.061677`, avg `0.014565`, median `0.015082`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.011498`, avg `0.007649`, median `0.010315`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.016989`, avg `0.006476`, median `0.010594`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.024768`, avg `0.01202`, median `0.014273`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.2`, primary_mae `0.067353`, avg `0.010483`, median `0.007243`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.081579`, avg `0.02114`, median `0.021115`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.008904`, avg `-0.002088`, median `-0.00051`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.009163`, avg `0.003889`, median `0.00454`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.013559`, avg `-0.00226`, median `-0.004581`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.036638`, avg `-0.001858`, median `0.000176`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.046862`, avg `-0.014294`, median `-0.024343`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.45`, primary_mae `0.013583`, avg `0.003185`, median `0.007843`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.5167`, primary_mae `0.016033`, avg `0.003782`, median `0.006112`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.4833`, primary_mae `0.027742`, avg `0.004354`, median `0.005535`
- 20d: sample `60`, primary_hit `0.5667`, primary_closer `0.4833`, primary_mae `0.056983`, avg `0.00795`, median `0.012323`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.5167`, primary_mae `0.073249`, avg `0.026376`, median `0.045588`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.008904, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.009163, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.013559, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.036638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.046862, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011913, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012736, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.008904, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013381, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015724, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.009163, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020436, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027522, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.013559, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030538, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060561, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.036638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053726, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.078137, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.046862, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.014248`, avg `-0.004255`, median `-0.003968`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.0099`, avg `-0.00032`, median `0.00171`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.020505`, avg `-0.001054`, median `-0.011067`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.049843`, avg `0.003945`, median `0.006243`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.093523`, avg `-0.015481`, median `-0.034556`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.6875`, primary_mae `0.01335`, avg `-0.001476`, median `0.003063`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.013273`, avg `-0.001151`, median `0.003417`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.021009`, avg `-0.001749`, median `-0.011067`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.04816`, avg `0.004516`, median `0.00675`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.082613`, avg `0.003361`, median `-0.02547`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.012736`, avg `0.006127`, median `0.009658`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.018289`, avg `0.004794`, median `0.009437`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.023958`, avg `0.009119`, median `0.011814`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.068289`, avg `0.009054`, median `0.007243`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.087106`, avg `0.020886`, median `0.021115`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4875`, primary_mae `0.012414`, avg `0.001867`, median `0.004164`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.014316`, avg `0.003809`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.024196`, avg `0.002701`, median `0.002713`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.051897`, avg `0.005498`, median `0.009961`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5375`, primary_mae `0.066652`, avg `0.016208`, median `0.019929`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4875`, primary_mae `0.012414`, avg `0.001867`, median `0.004164`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.014316`, avg `0.003809`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.024196`, avg `0.002701`, median `0.002713`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.051897`, avg `0.005498`, median `0.009961`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5375`, primary_mae `0.066652`, avg `0.016208`, median `0.019929`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.625`, primary_mae `0.011674`, avg `-0.002364`, median `0.000402`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.011101`, avg `0.001255`, median `0.003922`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.016699`, avg `-0.001994`, median `-0.005041`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.039544`, avg `0.004252`, median `0.006115`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.525`, primary_mae `0.061276`, avg `-0.001098`, median `-0.015624`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.011498`, avg `0.007649`, median `0.010315`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.016989`, avg `0.006476`, median `0.010594`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.024768`, avg `0.01202`, median `0.014273`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.2`, primary_mae `0.067353`, avg `0.010483`, median `0.007243`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.081579`, avg `0.02114`, median `0.021115`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4875`, primary_mae `0.012414`, avg `0.001867`, median `0.004164`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.014316`, avg `0.003809`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.024196`, avg `0.002701`, median `0.002713`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.051897`, avg `0.005498`, median `0.009961`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5375`, primary_mae `0.066652`, avg `0.016208`, median `0.019929`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.4875`, primary_mae `0.012414`, avg `0.001867`, median `0.004164`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.014316`, avg `0.003809`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.024196`, avg `0.002701`, median `0.002713`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.051897`, avg `0.005498`, median `0.009961`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5375`, primary_mae `0.066652`, avg `0.016208`, median `0.019929`

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
