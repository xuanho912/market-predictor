# Historical Replay Benchmark

Generated at: `2026-08-16T13:04:04.052546+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
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
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.017195`
- secondary_mean_absolute_error: `0.012575`
- primary_error_advantage: `-0.00462`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.024455`
- secondary_mean_absolute_error: `0.015656`
- primary_error_advantage: `-0.008799`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.033834`
- secondary_mean_absolute_error: `0.021976`
- primary_error_advantage: `-0.011858`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.066231`
- secondary_mean_absolute_error: `0.040075`
- primary_error_advantage: `-0.026156`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.225`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.093809`
- secondary_mean_absolute_error: `0.066296`
- primary_error_advantage: `-0.027513`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.014493`, as_primary `0`, as_primary_hit `None`, avg `0.003098`, median `0.004273`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.018784`, as_primary `0`, as_primary_hit `None`, avg `0.003759`, median `0.00431`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.024216`, as_primary `0`, as_primary_hit `None`, avg `0.009201`, median `0.01093`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.044208`, as_primary `0`, as_primary_hit `None`, avg `0.017225`, median `0.020147`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.070297`, as_primary `0`, as_primary_hit `None`, avg `0.032559`, median `0.039396`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.017195`, as_primary `80`, as_primary_hit `0.6`, avg `0.003098`, median `0.004273`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.024455`, as_primary `80`, as_primary_hit `0.6375`, avg `0.003759`, median `0.00431`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.033834`, as_primary `80`, as_primary_hit `0.6`, avg `0.009201`, median `0.01093`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.066231`, as_primary `80`, as_primary_hit `0.675`, avg `0.017225`, median `0.020147`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.093809`, as_primary `80`, as_primary_hit `0.625`, avg `0.032559`, median `0.039396`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.015222`, as_primary `0`, as_primary_hit `None`, avg `0.003098`, median `0.004273`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.016339`, as_primary `0`, as_primary_hit `None`, avg `0.003759`, median `0.00431`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.02868`, as_primary `0`, as_primary_hit `None`, avg `0.009201`, median `0.01093`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.070176`, as_primary `0`, as_primary_hit `None`, avg `0.017225`, median `0.020147`
- 60d: sample `80`, direction_hit `0.375`, path_mae `0.08254`, as_primary `0`, as_primary_hit `None`, avg `0.032559`, median `0.039396`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.012575`, as_primary `0`, as_primary_hit `None`, avg `0.003098`, median `0.004273`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.015656`, as_primary `0`, as_primary_hit `None`, avg `0.003759`, median `0.00431`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.021976`, as_primary `0`, as_primary_hit `None`, avg `0.009201`, median `0.01093`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.040075`, as_primary `0`, as_primary_hit `None`, avg `0.017225`, median `0.020147`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.066296`, as_primary `0`, as_primary_hit `None`, avg `0.032559`, median `0.039396`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.017123`, avg `0.002973`, median `0.003167`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.3`, primary_mae `0.026026`, avg `0.004872`, median `0.004845`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.035718`, avg `0.009477`, median `0.011691`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.35`, primary_mae `0.073182`, avg `0.015977`, median `0.012734`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.35`, primary_mae `0.079199`, avg `0.034703`, median `0.029561`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.017268`, avg `0.003222`, median `0.005105`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.022885`, avg `0.002647`, median `0.003612`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.275`, primary_mae `0.03195`, avg `0.008925`, median `0.00986`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.225`, primary_mae `0.05928`, avg `0.018474`, median `0.026122`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.108418`, avg `0.030414`, median `0.045588`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.015646`, avg `-0.000601`, median `0.000402`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.017376`, avg `0.004611`, median `0.004845`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.022121`, avg `0.004921`, median `0.005827`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.35`, primary_mae `0.040661`, avg `0.01084`, median `0.01963`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.064433`, avg `0.012401`, median `0.004522`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.275`, primary_mae `0.018745`, avg `0.006797`, median `0.006043`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.275`, primary_mae `0.031535`, avg `0.002908`, median `0.003203`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.3`, primary_mae `0.045547`, avg `0.013481`, median `0.012369`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.225`, primary_mae `0.091801`, avg `0.023611`, median `0.026201`
- 60d: sample `40`, primary_hit `0.75`, primary_closer `0.275`, primary_mae `0.123184`, avg `0.052717`, median `0.05686`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.015646, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.017376, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022121, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.040661, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.064433, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012575, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017195, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.015646, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015656, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024455, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.017376, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021976, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033834, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022121, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040075, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070176, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.040661, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066296, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.093809, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.064433, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.023807`, avg `-0.000728`, median `-0.000883`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.0`, primary_mae `0.028453`, avg `0.000875`, median `0.004667`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.027328`, avg `0.007606`, median `0.011059`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.125`, primary_mae `0.05439`, avg `0.01684`, median `0.015956`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.090144`, avg `0.006335`, median `-0.025539`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.024354`, avg `-0.000393`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.1875`, primary_mae `0.026563`, avg `0.005531`, median `0.004667`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.02696`, avg `0.01176`, median `0.011059`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.050723`, avg `0.023687`, median `0.026122`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.07842`, avg `0.018535`, median `0.012785`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.024354`, avg `-0.000393`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.1875`, primary_mae `0.026563`, avg `0.005531`, median `0.004667`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.02696`, avg `0.01176`, median `0.011059`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.050723`, avg `0.023687`, median `0.026122`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.07842`, avg `0.018535`, median `0.012785`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.3625`, primary_mae `0.017195`, avg `0.003098`, median `0.004273`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.024455`, avg `0.003759`, median `0.00431`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.033834`, avg `0.009201`, median `0.01093`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.2875`, primary_mae `0.066231`, avg `0.017225`, median `0.020147`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.3375`, primary_mae `0.093809`, avg `0.032559`, median `0.039396`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.3625`, primary_mae `0.017195`, avg `0.003098`, median `0.004273`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.024455`, avg `0.003759`, median `0.00431`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.033834`, avg `0.009201`, median `0.01093`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.2875`, primary_mae `0.066231`, avg `0.017225`, median `0.020147`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.3375`, primary_mae `0.093809`, avg `0.032559`, median `0.039396`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.015646`, avg `-0.000601`, median `0.000402`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.017376`, avg `0.004611`, median `0.004845`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.022121`, avg `0.004921`, median `0.005827`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.35`, primary_mae `0.040661`, avg `0.01084`, median `0.01963`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.064433`, avg `0.012401`, median `0.004522`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.02463`, avg `0.009257`, median `0.01087`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.042524`, avg `0.006839`, median `0.005687`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.055777`, avg `0.018491`, median `0.016311`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.114224`, avg `0.034864`, median `0.022139`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.35`, primary_mae `0.097409`, avg `0.074228`, median `0.0687`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.3625`, primary_mae `0.017195`, avg `0.003098`, median `0.004273`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.024455`, avg `0.003759`, median `0.00431`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.033834`, avg `0.009201`, median `0.01093`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.2875`, primary_mae `0.066231`, avg `0.017225`, median `0.020147`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.3375`, primary_mae `0.093809`, avg `0.032559`, median `0.039396`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.3625`, primary_mae `0.017195`, avg `0.003098`, median `0.004273`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.024455`, avg `0.003759`, median `0.00431`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.033834`, avg `0.009201`, median `0.01093`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.2875`, primary_mae `0.066231`, avg `0.017225`, median `0.020147`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.3375`, primary_mae `0.093809`, avg `0.032559`, median `0.039396`

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
