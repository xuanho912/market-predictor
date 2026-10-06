# Historical Replay Benchmark

Generated at: `2026-10-06T02:36:17.114642+00:00`
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
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.017592`
- secondary_mean_absolute_error: `0.016726`
- primary_error_advantage: `-0.000866`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.025991`
- secondary_mean_absolute_error: `0.020517`
- primary_error_advantage: `-0.005474`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.043271`
- secondary_mean_absolute_error: `0.033318`
- primary_error_advantage: `-0.009953`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.07577`
- secondary_mean_absolute_error: `0.059402`
- primary_error_advantage: `-0.016368`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.25`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.5`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.087551`
- secondary_mean_absolute_error: `0.068672`
- primary_error_advantage: `-0.018879`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016289`, as_primary `0`, as_primary_hit `None`, avg `-0.007025`, median `-0.004066`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.020736`, as_primary `0`, as_primary_hit `None`, avg `-0.011012`, median `-0.007554`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.031094`, as_primary `0`, as_primary_hit `None`, avg `-0.013625`, median `-0.010657`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.043004`, as_primary `0`, as_primary_hit `None`, avg `-0.003616`, median `0.007967`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.063484`, as_primary `0`, as_primary_hit `None`, avg `0.030122`, median `0.045479`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016726`, as_primary `0`, as_primary_hit `None`, avg `-0.007025`, median `-0.004066`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.020405`, as_primary `0`, as_primary_hit `None`, avg `-0.011012`, median `-0.007554`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.03647`, as_primary `0`, as_primary_hit `None`, avg `-0.013625`, median `-0.010657`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.061696`, as_primary `0`, as_primary_hit `None`, avg `-0.003616`, median `0.007967`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.067506`, as_primary `0`, as_primary_hit `None`, avg `0.030122`, median `0.045479`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.017592`, as_primary `80`, as_primary_hit `0.4`, avg `-0.007025`, median `-0.004066`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.025991`, as_primary `80`, as_primary_hit `0.425`, avg `-0.011012`, median `-0.007554`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.043271`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.013625`, median `-0.010657`
- 20d: sample `80`, direction_hit `0.45`, path_mae `0.07577`, as_primary `80`, as_primary_hit `0.55`, avg `-0.003616`, median `0.007967`
- 60d: sample `80`, direction_hit `0.25`, path_mae `0.087551`, as_primary `80`, as_primary_hit `0.75`, avg `0.030122`, median `0.045479`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016244`, as_primary `0`, as_primary_hit `None`, avg `-0.007025`, median `-0.004066`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.020386`, as_primary `0`, as_primary_hit `None`, avg `-0.011012`, median `-0.007554`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.029539`, as_primary `0`, as_primary_hit `None`, avg `-0.013625`, median `-0.010657`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.042746`, as_primary `0`, as_primary_hit `None`, avg `-0.003616`, median `0.007967`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.065461`, as_primary `0`, as_primary_hit `None`, avg `0.030122`, median `0.045479`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.017592`, avg `-0.007025`, median `-0.004066`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.025991`, avg `-0.011012`, median `-0.007554`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.043271`, avg `-0.013625`, median `-0.010657`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.07577`, avg `-0.003616`, median `0.007967`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.087551`, avg `0.030122`, median `0.045479`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.017592`, avg `-0.007025`, median `-0.004066`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.025991`, avg `-0.011012`, median `-0.007554`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.043271`, avg `-0.013625`, median `-0.010657`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.07577`, avg `-0.003616`, median `0.007967`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.087551`, avg `0.030122`, median `0.045479`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017592, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.4875, 'primary_mean_absolute_error': 0.025991, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5875, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.043271, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.07577, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.087551, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016244, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017592, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017592, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020386, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025991, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.4875, 'primary_mean_absolute_error': 0.025991, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029539, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043271, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5875, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.043271, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042746, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07577, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.07577, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.5, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.063484, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.087551, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.087551, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.011513`, avg `-0.002548`, median `0.00021`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.75`, primary_mae `0.009727`, avg `0.001216`, median `0.005524`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.034574`, avg `0.006939`, median `0.011529`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.082898`, avg `0.014696`, median `0.033594`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.075758`, avg `0.044563`, median `0.044525`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.010152`, avg `-0.000475`, median `0.000125`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.6875`, primary_mae `0.010636`, avg `-0.001468`, median `0.002359`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.032401`, avg `0.00818`, median `0.010165`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.081746`, avg `0.016069`, median `0.029416`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.066674`, avg `0.030946`, median `0.041986`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.5625`, primary_mae `0.016356`, avg `-0.020788`, median `-0.019403`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.5`, primary_mae `0.027976`, avg `-0.025659`, median `-0.017304`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.043972`, avg `-0.02304`, median `-0.03486`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.078599`, avg `-0.013249`, median `-0.016989`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.101665`, avg `0.046167`, median `0.095444`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.017592`, avg `-0.007025`, median `-0.004066`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.025991`, avg `-0.011012`, median `-0.007554`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.043271`, avg `-0.013625`, median `-0.010657`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.07577`, avg `-0.003616`, median `0.007967`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.087551`, avg `0.030122`, median `0.045479`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.017592`, avg `-0.007025`, median `-0.004066`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.025991`, avg `-0.011012`, median `-0.007554`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.043271`, avg `-0.013625`, median `-0.010657`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.07577`, avg `-0.003616`, median `0.007967`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.087551`, avg `0.030122`, median `0.045479`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.45`, primary_mae `0.016055`, avg `-0.005761`, median `-0.003662`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.022384`, avg `-0.009331`, median `-0.005714`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.4`, primary_mae `0.043569`, avg `-0.009851`, median `-0.005578`
- 20d: sample `60`, primary_hit `0.4333`, primary_closer `0.4`, primary_mae `0.073991`, avg `-0.000851`, median `0.011992`
- 60d: sample `60`, primary_hit `0.2333`, primary_closer `0.3`, primary_mae `0.078204`, avg `0.038192`, median `0.048298`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.017592`, avg `-0.007025`, median `-0.004066`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.025991`, avg `-0.011012`, median `-0.007554`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.043271`, avg `-0.013625`, median `-0.010657`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.07577`, avg `-0.003616`, median `0.007967`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.087551`, avg `0.030122`, median `0.045479`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.017592`, avg `-0.007025`, median `-0.004066`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.025991`, avg `-0.011012`, median `-0.007554`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.043271`, avg `-0.013625`, median `-0.010657`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.07577`, avg `-0.003616`, median `0.007967`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.087551`, avg `0.030122`, median `0.045479`

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
