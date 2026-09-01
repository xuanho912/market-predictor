# Historical Replay Benchmark

Generated at: `2026-09-01T08:56:35.475059+00:00`
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
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.022053`
- secondary_mean_absolute_error: `0.016947`
- primary_error_advantage: `-0.005106`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.022025`
- secondary_mean_absolute_error: `0.020108`
- primary_error_advantage: `-0.001917`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.036401`
- secondary_mean_absolute_error: `0.030607`
- primary_error_advantage: `-0.005794`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.057562`
- secondary_mean_absolute_error: `0.045751`
- primary_error_advantage: `-0.011811`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.077838`
- secondary_mean_absolute_error: `0.071206`
- primary_error_advantage: `-0.006632`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.016468`, as_primary `0`, as_primary_hit `None`, avg `-0.001546`, median `0.000684`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.019391`, as_primary `0`, as_primary_hit `None`, avg `-0.002145`, median `-0.001116`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.027064`, as_primary `0`, as_primary_hit `None`, avg `0.000536`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.033135`, as_primary `0`, as_primary_hit `None`, avg `0.011436`, median `0.018503`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.058742`, as_primary `0`, as_primary_hit `None`, avg `0.036535`, median `0.051777`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.01685`, as_primary `20`, as_primary_hit `0.45`, avg `-0.001546`, median `0.000684`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.021725`, as_primary `20`, as_primary_hit `0.45`, avg `-0.002145`, median `-0.001116`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.037134`, as_primary `20`, as_primary_hit `0.3`, avg `0.000536`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.047939`, as_primary `20`, as_primary_hit `0.55`, avg `0.011436`, median `0.018503`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.072593`, as_primary `20`, as_primary_hit `0.6`, avg `0.036535`, median `0.051777`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.022523`, as_primary `60`, as_primary_hit `0.5333`, avg `-0.001546`, median `0.000684`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.022113`, as_primary `60`, as_primary_hit `0.5167`, avg `-0.002145`, median `-0.001116`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.034707`, as_primary `60`, as_primary_hit `0.45`, avg `0.000536`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.063378`, as_primary `60`, as_primary_hit `0.75`, avg `0.011436`, median `0.018503`
- 60d: sample `80`, direction_hit `0.2875`, path_mae `0.085617`, as_primary `60`, as_primary_hit `0.75`, avg `0.036535`, median `0.051777`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.016442`, as_primary `0`, as_primary_hit `None`, avg `-0.001546`, median `0.000684`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.01895`, as_primary `0`, as_primary_hit `None`, avg `-0.002145`, median `-0.001116`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.02489`, as_primary `0`, as_primary_hit `None`, avg `0.000536`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.03258`, as_primary `0`, as_primary_hit `None`, avg `0.011436`, median `0.018503`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.056413`, as_primary `0`, as_primary_hit `None`, avg `0.036535`, median `0.051777`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.022053`, avg `-0.001546`, median `0.000684`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.022025`, avg `-0.002145`, median `-0.001116`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.036401`, avg `0.000536`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.057562`, avg `0.011436`, median `0.018503`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.4375`, primary_mae `0.077838`, avg `0.036535`, median `0.051777`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.021104`, avg `-0.003102`, median `-0.000413`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.018865`, avg `-0.002555`, median `0.000618`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.034589`, avg `-0.004821`, median `-0.010651`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.052949`, avg `0.001386`, median `0.012703`
- 60d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.077035`, avg `0.00719`, median `0.007994`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.023002`, avg `1.1e-05`, median `0.001944`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.025186`, avg `-0.001736`, median `-0.005336`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.038214`, avg `0.005894`, median `-0.001577`
- 20d: sample `40`, primary_hit `0.225`, primary_closer `0.225`, primary_mae `0.062175`, avg `0.021485`, median `0.027848`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.07864`, avg `0.065879`, median `0.073489`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.021104, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.018865, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.034589, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.052949, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.077035, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016442, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022523, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.021104, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01895, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022113, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.018865, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02489, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037134, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.034589, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03258, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.063378, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.052949, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056413, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.085617, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.077035, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.018976`, avg `-0.001645`, median `0.001949`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.013039`, avg `-0.006459`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.030407`, avg `0.012529`, median `0.020076`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.052232`, avg `0.027693`, median `0.030181`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.09008`, avg `0.065639`, median `0.076071`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.020153`, avg `-0.002081`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.017223`, avg `-0.005947`, median `-0.006113`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.026551`, avg `0.006531`, median `0.003189`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.375`, primary_mae `0.05036`, avg `0.018039`, median `0.030181`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.088718`, avg `0.047`, median `0.073193`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.028795`, avg `0.00642`, median `0.011055`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.037105`, avg `0.010203`, median `0.018266`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.060119`, avg `0.015021`, median `0.027272`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.125`, primary_mae `0.073456`, avg `0.027029`, median `0.024365`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.4375`, primary_mae `0.066711`, avg `0.074818`, median `0.058973`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.022053`, avg `-0.001546`, median `0.000684`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.022025`, avg `-0.002145`, median `-0.001116`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.036401`, avg `0.000536`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.057562`, avg `0.011436`, median `0.018503`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.4375`, primary_mae `0.077838`, avg `0.036535`, median `0.051777`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.022053`, avg `-0.001546`, median `0.000684`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.022025`, avg `-0.002145`, median `-0.001116`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.036401`, avg `0.000536`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.057562`, avg `0.011436`, median `0.018503`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.4375`, primary_mae `0.077838`, avg `0.036535`, median `0.051777`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.6`, primary_mae `0.007462`, avg `-0.001977`, median `-0.001535`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.009688`, avg `-0.00521`, median `-0.004452`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.02862`, avg `-0.007779`, median `-0.012375`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.7`, primary_mae `0.045`, avg `-0.00938`, median `0.006712`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.062501`, avg `0.016874`, median `0.032753`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.023002`, avg `1.1e-05`, median `0.001944`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.025186`, avg `-0.001736`, median `-0.005336`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.038214`, avg `0.005894`, median `-0.001577`
- 20d: sample `40`, primary_hit `0.225`, primary_closer `0.225`, primary_mae `0.062175`, avg `0.021485`, median `0.027848`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.07864`, avg `0.065879`, median `0.073489`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.022053`, avg `-0.001546`, median `0.000684`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.022025`, avg `-0.002145`, median `-0.001116`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.036401`, avg `0.000536`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.057562`, avg `0.011436`, median `0.018503`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.4375`, primary_mae `0.077838`, avg `0.036535`, median `0.051777`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4375`, primary_mae `0.022053`, avg `-0.001546`, median `0.000684`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.022025`, avg `-0.002145`, median `-0.001116`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.036401`, avg `0.000536`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.057562`, avg `0.011436`, median `0.018503`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.4375`, primary_mae `0.077838`, avg `0.036535`, median `0.051777`

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
