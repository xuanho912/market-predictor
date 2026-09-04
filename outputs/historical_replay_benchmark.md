# Historical Replay Benchmark

Generated at: `2026-09-04T16:25:43.757413+00:00`
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
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.021617`
- secondary_mean_absolute_error: `0.01451`
- primary_error_advantage: `-0.007107`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.020737`
- secondary_mean_absolute_error: `0.016619`
- primary_error_advantage: `-0.004118`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.3625`
- primary_vs_secondary_accuracy_spread: `0.275`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.029665`
- secondary_mean_absolute_error: `0.029024`
- primary_error_advantage: `-0.000641`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.055709`
- secondary_mean_absolute_error: `0.039401`
- primary_error_advantage: `-0.016308`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.083081`
- secondary_mean_absolute_error: `0.065931`
- primary_error_advantage: `-0.01715`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.015658`, as_primary `0`, as_primary_hit `None`, avg `-0.002781`, median `-0.001522`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.016833`, as_primary `0`, as_primary_hit `None`, avg `-0.001319`, median `0.000552`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.02304`, as_primary `0`, as_primary_hit `None`, avg `-0.001592`, median `-0.010434`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.030192`, as_primary `0`, as_primary_hit `None`, avg `0.005771`, median `0.017159`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.055588`, as_primary `0`, as_primary_hit `None`, avg `0.024809`, median `0.040414`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.014649`, as_primary `0`, as_primary_hit `None`, avg `-0.002781`, median `-0.001522`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.017405`, as_primary `0`, as_primary_hit `None`, avg `-0.001319`, median `0.000552`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.0312`, as_primary `0`, as_primary_hit `None`, avg `-0.001592`, median `-0.010434`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.044176`, as_primary `0`, as_primary_hit `None`, avg `0.005771`, median `0.017159`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.070373`, as_primary `0`, as_primary_hit `None`, avg `0.024809`, median `0.040414`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.021617`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.002781`, median `-0.001522`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.020737`, as_primary `80`, as_primary_hit `0.525`, avg `-0.001319`, median `0.000552`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.029665`, as_primary `80`, as_primary_hit `0.3625`, avg `-0.001592`, median `-0.010434`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.055709`, as_primary `80`, as_primary_hit `0.625`, avg `0.005771`, median `0.017159`
- 60d: sample `80`, direction_hit `0.3625`, path_mae `0.083081`, as_primary `80`, as_primary_hit `0.6375`, avg `0.024809`, median `0.040414`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.014624`, as_primary `0`, as_primary_hit `None`, avg `-0.002781`, median `-0.001522`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.016296`, as_primary `0`, as_primary_hit `None`, avg `-0.001319`, median `0.000552`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.022364`, as_primary `0`, as_primary_hit `None`, avg `-0.001592`, median `-0.010434`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.030557`, as_primary `0`, as_primary_hit `None`, avg `0.005771`, median `0.017159`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.056379`, as_primary `0`, as_primary_hit `None`, avg `0.024809`, median `0.040414`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.275`, primary_mae `0.021617`, avg `-0.002781`, median `-0.001522`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.3875`, primary_mae `0.020737`, avg `-0.001319`, median `0.000552`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.029665`, avg `-0.001592`, median `-0.010434`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3375`, primary_mae `0.055709`, avg `0.005771`, median `0.017159`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.083081`, avg `0.024809`, median `0.040414`

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
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.013173`, avg `-0.005217`, median `-0.004974`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.013985`, avg `-0.004146`, median `0.000725`
- 10d: sample `20`, primary_hit `0.9`, primary_closer `0.6`, primary_mae `0.017938`, avg `-0.015992`, median `-0.01712`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.060858`, avg `-0.025923`, median `-0.020035`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.063417`, avg `-0.013727`, median `-0.019635`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.3`, primary_mae `0.024432`, avg `-0.001969`, median `0.001087`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.4167`, primary_mae `0.022987`, avg `-0.000376`, median `0.000311`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.033574`, avg `0.003208`, median `-0.004843`
- 20d: sample `60`, primary_hit `0.2667`, primary_closer `0.3`, primary_mae `0.053992`, avg `0.016336`, median `0.024711`
- 60d: sample `60`, primary_hit `0.2667`, primary_closer `0.35`, primary_mae `0.089636`, avg `0.037654`, median `0.060929`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.013173, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.013985, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.9, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.017938, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2667, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.053992, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.063417, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014624, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021617, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.013173, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016296, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020737, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.013985, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_vs_secondary_accuracy_spread': 0.275, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022364, 'direction_hit_rate': 0.3625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0312, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.9, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.017938, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030192, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055709, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2667, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.053992, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055588, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.083081, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.063417, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.037962`, avg `0.004554`, median `0.006871`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.034578`, avg `0.010971`, median `0.007438`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.039923`, avg `0.002929`, median `0.001264`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.067242`, avg `0.011715`, median `0.028092`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.077478`, avg `-0.014287`, median `-0.004446`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.036995`, avg `-1.1e-05`, median `0.003489`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.036436`, avg `0.008832`, median `0.009264`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.046862`, avg `0.007305`, median `0.002658`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.066978`, avg `0.017324`, median `0.034463`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.111563`, avg `0.023682`, median `0.041664`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.012221`, avg `-0.006725`, median `-0.00849`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.013928`, avg `-0.005293`, median `0.000725`
- 10d: sample `16`, primary_hit `0.9375`, primary_closer `0.5625`, primary_mae `0.016655`, avg `-0.017102`, median `-0.015308`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.064156`, avg `-0.023422`, median `-0.011784`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.066583`, avg `-0.009464`, median `-0.01182`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.275`, primary_mae `0.021617`, avg `-0.002781`, median `-0.001522`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.3875`, primary_mae `0.020737`, avg `-0.001319`, median `0.000552`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.029665`, avg `-0.001592`, median `-0.010434`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3375`, primary_mae `0.055709`, avg `0.005771`, median `0.017159`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.083081`, avg `0.024809`, median `0.040414`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.275`, primary_mae `0.021617`, avg `-0.002781`, median `-0.001522`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.3875`, primary_mae `0.020737`, avg `-0.001319`, median `0.000552`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.029665`, avg `-0.001592`, median `-0.010434`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3375`, primary_mae `0.055709`, avg `0.005771`, median `0.017159`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.083081`, avg `0.024809`, median `0.040414`

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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.2833`, primary_mae `0.017011`, avg `-0.002788`, median `-0.001735`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.4333`, primary_mae `0.016252`, avg `-0.003083`, median `-0.003439`
- 10d: sample `60`, primary_hit `0.6667`, primary_closer `0.4667`, primary_mae `0.02535`, avg `-0.002772`, median `-0.010434`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.35`, primary_mae `0.053949`, avg `0.003526`, median `0.01374`
- 60d: sample `60`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.076126`, avg `0.02854`, median `0.047922`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.275`, primary_mae `0.021617`, avg `-0.002781`, median `-0.001522`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.3875`, primary_mae `0.020737`, avg `-0.001319`, median `0.000552`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.029665`, avg `-0.001592`, median `-0.010434`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3375`, primary_mae `0.055709`, avg `0.005771`, median `0.017159`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.083081`, avg `0.024809`, median `0.040414`

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
