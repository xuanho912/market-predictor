# Historical Replay Benchmark

Generated at: `2026-07-31T14:38:38.331387+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.023678`
- secondary_mean_absolute_error: `0.017528`
- primary_error_advantage: `-0.00615`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.027313`
- secondary_mean_absolute_error: `0.020135`
- primary_error_advantage: `-0.007178`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.035887`
- secondary_mean_absolute_error: `0.02546`
- primary_error_advantage: `-0.010427`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.073537`
- secondary_mean_absolute_error: `0.048773`
- primary_error_advantage: `-0.024764`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.115011`
- secondary_mean_absolute_error: `0.087526`
- primary_error_advantage: `-0.027485`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.01739`, as_primary `0`, as_primary_hit `None`, avg `-0.001571`, median `0.000655`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.019772`, as_primary `0`, as_primary_hit `None`, avg `-0.004434`, median `-0.001935`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.022977`, as_primary `0`, as_primary_hit `None`, avg `0.002723`, median `-0.000315`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.040532`, as_primary `0`, as_primary_hit `None`, avg `0.009304`, median `0.01543`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.076243`, as_primary `0`, as_primary_hit `None`, avg `0.003195`, median `0.009193`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.019623`, as_primary `0`, as_primary_hit `None`, avg `-0.001571`, median `0.000655`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.023716`, as_primary `0`, as_primary_hit `None`, avg `-0.004434`, median `-0.001935`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.02899`, as_primary `0`, as_primary_hit `None`, avg `0.002723`, median `-0.000315`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.061196`, as_primary `0`, as_primary_hit `None`, avg `0.009304`, median `0.01543`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.098406`, as_primary `0`, as_primary_hit `None`, avg `0.003195`, median `0.009193`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.023678`, as_primary `80`, as_primary_hit `0.525`, avg `-0.001571`, median `0.000655`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.027313`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.004434`, median `-0.001935`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.035887`, as_primary `80`, as_primary_hit `0.4875`, avg `0.002723`, median `-0.000315`
- 20d: sample `80`, direction_hit `0.4125`, path_mae `0.073537`, as_primary `80`, as_primary_hit `0.5875`, avg `0.009304`, median `0.01543`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.115011`, as_primary `80`, as_primary_hit `0.525`, avg `0.003195`, median `0.009193`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.017233`, as_primary `0`, as_primary_hit `None`, avg `-0.001571`, median `0.000655`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.01961`, as_primary `0`, as_primary_hit `None`, avg `-0.004434`, median `-0.001935`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.022552`, as_primary `0`, as_primary_hit `None`, avg `0.002723`, median `-0.000315`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.039766`, as_primary `0`, as_primary_hit `None`, avg `0.009304`, median `0.01543`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.077313`, as_primary `0`, as_primary_hit `None`, avg `0.003195`, median `0.009193`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3375`, primary_mae `0.023678`, avg `-0.001571`, median `0.000655`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.027313`, avg `-0.004434`, median `-0.001935`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3875`, primary_mae `0.035887`, avg `0.002723`, median `-0.000315`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.073537`, avg `0.009304`, median `0.01543`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.115011`, avg `0.003195`, median `0.009193`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.3333`, primary_mae `0.022664`, avg `0.000452`, median `0.000737`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.3667`, primary_mae `0.026662`, avg `-0.001185`, median `-0.000821`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.3`, primary_mae `0.041614`, avg `0.005339`, median `0.009991`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.3167`, primary_mae `0.075566`, avg `0.008653`, median `0.015131`
- 60d: sample `60`, primary_hit `0.5167`, primary_closer `0.4`, primary_mae `0.118322`, avg `-0.005771`, median `-0.003041`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.026719`, avg `-0.007641`, median `-0.005521`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.029265`, avg `-0.014181`, median `-0.01025`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.018706`, avg `-0.005124`, median `-0.009105`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.06745`, avg `0.011254`, median `0.018406`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.105078`, avg `0.030096`, median `0.041779`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3333, 'primary_mean_absolute_error': 0.022664, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.026662, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.018706, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.06745, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.105078, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017233, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023678, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3333, 'primary_mean_absolute_error': 0.022664, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01961, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027313, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.026662, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022552, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035887, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.018706, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039766, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073537, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.06745, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076243, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.115011, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.105078, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.016785`, avg `-0.019064`, median `-0.028431`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.018332`, avg `-0.026817`, median `-0.028941`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.013111`, avg `-0.012517`, median `-0.009593`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.059915`, avg `0.009732`, median `0.009201`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.095491`, avg `0.027859`, median `0.024759`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.024464`, avg `-0.009658`, median `-0.005521`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.029156`, avg `-0.015439`, median `-0.01025`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.019539`, avg `-0.005228`, median `-0.007383`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.070296`, avg `0.01217`, median `0.024617`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.116366`, avg `0.039546`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.019195`, avg `-0.004424`, median `-0.003306`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.025192`, avg `-0.01273`, median `-0.011636`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.04817`, avg `-0.003777`, median `0.009991`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.096005`, avg `-0.007358`, median `0.01001`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.151652`, avg `-0.046709`, median `-0.031034`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3375`, primary_mae `0.023678`, avg `-0.001571`, median `0.000655`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.027313`, avg `-0.004434`, median `-0.001935`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3875`, primary_mae `0.035887`, avg `0.002723`, median `-0.000315`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.073537`, avg `0.009304`, median `0.01543`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.115011`, avg `0.003195`, median `0.009193`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3375`, primary_mae `0.023678`, avg `-0.001571`, median `0.000655`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.027313`, avg `-0.004434`, median `-0.001935`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3875`, primary_mae `0.035887`, avg `0.002723`, median `-0.000315`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.073537`, avg `0.009304`, median `0.01543`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.115011`, avg `0.003195`, median `0.009193`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.019658`, avg `-0.004618`, median `-4.2e-05`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.020243`, avg `-0.009167`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.725`, primary_closer `0.55`, primary_mae `0.018982`, avg `-0.00743`, median `-0.010169`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.060108`, avg `-0.000452`, median `-0.002732`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.083199`, avg `0.014418`, median `0.003188`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.027698`, avg `0.001475`, median `0.005624`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.25`, primary_mae `0.034383`, avg `0.000298`, median `-0.00269`
- 10d: sample `40`, primary_hit `0.3`, primary_closer `0.225`, primary_mae `0.052793`, avg `0.012876`, median `0.023894`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.086965`, avg `0.019059`, median `0.029128`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.146823`, avg `-0.008027`, median `0.026861`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3375`, primary_mae `0.023678`, avg `-0.001571`, median `0.000655`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.027313`, avg `-0.004434`, median `-0.001935`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.3875`, primary_mae `0.035887`, avg `0.002723`, median `-0.000315`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.073537`, avg `0.009304`, median `0.01543`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.115011`, avg `0.003195`, median `0.009193`

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
