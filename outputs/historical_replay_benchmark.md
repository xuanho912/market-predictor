# Historical Replay Benchmark

Generated at: `2026-10-15T01:02:11.125615+00:00`
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
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.017186`
- secondary_mean_absolute_error: `0.016065`
- primary_error_advantage: `-0.001121`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.020741`
- secondary_mean_absolute_error: `0.01851`
- primary_error_advantage: `-0.002231`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.025155`
- secondary_mean_absolute_error: `0.025286`
- primary_error_advantage: `0.000131`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.053732`
- secondary_mean_absolute_error: `0.039658`
- primary_error_advantage: `-0.014074`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `-0.6`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.084787`
- secondary_mean_absolute_error: `0.060733`
- primary_error_advantage: `-0.024054`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.014971`, as_primary `0`, as_primary_hit `None`, avg `-0.008176`, median `-0.009938`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.016968`, as_primary `0`, as_primary_hit `None`, avg `-0.011436`, median `-0.01468`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.025146`, as_primary `0`, as_primary_hit `None`, avg `-0.007464`, median `-0.009673`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.035128`, as_primary `0`, as_primary_hit `None`, avg `0.015984`, median `0.017588`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.055843`, as_primary `0`, as_primary_hit `None`, avg `0.057636`, median `0.059722`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.015967`, as_primary `0`, as_primary_hit `None`, avg `-0.008176`, median `-0.009938`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.019983`, as_primary `0`, as_primary_hit `None`, avg `-0.011436`, median `-0.01468`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.034408`, as_primary `0`, as_primary_hit `None`, avg `-0.007464`, median `-0.009673`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.053209`, as_primary `0`, as_primary_hit `None`, avg `0.015984`, median `0.017588`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.06927`, as_primary `0`, as_primary_hit `None`, avg `0.057636`, median `0.059722`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.017186`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.008176`, median `-0.009938`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.020741`, as_primary `80`, as_primary_hit `0.375`, avg `-0.011436`, median `-0.01468`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.025155`, as_primary `80`, as_primary_hit `0.4`, avg `-0.007464`, median `-0.009673`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.053732`, as_primary `80`, as_primary_hit `0.6125`, avg `0.015984`, median `0.017588`
- 60d: sample `80`, direction_hit `0.2`, path_mae `0.084787`, as_primary `80`, as_primary_hit `0.8`, avg `0.057636`, median `0.059722`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.014989`, as_primary `0`, as_primary_hit `None`, avg `-0.008176`, median `-0.009938`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.016677`, as_primary `0`, as_primary_hit `None`, avg `-0.011436`, median `-0.01468`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.02204`, as_primary `0`, as_primary_hit `None`, avg `-0.007464`, median `-0.009673`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.032908`, as_primary `0`, as_primary_hit `None`, avg `0.015984`, median `0.017588`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.055615`, as_primary `0`, as_primary_hit `None`, avg `0.057636`, median `0.059722`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.017186`, avg `-0.008176`, median `-0.009938`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.020741`, avg `-0.011436`, median `-0.01468`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5375`, primary_mae `0.025155`, avg `-0.007464`, median `-0.009673`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.375`, primary_mae `0.053732`, avg `0.015984`, median `0.017588`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.325`, primary_mae `0.084787`, avg `0.057636`, median `0.059722`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.014159`, avg `-0.011745`, median `-0.010671`
- 5d: sample `20`, primary_hit `0.8`, primary_closer `0.4`, primary_mae `0.016571`, avg `-0.018067`, median `-0.021869`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.55`, primary_mae `0.032017`, avg `-0.020527`, median `-0.036035`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.070028`, avg `0.013366`, median `-0.000315`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.2`, primary_mae `0.079639`, avg `0.079642`, median `0.086161`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.023162`, avg `-0.009159`, median `-0.010064`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.030574`, avg `-0.013912`, median `-0.016241`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.025441`, avg `-0.005032`, median `-0.008236`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.067979`, avg `0.013901`, median `0.020794`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.131489`, avg `0.045481`, median `0.059313`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.015711`, avg `-0.005901`, median `-0.002999`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.01791`, avg `-0.006883`, median `-0.008171`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.021582`, avg `-0.002148`, median `-0.00321`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.03846`, avg `0.018335`, median `0.018851`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.4`, primary_mae `0.06401`, avg `0.05271`, median `0.05427`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.014159, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016571, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.021582, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.03846, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.06401, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014971, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017186, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.014159, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016677, 'direction_hit_rate': 0.375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020741, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016571, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02204, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034408, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.021582, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032908, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053732, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.03846, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': -0.6, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055615, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.084787, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.06401, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.024774`, avg `-0.00704`, median `-0.005846`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.035244`, avg `-0.006894`, median `-0.008611`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.0218`, avg `-0.00497`, median `-0.008724`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.089276`, avg `0.044382`, median `0.050926`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.173734`, avg `0.09719`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.025276`, avg `-0.006475`, median `-0.005846`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.032885`, avg `-0.011699`, median `-0.016241`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.023066`, avg `-0.004292`, median `-0.008236`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.075099`, avg `0.020962`, median `0.027639`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.143408`, avg `0.058792`, median `0.066096`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.012205`, avg `-0.014393`, median `-0.012206`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.014561`, avg `-0.020836`, median `-0.021869`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.030717`, avg `-0.022738`, median `-0.037567`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.066445`, avg `0.012079`, median `-0.003631`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.077154`, avg `0.073998`, median `0.079581`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.017186`, avg `-0.008176`, median `-0.009938`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.020741`, avg `-0.011436`, median `-0.01468`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5375`, primary_mae `0.025155`, avg `-0.007464`, median `-0.009673`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.375`, primary_mae `0.053732`, avg `0.015984`, median `0.017588`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.325`, primary_mae `0.084787`, avg `0.057636`, median `0.059722`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.017186`, avg `-0.008176`, median `-0.009938`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.020741`, avg `-0.011436`, median `-0.01468`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5375`, primary_mae `0.025155`, avg `-0.007464`, median `-0.009673`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.375`, primary_mae `0.053732`, avg `0.015984`, median `0.017588`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.325`, primary_mae `0.084787`, avg `0.057636`, median `0.059722`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.018772`, avg `-0.005894`, median `-0.002206`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.024559`, avg `-0.010436`, median `-0.012419`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.02322`, avg `-0.005031`, median `-0.007123`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.425`, primary_mae `0.051928`, avg `0.013728`, median `0.01955`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.089235`, avg `0.036857`, median `0.052147`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.0156`, avg `-0.010459`, median `-0.012206`
- 5d: sample `40`, primary_hit `0.7`, primary_closer `0.475`, primary_mae `0.016924`, avg `-0.012436`, median `-0.014798`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.027091`, avg `-0.009896`, median `-0.014448`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.055536`, avg `0.018241`, median `0.013497`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.275`, primary_mae `0.080339`, avg `0.078415`, median `0.079581`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.017186`, avg `-0.008176`, median `-0.009938`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.020741`, avg `-0.011436`, median `-0.01468`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5375`, primary_mae `0.025155`, avg `-0.007464`, median `-0.009673`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.375`, primary_mae `0.053732`, avg `0.015984`, median `0.017588`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.325`, primary_mae `0.084787`, avg `0.057636`, median `0.059722`

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
