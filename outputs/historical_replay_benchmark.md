# Historical Replay Benchmark

Generated at: `2026-06-15T13:43:10.443649+00:00`
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
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.013841`
- secondary_mean_absolute_error: `0.012561`
- primary_error_advantage: `-0.00128`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.35`
- primary_vs_secondary_accuracy_spread: `0.275`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.019745`
- secondary_mean_absolute_error: `0.015478`
- primary_error_advantage: `-0.004267`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.032059`
- secondary_mean_absolute_error: `0.027462`
- primary_error_advantage: `-0.004597`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.051897`
- secondary_mean_absolute_error: `0.050749`
- primary_error_advantage: `-0.001148`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.068593`
- secondary_mean_absolute_error: `0.058481`
- primary_error_advantage: `-0.010112`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.012732`, as_primary `0`, as_primary_hit `None`, avg `0.003805`, median `0.004633`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.016228`, as_primary `0`, as_primary_hit `None`, avg `0.004575`, median `0.004631`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.023838`, as_primary `0`, as_primary_hit `None`, avg `0.004325`, median `0.005826`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.034454`, as_primary `0`, as_primary_hit `None`, avg `0.005397`, median `0.015757`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.054779`, as_primary `0`, as_primary_hit `None`, avg `0.023263`, median `0.029874`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013841`, as_primary `80`, as_primary_hit `0.6125`, avg `0.003805`, median `0.004633`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.019745`, as_primary `80`, as_primary_hit `0.625`, avg `0.004575`, median `0.004631`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.032059`, as_primary `80`, as_primary_hit `0.5625`, avg `0.004325`, median `0.005826`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.051897`, as_primary `80`, as_primary_hit `0.65`, avg `0.005397`, median `0.015757`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.068593`, as_primary `80`, as_primary_hit `0.5625`, avg `0.023263`, median `0.029874`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.012745`, as_primary `0`, as_primary_hit `None`, avg `0.003805`, median `0.004633`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.015754`, as_primary `0`, as_primary_hit `None`, avg `0.004575`, median `0.004631`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.028113`, as_primary `0`, as_primary_hit `None`, avg `0.004325`, median `0.005826`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.059761`, as_primary `0`, as_primary_hit `None`, avg `0.005397`, median `0.015757`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.067678`, as_primary `0`, as_primary_hit `None`, avg `0.023263`, median `0.029874`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.012106`, as_primary `0`, as_primary_hit `None`, avg `0.003805`, median `0.004633`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.014638`, as_primary `0`, as_primary_hit `None`, avg `0.004575`, median `0.004631`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.022613`, as_primary `0`, as_primary_hit `None`, avg `0.004325`, median `0.005826`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.032393`, as_primary `0`, as_primary_hit `None`, avg `0.005397`, median `0.015757`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.05225`, as_primary `0`, as_primary_hit `None`, avg `0.023263`, median `0.029874`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.013841`, avg `0.003805`, median `0.004633`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.019745`, avg `0.004575`, median `0.004631`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.032059`, avg `0.004325`, median `0.005826`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.051897`, avg `0.005397`, median `0.015757`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.068593`, avg `0.023263`, median `0.029874`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.014833`, avg `0.004228`, median `0.002075`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.016206`, avg `0.006039`, median `0.004845`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.016235`, avg `0.007908`, median `0.008571`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.7`, primary_mae `0.042243`, avg `0.008271`, median `0.012734`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.063899`, avg `-0.00807`, median `-0.018485`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6333`, primary_closer `0.45`, primary_mae `0.01351`, avg `0.003664`, median `0.006469`
- 5d: sample `60`, primary_hit `0.5833`, primary_closer `0.3333`, primary_mae `0.020925`, avg `0.004087`, median `0.004573`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.037333`, avg `0.003131`, median `0.005103`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.3667`, primary_mae `0.055115`, avg `0.00444`, median `0.017134`
- 60d: sample `60`, primary_hit `0.6333`, primary_closer `0.3833`, primary_mae `0.070157`, avg `0.033708`, median `0.040333`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.016206, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.016235, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.042243, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.063899, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012106, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013841, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.35, 'primary_vs_secondary_accuracy_spread': 0.275, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014638, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019745, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.016206, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022613, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032059, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.016235, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032393, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059761, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.042243, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05225, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.068593, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.063899, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.013881`, avg `-0.007791`, median `-0.007158`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.015631`, avg `-0.011833`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.012386`, avg `0.008706`, median `0.006918`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.125`, primary_mae `0.015756`, avg `0.028852`, median `0.030181`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.032369`, avg `0.054535`, median `0.055714`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.014561`, avg `-0.005398`, median `-0.006238`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.015039`, avg `-0.005107`, median `-0.007506`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.015222`, avg `0.008574`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.024104`, avg `0.022746`, median `0.028979`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.053134`, avg `0.027526`, median `0.033759`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.014561`, avg `-0.005398`, median `-0.006238`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.015039`, avg `-0.005107`, median `-0.007506`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.015222`, avg `0.008574`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.024104`, avg `0.022746`, median `0.028979`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.053134`, avg `0.027526`, median `0.033759`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.013841`, avg `0.003805`, median `0.004633`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.019745`, avg `0.004575`, median `0.004631`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.032059`, avg `0.004325`, median `0.005826`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.051897`, avg `0.005397`, median `0.015757`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.068593`, avg `0.023263`, median `0.029874`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.013841`, avg `0.003805`, median `0.004633`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.019745`, avg `0.004575`, median `0.004631`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.032059`, avg `0.004325`, median `0.005826`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.051897`, avg `0.005397`, median `0.015757`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.068593`, avg `0.023263`, median `0.029874`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.013841`, avg `0.003805`, median `0.004633`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.019745`, avg `0.004575`, median `0.004631`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.032059`, avg `0.004325`, median `0.005826`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.051897`, avg `0.005397`, median `0.015757`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.068593`, avg `0.023263`, median `0.029874`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.013841`, avg `0.003805`, median `0.004633`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.019745`, avg `0.004575`, median `0.004631`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.032059`, avg `0.004325`, median `0.005826`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.051897`, avg `0.005397`, median `0.015757`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.068593`, avg `0.023263`, median `0.029874`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.013841`, avg `0.003805`, median `0.004633`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.019745`, avg `0.004575`, median `0.004631`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.032059`, avg `0.004325`, median `0.005826`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.051897`, avg `0.005397`, median `0.015757`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.068593`, avg `0.023263`, median `0.029874`

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
