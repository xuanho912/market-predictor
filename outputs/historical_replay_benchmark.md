# Historical Replay Benchmark

Generated at: `2026-06-22T15:55:04.986798+00:00`
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
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.01551`
- secondary_mean_absolute_error: `0.012995`
- primary_error_advantage: `-0.002515`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.016544`
- secondary_mean_absolute_error: `0.015462`
- primary_error_advantage: `-0.001082`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.025495`
- secondary_mean_absolute_error: `0.019653`
- primary_error_advantage: `-0.005842`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.038236`
- secondary_mean_absolute_error: `0.026022`
- primary_error_advantage: `-0.012214`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.059086`
- secondary_mean_absolute_error: `0.051564`
- primary_error_advantage: `-0.007522`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.013594`, as_primary `0`, as_primary_hit `None`, avg `-0.000551`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.015516`, as_primary `0`, as_primary_hit `None`, avg `-0.003843`, median `-0.003858`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.020217`, as_primary `0`, as_primary_hit `None`, avg `-0.002762`, median `-0.003658`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.02622`, as_primary `0`, as_primary_hit `None`, avg `0.007006`, median `0.015161`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.052214`, as_primary `0`, as_primary_hit `None`, avg `0.024482`, median `0.044937`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.01551`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.000551`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.016544`, as_primary `80`, as_primary_hit `0.45`, avg `-0.003843`, median `-0.003858`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.025495`, as_primary `80`, as_primary_hit `0.4`, avg `-0.002762`, median `-0.003658`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.038236`, as_primary `80`, as_primary_hit `0.675`, avg `0.007006`, median `0.015161`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.059086`, as_primary `80`, as_primary_hit `0.625`, avg `0.024482`, median `0.044937`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.013528`, as_primary `0`, as_primary_hit `None`, avg `-0.000551`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.017669`, as_primary `0`, as_primary_hit `None`, avg `-0.003843`, median `-0.003858`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.025611`, as_primary `0`, as_primary_hit `None`, avg `-0.002762`, median `-0.003658`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.053553`, as_primary `0`, as_primary_hit `None`, avg `0.007006`, median `0.015161`
- 60d: sample `80`, direction_hit `0.375`, path_mae `0.063049`, as_primary `0`, as_primary_hit `None`, avg `0.024482`, median `0.044937`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.012995`, as_primary `0`, as_primary_hit `None`, avg `-0.000551`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.015462`, as_primary `0`, as_primary_hit `None`, avg `-0.003843`, median `-0.003858`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.019653`, as_primary `0`, as_primary_hit `None`, avg `-0.002762`, median `-0.003658`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.026022`, as_primary `0`, as_primary_hit `None`, avg `0.007006`, median `0.015161`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.051564`, as_primary `0`, as_primary_hit `None`, avg `0.024482`, median `0.044937`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3375`, primary_mae `0.01551`, avg `-0.000551`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.016544`, avg `-0.003843`, median `-0.003858`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.025495`, avg `-0.002762`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.038236`, avg `0.007006`, median `0.015161`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.059086`, avg `0.024482`, median `0.044937`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.275`, primary_mae `0.014154`, avg `-0.002417`, median `-0.002845`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.015268`, avg `-0.006156`, median `-0.00538`
- 10d: sample `40`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.024277`, avg `-0.007505`, median `-0.007701`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.039579`, avg `-0.002852`, median `0.005773`
- 60d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.057183`, avg `0.00811`, median `0.021036`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.016867`, avg `0.001315`, median `-0.000152`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.017821`, avg `-0.001529`, median `-0.00156`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.026713`, avg `0.001982`, median `-0.001153`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.3`, primary_mae `0.036894`, avg `0.016863`, median `0.028346`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.45`, primary_mae `0.060989`, avg `0.040854`, median `0.061862`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.014154, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.015268, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.024277, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.036894, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.057183, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012995, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01551, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.014154, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015462, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017669, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.015268, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019653, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025611, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.024277, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026022, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053553, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.036894, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051564, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.063049, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.057183, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.017075`, avg `-0.005834`, median `-0.006094`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.015331`, avg `-0.017293`, median `-0.014993`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.010826`, avg `0.003857`, median `0.002506`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.125`, primary_mae `0.017687`, avg `0.0278`, median `0.030181`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.029412`, avg `0.07374`, median `0.083174`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.018106`, avg `-0.001885`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.014631`, avg `-0.009333`, median `-0.010753`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.01178`, avg `0.000354`, median `-0.001577`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.017101`, avg `0.03`, median `0.030746`
- 60d: sample `16`, primary_hit `1.0`, primary_closer `0.5625`, primary_mae `0.027278`, avg `0.080346`, median `0.088952`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.018106`, avg `-0.001885`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.014631`, avg `-0.009333`, median `-0.010753`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.01178`, avg `0.000354`, median `-0.001577`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.017101`, avg `0.03`, median `0.030746`
- 60d: sample `16`, primary_hit `1.0`, primary_closer `0.5625`, primary_mae `0.027278`, avg `0.080346`, median `0.088952`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3375`, primary_mae `0.01551`, avg `-0.000551`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.016544`, avg `-0.003843`, median `-0.003858`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.025495`, avg `-0.002762`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.038236`, avg `0.007006`, median `0.015161`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.059086`, avg `0.024482`, median `0.044937`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3375`, primary_mae `0.01551`, avg `-0.000551`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.016544`, avg `-0.003843`, median `-0.003858`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.025495`, avg `-0.002762`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.038236`, avg `0.007006`, median `0.015161`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.059086`, avg `0.024482`, median `0.044937`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.275`, primary_mae `0.014154`, avg `-0.002417`, median `-0.002845`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.015268`, avg `-0.006156`, median `-0.00538`
- 10d: sample `40`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.024277`, avg `-0.007505`, median `-0.007701`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.039579`, avg `-0.002852`, median `0.005773`
- 60d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.057183`, avg `0.00811`, median `0.021036`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.016867`, avg `0.001315`, median `-0.000152`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.017821`, avg `-0.001529`, median `-0.00156`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.026713`, avg `0.001982`, median `-0.001153`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.3`, primary_mae `0.036894`, avg `0.016863`, median `0.028346`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.45`, primary_mae `0.060989`, avg `0.040854`, median `0.061862`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3375`, primary_mae `0.01551`, avg `-0.000551`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.016544`, avg `-0.003843`, median `-0.003858`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.025495`, avg `-0.002762`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.038236`, avg `0.007006`, median `0.015161`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.059086`, avg `0.024482`, median `0.044937`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3375`, primary_mae `0.01551`, avg `-0.000551`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.016544`, avg `-0.003843`, median `-0.003858`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.3125`, primary_mae `0.025495`, avg `-0.002762`, median `-0.003658`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.038236`, avg `0.007006`, median `0.015161`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.059086`, avg `0.024482`, median `0.044937`

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
