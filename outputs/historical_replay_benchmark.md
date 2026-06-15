# Historical Replay Benchmark

Generated at: `2026-06-15T08:04:27.911863+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'high', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay', 'forward validation completed samples are below the minimum gate'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.014491`
- secondary_mean_absolute_error: `0.012671`
- primary_error_advantage: `-0.00182`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.3375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.016428`
- secondary_mean_absolute_error: `0.015135`
- primary_error_advantage: `-0.001293`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.023769`
- secondary_mean_absolute_error: `0.020715`
- primary_error_advantage: `-0.003054`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.04243`
- secondary_mean_absolute_error: `0.047327`
- primary_error_advantage: `0.004897`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.058157`
- secondary_mean_absolute_error: `0.054048`
- primary_error_advantage: `-0.004109`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.013053`, as_primary `0`, as_primary_hit `None`, avg `0.001175`, median `0.001005`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.015`, as_primary `0`, as_primary_hit `None`, avg `0.000734`, median `0.00281`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.01861`, as_primary `0`, as_primary_hit `None`, avg `0.001104`, median `-0.000811`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.027516`, as_primary `0`, as_primary_hit `None`, avg `0.002376`, median `0.006827`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.048409`, as_primary `0`, as_primary_hit `None`, avg `0.00681`, median `-0.003092`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014491`, as_primary `80`, as_primary_hit `0.525`, avg `0.001175`, median `0.001005`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.016428`, as_primary `80`, as_primary_hit `0.5875`, avg `0.000734`, median `0.00281`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.023769`, as_primary `80`, as_primary_hit `0.4875`, avg `0.001104`, median `-0.000811`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.04243`, as_primary `80`, as_primary_hit `0.5875`, avg `0.002376`, median `0.006827`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.058157`, as_primary `80`, as_primary_hit `0.475`, avg `0.00681`, median `-0.003092`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.012682`, as_primary `0`, as_primary_hit `None`, avg `0.001175`, median `0.001005`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.015203`, as_primary `0`, as_primary_hit `None`, avg `0.000734`, median `0.00281`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.021786`, as_primary `0`, as_primary_hit `None`, avg `0.001104`, median `-0.000811`
- 20d: sample `80`, direction_hit `0.4125`, path_mae `0.053281`, as_primary `0`, as_primary_hit `None`, avg `0.002376`, median `0.006827`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.063079`, as_primary `0`, as_primary_hit `None`, avg `0.00681`, median `-0.003092`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.012706`, as_primary `0`, as_primary_hit `None`, avg `0.001175`, median `0.001005`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.014371`, as_primary `0`, as_primary_hit `None`, avg `0.000734`, median `0.00281`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.018042`, as_primary `0`, as_primary_hit `None`, avg `0.001104`, median `-0.000811`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.027269`, as_primary `0`, as_primary_hit `None`, avg `0.002376`, median `0.006827`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.046728`, as_primary `0`, as_primary_hit `None`, avg `0.00681`, median `-0.003092`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.014491`, avg `0.001175`, median `0.001005`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4625`, primary_mae `0.016428`, avg `0.000734`, median `0.00281`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.023769`, avg `0.001104`, median `-0.000811`
- 20d: sample `80`, primary_hit `0.5875`, primary_closer `0.525`, primary_mae `0.04243`, avg `0.002376`, median `0.006827`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.058157`, avg `0.00681`, median `-0.003092`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.45`, primary_mae `0.014915`, avg `0.003798`, median `0.003108`
- 5d: sample `60`, primary_hit `0.6667`, primary_closer `0.45`, primary_mae `0.017532`, avg `0.004306`, median `0.005205`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.4667`, primary_mae `0.027226`, avg `0.001756`, median `0.001014`
- 20d: sample `60`, primary_hit `0.5167`, primary_closer `0.6`, primary_mae `0.046468`, avg `-0.003502`, median `0.002085`
- 60d: sample `60`, primary_hit `0.3833`, primary_closer `0.4833`, primary_mae `0.059011`, avg `-0.005213`, median `-0.012487`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.013221`, avg `-0.006693`, median `-0.009739`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.013115`, avg `-0.009981`, median `-0.007293`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.013396`, avg `-0.00085`, median `-0.001577`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.030315`, avg `0.020009`, median `0.028979`
- 60d: sample `20`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.055596`, avg `0.042877`, median `0.062395`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.013221, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.013115, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.013396, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.030315, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.055596, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012682, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014491, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.013221, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.3375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014371, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016428, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.013115, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018042, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023769, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.013396, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027269, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053281, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.030315, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.046728, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.063079, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.055596, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.010983`, avg `-0.008716`, median `-0.009739`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.012932`, avg `-0.00719`, median `-0.008697`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.016856`, avg `-0.001836`, median `-0.008733`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.0`, primary_mae `0.045659`, avg `0.003391`, median `0.016513`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.098052`, avg `-0.006235`, median `-0.004019`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.014253`, avg `-0.005211`, median `-0.005597`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.012977`, avg `-0.010099`, median `-0.010372`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.013334`, avg `-0.001201`, median `-0.001577`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.03022`, avg `0.019998`, median `0.028979`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.055269`, avg `0.043523`, median `0.073193`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.014253`, avg `-0.005211`, median `-0.005597`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.012977`, avg `-0.010099`, median `-0.010372`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.013334`, avg `-0.001201`, median `-0.001577`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.03022`, avg `0.019998`, median `0.028979`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.055269`, avg `0.043523`, median `0.073193`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.014491`, avg `0.001175`, median `0.001005`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4625`, primary_mae `0.016428`, avg `0.000734`, median `0.00281`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.023769`, avg `0.001104`, median `-0.000811`
- 20d: sample `80`, primary_hit `0.5875`, primary_closer `0.525`, primary_mae `0.04243`, avg `0.002376`, median `0.006827`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.058157`, avg `0.00681`, median `-0.003092`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.014491`, avg `0.001175`, median `0.001005`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4625`, primary_mae `0.016428`, avg `0.000734`, median `0.00281`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.023769`, avg `0.001104`, median `-0.000811`
- 20d: sample `80`, primary_hit `0.5875`, primary_closer `0.525`, primary_mae `0.04243`, avg `0.002376`, median `0.006827`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.058157`, avg `0.00681`, median `-0.003092`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.014491`, avg `0.001175`, median `0.001005`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4625`, primary_mae `0.016428`, avg `0.000734`, median `0.00281`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.023769`, avg `0.001104`, median `-0.000811`
- 20d: sample `80`, primary_hit `0.5875`, primary_closer `0.525`, primary_mae `0.04243`, avg `0.002376`, median `0.006827`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.058157`, avg `0.00681`, median `-0.003092`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.014491`, avg `0.001175`, median `0.001005`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4625`, primary_mae `0.016428`, avg `0.000734`, median `0.00281`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.023769`, avg `0.001104`, median `-0.000811`
- 20d: sample `80`, primary_hit `0.5875`, primary_closer `0.525`, primary_mae `0.04243`, avg `0.002376`, median `0.006827`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.058157`, avg `0.00681`, median `-0.003092`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.014491`, avg `0.001175`, median `0.001005`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.4625`, primary_mae `0.016428`, avg `0.000734`, median `0.00281`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.023769`, avg `0.001104`, median `-0.000811`
- 20d: sample `80`, primary_hit `0.5875`, primary_closer `0.525`, primary_mae `0.04243`, avg `0.002376`, median `0.006827`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.058157`, avg `0.00681`, median `-0.003092`

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
