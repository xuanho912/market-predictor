# Historical Replay Benchmark

Generated at: `2026-11-05T01:56:17.805997+00:00`
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
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.019353`
- secondary_mean_absolute_error: `0.022071`
- primary_error_advantage: `0.002718`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.65`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.029181`
- secondary_mean_absolute_error: `0.029995`
- primary_error_advantage: `0.000814`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.049943`
- secondary_mean_absolute_error: `0.049766`
- primary_error_advantage: `-0.000177`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.625`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.06746`
- secondary_mean_absolute_error: `0.06264`
- primary_error_advantage: `-0.00482`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.575`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.048526`
- secondary_mean_absolute_error: `0.048649`
- primary_error_advantage: `0.000123`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.575`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.01899`, as_primary `0`, as_primary_hit `None`, avg `0.004828`, median `0.009346`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.025913`, as_primary `0`, as_primary_hit `None`, avg `0.001975`, median `0.005155`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.039541`, as_primary `0`, as_primary_hit `None`, avg `-0.003825`, median `-0.003821`
- 20d: sample `80`, direction_hit `0.4625`, path_mae `0.043445`, as_primary `0`, as_primary_hit `None`, avg `-0.011146`, median `-0.017646`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.043966`, as_primary `0`, as_primary_hit `None`, avg `0.063218`, median `0.065892`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.020813`, as_primary `20`, as_primary_hit `0.65`, avg `0.004828`, median `0.009346`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.030657`, as_primary `20`, as_primary_hit `0.65`, avg `0.001975`, median `0.005155`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.05143`, as_primary `20`, as_primary_hit `0.55`, avg `-0.003825`, median `-0.003821`
- 20d: sample `80`, direction_hit `0.4625`, path_mae `0.06593`, as_primary `20`, as_primary_hit `0.5`, avg `-0.011146`, median `-0.017646`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.051276`, as_primary `20`, as_primary_hit `0.95`, avg `0.063218`, median `0.065892`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.020604`, as_primary `60`, as_primary_hit `0.6167`, avg `0.004828`, median `0.009346`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.029245`, as_primary `60`, as_primary_hit `0.5333`, avg `0.001975`, median `0.005155`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.052617`, as_primary `60`, as_primary_hit `0.4667`, avg `-0.003825`, median `-0.003821`
- 20d: sample `80`, direction_hit `0.5375`, path_mae `0.071197`, as_primary `60`, as_primary_hit `0.45`, avg `-0.011146`, median `-0.017646`
- 60d: sample `80`, direction_hit `0.1625`, path_mae `0.046711`, as_primary `60`, as_primary_hit `0.8`, avg `0.063218`, median `0.065892`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.019011`, as_primary `0`, as_primary_hit `None`, avg `0.004828`, median `0.009346`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.025292`, as_primary `0`, as_primary_hit `None`, avg `0.001975`, median `0.005155`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.038396`, as_primary `0`, as_primary_hit `None`, avg `-0.003825`, median `-0.003821`
- 20d: sample `80`, direction_hit `0.4625`, path_mae `0.043506`, as_primary `0`, as_primary_hit `None`, avg `-0.011146`, median `-0.017646`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.042033`, as_primary `0`, as_primary_hit `None`, avg `0.063218`, median `0.065892`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.019353`, avg `0.004828`, median `0.009346`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.029181`, avg `0.001975`, median `0.005155`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.049943`, avg `-0.003825`, median `-0.003821`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.06746`, avg `-0.011146`, median `-0.017646`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.048526`, avg `0.063218`, median `0.065892`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.65`, primary_mae `0.015895`, avg `0.003221`, median `0.007717`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.55`, primary_mae `0.024845`, avg `0.000386`, median `0.001372`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.038115`, avg `-0.005618`, median `-0.017149`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.575`, primary_mae `0.060348`, avg `-0.014161`, median `-0.022521`
- 60d: sample `40`, primary_hit `0.675`, primary_closer `0.575`, primary_mae `0.038573`, avg `0.040648`, median `0.045791`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.027946`, avg `0.00482`, median `0.011174`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.038429`, avg `0.001902`, median `0.008409`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.062187`, avg `0.001156`, median `0.008601`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.066916`, avg `-0.00797`, median `-0.008361`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.35`, primary_mae `0.048032`, avg `0.105937`, median `0.105065`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.017676`, avg `0.008051`, median `0.00957`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.028606`, avg `0.005225`, median `0.003858`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.061355`, avg `-0.005218`, median `-0.000815`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.082228`, avg `-0.008291`, median `0.014674`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.068926`, avg `0.065641`, median `0.091555`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.015895, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.024845, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.038115, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.060348, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.038573, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01899, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020813, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.015895, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025292, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030657, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.024845, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038396, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052617, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.038115, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043445, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071197, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.060348, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042033, 'direction_hit_rate': 0.8375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051276, 'direction_hit_rate': 0.8375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.038573, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.01986`, avg `0.004536`, median `0.008001`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.033555`, avg `0.003249`, median `0.00149`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.048289`, avg `0.002268`, median `0.004277`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.06794`, avg `-0.004281`, median `-0.002353`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.045209`, avg `0.052016`, median `0.067424`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.02065`, avg `0.001539`, median `0.010214`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.034446`, avg `0.000497`, median `0.001372`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.052004`, avg `0.00047`, median `-0.008604`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.080567`, avg `-0.016908`, median `-0.02913`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.045596`, avg `0.055811`, median `0.057737`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.026329`, avg `0.007844`, median `0.012755`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.036111`, avg `0.006126`, median `0.010244`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.06143`, avg `-0.001793`, median `0.008601`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.059984`, avg `-0.01577`, median `-0.017646`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.3125`, primary_mae `0.049563`, avg `0.110156`, median `0.105065`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.019353`, avg `0.004828`, median `0.009346`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.029181`, avg `0.001975`, median `0.005155`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.049943`, avg `-0.003825`, median `-0.003821`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.06746`, avg `-0.011146`, median `-0.017646`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.048526`, avg `0.063218`, median `0.065892`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.019353`, avg `0.004828`, median `0.009346`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.029181`, avg `0.001975`, median `0.005155`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.049943`, avg `-0.003825`, median `-0.003821`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.06746`, avg `-0.011146`, median `-0.017646`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.048526`, avg `0.063218`, median `0.065892`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.6167`, primary_mae `0.016489`, avg `0.004831`, median `0.008503`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.5333`, primary_mae `0.026099`, avg `0.001999`, median `0.001561`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.55`, primary_mae `0.045862`, avg `-0.005485`, median `-0.010602`
- 20d: sample `60`, primary_hit `0.55`, primary_closer `0.5167`, primary_mae `0.067641`, avg `-0.012205`, median `-0.020205`
- 60d: sample `60`, primary_hit `0.5167`, primary_closer `0.5167`, primary_mae `0.048691`, avg `0.048979`, median `0.054327`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.027946`, avg `0.00482`, median `0.011174`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.038429`, avg `0.001902`, median `0.008409`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.062187`, avg `0.001156`, median `0.008601`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.066916`, avg `-0.00797`, median `-0.008361`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.35`, primary_mae `0.048032`, avg `0.105937`, median `0.105065`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.019353`, avg `0.004828`, median `0.009346`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.029181`, avg `0.001975`, median `0.005155`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.049943`, avg `-0.003825`, median `-0.003821`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.06746`, avg `-0.011146`, median `-0.017646`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.048526`, avg `0.063218`, median `0.065892`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.019353`, avg `0.004828`, median `0.009346`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.029181`, avg `0.001975`, median `0.005155`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.049943`, avg `-0.003825`, median `-0.003821`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.06746`, avg `-0.011146`, median `-0.017646`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.048526`, avg `0.063218`, median `0.065892`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.019353`, avg `0.004828`, median `0.009346`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.029181`, avg `0.001975`, median `0.005155`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4875`, primary_mae `0.049943`, avg `-0.003825`, median `-0.003821`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.06746`, avg `-0.011146`, median `-0.017646`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.048526`, avg `0.063218`, median `0.065892`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
