# Historical Replay Benchmark

Generated at: `2026-08-27T11:16:43.064571+00:00`
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
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.01616`
- secondary_mean_absolute_error: `0.014882`
- primary_error_advantage: `-0.001278`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.022693`
- secondary_mean_absolute_error: `0.020777`
- primary_error_advantage: `-0.001916`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.03736`
- secondary_mean_absolute_error: `0.032851`
- primary_error_advantage: `-0.004509`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.061852`
- secondary_mean_absolute_error: `0.061936`
- primary_error_advantage: `8.4e-05`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.069519`
- secondary_mean_absolute_error: `0.067811`
- primary_error_advantage: `-0.001708`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014381`, as_primary `0`, as_primary_hit `None`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.019402`, as_primary `0`, as_primary_hit `None`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.027276`, as_primary `0`, as_primary_hit `None`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.04264`, as_primary `0`, as_primary_hit `None`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.058565`, as_primary `0`, as_primary_hit `None`, avg `0.032804`, median `0.033835`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.01616`, as_primary `80`, as_primary_hit `0.5875`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.022693`, as_primary `80`, as_primary_hit `0.5125`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.03736`, as_primary `80`, as_primary_hit `0.525`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.061852`, as_primary `80`, as_primary_hit `0.6375`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.069519`, as_primary `80`, as_primary_hit `0.6875`, avg `0.032804`, median `0.033835`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.016399`, as_primary `0`, as_primary_hit `None`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.022279`, as_primary `0`, as_primary_hit `None`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.041164`, as_primary `0`, as_primary_hit `None`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.080481`, as_primary `0`, as_primary_hit `None`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, direction_hit `0.3125`, path_mae `0.081869`, as_primary `0`, as_primary_hit `None`, avg `0.032804`, median `0.033835`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.01433`, as_primary `0`, as_primary_hit `None`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.019023`, as_primary `0`, as_primary_hit `None`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.026866`, as_primary `0`, as_primary_hit `None`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.040885`, as_primary `0`, as_primary_hit `None`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.057021`, as_primary `0`, as_primary_hit `None`, avg `0.032804`, median `0.033835`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.5`, primary_mae `0.01616`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.022693`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.03736`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.475`, primary_mae `0.061852`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.475`, primary_mae `0.069519`, avg `0.032804`, median `0.033835`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.5333`, primary_mae `0.016193`, avg `0.004613`, median `0.004172`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.5333`, primary_mae `0.023481`, avg `0.00181`, median `0.000781`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.4`, primary_mae `0.042426`, avg `0.001489`, median `-0.007304`
- 20d: sample `60`, primary_hit `0.6`, primary_closer `0.5333`, primary_mae `0.070831`, avg `0.002459`, median `0.013238`
- 60d: sample `60`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.070869`, avg `0.034551`, median `0.035382`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.016061`, avg `-0.004188`, median `-0.000182`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.020332`, avg `-0.004685`, median `-0.006106`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.022165`, avg `0.00933`, median `0.015859`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.034916`, avg `0.019512`, median `0.030181`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.06547`, avg `0.027561`, median `0.033759`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016061, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.020332, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.022165, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.034916, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.06547, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01433, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016399, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016061, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019023, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022693, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.020332, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026866, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041164, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.022165, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040885, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.080481, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.034916, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057021, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.081869, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.06547, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.011395`, avg `-0.00267`, median `0.001949`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.021421`, avg `-0.005701`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.017367`, avg `0.010786`, median `0.020076`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.0`, primary_mae `0.032556`, avg `0.019767`, median `0.027848`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.046103`, avg `0.04575`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.013551`, avg `-0.000646`, median `0.001949`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.020484`, avg `-0.003637`, median `-0.006388`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.021705`, avg `0.010849`, median `0.020076`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.032827`, avg `0.022127`, median `0.030181`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.055399`, avg `0.04128`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.013551`, avg `-0.000646`, median `0.001949`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.020484`, avg `-0.003637`, median `-0.006388`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.021705`, avg `0.010849`, median `0.020076`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.032827`, avg `0.022127`, median `0.030181`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.055399`, avg `0.04128`, median `0.052814`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.5`, primary_mae `0.01616`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.022693`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.03736`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.475`, primary_mae `0.061852`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.475`, primary_mae `0.069519`, avg `0.032804`, median `0.033835`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.5`, primary_mae `0.01616`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.022693`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.03736`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.475`, primary_mae `0.061852`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.475`, primary_mae `0.069519`, avg `0.032804`, median `0.033835`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.012451`, avg `-0.00141`, median `0.001107`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.525`, primary_mae `0.015835`, avg `-0.004956`, median `-0.005726`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.024837`, avg `0.001439`, median `0.003674`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.041843`, avg `0.00318`, median `0.018168`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.067031`, avg `0.018678`, median `0.031374`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017388`, avg `0.00554`, median `0.004986`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.025089`, avg `0.00164`, median `-0.000209`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.04392`, avg `0.004784`, median `-0.00228`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.079464`, avg `0.004676`, median `0.009671`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.425`, primary_mae `0.077888`, avg `0.046424`, median `0.058727`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.5`, primary_mae `0.01616`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.022693`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.03736`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.475`, primary_mae `0.061852`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.475`, primary_mae `0.069519`, avg `0.032804`, median `0.033835`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.5`, primary_mae `0.01616`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.022693`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.03736`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.475`, primary_mae `0.061852`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.475`, primary_mae `0.069519`, avg `0.032804`, median `0.033835`

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
