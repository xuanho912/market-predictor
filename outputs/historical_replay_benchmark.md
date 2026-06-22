# Historical Replay Benchmark

Generated at: `2026-06-22T17:05:23.008876+00:00`
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
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.015946`
- secondary_mean_absolute_error: `0.013381`
- primary_error_advantage: `-0.002565`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.016835`
- secondary_mean_absolute_error: `0.015721`
- primary_error_advantage: `-0.001114`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.023942`
- secondary_mean_absolute_error: `0.019153`
- primary_error_advantage: `-0.004789`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.03808`
- secondary_mean_absolute_error: `0.025878`
- primary_error_advantage: `-0.012202`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.059523`
- secondary_mean_absolute_error: `0.051685`
- primary_error_advantage: `-0.007838`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.013953`, as_primary `0`, as_primary_hit `None`, avg `-0.001205`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.015739`, as_primary `0`, as_primary_hit `None`, avg `-0.004455`, median `-0.00538`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.019308`, as_primary `0`, as_primary_hit `None`, avg `-0.003658`, median `-0.004981`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.02603`, as_primary `0`, as_primary_hit `None`, avg `0.006841`, median `0.013938`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.052534`, as_primary `0`, as_primary_hit `None`, avg `0.02315`, median `0.039962`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.015946`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.001205`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.016835`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.004455`, median `-0.00538`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.023942`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.003658`, median `-0.004981`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.03808`, as_primary `80`, as_primary_hit `0.675`, avg `0.006841`, median `0.013938`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.059523`, as_primary `80`, as_primary_hit `0.6125`, avg `0.02315`, median `0.039962`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.014096`, as_primary `0`, as_primary_hit `None`, avg `-0.001205`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017527`, as_primary `0`, as_primary_hit `None`, avg `-0.004455`, median `-0.00538`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.024715`, as_primary `0`, as_primary_hit `None`, avg `-0.003658`, median `-0.004981`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.053388`, as_primary `0`, as_primary_hit `None`, avg `0.006841`, median `0.013938`
- 60d: sample `80`, direction_hit `0.3875`, path_mae `0.062192`, as_primary `0`, as_primary_hit `None`, avg `0.02315`, median `0.039962`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.013381`, as_primary `0`, as_primary_hit `None`, avg `-0.001205`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.015721`, as_primary `0`, as_primary_hit `None`, avg `-0.004455`, median `-0.00538`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.019153`, as_primary `0`, as_primary_hit `None`, avg `-0.003658`, median `-0.004981`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.025878`, as_primary `0`, as_primary_hit `None`, avg `0.006841`, median `0.013938`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.051685`, as_primary `0`, as_primary_hit `None`, avg `0.02315`, median `0.039962`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3625`, primary_mae `0.015946`, avg `-0.001205`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.016835`, avg `-0.004455`, median `-0.00538`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.023942`, avg `-0.003658`, median `-0.004981`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.3125`, primary_mae `0.03808`, avg `0.006841`, median `0.013938`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.059523`, avg `0.02315`, median `0.039962`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.275`, primary_mae `0.014715`, avg `-0.002181`, median `-0.00191`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.016065`, avg `-0.006321`, median `-0.00538`
- 10d: sample `40`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.023983`, avg `-0.007587`, median `-0.008059`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.03971`, avg `-0.003047`, median `0.005773`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.058229`, avg `0.005512`, median `0.002524`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.017176`, avg `-0.000229`, median `-0.001207`
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

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.014715, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016065, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.023902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.03645, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.058229, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013381, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015946, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.014715, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015721, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017527, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016065, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019153, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024715, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.023902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025878, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053388, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.03645, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051685, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062192, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.058229, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

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
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.016873`, avg `-0.002012`, median `-5e-05`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.014525`, avg `-0.00944`, median `-0.010753`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.012292`, avg `-0.000115`, median `-0.001577`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.25`, primary_mae `0.020101`, avg `0.026999`, median `0.028979`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.5`, primary_mae `0.035335`, avg `0.071986`, median `0.083174`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.016873`, avg `-0.002012`, median `-5e-05`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.014525`, avg `-0.00944`, median `-0.010753`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.012292`, avg `-0.000115`, median `-0.001577`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.25`, primary_mae `0.020101`, avg `0.026999`, median `0.028979`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.5`, primary_mae `0.035335`, avg `0.071986`, median `0.083174`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3625`, primary_mae `0.015946`, avg `-0.001205`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.016835`, avg `-0.004455`, median `-0.00538`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.023942`, avg `-0.003658`, median `-0.004981`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.3125`, primary_mae `0.03808`, avg `0.006841`, median `0.013938`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.059523`, avg `0.02315`, median `0.039962`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3625`, primary_mae `0.015946`, avg `-0.001205`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.016835`, avg `-0.004455`, median `-0.00538`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.023942`, avg `-0.003658`, median `-0.004981`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.3125`, primary_mae `0.03808`, avg `0.006841`, median `0.013938`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.059523`, avg `0.02315`, median `0.039962`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.275`, primary_mae `0.014715`, avg `-0.002181`, median `-0.00191`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.016065`, avg `-0.006321`, median `-0.00538`
- 10d: sample `40`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.023983`, avg `-0.007587`, median `-0.008059`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.03971`, avg `-0.003047`, median `0.005773`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.058229`, avg `0.005512`, median `0.002524`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.017176`, avg `-0.000229`, median `-0.001207`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.017606`, avg `-0.002589`, median `-0.005063`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.325`, primary_mae `0.023902`, avg `0.00027`, median `-0.001481`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.3`, primary_mae `0.03645`, avg `0.016728`, median `0.028346`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.45`, primary_mae `0.060818`, avg `0.040788`, median `0.061862`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3625`, primary_mae `0.015946`, avg `-0.001205`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.016835`, avg `-0.004455`, median `-0.00538`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.023942`, avg `-0.003658`, median `-0.004981`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.3125`, primary_mae `0.03808`, avg `0.006841`, median `0.013938`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.059523`, avg `0.02315`, median `0.039962`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3625`, primary_mae `0.015946`, avg `-0.001205`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.016835`, avg `-0.004455`, median `-0.00538`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.023942`, avg `-0.003658`, median `-0.004981`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.3125`, primary_mae `0.03808`, avg `0.006841`, median `0.013938`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.059523`, avg `0.02315`, median `0.039962`

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
