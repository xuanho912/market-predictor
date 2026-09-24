# Historical Replay Benchmark

Generated at: `2026-09-24T01:06:46.037294+00:00`
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
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.01751`
- secondary_mean_absolute_error: `0.015265`
- primary_error_advantage: `-0.002245`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.023264`
- secondary_mean_absolute_error: `0.018861`
- primary_error_advantage: `-0.004403`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.033262`
- secondary_mean_absolute_error: `0.027189`
- primary_error_advantage: `-0.006073`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3875`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.7625`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.057731`
- secondary_mean_absolute_error: `0.042791`
- primary_error_advantage: `-0.01494`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.057847`
- secondary_mean_absolute_error: `0.047879`
- primary_error_advantage: `-0.009968`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.015483`, as_primary `0`, as_primary_hit `None`, avg `0.002573`, median `0.004149`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.020065`, as_primary `0`, as_primary_hit `None`, avg `0.00505`, median `0.007278`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.028245`, as_primary `0`, as_primary_hit `None`, avg `0.007943`, median `0.007087`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.040024`, as_primary `0`, as_primary_hit `None`, avg `0.032868`, median `0.03365`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.048106`, as_primary `0`, as_primary_hit `None`, avg `0.081503`, median `0.098227`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.017544`, as_primary `60`, as_primary_hit `0.6333`, avg `0.002573`, median `0.004149`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.023414`, as_primary `60`, as_primary_hit `0.6167`, avg `0.00505`, median `0.007278`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.033412`, as_primary `60`, as_primary_hit `0.65`, avg `0.007943`, median `0.007087`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.055656`, as_primary `60`, as_primary_hit `0.8667`, avg `0.032868`, median `0.03365`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.051125`, as_primary `60`, as_primary_hit `0.8667`, avg `0.081503`, median `0.098227`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.016093`, as_primary `20`, as_primary_hit `0.35`, avg `0.002573`, median `0.004149`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.019659`, as_primary `20`, as_primary_hit `0.45`, avg `0.00505`, median `0.007278`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.028804`, as_primary `20`, as_primary_hit `0.5`, avg `0.007943`, median `0.007087`
- 20d: sample `80`, direction_hit `0.2125`, path_mae `0.051335`, as_primary `20`, as_primary_hit `0.55`, avg `0.032868`, median `0.03365`
- 60d: sample `80`, direction_hit `0.1375`, path_mae `0.06211`, as_primary `20`, as_primary_hit `0.85`, avg `0.081503`, median `0.098227`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.01521`, as_primary `0`, as_primary_hit `None`, avg `0.002573`, median `0.004149`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.01824`, as_primary `0`, as_primary_hit `None`, avg `0.00505`, median `0.007278`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.026592`, as_primary `0`, as_primary_hit `None`, avg `0.007943`, median `0.007087`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.034854`, as_primary `0`, as_primary_hit `None`, avg `0.032868`, median `0.03365`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.046557`, as_primary `0`, as_primary_hit `None`, avg `0.081503`, median `0.098227`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.01751`, avg `0.002573`, median `0.004149`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.023264`, avg `0.00505`, median `0.007278`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.033262`, avg `0.007943`, median `0.007087`
- 20d: sample `80`, primary_hit `0.7625`, primary_closer `0.425`, primary_mae `0.057731`, avg `0.032868`, median `0.03365`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.4625`, primary_mae `0.057847`, avg `0.081503`, median `0.098227`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.55`, primary_mae `0.012652`, avg `0.009462`, median `0.016082`
- 5d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.019106`, avg `0.011301`, median `0.012047`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.025632`, avg `0.014822`, median `0.018067`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.04032`, avg `0.040946`, median `0.040733`
- 60d: sample `20`, primary_hit `0.9`, primary_closer `0.55`, primary_mae `0.031646`, avg `0.089881`, median `0.099778`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.016247`, avg `-0.004657`, median `-0.006398`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.020406`, avg `-0.00177`, median `-0.004042`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.03786`, avg `-0.003199`, median `-0.001779`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.067303`, avg `0.005644`, median `0.021827`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.2`, primary_mae `0.06215`, avg `0.086992`, median `0.103937`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.02057`, avg `0.002742`, median `0.003436`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.026771`, avg `0.005334`, median `0.00738`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.375`, primary_mae `0.034778`, avg `0.010075`, median `0.004776`
- 20d: sample `40`, primary_hit `0.9`, primary_closer `0.45`, primary_mae `0.061651`, avg `0.042441`, median `0.03338`
- 60d: sample `40`, primary_hit `0.85`, primary_closer `0.55`, primary_mae `0.068796`, avg `0.074569`, median `0.077578`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.012652, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.019106, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.025632, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.04032, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.9, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.031646, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01521, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017544, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.012652, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01824, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023414, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.019106, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026592, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033412, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.025632, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7625, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034854, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055656, 'direction_hit_rate': 0.7875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.04032, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.046557, 'direction_hit_rate': 0.8625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06211, 'direction_hit_rate': 0.1375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.9, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.031646, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.019387`, avg `-0.000656`, median `0.001049`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.024604`, avg `0.000493`, median `0.006272`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.02677`, avg `0.009459`, median `0.015682`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.03228`, avg `0.047912`, median `0.058396`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.625`, primary_mae `0.026352`, avg `0.104005`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.01436`, avg `0.006827`, median `0.013599`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.021492`, avg `0.008556`, median `0.008828`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.028084`, avg `0.012658`, median `0.016702`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.375`, primary_mae `0.038411`, avg `0.043124`, median `0.050926`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.625`, primary_mae `0.026836`, avg `0.095043`, median `0.104666`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.017898`, avg `-0.004025`, median `-0.002005`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.019927`, avg `-0.00487`, median `-0.006363`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.037293`, avg `-0.006261`, median `-0.017905`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.06187`, avg `-0.000378`, median `0.003968`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.064511`, avg `0.08296`, median `0.103937`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.01751`, avg `0.002573`, median `0.004149`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.023264`, avg `0.00505`, median `0.007278`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.033262`, avg `0.007943`, median `0.007087`
- 20d: sample `80`, primary_hit `0.7625`, primary_closer `0.425`, primary_mae `0.057731`, avg `0.032868`, median `0.03365`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.4625`, primary_mae `0.057847`, avg `0.081503`, median `0.098227`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.01751`, avg `0.002573`, median `0.004149`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.023264`, avg `0.00505`, median `0.007278`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.033262`, avg `0.007943`, median `0.007087`
- 20d: sample `80`, primary_hit `0.7625`, primary_closer `0.425`, primary_mae `0.057731`, avg `0.032868`, median `0.03365`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.4625`, primary_mae `0.057847`, avg `0.081503`, median `0.098227`

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
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.01751`, avg `0.002573`, median `0.004149`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.023264`, avg `0.00505`, median `0.007278`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.033262`, avg `0.007943`, median `0.007087`
- 20d: sample `80`, primary_hit `0.7625`, primary_closer `0.425`, primary_mae `0.057731`, avg `0.032868`, median `0.03365`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.4625`, primary_mae `0.057847`, avg `0.081503`, median `0.098227`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.01751`, avg `0.002573`, median `0.004149`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.023264`, avg `0.00505`, median `0.007278`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.033262`, avg `0.007943`, median `0.007087`
- 20d: sample `80`, primary_hit `0.7625`, primary_closer `0.425`, primary_mae `0.057731`, avg `0.032868`, median `0.03365`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.4625`, primary_mae `0.057847`, avg `0.081503`, median `0.098227`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4375`, primary_mae `0.01751`, avg `0.002573`, median `0.004149`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.023264`, avg `0.00505`, median `0.007278`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.033262`, avg `0.007943`, median `0.007087`
- 20d: sample `80`, primary_hit `0.7625`, primary_closer `0.425`, primary_mae `0.057731`, avg `0.032868`, median `0.03365`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.4625`, primary_mae `0.057847`, avg `0.081503`, median `0.098227`

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
