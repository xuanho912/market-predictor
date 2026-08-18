# Historical Replay Benchmark

Generated at: `2026-08-18T04:22:53.549544+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `60`
Historical replay grade: `FAIL`
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
- sample_size: `60`
- primary_hit_rate: `0.6167`
- secondary_hit_rate: `0.7167`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4333`
- primary_mean_absolute_error: `0.018997`
- secondary_mean_absolute_error: `0.016386`
- primary_error_advantage: `-0.002611`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 5d
- sample_size: `60`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6667`
- primary_vs_secondary_accuracy_spread: `-0.0667`
- primary_closer_than_secondary_rate: `0.4167`
- primary_mean_absolute_error: `0.027569`
- secondary_mean_absolute_error: `0.024654`
- primary_error_advantage: `-0.002915`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 10d
- sample_size: `60`
- primary_hit_rate: `0.6833`
- secondary_hit_rate: `0.7167`
- primary_vs_secondary_accuracy_spread: `-0.0333`
- primary_closer_than_secondary_rate: `0.4167`
- primary_mean_absolute_error: `0.03502`
- secondary_mean_absolute_error: `0.028588`
- primary_error_advantage: `-0.006432`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 20d
- sample_size: `60`
- primary_hit_rate: `0.6333`
- secondary_hit_rate: `0.9`
- primary_vs_secondary_accuracy_spread: `-0.2667`
- primary_closer_than_secondary_rate: `0.4667`
- primary_mean_absolute_error: `0.043128`
- secondary_mean_absolute_error: `0.043115`
- primary_error_advantage: `-1.3e-05`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 60d
- sample_size: `60`
- primary_hit_rate: `0.5833`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.1667`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.076545`
- secondary_mean_absolute_error: `0.077112`
- primary_error_advantage: `0.000567`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.7167`, path_mae `0.014164`, as_primary `0`, as_primary_hit `None`, avg `0.007726`, median `0.007355`
- 5d: sample `60`, direction_hit `0.6667`, path_mae `0.020606`, as_primary `0`, as_primary_hit `None`, avg `0.010155`, median `0.012522`
- 10d: sample `60`, direction_hit `0.7167`, path_mae `0.025858`, as_primary `0`, as_primary_hit `None`, avg `0.02069`, median `0.019243`
- 20d: sample `60`, direction_hit `0.9`, path_mae `0.036984`, as_primary `0`, as_primary_hit `None`, avg `0.03854`, median `0.031586`
- 60d: sample `60`, direction_hit `0.75`, path_mae `0.068572`, as_primary `0`, as_primary_hit `None`, avg `0.039412`, median `0.051138`

### bounce_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.7167`, path_mae `0.018044`, as_primary `40`, as_primary_hit `0.75`, avg `0.007726`, median `0.007355`
- 5d: sample `60`, direction_hit `0.6667`, path_mae `0.029707`, as_primary `40`, as_primary_hit `0.7`, avg `0.010155`, median `0.012522`
- 10d: sample `60`, direction_hit `0.7167`, path_mae `0.034294`, as_primary `40`, as_primary_hit `0.8`, avg `0.02069`, median `0.019243`
- 20d: sample `60`, direction_hit `0.9`, path_mae `0.053483`, as_primary `40`, as_primary_hit `0.9`, avg `0.03854`, median `0.031586`
- 60d: sample `60`, direction_hit `0.75`, path_mae `0.081599`, as_primary `40`, as_primary_hit `0.75`, avg `0.039412`, median `0.051138`

### failed_bounce_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.2833`, path_mae `0.022156`, as_primary `20`, as_primary_hit `0.65`, avg `0.007726`, median `0.007355`
- 5d: sample `60`, direction_hit `0.3333`, path_mae `0.029835`, as_primary `20`, as_primary_hit `0.6`, avg `0.010155`, median `0.012522`
- 10d: sample `60`, direction_hit `0.2833`, path_mae `0.032987`, as_primary `20`, as_primary_hit `0.55`, avg `0.02069`, median `0.019243`
- 20d: sample `60`, direction_hit `0.1`, path_mae `0.04145`, as_primary `20`, as_primary_hit `0.9`, avg `0.03854`, median `0.031586`
- 60d: sample `60`, direction_hit `0.25`, path_mae `0.089435`, as_primary `20`, as_primary_hit `0.75`, avg `0.039412`, median `0.051138`

