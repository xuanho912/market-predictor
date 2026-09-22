# Historical Replay Benchmark

Generated at: `2026-09-22T17:00:32.793947+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `PROMISING`
Overfit warning: `{'level': 'low', 'reasons': [], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_supportive_but_not_forward_validated`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.015607`
- secondary_mean_absolute_error: `0.016119`
- primary_error_advantage: `0.000512`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.01844`
- secondary_mean_absolute_error: `0.018282`
- primary_error_advantage: `-0.000158`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.026951`
- secondary_mean_absolute_error: `0.026794`
- primary_error_advantage: `-0.000157`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.6`
- primary_mean_absolute_error: `0.053186`
- secondary_mean_absolute_error: `0.06683`
- primary_error_advantage: `0.013644`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.074683`
- secondary_mean_absolute_error: `0.085182`
- primary_error_advantage: `0.010499`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.014167`, as_primary `0`, as_primary_hit `None`, avg `-0.00317`, median `-0.001439`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.015651`, as_primary `0`, as_primary_hit `None`, avg `-0.008777`, median `-0.007313`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.020775`, as_primary `0`, as_primary_hit `None`, avg `-0.010527`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.5375`, path_mae `0.037277`, as_primary `0`, as_primary_hit `None`, avg `0.001919`, median `0.002137`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.057989`, as_primary `0`, as_primary_hit `None`, avg `0.017003`, median `0.030631`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.016237`, as_primary `60`, as_primary_hit `0.5167`, avg `-0.00317`, median `-0.001439`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.018105`, as_primary `60`, as_primary_hit `0.5`, avg `-0.008777`, median `-0.007313`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.029097`, as_primary `60`, as_primary_hit `0.4`, avg `-0.010527`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.5375`, path_mae `0.057181`, as_primary `60`, as_primary_hit `0.6`, avg `0.001919`, median `0.002137`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.073309`, as_primary `60`, as_primary_hit `0.7`, avg `0.017003`, median `0.030631`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.015488`, as_primary `20`, as_primary_hit `0.3`, avg `-0.00317`, median `-0.001439`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.018618`, as_primary `20`, as_primary_hit `0.15`, avg `-0.008777`, median `-0.007313`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.024648`, as_primary `20`, as_primary_hit `0.2`, avg `-0.010527`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.4625`, path_mae `0.062835`, as_primary `20`, as_primary_hit `0.35`, avg `0.001919`, median `0.002137`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.086555`, as_primary `20`, as_primary_hit `0.6`, avg `0.017003`, median `0.030631`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.014047`, as_primary `0`, as_primary_hit `None`, avg `-0.00317`, median `-0.001439`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.015293`, as_primary `0`, as_primary_hit `None`, avg `-0.008777`, median `-0.007313`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.019327`, as_primary `0`, as_primary_hit `None`, avg `-0.010527`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.5375`, path_mae `0.03655`, as_primary `0`, as_primary_hit `None`, avg `0.001919`, median `0.002137`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.059763`, as_primary `0`, as_primary_hit `None`, avg `0.017003`, median `0.030631`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.5167`, primary_mae `0.016603`, avg `-0.003089`, median `0.001086`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017911`, avg `-0.007024`, median `-4e-06`
- 10d: sample `60`, primary_hit `0.4`, primary_closer `0.4333`, primary_mae `0.02739`, avg `-0.00565`, median `-0.007166`
- 20d: sample `60`, primary_hit `0.6`, primary_closer `0.5833`, primary_mae `0.047337`, avg `0.008197`, median `0.014286`
- 60d: sample `60`, primary_hit `0.7`, primary_closer `0.5833`, primary_mae `0.061284`, avg `0.021901`, median `0.034349`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.012617`, avg `-0.003414`, median `-0.003773`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.45`, primary_mae `0.020029`, avg `-0.014038`, median `-0.013615`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.75`, primary_mae `0.025634`, avg `-0.025159`, median `-0.032528`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.070735`, avg `-0.016913`, median `-0.03316`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.114878`, avg `0.002308`, median `0.019907`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.015385`, avg `-0.000285`, median `0.002996`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.017623`, avg `-0.00344`, median `0.001083`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.031731`, avg `-0.002409`, median `-0.005578`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.04271`, avg `0.009668`, median `0.014286`
- 60d: sample `40`, primary_hit `0.7`, primary_closer `0.575`, primary_mae `0.045253`, avg `0.01884`, median `0.029695`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.012617`, avg `-0.003414`, median `-0.003773`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.45`, primary_mae `0.020029`, avg `-0.014038`, median `-0.013615`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.75`, primary_mae `0.025634`, avg `-0.025159`, median `-0.032528`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.070735`, avg `-0.016913`, median `-0.03316`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.114878`, avg `0.002308`, median `0.019907`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.01904`, avg `-0.008696`, median `-0.009708`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.018485`, avg `-0.014191`, median `-0.012112`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.018706`, avg `-0.012133`, median `-0.013277`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.7`, primary_mae `0.056591`, avg `0.005254`, median `0.012154`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.093346`, avg `0.028024`, median `0.052632`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.012617, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017623, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.018706, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.04271, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.045253, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014047, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016237, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.012617, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015293, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018618, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017623, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019327, 'direction_hit_rate': 0.35}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029097, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.018706, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.6, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03655, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062835, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.04271, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057989, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.086555, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.045253, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.020321`, avg `-0.020054`, median `-0.02628`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.019313`, avg `-0.016882`, median `-0.014301`
- 10d: sample `8`, primary_hit `0.0`, primary_closer `0.375`, primary_mae `0.018131`, avg `-0.018343`, median `-0.017516`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.06322`, avg `-0.00332`, median `0.020913`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.110897`, avg `0.0071`, median `0.029112`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.017905`, avg `-0.011682`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.018383`, avg `-0.01475`, median `-0.016241`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.5625`, primary_mae `0.018675`, avg `-0.013101`, median `-0.013277`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.6875`, primary_mae `0.056311`, avg `0.006021`, median `0.020913`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.096843`, avg `0.023929`, median `0.052632`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.012042`, avg `-0.001937`, median `-0.002687`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.375`, primary_mae `0.022655`, avg `-0.011214`, median `-0.012686`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.75`, primary_mae `0.025763`, avg `-0.021338`, median `-0.032528`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.075738`, avg `-0.008699`, median `-0.029855`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.118598`, avg `0.014407`, median `0.019907`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.525`, primary_mae `0.015607`, avg `-0.00317`, median `-0.001439`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.01844`, avg `-0.008777`, median `-0.007313`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.026951`, avg `-0.010527`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.6125`, primary_closer `0.6`, primary_mae `0.053186`, avg `0.001919`, median `0.002137`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.55`, primary_mae `0.074683`, avg `0.017003`, median `0.030631`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.525`, primary_mae `0.015607`, avg `-0.00317`, median `-0.001439`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.01844`, avg `-0.008777`, median `-0.007313`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.026951`, avg `-0.010527`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.6125`, primary_closer `0.6`, primary_mae `0.053186`, avg `0.001919`, median `0.002137`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.55`, primary_mae `0.074683`, avg `0.017003`, median `0.030631`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.018092`, avg `-0.005907`, median `-0.003579`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.023218`, avg `-0.008694`, median `-0.0084`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.030544`, avg `-0.012805`, median `-0.010196`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.040863`, avg `0.009454`, median `0.007177`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.056049`, avg `0.02105`, median `0.041509`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.525`, primary_mae `0.015607`, avg `-0.00317`, median `-0.001439`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.01844`, avg `-0.008777`, median `-0.007313`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.026951`, avg `-0.010527`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.6125`, primary_closer `0.6`, primary_mae `0.053186`, avg `0.001919`, median `0.002137`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.55`, primary_mae `0.074683`, avg `0.017003`, median `0.030631`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.525`, primary_mae `0.015607`, avg `-0.00317`, median `-0.001439`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.01844`, avg `-0.008777`, median `-0.007313`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.026951`, avg `-0.010527`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.6125`, primary_closer `0.6`, primary_mae `0.053186`, avg `0.001919`, median `0.002137`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.55`, primary_mae `0.074683`, avg `0.017003`, median `0.030631`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.5333`, primary_mae `0.014778`, avg `-0.002258`, median `-0.001439`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.5`, primary_mae `0.016848`, avg `-0.008805`, median `-0.00651`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.5333`, primary_mae `0.025753`, avg `-0.009768`, median `-0.013993`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.6333`, primary_mae `0.057294`, avg `-0.000593`, median `0.002137`
- 60d: sample `60`, primary_hit `0.6167`, primary_closer `0.55`, primary_mae `0.080894`, avg `0.015654`, median `0.030631`

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
