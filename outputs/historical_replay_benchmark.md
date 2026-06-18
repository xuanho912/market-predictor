# Historical Replay Benchmark

Generated at: `2026-06-18T00:01:55.223435+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `STRONG_HISTORICAL_ONLY`
Overfit warning: `{'level': 'medium', 'reasons': ['forward validation completed samples are below the minimum gate'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_supportive_but_not_forward_validated`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.015861`
- secondary_mean_absolute_error: `0.016157`
- primary_error_advantage: `0.000296`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.019892`
- secondary_mean_absolute_error: `0.021229`
- primary_error_advantage: `0.001337`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.026205`
- secondary_mean_absolute_error: `0.028559`
- primary_error_advantage: `0.002354`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6167`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.6`
- primary_mean_absolute_error: `0.043859`
- secondary_mean_absolute_error: `0.047625`
- primary_error_advantage: `0.003766`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6833`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.073449`
- secondary_mean_absolute_error: `0.059233`
- primary_error_advantage: `-0.014216`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.0147`, as_primary `0`, as_primary_hit `None`, avg `0.001033`, median `0.001005`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.019327`, as_primary `0`, as_primary_hit `None`, avg `-0.000965`, median `-8.2e-05`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.024062`, as_primary `0`, as_primary_hit `None`, avg `0.002485`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.775`, path_mae `0.025572`, as_primary `0`, as_primary_hit `None`, avg `0.015948`, median `0.020805`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.050061`, as_primary `0`, as_primary_hit `None`, avg `0.036343`, median `0.054644`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.015798`, as_primary `40`, as_primary_hit `0.5`, avg `0.001033`, median `0.001005`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.02051`, as_primary `40`, as_primary_hit `0.525`, avg `-0.000965`, median `-8.2e-05`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.02759`, as_primary `40`, as_primary_hit `0.45`, avg `0.002485`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.775`, path_mae `0.038608`, as_primary `40`, as_primary_hit `0.75`, avg `0.015948`, median `0.020805`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.063449`, as_primary `40`, as_primary_hit `0.6`, avg `0.036343`, median `0.054644`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.016221`, as_primary `40`, as_primary_hit `0.525`, avg `0.001033`, median `0.001005`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.02061`, as_primary `40`, as_primary_hit `0.475`, avg `-0.000965`, median `-8.2e-05`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.027174`, as_primary `40`, as_primary_hit `0.5`, avg `0.002485`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.225`, path_mae `0.052876`, as_primary `40`, as_primary_hit `0.8`, avg `0.015948`, median `0.020805`
- 60d: sample `80`, direction_hit `0.3125`, path_mae `0.069233`, as_primary `40`, as_primary_hit `0.775`, avg `0.036343`, median `0.054644`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.014379`, as_primary `0`, as_primary_hit `None`, avg `0.001033`, median `0.001005`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.01855`, as_primary `0`, as_primary_hit `None`, avg `-0.000965`, median `-8.2e-05`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.021964`, as_primary `0`, as_primary_hit `None`, avg `0.002485`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.775`, path_mae `0.025134`, as_primary `0`, as_primary_hit `None`, avg `0.015948`, median `0.020805`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.049029`, as_primary `0`, as_primary_hit `None`, avg `0.036343`, median `0.054644`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.525`, primary_mae `0.015861`, avg `0.001033`, median `0.001005`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.019892`, avg `-0.000965`, median `-8.2e-05`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.575`, primary_mae `0.026205`, avg `0.002485`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.6`, primary_mae `0.043859`, avg `0.015948`, median `0.020805`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.073449`, avg `0.036343`, median `0.054644`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.65`, primary_mae `0.008134`, avg `-0.002801`, median `-0.003287`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.01266`, avg `-0.003981`, median `0.000449`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.75`, primary_mae `0.017116`, avg `-0.004634`, median `-0.003046`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.03134`, avg `6e-06`, median `0.01201`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.054715`, avg `-0.00993`, median `-0.011316`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.4833`, primary_mae `0.018437`, avg `0.002311`, median `0.001762`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.5167`, primary_mae `0.022302`, avg `4e-05`, median `-8.2e-05`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.5167`, primary_mae `0.029235`, avg `0.004858`, median `-0.001153`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.5667`, primary_mae `0.048033`, avg `0.021262`, median `0.028445`
- 60d: sample `60`, primary_hit `0.4167`, primary_closer `0.4167`, primary_mae `0.079693`, avg `0.051768`, median `0.070539`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.008134, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.01266, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.017116, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.03134, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.054715, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014379, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016221, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.008134, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01855, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02061, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.01266, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021964, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02759, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.017116, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.6, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025134, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052876, 'direction_hit_rate': 0.225}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.03134, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049029, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069233, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.054715, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.012027`, avg `0.007885`, median `0.00694`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.014097`, avg `-0.000723`, median `-0.001187`
- 10d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.051038`, avg `-0.006283`, median `-0.011`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.06259`, avg `0.002386`, median `0.01035`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.100479`, avg `0.030679`, median `0.030229`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.013616`, avg `0.005302`, median `0.002888`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.014968`, avg `0.004347`, median `0.001122`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.03608`, avg `0.007222`, median `-0.004104`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.049088`, avg `0.013154`, median `0.018729`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.5`, primary_mae `0.070016`, avg `0.062194`, median `0.078963`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.019894`, avg `-0.001595`, median `-0.010199`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.027926`, avg `-0.00276`, median `-0.006055`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.036617`, avg `0.001175`, median `0.000351`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.079151`, avg `0.018407`, median `0.033135`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.126129`, avg `0.032746`, median `0.059044`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.525`, primary_mae `0.015861`, avg `0.001033`, median `0.001005`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.019892`, avg `-0.000965`, median `-8.2e-05`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.575`, primary_mae `0.026205`, avg `0.002485`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.6`, primary_mae `0.043859`, avg `0.015948`, median `0.020805`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.073449`, avg `0.036343`, median `0.054644`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.525`, primary_mae `0.015861`, avg `0.001033`, median `0.001005`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.019892`, avg `-0.000965`, median `-8.2e-05`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.575`, primary_mae `0.026205`, avg `0.002485`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.6`, primary_mae `0.043859`, avg `0.015948`, median `0.020805`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.073449`, avg `0.036343`, median `0.054644`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.011344`, avg `0.000441`, median `0.000267`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.55`, primary_mae `0.014978`, avg `-0.000337`, median `0.002655`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.575`, primary_mae `0.027222`, avg `0.000112`, median `-0.00384`
- 20d: sample `40`, primary_hit `0.75`, primary_closer `0.725`, primary_mae `0.037944`, avg `0.009282`, median `0.017205`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.06334`, avg `0.027421`, median `0.038031`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.525`, primary_mae `0.020378`, avg `0.001625`, median `0.001005`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.024806`, avg `-0.001594`, median `-0.005063`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.025189`, avg `0.004859`, median `0.000351`
- 20d: sample `40`, primary_hit `0.2`, primary_closer `0.475`, primary_mae `0.049775`, avg `0.022614`, median `0.028709`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.4`, primary_mae `0.083557`, avg `0.045265`, median `0.067799`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.525`, primary_mae `0.015861`, avg `0.001033`, median `0.001005`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.019892`, avg `-0.000965`, median `-8.2e-05`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.575`, primary_mae `0.026205`, avg `0.002485`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.6`, primary_mae `0.043859`, avg `0.015948`, median `0.020805`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.073449`, avg `0.036343`, median `0.054644`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.525`, primary_mae `0.015861`, avg `0.001033`, median `0.001005`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.019892`, avg `-0.000965`, median `-8.2e-05`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.575`, primary_mae `0.026205`, avg `0.002485`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.6`, primary_mae `0.043859`, avg `0.015948`, median `0.020805`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.073449`, avg `0.036343`, median `0.054644`

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
