# Historical Replay Benchmark

Generated at: `2026-11-12T19:57:25.938708+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
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
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.022125`
- secondary_mean_absolute_error: `0.016755`
- primary_error_advantage: `-0.00537`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.022494`
- secondary_mean_absolute_error: `0.017006`
- primary_error_advantage: `-0.005488`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.046162`
- secondary_mean_absolute_error: `0.027442`
- primary_error_advantage: `-0.01872`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.054823`
- secondary_mean_absolute_error: `0.042151`
- primary_error_advantage: `-0.012672`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.091856`
- secondary_mean_absolute_error: `0.07301`
- primary_error_advantage: `-0.018846`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.017006`, as_primary `0`, as_primary_hit `None`, avg `0.001969`, median `0.001778`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.01863`, as_primary `0`, as_primary_hit `None`, avg `0.004224`, median `0.003558`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.028775`, as_primary `0`, as_primary_hit `None`, avg `0.004561`, median `-0.002374`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.035354`, as_primary `0`, as_primary_hit `None`, avg `0.016645`, median `0.015533`
- 60d: sample `80`, direction_hit `0.45`, path_mae `0.079458`, as_primary `0`, as_primary_hit `None`, avg `0.001643`, median `-0.005861`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.020878`, as_primary `60`, as_primary_hit `0.45`, avg `0.001969`, median `0.001778`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.022186`, as_primary `60`, as_primary_hit `0.5333`, avg `0.004224`, median `0.003558`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.042461`, as_primary `60`, as_primary_hit `0.45`, avg `0.004561`, median `-0.002374`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.057644`, as_primary `60`, as_primary_hit `0.65`, avg `0.016645`, median `0.015533`
- 60d: sample `80`, direction_hit `0.45`, path_mae `0.109376`, as_primary `60`, as_primary_hit `0.3833`, avg `0.001643`, median `-0.005861`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.018937`, as_primary `20`, as_primary_hit `0.75`, avg `0.001969`, median `0.001778`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.019573`, as_primary `20`, as_primary_hit `0.8`, avg `0.004224`, median `0.003558`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.039616`, as_primary `20`, as_primary_hit `0.6`, avg `0.004561`, median `-0.002374`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.055951`, as_primary `20`, as_primary_hit `0.75`, avg `0.016645`, median `0.015533`
- 60d: sample `80`, direction_hit `0.55`, path_mae `0.078117`, as_primary `20`, as_primary_hit `0.65`, avg `0.001643`, median `-0.005861`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.016346`, as_primary `0`, as_primary_hit `None`, avg `0.001969`, median `0.001778`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.016462`, as_primary `0`, as_primary_hit `None`, avg `0.004224`, median `0.003558`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.026881`, as_primary `0`, as_primary_hit `None`, avg `0.004561`, median `-0.002374`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.032017`, as_primary `0`, as_primary_hit `None`, avg `0.016645`, median `0.015533`
- 60d: sample `80`, direction_hit `0.45`, path_mae `0.067773`, as_primary `0`, as_primary_hit `None`, avg `0.001643`, median `-0.005861`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.022125`, avg `0.001969`, median `0.001778`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.022494`, avg `0.004224`, median `0.003558`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.3`, primary_mae `0.046162`, avg `0.004561`, median `-0.002374`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.054823`, avg `0.016645`, median `0.015533`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.091856`, avg `0.001643`, median `-0.005861`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.3667`, primary_mae `0.021115`, avg `-0.000664`, median `-0.004035`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.3667`, primary_mae `0.021618`, avg `0.001408`, median `0.000641`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.035046`, avg `0.003673`, median `-0.005404`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.4333`, primary_mae `0.051246`, avg `0.011558`, median `0.013391`
- 60d: sample `60`, primary_hit `0.3833`, primary_closer `0.3833`, primary_mae `0.092034`, avg `-0.005923`, median `-0.018716`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.025153`, avg `0.009868`, median `0.011763`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.02512`, avg `0.012674`, median `0.01257`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.15`, primary_mae `0.079509`, avg `0.007226`, median `0.01657`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.065554`, avg `0.031904`, median `0.030573`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.091322`, avg `0.024342`, median `0.024981`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.021115, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.021618, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.035046, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.051246, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.091322, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016346, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020878, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.021115, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016462, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022186, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.021618, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026881, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042461, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.035046, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032017, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057644, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.051246, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067773, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.109376, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.091322, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.032509`, avg `-0.008229`, median `-0.015036`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.032652`, avg `-0.005724`, median `-0.006463`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.066291`, avg `-0.007593`, median `-0.009365`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.125`, primary_mae `0.069024`, avg `-0.001571`, median `0.011966`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.135085`, avg `-0.03188`, median `-0.03254`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.025079`, avg `0.000592`, median `0.002768`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.028526`, avg `0.000199`, median `-0.004803`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.057729`, avg `0.006009`, median `0.003532`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.1875`, primary_mae `0.061175`, avg `0.013123`, median `0.011966`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.123969`, avg `-0.006373`, median `-0.024244`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.025092`, avg `0.009749`, median `0.011763`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.023805`, avg `0.009843`, median `0.01257`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.1875`, primary_mae `0.075119`, avg `0.000419`, median `0.009595`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.060948`, avg `0.026042`, median `0.021059`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.07739`, avg `0.031786`, median `0.024981`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.022125`, avg `0.001969`, median `0.001778`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.022494`, avg `0.004224`, median `0.003558`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.3`, primary_mae `0.046162`, avg `0.004561`, median `-0.002374`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.054823`, avg `0.016645`, median `0.015533`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.091856`, avg `0.001643`, median `-0.005861`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.022125`, avg `0.001969`, median `0.001778`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.022494`, avg `0.004224`, median `0.003558`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.3`, primary_mae `0.046162`, avg `0.004561`, median `-0.002374`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.054823`, avg `0.016645`, median `0.015533`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.091856`, avg `0.001643`, median `-0.005861`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.3667`, primary_mae `0.021115`, avg `-0.000664`, median `-0.004035`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.3667`, primary_mae `0.021618`, avg `0.001408`, median `0.000641`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.035046`, avg `0.003673`, median `-0.005404`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.4333`, primary_mae `0.051246`, avg `0.011558`, median `0.013391`
- 60d: sample `60`, primary_hit `0.3833`, primary_closer `0.3833`, primary_mae `0.092034`, avg `-0.005923`, median `-0.018716`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.025153`, avg `0.009868`, median `0.011763`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.02512`, avg `0.012674`, median `0.01257`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.15`, primary_mae `0.079509`, avg `0.007226`, median `0.01657`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.065554`, avg `0.031904`, median `0.030573`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.091322`, avg `0.024342`, median `0.024981`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.022125`, avg `0.001969`, median `0.001778`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.022494`, avg `0.004224`, median `0.003558`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.3`, primary_mae `0.046162`, avg `0.004561`, median `-0.002374`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.054823`, avg `0.016645`, median `0.015533`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.091856`, avg `0.001643`, median `-0.005861`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.022125`, avg `0.001969`, median `0.001778`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.022494`, avg `0.004224`, median `0.003558`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.3`, primary_mae `0.046162`, avg `0.004561`, median `-0.002374`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.054823`, avg `0.016645`, median `0.015533`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.091856`, avg `0.001643`, median `-0.005861`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.3375`, primary_mae `0.022125`, avg `0.001969`, median `0.001778`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.022494`, avg `0.004224`, median `0.003558`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.3`, primary_mae `0.046162`, avg `0.004561`, median `-0.002374`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.054823`, avg `0.016645`, median `0.015533`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.091856`, avg `0.001643`, median `-0.005861`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
