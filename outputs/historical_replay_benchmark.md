# Historical Replay Benchmark

Generated at: `2026-07-15T06:01:31.152130+00:00`
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
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.01844`
- secondary_mean_absolute_error: `0.016616`
- primary_error_advantage: `-0.001824`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.5625`
- primary_mean_absolute_error: `0.020938`
- secondary_mean_absolute_error: `0.022857`
- primary_error_advantage: `0.001919`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.5875`
- primary_mean_absolute_error: `0.024397`
- secondary_mean_absolute_error: `0.026374`
- primary_error_advantage: `0.001977`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.033854`
- secondary_mean_absolute_error: `0.033168`
- primary_error_advantage: `-0.000686`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.060443`
- secondary_mean_absolute_error: `0.055303`
- primary_error_advantage: `-0.00514`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.015637`, as_primary `0`, as_primary_hit `None`, avg `0.002457`, median `0.005602`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.020086`, as_primary `0`, as_primary_hit `None`, avg `0.003687`, median `0.005317`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.023073`, as_primary `0`, as_primary_hit `None`, avg `0.011993`, median `0.013478`
- 20d: sample `80`, direction_hit `0.8875`, path_mae `0.021818`, as_primary `0`, as_primary_hit `None`, avg `0.029142`, median `0.029185`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.048489`, as_primary `0`, as_primary_hit `None`, avg `0.045993`, median `0.063167`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.015507`, as_primary `20`, as_primary_hit `0.8`, avg `0.002457`, median `0.005602`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.022055`, as_primary `20`, as_primary_hit `0.75`, avg `0.003687`, median `0.005317`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.025918`, as_primary `20`, as_primary_hit `0.85`, avg `0.011993`, median `0.013478`
- 20d: sample `80`, direction_hit `0.8875`, path_mae `0.031924`, as_primary `20`, as_primary_hit `0.95`, avg `0.029142`, median `0.029185`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.053223`, as_primary `20`, as_primary_hit `0.95`, avg `0.045993`, median `0.063167`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.019549`, as_primary `60`, as_primary_hit `0.55`, avg `0.002457`, median `0.005602`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.02174`, as_primary `60`, as_primary_hit `0.4833`, avg `0.003687`, median `0.005317`
- 10d: sample `80`, direction_hit `0.3125`, path_mae `0.024852`, as_primary `60`, as_primary_hit `0.6333`, avg `0.011993`, median `0.013478`
- 20d: sample `80`, direction_hit `0.1125`, path_mae `0.035098`, as_primary `60`, as_primary_hit `0.8667`, avg `0.029142`, median `0.029185`
- 60d: sample `80`, direction_hit `0.25`, path_mae `0.062523`, as_primary `60`, as_primary_hit `0.6833`, avg `0.045993`, median `0.063167`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.015568`, as_primary `0`, as_primary_hit `None`, avg `0.002457`, median `0.005602`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.018955`, as_primary `0`, as_primary_hit `None`, avg `0.003687`, median `0.005317`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.021907`, as_primary `0`, as_primary_hit `None`, avg `0.011993`, median `0.013478`
- 20d: sample `80`, direction_hit `0.8875`, path_mae `0.020804`, as_primary `0`, as_primary_hit `None`, avg `0.029142`, median `0.029185`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.046557`, as_primary `0`, as_primary_hit `None`, avg `0.045993`, median `0.063167`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.01844`, avg `0.002457`, median `0.005602`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.5625`, primary_mae `0.020938`, avg `0.003687`, median `0.005317`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.5875`, primary_mae `0.024397`, avg `0.011993`, median `0.013478`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.5125`, primary_mae `0.033854`, avg `0.029142`, median `0.029185`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.060443`, avg `0.045993`, median `0.063167`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.01844`, avg `0.002457`, median `0.005602`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.5625`, primary_mae `0.020938`, avg `0.003687`, median `0.005317`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.5875`, primary_mae `0.024397`, avg `0.011993`, median `0.013478`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.5125`, primary_mae `0.033854`, avg `0.029142`, median `0.029185`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.060443`, avg `0.045993`, median `0.063167`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5375, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.01844, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.5625, 'primary_mean_absolute_error': 0.020938, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4875, 'primary_closer_than_secondary_rate': 0.5875, 'primary_mean_absolute_error': 0.024397, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3375, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.033854, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.060443, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015507, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019549, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5375, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.01844, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.5625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018955, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022055, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.5625, 'primary_mean_absolute_error': 0.020938, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.5875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021907, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025918, 'direction_hit_rate': 0.6875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4875, 'primary_closer_than_secondary_rate': 0.5875, 'primary_mean_absolute_error': 0.024397, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020804, 'direction_hit_rate': 0.8875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035098, 'direction_hit_rate': 0.1125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3375, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.033854, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.046557, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062523, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.060443, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.025669`, avg `-0.004536`, median `-0.00711`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.03115`, avg `-0.006532`, median `-0.009536`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.046221`, avg `0.015225`, median `0.029091`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.061322`, avg `0.018395`, median `0.028464`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.133616`, avg `0.045345`, median `0.083569`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.030192`, avg `-0.000142`, median `0.00075`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.032294`, avg `-0.004609`, median `-0.010026`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.039244`, avg `0.008817`, median `0.00651`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.059508`, avg `0.020264`, median `0.028464`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.113243`, avg `0.024768`, median `0.035271`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.015686`, avg `0.004755`, median `0.012314`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.625`, primary_mae `0.015445`, avg `0.007934`, median `0.009975`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.8125`, primary_mae `0.02224`, avg `0.011146`, median `0.012514`
- 20d: sample `16`, primary_hit `0.0`, primary_closer `0.5625`, primary_mae `0.031055`, avg `0.04652`, median `0.040733`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.5`, primary_mae `0.047526`, avg `0.081541`, median `0.086443`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.01844`, avg `0.002457`, median `0.005602`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.5625`, primary_mae `0.020938`, avg `0.003687`, median `0.005317`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.5875`, primary_mae `0.024397`, avg `0.011993`, median `0.013478`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.5125`, primary_mae `0.033854`, avg `0.029142`, median `0.029185`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.060443`, avg `0.045993`, median `0.063167`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.01844`, avg `0.002457`, median `0.005602`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.5625`, primary_mae `0.020938`, avg `0.003687`, median `0.005317`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.5875`, primary_mae `0.024397`, avg `0.011993`, median `0.013478`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.5125`, primary_mae `0.033854`, avg `0.029142`, median `0.029185`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.060443`, avg `0.045993`, median `0.063167`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.013478`, avg `0.003285`, median `0.006001`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.65`, primary_mae `0.017388`, avg `0.005137`, median `0.005083`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.016578`, avg `0.010547`, median `0.011243`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.575`, primary_mae `0.02139`, avg `0.024869`, median `0.026713`
- 60d: sample `40`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.040857`, avg `0.038587`, median `0.04634`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.55`, primary_mae `0.014821`, avg `0.004932`, median `0.006946`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.6167`, primary_mae `0.017514`, avg `0.007362`, median `0.008464`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.6333`, primary_mae `0.018691`, avg `0.013154`, median `0.013823`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.55`, primary_mae `0.026327`, avg `0.03311`, median `0.030184`
- 60d: sample `60`, primary_hit `0.4833`, primary_closer `0.6`, primary_mae `0.043249`, avg `0.054535`, median `0.066471`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.01844`, avg `0.002457`, median `0.005602`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.5625`, primary_mae `0.020938`, avg `0.003687`, median `0.005317`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.5875`, primary_mae `0.024397`, avg `0.011993`, median `0.013478`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.5125`, primary_mae `0.033854`, avg `0.029142`, median `0.029185`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.060443`, avg `0.045993`, median `0.063167`

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
