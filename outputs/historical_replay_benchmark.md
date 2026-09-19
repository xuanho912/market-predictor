# Historical Replay Benchmark

Generated at: `2026-09-19T15:56:00.344610+00:00`
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
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.018311`
- secondary_mean_absolute_error: `0.018574`
- primary_error_advantage: `0.000263`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.022958`
- secondary_mean_absolute_error: `0.021265`
- primary_error_advantage: `-0.001693`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.026583`
- secondary_mean_absolute_error: `0.027728`
- primary_error_advantage: `0.001145`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.058`
- secondary_mean_absolute_error: `0.049079`
- primary_error_advantage: `-0.008921`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.092371`
- secondary_mean_absolute_error: `0.069966`
- primary_error_advantage: `-0.022405`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3333`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.015835`, as_primary `0`, as_primary_hit `None`, avg `-0.004867`, median `-0.001349`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018173`, as_primary `0`, as_primary_hit `None`, avg `-0.009009`, median `-0.0084`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.022605`, as_primary `0`, as_primary_hit `None`, avg `-0.009298`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.035659`, as_primary `0`, as_primary_hit `None`, avg `0.007191`, median `0.010094`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.060751`, as_primary `0`, as_primary_hit `None`, avg `0.030002`, median `0.048222`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.018173`, as_primary `0`, as_primary_hit `None`, avg `-0.004867`, median `-0.001349`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.021676`, as_primary `0`, as_primary_hit `None`, avg `-0.009009`, median `-0.0084`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.031867`, as_primary `0`, as_primary_hit `None`, avg `-0.009298`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.057375`, as_primary `0`, as_primary_hit `None`, avg `0.007191`, median `0.010094`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.076247`, as_primary `0`, as_primary_hit `None`, avg `0.030002`, median `0.048222`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.018311`, as_primary `80`, as_primary_hit `0.475`, avg `-0.004867`, median `-0.001349`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.022958`, as_primary `80`, as_primary_hit `0.45`, avg `-0.009009`, median `-0.0084`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.026583`, as_primary `80`, as_primary_hit `0.4`, avg `-0.009298`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.45`, path_mae `0.058`, as_primary `80`, as_primary_hit `0.55`, avg `0.007191`, median `0.010094`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.092371`, as_primary `80`, as_primary_hit `0.725`, avg `0.030002`, median `0.048222`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.015648`, as_primary `0`, as_primary_hit `None`, avg `-0.004867`, median `-0.001349`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.017766`, as_primary `0`, as_primary_hit `None`, avg `-0.009009`, median `-0.0084`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.021071`, as_primary `0`, as_primary_hit `None`, avg `-0.009298`, median `-0.010169`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.033835`, as_primary `0`, as_primary_hit `None`, avg `0.007191`, median `0.010094`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.059873`, as_primary `0`, as_primary_hit `None`, avg `0.030002`, median `0.048222`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.5167`, primary_mae `0.016667`, avg `-0.003042`, median `0.002084`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.4333`, primary_mae `0.021756`, avg `-0.005896`, median `0.00102`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.025483`, avg `-0.002354`, median `-0.005329`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.35`, primary_mae `0.05157`, avg `0.01406`, median `0.015571`
- 60d: sample `60`, primary_hit `0.25`, primary_closer `0.3333`, primary_mae `0.072158`, avg `0.037455`, median `0.050131`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.023246`, avg `-0.01034`, median `-0.009953`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.45`, primary_mae `0.026561`, avg `-0.018347`, median `-0.018998`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.7`, primary_mae `0.029883`, avg `-0.030129`, median `-0.038709`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.077291`, avg `-0.013419`, median `-0.019479`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.15301`, avg `0.007643`, median `0.044372`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.01643`, avg `0.00406`, median `0.010894`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.021526`, avg `0.001351`, median `0.003555`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.030176`, avg `0.002998`, median `0.003495`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.2`, primary_mae `0.046494`, avg `0.009355`, median `0.001665`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.058125`, avg `0.033352`, median `0.031375`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.023246`, avg `-0.01034`, median `-0.009953`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.45`, primary_mae `0.026561`, avg `-0.018347`, median `-0.018998`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.7`, primary_mae `0.029883`, avg `-0.030129`, median `-0.038709`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.077291`, avg `-0.013419`, median `-0.019479`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.15301`, avg `0.007643`, median `0.044372`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.625`, primary_mae `0.016785`, avg `-0.006593`, median `-0.00165`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.021871`, avg `-0.00952`, median `-0.0084`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.023136`, avg `-0.00503`, median `-0.007251`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.054108`, avg `0.016413`, median `0.027381`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.079174`, avg `0.039507`, median `0.059117`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.01643, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.021526, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.023136, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.046494, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.058125, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015648, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018311, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.01643, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017766, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022958, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.021526, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021071, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031867, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.023136, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033835, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.046494, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059873, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.092371, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.058125, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.014867`, avg `0.011118`, median `0.011849`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.015102`, avg `-0.00482`, median `0.000984`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.015289`, avg `-0.005498`, median `-0.010197`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.029206`, avg `-0.003211`, median `-0.00092`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.041245`, avg `0.003417`, median `0.018611`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.015`, avg `0.006204`, median `0.011628`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.018841`, avg `0.001878`, median `0.001988`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.02666`, avg `0.005685`, median `0.006069`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.1875`, primary_mae `0.043884`, avg `0.01159`, median `0.001665`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.057602`, avg `0.03084`, median `0.028352`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.8125`, primary_closer `0.5`, primary_mae `0.018075`, avg `-0.011407`, median `-0.012736`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.022569`, avg `-0.019896`, median `-0.021584`
- 10d: sample `16`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.021737`, avg `-0.036375`, median `-0.038715`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.076012`, avg `-0.015843`, median `-0.019479`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.154572`, avg `0.003737`, median `0.044372`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.018311`, avg `-0.004867`, median `-0.001349`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.022958`, avg `-0.009009`, median `-0.0084`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.026583`, avg `-0.009298`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.058`, avg `0.007191`, median `0.010094`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.325`, primary_mae `0.092371`, avg `0.030002`, median `0.048222`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.018311`, avg `-0.004867`, median `-0.001349`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.022958`, avg `-0.009009`, median `-0.0084`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.026583`, avg `-0.009298`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.058`, avg `0.007191`, median `0.010094`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.325`, primary_mae `0.092371`, avg `0.030002`, median `0.048222`

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
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.018311`, avg `-0.004867`, median `-0.001349`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.022958`, avg `-0.009009`, median `-0.0084`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.026583`, avg `-0.009298`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.058`, avg `0.007191`, median `0.010094`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.325`, primary_mae `0.092371`, avg `0.030002`, median `0.048222`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.018311`, avg `-0.004867`, median `-0.001349`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.022958`, avg `-0.009009`, median `-0.0084`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.026583`, avg `-0.009298`, median `-0.010169`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.058`, avg `0.007191`, median `0.010094`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.325`, primary_mae `0.092371`, avg `0.030002`, median `0.048222`

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
