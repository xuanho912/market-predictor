# Historical Replay Benchmark

Generated at: `2026-10-02T01:37:33.911541+00:00`
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
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.017408`
- secondary_mean_absolute_error: `0.015899`
- primary_error_advantage: `-0.001509`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.019691`
- secondary_mean_absolute_error: `0.017657`
- primary_error_advantage: `-0.002034`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.023054`
- secondary_mean_absolute_error: `0.022344`
- primary_error_advantage: `-0.00071`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.25`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.5`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.051013`
- secondary_mean_absolute_error: `0.032126`
- primary_error_advantage: `-0.018887`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.0875`
- secondary_hit_rate: `0.9125`
- primary_vs_secondary_accuracy_spread: `-0.825`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.045403`
- secondary_mean_absolute_error: `0.040237`
- primary_error_advantage: `-0.005166`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.016044`, as_primary `0`, as_primary_hit `None`, avg `-0.001134`, median `-0.001263`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018742`, as_primary `0`, as_primary_hit `None`, avg `-0.000584`, median `-0.003529`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.024164`, as_primary `0`, as_primary_hit `None`, avg `0.004225`, median `0.006554`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.034602`, as_primary `0`, as_primary_hit `None`, avg `0.027474`, median `0.033434`
- 60d: sample `80`, direction_hit `0.9125`, path_mae `0.041406`, as_primary `0`, as_primary_hit `None`, avg `0.094628`, median `0.113154`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.016894`, as_primary `0`, as_primary_hit `None`, avg `-0.001134`, median `-0.001263`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.020314`, as_primary `0`, as_primary_hit `None`, avg `-0.000584`, median `-0.003529`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.026719`, as_primary `0`, as_primary_hit `None`, avg `0.004225`, median `0.006554`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.050667`, as_primary `0`, as_primary_hit `None`, avg `0.027474`, median `0.033434`
- 60d: sample `80`, direction_hit `0.9125`, path_mae `0.046754`, as_primary `0`, as_primary_hit `None`, avg `0.094628`, median `0.113154`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.017408`, as_primary `80`, as_primary_hit `0.475`, avg `-0.001134`, median `-0.001263`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.019691`, as_primary `80`, as_primary_hit `0.45`, avg `-0.000584`, median `-0.003529`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.023054`, as_primary `80`, as_primary_hit `0.6`, avg `0.004225`, median `0.006554`
- 20d: sample `80`, direction_hit `0.25`, path_mae `0.051013`, as_primary `80`, as_primary_hit `0.75`, avg `0.027474`, median `0.033434`
- 60d: sample `80`, direction_hit `0.0875`, path_mae `0.045403`, as_primary `80`, as_primary_hit `0.9125`, avg `0.094628`, median `0.113154`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.015899`, as_primary `0`, as_primary_hit `None`, avg `-0.001134`, median `-0.001263`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.017657`, as_primary `0`, as_primary_hit `None`, avg `-0.000584`, median `-0.003529`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.022344`, as_primary `0`, as_primary_hit `None`, avg `0.004225`, median `0.006554`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.032126`, as_primary `0`, as_primary_hit `None`, avg `0.027474`, median `0.033434`
- 60d: sample `80`, direction_hit `0.9125`, path_mae `0.040237`, as_primary `0`, as_primary_hit `None`, avg `0.094628`, median `0.113154`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.017408`, avg `-0.001134`, median `-0.001263`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.019691`, avg `-0.000584`, median `-0.003529`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.4375`, primary_mae `0.023054`, avg `0.004225`, median `0.006554`
- 20d: sample `80`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.051013`, avg `0.027474`, median `0.033434`
- 60d: sample `80`, primary_hit `0.0875`, primary_closer `0.4625`, primary_mae `0.045403`, avg `0.094628`, median `0.113154`

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
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.022572`, avg `-0.004632`, median `-0.006398`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.021499`, avg `-0.004042`, median `-0.005714`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.034126`, avg `-0.00253`, median `-0.003925`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.075881`, avg `0.002391`, median `0.005418`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.4`, primary_mae `0.033272`, avg `0.118903`, median `0.127413`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.4667`, primary_mae `0.015686`, avg `3.2e-05`, median `-0.000494`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.45`, primary_mae `0.019089`, avg `0.000569`, median `-0.002196`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.4333`, primary_mae `0.019364`, avg `0.006477`, median `0.00857`
- 20d: sample `60`, primary_hit `0.1667`, primary_closer `0.3`, primary_mae `0.042723`, avg `0.035835`, median `0.034052`
- 60d: sample `60`, primary_hit `0.1`, primary_closer `0.4833`, primary_mae `0.049446`, avg `0.086536`, median `0.101639`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.015686, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019089, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.019364, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1667, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.042723, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.033272, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015899, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017408, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.015686, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017657, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020314, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019089, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022344, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026719, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.019364, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.5, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032126, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051013, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1667, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.042723, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.0875, 'secondary_hit_rate': 0.9125, 'primary_vs_secondary_accuracy_spread': -0.825, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040237, 'direction_hit_rate': 0.9125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.046754, 'direction_hit_rate': 0.9125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.033272, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.012832`, avg `0.005815`, median `0.008014`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.015499`, avg `0.006695`, median `0.008828`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.014721`, avg `0.009347`, median `0.01205`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.035436`, avg `0.026788`, median `0.029102`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.75`, primary_mae `0.0093`, avg `0.114868`, median `0.11635`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.014842`, avg `0.00339`, median `0.003357`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.016821`, avg `0.004505`, median `0.006272`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.019352`, avg `0.006854`, median `0.01205`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.037355`, avg `0.030284`, median `0.033084`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.5625`, primary_mae `0.039856`, avg `0.086058`, median `0.111461`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.020141`, avg `-0.006554`, median `-0.010376`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.019853`, avg `-0.003422`, median `-0.005714`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.034537`, avg `-0.001776`, median `-0.003925`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.065928`, avg `-0.007903`, median `-0.016989`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.375`, primary_mae `0.029647`, avg `0.12167`, median `0.122732`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.017408`, avg `-0.001134`, median `-0.001263`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.019691`, avg `-0.000584`, median `-0.003529`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.4375`, primary_mae `0.023054`, avg `0.004225`, median `0.006554`
- 20d: sample `80`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.051013`, avg `0.027474`, median `0.033434`
- 60d: sample `80`, primary_hit `0.0875`, primary_closer `0.4625`, primary_mae `0.045403`, avg `0.094628`, median `0.113154`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.017408`, avg `-0.001134`, median `-0.001263`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.019691`, avg `-0.000584`, median `-0.003529`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.4375`, primary_mae `0.023054`, avg `0.004225`, median `0.006554`
- 20d: sample `80`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.051013`, avg `0.027474`, median `0.033434`
- 60d: sample `80`, primary_hit `0.0875`, primary_closer `0.4625`, primary_mae `0.045403`, avg `0.094628`, median `0.113154`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.017408`, avg `-0.001134`, median `-0.001263`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.019691`, avg `-0.000584`, median `-0.003529`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.4375`, primary_mae `0.023054`, avg `0.004225`, median `0.006554`
- 20d: sample `80`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.051013`, avg `0.027474`, median `0.033434`
- 60d: sample `80`, primary_hit `0.0875`, primary_closer `0.4625`, primary_mae `0.045403`, avg `0.094628`, median `0.113154`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.017408`, avg `-0.001134`, median `-0.001263`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.019691`, avg `-0.000584`, median `-0.003529`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.4375`, primary_mae `0.023054`, avg `0.004225`, median `0.006554`
- 20d: sample `80`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.051013`, avg `0.027474`, median `0.033434`
- 60d: sample `80`, primary_hit `0.0875`, primary_closer `0.4625`, primary_mae `0.045403`, avg `0.094628`, median `0.113154`

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
