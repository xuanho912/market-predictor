# Historical Replay Benchmark

Generated at: `2026-08-13T23:54:21.905416+00:00`
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
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3667`
- primary_mean_absolute_error: `0.016412`
- secondary_mean_absolute_error: `0.01274`
- primary_error_advantage: `-0.003672`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 5d
- sample_size: `60`
- primary_hit_rate: `0.6667`
- secondary_hit_rate: `0.6667`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.026846`
- secondary_mean_absolute_error: `0.016716`
- primary_error_advantage: `-0.01013`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 10d
- sample_size: `60`
- primary_hit_rate: `0.5833`
- secondary_hit_rate: `0.5833`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3333`
- primary_mean_absolute_error: `0.03696`
- secondary_mean_absolute_error: `0.023489`
- primary_error_advantage: `-0.013471`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

### 20d
- sample_size: `60`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.07061`
- secondary_mean_absolute_error: `0.040355`
- primary_error_advantage: `-0.030255`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.225`

### 60d
- sample_size: `60`
- primary_hit_rate: `0.6667`
- secondary_hit_rate: `0.6667`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3167`
- primary_mean_absolute_error: `0.083272`
- secondary_mean_absolute_error: `0.063616`
- primary_error_advantage: `-0.019656`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

## Scenario Type Performance

### base_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.6`, path_mae `0.014173`, as_primary `0`, as_primary_hit `None`, avg `0.004712`, median `0.005013`
- 5d: sample `60`, direction_hit `0.6667`, path_mae `0.020586`, as_primary `0`, as_primary_hit `None`, avg `0.005142`, median `0.00573`
- 10d: sample `60`, direction_hit `0.5833`, path_mae `0.025566`, as_primary `0`, as_primary_hit `None`, avg `0.007645`, median `0.008249`
- 20d: sample `60`, direction_hit `0.65`, path_mae `0.04463`, as_primary `0`, as_primary_hit `None`, avg `0.010973`, median `0.012734`
- 60d: sample `60`, direction_hit `0.6667`, path_mae `0.062978`, as_primary `0`, as_primary_hit `None`, avg `0.028258`, median `0.044817`

### bounce_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.6`, path_mae `0.016412`, as_primary `60`, as_primary_hit `0.6`, avg `0.004712`, median `0.005013`
- 5d: sample `60`, direction_hit `0.6667`, path_mae `0.026846`, as_primary `60`, as_primary_hit `0.6667`, avg `0.005142`, median `0.00573`
- 10d: sample `60`, direction_hit `0.5833`, path_mae `0.03696`, as_primary `60`, as_primary_hit `0.5833`, avg `0.007645`, median `0.008249`
- 20d: sample `60`, direction_hit `0.65`, path_mae `0.07061`, as_primary `60`, as_primary_hit `0.65`, avg `0.010973`, median `0.012734`
- 60d: sample `60`, direction_hit `0.6667`, path_mae `0.083272`, as_primary `60`, as_primary_hit `0.6667`, avg `0.028258`, median `0.044817`

### failed_bounce_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.4`, path_mae `0.013937`, as_primary `0`, as_primary_hit `None`, avg `0.004712`, median `0.005013`
- 5d: sample `60`, direction_hit `0.3333`, path_mae `0.017077`, as_primary `0`, as_primary_hit `None`, avg `0.005142`, median `0.00573`
- 10d: sample `60`, direction_hit `0.4167`, path_mae `0.030976`, as_primary `0`, as_primary_hit `None`, avg `0.007645`, median `0.008249`
- 20d: sample `60`, direction_hit `0.35`, path_mae `0.076748`, as_primary `0`, as_primary_hit `None`, avg `0.010973`, median `0.012734`
- 60d: sample `60`, direction_hit `0.3333`, path_mae `0.094308`, as_primary `0`, as_primary_hit `None`, avg `0.028258`, median `0.044817`

