# Historical Replay Benchmark

Generated at: `2026-06-22T23:54:32.928446+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'high', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay', 'forward validation completed samples are below the minimum gate'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.015654`
- secondary_mean_absolute_error: `0.013923`
- primary_error_advantage: `-0.001731`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.017472`
- secondary_mean_absolute_error: `0.016065`
- primary_error_advantage: `-0.001407`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.025275`
- secondary_mean_absolute_error: `0.019516`
- primary_error_advantage: `-0.005759`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.0383`
- secondary_mean_absolute_error: `0.02563`
- primary_error_advantage: `-0.01267`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.059494`
- secondary_mean_absolute_error: `0.051324`
- primary_error_advantage: `-0.00817`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.01425`, as_primary `0`, as_primary_hit `None`, avg `-0.000697`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.016152`, as_primary `0`, as_primary_hit `None`, avg `-0.004072`, median `-0.00538`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.020002`, as_primary `0`, as_primary_hit `None`, avg `-0.003143`, median `-0.003658`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.025923`, as_primary `0`, as_primary_hit `None`, avg `0.006565`, median `0.012734`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.051922`, as_primary `0`, as_primary_hit `None`, avg `0.023782`, median `0.039962`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.015654`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.000697`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.017472`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.004072`, median `-0.00538`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.025275`, as_primary `80`, as_primary_hit `0.4`, avg `-0.003143`, median `-0.003658`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.0383`, as_primary `80`, as_primary_hit `0.6625`, avg `0.006565`, median `0.012734`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.059494`, as_primary `80`, as_primary_hit `0.625`, avg `0.023782`, median `0.039962`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.014613`, as_primary `0`, as_primary_hit `None`, avg `-0.000697`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.01791`, as_primary `0`, as_primary_hit `None`, avg `-0.004072`, median `-0.00538`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.02523`, as_primary `0`, as_primary_hit `None`, avg `-0.003143`, median `-0.003658`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.053112`, as_primary `0`, as_primary_hit `None`, avg `0.006565`, median `0.012734`
- 60d: sample `80`, direction_hit `0.375`, path_mae `0.062745`, as_primary `0`, as_primary_hit `None`, avg `0.023782`, median `0.039962`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.013923`, as_primary `0`, as_primary_hit `None`, avg `-0.000697`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.016065`, as_primary `0`, as_primary_hit `None`, avg `-0.004072`, median `-0.00538`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.019516`, as_primary `0`, as_primary_hit `None`, avg `-0.003143`, median `-0.003658`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.02563`, as_primary `0`, as_primary_hit `None`, avg `0.006565`, median `0.012734`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.051324`, as_primary `0`, as_primary_hit `None`, avg `0.023782`, median `0.039962`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.375`, primary_mae `0.015654`, avg `-0.000697`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.017472`, avg `-0.004072`, median `-0.00538`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.025275`, avg `-0.003143`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.3125`, primary_mae `0.0383`, avg `0.006565`, median `0.012734`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.059494`, avg `0.023782`, median `0.039962`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.014156`, avg `-0.001164`, median `-0.00191`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.017338`, avg `-0.005555`, median `-0.00538`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.026648`, avg `-0.006555`, median `-0.007701`
- 20d: sample `40`, primary_hit `0.55`, primary_closer `0.325`, primary_mae `0.040151`, avg `-0.003598`, median `0.00368`
- 60d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.058171`, avg `0.006776`, median `0.021036`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.017151`, avg `-0.000229`, median `-0.001207`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.017606`, avg `-0.002589`, median `-0.005063`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.325`, primary_mae `0.023902`, avg `0.00027`, median `-0.001481`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.3`, primary_mae `0.03645`, avg `0.016728`, median `0.028346`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.45`, primary_mae `0.060818`, avg `0.040788`, median `0.061862`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.014156, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.017338, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.023902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.03645, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.058171, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013923, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015654, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.014156, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016065, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01791, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.017338, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019516, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025275, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.023902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02563, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053112, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.03645, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051324, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062745, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.058171, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.01689`, avg `-0.005957`, median `-0.006094`
- 5d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.015484`, avg `-0.018169`, median `-0.014993`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.011207`, avg `0.004766`, median `0.006144`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.125`, primary_mae `0.017352`, avg `0.028135`, median `0.030181`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.027189`, avg `0.075992`, median `0.086868`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.017395`, avg `-0.002565`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.014892`, avg `-0.009072`, median `-0.010753`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.01282`, avg `0.003059`, median `-0.000811`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.017336`, avg `0.029764`, median `0.030181`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.5625`, primary_mae `0.032758`, avg `0.074865`, median `0.088952`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.017395`, avg `-0.002565`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.014892`, avg `-0.009072`, median `-0.010753`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.01282`, avg `0.003059`, median `-0.000811`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.017336`, avg `0.029764`, median `0.030181`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.5625`, primary_mae `0.032758`, avg `0.074865`, median `0.088952`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.375`, primary_mae `0.015654`, avg `-0.000697`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.017472`, avg `-0.004072`, median `-0.00538`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.025275`, avg `-0.003143`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.3125`, primary_mae `0.0383`, avg `0.006565`, median `0.012734`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.059494`, avg `0.023782`, median `0.039962`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.375`, primary_mae `0.015654`, avg `-0.000697`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.017472`, avg `-0.004072`, median `-0.00538`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.025275`, avg `-0.003143`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.3125`, primary_mae `0.0383`, avg `0.006565`, median `0.012734`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.059494`, avg `0.023782`, median `0.039962`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.014156`, avg `-0.001164`, median `-0.00191`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.017338`, avg `-0.005555`, median `-0.00538`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.026648`, avg `-0.006555`, median `-0.007701`
- 20d: sample `40`, primary_hit `0.55`, primary_closer `0.325`, primary_mae `0.040151`, avg `-0.003598`, median `0.00368`
- 60d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.058171`, avg `0.006776`, median `0.021036`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.017151`, avg `-0.000229`, median `-0.001207`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.017606`, avg `-0.002589`, median `-0.005063`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.325`, primary_mae `0.023902`, avg `0.00027`, median `-0.001481`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.3`, primary_mae `0.03645`, avg `0.016728`, median `0.028346`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.45`, primary_mae `0.060818`, avg `0.040788`, median `0.061862`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.375`, primary_mae `0.015654`, avg `-0.000697`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.017472`, avg `-0.004072`, median `-0.00538`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.025275`, avg `-0.003143`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.3125`, primary_mae `0.0383`, avg `0.006565`, median `0.012734`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.059494`, avg `0.023782`, median `0.039962`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.375`, primary_mae `0.015654`, avg `-0.000697`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.017472`, avg `-0.004072`, median `-0.00538`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.025275`, avg `-0.003143`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.3125`, primary_mae `0.0383`, avg `0.006565`, median `0.012734`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.059494`, avg `0.023782`, median `0.039962`

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
