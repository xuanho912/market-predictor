# Historical Replay Benchmark

Generated at: `2026-08-27T22:19:44.349781+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
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
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.015549`
- secondary_mean_absolute_error: `0.016948`
- primary_error_advantage: `0.001399`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.020554`
- secondary_mean_absolute_error: `0.020628`
- primary_error_advantage: `7.4e-05`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.035533`
- secondary_mean_absolute_error: `0.030194`
- primary_error_advantage: `-0.005339`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.057777`
- secondary_mean_absolute_error: `0.050253`
- primary_error_advantage: `-0.007524`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.077411`
- secondary_mean_absolute_error: `0.070339`
- primary_error_advantage: `-0.007072`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5125`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.014712`, as_primary `0`, as_primary_hit `None`, avg `0.000302`, median `0.002198`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.018342`, as_primary `0`, as_primary_hit `None`, avg `-2.6e-05`, median `0.001056`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.027377`, as_primary `0`, as_primary_hit `None`, avg `0.000362`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.033922`, as_primary `0`, as_primary_hit `None`, avg `0.006331`, median `0.01801`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.05817`, as_primary `0`, as_primary_hit `None`, avg `0.02914`, median `0.026371`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.015586`, as_primary `60`, as_primary_hit `0.5833`, avg `0.000302`, median `0.002198`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.020499`, as_primary `60`, as_primary_hit `0.5333`, avg `-2.6e-05`, median `0.001056`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.037548`, as_primary `60`, as_primary_hit `0.5`, avg `0.000362`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.05175`, as_primary `60`, as_primary_hit `0.6833`, avg `0.006331`, median `0.01801`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.071253`, as_primary `60`, as_primary_hit `0.65`, avg `0.02914`, median `0.026371`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.018004`, as_primary `20`, as_primary_hit `0.45`, avg `0.000302`, median `0.002198`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.021792`, as_primary `20`, as_primary_hit `0.55`, avg `-2.6e-05`, median `0.001056`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.033902`, as_primary `20`, as_primary_hit `0.3`, avg `0.000362`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.067848`, as_primary `20`, as_primary_hit `0.55`, avg `0.006331`, median `0.01801`
- 60d: sample `80`, direction_hit `0.35`, path_mae `0.077508`, as_primary `20`, as_primary_hit `0.65`, avg `0.02914`, median `0.026371`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.014992`, as_primary `0`, as_primary_hit `None`, avg `0.000302`, median `0.002198`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.01817`, as_primary `0`, as_primary_hit `None`, avg `-2.6e-05`, median `0.001056`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.025443`, as_primary `0`, as_primary_hit `None`, avg `0.000362`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.034873`, as_primary `0`, as_primary_hit `None`, avg `0.006331`, median `0.01801`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.054832`, as_primary `0`, as_primary_hit `None`, avg `0.02914`, median `0.026371`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.5375`, primary_mae `0.015549`, avg `0.000302`, median `0.002198`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.020554`, avg `-2.6e-05`, median `0.001056`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.035533`, avg `0.000362`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.057777`, avg `0.006331`, median `0.01801`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5125`, primary_mae `0.077411`, avg `0.02914`, median `0.026371`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6`, primary_closer `0.5333`, primary_mae `0.015992`, avg `0.001672`, median `0.002677`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.4833`, primary_mae `0.021861`, avg `0.001556`, median `0.001499`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.4833`, primary_mae `0.039133`, avg `-0.000311`, median `-0.008001`
- 20d: sample `60`, primary_hit `0.5833`, primary_closer `0.4`, primary_mae `0.062633`, avg `0.002511`, median `0.011092`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.4833`, primary_mae `0.075585`, avg `0.027177`, median `0.0209`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.014221`, avg `-0.003809`, median `-0.000127`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.016633`, avg `-0.004774`, median `-0.004713`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.024733`, avg `0.00238`, median `-0.006389`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.7`, primary_mae `0.043209`, avg `0.01779`, median `0.027848`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.082887`, avg `0.035029`, median `0.052814`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.014221, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016633, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.024733, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.043209, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.075585, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014712, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018004, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.014221, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01817, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021792, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016633, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025443, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037548, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.024733, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033922, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067848, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.043209, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054832, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.077508, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.075585, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.011047`, avg `-0.006581`, median `-0.000127`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.015892`, avg `-0.0078`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.018641`, avg `0.005104`, median `0.013417`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.043178`, avg `0.014801`, median `0.027848`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.076148`, avg `0.038143`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.014051`, avg `-0.003091`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.017188`, avg `-0.003502`, median `-0.004713`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.022658`, avg `0.00703`, median `0.013417`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.043946`, avg `0.015519`, median `0.027848`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.082822`, avg `0.032284`, median `0.052814`

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
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.5375`, primary_mae `0.015549`, avg `0.000302`, median `0.002198`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.020554`, avg `-2.6e-05`, median `0.001056`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.035533`, avg `0.000362`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.057777`, avg `0.006331`, median `0.01801`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5125`, primary_mae `0.077411`, avg `0.02914`, median `0.026371`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.5375`, primary_mae `0.015549`, avg `0.000302`, median `0.002198`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.020554`, avg `-2.6e-05`, median `0.001056`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.035533`, avg `0.000362`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.057777`, avg `0.006331`, median `0.01801`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5125`, primary_mae `0.077411`, avg `0.02914`, median `0.026371`

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
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.5167`, primary_mae `0.014459`, avg `0.00054`, median `0.001813`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.4167`, primary_mae `0.020419`, avg `-0.000898`, median `0.000781`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.4833`, primary_mae `0.034297`, avg `0.000887`, median `-0.007064`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.4167`, primary_mae `0.062127`, avg `0.00709`, median `0.019103`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.4333`, primary_mae `0.087958`, avg `0.041054`, median `0.047922`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.5375`, primary_mae `0.015549`, avg `0.000302`, median `0.002198`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.020554`, avg `-2.6e-05`, median `0.001056`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.035533`, avg `0.000362`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.057777`, avg `0.006331`, median `0.01801`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5125`, primary_mae `0.077411`, avg `0.02914`, median `0.026371`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.5375`, primary_mae `0.015549`, avg `0.000302`, median `0.002198`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.020554`, avg `-2.6e-05`, median `0.001056`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.035533`, avg `0.000362`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.057777`, avg `0.006331`, median `0.01801`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5125`, primary_mae `0.077411`, avg `0.02914`, median `0.026371`

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
