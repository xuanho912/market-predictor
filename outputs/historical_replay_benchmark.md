# Historical Replay Benchmark

Generated at: `2026-11-10T04:24:41.018706+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
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
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.017865`
- secondary_mean_absolute_error: `0.01738`
- primary_error_advantage: `-0.000485`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.020885`
- secondary_mean_absolute_error: `0.021963`
- primary_error_advantage: `0.001078`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.043164`
- secondary_mean_absolute_error: `0.036962`
- primary_error_advantage: `-0.006202`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.063697`
- secondary_mean_absolute_error: `0.049055`
- primary_error_advantage: `-0.014642`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.046104`
- secondary_mean_absolute_error: `0.051357`
- primary_error_advantage: `0.005253`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.7`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.017094`, as_primary `0`, as_primary_hit `None`, avg `0.0051`, median `0.007269`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.022481`, as_primary `0`, as_primary_hit `None`, avg `0.009923`, median `0.007798`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.029852`, as_primary `0`, as_primary_hit `None`, avg `0.017436`, median `0.021348`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.035867`, as_primary `0`, as_primary_hit `None`, avg `0.026853`, median `0.031988`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.036798`, as_primary `0`, as_primary_hit `None`, avg `0.050551`, median `0.060948`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.018896`, as_primary `20`, as_primary_hit `0.65`, avg `0.0051`, median `0.007269`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.02753`, as_primary `20`, as_primary_hit `0.75`, avg `0.009923`, median `0.007798`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.038856`, as_primary `20`, as_primary_hit `0.85`, avg `0.017436`, median `0.021348`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.049561`, as_primary `20`, as_primary_hit `0.7`, avg `0.026853`, median `0.031988`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.045959`, as_primary `20`, as_primary_hit `0.75`, avg `0.050551`, median `0.060948`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.018651`, as_primary `60`, as_primary_hit `0.6333`, avg `0.0051`, median `0.007269`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.020856`, as_primary `60`, as_primary_hit `0.5833`, avg `0.009923`, median `0.007798`
- 10d: sample `80`, direction_hit `0.2875`, path_mae `0.045456`, as_primary `60`, as_primary_hit `0.6667`, avg `0.017436`, median `0.021348`
- 20d: sample `80`, direction_hit `0.2625`, path_mae `0.069509`, as_primary `60`, as_primary_hit `0.75`, avg `0.026853`, median `0.031988`
- 60d: sample `80`, direction_hit `0.1875`, path_mae `0.052494`, as_primary `60`, as_primary_hit `0.8333`, avg `0.050551`, median `0.060948`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.016256`, as_primary `0`, as_primary_hit `None`, avg `0.0051`, median `0.007269`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.02009`, as_primary `0`, as_primary_hit `None`, avg `0.009923`, median `0.007798`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.029717`, as_primary `0`, as_primary_hit `None`, avg `0.017436`, median `0.021348`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.036344`, as_primary `0`, as_primary_hit `None`, avg `0.026853`, median `0.031988`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.036765`, as_primary `0`, as_primary_hit `None`, avg `0.050551`, median `0.060948`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.017865`, avg `0.0051`, median `0.007269`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020885`, avg `0.009923`, median `0.007798`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.043164`, avg `0.017436`, median `0.021348`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.063697`, avg `0.026853`, median `0.031988`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.475`, primary_mae `0.046104`, avg `0.050551`, median `0.060948`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.017865`, avg `0.0051`, median `0.007269`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020885`, avg `0.009923`, median `0.007798`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.043164`, avg `0.017436`, median `0.021348`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.063697`, avg `0.026853`, median `0.031988`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.475`, primary_mae `0.046104`, avg `0.050551`, median `0.060948`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.017865, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.020885, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4625, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.043164, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3625, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.063697, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3125, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.046104, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016256, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018896, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.017865, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02009, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02753, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.020885, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029717, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045456, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4625, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.043164, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035867, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069509, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3625, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.063697, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036765, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052494, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3125, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.046104, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.020334`, avg `0.011527`, median `0.019294`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.125`, primary_mae `0.030955`, avg `0.024533`, median `0.032263`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.031844`, avg `0.026699`, median `0.035162`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.037885`, avg `0.031554`, median `0.051313`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.057236`, avg `0.036447`, median `0.055914`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.020378`, avg `0.002314`, median `0.009841`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.023804`, avg `0.013972`, median `0.016506`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.5625`, primary_mae `0.032941`, avg `0.020825`, median `0.019849`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.048855`, avg `0.020787`, median `0.037272`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.056663`, avg `0.039513`, median `0.052516`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.020083`, avg `0.010562`, median `0.011246`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.025443`, avg `0.014272`, median `0.006005`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.069006`, avg `0.01505`, median `0.034572`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.100033`, avg `0.041214`, median `0.054498`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.3125`, primary_mae `0.028633`, avg `0.077497`, median `0.077786`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.017865`, avg `0.0051`, median `0.007269`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020885`, avg `0.009923`, median `0.007798`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.043164`, avg `0.017436`, median `0.021348`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.063697`, avg `0.026853`, median `0.031988`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.475`, primary_mae `0.046104`, avg `0.050551`, median `0.060948`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.017865`, avg `0.0051`, median `0.007269`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020885`, avg `0.009923`, median `0.007798`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.043164`, avg `0.017436`, median `0.021348`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.063697`, avg `0.026853`, median `0.031988`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.475`, primary_mae `0.046104`, avg `0.050551`, median `0.060948`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.6`, primary_mae `0.014909`, avg `0.001102`, median `0.006346`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.019099`, avg `0.008439`, median `0.010083`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.033022`, avg `0.014582`, median `0.014615`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.049891`, avg `0.01855`, median `0.023856`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.051634`, avg `0.038068`, median `0.044361`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.020821`, avg `0.009099`, median `0.009971`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.022672`, avg `0.011407`, median `0.004838`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.3`, primary_mae `0.053305`, avg `0.020291`, median `0.032272`
- 20d: sample `40`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.077503`, avg `0.035156`, median `0.047263`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.325`, primary_mae `0.040575`, avg `0.063034`, median `0.0728`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.017865`, avg `0.0051`, median `0.007269`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020885`, avg `0.009923`, median `0.007798`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.043164`, avg `0.017436`, median `0.021348`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.063697`, avg `0.026853`, median `0.031988`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.475`, primary_mae `0.046104`, avg `0.050551`, median `0.060948`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.017865`, avg `0.0051`, median `0.007269`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020885`, avg `0.009923`, median `0.007798`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.043164`, avg `0.017436`, median `0.021348`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.063697`, avg `0.026853`, median `0.031988`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.475`, primary_mae `0.046104`, avg `0.050551`, median `0.060948`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.017865`, avg `0.0051`, median `0.007269`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020885`, avg `0.009923`, median `0.007798`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.043164`, avg `0.017436`, median `0.021348`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.063697`, avg `0.026853`, median `0.031988`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.475`, primary_mae `0.046104`, avg `0.050551`, median `0.060948`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.017865`, avg `0.0051`, median `0.007269`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020885`, avg `0.009923`, median `0.007798`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.043164`, avg `0.017436`, median `0.021348`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.063697`, avg `0.026853`, median `0.031988`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.475`, primary_mae `0.046104`, avg `0.050551`, median `0.060948`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
