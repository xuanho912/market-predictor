# Historical Replay Benchmark

Generated at: `2026-09-09T06:02:53.632437+00:00`
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
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.020583`
- secondary_mean_absolute_error: `0.013596`
- primary_error_advantage: `-0.006987`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3167`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.01999`
- secondary_mean_absolute_error: `0.016933`
- primary_error_advantage: `-0.003057`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.030739`
- secondary_mean_absolute_error: `0.030042`
- primary_error_advantage: `-0.000697`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.054727`
- secondary_mean_absolute_error: `0.041188`
- primary_error_advantage: `-0.013539`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.25`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.5`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.084006`
- secondary_mean_absolute_error: `0.06259`
- primary_error_advantage: `-0.021416`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.014358`, as_primary `0`, as_primary_hit `None`, avg `-0.000452`, median `0.000609`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017037`, as_primary `0`, as_primary_hit `None`, avg `0.000652`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.025765`, as_primary `0`, as_primary_hit `None`, avg `0.001371`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.034391`, as_primary `0`, as_primary_hit `None`, avg `0.011166`, median `0.017664`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.059514`, as_primary `0`, as_primary_hit `None`, avg `0.041163`, median `0.058112`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.014151`, as_primary `0`, as_primary_hit `None`, avg `-0.000452`, median `0.000609`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.018357`, as_primary `0`, as_primary_hit `None`, avg `0.000652`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.035267`, as_primary `0`, as_primary_hit `None`, avg `0.001371`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.048398`, as_primary `0`, as_primary_hit `None`, avg `0.011166`, median `0.017664`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.071469`, as_primary `0`, as_primary_hit `None`, avg `0.041163`, median `0.058112`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.020583`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.000452`, median `0.000609`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.01999`, as_primary `80`, as_primary_hit `0.5625`, avg `0.000652`, median `0.001271`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.030739`, as_primary `80`, as_primary_hit `0.4125`, avg `0.001371`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.054727`, as_primary `80`, as_primary_hit `0.675`, avg `0.011166`, median `0.017664`
- 60d: sample `80`, direction_hit `0.25`, path_mae `0.084006`, as_primary `80`, as_primary_hit `0.75`, avg `0.041163`, median `0.058112`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.013625`, as_primary `0`, as_primary_hit `None`, avg `-0.000452`, median `0.000609`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.016828`, as_primary `0`, as_primary_hit `None`, avg `0.000652`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.023329`, as_primary `0`, as_primary_hit `None`, avg `0.001371`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.032251`, as_primary `0`, as_primary_hit `None`, avg `0.011166`, median `0.017664`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.05661`, as_primary `0`, as_primary_hit `None`, avg `0.041163`, median `0.058112`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.325`, primary_mae `0.020583`, avg `-0.000452`, median `0.000609`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.01999`, avg `0.000652`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.55`, primary_mae `0.030739`, avg `0.001371`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.054727`, avg `0.011166`, median `0.017664`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.084006`, avg `0.041163`, median `0.058112`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.010077`, avg `-0.003443`, median `-0.005951`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.010531`, avg `-0.003933`, median `-0.000876`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.021771`, avg `-0.009551`, median `-0.013311`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.065397`, avg `-0.015866`, median `-0.005516`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.083176`, avg `0.011287`, median `0.013899`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.2667`, primary_mae `0.024085`, avg `0.000545`, median `0.002077`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.4`, primary_mae `0.023143`, avg `0.00218`, median `0.00416`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4833`, primary_mae `0.033728`, avg `0.005011`, median `-0.002174`
- 20d: sample `60`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.05117`, avg `0.020177`, median `0.025986`
- 60d: sample `60`, primary_hit `0.1667`, primary_closer `0.3667`, primary_mae `0.084283`, avg `0.051121`, median `0.0618`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.010077, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.010531, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.021771, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.05117, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.083176, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013625, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020583, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.010077, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016828, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01999, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.010531, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023329, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035267, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.021771, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032251, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054727, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.05117, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.5, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05661, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.084006, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.083176, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.021775`, avg `-0.002268`, median `-0.001578`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.021968`, avg `0.010126`, median `0.009925`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.032101`, avg `-0.001276`, median `-0.015286`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.060303`, avg `0.005107`, median `0.004833`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.114268`, avg `0.044291`, median `0.077806`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.125`, primary_mae `0.027634`, avg `0.00365`, median `0.003155`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.023239`, avg `0.011459`, median `0.01094`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.039815`, avg `0.007186`, median `0.006501`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.063602`, avg `0.014334`, median `0.010724`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.4375`, primary_mae `0.100728`, avg `0.039442`, median `0.04886`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.029656`, avg `0.006678`, median `0.009495`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.031225`, avg `0.007698`, median `0.009408`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.040663`, avg `0.012322`, median `-0.000867`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.042116`, avg `0.033978`, median `0.027235`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.4375`, primary_mae `0.055991`, avg `0.072489`, median `0.066772`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.325`, primary_mae `0.020583`, avg `-0.000452`, median `0.000609`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.01999`, avg `0.000652`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.55`, primary_mae `0.030739`, avg `0.001371`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.054727`, avg `0.011166`, median `0.017664`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.084006`, avg `0.041163`, median `0.058112`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.325`, primary_mae `0.020583`, avg `-0.000452`, median `0.000609`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.01999`, avg `0.000652`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.55`, primary_mae `0.030739`, avg `0.001371`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.054727`, avg `0.011166`, median `0.017664`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.084006`, avg `0.041163`, median `0.058112`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.010077`, avg `-0.003443`, median `-0.005951`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.010531`, avg `-0.003933`, median `-0.000876`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.021771`, avg `-0.009551`, median `-0.013311`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.065397`, avg `-0.015866`, median `-0.005516`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.083176`, avg `0.011287`, median `0.013899`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.325`, primary_mae `0.022101`, avg `0.000205`, median `0.001944`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.02228`, avg `-0.001485`, median `0.000311`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.030656`, avg `0.004884`, median `-0.004843`
- 20d: sample `40`, primary_hit `0.175`, primary_closer `0.275`, primary_mae `0.047943`, avg `0.025495`, median `0.029097`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.35`, primary_mae `0.075962`, avg `0.059442`, median `0.066423`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.325`, primary_mae `0.020583`, avg `-0.000452`, median `0.000609`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.01999`, avg `0.000652`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.55`, primary_mae `0.030739`, avg `0.001371`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.054727`, avg `0.011166`, median `0.017664`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.084006`, avg `0.041163`, median `0.058112`

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
