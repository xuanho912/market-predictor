# Historical Replay Benchmark

Generated at: `2026-07-21T23:46:14.171555+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.015547`
- secondary_mean_absolute_error: `0.015577`
- primary_error_advantage: `3e-05`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.019419`
- secondary_mean_absolute_error: `0.018611`
- primary_error_advantage: `-0.000808`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.5625`
- primary_mean_absolute_error: `0.0259`
- secondary_mean_absolute_error: `0.028773`
- primary_error_advantage: `0.002873`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.064573`
- secondary_mean_absolute_error: `0.046826`
- primary_error_advantage: `-0.017747`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.111496`
- secondary_mean_absolute_error: `0.080238`
- primary_error_advantage: `-0.031258`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.013273`, as_primary `0`, as_primary_hit `None`, avg `-0.003695`, median `0.0`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.015602`, as_primary `0`, as_primary_hit `None`, avg `-0.004176`, median `-0.001935`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.02301`, as_primary `0`, as_primary_hit `None`, avg `-0.003767`, median `-0.007623`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.036228`, as_primary `0`, as_primary_hit `None`, avg `0.006994`, median `0.015926`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.073207`, as_primary `0`, as_primary_hit `None`, avg `0.017227`, median `0.04052`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015579`, as_primary `0`, as_primary_hit `None`, avg `-0.003695`, median `0.0`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.019181`, as_primary `0`, as_primary_hit `None`, avg `-0.004176`, median `-0.001935`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.030717`, as_primary `0`, as_primary_hit `None`, avg `-0.003767`, median `-0.007623`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.048935`, as_primary `0`, as_primary_hit `None`, avg `0.006994`, median `0.015926`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.086925`, as_primary `0`, as_primary_hit `None`, avg `0.017227`, median `0.04052`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015547`, as_primary `80`, as_primary_hit `0.5`, avg `-0.003695`, median `0.0`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.019419`, as_primary `80`, as_primary_hit `0.45`, avg `-0.004176`, median `-0.001935`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.0259`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.003767`, median `-0.007623`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.064573`, as_primary `80`, as_primary_hit `0.6625`, avg `0.006994`, median `0.015926`
- 60d: sample `80`, direction_hit `0.4`, path_mae `0.111496`, as_primary `80`, as_primary_hit `0.6`, avg `0.017227`, median `0.04052`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.01297`, as_primary `0`, as_primary_hit `None`, avg `-0.003695`, median `0.0`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.015099`, as_primary `0`, as_primary_hit `None`, avg `-0.004176`, median `-0.001935`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.021302`, as_primary `0`, as_primary_hit `None`, avg `-0.003767`, median `-0.007623`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.036178`, as_primary `0`, as_primary_hit `None`, avg `0.006994`, median `0.015926`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.072716`, as_primary `0`, as_primary_hit `None`, avg `0.017227`, median `0.04052`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.02256`, avg `-0.010447`, median `-0.009708`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.030411`, avg `-0.015121`, median `-0.016241`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.017441`, avg `-0.005842`, median `-0.007383`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.071611`, avg `0.013934`, median `0.023936`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.112506`, avg `0.04197`, median `0.059313`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.5167`, primary_mae `0.01321`, avg `-0.001445`, median `0.000609`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.5667`, primary_mae `0.015755`, avg `-0.000528`, median `-0.000392`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.5333`, primary_mae `0.028719`, avg `-0.003076`, median `-0.007955`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.3667`, primary_mae `0.062227`, avg `0.004681`, median `0.013099`
- 60d: sample `60`, primary_hit `0.4333`, primary_closer `0.3667`, primary_mae `0.11116`, avg `0.00898`, median `0.024439`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.5167`, primary_mae `0.01321`, avg `-0.001445`, median `0.000609`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.5667`, primary_mae `0.015755`, avg `-0.000528`, median `-0.000392`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.5333`, primary_mae `0.028719`, avg `-0.003076`, median `-0.007955`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.3667`, primary_mae `0.062227`, avg `0.004681`, median `0.013099`
- 60d: sample `60`, primary_hit `0.4333`, primary_closer `0.3667`, primary_mae `0.11116`, avg `0.00898`, median `0.024439`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.02256`, avg `-0.010447`, median `-0.009708`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.030411`, avg `-0.015121`, median `-0.016241`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.017441`, avg `-0.005842`, median `-0.007383`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.071611`, avg `0.013934`, median `0.023936`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.112506`, avg `0.04197`, median `0.059313`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.01321, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.015755, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.017441, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.062227, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.11116, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01297, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015579, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.01321, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015099, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019419, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.015755, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.5625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021302, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030717, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.017441, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036178, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064573, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.062227, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072716, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.111496, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.11116, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.020078`, avg `-0.012643`, median `-0.005846`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.027999`, avg `-0.016654`, median `-0.019178`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.013602`, avg `-0.011849`, median `-0.012486`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.077358`, avg `0.025786`, median `0.031583`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.12867`, avg `0.065978`, median `0.079666`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.022965`, avg `-0.010841`, median `-0.009708`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.030744`, avg `-0.015748`, median `-0.019178`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.75`, primary_mae `0.016602`, avg `-0.007709`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.069788`, avg `0.010274`, median `0.020913`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.110136`, avg `0.037639`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.010818`, avg `0.003577`, median `0.003846`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.625`, primary_mae `0.014562`, avg `0.002145`, median `-0.000392`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.031263`, avg `-0.014691`, median `-0.02037`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.079746`, avg `-0.022715`, median `-0.015599`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.138901`, avg `-0.061639`, median `-0.075187`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.015547`, avg `-0.003695`, median `0.0`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5375`, primary_mae `0.019419`, avg `-0.004176`, median `-0.001935`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.5625`, primary_mae `0.0259`, avg `-0.003767`, median `-0.007623`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.375`, primary_mae `0.064573`, avg `0.006994`, median `0.015926`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.111496`, avg `0.017227`, median `0.04052`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4875`, primary_mae `0.015547`, avg `-0.003695`, median `0.0`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5375`, primary_mae `0.019419`, avg `-0.004176`, median `-0.001935`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.5625`, primary_mae `0.0259`, avg `-0.003767`, median `-0.007623`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.375`, primary_mae `0.064573`, avg `0.006994`, median `0.015926`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.111496`, avg `0.017227`, median `0.04052`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.017328`, avg `-0.005798`, median `-0.001543`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.55`, primary_mae `0.021347`, avg `-0.008455`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.7`, primary_closer `0.65`, primary_mae `0.019538`, avg `-0.006177`, median `-0.008819`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.066825`, avg `0.005486`, median `0.017343`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.0925`, avg `0.028506`, median `0.041779`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.017325`, avg `-0.004392`, median `-0.003808`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.020934`, avg `-0.001842`, median `-0.007626`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.032382`, avg `0.010078`, median `0.015719`
- 20d: sample `20`, primary_hit `0.05`, primary_closer `0.35`, primary_mae `0.038526`, avg `0.032445`, median `0.037591`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.091583`, avg `0.041355`, median `0.064792`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

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
