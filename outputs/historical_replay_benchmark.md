# Historical Replay Benchmark

Generated at: `2026-07-15T04:20:49.385822+00:00`
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
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.016636`
- secondary_mean_absolute_error: `0.014207`
- primary_error_advantage: `-0.002429`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.021971`
- secondary_mean_absolute_error: `0.019836`
- primary_error_advantage: `-0.002135`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.024296`
- secondary_mean_absolute_error: `0.024639`
- primary_error_advantage: `0.000343`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.9`
- primary_vs_secondary_accuracy_spread: `-0.575`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.030954`
- secondary_mean_absolute_error: `0.028078`
- primary_error_advantage: `-0.002876`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.7625`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.059344`
- secondary_mean_absolute_error: `0.044189`
- primary_error_advantage: `-0.015155`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.013817`, as_primary `0`, as_primary_hit `None`, avg `0.003752`, median `0.005602`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.020153`, as_primary `0`, as_primary_hit `None`, avg `0.004242`, median `0.008034`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.023522`, as_primary `0`, as_primary_hit `None`, avg `0.011842`, median `0.011623`
- 20d: sample `80`, direction_hit `0.9`, path_mae `0.021674`, as_primary `0`, as_primary_hit `None`, avg `0.027738`, median `0.025773`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.041283`, as_primary `0`, as_primary_hit `None`, avg `0.041495`, median `0.051138`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.015177`, as_primary `20`, as_primary_hit `0.8`, avg `0.003752`, median `0.005602`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.022124`, as_primary `20`, as_primary_hit `0.75`, avg `0.004242`, median `0.008034`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.028073`, as_primary `20`, as_primary_hit `0.85`, avg `0.011842`, median `0.011623`
- 20d: sample `80`, direction_hit `0.9`, path_mae `0.032718`, as_primary `20`, as_primary_hit `0.95`, avg `0.027738`, median `0.025773`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.044738`, as_primary `20`, as_primary_hit `0.95`, avg `0.041495`, median `0.051138`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.017184`, as_primary `60`, as_primary_hit `0.5667`, avg `0.003752`, median `0.005602`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.022773`, as_primary `60`, as_primary_hit `0.5167`, avg `0.004242`, median `0.008034`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.024751`, as_primary `60`, as_primary_hit `0.5833`, avg `0.011842`, median `0.011623`
- 20d: sample `80`, direction_hit `0.1`, path_mae `0.032198`, as_primary `60`, as_primary_hit `0.8833`, avg `0.027738`, median `0.025773`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.061424`, as_primary `60`, as_primary_hit `0.7`, avg `0.041495`, median `0.051138`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.013752`, as_primary `0`, as_primary_hit `None`, avg `0.003752`, median `0.005602`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.019077`, as_primary `0`, as_primary_hit `None`, avg `0.004242`, median `0.008034`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.021528`, as_primary `0`, as_primary_hit `None`, avg `0.011842`, median `0.011623`
- 20d: sample `80`, direction_hit `0.9`, path_mae `0.019707`, as_primary `0`, as_primary_hit `None`, avg `0.027738`, median `0.025773`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.042444`, as_primary `0`, as_primary_hit `None`, avg `0.041495`, median `0.051138`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.475`, primary_mae `0.015697`, avg `0.002258`, median `0.004571`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.023004`, avg `0.002965`, median `0.00793`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.024919`, avg `0.014057`, median `0.015738`
- 20d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.035685`, avg `0.022983`, median `0.025773`
- 60d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.068506`, avg `0.044041`, median `0.060603`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.017575`, avg `0.005246`, median `0.01081`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.020937`, avg `0.005519`, median `0.008828`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.575`, primary_mae `0.023672`, avg `0.009626`, median `0.003724`
- 20d: sample `40`, primary_hit `0.05`, primary_closer `0.5`, primary_mae `0.026222`, avg `0.032493`, median `0.02635`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.050182`, avg `0.038948`, median `0.032884`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.016636`, avg `0.003752`, median `0.005602`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.021971`, avg `0.004242`, median `0.008034`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.5125`, primary_mae `0.024296`, avg `0.011842`, median `0.011623`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.4625`, primary_mae `0.030954`, avg `0.027738`, median `0.025773`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.4`, primary_mae `0.059344`, avg `0.041495`, median `0.051138`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.4625, 'primary_mean_absolute_error': 0.016636, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.021971, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.024296, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.4625, 'primary_mean_absolute_error': 0.030954, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4625, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.059344, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013752, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017184, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.4625, 'primary_mean_absolute_error': 0.016636, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019077, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022773, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.021971, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021528, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028073, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.024296, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.9, 'primary_vs_secondary_accuracy_spread': -0.575, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019707, 'direction_hit_rate': 0.9}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032718, 'direction_hit_rate': 0.9}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.4625, 'primary_mean_absolute_error': 0.030954, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.7625, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041283, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061424, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4625, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.059344, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.022099`, avg `-0.003861`, median `-0.004407`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.037077`, avg `-0.000193`, median `0.005181`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.041797`, avg `0.014219`, median `0.029091`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.052012`, avg `0.011471`, median `0.021827`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.118047`, avg `0.039214`, median `0.07206`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.023701`, avg `-0.002039`, median `-0.000629`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.03178`, avg `-0.00705`, median `-0.010026`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.039406`, avg `0.015909`, median `0.024797`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.5625`, primary_mae `0.055626`, avg `0.01975`, median `0.017154`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.110619`, avg `0.034948`, median `0.06708`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.019003`, avg `0.009546`, median `0.012678`
- 5d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.016673`, avg `0.015485`, median `0.017098`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.5625`, primary_mae `0.019171`, avg `0.020804`, median `0.024318`
- 20d: sample `16`, primary_hit `0.0`, primary_closer `0.375`, primary_mae `0.032553`, avg `0.049572`, median `0.050926`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.25`, primary_mae `0.063662`, avg `0.079313`, median `0.091366`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.016636`, avg `0.003752`, median `0.005602`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.021971`, avg `0.004242`, median `0.008034`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.5125`, primary_mae `0.024296`, avg `0.011842`, median `0.011623`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.4625`, primary_mae `0.030954`, avg `0.027738`, median `0.025773`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.4`, primary_mae `0.059344`, avg `0.041495`, median `0.051138`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.016636`, avg `0.003752`, median `0.005602`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.021971`, avg `0.004242`, median `0.008034`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.5125`, primary_mae `0.024296`, avg `0.011842`, median `0.011623`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.4625`, primary_mae `0.030954`, avg `0.027738`, median `0.025773`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.4`, primary_mae `0.059344`, avg `0.041495`, median `0.051138`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.011458`, avg `0.003777`, median `0.006001`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.01751`, avg `0.003883`, median `0.006888`
- 10d: sample `40`, primary_hit `0.725`, primary_closer `0.55`, primary_mae `0.017229`, avg `0.007895`, median `0.005736`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.0189`, avg `0.022083`, median `0.024168`
- 60d: sample `40`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.032837`, avg `0.028336`, median `0.033893`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.4833`, primary_mae `0.013653`, avg `0.00525`, median `0.006946`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.4333`, primary_mae `0.017715`, avg `0.006707`, median `0.009345`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.5333`, primary_mae `0.019452`, avg `0.011059`, median `0.010651`
- 20d: sample `60`, primary_hit `0.35`, primary_closer `0.4333`, primary_mae `0.02307`, avg `0.030523`, median `0.028076`
- 60d: sample `60`, primary_hit `0.4833`, primary_closer `0.4`, primary_mae `0.042`, avg `0.044111`, median `0.04634`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.016636`, avg `0.003752`, median `0.005602`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.021971`, avg `0.004242`, median `0.008034`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.5125`, primary_mae `0.024296`, avg `0.011842`, median `0.011623`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.4625`, primary_mae `0.030954`, avg `0.027738`, median `0.025773`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.4`, primary_mae `0.059344`, avg `0.041495`, median `0.051138`

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
