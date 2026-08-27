# Historical Replay Benchmark

Generated at: `2026-08-27T04:31:19.013897+00:00`
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
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.016116`
- secondary_mean_absolute_error: `0.014513`
- primary_error_advantage: `-0.001603`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.023121`
- secondary_mean_absolute_error: `0.019773`
- primary_error_advantage: `-0.003348`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.041435`
- secondary_mean_absolute_error: `0.032038`
- primary_error_advantage: `-0.009397`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.076556`
- secondary_mean_absolute_error: `0.046385`
- primary_error_advantage: `-0.030171`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.275`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.074543`
- secondary_mean_absolute_error: `0.060026`
- primary_error_advantage: `-0.014517`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4`

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
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.01616`, as_primary `20`, as_primary_hit `0.5`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.022693`, as_primary `20`, as_primary_hit `0.45`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.03736`, as_primary `20`, as_primary_hit `0.65`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.061852`, as_primary `20`, as_primary_hit `0.75`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.069519`, as_primary `20`, as_primary_hit `0.65`, avg `0.032804`, median `0.033835`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.016399`, as_primary `60`, as_primary_hit `0.6167`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.022279`, as_primary `60`, as_primary_hit `0.5333`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.041164`, as_primary `60`, as_primary_hit `0.4833`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.080481`, as_primary `60`, as_primary_hit `0.6`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, direction_hit `0.3125`, path_mae `0.081869`, as_primary `60`, as_primary_hit `0.7`, avg `0.032804`, median `0.033835`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.01433`, as_primary `0`, as_primary_hit `None`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.019023`, as_primary `0`, as_primary_hit `None`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.026866`, as_primary `0`, as_primary_hit `None`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.040885`, as_primary `0`, as_primary_hit `None`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.057021`, as_primary `0`, as_primary_hit `None`, avg `0.032804`, median `0.033835`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.4`, primary_mae `0.016601`, avg `0.002297`, median `0.002198`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.4`, primary_mae `0.023889`, avg `-0.000468`, median `-0.002992`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.040572`, avg `0.006299`, median `0.008315`
- 20d: sample `60`, primary_hit `0.5333`, primary_closer `0.2667`, primary_mae `0.071797`, avg `0.009621`, median `0.018168`
- 60d: sample `60`, primary_hit `0.4`, primary_closer `0.4167`, primary_mae `0.074057`, avg `0.040136`, median `0.04041`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.014661`, avg `0.002759`, median `0.003489`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.020816`, avg `0.002148`, median `0.004262`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.044025`, avg `-0.0051`, median `-0.010677`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.090831`, avg `-0.001974`, median `0.015944`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.075999`, avg `0.010806`, median `0.009053`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.012061`, avg `0.002064`, median `0.002957`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.01781`, avg `-0.00154`, median `0.000781`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.575`, primary_mae `0.0351`, avg `-0.005776`, median `-0.010677`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.3`, primary_mae `0.082271`, avg `-0.007563`, median `0.011844`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.078281`, avg `0.0103`, median `0.009053`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.020171`, avg `0.002762`, median `0.002335`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.028431`, avg `0.001912`, median `-0.002992`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.047771`, avg `0.012675`, median `0.015859`
- 20d: sample `40`, primary_hit `0.55`, primary_closer `0.25`, primary_mae `0.07084`, avg `0.021007`, median `0.025986`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.070804`, avg `0.055308`, median `0.059662`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.012061, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.01781, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.0351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.07084, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.070804, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01433, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016399, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.012061, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019023, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022693, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.01781, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026866, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041164, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.0351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040885, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.080481, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.07084, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057021, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.081869, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.070804, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

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
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.013353`, avg `-0.000602`, median `0.001086`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.019139`, avg `-0.001679`, median `0.000458`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.038083`, avg `-0.01343`, median `-0.012201`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.083645`, avg `-0.012707`, median `0.013942`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.072568`, avg `0.005319`, median `0.007994`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.016116`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.023121`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.041435`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.275`, primary_mae `0.076556`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.074543`, avg `0.032804`, median `0.033835`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.016116`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.023121`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.041435`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.275`, primary_mae `0.076556`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.074543`, avg `0.032804`, median `0.033835`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.012761`, avg `-0.00141`, median `0.001107`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.017568`, avg `-0.004956`, median `-0.005726`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.55`, primary_mae `0.02417`, avg `0.001439`, median `0.003674`
- 20d: sample `40`, primary_hit `0.625`, primary_closer `0.3`, primary_mae `0.054314`, avg `0.00318`, median `0.018168`
- 60d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.073017`, avg `0.018678`, median `0.031374`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.016871`, avg `0.00554`, median `0.004986`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.025668`, avg `0.00164`, median `-0.000209`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.049776`, avg `0.004784`, median `-0.00228`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.25`, primary_mae `0.090238`, avg `0.004676`, median `0.009671`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.425`, primary_mae `0.078351`, avg `0.046424`, median `0.058727`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.016116`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.023121`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.041435`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.275`, primary_mae `0.076556`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.074543`, avg `0.032804`, median `0.033835`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.016116`, avg `0.002413`, median `0.002615`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.023121`, avg `0.000186`, median `0.000497`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.041435`, avg `0.003449`, median `0.004547`
- 20d: sample `80`, primary_hit `0.4875`, primary_closer `0.275`, primary_mae `0.076556`, avg `0.006722`, median `0.016995`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.074543`, avg `0.032804`, median `0.033835`

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
