# Historical Replay Benchmark

Generated at: `2026-06-15T17:17:04.751506+00:00`
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
- primary_mean_absolute_error: `0.014276`
- secondary_mean_absolute_error: `0.013051`
- primary_error_advantage: `-0.001225`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.019453`
- secondary_mean_absolute_error: `0.01599`
- primary_error_advantage: `-0.003463`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.029038`
- secondary_mean_absolute_error: `0.027229`
- primary_error_advantage: `-0.001809`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.051704`
- secondary_mean_absolute_error: `0.045683`
- primary_error_advantage: `-0.006021`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.07014`
- secondary_mean_absolute_error: `0.059811`
- primary_error_advantage: `-0.010329`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013163`, as_primary `0`, as_primary_hit `None`, avg `0.003936`, median `0.004555`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.016338`, as_primary `0`, as_primary_hit `None`, avg `0.0056`, median `0.005205`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.022237`, as_primary `0`, as_primary_hit `None`, avg `0.007395`, median `0.007534`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.033965`, as_primary `0`, as_primary_hit `None`, avg `0.007161`, median `0.01579`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.056524`, as_primary `0`, as_primary_hit `None`, avg `0.024832`, median `0.031374`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.014276`, as_primary `80`, as_primary_hit `0.6125`, avg `0.003936`, median `0.004555`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.019453`, as_primary `80`, as_primary_hit `0.6375`, avg `0.0056`, median `0.005205`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.029038`, as_primary `80`, as_primary_hit `0.6`, avg `0.007395`, median `0.007534`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.051704`, as_primary `80`, as_primary_hit `0.675`, avg `0.007161`, median `0.01579`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.07014`, as_primary `80`, as_primary_hit `0.5875`, avg `0.024832`, median `0.031374`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.013144`, as_primary `0`, as_primary_hit `None`, avg `0.003936`, median `0.004555`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.016549`, as_primary `0`, as_primary_hit `None`, avg `0.0056`, median `0.005205`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.029253`, as_primary `0`, as_primary_hit `None`, avg `0.007395`, median `0.007534`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.063892`, as_primary `0`, as_primary_hit `None`, avg `0.007161`, median `0.01579`
- 60d: sample `80`, direction_hit `0.4125`, path_mae `0.072905`, as_primary `0`, as_primary_hit `None`, avg `0.024832`, median `0.031374`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.012341`, as_primary `0`, as_primary_hit `None`, avg `0.003936`, median `0.004555`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.014736`, as_primary `0`, as_primary_hit `None`, avg `0.0056`, median `0.005205`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.021323`, as_primary `0`, as_primary_hit `None`, avg `0.007395`, median `0.007534`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.032841`, as_primary `0`, as_primary_hit `None`, avg `0.007161`, median `0.01579`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.053997`, as_primary `0`, as_primary_hit `None`, avg `0.024832`, median `0.031374`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.014276`, avg `0.003936`, median `0.004555`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3625`, primary_mae `0.019453`, avg `0.0056`, median `0.005205`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.029038`, avg `0.007395`, median `0.007534`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.3625`, primary_mae `0.051704`, avg `0.007161`, median `0.01579`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4125`, primary_mae `0.07014`, avg `0.024832`, median `0.031374`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.425`, primary_mae `0.01405`, avg `0.005724`, median `0.004633`
- 5d: sample `40`, primary_hit `0.775`, primary_closer `0.4`, primary_mae `0.017257`, avg `0.009631`, median `0.008615`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.575`, primary_mae `0.027145`, avg `0.007482`, median `0.008571`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.053989`, avg `0.000507`, median `0.01042`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.07428`, avg `0.006549`, median `-0.00576`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.014502`, avg `0.002147`, median `0.003745`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.02165`, avg `0.001569`, median `-0.000454`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.03093`, avg `0.007309`, median `0.006918`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.225`, primary_mae `0.049418`, avg `0.013814`, median `0.019428`
- 60d: sample `40`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.066`, avg `0.043115`, median `0.053882`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.01405, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.017257, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.027145, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.049418, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.066, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012341, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014276, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.01405, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014736, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019453, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.017257, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021323, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029253, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.027145, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032841, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.063892, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.049418, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053997, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072905, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.066, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.014963`, avg `-0.006356`, median `-0.005255`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.019403`, avg `-0.007284`, median `-0.010372`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.01491`, avg `0.005714`, median `0.006918`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.0`, primary_mae `0.02524`, avg `0.022118`, median `0.027661`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.052983`, avg `0.029911`, median `0.037982`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.015663`, avg `-0.003068`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.018223`, avg `-0.003972`, median `-0.007506`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.015353`, avg `0.007518`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.026474`, avg `0.0228`, median `0.028979`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.056387`, avg `0.036473`, median `0.055714`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.015663`, avg `-0.003068`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.018223`, avg `-0.003972`, median `-0.007506`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.015353`, avg `0.007518`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.026474`, avg `0.0228`, median `0.028979`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.056387`, avg `0.036473`, median `0.055714`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.014276`, avg `0.003936`, median `0.004555`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3625`, primary_mae `0.019453`, avg `0.0056`, median `0.005205`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.029038`, avg `0.007395`, median `0.007534`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.3625`, primary_mae `0.051704`, avg `0.007161`, median `0.01579`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4125`, primary_mae `0.07014`, avg `0.024832`, median `0.031374`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.014276`, avg `0.003936`, median `0.004555`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3625`, primary_mae `0.019453`, avg `0.0056`, median `0.005205`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.029038`, avg `0.007395`, median `0.007534`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.3625`, primary_mae `0.051704`, avg `0.007161`, median `0.01579`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4125`, primary_mae `0.07014`, avg `0.024832`, median `0.031374`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.014276`, avg `0.003936`, median `0.004555`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3625`, primary_mae `0.019453`, avg `0.0056`, median `0.005205`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.029038`, avg `0.007395`, median `0.007534`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.3625`, primary_mae `0.051704`, avg `0.007161`, median `0.01579`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4125`, primary_mae `0.07014`, avg `0.024832`, median `0.031374`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.014276`, avg `0.003936`, median `0.004555`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3625`, primary_mae `0.019453`, avg `0.0056`, median `0.005205`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.029038`, avg `0.007395`, median `0.007534`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.3625`, primary_mae `0.051704`, avg `0.007161`, median `0.01579`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4125`, primary_mae `0.07014`, avg `0.024832`, median `0.031374`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.014276`, avg `0.003936`, median `0.004555`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3625`, primary_mae `0.019453`, avg `0.0056`, median `0.005205`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.029038`, avg `0.007395`, median `0.007534`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.3625`, primary_mae `0.051704`, avg `0.007161`, median `0.01579`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4125`, primary_mae `0.07014`, avg `0.024832`, median `0.031374`

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