### analog_average_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.7167`, path_mae `0.014268`, as_primary `0`, as_primary_hit `None`, avg `0.007726`, median `0.007355`
- 5d: sample `60`, direction_hit `0.6667`, path_mae `0.019781`, as_primary `0`, as_primary_hit `None`, avg `0.010155`, median `0.012522`
- 10d: sample `60`, direction_hit `0.7167`, path_mae `0.024217`, as_primary `0`, as_primary_hit `None`, avg `0.02069`, median `0.019243`
- 20d: sample `60`, direction_hit `0.9`, path_mae `0.028373`, as_primary `0`, as_primary_hit `None`, avg `0.03854`, median `0.031586`
- 60d: sample `60`, direction_hit `0.75`, path_mae `0.064373`, as_primary `0`, as_primary_hit `None`, avg `0.039412`, median `0.051138`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4333`, primary_mae `0.018997`, avg `0.007726`, median `0.007355`
- 5d: sample `60`, primary_hit `0.6`, primary_closer `0.4167`, primary_mae `0.027569`, avg `0.010155`, median `0.012522`
- 10d: sample `60`, primary_hit `0.6833`, primary_closer `0.4167`, primary_mae `0.03502`, avg `0.02069`, median `0.019243`
- 20d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.043128`, avg `0.03854`, median `0.031586`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.076545`, avg `0.039412`, median `0.051138`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4333`, primary_mae `0.018997`, avg `0.007726`, median `0.007355`
- 5d: sample `60`, primary_hit `0.6`, primary_closer `0.4167`, primary_mae `0.027569`, avg `0.010155`, median `0.012522`
- 10d: sample `60`, primary_hit `0.6833`, primary_closer `0.4167`, primary_mae `0.03502`, avg `0.02069`, median `0.019243`
- 20d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.043128`, avg `0.03854`, median `0.031586`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.076545`, avg `0.039412`, median `0.051138`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.018997, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.027569, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.03502, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.043128, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.076545, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6167, 'secondary_hit_rate': 0.7167, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4333, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 60, 'path_mean_absolute_error': 0.014164, 'direction_hit_rate': 0.7167}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.022156, 'direction_hit_rate': 0.2833}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.018997, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6667, 'primary_vs_secondary_accuracy_spread': -0.0667, 'primary_closer_than_secondary_rate': 0.4167, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.019781, 'direction_hit_rate': 0.6667}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.029835, 'direction_hit_rate': 0.3333}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.027569, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6833, 'secondary_hit_rate': 0.7167, 'primary_vs_secondary_accuracy_spread': -0.0333, 'primary_closer_than_secondary_rate': 0.4167, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.024217, 'direction_hit_rate': 0.7167}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.034294, 'direction_hit_rate': 0.7167}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.03502, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6333, 'secondary_hit_rate': 0.9, 'primary_vs_secondary_accuracy_spread': -0.2667, 'primary_closer_than_secondary_rate': 0.4667, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.028373, 'direction_hit_rate': 0.9}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.053483, 'direction_hit_rate': 0.9}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.043128, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5833, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.1667, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.064373, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.089435, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.076545, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `6`
- 3d: sample `6`, primary_hit `0.6667`, primary_closer `0.6667`, primary_mae `0.018788`, avg `-0.001592`, median `-0.002451`
- 5d: sample `6`, primary_hit `0.8333`, primary_closer `1.0`, primary_mae `0.011468`, avg `-0.01503`, median `-0.016428`
- 10d: sample `6`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.014212`, avg `-0.01096`, median `-0.010564`
- 20d: sample `6`, primary_hit `0.0`, primary_closer `1.0`, primary_mae `0.018301`, avg `0.025573`, median `0.02865`
- 60d: sample `6`, primary_hit `0.1667`, primary_closer `1.0`, primary_mae `0.056719`, avg `0.004604`, median `0.029695`

### top_20
- sample_size: `12`
- 3d: sample `12`, primary_hit `0.5`, primary_closer `0.5833`, primary_mae `0.023638`, avg `0.001294`, median `0.000551`
- 5d: sample `12`, primary_hit `0.5`, primary_closer `0.6667`, primary_mae `0.025951`, avg `0.003398`, median `-0.002828`
- 10d: sample `12`, primary_hit `0.6667`, primary_closer `0.6667`, primary_mae `0.03894`, avg `0.009018`, median `-0.006988`
- 20d: sample `12`, primary_hit `0.1667`, primary_closer `0.75`, primary_mae `0.047851`, avg `0.049695`, median `0.032633`
- 60d: sample `12`, primary_hit `0.25`, primary_closer `0.6667`, primary_mae `0.100797`, avg `0.044605`, median `0.030631`

### bottom_20
- sample_size: `12`
- 3d: sample `12`, primary_hit `0.5`, primary_closer `0.5833`, primary_mae `0.023638`, avg `0.001294`, median `0.000551`
- 5d: sample `12`, primary_hit `0.5`, primary_closer `0.6667`, primary_mae `0.025951`, avg `0.003398`, median `-0.002828`
- 10d: sample `12`, primary_hit `0.6667`, primary_closer `0.6667`, primary_mae `0.03894`, avg `0.009018`, median `-0.006988`
- 20d: sample `12`, primary_hit `0.1667`, primary_closer `0.75`, primary_mae `0.047851`, avg `0.049695`, median `0.032633`
- 60d: sample `12`, primary_hit `0.25`, primary_closer `0.6667`, primary_mae `0.100797`, avg `0.044605`, median `0.030631`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4333`, primary_mae `0.018997`, avg `0.007726`, median `0.007355`
- 5d: sample `60`, primary_hit `0.6`, primary_closer `0.4167`, primary_mae `0.027569`, avg `0.010155`, median `0.012522`
- 10d: sample `60`, primary_hit `0.6833`, primary_closer `0.4167`, primary_mae `0.03502`, avg `0.02069`, median `0.019243`
- 20d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.043128`, avg `0.03854`, median `0.031586`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.076545`, avg `0.039412`, median `0.051138`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4333`, primary_mae `0.018997`, avg `0.007726`, median `0.007355`
- 5d: sample `60`, primary_hit `0.6`, primary_closer `0.4167`, primary_mae `0.027569`, avg `0.010155`, median `0.012522`
- 10d: sample `60`, primary_hit `0.6833`, primary_closer `0.4167`, primary_mae `0.03502`, avg `0.02069`, median `0.019243`
- 20d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.043128`, avg `0.03854`, median `0.031586`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.076545`, avg `0.039412`, median `0.051138`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.8`, primary_closer `0.5`, primary_mae `0.005907`, avg `0.005021`, median `0.005602`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.011957`, avg `0.009975`, median `0.011847`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.45`, primary_mae `0.011955`, avg `0.016016`, median `0.017776`
- 20d: sample `20`, primary_hit `1.0`, primary_closer `0.35`, primary_mae `0.015615`, avg `0.030699`, median `0.032326`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.4`, primary_mae `0.029845`, avg `0.055448`, median `0.056479`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.028276`, avg `0.008833`, median `0.012771`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.031742`, avg `0.011208`, median `0.008491`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.052234`, avg `0.024212`, median `0.027698`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.75`, primary_mae `0.057005`, avg `0.06102`, median `0.046481`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.6`, primary_mae `0.109903`, avg `0.046573`, median `0.041986`

### options_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4333`, primary_mae `0.018997`, avg `0.007726`, median `0.007355`
- 5d: sample `60`, primary_hit `0.6`, primary_closer `0.4167`, primary_mae `0.027569`, avg `0.010155`, median `0.012522`
- 10d: sample `60`, primary_hit `0.6833`, primary_closer `0.4167`, primary_mae `0.03502`, avg `0.02069`, median `0.019243`
- 20d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.043128`, avg `0.03854`, median `0.031586`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.076545`, avg `0.039412`, median `0.051138`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4333`, primary_mae `0.018997`, avg `0.007726`, median `0.007355`
- 5d: sample `60`, primary_hit `0.6`, primary_closer `0.4167`, primary_mae `0.027569`, avg `0.010155`, median `0.012522`
- 10d: sample `60`, primary_hit `0.6833`, primary_closer `0.4167`, primary_mae `0.03502`, avg `0.02069`, median `0.019243`
- 20d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.043128`, avg `0.03854`, median `0.031586`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.076545`, avg `0.039412`, median `0.051138`

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
