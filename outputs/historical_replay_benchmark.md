# Historical Replay Benchmark

Generated at: `2026-07-02T23:42:42.900734+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.013858`
- secondary_mean_absolute_error: `0.013629`
- primary_error_advantage: `-0.000229`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.6`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.01861`
- secondary_mean_absolute_error: `0.016779`
- primary_error_advantage: `-0.001831`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.022292`
- secondary_mean_absolute_error: `0.021685`
- primary_error_advantage: `-0.000607`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.043705`
- secondary_mean_absolute_error: `0.045131`
- primary_error_advantage: `0.001426`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.078825`
- secondary_mean_absolute_error: `0.077098`
- primary_error_advantage: `-0.001727`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.012596`, as_primary `0`, as_primary_hit `None`, avg `-0.002581`, median `-0.00397`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.016401`, as_primary `0`, as_primary_hit `None`, avg `-0.003769`, median `-0.003063`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.018153`, as_primary `0`, as_primary_hit `None`, avg `0.001759`, median `-8e-06`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.026779`, as_primary `0`, as_primary_hit `None`, avg `0.010343`, median `0.01201`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.059564`, as_primary `0`, as_primary_hit `None`, avg `0.01034`, median `0.005661`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.01387`, as_primary `60`, as_primary_hit `0.4167`, avg `-0.002581`, median `-0.00397`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.017983`, as_primary `60`, as_primary_hit `0.4167`, avg `-0.003769`, median `-0.003063`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.022307`, as_primary `60`, as_primary_hit `0.4833`, avg `0.001759`, median `-8e-06`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.041651`, as_primary `60`, as_primary_hit `0.6333`, avg `0.010343`, median `0.01201`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.081521`, as_primary `60`, as_primary_hit `0.5833`, avg `0.01034`, median `0.005661`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.013617`, as_primary `20`, as_primary_hit `0.35`, avg `-0.002581`, median `-0.00397`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.017406`, as_primary `20`, as_primary_hit `0.6`, avg `-0.003769`, median `-0.003063`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.02167`, as_primary `20`, as_primary_hit `0.55`, avg `0.001759`, median `-8e-06`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.047186`, as_primary `20`, as_primary_hit `0.7`, avg `0.010343`, median `0.01201`
- 60d: sample `80`, direction_hit `0.4875`, path_mae `0.074402`, as_primary `20`, as_primary_hit `0.3`, avg `0.01034`, median `0.005661`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.012248`, as_primary `0`, as_primary_hit `None`, avg `-0.002581`, median `-0.00397`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.016006`, as_primary `0`, as_primary_hit `None`, avg `-0.003769`, median `-0.003063`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.017752`, as_primary `0`, as_primary_hit `None`, avg `0.001759`, median `-8e-06`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.025393`, as_primary `0`, as_primary_hit `None`, avg `0.010343`, median `0.01201`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.056152`, as_primary `0`, as_primary_hit `None`, avg `0.01034`, median `0.005661`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.5333`, primary_mae `0.015846`, avg `-0.002292`, median `-0.00397`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.5167`, primary_mae `0.020419`, avg `-0.005256`, median `-0.006946`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.5`, primary_mae `0.026356`, avg `0.001446`, median `-0.001166`
- 20d: sample `60`, primary_hit `0.6333`, primary_closer `0.55`, primary_mae `0.046829`, avg `0.010524`, median `0.011034`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.090227`, avg `0.02446`, median `0.035568`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.007894`, avg `-0.00345`, median `-0.004103`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.013185`, avg `0.000693`, median `0.00337`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.65`, primary_mae `0.010103`, avg `0.002697`, median `0.001279`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.034333`, avg `0.009802`, median `0.013848`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.044618`, avg `-0.032019`, median `-0.038871`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.019043`, avg `0.003518`, median `0.003542`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.025851`, avg `0.001981`, median `-0.001363`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.038901`, avg `0.006441`, median `0.011494`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.041791`, avg `0.010095`, median `0.013099`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.074761`, avg `0.003339`, median `-0.002406`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.007894`, avg `-0.00345`, median `-0.004103`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.013185`, avg `0.000693`, median `0.00337`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.65`, primary_mae `0.010103`, avg `0.002697`, median `0.001279`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.034333`, avg `0.009802`, median `0.013848`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.044618`, avg `-0.032019`, median `-0.038871`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.35`, primary_closer `0.575`, primary_mae `0.014248`, avg `-0.005196`, median `-0.005904`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.55`, primary_mae `0.017703`, avg `-0.008874`, median `-0.007149`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.020083`, avg `-0.001052`, median `-0.00603`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.049348`, avg `0.010738`, median `0.007665`
- 60d: sample `40`, primary_hit `0.65`, primary_closer `0.575`, primary_mae `0.09796`, avg `0.035021`, median `0.054678`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.007894, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013185, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.010103, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.034333, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.044618, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012248, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01387, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.007894, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016006, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017983, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013185, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017752, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022307, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.010103, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025393, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.047186, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.034333, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056152, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.081521, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.044618, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.019027`, avg `-0.01179`, median `-0.01401`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.023474`, avg `-0.012668`, median `-0.023515`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.016404`, avg `-0.004832`, median `-0.008173`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.032344`, avg `0.030838`, median `0.036311`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.062372`, avg `0.063648`, median `0.086267`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.016539`, avg `-0.010721`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.017517`, avg `-0.011319`, median `-0.010372`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.5625`, primary_mae `0.015917`, avg `-0.007014`, median `-0.008733`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.044186`, avg `0.019876`, median `0.025462`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.08511`, avg `0.042498`, median `0.062395`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.008018`, avg `-0.002716`, median `-0.002721`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.014366`, avg `0.000146`, median `0.00337`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.625`, primary_mae `0.010554`, avg `0.003587`, median `0.001279`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.033242`, avg `0.010654`, median `0.013848`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.041405`, avg `-0.033989`, median `-0.039821`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.525`, primary_mae `0.013858`, avg `-0.002581`, median `-0.00397`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.475`, primary_mae `0.01861`, avg `-0.003769`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.5375`, primary_mae `0.022292`, avg `0.001759`, median `-8e-06`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.043705`, avg `0.010343`, median `0.01201`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.078825`, avg `0.01034`, median `0.005661`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.525`, primary_mae `0.013858`, avg `-0.002581`, median `-0.00397`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.475`, primary_mae `0.01861`, avg `-0.003769`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.5375`, primary_mae `0.022292`, avg `0.001759`, median `-8e-06`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.043705`, avg `0.010343`, median `0.01201`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.078825`, avg `0.01034`, median `0.005661`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.5333`, primary_mae `0.015846`, avg `-0.002292`, median `-0.00397`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.5167`, primary_mae `0.020419`, avg `-0.005256`, median `-0.006946`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.5`, primary_mae `0.026356`, avg `0.001446`, median `-0.001166`
- 20d: sample `60`, primary_hit `0.6333`, primary_closer `0.55`, primary_mae `0.046829`, avg `0.010524`, median `0.011034`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.090227`, avg `0.02446`, median `0.035568`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.007894`, avg `-0.00345`, median `-0.004103`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.013185`, avg `0.000693`, median `0.00337`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.65`, primary_mae `0.010103`, avg `0.002697`, median `0.001279`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.034333`, avg `0.009802`, median `0.013848`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.044618`, avg `-0.032019`, median `-0.038871`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.525`, primary_mae `0.013858`, avg `-0.002581`, median `-0.00397`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.475`, primary_mae `0.01861`, avg `-0.003769`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.5375`, primary_mae `0.022292`, avg `0.001759`, median `-8e-06`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.043705`, avg `0.010343`, median `0.01201`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.078825`, avg `0.01034`, median `0.005661`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.525`, primary_mae `0.013858`, avg `-0.002581`, median `-0.00397`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.475`, primary_mae `0.01861`, avg `-0.003769`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.5375`, primary_mae `0.022292`, avg `0.001759`, median `-8e-06`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.043705`, avg `0.010343`, median `0.01201`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.078825`, avg `0.01034`, median `0.005661`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.525`, primary_mae `0.013858`, avg `-0.002581`, median `-0.00397`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.475`, primary_mae `0.01861`, avg `-0.003769`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.5375`, primary_mae `0.022292`, avg `0.001759`, median `-8e-06`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.043705`, avg `0.010343`, median `0.01201`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.078825`, avg `0.01034`, median `0.005661`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
