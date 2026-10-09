# Historical Replay Benchmark

Generated at: `2026-10-09T01:25:58.763186+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_supportive_but_not_forward_validated`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.3125`
- primary_vs_secondary_accuracy_spread: `0.375`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.020075`
- secondary_mean_absolute_error: `0.018346`
- primary_error_advantage: `-0.001729`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.35`
- primary_vs_secondary_accuracy_spread: `0.3`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.02379`
- secondary_mean_absolute_error: `0.023836`
- primary_error_advantage: `4.6e-05`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.032895`
- secondary_mean_absolute_error: `0.03611`
- primary_error_advantage: `0.003215`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.5625`
- primary_mean_absolute_error: `0.057508`
- secondary_mean_absolute_error: `0.066875`
- primary_error_advantage: `0.009367`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.056084`
- secondary_mean_absolute_error: `0.059013`
- primary_error_advantage: `0.002929`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.016868`, as_primary `0`, as_primary_hit `None`, avg `-0.002886`, median `-0.002276`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.021236`, as_primary `0`, as_primary_hit `None`, avg `-0.00483`, median `-0.010999`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.031379`, as_primary `0`, as_primary_hit `None`, avg `-0.000456`, median `0.000957`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.046285`, as_primary `0`, as_primary_hit `None`, avg `0.029362`, median `0.028999`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.048254`, as_primary `0`, as_primary_hit `None`, avg `0.069369`, median `0.084258`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.017486`, as_primary `20`, as_primary_hit `0.75`, avg `-0.002886`, median `-0.002276`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.024609`, as_primary `20`, as_primary_hit `0.65`, avg `-0.00483`, median `-0.010999`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.037973`, as_primary `20`, as_primary_hit `0.75`, avg `-0.000456`, median `0.000957`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.06525`, as_primary `20`, as_primary_hit `0.85`, avg `0.029362`, median `0.028999`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.059186`, as_primary `20`, as_primary_hit `0.95`, avg `0.069369`, median `0.084258`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.020934`, as_primary `60`, as_primary_hit `0.3333`, avg `-0.002886`, median `-0.002276`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.023017`, as_primary `60`, as_primary_hit `0.35`, avg `-0.00483`, median `-0.010999`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.031032`, as_primary `60`, as_primary_hit `0.45`, avg `-0.000456`, median `0.000957`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.059133`, as_primary `60`, as_primary_hit `0.6833`, avg `0.029362`, median `0.028999`
- 60d: sample `80`, direction_hit `0.1625`, path_mae `0.055911`, as_primary `60`, as_primary_hit `0.8`, avg `0.069369`, median `0.084258`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.01619`, as_primary `0`, as_primary_hit `None`, avg `-0.002886`, median `-0.002276`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.019523`, as_primary `0`, as_primary_hit `None`, avg `-0.00483`, median `-0.010999`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.027643`, as_primary `0`, as_primary_hit `None`, avg `-0.000456`, median `0.000957`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.040143`, as_primary `0`, as_primary_hit `None`, avg `0.029362`, median `0.028999`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.047539`, as_primary `0`, as_primary_hit `None`, avg `0.069369`, median `0.084258`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6875`, primary_closer `0.45`, primary_mae `0.020075`, avg `-0.002886`, median `-0.002276`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.02379`, avg `-0.00483`, median `-0.010999`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.032895`, avg `-0.000456`, median `0.000957`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.5625`, primary_mae `0.057508`, avg `0.029362`, median `0.028999`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.056084`, avg `0.069369`, median `0.084258`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.012101`, avg `0.008481`, median `0.012678`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.02018`, avg `0.00962`, median `0.009975`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.027224`, avg `0.01323`, median `0.013533`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.5`, primary_mae `0.038555`, avg `0.042711`, median `0.040733`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.4`, primary_mae `0.025971`, avg `0.093442`, median `0.099615`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.9`, primary_closer `0.2`, primary_mae `0.02982`, avg `-0.015472`, median `-0.011068`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.025045`, avg `-0.020944`, median `-0.023937`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.041278`, avg `-0.013717`, median `-0.032841`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.090284`, avg `0.020444`, median `0.019624`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.077521`, avg `0.076745`, median `0.092349`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.01919`, avg `-0.002277`, median `-0.002999`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.575`, primary_mae `0.024967`, avg `-0.003998`, median `-0.013612`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.03154`, avg `-0.000668`, median `-0.002285`
- 20d: sample `40`, primary_hit `0.225`, primary_closer `0.625`, primary_mae `0.050596`, avg `0.027147`, median `0.024852`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.525`, primary_mae `0.060422`, avg `0.053645`, median `0.044239`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.012101, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.02018, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.027224, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.038555, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.025971, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.3125, 'primary_vs_secondary_accuracy_spread': 0.375, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01619, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020934, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.012101, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.35, 'primary_vs_secondary_accuracy_spread': 0.3, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019523, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024609, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.02018, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027643, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037973, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.027224, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.5625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040143, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06525, 'direction_hit_rate': 0.725}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.038555, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.047539, 'direction_hit_rate': 0.8375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059186, 'direction_hit_rate': 0.8375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.025971, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.013099`, avg `0.010606`, median `0.016621`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.017173`, avg `0.014887`, median `0.012047`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.024824`, avg `0.016471`, median `0.017921`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.875`, primary_mae `0.021695`, avg `0.059849`, median `0.060676`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.375`, primary_mae `0.015877`, avg `0.105861`, median `0.099778`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.013511`, avg `0.007015`, median `0.012449`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.022844`, avg `0.007893`, median `0.008828`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.028455`, avg `0.013055`, median `0.015682`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.625`, primary_mae `0.02968`, avg `0.051855`, median `0.058396`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.030045`, avg `0.090134`, median `0.09828`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.125`, primary_mae `0.03194`, avg `-0.010673`, median `-0.010671`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.1875`, primary_mae `0.025279`, avg `-0.018244`, median `-0.022951`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.039665`, avg `-0.012731`, median `-0.029899`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.091779`, avg `0.022627`, median `0.019624`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.073587`, avg `0.074214`, median `0.085768`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6875`, primary_closer `0.45`, primary_mae `0.020075`, avg `-0.002886`, median `-0.002276`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.02379`, avg `-0.00483`, median `-0.010999`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.032895`, avg `-0.000456`, median `0.000957`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.5625`, primary_mae `0.057508`, avg `0.029362`, median `0.028999`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.056084`, avg `0.069369`, median `0.084258`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6875`, primary_closer `0.45`, primary_mae `0.020075`, avg `-0.002886`, median `-0.002276`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.02379`, avg `-0.00483`, median `-0.010999`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.032895`, avg `-0.000456`, median `0.000957`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.5625`, primary_mae `0.057508`, avg `0.029362`, median `0.028999`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.056084`, avg `0.069369`, median `0.084258`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.012101`, avg `0.008481`, median `0.012678`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.02018`, avg `0.00962`, median `0.009975`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.027224`, avg `0.01323`, median `0.013533`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.5`, primary_mae `0.038555`, avg `0.042711`, median `0.040733`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.4`, primary_mae `0.025971`, avg `0.093442`, median `0.099615`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.024718`, avg `-0.007327`, median `-0.009933`
- 5d: sample `40`, primary_hit `0.7`, primary_closer `0.425`, primary_mae `0.025253`, avg `-0.01019`, median `-0.01806`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.7`, primary_mae `0.033528`, avg `-0.001478`, median `-0.009917`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.65`, primary_mae `0.06648`, avg `0.032865`, median `0.026541`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.076419`, avg `0.074789`, median `0.085768`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6875`, primary_closer `0.45`, primary_mae `0.020075`, avg `-0.002886`, median `-0.002276`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.02379`, avg `-0.00483`, median `-0.010999`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.032895`, avg `-0.000456`, median `0.000957`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.5625`, primary_mae `0.057508`, avg `0.029362`, median `0.028999`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.056084`, avg `0.069369`, median `0.084258`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6875`, primary_closer `0.45`, primary_mae `0.020075`, avg `-0.002886`, median `-0.002276`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.02379`, avg `-0.00483`, median `-0.010999`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.032895`, avg `-0.000456`, median `0.000957`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.5625`, primary_mae `0.057508`, avg `0.029362`, median `0.028999`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.056084`, avg `0.069369`, median `0.084258`

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
