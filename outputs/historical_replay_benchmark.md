# Historical Replay Benchmark

Generated at: `2026-10-06T01:31:12.541258+00:00`
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
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.016294`
- secondary_mean_absolute_error: `0.016024`
- primary_error_advantage: `-0.00027`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.020505`
- secondary_mean_absolute_error: `0.01883`
- primary_error_advantage: `-0.001675`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.024016`
- secondary_mean_absolute_error: `0.022614`
- primary_error_advantage: `-0.001402`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.048727`
- secondary_mean_absolute_error: `0.036257`
- primary_error_advantage: `-0.01247`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.9`
- primary_vs_secondary_accuracy_spread: `-0.575`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.050781`
- secondary_mean_absolute_error: `0.042339`
- primary_error_advantage: `-0.008442`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.014864`, as_primary `0`, as_primary_hit `None`, avg `-0.001403`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.019667`, as_primary `0`, as_primary_hit `None`, avg `0.000615`, median `-0.0029`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.023381`, as_primary `0`, as_primary_hit `None`, avg `0.005405`, median `0.004426`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.033412`, as_primary `0`, as_primary_hit `None`, avg `0.022814`, median `0.028383`
- 60d: sample `80`, direction_hit `0.9`, path_mae `0.042702`, as_primary `0`, as_primary_hit `None`, avg `0.08434`, median `0.101454`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.015979`, as_primary `20`, as_primary_hit `0.75`, avg `-0.001403`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.021198`, as_primary `20`, as_primary_hit `0.65`, avg `0.000615`, median `-0.0029`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.027358`, as_primary `20`, as_primary_hit `0.75`, avg `0.005405`, median `0.004426`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.047254`, as_primary `20`, as_primary_hit `0.8`, avg `0.022814`, median `0.028383`
- 60d: sample `80`, direction_hit `0.9`, path_mae `0.046313`, as_primary `20`, as_primary_hit `0.95`, avg `0.08434`, median `0.101454`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.016215`, as_primary `60`, as_primary_hit `0.3833`, avg `-0.001403`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.020031`, as_primary `60`, as_primary_hit `0.4`, avg `0.000615`, median `-0.0029`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.021968`, as_primary `60`, as_primary_hit `0.5833`, avg `0.005405`, median `0.004426`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.049103`, as_primary `60`, as_primary_hit `0.6833`, avg `0.022814`, median `0.028383`
- 60d: sample `80`, direction_hit `0.1`, path_mae `0.050104`, as_primary `60`, as_primary_hit `0.8833`, avg `0.08434`, median `0.101454`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.01492`, as_primary `0`, as_primary_hit `None`, avg `-0.001403`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.018092`, as_primary `0`, as_primary_hit `None`, avg `0.000615`, median `-0.0029`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.021093`, as_primary `0`, as_primary_hit `None`, avg `0.005405`, median `0.004426`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.03054`, as_primary `0`, as_primary_hit `None`, avg `0.022814`, median `0.028383`
- 60d: sample `80`, direction_hit `0.9`, path_mae `0.044292`, as_primary `0`, as_primary_hit `None`, avg `0.08434`, median `0.101454`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.6`, primary_mae `0.012382`, avg `0.008195`, median `0.012449`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.019084`, avg `0.009581`, median `0.009975`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.029418`, avg `0.015006`, median `0.016702`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.04304`, avg `0.037957`, median `0.034737`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.5`, primary_mae `0.032878`, avg `0.094492`, median `0.104666`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.5`, primary_mae `0.017598`, avg `-0.004603`, median `-0.003835`
- 5d: sample `60`, primary_hit `0.6`, primary_closer `0.4167`, primary_mae `0.020978`, avg `-0.002373`, median `-0.00613`
- 10d: sample `60`, primary_hit `0.4167`, primary_closer `0.5333`, primary_mae `0.022215`, avg `0.002204`, median `0.003868`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.3667`, primary_mae `0.050623`, avg `0.017766`, median `0.026945`
- 60d: sample `60`, primary_hit `0.1167`, primary_closer `0.4667`, primary_mae `0.056749`, avg `0.080956`, median `0.100663`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.6`, primary_mae `0.012382`, avg `0.008195`, median `0.012449`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.019084`, avg `0.009581`, median `0.009975`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.029418`, avg `0.015006`, median `0.016702`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.04304`, avg `0.037957`, median `0.034737`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.5`, primary_mae `0.032878`, avg `0.094492`, median `0.104666`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.016196`, avg `-0.005617`, median `-0.004876`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.01883`, avg `-0.003581`, median `-0.004714`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.55`, primary_mae `0.02305`, avg `0.001372`, median `0.004736`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.425`, primary_mae `0.057191`, avg `0.011995`, median `0.027677`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.525`, primary_mae `0.042157`, avg `0.087876`, median `0.10578`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.020402`, avg `-0.002574`, median `-0.002451`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.025273`, avg `4.3e-05`, median `-0.010492`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020545`, avg `0.00387`, median `0.00107`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.037488`, avg `0.02931`, median `0.026541`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.35`, primary_mae `0.085933`, avg `0.067117`, median `0.07246`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.012382, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01883, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.020545, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.037488, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.032878, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014864, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016215, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.012382, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018092, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021198, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01883, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021093, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027358, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.020545, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03054, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049103, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.037488, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.9, 'primary_vs_secondary_accuracy_spread': -0.575, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042702, 'direction_hit_rate': 0.9}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050104, 'direction_hit_rate': 0.1}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.032878, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.013706`, avg `0.005815`, median `0.008014`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.018062`, avg `0.006695`, median `0.008828`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.125`, primary_mae `0.029886`, avg `0.009347`, median `0.01205`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.052559`, avg `0.026788`, median `0.029102`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.75`, primary_mae `0.010189`, avg `0.114868`, median `0.11635`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.013619`, avg `0.005263`, median `0.012314`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.020181`, avg `0.006101`, median `0.008828`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.1875`, primary_mae `0.031213`, avg `0.009625`, median `0.01205`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.046299`, avg `0.033821`, median `0.032756`
- 60d: sample `16`, primary_hit `1.0`, primary_closer `0.5625`, primary_mae `0.023163`, avg `0.104288`, median `0.110419`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.021453`, avg `-0.009172`, median `-0.010089`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.02583`, avg `-0.00313`, median `-0.005714`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.039027`, avg `0.001881`, median `0.012828`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.079116`, avg `0.010585`, median `0.030078`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.5625`, primary_mae `0.036276`, avg `0.093015`, median `0.108489`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.525`, primary_mae `0.016294`, avg `-0.001403`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.020505`, avg `0.000615`, median `-0.0029`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.024016`, avg `0.005405`, median `0.004426`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.048727`, avg `0.022814`, median `0.028383`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.475`, primary_mae `0.050781`, avg `0.08434`, median `0.101454`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.525`, primary_mae `0.016294`, avg `-0.001403`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.020505`, avg `0.000615`, median `-0.0029`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.024016`, avg `0.005405`, median `0.004426`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.048727`, avg `0.022814`, median `0.028383`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.475`, primary_mae `0.050781`, avg `0.08434`, median `0.101454`

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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.5`, primary_mae `0.017598`, avg `-0.004603`, median `-0.003835`
- 5d: sample `60`, primary_hit `0.6`, primary_closer `0.4167`, primary_mae `0.020978`, avg `-0.002373`, median `-0.00613`
- 10d: sample `60`, primary_hit `0.4167`, primary_closer `0.5333`, primary_mae `0.022215`, avg `0.002204`, median `0.003868`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.3667`, primary_mae `0.050623`, avg `0.017766`, median `0.026945`
- 60d: sample `60`, primary_hit `0.1167`, primary_closer `0.4667`, primary_mae `0.056749`, avg `0.080956`, median `0.100663`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.525`, primary_mae `0.016294`, avg `-0.001403`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.020505`, avg `0.000615`, median `-0.0029`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.024016`, avg `0.005405`, median `0.004426`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.048727`, avg `0.022814`, median `0.028383`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.475`, primary_mae `0.050781`, avg `0.08434`, median `0.101454`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.525`, primary_mae `0.016294`, avg `-0.001403`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.020505`, avg `0.000615`, median `-0.0029`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.024016`, avg `0.005405`, median `0.004426`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.048727`, avg `0.022814`, median `0.028383`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.475`, primary_mae `0.050781`, avg `0.08434`, median `0.101454`

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
