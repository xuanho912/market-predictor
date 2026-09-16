# Historical Replay Benchmark

Generated at: `2026-09-16T01:24:35.826903+00:00`
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
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.028086`
- secondary_mean_absolute_error: `0.019369`
- primary_error_advantage: `-0.008717`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.027715`
- secondary_mean_absolute_error: `0.020491`
- primary_error_advantage: `-0.007224`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.045111`
- secondary_mean_absolute_error: `0.030668`
- primary_error_advantage: `-0.014443`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.069042`
- secondary_mean_absolute_error: `0.040524`
- primary_error_advantage: `-0.028518`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.225`
- secondary_hit_rate: `0.775`
- primary_vs_secondary_accuracy_spread: `-0.55`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.065609`
- secondary_mean_absolute_error: `0.057889`
- primary_error_advantage: `-0.00772`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.019458`, as_primary `0`, as_primary_hit `None`, avg `0.004277`, median `0.006695`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.02173`, as_primary `0`, as_primary_hit `None`, avg `0.006056`, median `0.00805`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.032007`, as_primary `0`, as_primary_hit `None`, avg `0.007353`, median `0.008459`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.041619`, as_primary `0`, as_primary_hit `None`, avg `0.024821`, median `0.032589`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.055435`, as_primary `0`, as_primary_hit `None`, avg `0.068471`, median `0.079408`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.021186`, as_primary `0`, as_primary_hit `None`, avg `0.004277`, median `0.006695`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.02588`, as_primary `0`, as_primary_hit `None`, avg `0.006056`, median `0.00805`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.039115`, as_primary `0`, as_primary_hit `None`, avg `0.007353`, median `0.008459`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.060088`, as_primary `0`, as_primary_hit `None`, avg `0.024821`, median `0.032589`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.061661`, as_primary `0`, as_primary_hit `None`, avg `0.068471`, median `0.079408`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.028086`, as_primary `80`, as_primary_hit `0.625`, avg `0.004277`, median `0.006695`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.027715`, as_primary `80`, as_primary_hit `0.5875`, avg `0.006056`, median `0.00805`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.045111`, as_primary `80`, as_primary_hit `0.6125`, avg `0.007353`, median `0.008459`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.069042`, as_primary `80`, as_primary_hit `0.6875`, avg `0.024821`, median `0.032589`
- 60d: sample `80`, direction_hit `0.225`, path_mae `0.065609`, as_primary `80`, as_primary_hit `0.775`, avg `0.068471`, median `0.079408`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.019369`, as_primary `0`, as_primary_hit `None`, avg `0.004277`, median `0.006695`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.020491`, as_primary `0`, as_primary_hit `None`, avg `0.006056`, median `0.00805`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.030668`, as_primary `0`, as_primary_hit `None`, avg `0.007353`, median `0.008459`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.040524`, as_primary `0`, as_primary_hit `None`, avg `0.024821`, median `0.032589`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.057889`, as_primary `0`, as_primary_hit `None`, avg `0.068471`, median `0.079408`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.2875`, primary_mae `0.028086`, avg `0.004277`, median `0.006695`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.027715`, avg `0.006056`, median `0.00805`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.325`, primary_mae `0.045111`, avg `0.007353`, median `0.008459`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.2875`, primary_mae `0.069042`, avg `0.024821`, median `0.032589`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3625`, primary_mae `0.065609`, avg `0.068471`, median `0.079408`

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
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.3`, primary_mae `0.029648`, avg `0.000726`, median `0.001552`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.325`, primary_mae `0.027841`, avg `-0.000491`, median `-0.002914`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.043858`, avg `-0.002177`, median `0.000876`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.062054`, avg `0.013917`, median `0.030823`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.074622`, avg `0.035849`, median `0.058851`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.325`, primary_closer `0.275`, primary_mae `0.026524`, avg `0.007829`, median `0.012428`
- 5d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.027589`, avg `0.012602`, median `0.013727`
- 10d: sample `40`, primary_hit `0.325`, primary_closer `0.3`, primary_mae `0.046363`, avg `0.016882`, median `0.014856`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.07603`, avg `0.035726`, median `0.034552`
- 60d: sample `40`, primary_hit `0.1`, primary_closer `0.375`, primary_mae `0.056595`, avg `0.101094`, median `0.11635`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.026524, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.027589, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.043858, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.062054, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.056595, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019369, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028086, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.026524, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020491, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027715, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.027589, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030668, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045111, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.043858, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040524, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069042, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.062054, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.225, 'secondary_hit_rate': 0.775, 'primary_vs_secondary_accuracy_spread': -0.55, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055435, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065609, 'direction_hit_rate': 0.225}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.056595, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.020148`, avg `-0.000237`, median `0.001049`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.019163`, avg `0.000661`, median `0.006272`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.024567`, avg `0.008333`, median `0.013415`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.0`, primary_mae `0.089629`, avg `0.044381`, median `0.050926`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.063616`, avg `0.088721`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.022579`, avg `0.00331`, median `0.008014`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.021628`, avg `0.003713`, median `0.008828`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.027002`, avg `0.006237`, median `0.01205`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.076847`, avg `0.021923`, median `0.029476`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.4375`, primary_mae `0.054457`, avg `0.068685`, median `0.093308`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.031132`, avg `0.011546`, median `0.021377`
- 5d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.032774`, avg `0.02033`, median `0.016178`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.064165`, avg `0.020977`, median `0.019072`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.076678`, avg `0.04935`, median `0.034563`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.375`, primary_mae `0.062946`, avg `0.119977`, median `0.147547`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.2875`, primary_mae `0.028086`, avg `0.004277`, median `0.006695`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.027715`, avg `0.006056`, median `0.00805`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.325`, primary_mae `0.045111`, avg `0.007353`, median `0.008459`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.2875`, primary_mae `0.069042`, avg `0.024821`, median `0.032589`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3625`, primary_mae `0.065609`, avg `0.068471`, median `0.079408`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.2875`, primary_mae `0.028086`, avg `0.004277`, median `0.006695`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.027715`, avg `0.006056`, median `0.00805`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.325`, primary_mae `0.045111`, avg `0.007353`, median `0.008459`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.2875`, primary_mae `0.069042`, avg `0.024821`, median `0.032589`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3625`, primary_mae `0.065609`, avg `0.068471`, median `0.079408`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.2875`, primary_mae `0.028086`, avg `0.004277`, median `0.006695`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.027715`, avg `0.006056`, median `0.00805`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.325`, primary_mae `0.045111`, avg `0.007353`, median `0.008459`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.2875`, primary_mae `0.069042`, avg `0.024821`, median `0.032589`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3625`, primary_mae `0.065609`, avg `0.068471`, median `0.079408`

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
