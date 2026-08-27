# Historical Replay Benchmark

Generated at: `2026-08-27T14:48:41.634101+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `PROMISING`
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
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.017885`
- secondary_mean_absolute_error: `0.019494`
- primary_error_advantage: `0.001609`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.021342`
- secondary_mean_absolute_error: `0.022025`
- primary_error_advantage: `0.000683`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.035319`
- secondary_mean_absolute_error: `0.031357`
- primary_error_advantage: `-0.003962`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.054928`
- secondary_mean_absolute_error: `0.047184`
- primary_error_advantage: `-0.007744`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.072255`
- secondary_mean_absolute_error: `0.073488`
- primary_error_advantage: `0.001233`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5125`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.015793`, as_primary `0`, as_primary_hit `None`, avg `-0.000408`, median `0.001813`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.019014`, as_primary `0`, as_primary_hit `None`, avg `-0.000913`, median `0.000781`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.027026`, as_primary `0`, as_primary_hit `None`, avg `0.000942`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.032882`, as_primary `0`, as_primary_hit `None`, avg `0.006942`, median `0.015026`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.056491`, as_primary `0`, as_primary_hit `None`, avg `0.02934`, median `0.031178`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.017923`, as_primary `60`, as_primary_hit `0.5667`, avg `-0.000408`, median `0.001813`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.021286`, as_primary `60`, as_primary_hit `0.5333`, avg `-0.000913`, median `0.000781`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.037334`, as_primary `60`, as_primary_hit `0.4833`, avg `0.000942`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.048901`, as_primary `60`, as_primary_hit `0.6833`, avg `0.006942`, median `0.015026`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.066097`, as_primary `60`, as_primary_hit `0.6833`, avg `0.02934`, median `0.031178`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.020531`, as_primary `20`, as_primary_hit `0.45`, avg `-0.000408`, median `0.001813`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.023771`, as_primary `20`, as_primary_hit `0.55`, avg `-0.000913`, median `0.000781`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.034256`, as_primary `20`, as_primary_hit `0.3`, avg `0.000942`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.06143`, as_primary `20`, as_primary_hit `0.55`, avg `0.006942`, median `0.015026`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.08132`, as_primary `20`, as_primary_hit `0.65`, avg `0.02934`, median `0.031178`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.015931`, as_primary `0`, as_primary_hit `None`, avg `-0.000408`, median `0.001813`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.018852`, as_primary `0`, as_primary_hit `None`, avg `-0.000913`, median `0.000781`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.024892`, as_primary `0`, as_primary_hit `None`, avg `0.000942`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.032786`, as_primary `0`, as_primary_hit `None`, avg `0.006942`, median `0.015026`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.053803`, as_primary `0`, as_primary_hit `None`, avg `0.02934`, median `0.031178`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.55`, primary_mae `0.017885`, avg `-0.000408`, median `0.001813`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.021342`, avg `-0.000913`, median `0.000781`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.035319`, avg `0.000942`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.054928`, avg `0.006942`, median `0.015026`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.5125`, primary_mae `0.072255`, avg `0.02934`, median `0.031178`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5667`, primary_closer `0.5667`, primary_mae `0.017776`, avg `-0.000216`, median `0.001417`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.5167`, primary_mae `0.022386`, avg `1.4e-05`, median `0.001271`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.4833`, primary_mae `0.037851`, avg `-9.3e-05`, median `-0.008297`
- 20d: sample `60`, primary_hit `0.5833`, primary_closer `0.3833`, primary_mae `0.060926`, avg `0.004398`, median `0.011092`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.4833`, primary_mae `0.071758`, avg `0.028736`, median `0.026371`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.018215`, avg `-0.000985`, median `0.001949`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.018211`, avg `-0.003692`, median `-0.002115`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.027724`, avg `0.004048`, median `-0.001577`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.7`, primary_mae `0.036935`, avg `0.014573`, median `0.024592`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.073745`, avg `0.031153`, median `0.052814`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.017776, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018211, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.027724, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.036935, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.071758, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015793, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020531, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.017776, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018852, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023771, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018211, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024892, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037334, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.027724, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032786, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06143, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.036935, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053803, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.08132, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.071758, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.020713`, avg `-0.006581`, median `-0.000127`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.020407`, avg `-0.0078`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.023395`, avg `0.005104`, median `0.013417`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.033873`, avg `0.014801`, median `0.027848`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.064682`, avg `0.038143`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.019899`, avg `-0.003091`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.019446`, avg `-0.003502`, median `-0.004713`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.025756`, avg `0.00703`, median `0.013417`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.036698`, avg `0.015519`, median `0.027848`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.073133`, avg `0.032284`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.007225`, avg `-0.001374`, median `-0.001535`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.009859`, avg `-0.007511`, median `-0.007934`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.01967`, avg `-0.008114`, median `-0.00951`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.067005`, avg `-0.007696`, median `0.006712`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.081696`, avg `0.028385`, median `0.045303`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.55`, primary_mae `0.017885`, avg `-0.000408`, median `0.001813`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.021342`, avg `-0.000913`, median `0.000781`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.035319`, avg `0.000942`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.054928`, avg `0.006942`, median `0.015026`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.5125`, primary_mae `0.072255`, avg `0.02934`, median `0.031178`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.55`, primary_mae `0.017885`, avg `-0.000408`, median `0.001813`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.021342`, avg `-0.000913`, median `0.000781`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.035319`, avg `0.000942`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.054928`, avg `0.006942`, median `0.015026`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.5125`, primary_mae `0.072255`, avg `0.02934`, median `0.031178`

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
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.016499`, avg `0.000967`, median `0.001813`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.4333`, primary_mae `0.02057`, avg `-0.000684`, median `0.000781`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.5`, primary_mae `0.032697`, avg `0.002977`, median `-0.006885`
- 20d: sample `60`, primary_hit `0.6333`, primary_closer `0.4167`, primary_mae `0.057191`, avg `0.009042`, median `0.017157`
- 60d: sample `60`, primary_hit `0.6333`, primary_closer `0.4333`, primary_mae `0.079339`, avg `0.043066`, median `0.055734`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.55`, primary_mae `0.017885`, avg `-0.000408`, median `0.001813`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.021342`, avg `-0.000913`, median `0.000781`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.035319`, avg `0.000942`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.054928`, avg `0.006942`, median `0.015026`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.5125`, primary_mae `0.072255`, avg `0.02934`, median `0.031178`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.55`, primary_mae `0.017885`, avg `-0.000408`, median `0.001813`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4875`, primary_mae `0.021342`, avg `-0.000913`, median `0.000781`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.475`, primary_mae `0.035319`, avg `0.000942`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.054928`, avg `0.006942`, median `0.015026`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.5125`, primary_mae `0.072255`, avg `0.02934`, median `0.031178`

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
