# Historical Replay Benchmark

Generated at: `2026-09-14T18:07:37.487914+00:00`
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
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.019593`
- secondary_mean_absolute_error: `0.013361`
- primary_error_advantage: `-0.006232`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.021313`
- secondary_mean_absolute_error: `0.016316`
- primary_error_advantage: `-0.004997`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.029637`
- secondary_mean_absolute_error: `0.024722`
- primary_error_advantage: `-0.004915`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.06445`
- secondary_mean_absolute_error: `0.036237`
- primary_error_advantage: `-0.028213`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.109766`
- secondary_mean_absolute_error: `0.072134`
- primary_error_advantage: `-0.037632`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013508`, as_primary `0`, as_primary_hit `None`, avg `0.002092`, median `0.004891`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.017216`, as_primary `0`, as_primary_hit `None`, avg `-0.00116`, median `0.001195`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.028492`, as_primary `0`, as_primary_hit `None`, avg `-0.001312`, median `-0.006203`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.03855`, as_primary `0`, as_primary_hit `None`, avg `0.014018`, median `0.017664`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.07613`, as_primary `0`, as_primary_hit `None`, avg `0.036356`, median `0.062573`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.014984`, as_primary `0`, as_primary_hit `None`, avg `0.002092`, median `0.004891`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.022073`, as_primary `0`, as_primary_hit `None`, avg `-0.00116`, median `0.001195`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.038667`, as_primary `0`, as_primary_hit `None`, avg `-0.001312`, median `-0.006203`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.056515`, as_primary `0`, as_primary_hit `None`, avg `0.014018`, median `0.017664`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.081459`, as_primary `0`, as_primary_hit `None`, avg `0.036356`, median `0.062573`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.019593`, as_primary `80`, as_primary_hit `0.6125`, avg `0.002092`, median `0.004891`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.021313`, as_primary `80`, as_primary_hit `0.55`, avg `-0.00116`, median `0.001195`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.029637`, as_primary `80`, as_primary_hit `0.425`, avg `-0.001312`, median `-0.006203`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.06445`, as_primary `80`, as_primary_hit `0.6375`, avg `0.014018`, median `0.017664`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.109766`, as_primary `80`, as_primary_hit `0.675`, avg `0.036356`, median `0.062573`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013361`, as_primary `0`, as_primary_hit `None`, avg `0.002092`, median `0.004891`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.016316`, as_primary `0`, as_primary_hit `None`, avg `-0.00116`, median `0.001195`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.024722`, as_primary `0`, as_primary_hit `None`, avg `-0.001312`, median `-0.006203`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.036237`, as_primary `0`, as_primary_hit `None`, avg `0.014018`, median `0.017664`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.072134`, as_primary `0`, as_primary_hit `None`, avg `0.036356`, median `0.062573`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.275`, primary_mae `0.019593`, avg `0.002092`, median `0.004891`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.3375`, primary_mae `0.021313`, avg `-0.00116`, median `0.001195`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.029637`, avg `-0.001312`, median `-0.006203`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.2625`, primary_mae `0.06445`, avg `0.014018`, median `0.017664`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.35`, primary_mae `0.109766`, avg `0.036356`, median `0.062573`

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
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.2833`, primary_mae `0.020706`, avg `0.0`, median `0.001095`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.3167`, primary_mae `0.02081`, avg `-0.00298`, median `0.000888`
- 10d: sample `60`, primary_hit `0.6333`, primary_closer `0.3833`, primary_mae `0.028914`, avg `-0.006742`, median `-0.008973`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.2333`, primary_mae `0.069715`, avg `0.006405`, median `0.008407`
- 60d: sample `60`, primary_hit `0.3667`, primary_closer `0.3667`, primary_mae `0.117467`, avg `0.026213`, median `0.059722`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.016254`, avg `0.008365`, median `0.011608`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.022823`, avg `0.004299`, median `0.003708`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.031804`, avg `0.014977`, median `0.007815`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.35`, primary_mae `0.048656`, avg `0.036857`, median `0.032326`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.086662`, avg `0.066782`, median `0.074283`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.016254, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.02081, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.028914, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.048656, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.086662, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013361, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019593, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.016254, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016316, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022073, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.02081, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024722, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038667, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.028914, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036237, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06445, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.048656, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072134, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.109766, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.086662, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.029101`, avg `0.001097`, median `0.003063`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.030203`, avg `-0.00198`, median `0.003417`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.021977`, avg `0.004504`, median `-0.003208`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.06918`, avg `0.042901`, median `0.044911`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.140777`, avg `0.091304`, median `0.111045`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.026852`, avg `-0.003722`, median `0.000341`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.025988`, avg `-0.010827`, median `-0.002115`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.016735`, avg `-0.007575`, median `-0.008733`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.046461`, avg `0.015683`, median `0.013313`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.082472`, avg `0.028142`, median `0.029112`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.1875`, primary_mae `0.021272`, avg `0.002604`, median `0.003143`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.026911`, avg `0.004441`, median `0.006922`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.049715`, avg `-0.006711`, median `-0.019376`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.1875`, primary_mae `0.093094`, avg `-0.001825`, median `-0.001846`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.211384`, avg `0.033016`, median `0.091642`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.275`, primary_mae `0.019593`, avg `0.002092`, median `0.004891`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.3375`, primary_mae `0.021313`, avg `-0.00116`, median `0.001195`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.029637`, avg `-0.001312`, median `-0.006203`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.2625`, primary_mae `0.06445`, avg `0.014018`, median `0.017664`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.35`, primary_mae `0.109766`, avg `0.036356`, median `0.062573`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.275`, primary_mae `0.019593`, avg `0.002092`, median `0.004891`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.3375`, primary_mae `0.021313`, avg `-0.00116`, median `0.001195`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.029637`, avg `-0.001312`, median `-0.006203`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.2625`, primary_mae `0.06445`, avg `0.014018`, median `0.017664`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.35`, primary_mae `0.109766`, avg `0.036356`, median `0.062573`

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
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.275`, primary_mae `0.019593`, avg `0.002092`, median `0.004891`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.3375`, primary_mae `0.021313`, avg `-0.00116`, median `0.001195`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.029637`, avg `-0.001312`, median `-0.006203`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.2625`, primary_mae `0.06445`, avg `0.014018`, median `0.017664`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.35`, primary_mae `0.109766`, avg `0.036356`, median `0.062573`

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
