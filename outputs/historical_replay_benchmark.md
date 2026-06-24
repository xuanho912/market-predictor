# Historical Replay Benchmark

Generated at: `2026-06-24T23:47:29.230235+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.016716`
- secondary_mean_absolute_error: `0.017089`
- primary_error_advantage: `0.000373`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.525`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.020282`
- secondary_mean_absolute_error: `0.019874`
- primary_error_advantage: `-0.000408`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.02915`
- secondary_mean_absolute_error: `0.027152`
- primary_error_advantage: `-0.001998`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.049888`
- secondary_mean_absolute_error: `0.033793`
- primary_error_advantage: `-0.016095`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.7875`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.060629`
- secondary_mean_absolute_error: `0.045075`
- primary_error_advantage: `-0.015554`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.01582`, as_primary `0`, as_primary_hit `None`, avg `0.00219`, median `0.000401`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018814`, as_primary `0`, as_primary_hit `None`, avg `-0.001794`, median `-0.004047`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.023669`, as_primary `0`, as_primary_hit `None`, avg `0.001027`, median `-0.001443`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.03001`, as_primary `0`, as_primary_hit `None`, avg `0.013646`, median `0.020408`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.044371`, as_primary `0`, as_primary_hit `None`, avg `0.047114`, median `0.064937`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.017089`, as_primary `40`, as_primary_hit `0.55`, avg `0.00219`, median `0.000401`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.020551`, as_primary `40`, as_primary_hit `0.575`, avg `-0.001794`, median `-0.004047`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.030649`, as_primary `40`, as_primary_hit `0.525`, avg `0.001027`, median `-0.001443`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.042256`, as_primary `40`, as_primary_hit `0.725`, avg `0.013646`, median `0.020408`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.060672`, as_primary `40`, as_primary_hit `0.8`, avg `0.047114`, median `0.064937`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.016819`, as_primary `40`, as_primary_hit `0.45`, avg `0.00219`, median `0.000401`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.019924`, as_primary `40`, as_primary_hit `0.325`, avg `-0.001794`, median `-0.004047`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.029727`, as_primary `40`, as_primary_hit `0.425`, avg `0.001027`, median `-0.001443`
- 20d: sample `80`, direction_hit `0.25`, path_mae `0.061131`, as_primary `40`, as_primary_hit `0.775`, avg `0.013646`, median `0.020408`
- 60d: sample `80`, direction_hit `0.2125`, path_mae `0.064252`, as_primary `40`, as_primary_hit `0.775`, avg `0.047114`, median `0.064937`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015521`, as_primary `0`, as_primary_hit `None`, avg `0.00219`, median `0.000401`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018158`, as_primary `0`, as_primary_hit `None`, avg `-0.001794`, median `-0.004047`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.022686`, as_primary `0`, as_primary_hit `None`, avg `0.001027`, median `-0.001443`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.030212`, as_primary `0`, as_primary_hit `None`, avg `0.013646`, median `0.020408`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.045672`, as_primary `0`, as_primary_hit `None`, avg `0.047114`, median `0.064937`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.5333`, primary_mae `0.016057`, avg `0.001519`, median `-0.000961`
- 5d: sample `60`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.020586`, avg `-0.002971`, median `-0.006423`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.5167`, primary_mae `0.026501`, avg `-0.000311`, median `-0.001443`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.35`, primary_mae `0.04446`, avg `0.015059`, median `0.020767`
- 60d: sample `60`, primary_hit `0.4`, primary_closer `0.4333`, primary_mae `0.048937`, avg `0.042458`, median `0.058512`

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.018692`, avg `0.004201`, median `0.005019`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.01937`, avg `0.001736`, median `0.004977`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.037097`, avg `0.005043`, median `-0.001374`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.066174`, avg `0.009407`, median `0.017625`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.2`, primary_mae `0.095707`, avg `0.061082`, median `0.073795`

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
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.016716`, avg `0.00219`, median `0.000401`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.020282`, avg `-0.001794`, median `-0.004047`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.02915`, avg `0.001027`, median `-0.001443`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.049888`, avg `0.013646`, median `0.020408`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.060629`, avg `0.047114`, median `0.064937`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.016716, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.020282, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4625, 'primary_mean_absolute_error': 0.02915, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.049888, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5125, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.060629, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015521, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017089, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.016716, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018158, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020551, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.020282, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022686, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030649, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4625, 'primary_mean_absolute_error': 0.02915, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03001, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061131, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.049888, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.7875, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044371, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064252, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5125, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.060629, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.014264`, avg `0.005045`, median `-0.00158`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.014359`, avg `0.004988`, median `0.004992`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.040733`, avg `0.00317`, median `-0.00727`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.068486`, avg `0.006138`, median `0.017625`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.125`, primary_mae `0.084879`, avg `0.06146`, median `0.073701`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.01796`, avg `0.000272`, median `-0.00158`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.019219`, avg `-0.001419`, median `-0.001187`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.1875`, primary_mae `0.039823`, avg `0.001847`, median `-0.004104`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.069739`, avg `0.006644`, median `0.017625`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.100273`, avg `0.059128`, median `0.074817`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.015473`, avg `0.002456`, median `0.000401`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.014562`, avg `-0.00731`, median `-0.007674`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.625`, primary_mae `0.012521`, avg `0.003929`, median `-0.001443`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.4375`, primary_mae `0.025436`, avg `0.023842`, median `0.026537`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.5625`, primary_mae `0.020372`, avg `0.075195`, median `0.074488`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.016716`, avg `0.00219`, median `0.000401`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.020282`, avg `-0.001794`, median `-0.004047`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.02915`, avg `0.001027`, median `-0.001443`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.049888`, avg `0.013646`, median `0.020408`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.060629`, avg `0.047114`, median `0.064937`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.016716`, avg `0.00219`, median `0.000401`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.020282`, avg `-0.001794`, median `-0.004047`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.02915`, avg `0.001027`, median `-0.001443`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.049888`, avg `0.013646`, median `0.020408`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.060629`, avg `0.047114`, median `0.064937`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.525`, primary_mae `0.016294`, avg `0.000459`, median `-0.003574`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.018546`, avg `-0.002582`, median `-0.00294`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.035413`, avg `-0.001238`, median `-0.00384`
- 20d: sample `40`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.066755`, avg `0.002014`, median `0.015735`
- 60d: sample `40`, primary_hit `0.625`, primary_closer `0.3`, primary_mae `0.074044`, avg `0.033811`, median `0.045791`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.5333`, primary_mae `0.016057`, avg `0.001519`, median `-0.000961`
- 5d: sample `60`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.020586`, avg `-0.002971`, median `-0.006423`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.5167`, primary_mae `0.026501`, avg `-0.000311`, median `-0.001443`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.35`, primary_mae `0.04446`, avg `0.015059`, median `0.020767`
- 60d: sample `60`, primary_hit `0.4`, primary_closer `0.4333`, primary_mae `0.048937`, avg `0.042458`, median `0.058512`

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
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.018244`, avg `0.003653`, median `0.00428`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.023096`, avg `0.002339`, median `0.006722`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.035418`, avg `0.004209`, median `0.001635`
- 20d: sample `40`, primary_hit `0.725`, primary_closer `0.35`, primary_mae `0.053755`, avg `0.018583`, median `0.030575`
- 60d: sample `40`, primary_hit `0.8`, primary_closer `0.225`, primary_mae `0.083827`, avg `0.056939`, median `0.070539`

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
