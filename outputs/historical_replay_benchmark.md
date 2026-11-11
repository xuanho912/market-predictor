# Historical Replay Benchmark

Generated at: `2026-11-11T01:32:39.691336+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.01784`
- secondary_mean_absolute_error: `0.020686`
- primary_error_advantage: `0.002846`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.575`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.026869`
- secondary_mean_absolute_error: `0.02821`
- primary_error_advantage: `0.001341`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.050138`
- secondary_mean_absolute_error: `0.04944`
- primary_error_advantage: `-0.000698`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.06695`
- secondary_mean_absolute_error: `0.061241`
- primary_error_advantage: `-0.005709`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1625`
- secondary_hit_rate: `0.8375`
- primary_vs_secondary_accuracy_spread: `-0.675`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.0451`
- secondary_mean_absolute_error: `0.049486`
- primary_error_advantage: `0.004386`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.018029`, as_primary `0`, as_primary_hit `None`, avg `0.00412`, median `0.006842`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.024993`, as_primary `0`, as_primary_hit `None`, avg `0.001242`, median `0.001314`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.039977`, as_primary `0`, as_primary_hit `None`, avg `-0.006316`, median `-0.013087`
- 20d: sample `80`, direction_hit `0.4`, path_mae `0.042222`, as_primary `0`, as_primary_hit `None`, avg `-0.015075`, median `-0.022787`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.042116`, as_primary `0`, as_primary_hit `None`, avg `0.064167`, median `0.065936`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.021037`, as_primary `0`, as_primary_hit `None`, avg `0.00412`, median `0.006842`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.029442`, as_primary `0`, as_primary_hit `None`, avg `0.001242`, median `0.001314`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.053759`, as_primary `0`, as_primary_hit `None`, avg `-0.006316`, median `-0.013087`
- 20d: sample `80`, direction_hit `0.4`, path_mae `0.069055`, as_primary `0`, as_primary_hit `None`, avg `-0.015075`, median `-0.022787`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.05006`, as_primary `0`, as_primary_hit `None`, avg `0.064167`, median `0.065936`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.01784`, as_primary `80`, as_primary_hit `0.6`, avg `0.00412`, median `0.006842`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.026869`, as_primary `80`, as_primary_hit `0.5125`, avg `0.001242`, median `0.001314`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.050138`, as_primary `80`, as_primary_hit `0.425`, avg `-0.006316`, median `-0.013087`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.06695`, as_primary `80`, as_primary_hit `0.4`, avg `-0.015075`, median `-0.022787`
- 60d: sample `80`, direction_hit `0.1625`, path_mae `0.0451`, as_primary `80`, as_primary_hit `0.8375`, avg `0.064167`, median `0.065936`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.017499`, as_primary `0`, as_primary_hit `None`, avg `0.00412`, median `0.006842`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.024355`, as_primary `0`, as_primary_hit `None`, avg `0.001242`, median `0.001314`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.038484`, as_primary `0`, as_primary_hit `None`, avg `-0.006316`, median `-0.013087`
- 20d: sample `80`, direction_hit `0.4`, path_mae `0.042355`, as_primary `0`, as_primary_hit `None`, avg `-0.015075`, median `-0.022787`
- 60d: sample `80`, direction_hit `0.8375`, path_mae `0.040694`, as_primary `0`, as_primary_hit `None`, avg `0.064167`, median `0.065936`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.7`, primary_mae `0.016902`, avg `0.005781`, median `0.00957`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.025385`, avg `0.001372`, median `-0.002987`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.0595`, avg `-0.007073`, median `-0.003593`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.08282`, avg `-0.007699`, median `0.007176`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.073418`, avg `0.070133`, median `0.099914`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.5333`, primary_mae `0.018153`, avg `0.003566`, median `0.005729`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.5`, primary_mae `0.027363`, avg `0.001199`, median `0.002517`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.047017`, avg `-0.006063`, median `-0.013625`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.4667`, primary_mae `0.061659`, avg `-0.017533`, median `-0.025593`
- 60d: sample `60`, primary_hit `0.15`, primary_closer `0.5833`, primary_mae `0.035661`, avg `0.062179`, median `0.059962`

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
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.5333`, primary_mae `0.018153`, avg `0.003566`, median `0.005729`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.5`, primary_mae `0.027363`, avg `0.001199`, median `0.002517`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.047017`, avg `-0.006063`, median `-0.013625`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.4667`, primary_mae `0.061659`, avg `-0.017533`, median `-0.025593`
- 60d: sample `60`, primary_hit `0.15`, primary_closer `0.5833`, primary_mae `0.035661`, avg `0.062179`, median `0.059962`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.7`, primary_mae `0.016902`, avg `0.005781`, median `0.00957`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.025385`, avg `0.001372`, median `-0.002987`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.0595`, avg `-0.007073`, median `-0.003593`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.08282`, avg `-0.007699`, median `0.007176`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.073418`, avg `0.070133`, median `0.099914`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.016902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.025385, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.047017, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.061659, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.5833, 'primary_mean_absolute_error': 0.035661, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017499, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021037, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.016902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024355, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029442, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.025385, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038484, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053759, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.047017, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042222, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069055, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.061659, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1625, 'secondary_hit_rate': 0.8375, 'primary_vs_secondary_accuracy_spread': -0.675, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040694, 'direction_hit_rate': 0.8375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05006, 'direction_hit_rate': 0.8375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.5833, 'primary_mean_absolute_error': 0.035661, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.75`, primary_mae `0.016108`, avg `0.002882`, median `0.004949`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.029342`, avg `0.005307`, median `0.003699`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.067156`, avg `-0.006788`, median `0.01896`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.086784`, avg `-0.004139`, median `0.015107`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.070259`, avg `0.063584`, median `0.081203`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.6875`, primary_mae `0.016402`, avg `0.005179`, median `0.005949`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.028226`, avg `0.002462`, median `0.002487`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.060964`, avg `-0.008081`, median `0.003773`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.078871`, avg `-0.012579`, median `0.007176`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.068794`, avg `0.058801`, median `0.081203`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.020847`, avg `0.00406`, median `0.010191`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.033409`, avg `0.002791`, median `0.006091`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.050419`, avg `-0.010339`, median `-0.016103`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.045366`, avg `-0.030532`, median `-0.041695`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.5625`, primary_mae `0.029801`, avg `0.090124`, median `0.094379`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.575`, primary_mae `0.01784`, avg `0.00412`, median `0.006842`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5125`, primary_mae `0.026869`, avg `0.001242`, median `0.001314`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.050138`, avg `-0.006316`, median `-0.013087`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.06695`, avg `-0.015075`, median `-0.022787`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.5375`, primary_mae `0.0451`, avg `0.064167`, median `0.065936`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.575`, primary_mae `0.01784`, avg `0.00412`, median `0.006842`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5125`, primary_mae `0.026869`, avg `0.001242`, median `0.001314`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.050138`, avg `-0.006316`, median `-0.013087`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.06695`, avg `-0.015075`, median `-0.022787`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.5375`, primary_mae `0.0451`, avg `0.064167`, median `0.065936`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.6167`, primary_mae `0.016915`, avg `0.002731`, median `0.004101`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.5833`, primary_mae `0.024282`, avg `-0.000934`, median `-0.004697`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.5833`, primary_mae `0.047703`, avg `-0.008144`, median `-0.01583`
- 20d: sample `60`, primary_hit `0.6`, primary_closer `0.4667`, primary_mae `0.069931`, avg `-0.014419`, median `-0.022521`
- 60d: sample `60`, primary_hit `0.2167`, primary_closer `0.5667`, primary_mae `0.047613`, avg `0.050701`, median `0.056969`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.020617`, avg `0.008287`, median `0.012755`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.034628`, avg `0.007773`, median `0.009092`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.05744`, avg `-0.00083`, median `-0.001706`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.058007`, avg `-0.017041`, median `-0.028587`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.45`, primary_mae `0.037562`, avg `0.104567`, median `0.101574`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.575`, primary_mae `0.01784`, avg `0.00412`, median `0.006842`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5125`, primary_mae `0.026869`, avg `0.001242`, median `0.001314`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.050138`, avg `-0.006316`, median `-0.013087`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.06695`, avg `-0.015075`, median `-0.022787`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.5375`, primary_mae `0.0451`, avg `0.064167`, median `0.065936`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.575`, primary_mae `0.01784`, avg `0.00412`, median `0.006842`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5125`, primary_mae `0.026869`, avg `0.001242`, median `0.001314`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.050138`, avg `-0.006316`, median `-0.013087`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.06695`, avg `-0.015075`, median `-0.022787`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.5375`, primary_mae `0.0451`, avg `0.064167`, median `0.065936`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.575`, primary_mae `0.01784`, avg `0.00412`, median `0.006842`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5125`, primary_mae `0.026869`, avg `0.001242`, median `0.001314`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.050138`, avg `-0.006316`, median `-0.013087`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.06695`, avg `-0.015075`, median `-0.022787`
- 60d: sample `80`, primary_hit `0.1625`, primary_closer `0.5375`, primary_mae `0.0451`, avg `0.064167`, median `0.065936`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
