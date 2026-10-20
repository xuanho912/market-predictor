# Historical Replay Benchmark

Generated at: `2026-10-20T17:10:56.474684+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.016891`
- secondary_mean_absolute_error: `0.015359`
- primary_error_advantage: `-0.001532`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.020715`
- secondary_mean_absolute_error: `0.018334`
- primary_error_advantage: `-0.002381`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.028778`
- secondary_mean_absolute_error: `0.025406`
- primary_error_advantage: `-0.003372`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.053603`
- secondary_mean_absolute_error: `0.035157`
- primary_error_advantage: `-0.018446`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.10749`
- secondary_mean_absolute_error: `0.069715`
- primary_error_advantage: `-0.037775`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.015912`, as_primary `0`, as_primary_hit `None`, avg `-0.003356`, median `-0.003205`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.019614`, as_primary `0`, as_primary_hit `None`, avg `-0.002657`, median `0.000839`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.027023`, as_primary `0`, as_primary_hit `None`, avg `-0.000886`, median `-0.000315`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.034994`, as_primary `0`, as_primary_hit `None`, avg `0.016189`, median `0.01259`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.067259`, as_primary `0`, as_primary_hit `None`, avg `0.037071`, median `0.052152`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.017149`, as_primary `0`, as_primary_hit `None`, avg `-0.003356`, median `-0.003205`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.024091`, as_primary `0`, as_primary_hit `None`, avg `-0.002657`, median `0.000839`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.035989`, as_primary `0`, as_primary_hit `None`, avg `-0.000886`, median `-0.000315`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.050885`, as_primary `0`, as_primary_hit `None`, avg `0.016189`, median `0.01259`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.085988`, as_primary `0`, as_primary_hit `None`, avg `0.037071`, median `0.052152`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.016891`, as_primary `80`, as_primary_hit `0.45`, avg `-0.003356`, median `-0.003205`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.020715`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.002657`, median `0.000839`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.028778`, as_primary `80`, as_primary_hit `0.475`, avg `-0.000886`, median `-0.000315`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.053603`, as_primary `80`, as_primary_hit `0.6125`, avg `0.016189`, median `0.01259`
- 60d: sample `80`, direction_hit `0.3125`, path_mae `0.10749`, as_primary `80`, as_primary_hit `0.6875`, avg `0.037071`, median `0.052152`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.015352`, as_primary `0`, as_primary_hit `None`, avg `-0.003356`, median `-0.003205`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.018076`, as_primary `0`, as_primary_hit `None`, avg `-0.002657`, median `0.000839`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.024584`, as_primary `0`, as_primary_hit `None`, avg `-0.000886`, median `-0.000315`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.033004`, as_primary `0`, as_primary_hit `None`, avg `0.016189`, median `0.01259`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.066926`, as_primary `0`, as_primary_hit `None`, avg `0.037071`, median `0.052152`

## Edge Status Performance

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017856`, avg `-0.004568`, median `-0.007364`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.022763`, avg `-0.002532`, median `-0.006074`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.040275`, avg `-0.001604`, median `-0.004345`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.275`, primary_mae `0.061971`, avg `0.015359`, median `0.008277`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.25`, primary_mae `0.121982`, avg `0.059612`, median `0.068484`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015926`, avg `-0.002144`, median `0.001174`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.018668`, avg `-0.002782`, median `0.002614`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.01728`, avg `-0.000168`, median `-0.000315`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.045234`, avg `0.01702`, median `0.020913`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.092998`, avg `0.014529`, median `0.028478`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017856`, avg `-0.004568`, median `-0.007364`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.022763`, avg `-0.002532`, median `-0.006074`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.040275`, avg `-0.001604`, median `-0.004345`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.275`, primary_mae `0.061971`, avg `0.015359`, median `0.008277`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.25`, primary_mae `0.121982`, avg `0.059612`, median `0.068484`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015926`, avg `-0.002144`, median `0.001174`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.018668`, avg `-0.002782`, median `0.002614`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.01728`, avg `-0.000168`, median `-0.000315`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.045234`, avg `0.01702`, median `0.020913`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.092998`, avg `0.014529`, median `0.028478`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.015926, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018668, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01728, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.045234, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.092998, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015352, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017149, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.015926, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018076, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024091, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018668, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024584, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035989, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01728, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033004, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053603, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.045234, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066926, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.10749, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.092998, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.012269`, avg `0.00592`, median `0.00607`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.010007`, avg `0.006419`, median `0.009732`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.010338`, avg `0.008099`, median `0.007771`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.038569`, avg `0.017643`, median `0.021414`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.10167`, avg `-0.009263`, median `0.035301`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.011019`, avg `0.000307`, median `0.002845`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.012546`, avg `0.002082`, median `0.006873`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.014705`, avg `0.00971`, median `0.007771`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.042446`, avg `0.019581`, median `0.024588`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.091272`, avg `-0.005238`, median `0.023396`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.018765`, avg `-0.007591`, median `-0.013275`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.020549`, avg `-0.000396`, median `-0.000601`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.039588`, avg `0.010715`, median `0.007808`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.1875`, primary_mae `0.058173`, avg `0.024294`, median `0.012724`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.138878`, avg `0.078226`, median `0.068484`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.016891`, avg `-0.003356`, median `-0.003205`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4625`, primary_mae `0.020715`, avg `-0.002657`, median `0.000839`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.028778`, avg `-0.000886`, median `-0.000315`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.2875`, primary_mae `0.053603`, avg `0.016189`, median `0.01259`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.10749`, avg `0.037071`, median `0.052152`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.016891`, avg `-0.003356`, median `-0.003205`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4625`, primary_mae `0.020715`, avg `-0.002657`, median `0.000839`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.028778`, avg `-0.000886`, median `-0.000315`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.2875`, primary_mae `0.053603`, avg `0.016189`, median `0.01259`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.10749`, avg `0.037071`, median `0.052152`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015926`, avg `-0.002144`, median `0.001174`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.018668`, avg `-0.002782`, median `0.002614`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.01728`, avg `-0.000168`, median `-0.000315`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.045234`, avg `0.01702`, median `0.020913`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.092998`, avg `0.014529`, median `0.028478`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017856`, avg `-0.004568`, median `-0.007364`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.022763`, avg `-0.002532`, median `-0.006074`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.040275`, avg `-0.001604`, median `-0.004345`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.275`, primary_mae `0.061971`, avg `0.015359`, median `0.008277`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.25`, primary_mae `0.121982`, avg `0.059612`, median `0.068484`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.016891`, avg `-0.003356`, median `-0.003205`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4625`, primary_mae `0.020715`, avg `-0.002657`, median `0.000839`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.028778`, avg `-0.000886`, median `-0.000315`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.2875`, primary_mae `0.053603`, avg `0.016189`, median `0.01259`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.10749`, avg `0.037071`, median `0.052152`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.016891`, avg `-0.003356`, median `-0.003205`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4625`, primary_mae `0.020715`, avg `-0.002657`, median `0.000839`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.028778`, avg `-0.000886`, median `-0.000315`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.2875`, primary_mae `0.053603`, avg `0.016189`, median `0.01259`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.10749`, avg `0.037071`, median `0.052152`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
