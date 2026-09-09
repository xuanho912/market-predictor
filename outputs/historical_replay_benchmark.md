# Historical Replay Benchmark

Generated at: `2026-09-09T23:31:06.931611+00:00`
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
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.018268`
- secondary_mean_absolute_error: `0.013039`
- primary_error_advantage: `-0.005229`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.018079`
- secondary_mean_absolute_error: `0.014412`
- primary_error_advantage: `-0.003667`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.030414`
- secondary_mean_absolute_error: `0.024933`
- primary_error_advantage: `-0.005481`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.056674`
- secondary_mean_absolute_error: `0.036253`
- primary_error_advantage: `-0.020421`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2625`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.475`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.087958`
- secondary_mean_absolute_error: `0.058046`
- primary_error_advantage: `-0.029912`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.012146`, as_primary `0`, as_primary_hit `None`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.014869`, as_primary `0`, as_primary_hit `None`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.025316`, as_primary `0`, as_primary_hit `None`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.036218`, as_primary `0`, as_primary_hit `None`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.059138`, as_primary `0`, as_primary_hit `None`, avg `0.04334`, median `0.05856`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.013944`, as_primary `0`, as_primary_hit `None`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.017681`, as_primary `0`, as_primary_hit `None`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.036092`, as_primary `0`, as_primary_hit `None`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.052502`, as_primary `0`, as_primary_hit `None`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.069538`, as_primary `0`, as_primary_hit `None`, avg `0.04334`, median `0.05856`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.018268`, as_primary `80`, as_primary_hit `0.575`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.018079`, as_primary `80`, as_primary_hit `0.625`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.030414`, as_primary `80`, as_primary_hit `0.425`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.056674`, as_primary `80`, as_primary_hit `0.6625`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, direction_hit `0.2625`, path_mae `0.087958`, as_primary `80`, as_primary_hit `0.7375`, avg `0.04334`, median `0.05856`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.012366`, as_primary `0`, as_primary_hit `None`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.014549`, as_primary `0`, as_primary_hit `None`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.022173`, as_primary `0`, as_primary_hit `None`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.033532`, as_primary `0`, as_primary_hit `None`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.058147`, as_primary `0`, as_primary_hit `None`, avg `0.04334`, median `0.05856`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.018268`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.018079`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.030414`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.3`, primary_mae `0.056674`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.325`, primary_mae `0.087958`, avg `0.04334`, median `0.05856`

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
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.3833`, primary_mae `0.015071`, avg `2.3e-05`, median `0.000609`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.35`, primary_mae `0.014331`, avg `0.00035`, median `0.001723`
- 10d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.025351`, avg `-0.00395`, median `-0.008001`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.3`, primary_mae `0.05971`, avg `0.003482`, median `0.012243`
- 60d: sample `60`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.093895`, avg `0.030861`, median `0.047025`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.2`, primary_mae `0.027856`, avg `0.00896`, median `0.010341`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.029321`, avg `0.011765`, median `0.011918`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.045601`, avg `0.021005`, median `0.019602`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.3`, primary_mae `0.047567`, avg `0.041845`, median `0.036414`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.070148`, avg `0.080777`, median `0.077217`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.015071, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.014331, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.025351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047567, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.070148, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012146, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018268, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.015071, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014549, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018079, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.014331, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022173, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036092, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.025351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033532, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056674, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047567, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.475, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058147, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.087958, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.070148, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.022492`, avg `-0.0016`, median `-0.000127`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.014056`, avg `-0.007978`, median `-0.008697`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.032475`, avg `0.004226`, median `0.003189`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.064069`, avg `0.020874`, median `0.030181`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.127573`, avg `0.059214`, median `0.072376`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.020541`, avg `-0.005473`, median `-0.004159`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.017847`, avg `-0.010343`, median `-0.008697`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.028427`, avg `-0.002918`, median `-0.006514`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.059654`, avg `0.013856`, median `0.029731`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.115326`, avg `0.043117`, median `0.063523`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.028872`, avg `0.010358`, median `0.011055`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.028299`, avg `0.011115`, median `0.011612`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.044017`, avg `0.018835`, median `0.019602`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.045515`, avg `0.039351`, median `0.036414`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.069319`, avg `0.080578`, median `0.077217`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.018268`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.018079`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.030414`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.3`, primary_mae `0.056674`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.325`, primary_mae `0.087958`, avg `0.04334`, median `0.05856`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.018268`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.018079`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.030414`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.3`, primary_mae `0.056674`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.325`, primary_mae `0.087958`, avg `0.04334`, median `0.05856`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.011042`, avg `-0.001182`, median `-0.002618`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.010754`, avg `-0.002159`, median `0.001088`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.022541`, avg `-0.008195`, median `-0.011447`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.066368`, avg `-0.008574`, median `0.001741`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.082982`, avg `0.01961`, median `0.045303`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.2833`, primary_mae `0.020676`, avg `0.003404`, median `0.006118`
- 5d: sample `60`, primary_hit `0.3667`, primary_closer `0.3333`, primary_mae `0.02052`, avg `0.004991`, median `0.007974`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.3667`, primary_mae `0.033038`, avg `0.005783`, median `-0.002174`
- 20d: sample `60`, primary_hit `0.2833`, primary_closer `0.2833`, primary_mae `0.053443`, avg `0.020288`, median `0.027649`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.2833`, primary_mae `0.089616`, avg `0.051249`, median `0.0618`

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
