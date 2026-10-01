# Historical Replay Benchmark

Generated at: `2026-10-01T00:11:11.593244+00:00`
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
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.016704`
- secondary_mean_absolute_error: `0.015638`
- primary_error_advantage: `-0.001066`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.018805`
- secondary_mean_absolute_error: `0.017927`
- primary_error_advantage: `-0.000878`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.023792`
- secondary_mean_absolute_error: `0.023162`
- primary_error_advantage: `-0.00063`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2375`
- secondary_hit_rate: `0.7625`
- primary_vs_secondary_accuracy_spread: `-0.525`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.050244`
- secondary_mean_absolute_error: `0.035712`
- primary_error_advantage: `-0.014532`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1`
- secondary_hit_rate: `0.9`
- primary_vs_secondary_accuracy_spread: `-0.8`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.052224`
- secondary_mean_absolute_error: `0.040794`
- primary_error_advantage: `-0.01143`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.016046`, as_primary `0`, as_primary_hit `None`, avg `-0.001217`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.019125`, as_primary `0`, as_primary_hit `None`, avg `0.000884`, median `-0.001427`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.026398`, as_primary `0`, as_primary_hit `None`, avg `0.005449`, median `0.006554`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.036193`, as_primary `0`, as_primary_hit `None`, avg `0.028177`, median `0.032731`
- 60d: sample `80`, direction_hit `0.9`, path_mae `0.042808`, as_primary `0`, as_primary_hit `None`, avg `0.090182`, median `0.10578`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.017363`, as_primary `0`, as_primary_hit `None`, avg `-0.001217`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.021045`, as_primary `0`, as_primary_hit `None`, avg `0.000884`, median `-0.001427`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.031756`, as_primary `0`, as_primary_hit `None`, avg `0.005449`, median `0.006554`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.051451`, as_primary `0`, as_primary_hit `None`, avg `0.028177`, median `0.032731`
- 60d: sample `80`, direction_hit `0.9`, path_mae `0.048736`, as_primary `0`, as_primary_hit `None`, avg `0.090182`, median `0.10578`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.016704`, as_primary `80`, as_primary_hit `0.475`, avg `-0.001217`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.018805`, as_primary `80`, as_primary_hit `0.4875`, avg `0.000884`, median `-0.001427`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.023792`, as_primary `80`, as_primary_hit `0.6125`, avg `0.005449`, median `0.006554`
- 20d: sample `80`, direction_hit `0.2375`, path_mae `0.050244`, as_primary `80`, as_primary_hit `0.7625`, avg `0.028177`, median `0.032731`
- 60d: sample `80`, direction_hit `0.1`, path_mae `0.052224`, as_primary `80`, as_primary_hit `0.9`, avg `0.090182`, median `0.10578`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.015691`, as_primary `0`, as_primary_hit `None`, avg `-0.001217`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.017964`, as_primary `0`, as_primary_hit `None`, avg `0.000884`, median `-0.001427`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.023137`, as_primary `0`, as_primary_hit `None`, avg `0.005449`, median `0.006554`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.032167`, as_primary `0`, as_primary_hit `None`, avg `0.028177`, median `0.032731`
- 60d: sample `80`, direction_hit `0.9`, path_mae `0.041142`, as_primary `0`, as_primary_hit `None`, avg `0.090182`, median `0.10578`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.013198`, avg `0.005675`, median `0.010739`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.015366`, avg `0.007865`, median `0.009975`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.018966`, avg `0.011045`, median `0.014434`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.5`, primary_mae `0.04052`, avg `0.033933`, median `0.033084`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.65`, primary_mae `0.038784`, avg `0.084843`, median `0.104666`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.45`, primary_mae `0.017872`, avg `-0.003515`, median `-0.003098`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.5`, primary_mae `0.019952`, avg `-0.001444`, median `-0.005714`
- 10d: sample `60`, primary_hit `0.4167`, primary_closer `0.45`, primary_mae `0.025401`, avg `0.003584`, median `0.004251`
- 20d: sample `60`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.053485`, avg `0.026259`, median `0.032731`
- 60d: sample `60`, primary_hit `0.1`, primary_closer `0.3833`, primary_mae `0.056704`, avg `0.091962`, median `0.10578`

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
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.017526`, avg `-0.00724`, median `-0.010089`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.021373`, avg `-0.004168`, median `-0.005714`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.034128`, avg `-0.002528`, median `-0.003925`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.070794`, avg `-0.002695`, median `0.005418`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.4`, primary_mae `0.035889`, avg `0.114468`, median `0.115176`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.013265`, avg `0.002969`, median `0.004286`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.01446`, avg `0.003947`, median `0.005603`
- 10d: sample `40`, primary_hit `0.25`, primary_closer `0.425`, primary_mae `0.017024`, avg `0.009233`, median `0.009969`
- 20d: sample `40`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.041671`, avg `0.036903`, median `0.038653`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.55`, primary_mae `0.037642`, avg `0.090629`, median `0.10578`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.022759`, avg `-0.003568`, median `-0.006849`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.024928`, avg `-0.000192`, median `-0.012844`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.026995`, avg `0.005861`, median `-0.000753`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.04684`, avg `0.041599`, median `0.029993`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.097723`, avg `0.065002`, median `0.055391`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.013265, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.01446, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.017024, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.041671, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.035889, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015691, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017363, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.013265, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017964, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021045, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.01446, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023137, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031756, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.017024, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_vs_secondary_accuracy_spread': -0.525, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032167, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051451, 'direction_hit_rate': 0.7625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.041671, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1, 'secondary_hit_rate': 0.9, 'primary_vs_secondary_accuracy_spread': -0.8, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041142, 'direction_hit_rate': 0.9}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052224, 'direction_hit_rate': 0.1}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.035889, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.013124`, avg `0.005815`, median `0.008014`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.015499`, avg `0.006695`, median `0.008828`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.014721`, avg `0.009347`, median `0.01205`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.035436`, avg `0.026788`, median `0.029102`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.5`, primary_mae `0.0093`, avg `0.114868`, median `0.11635`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.015847`, avg `0.003724`, median `0.003357`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.015717`, avg `0.005681`, median `0.008828`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.01823`, avg `0.008671`, median `0.014434`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.4375`, primary_mae `0.039324`, avg `0.032252`, median `0.036357`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.5625`, primary_mae `0.031539`, avg `0.094375`, median `0.111461`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.017602`, avg `-0.006554`, median `-0.010376`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.019853`, avg `-0.003422`, median `-0.005714`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.034537`, avg `-0.001776`, median `-0.003925`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.065928`, avg `-0.007903`, median `-0.016989`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.4375`, primary_mae `0.029647`, avg `0.12167`, median `0.122732`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.016704`, avg `-0.001217`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.018805`, avg `0.000884`, median `-0.001427`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.023792`, avg `0.005449`, median `0.006554`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.35`, primary_mae `0.050244`, avg `0.028177`, median `0.032731`
- 60d: sample `80`, primary_hit `0.1`, primary_closer `0.45`, primary_mae `0.052224`, avg `0.090182`, median `0.10578`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.016704`, avg `-0.001217`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.018805`, avg `0.000884`, median `-0.001427`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.023792`, avg `0.005449`, median `0.006554`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.35`, primary_mae `0.050244`, avg `0.028177`, median `0.032731`
- 60d: sample `80`, primary_hit `0.1`, primary_closer `0.45`, primary_mae `0.052224`, avg `0.090182`, median `0.10578`

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
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.016704`, avg `-0.001217`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.018805`, avg `0.000884`, median `-0.001427`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.023792`, avg `0.005449`, median `0.006554`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.35`, primary_mae `0.050244`, avg `0.028177`, median `0.032731`
- 60d: sample `80`, primary_hit `0.1`, primary_closer `0.45`, primary_mae `0.052224`, avg `0.090182`, median `0.10578`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4625`, primary_mae `0.016704`, avg `-0.001217`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.018805`, avg `0.000884`, median `-0.001427`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.023792`, avg `0.005449`, median `0.006554`
- 20d: sample `80`, primary_hit `0.2375`, primary_closer `0.35`, primary_mae `0.050244`, avg `0.028177`, median `0.032731`
- 60d: sample `80`, primary_hit `0.1`, primary_closer `0.45`, primary_mae `0.052224`, avg `0.090182`, median `0.10578`

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
