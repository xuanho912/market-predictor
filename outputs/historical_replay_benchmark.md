# Historical Replay Benchmark

Generated at: `2026-10-30T18:09:51.467806+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.027561`
- secondary_mean_absolute_error: `0.0221`
- primary_error_advantage: `-0.005461`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.035188`
- secondary_mean_absolute_error: `0.029902`
- primary_error_advantage: `-0.005286`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.625`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.3375`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.051029`
- secondary_mean_absolute_error: `0.039666`
- primary_error_advantage: `-0.011363`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.062547`
- secondary_mean_absolute_error: `0.048005`
- primary_error_advantage: `-0.014542`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `-0.6`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.045659`
- secondary_mean_absolute_error: `0.037798`
- primary_error_advantage: `-0.007861`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.019873`, as_primary `0`, as_primary_hit `None`, avg `-0.000689`, median `-0.002837`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.0274`, as_primary `0`, as_primary_hit `None`, avg `0.004165`, median `0.007025`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.030913`, as_primary `0`, as_primary_hit `None`, avg `0.013886`, median `0.0201`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.03545`, as_primary `0`, as_primary_hit `None`, avg `0.025441`, median `0.031427`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.031482`, as_primary `0`, as_primary_hit `None`, avg `0.044912`, median `0.058454`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.02486`, as_primary `0`, as_primary_hit `None`, avg `-0.000689`, median `-0.002837`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.034173`, as_primary `0`, as_primary_hit `None`, avg `0.004165`, median `0.007025`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.043998`, as_primary `0`, as_primary_hit `None`, avg `0.013886`, median `0.0201`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.053085`, as_primary `0`, as_primary_hit `None`, avg `0.025441`, median `0.031427`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.038058`, as_primary `0`, as_primary_hit `None`, avg `0.044912`, median `0.058454`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.027561`, as_primary `80`, as_primary_hit `0.45`, avg `-0.000689`, median `-0.002837`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.035188`, as_primary `80`, as_primary_hit `0.5625`, avg `0.004165`, median `0.007025`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.051029`, as_primary `80`, as_primary_hit `0.6625`, avg `0.013886`, median `0.0201`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.062547`, as_primary `80`, as_primary_hit `0.725`, avg `0.025441`, median `0.031427`
- 60d: sample `80`, direction_hit `0.2`, path_mae `0.045659`, as_primary `80`, as_primary_hit `0.8`, avg `0.044912`, median `0.058454`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.019119`, as_primary `0`, as_primary_hit `None`, avg `-0.000689`, median `-0.002837`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.024472`, as_primary `0`, as_primary_hit `None`, avg `0.004165`, median `0.007025`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.02978`, as_primary `0`, as_primary_hit `None`, avg `0.013886`, median `0.0201`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.035023`, as_primary `0`, as_primary_hit `None`, avg `0.025441`, median `0.031427`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.031907`, as_primary `0`, as_primary_hit `None`, avg `0.044912`, median `0.058454`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.027561`, avg `-0.000689`, median `-0.002837`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.475`, primary_mae `0.035188`, avg `0.004165`, median `0.007025`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.051029`, avg `0.013886`, median `0.0201`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3875`, primary_mae `0.062547`, avg `0.025441`, median `0.031427`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.3375`, primary_mae `0.045659`, avg `0.044912`, median `0.058454`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.042812`, avg `-0.001546`, median `-0.005206`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.035861`, avg `0.010975`, median `0.00445`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.050716`, avg `0.025784`, median `0.032704`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.067108`, avg `0.043512`, median `0.053281`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.35`, primary_mae `0.03302`, avg `0.060312`, median `0.068874`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.021134`, avg `0.001613`, median `-0.001284`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.625`, primary_mae `0.020201`, avg `0.004751`, median `-0.003772`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.041999`, avg `0.013506`, median `0.015958`
- 20d: sample `40`, primary_hit `0.2`, primary_closer `0.425`, primary_mae `0.051344`, avg `0.030718`, median `0.030717`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.275`, primary_mae `0.045735`, avg `0.060215`, median `0.070461`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.025164`, avg `-0.004437`, median `-0.003305`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.064488`, avg `-0.003818`, median `0.012556`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.069403`, avg `0.002746`, median `0.013872`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.080392`, avg `-0.003185`, median `-0.002917`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.058145`, avg `-0.001093`, median `0.004209`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.021134, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.020201, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.041999, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.051344, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.03302, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019119, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027561, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.021134, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024472, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035188, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.020201, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.3375, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02978, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051029, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.041999, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035023, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062547, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.051344, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': -0.6, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031482, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045659, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.03302, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016529`, avg `-0.001501`, median `-0.004204`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.019644`, avg `0.003122`, median `-0.00117`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.044578`, avg `0.002094`, median `0.002287`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.042662`, avg `0.019394`, median `0.021287`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.046944`, avg `0.029337`, median `0.042816`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.01721`, avg `-4.9e-05`, median `-0.004204`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.02197`, avg `0.005974`, median `0.007025`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.049282`, avg `0.010922`, median `0.012283`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.056483`, avg `0.033216`, median `0.034376`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.057815`, avg `0.049601`, median `0.055066`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.043031`, avg `0.003012`, median `-0.001732`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.038052`, avg `0.012649`, median `0.014935`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.052825`, avg `0.033946`, median `0.034572`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.0625`, primary_mae `0.075872`, avg `0.053257`, median `0.054498`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.032794`, avg `0.064058`, median `0.072277`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.027561`, avg `-0.000689`, median `-0.002837`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.475`, primary_mae `0.035188`, avg `0.004165`, median `0.007025`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.051029`, avg `0.013886`, median `0.0201`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3875`, primary_mae `0.062547`, avg `0.025441`, median `0.031427`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.3375`, primary_mae `0.045659`, avg `0.044912`, median `0.058454`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.027561`, avg `-0.000689`, median `-0.002837`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.475`, primary_mae `0.035188`, avg `0.004165`, median `0.007025`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.051029`, avg `0.013886`, median `0.0201`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3875`, primary_mae `0.062547`, avg `0.025441`, median `0.031427`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.3375`, primary_mae `0.045659`, avg `0.044912`, median `0.058454`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.022477`, avg `-0.000404`, median `-0.002129`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.034963`, avg `0.001895`, median `0.00829`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.051134`, avg `0.009919`, median `0.015122`
- 20d: sample `60`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.061027`, avg `0.019417`, median `0.028608`
- 60d: sample `60`, primary_hit `0.2333`, primary_closer `0.3333`, primary_mae `0.049872`, avg `0.039779`, median `0.054701`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.042812`, avg `-0.001546`, median `-0.005206`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.035861`, avg `0.010975`, median `0.00445`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.050716`, avg `0.025784`, median `0.032704`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.067108`, avg `0.043512`, median `0.053281`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.35`, primary_mae `0.03302`, avg `0.060312`, median `0.068874`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.027561`, avg `-0.000689`, median `-0.002837`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.475`, primary_mae `0.035188`, avg `0.004165`, median `0.007025`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.051029`, avg `0.013886`, median `0.0201`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3875`, primary_mae `0.062547`, avg `0.025441`, median `0.031427`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.3375`, primary_mae `0.045659`, avg `0.044912`, median `0.058454`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5667`, primary_closer `0.4`, primary_mae `0.028555`, avg `-0.002332`, median `-0.004085`
- 5d: sample `60`, primary_hit `0.4`, primary_closer `0.4167`, primary_mae `0.040589`, avg `0.003379`, median `0.00829`
- 10d: sample `60`, primary_hit `0.3167`, primary_closer `0.3333`, primary_mae `0.055616`, avg `0.012575`, median `0.019703`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.3667`, primary_mae `0.06667`, avg `0.022433`, median `0.032541`
- 60d: sample `60`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.048751`, avg `0.033784`, median `0.042812`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.027561`, avg `-0.000689`, median `-0.002837`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.475`, primary_mae `0.035188`, avg `0.004165`, median `0.007025`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.051029`, avg `0.013886`, median `0.0201`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3875`, primary_mae `0.062547`, avg `0.025441`, median `0.031427`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.3375`, primary_mae `0.045659`, avg `0.044912`, median `0.058454`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
