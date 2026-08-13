# Historical Replay Benchmark

Generated at: `2026-08-13T22:23:21.437418+00:00`
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
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.017228`
- secondary_mean_absolute_error: `0.012827`
- primary_error_advantage: `-0.004401`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.026839`
- secondary_mean_absolute_error: `0.016552`
- primary_error_advantage: `-0.010287`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.035029`
- secondary_mean_absolute_error: `0.022327`
- primary_error_advantage: `-0.012702`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.065194`
- secondary_mean_absolute_error: `0.037019`
- primary_error_advantage: `-0.028175`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.225`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.081309`
- secondary_mean_absolute_error: `0.064777`
- primary_error_advantage: `-0.016532`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.01415`, as_primary `0`, as_primary_hit `None`, avg `0.00456`, median `0.005013`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.020344`, as_primary `0`, as_primary_hit `None`, avg `0.005037`, median `0.005323`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.024371`, as_primary `0`, as_primary_hit `None`, avg `0.007984`, median `0.00986`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.040815`, as_primary `0`, as_primary_hit `None`, avg `0.014437`, median `0.015644`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.064183`, as_primary `0`, as_primary_hit `None`, avg `0.027209`, median `0.045588`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.017228`, as_primary `80`, as_primary_hit `0.6125`, avg `0.00456`, median `0.005013`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.026839`, as_primary `80`, as_primary_hit `0.6375`, avg `0.005037`, median `0.005323`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.035029`, as_primary `80`, as_primary_hit `0.6125`, avg `0.007984`, median `0.00986`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.065194`, as_primary `80`, as_primary_hit `0.6875`, avg `0.014437`, median `0.015644`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.081309`, as_primary `80`, as_primary_hit `0.6375`, avg `0.027209`, median `0.045588`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.01339`, as_primary `0`, as_primary_hit `None`, avg `0.00456`, median `0.005013`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.01738`, as_primary `0`, as_primary_hit `None`, avg `0.005037`, median `0.005323`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.029139`, as_primary `0`, as_primary_hit `None`, avg `0.007984`, median `0.00986`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.07052`, as_primary `0`, as_primary_hit `None`, avg `0.014437`, median `0.015644`
- 60d: sample `80`, direction_hit `0.3625`, path_mae `0.090462`, as_primary `0`, as_primary_hit `None`, avg `0.027209`, median `0.045588`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.012827`, as_primary `0`, as_primary_hit `None`, avg `0.00456`, median `0.005013`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.016552`, as_primary `0`, as_primary_hit `None`, avg `0.005037`, median `0.005323`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.022327`, as_primary `0`, as_primary_hit `None`, avg `0.007984`, median `0.00986`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.037019`, as_primary `0`, as_primary_hit `None`, avg `0.014437`, median `0.015644`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.064777`, as_primary `0`, as_primary_hit `None`, avg `0.027209`, median `0.045588`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.022698`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.040953`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.059336`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.118384`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.093365`, avg `0.052484`, median `0.06367`

### STRONG_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6`, primary_closer `0.4167`, primary_mae `0.015405`, avg `0.003316`, median `0.003447`
- 5d: sample `60`, primary_hit `0.6667`, primary_closer `0.3333`, primary_mae `0.022134`, avg `0.00602`, median `0.00573`
- 10d: sample `60`, primary_hit `0.6333`, primary_closer `0.35`, primary_mae `0.026927`, avg `0.008198`, median `0.00986`
- 20d: sample `60`, primary_hit `0.7167`, primary_closer `0.2833`, primary_mae `0.047463`, avg `0.013493`, median `0.019709`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.3833`, primary_mae `0.077291`, avg `0.018784`, median `0.044817`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6`, primary_closer `0.3667`, primary_mae `0.017817`, avg `0.003332`, median `0.004555`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.2833`, primary_mae `0.02691`, avg `0.004478`, median `0.005202`
- 10d: sample `60`, primary_hit `0.6167`, primary_closer `0.3833`, primary_mae `0.034298`, avg `0.007238`, median `0.01093`
- 20d: sample `60`, primary_hit `0.7167`, primary_closer `0.2667`, primary_mae `0.064643`, avg `0.015898`, median `0.015644`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.3667`, primary_mae `0.079274`, avg `0.02595`, median `0.028346`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.015464`, avg `0.008247`, median `0.009306`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.026625`, avg `0.006714`, median `0.00573`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.03722`, avg `0.010223`, median `0.00588`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.25`, primary_mae `0.066846`, avg `0.010053`, median `0.015334`
- 60d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.087416`, avg `0.030985`, median `0.059654`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015464, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.026625, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.034298, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7167, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.064643, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.079274, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012827, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017228, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015464, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016552, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026839, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.026625, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022327, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035029, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.034298, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037019, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07052, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7167, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.064643, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064183, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.090462, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.079274, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.023807`, avg `-0.000728`, median `-0.000883`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.028453`, avg `0.000875`, median `0.004667`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.027328`, avg `0.007606`, median `0.011059`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.125`, primary_mae `0.05439`, avg `0.01684`, median `0.015956`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.090144`, avg `0.006335`, median `-0.025539`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.024354`, avg `-0.000393`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.026563`, avg `0.005531`, median `0.004667`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.02696`, avg `0.01176`, median `0.011059`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.050723`, avg `0.023687`, median `0.026122`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.07842`, avg `0.018535`, median `0.012785`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.024354`, avg `-0.000393`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.026563`, avg `0.005531`, median `0.004667`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.02696`, avg `0.01176`, median `0.011059`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.050723`, avg `0.023687`, median `0.026122`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.07842`, avg `0.018535`, median `0.012785`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.375`, primary_mae `0.017228`, avg `0.00456`, median `0.005013`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.026839`, avg `0.005037`, median `0.005323`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3375`, primary_mae `0.035029`, avg `0.007984`, median `0.00986`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.2625`, primary_mae `0.065194`, avg `0.014437`, median `0.015644`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.35`, primary_mae `0.081309`, avg `0.027209`, median `0.045588`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.375`, primary_mae `0.017228`, avg `0.00456`, median `0.005013`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.026839`, avg `0.005037`, median `0.005323`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3375`, primary_mae `0.035029`, avg `0.007984`, median `0.00986`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.2625`, primary_mae `0.065194`, avg `0.014437`, median `0.015644`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.35`, primary_mae `0.081309`, avg `0.027209`, median `0.045588`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.425`, primary_mae `0.015376`, avg `0.000851`, median `0.001025`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.019888`, avg `0.005673`, median `0.005885`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.425`, primary_mae `0.02178`, avg `0.007186`, median `0.011059`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.3`, primary_mae `0.037772`, avg `0.015213`, median `0.020543`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.072228`, avg `0.012684`, median `0.007512`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.022698`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.040953`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.059336`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.118384`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.093365`, avg `0.052484`, median `0.06367`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.375`, primary_mae `0.017228`, avg `0.00456`, median `0.005013`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.026839`, avg `0.005037`, median `0.005323`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3375`, primary_mae `0.035029`, avg `0.007984`, median `0.00986`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.2625`, primary_mae `0.065194`, avg `0.014437`, median `0.015644`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.35`, primary_mae `0.081309`, avg `0.027209`, median `0.045588`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.375`, primary_mae `0.017228`, avg `0.00456`, median `0.005013`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3`, primary_mae `0.026839`, avg `0.005037`, median `0.005323`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3375`, primary_mae `0.035029`, avg `0.007984`, median `0.00986`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.2625`, primary_mae `0.065194`, avg `0.014437`, median `0.015644`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.35`, primary_mae `0.081309`, avg `0.027209`, median `0.045588`

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
