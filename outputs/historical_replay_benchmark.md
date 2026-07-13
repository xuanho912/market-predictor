# Historical Replay Benchmark

Generated at: `2026-07-13T23:41:25.614647+00:00`
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
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.022447`
- secondary_mean_absolute_error: `0.018216`
- primary_error_advantage: `-0.004231`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.028344`
- secondary_mean_absolute_error: `0.024371`
- primary_error_advantage: `-0.003973`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.032046`
- secondary_mean_absolute_error: `0.029679`
- primary_error_advantage: `-0.002367`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.056802`
- secondary_mean_absolute_error: `0.053031`
- primary_error_advantage: `-0.003771`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.5625`
- primary_mean_absolute_error: `0.085179`
- secondary_mean_absolute_error: `0.092484`
- primary_error_advantage: `0.007305`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5625`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.01812`, as_primary `0`, as_primary_hit `None`, avg `-0.004548`, median `-0.000929`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.022146`, as_primary `0`, as_primary_hit `None`, avg `-0.005435`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.024186`, as_primary `0`, as_primary_hit `None`, avg `-0.00253`, median `-0.004217`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.034734`, as_primary `0`, as_primary_hit `None`, avg `0.011535`, median `0.018039`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.06949`, as_primary `0`, as_primary_hit `None`, avg `0.02519`, median `0.04627`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.017982`, as_primary `20`, as_primary_hit `0.4`, avg `-0.004548`, median `-0.000929`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.022035`, as_primary `20`, as_primary_hit `0.4`, avg `-0.005435`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.029832`, as_primary `20`, as_primary_hit `0.3`, avg `-0.00253`, median `-0.004217`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.04679`, as_primary `20`, as_primary_hit `0.7`, avg `0.011535`, median `0.018039`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.0812`, as_primary `20`, as_primary_hit `0.75`, avg `0.02519`, median `0.04627`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.02268`, as_primary `60`, as_primary_hit `0.5167`, avg `-0.004548`, median `-0.000929`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.03068`, as_primary `60`, as_primary_hit `0.5167`, avg `-0.005435`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.031892`, as_primary `60`, as_primary_hit `0.4833`, avg `-0.00253`, median `-0.004217`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.063043`, as_primary `60`, as_primary_hit `0.7`, avg `0.011535`, median `0.018039`
- 60d: sample `80`, direction_hit `0.3625`, path_mae `0.096463`, as_primary `60`, as_primary_hit `0.6`, avg `0.02519`, median `0.04627`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.017409`, as_primary `0`, as_primary_hit `None`, avg `-0.004548`, median `-0.000929`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.021463`, as_primary `0`, as_primary_hit `None`, avg `-0.005435`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.023602`, as_primary `0`, as_primary_hit `None`, avg `-0.00253`, median `-0.004217`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.034329`, as_primary `0`, as_primary_hit `None`, avg `0.011535`, median `0.018039`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.067641`, as_primary `0`, as_primary_hit `None`, avg `0.02519`, median `0.04627`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4`, primary_mae `0.022447`, avg `-0.004548`, median `-0.000929`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.028344`, avg `-0.005435`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.032046`, avg `-0.00253`, median `-0.004217`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.056802`, avg `0.011535`, median `0.018039`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.5625`, primary_mae `0.085179`, avg `0.02519`, median `0.04627`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.01671`, avg `-0.007867`, median `-0.002721`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.026662`, avg `-0.005932`, median `0.002596`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.041879`, avg `-0.009372`, median `-0.003423`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.2`, primary_mae `0.076645`, avg `-0.00609`, median `0.011472`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.072351`, avg `-0.015813`, median `0.012183`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.4333`, primary_mae `0.024359`, avg `-0.003442`, median `0.000148`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4167`, primary_mae `0.028904`, avg `-0.005269`, median `-0.000921`
- 10d: sample `60`, primary_hit `0.4167`, primary_closer `0.5333`, primary_mae `0.028768`, avg `-0.000249`, median `-0.004577`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.55`, primary_mae `0.050188`, avg `0.01741`, median `0.020794`
- 60d: sample `60`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.089455`, avg `0.038858`, median `0.056701`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.01671, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.026662, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.028768, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.050188, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.072351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017409, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02268, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.01671, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021463, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03068, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.026662, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023602, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031892, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.028768, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034329, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.063043, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.050188, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.5625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067641, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.096463, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.072351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.024137`, avg `-0.01428`, median `-0.016078`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.028693`, avg `-0.021322`, median `-0.021157`
- 10d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.031819`, avg `-0.016048`, median `-0.019121`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.064954`, avg `-0.001322`, median `0.014689`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.094947`, avg `0.0335`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.022684`, avg `-0.008374`, median `-0.005846`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.021498`, avg `-0.010795`, median `-0.006116`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.025023`, avg `-0.003773`, median `-0.008724`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.75`, primary_mae `0.045065`, avg `0.020852`, median `0.027639`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.8125`, primary_mae `0.068513`, avg `0.062177`, median `0.066096`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.017041`, avg `-0.005815`, median `-0.001026`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.026855`, avg `-0.00179`, median `0.004486`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.041574`, avg `-0.006785`, median `-0.003423`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.125`, primary_mae `0.078871`, avg `-0.000386`, median `0.011472`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.068471`, avg `-0.020827`, median `-0.004562`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4`, primary_mae `0.022447`, avg `-0.004548`, median `-0.000929`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.028344`, avg `-0.005435`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.032046`, avg `-0.00253`, median `-0.004217`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.056802`, avg `0.011535`, median `0.018039`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.5625`, primary_mae `0.085179`, avg `0.02519`, median `0.04627`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4`, primary_mae `0.022447`, avg `-0.004548`, median `-0.000929`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.028344`, avg `-0.005435`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.032046`, avg `-0.00253`, median `-0.004217`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.056802`, avg `0.011535`, median `0.018039`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.5625`, primary_mae `0.085179`, avg `0.02519`, median `0.04627`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.018898`, avg `-0.004467`, median `-0.002547`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.4667`, primary_mae `0.02451`, avg `-0.0044`, median `0.001204`
- 10d: sample `60`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.031662`, avg `-0.000906`, median `-0.000315`
- 20d: sample `60`, primary_hit `0.4333`, primary_closer `0.4833`, primary_mae `0.053802`, avg `0.011551`, median `0.017588`
- 60d: sample `60`, primary_hit `0.5`, primary_closer `0.6333`, primary_mae `0.071565`, avg `0.027689`, median `0.04627`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.017355`, avg `-0.002079`, median `-0.000919`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.024735`, avg `0.000491`, median `0.003601`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.034099`, avg `0.002073`, median `0.002812`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.055183`, avg `0.010116`, median `0.013604`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.6`, primary_mae `0.064219`, avg `0.019542`, median `0.038362`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.4`, primary_mae `0.022447`, avg `-0.004548`, median `-0.000929`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.4125`, primary_mae `0.028344`, avg `-0.005435`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.032046`, avg `-0.00253`, median `-0.004217`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.4625`, primary_mae `0.056802`, avg `0.011535`, median `0.018039`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.5625`, primary_mae `0.085179`, avg `0.02519`, median `0.04627`

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
