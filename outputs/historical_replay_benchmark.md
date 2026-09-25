# Historical Replay Benchmark

Generated at: `2026-09-25T01:34:33.750863+00:00`
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
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.016789`
- secondary_mean_absolute_error: `0.014221`
- primary_error_advantage: `-0.002568`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.022048`
- secondary_mean_absolute_error: `0.017985`
- primary_error_advantage: `-0.004063`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.037808`
- secondary_mean_absolute_error: `0.027948`
- primary_error_advantage: `-0.00986`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.064721`
- secondary_mean_absolute_error: `0.045856`
- primary_error_advantage: `-0.018865`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.06489`
- secondary_mean_absolute_error: `0.044757`
- primary_error_advantage: `-0.020133`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.014868`, as_primary `0`, as_primary_hit `None`, avg `-0.00234`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.017998`, as_primary `0`, as_primary_hit `None`, avg `-0.002953`, median `0.000899`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.027591`, as_primary `0`, as_primary_hit `None`, avg `8.5e-05`, median `0.006147`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.038141`, as_primary `0`, as_primary_hit `None`, avg `0.015202`, median `0.020358`
- 60d: sample `80`, direction_hit `0.875`, path_mae `0.043522`, as_primary `0`, as_primary_hit `None`, avg `0.061996`, median `0.07908`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.014456`, as_primary `20`, as_primary_hit `0.65`, avg `-0.00234`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.017685`, as_primary `20`, as_primary_hit `0.65`, avg `-0.002953`, median `0.000899`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.031105`, as_primary `20`, as_primary_hit `0.75`, avg `8.5e-05`, median `0.006147`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.055272`, as_primary `20`, as_primary_hit `0.8`, avg `0.015202`, median `0.020358`
- 60d: sample `80`, direction_hit `0.875`, path_mae `0.043612`, as_primary `20`, as_primary_hit `1.0`, avg `0.061996`, median `0.07908`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.016773`, as_primary `60`, as_primary_hit `0.4333`, avg `-0.00234`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.022119`, as_primary `60`, as_primary_hit `0.4833`, avg `-0.002953`, median `0.000899`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.037728`, as_primary `60`, as_primary_hit `0.55`, avg `8.5e-05`, median `0.006147`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.06548`, as_primary `60`, as_primary_hit `0.6333`, avg `0.015202`, median `0.020358`
- 60d: sample `80`, direction_hit `0.125`, path_mae `0.064449`, as_primary `60`, as_primary_hit `0.8333`, avg `0.061996`, median `0.07908`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.014447`, as_primary `0`, as_primary_hit `None`, avg `-0.00234`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.017689`, as_primary `0`, as_primary_hit `None`, avg `-0.002953`, median `0.000899`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.027817`, as_primary `0`, as_primary_hit `None`, avg `8.5e-05`, median `0.006147`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.038192`, as_primary `0`, as_primary_hit `None`, avg `0.015202`, median `0.020358`
- 60d: sample `80`, direction_hit `0.875`, path_mae `0.044759`, as_primary `0`, as_primary_hit `None`, avg `0.061996`, median `0.07908`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.016789`, avg `-0.00234`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.022048`, avg `-0.002953`, median `0.000899`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.037808`, avg `8.5e-05`, median `0.006147`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.064721`, avg `0.015202`, median `0.020358`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.06489`, avg `0.061996`, median `0.07908`

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
- 3d: sample `60`, primary_hit `0.5667`, primary_closer `0.4167`, primary_mae `0.018082`, avg `-0.004905`, median `-0.003662`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.3833`, primary_mae `0.02413`, avg `-0.006697`, median `-0.003597`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.043548`, avg `-0.004399`, median `0.004921`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.3333`, primary_mae `0.073364`, avg `0.008522`, median `0.015571`
- 60d: sample `60`, primary_hit `0.1667`, primary_closer `0.2667`, primary_mae `0.077257`, avg `0.049552`, median `0.055681`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.012911`, avg `0.005357`, median `0.008375`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.015804`, avg `0.008277`, median `0.009975`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.020587`, avg `0.013538`, median `0.016702`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.5`, primary_mae `0.038792`, avg `0.035241`, median `0.032756`
- 60d: sample `20`, primary_hit `1.0`, primary_closer `0.4`, primary_mae `0.027788`, avg `0.09933`, median `0.107717`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.012911, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.015804, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.020587, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.038792, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 1.0, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.027788, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014447, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016773, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.012911, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017685, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022119, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.015804, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027591, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037728, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.020587, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038141, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06548, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.038792, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043522, 'direction_hit_rate': 0.875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064449, 'direction_hit_rate': 0.125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 1.0, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.027788, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.012832`, avg `0.005815`, median `0.008014`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.014792`, avg `0.006695`, median `0.008828`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.01658`, avg `0.009347`, median `0.01205`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.045009`, avg `0.026788`, median `0.029102`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.009937`, avg `0.114868`, median `0.11635`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.01366`, avg `0.001739`, median `0.003357`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.016449`, avg `0.006766`, median `0.008828`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.019817`, avg `0.010293`, median `0.016702`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.041111`, avg `0.031248`, median `0.029448`
- 60d: sample `16`, primary_hit `1.0`, primary_closer `0.4375`, primary_mae `0.027217`, avg `0.099981`, median `0.111461`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.023508`, avg `-0.018385`, median `-0.012143`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.02916`, avg `-0.018561`, median `-0.017304`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.053685`, avg `-0.005562`, median `-0.006323`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.088744`, avg `0.015243`, median `0.034922`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.10744`, avg `0.076472`, median `0.114142`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.016789`, avg `-0.00234`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.022048`, avg `-0.002953`, median `0.000899`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.037808`, avg `8.5e-05`, median `0.006147`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.064721`, avg `0.015202`, median `0.020358`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.06489`, avg `0.061996`, median `0.07908`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.016789`, avg `-0.00234`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.022048`, avg `-0.002953`, median `0.000899`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.037808`, avg `8.5e-05`, median `0.006147`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.064721`, avg `0.015202`, median `0.020358`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.06489`, avg `0.061996`, median `0.07908`

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
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.016789`, avg `-0.00234`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.022048`, avg `-0.002953`, median `0.000899`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.037808`, avg `8.5e-05`, median `0.006147`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.064721`, avg `0.015202`, median `0.020358`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.06489`, avg `0.061996`, median `0.07908`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.016789`, avg `-0.00234`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.022048`, avg `-0.002953`, median `0.000899`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.037808`, avg `8.5e-05`, median `0.006147`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.064721`, avg `0.015202`, median `0.020358`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.06489`, avg `0.061996`, median `0.07908`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.016789`, avg `-0.00234`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.022048`, avg `-0.002953`, median `0.000899`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.037808`, avg `8.5e-05`, median `0.006147`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.064721`, avg `0.015202`, median `0.020358`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.06489`, avg `0.061996`, median `0.07908`

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
