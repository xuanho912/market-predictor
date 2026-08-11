# Historical Replay Benchmark

Generated at: `2026-08-11T13:48:34.369709+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.017215`
- secondary_mean_absolute_error: `0.016773`
- primary_error_advantage: `-0.000442`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.021513`
- secondary_mean_absolute_error: `0.018455`
- primary_error_advantage: `-0.003058`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.032747`
- secondary_mean_absolute_error: `0.029871`
- primary_error_advantage: `-0.002876`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.057402`
- secondary_mean_absolute_error: `0.056908`
- primary_error_advantage: `-0.000494`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.079498`
- secondary_mean_absolute_error: `0.080252`
- primary_error_advantage: `0.000754`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.014606`, as_primary `0`, as_primary_hit `None`, avg `0.002747`, median `0.005105`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.018761`, as_primary `0`, as_primary_hit `None`, avg `0.004584`, median `0.005323`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.027014`, as_primary `0`, as_primary_hit `None`, avg `0.006678`, median `0.006542`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.040867`, as_primary `0`, as_primary_hit `None`, avg `0.012965`, median `0.014634`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.065669`, as_primary `0`, as_primary_hit `None`, avg `0.030289`, median `0.045588`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.017728`, as_primary `60`, as_primary_hit `0.5833`, avg `0.002747`, median `0.005105`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.024784`, as_primary `60`, as_primary_hit `0.6833`, avg `0.004584`, median `0.005323`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.036153`, as_primary `60`, as_primary_hit `0.5667`, avg `0.006678`, median `0.006542`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.062626`, as_primary `60`, as_primary_hit `0.6667`, avg `0.012965`, median `0.014634`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.081295`, as_primary `60`, as_primary_hit `0.5667`, avg `0.030289`, median `0.045588`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.020839`, as_primary `20`, as_primary_hit `0.75`, avg `0.002747`, median `0.005105`
- 5d: sample `80`, direction_hit `0.3375`, path_mae `0.021785`, as_primary `20`, as_primary_hit `0.6`, avg `0.004584`, median `0.005323`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.034173`, as_primary `20`, as_primary_hit `0.6`, avg `0.006678`, median `0.006542`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.071852`, as_primary `20`, as_primary_hit `0.75`, avg `0.012965`, median `0.014634`
- 60d: sample `80`, direction_hit `0.4`, path_mae `0.088782`, as_primary `20`, as_primary_hit `0.7`, avg `0.030289`, median `0.045588`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.014372`, as_primary `0`, as_primary_hit `None`, avg `0.002747`, median `0.005105`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.016834`, as_primary `0`, as_primary_hit `None`, avg `0.004584`, median `0.005323`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.024351`, as_primary `0`, as_primary_hit `None`, avg `0.006678`, median `0.006542`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.037798`, as_primary `0`, as_primary_hit `None`, avg `0.012965`, median `0.014634`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.062448`, as_primary `0`, as_primary_hit `None`, avg `0.030289`, median `0.045588`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017215`, avg `0.002747`, median `0.005105`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.45`, primary_mae `0.021513`, avg `0.004584`, median `0.005323`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.032747`, avg `0.006678`, median `0.006542`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.057402`, avg `0.012965`, median `0.014634`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.079498`, avg `0.030289`, median `0.045588`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.675`, primary_mae `0.011829`, avg `0.002181`, median `0.003213`
- 5d: sample `40`, primary_hit `0.725`, primary_closer `0.55`, primary_mae `0.013617`, avg `0.005364`, median `0.006292`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.575`, primary_mae `0.02496`, avg `0.002945`, median `0.005212`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.675`, primary_mae `0.048667`, avg `0.000182`, median `0.01201`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.069055`, avg `0.017502`, median `0.044393`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.022601`, avg `0.003313`, median `0.009658`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.029408`, avg `0.003804`, median `0.003509`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.040533`, avg `0.01041`, median `0.01093`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.25`, primary_mae `0.066138`, avg `0.025748`, median `0.023697`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.089942`, avg `0.043075`, median `0.053988`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.675, 'primary_mean_absolute_error': 0.011829, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.013617, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.02496, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.675, 'primary_mean_absolute_error': 0.048667, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.069055, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014372, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020839, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.675, 'primary_mean_absolute_error': 0.011829, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016834, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024784, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.013617, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024351, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036153, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.02496, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037798, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071852, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.675, 'primary_mean_absolute_error': 0.048667, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062448, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.088782, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.069055, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.025799`, avg `-0.003813`, median `-0.002198`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.125`, primary_mae `0.028429`, avg `0.000899`, median `0.003509`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.032668`, avg `0.002265`, median `0.002208`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.061971`, avg `0.009259`, median `0.014663`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.109216`, avg `-0.012738`, median `-0.032183`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.024934`, avg `-0.002935`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.025497`, avg `0.004618`, median `0.003509`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.030879`, avg `0.005864`, median `0.006104`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.1875`, primary_mae `0.060368`, avg `0.012246`, median `0.02136`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.090078`, avg `0.006806`, median `-0.012556`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.024934`, avg `-0.002935`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.025497`, avg `0.004618`, median `0.003509`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.030879`, avg `0.005864`, median `0.006104`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.1875`, primary_mae `0.060368`, avg `0.012246`, median `0.02136`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.090078`, avg `0.006806`, median `-0.012556`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017215`, avg `0.002747`, median `0.005105`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.45`, primary_mae `0.021513`, avg `0.004584`, median `0.005323`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.032747`, avg `0.006678`, median `0.006542`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.057402`, avg `0.012965`, median `0.014634`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.079498`, avg `0.030289`, median `0.045588`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017215`, avg `0.002747`, median `0.005105`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.45`, primary_mae `0.021513`, avg `0.004584`, median `0.005323`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.032747`, avg `0.006678`, median `0.006542`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.057402`, avg `0.012965`, median `0.014634`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.079498`, avg `0.030289`, median `0.045588`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.625`, primary_mae `0.017121`, avg `-0.002537`, median `0.000173`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.425`, primary_mae `0.018623`, avg `0.003833`, median `0.00431`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.023525`, avg `0.004229`, median `0.005479`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.475`, primary_mae `0.04422`, avg `0.007792`, median `0.012734`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.071666`, avg `0.007279`, median `-0.011046`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.021081`, avg `0.007955`, median `0.011608`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.031277`, avg `0.003606`, median `0.005967`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.048361`, avg `0.015564`, median `0.012095`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.072728`, avg `0.037269`, median `0.03141`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.099802`, avg `0.068731`, median `0.079781`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017215`, avg `0.002747`, median `0.005105`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.45`, primary_mae `0.021513`, avg `0.004584`, median `0.005323`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.032747`, avg `0.006678`, median `0.006542`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.057402`, avg `0.012965`, median `0.014634`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.079498`, avg `0.030289`, median `0.045588`

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
