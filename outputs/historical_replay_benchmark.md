# Historical Replay Benchmark

Generated at: `2026-08-25T04:24:09.794744+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.016813`
- secondary_mean_absolute_error: `0.017905`
- primary_error_advantage: `0.001092`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5125`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.019542`
- secondary_mean_absolute_error: `0.020615`
- primary_error_advantage: `0.001073`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.028611`
- secondary_mean_absolute_error: `0.029713`
- primary_error_advantage: `0.001102`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.051662`
- secondary_mean_absolute_error: `0.044157`
- primary_error_advantage: `-0.007505`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.061004`
- secondary_mean_absolute_error: `0.064222`
- primary_error_advantage: `0.003218`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014825`, as_primary `0`, as_primary_hit `None`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017533`, as_primary `0`, as_primary_hit `None`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.022623`, as_primary `0`, as_primary_hit `None`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.031125`, as_primary `0`, as_primary_hit `None`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.051792`, as_primary `0`, as_primary_hit `None`, avg `0.02577`, median `0.033835`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.015513`, as_primary `20`, as_primary_hit `0.55`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.019654`, as_primary `20`, as_primary_hit `0.55`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.032692`, as_primary `20`, as_primary_hit `0.5`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.043349`, as_primary `20`, as_primary_hit `0.75`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.061504`, as_primary `20`, as_primary_hit `0.7`, avg `0.02577`, median `0.033835`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.019421`, as_primary `60`, as_primary_hit `0.5167`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.020957`, as_primary `60`, as_primary_hit `0.5667`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.028111`, as_primary `60`, as_primary_hit `0.4833`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.05608`, as_primary `60`, as_primary_hit `0.5833`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, direction_hit `0.3375`, path_mae `0.070203`, as_primary `60`, as_primary_hit `0.65`, avg `0.02577`, median `0.033835`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014665`, as_primary `0`, as_primary_hit `None`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017294`, as_primary `0`, as_primary_hit `None`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.021523`, as_primary `0`, as_primary_hit `None`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.031533`, as_primary `0`, as_primary_hit `None`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.049054`, as_primary `0`, as_primary_hit `None`, avg `0.02577`, median `0.033835`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.016813`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.019542`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.028611`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.051662`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.061004`, avg `0.02577`, median `0.033835`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.017491`, avg `0.002039`, median `0.002264`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.020441`, avg `0.006481`, median `0.005727`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.033498`, avg `0.009127`, median `0.01332`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.069818`, avg `0.004618`, median `0.016578`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.072129`, avg `-0.005603`, median `0.009053`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.01457`, avg `-0.001757`, median `-0.000614`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.013241`, avg `-0.003146`, median `0.000725`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.024375`, avg `-0.011711`, median `-0.013778`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.066453`, avg `-0.020159`, median `-0.005516`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.070277`, avg `-0.006555`, median `-0.017876`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.575`, primary_mae `0.017595`, avg `0.000191`, median `0.001949`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.55`, primary_mae `0.022242`, avg `-2.6e-05`, median `0.000311`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.028287`, avg `0.007503`, median `0.006375`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.525`, primary_mae `0.035189`, avg `0.021023`, median `0.029731`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.575`, primary_mae `0.050804`, avg `0.057618`, median `0.062955`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.01457, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013241, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.024375, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.035189, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.050804, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014665, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019421, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.01457, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017294, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020957, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013241, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021523, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032692, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.024375, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031125, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05608, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.035189, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049054, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070203, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.050804, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016392`, avg `-0.006252`, median `0.001949`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.025237`, avg `-0.011032`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.024765`, avg `0.005548`, median `0.013417`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.036375`, avg `0.016823`, median `0.027848`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.051645`, avg `0.046649`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.625`, primary_mae `0.018391`, avg `-0.002855`, median `0.001949`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.025144`, avg `-0.00797`, median `-0.006374`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.02432`, avg `0.007828`, median `0.009998`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.75`, primary_mae `0.033535`, avg `0.021419`, median `0.029731`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.05011`, avg `0.044031`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.020784`, avg `0.006485`, median `0.010157`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.02608`, avg `0.00678`, median `0.004904`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.032603`, avg `0.012422`, median `0.017251`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.035388`, avg `0.026432`, median `0.028152`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.4375`, primary_mae `0.045225`, avg `0.081965`, median `0.071545`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.016813`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.019542`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.028611`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.051662`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.061004`, avg `0.02577`, median `0.033835`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.016813`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.019542`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.028611`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.051662`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.061004`, avg `0.02577`, median `0.033835`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.015767`, avg `-0.002336`, median `0.000402`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.017612`, avg `-0.004611`, median `0.000633`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.575`, primary_mae `0.025239`, avg `-0.003159`, median `-0.007623`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.525`, primary_mae `0.051744`, avg `-0.001384`, median `0.009981`
- 60d: sample `40`, primary_hit `0.675`, primary_closer `0.625`, primary_mae `0.065154`, avg `0.013564`, median `0.020962`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.016398`, avg `0.00077`, median `-0.000614`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.017871`, avg `0.001439`, median `0.000725`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.027423`, avg `-0.001048`, median `-0.007304`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.049898`, avg `0.002248`, median `0.004976`
- 60d: sample `40`, primary_hit `0.325`, primary_closer `0.5`, primary_mae `0.055928`, avg `0.037499`, median `0.053572`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.016813`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.019542`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.028611`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.051662`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.061004`, avg `0.02577`, median `0.033835`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.016813`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.019542`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.028611`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.051662`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.061004`, avg `0.02577`, median `0.033835`

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
