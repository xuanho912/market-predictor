# Historical Replay Benchmark

Generated at: `2026-11-12T11:52:26.789825+00:00`
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
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.016949`
- secondary_mean_absolute_error: `0.01957`
- primary_error_advantage: `0.002621`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.023376`
- secondary_mean_absolute_error: `0.021836`
- primary_error_advantage: `-0.00154`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `-0.0125`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.036601`
- secondary_mean_absolute_error: `0.033939`
- primary_error_advantage: `-0.002662`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.3375`
- primary_vs_secondary_accuracy_spread: `0.325`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.045369`
- secondary_mean_absolute_error: `0.042243`
- primary_error_advantage: `-0.003126`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.056882`
- secondary_mean_absolute_error: `0.068293`
- primary_error_advantage: `0.011411`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.7`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015374`, as_primary `0`, as_primary_hit `None`, avg `-0.002046`, median `-0.005844`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.020177`, as_primary `0`, as_primary_hit `None`, avg `-0.002136`, median `-0.005558`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.026864`, as_primary `0`, as_primary_hit `None`, avg `0.005094`, median `0.006521`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.025875`, as_primary `0`, as_primary_hit `None`, avg `0.020337`, median `0.025687`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.048478`, as_primary `0`, as_primary_hit `None`, avg `0.041617`, median `0.060132`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.017452`, as_primary `60`, as_primary_hit `0.4333`, avg `-0.002046`, median `-0.005844`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.023376`, as_primary `60`, as_primary_hit `0.4667`, avg `-0.002136`, median `-0.005558`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.034263`, as_primary `60`, as_primary_hit `0.5333`, avg `0.005094`, median `0.006521`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.040039`, as_primary `60`, as_primary_hit `0.8`, avg `0.020337`, median `0.025687`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.05251`, as_primary `60`, as_primary_hit `0.7333`, avg `0.041617`, median `0.060132`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.019455`, as_primary `20`, as_primary_hit `0.35`, avg `-0.002046`, median `-0.005844`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.021836`, as_primary `20`, as_primary_hit `0.5`, avg `-0.002136`, median `-0.005558`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.036735`, as_primary `20`, as_primary_hit `0.65`, avg `0.005094`, median `0.006521`
- 20d: sample `80`, direction_hit `0.2125`, path_mae `0.05037`, as_primary `20`, as_primary_hit `0.75`, avg `0.020337`, median `0.025687`
- 60d: sample `80`, direction_hit `0.25`, path_mae `0.072326`, as_primary `20`, as_primary_hit `0.8`, avg `0.041617`, median `0.060132`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015191`, as_primary `0`, as_primary_hit `None`, avg `-0.002046`, median `-0.005844`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.019451`, as_primary `0`, as_primary_hit `None`, avg `-0.002136`, median `-0.005558`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.026122`, as_primary `0`, as_primary_hit `None`, avg `0.005094`, median `0.006521`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.025036`, as_primary `0`, as_primary_hit `None`, avg `0.020337`, median `0.025687`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.049814`, as_primary `0`, as_primary_hit `None`, avg `0.041617`, median `0.060132`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.575`, primary_mae `0.016949`, avg `-0.002046`, median `-0.005844`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.023376`, avg `-0.002136`, median `-0.005558`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.036601`, avg `0.005094`, median `0.006521`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.5`, primary_mae `0.045369`, avg `0.020337`, median `0.025687`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.056882`, avg `0.041617`, median `0.060132`

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
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.016333`, avg `-0.003812`, median `-0.011553`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.02225`, avg `-0.004469`, median `-0.005578`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.038276`, avg `0.003312`, median `0.008`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.2`, primary_mae `0.062993`, avg `0.017965`, median `0.028361`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.067744`, avg `0.050101`, median `0.064363`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.5667`, primary_mae `0.017154`, avg `-0.001458`, median `-0.002703`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4833`, primary_mae `0.023751`, avg `-0.001359`, median `-0.005558`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4833`, primary_mae `0.036043`, avg `0.005688`, median `0.006262`
- 20d: sample `60`, primary_hit `0.8`, primary_closer `0.6`, primary_mae `0.039494`, avg `0.021128`, median `0.024827`
- 60d: sample `60`, primary_hit `0.7333`, primary_closer `0.6667`, primary_mae `0.053261`, avg `0.038789`, median `0.056661`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.016333, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.02225, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.036043, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.039494, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7333, 'primary_closer_than_secondary_rate': 0.6667, 'primary_mean_absolute_error': 0.053261, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015191, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019455, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.016333, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019451, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023376, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.02225, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': -0.0125, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026122, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036735, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.036043, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.3375, 'primary_vs_secondary_accuracy_spread': 0.325, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025036, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05037, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.039494, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048478, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072326, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7333, 'primary_closer_than_secondary_rate': 0.6667, 'primary_mean_absolute_error': 0.053261, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.024972`, avg `-5e-05`, median `-0.004159`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.029809`, avg `0.001194`, median `-0.010753`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.023934`, avg `0.021796`, median `0.022448`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.031455`, avg `0.033882`, median `0.031427`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.875`, primary_mae `0.01981`, avg `0.079187`, median `0.086868`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.022508`, avg `0.000937`, median `0.000401`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.028864`, avg `-0.001823`, median `-0.005558`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.033898`, avg `0.00841`, median `0.003189`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.6875`, primary_mae `0.037033`, avg `0.024938`, median `0.028445`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.6875`, primary_mae `0.046572`, avg `0.050009`, median `0.070816`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.017303`, avg `-0.00254`, median `-0.011553`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.024567`, avg `-0.001784`, median `0.004066`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.041157`, avg `0.00534`, median `0.011684`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.125`, primary_mae `0.066564`, avg `0.022172`, median `0.028361`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.07028`, avg `0.060935`, median `0.069067`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.575`, primary_mae `0.016949`, avg `-0.002046`, median `-0.005844`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.023376`, avg `-0.002136`, median `-0.005558`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.036601`, avg `0.005094`, median `0.006521`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.5`, primary_mae `0.045369`, avg `0.020337`, median `0.025687`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.056882`, avg `0.041617`, median `0.060132`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.575`, primary_mae `0.016949`, avg `-0.002046`, median `-0.005844`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.023376`, avg `-0.002136`, median `-0.005558`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.036601`, avg `0.005094`, median `0.006521`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.5`, primary_mae `0.045369`, avg `0.020337`, median `0.025687`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.056882`, avg `0.041617`, median `0.060132`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.5667`, primary_mae `0.017154`, avg `-0.001458`, median `-0.002703`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4833`, primary_mae `0.023751`, avg `-0.001359`, median `-0.005558`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4833`, primary_mae `0.036043`, avg `0.005688`, median `0.006262`
- 20d: sample `60`, primary_hit `0.8`, primary_closer `0.6`, primary_mae `0.039494`, avg `0.021128`, median `0.024827`
- 60d: sample `60`, primary_hit `0.7333`, primary_closer `0.6667`, primary_mae `0.053261`, avg `0.038789`, median `0.056661`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.016333`, avg `-0.003812`, median `-0.011553`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.02225`, avg `-0.004469`, median `-0.005578`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.038276`, avg `0.003312`, median `0.008`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.2`, primary_mae `0.062993`, avg `0.017965`, median `0.028361`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.067744`, avg `0.050101`, median `0.064363`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.575`, primary_mae `0.016949`, avg `-0.002046`, median `-0.005844`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.023376`, avg `-0.002136`, median `-0.005558`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.036601`, avg `0.005094`, median `0.006521`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.5`, primary_mae `0.045369`, avg `0.020337`, median `0.025687`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.056882`, avg `0.041617`, median `0.060132`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.575`, primary_mae `0.016949`, avg `-0.002046`, median `-0.005844`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.023376`, avg `-0.002136`, median `-0.005558`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.036601`, avg `0.005094`, median `0.006521`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.5`, primary_mae `0.045369`, avg `0.020337`, median `0.025687`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.056882`, avg `0.041617`, median `0.060132`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.575`, primary_mae `0.016949`, avg `-0.002046`, median `-0.005844`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.023376`, avg `-0.002136`, median `-0.005558`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.036601`, avg `0.005094`, median `0.006521`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.5`, primary_mae `0.045369`, avg `0.020337`, median `0.025687`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.056882`, avg `0.041617`, median `0.060132`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
