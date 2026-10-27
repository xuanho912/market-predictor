# Historical Replay Benchmark

Generated at: `2026-10-27T18:04:15.639411+00:00`
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
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.016951`
- secondary_mean_absolute_error: `0.014652`
- primary_error_advantage: `-0.002299`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.021641`
- secondary_mean_absolute_error: `0.017361`
- primary_error_advantage: `-0.00428`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.03289`
- secondary_mean_absolute_error: `0.031925`
- primary_error_advantage: `-0.000965`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.051663`
- secondary_mean_absolute_error: `0.040151`
- primary_error_advantage: `-0.011512`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.072817`
- secondary_mean_absolute_error: `0.05661`
- primary_error_advantage: `-0.016207`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014543`, as_primary `0`, as_primary_hit `None`, avg `0.003957`, median `0.004638`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.018555`, as_primary `0`, as_primary_hit `None`, avg `0.006976`, median `0.006772`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.025679`, as_primary `0`, as_primary_hit `None`, avg `0.010341`, median `0.009023`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.032586`, as_primary `0`, as_primary_hit `None`, avg `0.016793`, median `0.019102`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.048175`, as_primary `0`, as_primary_hit `None`, avg `0.033859`, median `0.045278`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.015701`, as_primary `40`, as_primary_hit `0.55`, avg `0.003957`, median `0.004638`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.020118`, as_primary `40`, as_primary_hit `0.5`, avg `0.006976`, median `0.006772`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.032915`, as_primary `40`, as_primary_hit `0.575`, avg `0.010341`, median `0.009023`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.043987`, as_primary `40`, as_primary_hit `0.825`, avg `0.016793`, median `0.019102`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.053917`, as_primary `40`, as_primary_hit `0.775`, avg `0.033859`, median `0.045278`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.016038`, as_primary `40`, as_primary_hit `0.625`, avg `0.003957`, median `0.004638`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.018893`, as_primary `40`, as_primary_hit `0.7`, avg `0.006976`, median `0.006772`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.034476`, as_primary `40`, as_primary_hit `0.725`, avg `0.010341`, median `0.009023`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.052495`, as_primary `40`, as_primary_hit `0.575`, avg `0.016793`, median `0.019102`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.075963`, as_primary `40`, as_primary_hit `0.75`, avg `0.033859`, median `0.045278`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014163`, as_primary `0`, as_primary_hit `None`, avg `0.003957`, median `0.004638`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.017145`, as_primary `0`, as_primary_hit `None`, avg `0.006976`, median `0.006772`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.023555`, as_primary `0`, as_primary_hit `None`, avg `0.010341`, median `0.009023`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.030011`, as_primary `0`, as_primary_hit `None`, avg `0.016793`, median `0.019102`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.048724`, as_primary `0`, as_primary_hit `None`, avg `0.033859`, median `0.045278`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.4167`, primary_mae `0.015079`, avg `0.004571`, median `0.004638`
- 5d: sample `60`, primary_hit `0.4`, primary_closer `0.3667`, primary_mae `0.021756`, avg `0.007391`, median `0.006772`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.5167`, primary_mae `0.034643`, avg `0.011658`, median `0.009202`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.45`, primary_mae `0.054659`, avg `0.019847`, median `0.025176`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.4667`, primary_mae `0.0629`, avg `0.032941`, median `0.047453`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.022567`, avg `0.002112`, median `0.005065`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.021296`, avg `0.005731`, median `0.006972`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.027632`, avg `0.00639`, median `0.008601`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.042675`, avg `0.007631`, median `0.001221`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.102568`, avg `0.036613`, median `0.031522`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.022567`, avg `0.002112`, median `0.005065`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.021296`, avg `0.005731`, median `0.006972`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.027632`, avg `0.00639`, median `0.008601`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.042675`, avg `0.007631`, median `0.001221`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.102568`, avg `0.036613`, median `0.031522`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.4167`, primary_mae `0.015079`, avg `0.004571`, median `0.004638`
- 5d: sample `60`, primary_hit `0.4`, primary_closer `0.3667`, primary_mae `0.021756`, avg `0.007391`, median `0.006772`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.5167`, primary_mae `0.034643`, avg `0.011658`, median `0.009202`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.45`, primary_mae `0.054659`, avg `0.019847`, median `0.025176`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.4667`, primary_mae `0.0629`, avg `0.032941`, median `0.047453`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.015079, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.021296, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.027632, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.042675, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.0629, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014163, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016038, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.015079, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017145, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020118, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.021296, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023555, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034476, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.027632, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030011, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052495, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.042675, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048175, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075963, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.0629, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.02214`, avg `0.005635`, median `0.002901`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.030477`, avg `0.006385`, median `0.001226`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.040892`, avg `0.015161`, median `0.014259`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.038046`, avg `0.033414`, median `0.029911`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.625`, primary_mae `0.026414`, avg `0.067525`, median `0.070816`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.02129`, avg `0.006138`, median `0.002901`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.03042`, avg `0.005863`, median `0.003191`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.037733`, avg `0.018814`, median `0.014259`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.375`, primary_mae `0.035065`, avg `0.035927`, median `0.029994`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.75`, primary_mae `0.027994`, avg `0.07276`, median `0.086868`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.024069`, avg `0.001123`, median `-0.001683`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.020112`, avg `0.005349`, median `0.006972`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.025241`, avg `0.003355`, median `0.005647`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.038605`, avg `0.003359`, median `-0.008338`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.107026`, avg `0.038425`, median `0.031522`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.016951`, avg `0.003957`, median `0.004638`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.021641`, avg `0.006976`, median `0.006772`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.03289`, avg `0.010341`, median `0.009023`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.051663`, avg `0.016793`, median `0.019102`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.4125`, primary_mae `0.072817`, avg `0.033859`, median `0.045278`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.016951`, avg `0.003957`, median `0.004638`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.021641`, avg `0.006976`, median `0.006772`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.03289`, avg `0.010341`, median `0.009023`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.051663`, avg `0.016793`, median `0.019102`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.4125`, primary_mae `0.072817`, avg `0.033859`, median `0.045278`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.4167`, primary_mae `0.015079`, avg `0.004571`, median `0.004638`
- 5d: sample `60`, primary_hit `0.4`, primary_closer `0.3667`, primary_mae `0.021756`, avg `0.007391`, median `0.006772`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.5167`, primary_mae `0.034643`, avg `0.011658`, median `0.009202`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.45`, primary_mae `0.054659`, avg `0.019847`, median `0.025176`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.4667`, primary_mae `0.0629`, avg `0.032941`, median `0.047453`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.022567`, avg `0.002112`, median `0.005065`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.021296`, avg `0.005731`, median `0.006972`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.027632`, avg `0.00639`, median `0.008601`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.042675`, avg `0.007631`, median `0.001221`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.102568`, avg `0.036613`, median `0.031522`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.016951`, avg `0.003957`, median `0.004638`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.021641`, avg `0.006976`, median `0.006772`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.03289`, avg `0.010341`, median `0.009023`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.051663`, avg `0.016793`, median `0.019102`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.4125`, primary_mae `0.072817`, avg `0.033859`, median `0.045278`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.016951`, avg `0.003957`, median `0.004638`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.021641`, avg `0.006976`, median `0.006772`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.03289`, avg `0.010341`, median `0.009023`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.051663`, avg `0.016793`, median `0.019102`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.4125`, primary_mae `0.072817`, avg `0.033859`, median `0.045278`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
