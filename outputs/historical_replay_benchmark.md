# Historical Replay Benchmark

Generated at: `2026-09-16T08:53:37.047441+00:00`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.021425`
- secondary_mean_absolute_error: `0.014364`
- primary_error_advantage: `-0.007061`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.0223`
- secondary_mean_absolute_error: `0.016827`
- primary_error_advantage: `-0.005473`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.030352`
- secondary_mean_absolute_error: `0.02471`
- primary_error_advantage: `-0.005642`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.2375`
- primary_mean_absolute_error: `0.055878`
- secondary_mean_absolute_error: `0.031091`
- primary_error_advantage: `-0.024787`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2625`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.475`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.108711`
- secondary_mean_absolute_error: `0.066628`
- primary_error_advantage: `-0.042083`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014782`, as_primary `0`, as_primary_hit `None`, avg `0.000308`, median `0.000691`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.016927`, as_primary `0`, as_primary_hit `None`, avg `-0.003976`, median `4.2e-05`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.025858`, as_primary `0`, as_primary_hit `None`, avg `-0.005586`, median `-0.008001`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.031605`, as_primary `0`, as_primary_hit `None`, avg `0.009014`, median `0.008518`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.071338`, as_primary `0`, as_primary_hit `None`, avg `0.041106`, median `0.060495`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.016256`, as_primary `0`, as_primary_hit `None`, avg `0.000308`, median `0.000691`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.02036`, as_primary `0`, as_primary_hit `None`, avg `-0.003976`, median `4.2e-05`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.03639`, as_primary `0`, as_primary_hit `None`, avg `-0.005586`, median `-0.008001`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.049713`, as_primary `0`, as_primary_hit `None`, avg `0.009014`, median `0.008518`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.07286`, as_primary `0`, as_primary_hit `None`, avg `0.041106`, median `0.060495`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.021425`, as_primary `80`, as_primary_hit `0.525`, avg `0.000308`, median `0.000691`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.0223`, as_primary `80`, as_primary_hit `0.5`, avg `-0.003976`, median `4.2e-05`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.030352`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.005586`, median `-0.008001`
- 20d: sample `80`, direction_hit `0.425`, path_mae `0.055878`, as_primary `80`, as_primary_hit `0.575`, avg `0.009014`, median `0.008518`
- 60d: sample `80`, direction_hit `0.2625`, path_mae `0.108711`, as_primary `80`, as_primary_hit `0.7375`, avg `0.041106`, median `0.060495`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014364`, as_primary `0`, as_primary_hit `None`, avg `0.000308`, median `0.000691`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.016827`, as_primary `0`, as_primary_hit `None`, avg `-0.003976`, median `4.2e-05`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.02471`, as_primary `0`, as_primary_hit `None`, avg `-0.005586`, median `-0.008001`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.031091`, as_primary `0`, as_primary_hit `None`, avg `0.009014`, median `0.008518`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.066628`, as_primary `0`, as_primary_hit `None`, avg `0.041106`, median `0.060495`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.2875`, primary_mae `0.021425`, avg `0.000308`, median `0.000691`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.3625`, primary_mae `0.0223`, avg `-0.003976`, median `4.2e-05`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.375`, primary_mae `0.030352`, avg `-0.005586`, median `-0.008001`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2375`, primary_mae `0.055878`, avg `0.009014`, median `0.008518`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.325`, primary_mae `0.108711`, avg `0.041106`, median `0.060495`

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
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.2833`, primary_mae `0.021085`, avg `-0.001006`, median `-0.000519`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.35`, primary_mae `0.022178`, avg `-0.00606`, median `-0.001281`
- 10d: sample `60`, primary_hit `0.6333`, primary_closer `0.3667`, primary_mae `0.026128`, avg `-0.008357`, median `-0.009483`
- 20d: sample `60`, primary_hit `0.45`, primary_closer `0.2167`, primary_mae `0.058551`, avg `0.006152`, median `0.007005`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.3167`, primary_mae `0.117244`, avg `0.032018`, median `0.059722`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.022444`, avg `0.004249`, median `0.009116`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.022664`, avg `0.002275`, median `0.003973`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.043027`, avg `0.002728`, median `0.011331`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.047861`, avg `0.0176`, median `0.014651`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.35`, primary_mae `0.083114`, avg `0.068368`, median `0.064505`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.2833, 'primary_mean_absolute_error': 0.021085, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022178, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.026128, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047861, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.083114, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014364, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021425, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.2833, 'primary_mean_absolute_error': 0.021085, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016827, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0223, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022178, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02471, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03639, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.026128, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.2375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031091, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055878, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047861, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.475, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066628, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.108711, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.083114, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.027075`, avg `0.000507`, median `0.000341`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.027662`, avg `-0.00539`, median `0.002018`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.021654`, avg `0.002087`, median `-0.003556`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.063137`, avg `0.03836`, median `0.047524`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.133669`, avg `0.083903`, median `0.103033`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.024156`, avg `-0.00402`, median `-0.005521`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.024663`, avg `-0.009648`, median `-0.002115`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.020548`, avg `-0.007437`, median `-0.008236`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.047086`, avg `0.018373`, median `0.017863`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.089553`, avg `0.03493`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.024499`, avg `0.001576`, median `0.000803`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.029469`, avg `-0.000513`, median `0.002102`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.033614`, avg `-0.018527`, median `-0.028209`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.1875`, primary_mae `0.061574`, avg `-0.016001`, median `-0.020813`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.18207`, avg `0.016882`, median `0.044579`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.2875`, primary_mae `0.021425`, avg `0.000308`, median `0.000691`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.3625`, primary_mae `0.0223`, avg `-0.003976`, median `4.2e-05`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.375`, primary_mae `0.030352`, avg `-0.005586`, median `-0.008001`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2375`, primary_mae `0.055878`, avg `0.009014`, median `0.008518`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.325`, primary_mae `0.108711`, avg `0.041106`, median `0.060495`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.2875`, primary_mae `0.021425`, avg `0.000308`, median `0.000691`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.3625`, primary_mae `0.0223`, avg `-0.003976`, median `4.2e-05`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.375`, primary_mae `0.030352`, avg `-0.005586`, median `-0.008001`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2375`, primary_mae `0.055878`, avg `0.009014`, median `0.008518`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.325`, primary_mae `0.108711`, avg `0.041106`, median `0.060495`

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
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.2875`, primary_mae `0.021425`, avg `0.000308`, median `0.000691`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.3625`, primary_mae `0.0223`, avg `-0.003976`, median `4.2e-05`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.375`, primary_mae `0.030352`, avg `-0.005586`, median `-0.008001`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2375`, primary_mae `0.055878`, avg `0.009014`, median `0.008518`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.325`, primary_mae `0.108711`, avg `0.041106`, median `0.060495`

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