### analog_average_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.6`, path_mae `0.01274`, as_primary `0`, as_primary_hit `None`, avg `0.004712`, median `0.005013`
- 5d: sample `60`, direction_hit `0.6667`, path_mae `0.016716`, as_primary `0`, as_primary_hit `None`, avg `0.005142`, median `0.00573`
- 10d: sample `60`, direction_hit `0.5833`, path_mae `0.023489`, as_primary `0`, as_primary_hit `None`, avg `0.007645`, median `0.008249`
- 20d: sample `60`, direction_hit `0.65`, path_mae `0.040355`, as_primary `0`, as_primary_hit `None`, avg `0.010973`, median `0.012734`
- 60d: sample `60`, direction_hit `0.6667`, path_mae `0.063616`, as_primary `0`, as_primary_hit `None`, avg `0.028258`, median `0.044817`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.016886`, avg `0.002944`, median `0.004555`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.275`, primary_mae `0.026956`, avg `0.004355`, median `0.005768`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.03683`, avg `0.006356`, median `0.008981`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.072491`, avg `0.011432`, median `0.01201`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.0812`, avg `0.026895`, median `0.023142`

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.015464`, avg `0.008247`, median `0.009306`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.026625`, avg `0.006714`, median `0.00573`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.03722`, avg `0.010223`, median `0.00588`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.25`, primary_mae `0.066846`, avg `0.010053`, median `0.015334`
- 60d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.087416`, avg `0.030985`, median `0.059654`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.016886`, avg `0.002944`, median `0.004555`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.275`, primary_mae `0.026956`, avg `0.004355`, median `0.005768`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.03683`, avg `0.006356`, median `0.008981`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.072491`, avg `0.011432`, median `0.01201`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.0812`, avg `0.026895`, median `0.023142`

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
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.03683, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.066846, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.0812, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3667, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.01274, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.016412, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015464, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6667, 'secondary_hit_rate': 0.6667, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.016716, 'direction_hit_rate': 0.6667}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.026846, 'direction_hit_rate': 0.6667}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.026625, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5833, 'secondary_hit_rate': 0.5833, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3333, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.023489, 'direction_hit_rate': 0.5833}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.03696, 'direction_hit_rate': 0.5833}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.03683, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.040355, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.076748, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.066846, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6667, 'secondary_hit_rate': 0.6667, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3167, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 60, 'path_mean_absolute_error': 0.062978, 'direction_hit_rate': 0.6667}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.094308, 'direction_hit_rate': 0.3333}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.0812, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `6`
- 3d: sample `6`, primary_hit `1.0`, primary_closer `0.3333`, primary_mae `0.011972`, avg `0.017327`, median `0.014414`
- 5d: sample `6`, primary_hit `0.6667`, primary_closer `0.1667`, primary_mae `0.034372`, avg `0.004391`, median `0.005572`
- 10d: sample `6`, primary_hit `0.5`, primary_closer `0.1667`, primary_mae `0.06782`, avg `-0.005403`, median `0.00239`
- 20d: sample `6`, primary_hit `0.1667`, primary_closer `0.1667`, primary_mae `0.141622`, avg `-0.013283`, median `-0.016119`
- 60d: sample `6`, primary_hit `0.5`, primary_closer `0.1667`, primary_mae `0.111356`, avg `0.02782`, median `0.024057`

### top_20
- sample_size: `12`
- 3d: sample `12`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.021511`, avg `0.0096`, median `0.011008`
- 5d: sample `12`, primary_hit `0.6667`, primary_closer `0.1667`, primary_mae `0.041225`, avg `0.001381`, median `0.005687`
- 10d: sample `12`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.065005`, avg `0.001412`, median `0.00239`
- 20d: sample `12`, primary_hit `0.5`, primary_closer `0.1667`, primary_mae `0.125807`, avg `0.00846`, median `0.003774`
- 60d: sample `12`, primary_hit `0.75`, primary_closer `0.1667`, primary_mae `0.09562`, avg `0.045238`, median `0.043992`

### bottom_20
- sample_size: `12`
- 3d: sample `12`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.021511`, avg `0.0096`, median `0.011008`
- 5d: sample `12`, primary_hit `0.6667`, primary_closer `0.1667`, primary_mae `0.041225`, avg `0.001381`, median `0.005687`
- 10d: sample `12`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.065005`, avg `0.001412`, median `0.00239`
- 20d: sample `12`, primary_hit `0.5`, primary_closer `0.1667`, primary_mae `0.125807`, avg `0.00846`, median `0.003774`
- 60d: sample `12`, primary_hit `0.75`, primary_closer `0.1667`, primary_mae `0.09562`, avg `0.045238`, median `0.043992`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6`, primary_closer `0.3667`, primary_mae `0.016412`, avg `0.004712`, median `0.005013`
- 5d: sample `60`, primary_hit `0.6667`, primary_closer `0.3`, primary_mae `0.026846`, avg `0.005142`, median `0.00573`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.3333`, primary_mae `0.03696`, avg `0.007645`, median `0.008249`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.07061`, avg `0.010973`, median `0.012734`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.3167`, primary_mae `0.083272`, avg `0.028258`, median `0.044817`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6`, primary_closer `0.3667`, primary_mae `0.016412`, avg `0.004712`, median `0.005013`
- 5d: sample `60`, primary_hit `0.6667`, primary_closer `0.3`, primary_mae `0.026846`, avg `0.005142`, median `0.00573`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.3333`, primary_mae `0.03696`, avg `0.007645`, median `0.008249`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.07061`, avg `0.010973`, median `0.012734`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.3167`, primary_mae `0.083272`, avg `0.028258`, median `0.044817`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.425`, primary_mae `0.013268`, avg `0.002922`, median `0.003447`
- 5d: sample `40`, primary_hit `0.725`, primary_closer `0.35`, primary_mae `0.019792`, avg `0.006668`, median `0.006292`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.025773`, avg `0.007797`, median `0.008249`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.35`, primary_mae `0.046722`, avg `0.007826`, median `0.013593`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.078226`, avg `0.016145`, median `0.044165`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.022698`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.040953`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.059336`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.118384`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.093365`, avg `0.052484`, median `0.06367`

### options_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6`, primary_closer `0.3667`, primary_mae `0.016412`, avg `0.004712`, median `0.005013`
- 5d: sample `60`, primary_hit `0.6667`, primary_closer `0.3`, primary_mae `0.026846`, avg `0.005142`, median `0.00573`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.3333`, primary_mae `0.03696`, avg `0.007645`, median `0.008249`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.07061`, avg `0.010973`, median `0.012734`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.3167`, primary_mae `0.083272`, avg `0.028258`, median `0.044817`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6`, primary_closer `0.3667`, primary_mae `0.016412`, avg `0.004712`, median `0.005013`
- 5d: sample `60`, primary_hit `0.6667`, primary_closer `0.3`, primary_mae `0.026846`, avg `0.005142`, median `0.00573`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.3333`, primary_mae `0.03696`, avg `0.007645`, median `0.008249`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.07061`, avg `0.010973`, median `0.012734`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.3167`, primary_mae `0.083272`, avg `0.028258`, median `0.044817`

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
