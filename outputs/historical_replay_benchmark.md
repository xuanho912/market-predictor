# Historical Replay Benchmark

Generated at: `2026-08-31T19:11:11.074763+00:00`
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
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.021451`
- secondary_mean_absolute_error: `0.016199`
- primary_error_advantage: `-0.005252`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.022939`
- secondary_mean_absolute_error: `0.019435`
- primary_error_advantage: `-0.003504`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.037685`
- secondary_mean_absolute_error: `0.029155`
- primary_error_advantage: `-0.00853`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.058609`
- secondary_mean_absolute_error: `0.045904`
- primary_error_advantage: `-0.012705`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.078667`
- secondary_mean_absolute_error: `0.068534`
- primary_error_advantage: `-0.010133`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.01622`, as_primary `0`, as_primary_hit `None`, avg `-7.7e-05`, median `0.001946`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.019346`, as_primary `0`, as_primary_hit `None`, avg `-0.000224`, median `0.000482`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.026658`, as_primary `0`, as_primary_hit `None`, avg `0.001752`, median `-0.004843`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.033828`, as_primary `0`, as_primary_hit `None`, avg `0.012278`, median `0.020543`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.059699`, as_primary `0`, as_primary_hit `None`, avg `0.036168`, median `0.047922`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.016504`, as_primary `20`, as_primary_hit `0.5`, avg `-7.7e-05`, median `0.001946`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.021052`, as_primary `20`, as_primary_hit `0.45`, avg `-0.000224`, median `0.000482`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.03575`, as_primary `20`, as_primary_hit `0.3`, avg `0.001752`, median `-0.004843`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.047978`, as_primary `20`, as_primary_hit `0.55`, avg `0.012278`, median `0.020543`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.07095`, as_primary `20`, as_primary_hit `0.6`, avg `0.036168`, median `0.047922`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.021724`, as_primary `60`, as_primary_hit `0.5667`, avg `-7.7e-05`, median `0.001946`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.023026`, as_primary `60`, as_primary_hit `0.55`, avg `-0.000224`, median `0.000482`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.035922`, as_primary `60`, as_primary_hit `0.4833`, avg `0.001752`, median `-0.004843`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.06422`, as_primary `60`, as_primary_hit `0.75`, avg `0.012278`, median `0.020543`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.085644`, as_primary `60`, as_primary_hit `0.7667`, avg `0.036168`, median `0.047922`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.015687`, as_primary `0`, as_primary_hit `None`, avg `-7.7e-05`, median `0.001946`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.018407`, as_primary `0`, as_primary_hit `None`, avg `-0.000224`, median `0.000482`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.024871`, as_primary `0`, as_primary_hit `None`, avg `0.001752`, median `-0.004843`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.033497`, as_primary `0`, as_primary_hit `None`, avg `0.012278`, median `0.020543`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.056781`, as_primary `0`, as_primary_hit `None`, avg `0.036168`, median `0.047922`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4125`, primary_mae `0.021451`, avg `-7.7e-05`, median `0.001946`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022939`, avg `-0.000224`, median `0.000482`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.037685`, avg `0.001752`, median `-0.004843`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.058609`, avg `0.012278`, median `0.020543`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.078667`, avg `0.036168`, median `0.047922`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.4`, primary_mae `0.022661`, avg `0.000848`, median `0.002677`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.4167`, primary_mae `0.024691`, avg `0.001605`, median `0.001056`
- 10d: sample `60`, primary_hit `0.4167`, primary_closer `0.35`, primary_mae `0.042418`, avg `0.001416`, median `-0.007304`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.4`, primary_mae `0.059606`, avg `0.008086`, median `0.0142`
- 60d: sample `60`, primary_hit `0.3667`, primary_closer `0.45`, primary_mae `0.072381`, avg `0.028471`, median `0.031782`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.017819`, avg `-0.002852`, median `-0.001735`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.017682`, avg `-0.005709`, median `-0.006113`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.023486`, avg `0.002758`, median `-0.001577`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.055618`, avg `0.024854`, median `0.031427`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.097525`, avg `0.059262`, median `0.083174`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017819, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.017682, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.023486, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.055618, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.072381, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015687, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021724, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017819, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018407, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023026, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.017682, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024871, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035922, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.023486, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033497, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06422, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.055618, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056781, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.085644, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.072381, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.01455`, avg `-0.003731`, median `-0.000127`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.011255`, avg `-0.008244`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.030365`, avg `0.012486`, median `0.020076`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.054472`, avg `0.029933`, median `0.031427`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.105793`, avg `0.081351`, median `0.093846`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.017612`, avg `-0.001329`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016921`, avg `-0.007367`, median `-0.010372`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.026785`, avg `0.007624`, median `0.003189`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.3125`, primary_mae `0.055238`, avg `0.025765`, median `0.031427`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.094577`, avg `0.062199`, median `0.083174`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.034983`, avg `-0.002126`, median `0.006871`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.031369`, avg `0.003144`, median `0.007`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.040136`, avg `-0.003091`, median `-0.007124`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.059829`, avg `0.009917`, median `0.015879`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.091562`, avg `-0.006674`, median `0.006109`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4125`, primary_mae `0.021451`, avg `-7.7e-05`, median `0.001946`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022939`, avg `-0.000224`, median `0.000482`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.037685`, avg `0.001752`, median `-0.004843`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.058609`, avg `0.012278`, median `0.020543`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.078667`, avg `0.036168`, median `0.047922`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4125`, primary_mae `0.021451`, avg `-7.7e-05`, median `0.001946`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022939`, avg `-0.000224`, median `0.000482`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.037685`, avg `0.001752`, median `-0.004843`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.058609`, avg `0.012278`, median `0.020543`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.078667`, avg `0.036168`, median `0.047922`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.007752`, avg `-0.000893`, median `-0.000413`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.009824`, avg `-0.005075`, median `-0.004452`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.028757`, avg `-0.007915`, median `-0.01374`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.7`, primary_mae `0.04541`, avg `-0.00979`, median `0.006712`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.064893`, avg `0.014482`, median `0.032753`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.021305`, avg `0.000453`, median `0.001944`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.024663`, avg `-0.000883`, median `-0.005336`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.038622`, avg `0.006302`, median `-0.001577`
- 20d: sample `40`, primary_hit `0.225`, primary_closer `0.225`, primary_mae `0.06268`, avg `0.02199`, median `0.029731`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.078365`, avg `0.065605`, median `0.068495`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4125`, primary_mae `0.021451`, avg `-7.7e-05`, median `0.001946`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022939`, avg `-0.000224`, median `0.000482`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.037685`, avg `0.001752`, median `-0.004843`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.058609`, avg `0.012278`, median `0.020543`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.078667`, avg `0.036168`, median `0.047922`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4125`, primary_mae `0.021451`, avg `-7.7e-05`, median `0.001946`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022939`, avg `-0.000224`, median `0.000482`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.037685`, avg `0.001752`, median `-0.004843`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.058609`, avg `0.012278`, median `0.020543`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.078667`, avg `0.036168`, median `0.047922`

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
