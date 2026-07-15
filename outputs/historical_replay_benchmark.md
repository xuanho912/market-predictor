# Historical Replay Benchmark

Generated at: `2026-07-15T14:12:59.824704+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
Overfit warning: `{'level': 'low', 'reasons': [], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.012766`
- secondary_mean_absolute_error: `0.012216`
- primary_error_advantage: `-0.00055`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.018361`
- secondary_mean_absolute_error: `0.016507`
- primary_error_advantage: `-0.001854`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.027667`
- secondary_mean_absolute_error: `0.024071`
- primary_error_advantage: `-0.003596`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.071045`
- secondary_mean_absolute_error: `0.045188`
- primary_error_advantage: `-0.025857`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.074614`
- secondary_mean_absolute_error: `0.071303`
- primary_error_advantage: `-0.003311`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.011938`, as_primary `0`, as_primary_hit `None`, avg `7.1e-05`, median `0.000463`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.016189`, as_primary `0`, as_primary_hit `None`, avg `-0.000174`, median `0.003801`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.021172`, as_primary `0`, as_primary_hit `None`, avg `-0.001909`, median `0.000879`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.033124`, as_primary `0`, as_primary_hit `None`, avg `-0.001075`, median `0.009961`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.06284`, as_primary `0`, as_primary_hit `None`, avg `-0.006795`, median `-0.011052`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.012216`, as_primary `0`, as_primary_hit `None`, avg `7.1e-05`, median `0.000463`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.016507`, as_primary `0`, as_primary_hit `None`, avg `-0.000174`, median `0.003801`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.024071`, as_primary `0`, as_primary_hit `None`, avg `-0.001909`, median `0.000879`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.045188`, as_primary `0`, as_primary_hit `None`, avg `-0.001075`, median `0.009961`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.071303`, as_primary `0`, as_primary_hit `None`, avg `-0.006795`, median `-0.011052`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.012766`, as_primary `80`, as_primary_hit `0.525`, avg `7.1e-05`, median `0.000463`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018361`, as_primary `80`, as_primary_hit `0.55`, avg `-0.000174`, median `0.003801`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.027667`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.001909`, median `0.000879`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.071045`, as_primary `80`, as_primary_hit `0.675`, avg `-0.001075`, median `0.009961`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.074614`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.006795`, median `-0.011052`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.011402`, as_primary `0`, as_primary_hit `None`, avg `7.1e-05`, median `0.000463`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.015508`, as_primary `0`, as_primary_hit `None`, avg `-0.000174`, median `0.003801`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.020858`, as_primary `0`, as_primary_hit `None`, avg `-0.001909`, median `0.000879`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.033501`, as_primary `0`, as_primary_hit `None`, avg `-0.001075`, median `0.009961`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.060815`, as_primary `0`, as_primary_hit `None`, avg `-0.006795`, median `-0.011052`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.6`, primary_mae `0.009796`, avg `0.00185`, median `0.000463`
- 5d: sample `60`, primary_hit `0.4333`, primary_closer `0.5833`, primary_mae `0.015008`, avg `0.001736`, median `0.00487`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.4`, primary_mae `0.02777`, avg `-0.001458`, median `0.001302`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.2833`, primary_mae `0.069527`, avg `-0.001782`, median `0.009961`
- 60d: sample `60`, primary_hit `0.5667`, primary_closer `0.5167`, primary_mae `0.065005`, avg `-0.007443`, median `-0.011052`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.021676`, avg `-0.005267`, median `-8.6e-05`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.02842`, avg `-0.005904`, median `-0.001055`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.027357`, avg `-0.003263`, median `-0.000777`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.075598`, avg `0.001048`, median `0.014663`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.103441`, avg `-0.004853`, median `-0.017896`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.65`, primary_mae `0.007918`, avg `-0.002692`, median `-0.002721`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.65`, primary_mae `0.012427`, avg `0.001094`, median `0.004486`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.25`, primary_mae `0.026468`, avg `-0.001612`, median `0.002926`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.057583`, avg `0.002497`, median `0.01201`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.055313`, avg `-0.023665`, median `-0.030547`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.0169`, avg `-0.001585`, median `-0.000648`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.023411`, avg `-0.00441`, median `-0.003493`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.028605`, avg `-0.003416`, median `-0.000777`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.087637`, avg `-0.004363`, median `0.008468`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.078859`, avg `-0.008669`, median `-0.011052`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.6`, primary_mae `0.009345`, avg `0.006145`, median `0.00544`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.014194`, avg `0.007032`, median `0.006405`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.02699`, avg `0.000808`, median `-0.00151`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.051321`, avg `0.00193`, median `0.00878`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.085424`, avg `0.013821`, median `0.027639`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.007918, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.012427, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.026468, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.051321, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.055313, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011402, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012766, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.007918, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015508, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018361, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.012427, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020858, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027667, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.026468, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033124, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071045, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.051321, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060815, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074614, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.055313, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.009366`, avg `0.002558`, median `0.000638`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.012254`, avg `0.007858`, median `0.009025`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.031101`, avg `0.006281`, median `0.004222`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.035158`, avg `-0.012556`, median `-0.008396`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.09456`, avg `0.020729`, median `0.046764`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.625`, primary_mae `0.009164`, avg `0.005442`, median `0.00431`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.011669`, avg `0.007023`, median `0.006047`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.025428`, avg `-0.002083`, median `-0.00151`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.047375`, avg `-0.002463`, median `0.006376`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.090373`, avg `0.016361`, median `0.046764`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.022205`, avg `-0.003882`, median `-8.6e-05`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.028045`, avg `-0.004676`, median `0.00024`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.027616`, avg `-0.003565`, median `-0.000777`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.082093`, avg `0.005508`, median `0.02136`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.11116`, avg `0.006524`, median `0.003555`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.012766`, avg `7.1e-05`, median `0.000463`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.018361`, avg `-0.000174`, median `0.003801`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.027667`, avg `-0.001909`, median `0.000879`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.2875`, primary_mae `0.071045`, avg `-0.001075`, median `0.009961`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.525`, primary_mae `0.074614`, avg `-0.006795`, median `-0.011052`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.012766`, avg `7.1e-05`, median `0.000463`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.018361`, avg `-0.000174`, median `0.003801`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.027667`, avg `-0.001909`, median `0.000879`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.2875`, primary_mae `0.071045`, avg `-0.001075`, median `0.009961`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.525`, primary_mae `0.074614`, avg `-0.006795`, median `-0.011052`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.010022`, avg `-0.000297`, median `-0.002547`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.6`, primary_mae `0.015414`, avg `-0.000911`, median `0.003801`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.028161`, avg `-0.002591`, median `0.002812`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.07863`, avg `-0.003638`, median `0.010966`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.55`, primary_mae `0.054795`, avg `-0.018075`, median `-0.014755`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.5333`, primary_mae `0.013906`, avg `-0.001954`, median `-0.00203`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.5`, primary_mae `0.019749`, avg `-0.002576`, median `0.003016`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.3833`, primary_mae `0.027893`, avg `-0.002815`, median `0.001939`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.2667`, primary_mae `0.077619`, avg `-0.002076`, median `0.010966`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.07101`, avg `-0.013668`, median `-0.014755`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.012766`, avg `7.1e-05`, median `0.000463`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.018361`, avg `-0.000174`, median `0.003801`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.027667`, avg `-0.001909`, median `0.000879`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.2875`, primary_mae `0.071045`, avg `-0.001075`, median `0.009961`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.525`, primary_mae `0.074614`, avg `-0.006795`, median `-0.011052`

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
