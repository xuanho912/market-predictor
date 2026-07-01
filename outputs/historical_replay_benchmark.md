# Historical Replay Benchmark

Generated at: `2026-07-01T23:55:40.955554+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'low', 'reasons': [], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `not_proven_or_mixed`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_supportive_but_not_forward_validated`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.012453`
- secondary_mean_absolute_error: `0.014499`
- primary_error_advantage: `0.002046`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6333`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.016854`
- secondary_mean_absolute_error: `0.01939`
- primary_error_advantage: `0.002536`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.023047`
- secondary_mean_absolute_error: `0.022706`
- primary_error_advantage: `-0.000341`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.055438`
- secondary_mean_absolute_error: `0.041687`
- primary_error_advantage: `-0.013751`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.3125`
- primary_vs_secondary_accuracy_spread: `0.375`
- primary_closer_than_secondary_rate: `0.625`
- primary_mean_absolute_error: `0.070619`
- secondary_mean_absolute_error: `0.072003`
- primary_error_advantage: `0.001384`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.01202`, as_primary `0`, as_primary_hit `None`, avg `-0.004399`, median `-0.005904`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.016258`, as_primary `0`, as_primary_hit `None`, avg `-0.005857`, median `-0.004256`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.018398`, as_primary `0`, as_primary_hit `None`, avg `-0.00131`, median `-0.003425`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.029288`, as_primary `0`, as_primary_hit `None`, avg `0.0053`, median `0.00995`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.053315`, as_primary `0`, as_primary_hit `None`, avg `0.006851`, median `-0.00576`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.012439`, as_primary `40`, as_primary_hit `0.325`, avg `-0.004399`, median `-0.005904`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018538`, as_primary `40`, as_primary_hit `0.35`, avg `-0.005857`, median `-0.004256`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.022156`, as_primary `40`, as_primary_hit `0.425`, avg `-0.00131`, median `-0.003425`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.042103`, as_primary `40`, as_primary_hit `0.625`, avg `0.0053`, median `0.00995`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.074803`, as_primary `40`, as_primary_hit `0.65`, avg `0.006851`, median `-0.00576`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.014513`, as_primary `40`, as_primary_hit `0.425`, avg `-0.004399`, median `-0.005904`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.017706`, as_primary `40`, as_primary_hit `0.55`, avg `-0.005857`, median `-0.004256`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.023597`, as_primary `40`, as_primary_hit `0.5`, avg `-0.00131`, median `-0.003425`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.055022`, as_primary `40`, as_primary_hit `0.65`, avg `0.0053`, median `0.00995`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.067819`, as_primary `40`, as_primary_hit `0.275`, avg `0.006851`, median `-0.00576`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.011353`, as_primary `0`, as_primary_hit `None`, avg `-0.004399`, median `-0.005904`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.016102`, as_primary `0`, as_primary_hit `None`, avg `-0.005857`, median `-0.004256`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.01827`, as_primary `0`, as_primary_hit `None`, avg `-0.00131`, median `-0.003425`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.027909`, as_primary `0`, as_primary_hit `None`, avg `0.0053`, median `0.00995`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.050835`, as_primary `0`, as_primary_hit `None`, avg `0.006851`, median `-0.00576`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.012453`, avg `-0.004399`, median `-0.005904`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.016854`, avg `-0.005857`, median `-0.004256`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.023047`, avg `-0.00131`, median `-0.003425`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.055438`, avg `0.0053`, median `0.00995`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.070619`, avg `0.006851`, median `-0.00576`

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
- 3d: sample `20`, primary_hit `0.8`, primary_closer `0.2`, primary_mae `0.009891`, avg `-0.007043`, median `-0.008115`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.014389`, avg `-0.005437`, median `-5e-05`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.25`, primary_mae `0.024489`, avg `-0.005011`, median `-0.003297`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.059485`, avg `-0.002027`, median `0.009366`
- 60d: sample `20`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.039969`, avg `-0.029323`, median `-0.03329`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3333`, primary_closer `0.6333`, primary_mae `0.013306`, avg `-0.003518`, median `-0.00397`
- 5d: sample `60`, primary_hit `0.3667`, primary_closer `0.5333`, primary_mae `0.017676`, avg `-0.005997`, median `-0.005474`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.5`, primary_mae `0.022567`, avg `-7.7e-05`, median `-0.003912`
- 20d: sample `60`, primary_hit `0.5167`, primary_closer `0.4`, primary_mae `0.054089`, avg `0.007743`, median `0.00995`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.5833`, primary_mae `0.080836`, avg `0.01891`, median `0.012182`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.009891, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014389, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.022567, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.054089, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.039969, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011353, 'direction_hit_rate': 0.375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014513, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.009891, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016102, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018538, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014389, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01827, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023597, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.022567, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027909, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055022, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.054089, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.3125, 'primary_vs_secondary_accuracy_spread': 0.375, 'primary_closer_than_secondary_rate': 0.625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050835, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074803, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.039969, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.018712`, avg `-0.01179`, median `-0.01401`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.023474`, avg `-0.012668`, median `-0.023515`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.016404`, avg `-0.004832`, median `-0.008173`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.032344`, avg `0.030838`, median `0.036311`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.062372`, avg `0.063648`, median `0.086267`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.017983`, avg `-0.012635`, median `-0.013117`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.020927`, avg `-0.014633`, median `-0.019358`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.4375`, primary_mae `0.018006`, avg `-0.009069`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.046956`, avg `0.017106`, median `0.023936`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.084377`, avg `0.043231`, median `0.059313`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.1875`, primary_mae `0.011421`, avg `-0.006371`, median `-0.00667`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.014796`, avg `-0.005145`, median `-0.001347`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.1875`, primary_mae `0.026889`, avg `-0.004251`, median `-0.000739`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.058175`, avg `-0.005319`, median `0.006641`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.044855`, avg `-0.035023`, median `-0.043993`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.012453`, avg `-0.004399`, median `-0.005904`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.016854`, avg `-0.005857`, median `-0.004256`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.023047`, avg `-0.00131`, median `-0.003425`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.055438`, avg `0.0053`, median `0.00995`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.070619`, avg `0.006851`, median `-0.00576`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.012453`, avg `-0.004399`, median `-0.005904`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.016854`, avg `-0.005857`, median `-0.004256`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.023047`, avg `-0.00131`, median `-0.003425`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.055438`, avg `0.0053`, median `0.00995`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.070619`, avg `0.006851`, median `-0.00576`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3333`, primary_closer `0.6333`, primary_mae `0.013306`, avg `-0.003518`, median `-0.00397`
- 5d: sample `60`, primary_hit `0.3667`, primary_closer `0.5333`, primary_mae `0.017676`, avg `-0.005997`, median `-0.005474`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.5`, primary_mae `0.022567`, avg `-7.7e-05`, median `-0.003912`
- 20d: sample `60`, primary_hit `0.5167`, primary_closer `0.4`, primary_mae `0.054089`, avg `0.007743`, median `0.00995`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.5833`, primary_mae `0.080836`, avg `0.01891`, median `0.012182`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.8`, primary_closer `0.2`, primary_mae `0.009891`, avg `-0.007043`, median `-0.008115`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.014389`, avg `-0.005437`, median `-5e-05`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.25`, primary_mae `0.024489`, avg `-0.005011`, median `-0.003297`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.059485`, avg `-0.002027`, median `0.009366`
- 60d: sample `20`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.039969`, avg `-0.029323`, median `-0.03329`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.012453`, avg `-0.004399`, median `-0.005904`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.016854`, avg `-0.005857`, median `-0.004256`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.023047`, avg `-0.00131`, median `-0.003425`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.055438`, avg `0.0053`, median `0.00995`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.070619`, avg `0.006851`, median `-0.00576`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.012453`, avg `-0.004399`, median `-0.005904`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.5125`, primary_mae `0.016854`, avg `-0.005857`, median `-0.004256`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.023047`, avg `-0.00131`, median `-0.003425`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.055438`, avg `0.0053`, median `0.00995`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.070619`, avg `0.006851`, median `-0.00576`

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
