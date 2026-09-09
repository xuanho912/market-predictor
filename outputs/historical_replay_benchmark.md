# Historical Replay Benchmark

Generated at: `2026-09-09T01:14:23.205095+00:00`
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
- primary_hit_rate: `0.2625`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.475`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.024571`
- secondary_mean_absolute_error: `0.016672`
- primary_error_advantage: `-0.007899`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.325`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.25`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.5`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.027559`
- secondary_mean_absolute_error: `0.020569`
- primary_error_advantage: `-0.00699`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.0449`
- secondary_mean_absolute_error: `0.03441`
- primary_error_advantage: `-0.01049`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3625`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.063514`
- secondary_mean_absolute_error: `0.044735`
- primary_error_advantage: `-0.018779`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3375`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.225`
- secondary_hit_rate: `0.775`
- primary_vs_secondary_accuracy_spread: `-0.55`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.0766`
- secondary_mean_absolute_error: `0.052081`
- primary_error_advantage: `-0.024519`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3125`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7375`, path_mae `0.016077`, as_primary `0`, as_primary_hit `None`, avg `0.009403`, median `0.012554`
- 5d: sample `80`, direction_hit `0.75`, path_mae `0.018818`, as_primary `0`, as_primary_hit `None`, avg `0.012397`, median `0.014719`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.029717`, as_primary `0`, as_primary_hit `None`, avg `0.014665`, median `0.020836`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.041806`, as_primary `0`, as_primary_hit `None`, avg `0.027639`, median `0.030996`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.054442`, as_primary `0`, as_primary_hit `None`, avg `0.061001`, median `0.069591`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7375`, path_mae `0.016773`, as_primary `0`, as_primary_hit `None`, avg `0.009403`, median `0.012554`
- 5d: sample `80`, direction_hit `0.75`, path_mae `0.022877`, as_primary `0`, as_primary_hit `None`, avg `0.012397`, median `0.014719`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.037012`, as_primary `0`, as_primary_hit `None`, avg `0.014665`, median `0.020836`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.058168`, as_primary `0`, as_primary_hit `None`, avg `0.027639`, median `0.030996`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.054884`, as_primary `0`, as_primary_hit `None`, avg `0.061001`, median `0.069591`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.2625`, path_mae `0.024571`, as_primary `80`, as_primary_hit `0.7375`, avg `0.009403`, median `0.012554`
- 5d: sample `80`, direction_hit `0.25`, path_mae `0.027559`, as_primary `80`, as_primary_hit `0.75`, avg `0.012397`, median `0.014719`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.0449`, as_primary `80`, as_primary_hit `0.6625`, avg `0.014665`, median `0.020836`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.063514`, as_primary `80`, as_primary_hit `0.725`, avg `0.027639`, median `0.030996`
- 60d: sample `80`, direction_hit `0.225`, path_mae `0.0766`, as_primary `80`, as_primary_hit `0.775`, avg `0.061001`, median `0.069591`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7375`, path_mae `0.015926`, as_primary `0`, as_primary_hit `None`, avg `0.009403`, median `0.012554`
- 5d: sample `80`, direction_hit `0.75`, path_mae `0.018531`, as_primary `0`, as_primary_hit `None`, avg `0.012397`, median `0.014719`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.030073`, as_primary `0`, as_primary_hit `None`, avg `0.014665`, median `0.020836`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.038165`, as_primary `0`, as_primary_hit `None`, avg `0.027639`, median `0.030996`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.053259`, as_primary `0`, as_primary_hit `None`, avg `0.061001`, median `0.069591`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.2625`, primary_closer `0.325`, primary_mae `0.024571`, avg `0.009403`, median `0.012554`
- 5d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.027559`, avg `0.012397`, median `0.014719`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.3625`, primary_mae `0.0449`, avg `0.014665`, median `0.020836`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.063514`, avg `0.027639`, median `0.030996`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3125`, primary_mae `0.0766`, avg `0.061001`, median `0.069591`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.016065`, avg `0.002976`, median `0.006198`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.019561`, avg `0.001476`, median `0.006661`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.034195`, avg `-0.009403`, median `-0.010529`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.063145`, avg `-0.001329`, median `0.011795`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.045598`, avg `0.030834`, median `0.039962`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.2333`, primary_closer `0.3167`, primary_mae `0.027407`, avg `0.011545`, median `0.017216`
- 5d: sample `60`, primary_hit `0.1833`, primary_closer `0.35`, primary_mae `0.030225`, avg `0.016038`, median `0.01826`
- 10d: sample `60`, primary_hit `0.2667`, primary_closer `0.3167`, primary_mae `0.048469`, avg `0.022688`, median `0.028836`
- 20d: sample `60`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.063637`, avg `0.037295`, median `0.034838`
- 60d: sample `60`, primary_hit `0.1833`, primary_closer `0.2667`, primary_mae `0.086935`, avg `0.071056`, median `0.083815`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.016065, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019561, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.034195, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.063145, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.045598, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.475, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015926, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024571, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.016065, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.5, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018531, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027559, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019561, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029717, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0449, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.034195, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038165, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.063514, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.063145, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.225, 'secondary_hit_rate': 0.775, 'primary_vs_secondary_accuracy_spread': -0.55, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053259, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0766, 'direction_hit_rate': 0.225}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.045598, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.040614`, avg `-0.007348`, median `0.001503`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.040691`, avg `-0.003974`, median `-0.005864`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.053621`, avg `0.001997`, median `-0.00147`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.049746`, avg `0.008006`, median `0.005403`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.081042`, avg `-0.030549`, median `-0.014872`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.044482`, avg `0.001708`, median `0.00781`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.04516`, avg `0.003684`, median `0.010362`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.05634`, avg `0.005307`, median `0.008121`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.054794`, avg `0.010231`, median `0.013236`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.113509`, avg `0.021389`, median `0.061361`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.0625`, primary_closer `0.25`, primary_mae `0.017716`, avg `0.020364`, median `0.020771`
- 5d: sample `16`, primary_hit `0.0625`, primary_closer `0.25`, primary_mae `0.025807`, avg `0.02858`, median `0.027685`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.050445`, avg `0.043808`, median `0.047952`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.25`, primary_mae `0.081227`, avg `0.071377`, median `0.056024`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.375`, primary_mae `0.086506`, avg `0.10268`, median `0.147302`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.2625`, primary_closer `0.325`, primary_mae `0.024571`, avg `0.009403`, median `0.012554`
- 5d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.027559`, avg `0.012397`, median `0.014719`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.3625`, primary_mae `0.0449`, avg `0.014665`, median `0.020836`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.063514`, avg `0.027639`, median `0.030996`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3125`, primary_mae `0.0766`, avg `0.061001`, median `0.069591`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.2625`, primary_closer `0.325`, primary_mae `0.024571`, avg `0.009403`, median `0.012554`
- 5d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.027559`, avg `0.012397`, median `0.014719`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.3625`, primary_mae `0.0449`, avg `0.014665`, median `0.020836`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.063514`, avg `0.027639`, median `0.030996`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3125`, primary_mae `0.0766`, avg `0.061001`, median `0.069591`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.016065`, avg `0.002976`, median `0.006198`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.019561`, avg `0.001476`, median `0.006661`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.034195`, avg `-0.009403`, median `-0.010529`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.063145`, avg `-0.001329`, median `0.011795`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.045598`, avg `0.030834`, median `0.039962`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.175`, primary_closer `0.3`, primary_mae `0.018194`, avg `0.01527`, median `0.018532`
- 5d: sample `40`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.021498`, avg `0.020571`, median `0.023346`
- 10d: sample `40`, primary_hit `0.225`, primary_closer `0.275`, primary_mae `0.041436`, avg `0.02797`, median `0.034294`
- 20d: sample `40`, primary_hit `0.15`, primary_closer `0.225`, primary_mae `0.065901`, avg `0.048364`, median `0.046213`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.275`, primary_mae `0.06946`, avg `0.089755`, median `0.098004`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.2625`, primary_closer `0.325`, primary_mae `0.024571`, avg `0.009403`, median `0.012554`
- 5d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.027559`, avg `0.012397`, median `0.014719`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.3625`, primary_mae `0.0449`, avg `0.014665`, median `0.020836`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.063514`, avg `0.027639`, median `0.030996`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3125`, primary_mae `0.0766`, avg `0.061001`, median `0.069591`

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
