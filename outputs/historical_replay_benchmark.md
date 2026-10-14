# Historical Replay Benchmark

Generated at: `2026-10-14T17:15:11.002594+00:00`
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
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.3625`
- primary_vs_secondary_accuracy_spread: `0.275`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.018438`
- secondary_mean_absolute_error: `0.016744`
- primary_error_advantage: `-0.001694`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.3625`
- primary_vs_secondary_accuracy_spread: `0.275`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.021858`
- secondary_mean_absolute_error: `0.019538`
- primary_error_advantage: `-0.00232`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.027111`
- secondary_mean_absolute_error: `0.027886`
- primary_error_advantage: `0.000775`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.056594`
- secondary_mean_absolute_error: `0.041082`
- primary_error_advantage: `-0.015512`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.079925`
- secondary_mean_absolute_error: `0.059172`
- primary_error_advantage: `-0.020753`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.015994`, as_primary `0`, as_primary_hit `None`, avg `-0.008069`, median `-0.010184`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.017533`, as_primary `0`, as_primary_hit `None`, avg `-0.011107`, median `-0.013608`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.026393`, as_primary `0`, as_primary_hit `None`, avg `-0.008813`, median `-0.0103`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.036297`, as_primary `0`, as_primary_hit `None`, avg `0.01298`, median `0.013348`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.053694`, as_primary `0`, as_primary_hit `None`, avg `0.059104`, median `0.059722`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.017297`, as_primary `0`, as_primary_hit `None`, avg `-0.008069`, median `-0.010184`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.020111`, as_primary `0`, as_primary_hit `None`, avg `-0.011107`, median `-0.013608`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.035887`, as_primary `0`, as_primary_hit `None`, avg `-0.008813`, median `-0.0103`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.05525`, as_primary `0`, as_primary_hit `None`, avg `0.01298`, median `0.013348`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.068316`, as_primary `0`, as_primary_hit `None`, avg `0.059104`, median `0.059722`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.018438`, as_primary `80`, as_primary_hit `0.3625`, avg `-0.008069`, median `-0.010184`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.021858`, as_primary `80`, as_primary_hit `0.3625`, avg `-0.011107`, median `-0.013608`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.027111`, as_primary `80`, as_primary_hit `0.3875`, avg `-0.008813`, median `-0.0103`
- 20d: sample `80`, direction_hit `0.4375`, path_mae `0.056594`, as_primary `80`, as_primary_hit `0.5625`, avg `0.01298`, median `0.013348`
- 60d: sample `80`, direction_hit `0.1875`, path_mae `0.079925`, as_primary `80`, as_primary_hit `0.8125`, avg `0.059104`, median `0.059722`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.015607`, as_primary `0`, as_primary_hit `None`, avg `-0.008069`, median `-0.010184`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.017434`, as_primary `0`, as_primary_hit `None`, avg `-0.011107`, median `-0.013608`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.02356`, as_primary `0`, as_primary_hit `None`, avg `-0.008813`, median `-0.0103`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.034065`, as_primary `0`, as_primary_hit `None`, avg `0.01298`, median `0.013348`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.054042`, as_primary `0`, as_primary_hit `None`, avg `0.059104`, median `0.059722`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.018438`, avg `-0.008069`, median `-0.010184`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.45`, primary_mae `0.021858`, avg `-0.011107`, median `-0.013608`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.5125`, primary_mae `0.027111`, avg `-0.008813`, median `-0.0103`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.056594`, avg `0.01298`, median `0.013348`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.325`, primary_mae `0.079925`, avg `0.059104`, median `0.059722`

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
- 3d: sample `20`, primary_hit `0.85`, primary_closer `0.3`, primary_mae `0.014865`, avg `-0.011039`, median `-0.012143`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.35`, primary_mae `0.018108`, avg `-0.01653`, median `-0.021206`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.034234`, avg `-0.018576`, median `-0.037567`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.066214`, avg `0.009553`, median `-0.003631`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.2`, primary_mae `0.075707`, avg `0.075711`, median `0.079581`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.021331`, avg `-0.008721`, median `-0.010064`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.025678`, avg `-0.014498`, median `-0.016241`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.024084`, avg `-0.007358`, median `-0.010944`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.067585`, avg `0.011975`, median `0.019252`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.117653`, avg `0.046515`, median `0.059313`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.018777`, avg `-0.006257`, median `-0.005583`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.021824`, avg `-0.006701`, median `-0.00462`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.025063`, avg `-0.00466`, median `-0.006775`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.425`, primary_mae `0.046288`, avg `0.015195`, median `0.017072`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.425`, primary_mae `0.063169`, avg `0.057095`, median `0.054674`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.014865, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.018108, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.024084, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.046288, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.063169, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_vs_secondary_accuracy_spread': 0.275, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015607, 'direction_hit_rate': 0.3625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018438, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.014865, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_vs_secondary_accuracy_spread': 0.275, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017434, 'direction_hit_rate': 0.3625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021858, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.018108, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02356, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035887, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.024084, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034065, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056594, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.046288, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053694, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.079925, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.063169, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.023351`, avg `-0.00704`, median `-0.005846`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.028761`, avg `-0.006894`, median `-0.008611`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.022839`, avg `-0.00497`, median `-0.008724`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.09119`, avg `0.044382`, median `0.050926`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.155147`, avg `0.09719`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.02056`, avg `-0.009066`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.025548`, avg `-0.015274`, median `-0.019358`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.5625`, primary_mae `0.022268`, avg `-0.010306`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.071359`, avg `0.013548`, median `0.023936`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.119013`, avg `0.044578`, median `0.059313`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.012448`, avg `-0.01415`, median `-0.012143`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.015772`, avg `-0.019625`, median `-0.021206`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.030196`, avg `-0.023591`, median `-0.038377`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.069029`, avg `0.015031`, median `-0.003631`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.125`, primary_mae `0.082226`, avg `0.081348`, median `0.086161`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.018438`, avg `-0.008069`, median `-0.010184`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.45`, primary_mae `0.021858`, avg `-0.011107`, median `-0.013608`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.5125`, primary_mae `0.027111`, avg `-0.008813`, median `-0.0103`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.056594`, avg `0.01298`, median `0.013348`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.325`, primary_mae `0.079925`, avg `0.059104`, median `0.059722`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.018438`, avg `-0.008069`, median `-0.010184`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.45`, primary_mae `0.021858`, avg `-0.011107`, median `-0.013608`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.5125`, primary_mae `0.027111`, avg `-0.008813`, median `-0.0103`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.056594`, avg `0.01298`, median `0.013348`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.325`, primary_mae `0.079925`, avg `0.059104`, median `0.059722`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.020052`, avg `-0.006483`, median `-0.002999`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.025214`, avg `-0.011464`, median `-0.012743`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.027124`, avg `-0.008689`, median `-0.008686`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.05912`, avg `0.009985`, median `0.016081`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.080745`, avg `0.036815`, median `0.052147`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.725`, primary_closer `0.35`, primary_mae `0.016823`, avg `-0.009655`, median `-0.013281`
- 5d: sample `40`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.018503`, avg `-0.01075`, median `-0.013608`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.027098`, avg `-0.008938`, median `-0.013578`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.054068`, avg `0.015974`, median `0.009045`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.3`, primary_mae `0.079104`, avg `0.081393`, median `0.079581`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.018438`, avg `-0.008069`, median `-0.010184`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.45`, primary_mae `0.021858`, avg `-0.011107`, median `-0.013608`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.5125`, primary_mae `0.027111`, avg `-0.008813`, median `-0.0103`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.056594`, avg `0.01298`, median `0.013348`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.325`, primary_mae `0.079925`, avg `0.059104`, median `0.059722`

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
