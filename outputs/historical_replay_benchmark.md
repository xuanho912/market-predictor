# Historical Replay Benchmark

Generated at: `2026-10-01T18:27:34.457134+00:00`
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
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.016607`
- secondary_mean_absolute_error: `0.015321`
- primary_error_advantage: `-0.001286`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.02264`
- secondary_mean_absolute_error: `0.018773`
- primary_error_advantage: `-0.003867`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.038946`
- secondary_mean_absolute_error: `0.027`
- primary_error_advantage: `-0.011946`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.075196`
- secondary_mean_absolute_error: `0.042984`
- primary_error_advantage: `-0.032212`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.082732`
- secondary_mean_absolute_error: `0.054803`
- primary_error_advantage: `-0.027929`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.015191`, as_primary `0`, as_primary_hit `None`, avg `-0.004906`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.018644`, as_primary `0`, as_primary_hit `None`, avg `-0.007962`, median `-0.006281`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.027487`, as_primary `0`, as_primary_hit `None`, avg `-0.006594`, median `-1e-06`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.043391`, as_primary `0`, as_primary_hit `None`, avg `0.003321`, median `0.012636`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.053347`, as_primary `0`, as_primary_hit `None`, avg `0.051174`, median `0.059117`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.014762`, as_primary `0`, as_primary_hit `None`, avg `-0.004906`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.019424`, as_primary `0`, as_primary_hit `None`, avg `-0.007962`, median `-0.006281`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.033034`, as_primary `0`, as_primary_hit `None`, avg `-0.006594`, median `-1e-06`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.064934`, as_primary `0`, as_primary_hit `None`, avg `0.003321`, median `0.012636`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.061539`, as_primary `0`, as_primary_hit `None`, avg `0.051174`, median `0.059117`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.016607`, as_primary `80`, as_primary_hit `0.425`, avg `-0.004906`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.02264`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.007962`, median `-0.006281`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.038946`, as_primary `80`, as_primary_hit `0.5`, avg `-0.006594`, median `-1e-06`
- 20d: sample `80`, direction_hit `0.4375`, path_mae `0.075196`, as_primary `80`, as_primary_hit `0.5625`, avg `0.003321`, median `0.012636`
- 60d: sample `80`, direction_hit `0.1875`, path_mae `0.082732`, as_primary `80`, as_primary_hit `0.8125`, avg `0.051174`, median `0.059117`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.015321`, as_primary `0`, as_primary_hit `None`, avg `-0.004906`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.018773`, as_primary `0`, as_primary_hit `None`, avg `-0.007962`, median `-0.006281`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.027`, as_primary `0`, as_primary_hit `None`, avg `-0.006594`, median `-1e-06`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.042984`, as_primary `0`, as_primary_hit `None`, avg `0.003321`, median `0.012636`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.054803`, as_primary `0`, as_primary_hit `None`, avg `0.051174`, median `0.059117`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.016607`, avg `-0.004906`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.02264`, avg `-0.007962`, median `-0.006281`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.038946`, avg `-0.006594`, median `-1e-06`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.075196`, avg `0.003321`, median `0.012636`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.082732`, avg `0.051174`, median `0.059117`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.7`, primary_closer `0.375`, primary_mae `0.020194`, avg `-0.011316`, median `-0.010184`
- 5d: sample `40`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.026379`, avg `-0.013413`, median `-0.012577`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.043097`, avg `-0.01`, median `-0.010944`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.3`, primary_mae `0.083621`, avg `0.000653`, median `-0.001058`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.099303`, avg `0.061762`, median `0.092349`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.01302`, avg `0.001505`, median `0.003`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.018901`, avg `-0.002512`, median `0.003018`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.275`, primary_mae `0.034796`, avg `-0.003188`, median `0.005613`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.2`, primary_mae `0.06677`, avg `0.00599`, median `0.01444`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.25`, primary_mae `0.066162`, avg `0.040586`, median `0.045545`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.01302, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018901, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.034796, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.06677, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.066162, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014762, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016607, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.01302, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018644, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02264, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018901, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038946, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.034796, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042984, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075196, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.06677, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053347, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.082732, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.066162, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.013511`, avg `0.001368`, median `0.003983`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.015267`, avg `-0.001273`, median `0.001171`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.03035`, avg `0.006154`, median `0.00365`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.0`, primary_mae `0.092174`, avg `0.028741`, median `0.032633`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.073393`, avg `0.037695`, median `0.04613`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.008995`, avg `0.000853`, median `0.000437`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.014247`, avg `-0.002937`, median `0.001171`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.029433`, avg `0.002246`, median `0.006069`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.077642`, avg `0.011719`, median `0.020612`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.06563`, avg `0.027576`, median `0.032017`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.025006`, avg `-0.002958`, median `0.00065`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.034274`, avg `-0.010156`, median `-0.009034`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.044864`, avg `-0.012323`, median `-0.008724`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.085607`, avg `0.003546`, median `0.015746`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.142009`, avg `0.059756`, median `0.086104`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.016607`, avg `-0.004906`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.02264`, avg `-0.007962`, median `-0.006281`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.038946`, avg `-0.006594`, median `-1e-06`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.075196`, avg `0.003321`, median `0.012636`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.082732`, avg `0.051174`, median `0.059117`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.016607`, avg `-0.004906`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.02264`, avg `-0.007962`, median `-0.006281`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.038946`, avg `-0.006594`, median `-1e-06`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.075196`, avg `0.003321`, median `0.012636`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.082732`, avg `0.051174`, median `0.059117`

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
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.016607`, avg `-0.004906`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.02264`, avg `-0.007962`, median `-0.006281`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.038946`, avg `-0.006594`, median `-1e-06`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.075196`, avg `0.003321`, median `0.012636`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.082732`, avg `0.051174`, median `0.059117`

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
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.016607`, avg `-0.004906`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.02264`, avg `-0.007962`, median `-0.006281`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.038946`, avg `-0.006594`, median `-1e-06`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.075196`, avg `0.003321`, median `0.012636`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.082732`, avg `0.051174`, median `0.059117`

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
