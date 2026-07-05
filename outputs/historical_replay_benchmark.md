# Historical Replay Benchmark

Generated at: `2026-07-05T15:32:33.645361+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_mixed_or_not_better_keep_confidence_capped`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.015214`
- secondary_mean_absolute_error: `0.013087`
- primary_error_advantage: `-0.002127`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.01811`
- secondary_mean_absolute_error: `0.017021`
- primary_error_advantage: `-0.001089`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.022581`
- secondary_mean_absolute_error: `0.018888`
- primary_error_advantage: `-0.003693`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.036203`
- secondary_mean_absolute_error: `0.038231`
- primary_error_advantage: `0.002028`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.060959`
- secondary_mean_absolute_error: `0.056967`
- primary_error_advantage: `-0.003992`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.013401`, as_primary `0`, as_primary_hit `None`, avg `-0.001166`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.016596`, as_primary `0`, as_primary_hit `None`, avg `-0.002632`, median `-0.003063`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.018519`, as_primary `0`, as_primary_hit `None`, avg `0.001648`, median `-0.000307`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.022317`, as_primary `0`, as_primary_hit `None`, avg `0.007811`, median `0.01201`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.051764`, as_primary `0`, as_primary_hit `None`, avg `0.008408`, median `0.003509`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.015214`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.001166`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.01811`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.002632`, median `-0.003063`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.022581`, as_primary `80`, as_primary_hit `0.4875`, avg `0.001648`, median `-0.000307`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.036203`, as_primary `80`, as_primary_hit `0.6875`, avg `0.007811`, median `0.01201`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.060959`, as_primary `80`, as_primary_hit `0.5125`, avg `0.008408`, median `0.003509`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.013059`, as_primary `0`, as_primary_hit `None`, avg `-0.001166`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.017021`, as_primary `0`, as_primary_hit `None`, avg `-0.002632`, median `-0.003063`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.018955`, as_primary `0`, as_primary_hit `None`, avg `0.001648`, median `-0.000307`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.043193`, as_primary `0`, as_primary_hit `None`, avg `0.007811`, median `0.01201`
- 60d: sample `80`, direction_hit `0.4875`, path_mae `0.065295`, as_primary `0`, as_primary_hit `None`, avg `0.008408`, median `0.003509`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.012875`, as_primary `0`, as_primary_hit `None`, avg `-0.001166`, median `-0.001412`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.016415`, as_primary `0`, as_primary_hit `None`, avg `-0.002632`, median `-0.003063`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.017852`, as_primary `0`, as_primary_hit `None`, avg `0.001648`, median `-0.000307`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.021786`, as_primary `0`, as_primary_hit `None`, avg `0.007811`, median `0.01201`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.05069`, as_primary `0`, as_primary_hit `None`, avg `0.008408`, median `0.003509`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.016226`, avg `0.001398`, median `-8.6e-05`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.4333`, primary_mae `0.019535`, avg `0.000211`, median `0.00286`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.45`, primary_mae `0.026084`, avg `0.004385`, median `0.003079`
- 20d: sample `60`, primary_hit `0.6667`, primary_closer `0.6167`, primary_mae `0.035996`, avg `0.005261`, median `0.0103`
- 60d: sample `60`, primary_hit `0.45`, primary_closer `0.4667`, primary_mae `0.0566`, avg `-0.0009`, median `-0.007739`

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.012176`, avg `-0.008858`, median `-0.010064`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.013833`, avg `-0.01116`, median `-0.010559`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.012072`, avg `-0.006564`, median `-0.006885`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.036822`, avg `0.015459`, median `0.020913`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.074035`, avg `0.036332`, median `0.052814`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.014299`, avg `0.001634`, median `-0.00052`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.015969`, avg `0.000266`, median `0.00286`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.020784`, avg `0.007579`, median `0.003193`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.55`, primary_mae `0.037414`, avg `0.005152`, median `0.0103`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.053539`, avg `0.000353`, median `-0.017782`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.016128`, avg `-0.003965`, median `-0.008109`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.02025`, avg `-0.00553`, median `-0.01048`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.024379`, avg `-0.004283`, median `-0.006885`
- 20d: sample `40`, primary_hit `0.75`, primary_closer `0.475`, primary_mae `0.034992`, avg `0.010469`, median `0.015289`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.068379`, avg `0.016463`, median `0.008026`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.014299, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.015969, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.020784, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.034992, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.053539, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012875, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015214, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.014299, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016415, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01811, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.015969, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017852, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022581, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.020784, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021786, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043193, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.034992, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05069, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065295, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.053539, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.013106`, avg `-0.010839`, median `-0.009739`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.014594`, avg `-0.008852`, median `-0.008736`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.015599`, avg `-0.008261`, median `-0.012789`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.043592`, avg `0.004923`, median `0.016513`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.110063`, avg `-0.005336`, median `-0.004019`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.012372`, avg `-0.011114`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.014207`, avg `-0.012154`, median `-0.012995`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.013377`, avg `-0.006933`, median `-0.008733`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.1875`, primary_mae `0.038298`, avg `0.014924`, median `0.020913`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.073779`, avg `0.037998`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.016101`, avg `0.005845`, median `0.008122`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.021526`, avg `0.006639`, median `0.01079`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.031523`, avg `0.004703`, median `0.007973`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.032391`, avg `0.006552`, median `0.013099`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.055383`, avg `0.007825`, median `-0.002406`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.015214`, avg `-0.001166`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.01811`, avg `-0.002632`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.022581`, avg `0.001648`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.5125`, primary_mae `0.036203`, avg `0.007811`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.060959`, avg `0.008408`, median `0.003509`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.015214`, avg `-0.001166`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.01811`, avg `-0.002632`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.022581`, avg `0.001648`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.5125`, primary_mae `0.036203`, avg `0.007811`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.060959`, avg `0.008408`, median `0.003509`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.015214`, avg `-0.001166`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.01811`, avg `-0.002632`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.022581`, avg `0.001648`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.5125`, primary_mae `0.036203`, avg `0.007811`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.060959`, avg `0.008408`, median `0.003509`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.015214`, avg `-0.001166`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.01811`, avg `-0.002632`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.022581`, avg `0.001648`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.5125`, primary_mae `0.036203`, avg `0.007811`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.060959`, avg `0.008408`, median `0.003509`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.015214`, avg `-0.001166`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.01811`, avg `-0.002632`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.022581`, avg `0.001648`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.5125`, primary_mae `0.036203`, avg `0.007811`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.060959`, avg `0.008408`, median `0.003509`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.015214`, avg `-0.001166`, median `-0.001412`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.01811`, avg `-0.002632`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.022581`, avg `0.001648`, median `-0.000307`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.5125`, primary_mae `0.036203`, avg `0.007811`, median `0.01201`
- 60d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.060959`, avg `0.008408`, median `0.003509`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
