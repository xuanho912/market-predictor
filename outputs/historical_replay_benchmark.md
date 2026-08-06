# Historical Replay Benchmark

Generated at: `2026-08-06T14:37:45.844107+00:00`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.017492`
- secondary_mean_absolute_error: `0.014758`
- primary_error_advantage: `-0.002734`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.019421`
- secondary_mean_absolute_error: `0.018881`
- primary_error_advantage: `-0.00054`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.02947`
- secondary_mean_absolute_error: `0.028552`
- primary_error_advantage: `-0.000918`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.057314`
- secondary_mean_absolute_error: `0.05633`
- primary_error_advantage: `-0.000984`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.072611`
- secondary_mean_absolute_error: `0.070965`
- primary_error_advantage: `-0.001646`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.014398`, as_primary `0`, as_primary_hit `None`, avg `0.002206`, median `0.004273`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.017401`, as_primary `0`, as_primary_hit `None`, avg `0.004269`, median `0.005545`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.025703`, as_primary `0`, as_primary_hit `None`, avg `0.006071`, median `0.006542`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.036912`, as_primary `0`, as_primary_hit `None`, avg `0.013643`, median `0.014634`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.060463`, as_primary `0`, as_primary_hit `None`, avg `0.024541`, median `0.031767`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.017094`, as_primary `40`, as_primary_hit `0.575`, avg `0.002206`, median `0.004273`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.022112`, as_primary `40`, as_primary_hit `0.75`, avg `0.004269`, median `0.005545`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.032706`, as_primary `40`, as_primary_hit `0.575`, avg `0.006071`, median `0.006542`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.059641`, as_primary `40`, as_primary_hit `0.675`, avg `0.013643`, median `0.014634`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.079143`, as_primary `40`, as_primary_hit `0.55`, avg `0.024541`, median `0.031767`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016959`, as_primary `40`, as_primary_hit `0.625`, avg `0.002206`, median `0.004273`
- 5d: sample `80`, direction_hit `0.3125`, path_mae `0.020134`, as_primary `40`, as_primary_hit `0.625`, avg `0.004269`, median `0.005545`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.030872`, as_primary `40`, as_primary_hit `0.6`, avg `0.006071`, median `0.006542`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.065869`, as_primary `40`, as_primary_hit `0.725`, avg `0.013643`, median `0.014634`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.071113`, as_primary `40`, as_primary_hit `0.575`, avg `0.024541`, median `0.031767`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.013914`, as_primary `0`, as_primary_hit `None`, avg `0.002206`, median `0.004273`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.015942`, as_primary `0`, as_primary_hit `None`, avg `0.004269`, median `0.005545`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.023339`, as_primary `0`, as_primary_hit `None`, avg `0.006071`, median `0.006542`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.034443`, as_primary `0`, as_primary_hit `None`, avg `0.013643`, median `0.014634`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.057037`, as_primary `0`, as_primary_hit `None`, avg `0.024541`, median `0.031767`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.017492`, avg `0.002206`, median `0.004273`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.019421`, avg `0.004269`, median `0.005545`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.02947`, avg `0.006071`, median `0.006542`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.057314`, avg `0.013643`, median `0.014634`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.5125`, primary_mae `0.072611`, avg `0.024541`, median `0.031767`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.017077`, avg `0.000297`, median `0.001723`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.55`, primary_mae `0.017127`, avg `0.00445`, median `0.005323`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.5167`, primary_mae `0.026276`, avg `0.003448`, median `0.005212`
- 20d: sample `60`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.053303`, avg `0.006842`, median `0.0135`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.067138`, avg `0.013194`, median `0.015082`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.01874`, avg `0.007934`, median `0.011854`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.026304`, avg `0.003726`, median `0.008022`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.039053`, avg `0.013941`, median `0.011814`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.069349`, avg `0.034045`, median `0.022345`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.089029`, avg `0.058582`, median `0.075516`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017077, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.017127, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.026276, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.053303, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.067138, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013914, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017094, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017077, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015942, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022112, 'direction_hit_rate': 0.6875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.017127, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023339, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032706, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.026276, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034443, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065869, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.053303, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057037, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.079143, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.067138, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.021843`, avg `-0.003813`, median `-0.002198`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.019614`, avg `0.000899`, median `0.003509`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020836`, avg `0.002265`, median `0.002208`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.058568`, avg `0.009259`, median `0.014663`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.75`, primary_mae `0.046041`, avg `-0.012738`, median `-0.032183`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.024404`, avg `-0.003882`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.018539`, avg `0.001466`, median `0.00171`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.020308`, avg `0.00012`, median `-0.000777`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.061383`, avg `0.006294`, median `0.014663`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.625`, primary_mae `0.060361`, avg `0.007054`, median `-0.012556`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.019749`, avg `0.007219`, median `0.010545`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.028222`, avg `0.002211`, median `0.003708`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.038032`, avg `0.010811`, median `0.003199`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.071395`, avg `0.034733`, median `0.022145`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.08918`, avg `0.051237`, median `0.070486`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.017492`, avg `0.002206`, median `0.004273`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.019421`, avg `0.004269`, median `0.005545`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.02947`, avg `0.006071`, median `0.006542`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.057314`, avg `0.013643`, median `0.014634`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.5125`, primary_mae `0.072611`, avg `0.024541`, median `0.031767`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.017492`, avg `0.002206`, median `0.004273`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.019421`, avg `0.004269`, median `0.005545`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.02947`, avg `0.006071`, median `0.006542`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.057314`, avg `0.013643`, median `0.014634`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.5125`, primary_mae `0.072611`, avg `0.024541`, median `0.031767`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.017077`, avg `0.000297`, median `0.001723`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.55`, primary_mae `0.017127`, avg `0.00445`, median `0.005323`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.5167`, primary_mae `0.026276`, avg `0.003448`, median `0.005212`
- 20d: sample `60`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.053303`, avg `0.006842`, median `0.0135`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.067138`, avg `0.013194`, median `0.015082`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.01874`, avg `0.007934`, median `0.011854`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.026304`, avg `0.003726`, median `0.008022`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.039053`, avg `0.013941`, median `0.011814`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.069349`, avg `0.034045`, median `0.022345`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.089029`, avg `0.058582`, median `0.075516`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.017492`, avg `0.002206`, median `0.004273`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.019421`, avg `0.004269`, median `0.005545`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.02947`, avg `0.006071`, median `0.006542`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.057314`, avg `0.013643`, median `0.014634`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.5125`, primary_mae `0.072611`, avg `0.024541`, median `0.031767`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.017492`, avg `0.002206`, median `0.004273`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.019421`, avg `0.004269`, median `0.005545`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.02947`, avg `0.006071`, median `0.006542`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.057314`, avg `0.013643`, median `0.014634`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.5125`, primary_mae `0.072611`, avg `0.024541`, median `0.031767`

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
