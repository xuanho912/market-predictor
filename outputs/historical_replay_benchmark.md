# Historical Replay Benchmark

Generated at: `2026-07-30T04:26:16.940406+00:00`
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
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.02332`
- secondary_mean_absolute_error: `0.01696`
- primary_error_advantage: `-0.00636`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.032141`
- secondary_mean_absolute_error: `0.022361`
- primary_error_advantage: `-0.00978`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.039491`
- secondary_mean_absolute_error: `0.031322`
- primary_error_advantage: `-0.008169`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.071843`
- secondary_mean_absolute_error: `0.050043`
- primary_error_advantage: `-0.0218`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.085915`
- secondary_mean_absolute_error: `0.076172`
- primary_error_advantage: `-0.009743`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.01669`, as_primary `0`, as_primary_hit `None`, avg `0.002009`, median `0.005148`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.021912`, as_primary `0`, as_primary_hit `None`, avg `0.003815`, median `0.003164`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.029401`, as_primary `0`, as_primary_hit `None`, avg `0.007665`, median `0.008358`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.042462`, as_primary `0`, as_primary_hit `None`, avg `0.026051`, median `0.024172`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.069833`, as_primary `0`, as_primary_hit `None`, avg `0.051898`, median `0.059722`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.018288`, as_primary `0`, as_primary_hit `None`, avg `0.002009`, median `0.005148`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.025205`, as_primary `0`, as_primary_hit `None`, avg `0.003815`, median `0.003164`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.036116`, as_primary `0`, as_primary_hit `None`, avg `0.007665`, median `0.008358`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.060832`, as_primary `0`, as_primary_hit `None`, avg `0.026051`, median `0.024172`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.087431`, as_primary `0`, as_primary_hit `None`, avg `0.051898`, median `0.059722`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.02332`, as_primary `80`, as_primary_hit `0.6375`, avg `0.002009`, median `0.005148`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.032141`, as_primary `80`, as_primary_hit `0.6`, avg `0.003815`, median `0.003164`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.039491`, as_primary `80`, as_primary_hit `0.5625`, avg `0.007665`, median `0.008358`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.071843`, as_primary `80`, as_primary_hit `0.65`, avg `0.026051`, median `0.024172`
- 60d: sample `80`, direction_hit `0.3375`, path_mae `0.085915`, as_primary `80`, as_primary_hit `0.6625`, avg `0.051898`, median `0.059722`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.016334`, as_primary `0`, as_primary_hit `None`, avg `0.002009`, median `0.005148`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.02184`, as_primary `0`, as_primary_hit `None`, avg `0.003815`, median `0.003164`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.029169`, as_primary `0`, as_primary_hit `None`, avg `0.007665`, median `0.008358`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.041822`, as_primary `0`, as_primary_hit `None`, avg `0.026051`, median `0.024172`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.066873`, as_primary `0`, as_primary_hit `None`, avg `0.051898`, median `0.059722`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.375`, primary_mae `0.02332`, avg `0.002009`, median `0.005148`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.3875`, primary_mae `0.032141`, avg `0.003815`, median `0.003164`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.039491`, avg `0.007665`, median `0.008358`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.071843`, avg `0.026051`, median `0.024172`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.085915`, avg `0.051898`, median `0.059722`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.375`, primary_mae `0.02332`, avg `0.002009`, median `0.005148`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.3875`, primary_mae `0.032141`, avg `0.003815`, median `0.003164`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.039491`, avg `0.007665`, median `0.008358`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.071843`, avg `0.026051`, median `0.024172`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.085915`, avg `0.051898`, median `0.059722`

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

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3625, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.02332, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.032141, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.039491, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.071843, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3375, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.085915, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016334, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02332, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3625, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.02332, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02184, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032141, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.032141, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029169, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039491, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.039491, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041822, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071843, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.071843, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066873, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.087431, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3375, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.085915, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.027234`, avg `-0.004292`, median `0.002815`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.031651`, avg `-0.009125`, median `0.001655`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.020978`, avg `-0.000565`, median `-0.000368`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.038432`, avg `0.015938`, median `-5.5e-05`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.065969`, avg `0.02124`, median `-0.024263`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.032445`, avg `0.002206`, median `0.00978`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.038084`, avg `-0.000854`, median `0.003648`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.625`, primary_mae `0.018899`, avg `0.004238`, median `-0.000368`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.046205`, avg `0.02222`, median `0.023723`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.080959`, avg `0.042447`, median `0.043194`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.027937`, avg `0.003433`, median `0.008128`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.051572`, avg `0.007994`, median `0.013962`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.062337`, avg `0.007386`, median `0.020901`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.112646`, avg `0.037937`, median `0.062929`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.146166`, avg `0.077131`, median `0.086441`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.375`, primary_mae `0.02332`, avg `0.002009`, median `0.005148`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.3875`, primary_mae `0.032141`, avg `0.003815`, median `0.003164`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.039491`, avg `0.007665`, median `0.008358`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.071843`, avg `0.026051`, median `0.024172`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.085915`, avg `0.051898`, median `0.059722`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.375`, primary_mae `0.02332`, avg `0.002009`, median `0.005148`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.3875`, primary_mae `0.032141`, avg `0.003815`, median `0.003164`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.039491`, avg `0.007665`, median `0.008358`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.071843`, avg `0.026051`, median `0.024172`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.085915`, avg `0.051898`, median `0.059722`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.020833`, avg `-0.001629`, median `0.001272`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.022306`, avg `-0.003778`, median `0.001195`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.6`, primary_mae `0.020681`, avg `-0.003009`, median `-0.003556`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.052662`, avg `0.007946`, median `0.003386`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.067036`, avg `0.021756`, median `0.033739`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.025808`, avg `0.005647`, median `0.00965`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.041975`, avg `0.011409`, median `0.013905`
- 10d: sample `40`, primary_hit `0.3`, primary_closer `0.275`, primary_mae `0.0583`, avg `0.018339`, median `0.025222`
- 20d: sample `40`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.091023`, avg `0.044155`, median `0.059913`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.104793`, avg `0.08204`, median `0.096261`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.375`, primary_mae `0.02332`, avg `0.002009`, median `0.005148`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.3875`, primary_mae `0.032141`, avg `0.003815`, median `0.003164`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.039491`, avg `0.007665`, median `0.008358`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.071843`, avg `0.026051`, median `0.024172`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.085915`, avg `0.051898`, median `0.059722`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.375`, primary_mae `0.02332`, avg `0.002009`, median `0.005148`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.3875`, primary_mae `0.032141`, avg `0.003815`, median `0.003164`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.039491`, avg `0.007665`, median `0.008358`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.071843`, avg `0.026051`, median `0.024172`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.085915`, avg `0.051898`, median `0.059722`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3625`, primary_closer `0.375`, primary_mae `0.02332`, avg `0.002009`, median `0.005148`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.3875`, primary_mae `0.032141`, avg `0.003815`, median `0.003164`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.039491`, avg `0.007665`, median `0.008358`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.071843`, avg `0.026051`, median `0.024172`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.425`, primary_mae `0.085915`, avg `0.051898`, median `0.059722`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
