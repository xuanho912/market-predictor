# Historical Replay Benchmark

Generated at: `2026-07-18T13:52:29.582330+00:00`
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
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.020664`
- secondary_mean_absolute_error: `0.014165`
- primary_error_advantage: `-0.006499`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.02507`
- secondary_mean_absolute_error: `0.017542`
- primary_error_advantage: `-0.007528`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.225`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.027452`
- secondary_mean_absolute_error: `0.026388`
- primary_error_advantage: `-0.001064`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2625`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.475`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.056993`
- secondary_mean_absolute_error: `0.038392`
- primary_error_advantage: `-0.018601`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.091794`
- secondary_mean_absolute_error: `0.070175`
- primary_error_advantage: `-0.021619`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.014323`, as_primary `0`, as_primary_hit `None`, avg `-0.001194`, median `0.001884`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017142`, as_primary `0`, as_primary_hit `None`, avg `-0.000571`, median `0.002095`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.025047`, as_primary `0`, as_primary_hit `None`, avg `-0.000321`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.031283`, as_primary `0`, as_primary_hit `None`, avg `0.016358`, median `0.019949`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.062763`, as_primary `0`, as_primary_hit `None`, avg `0.037739`, median `0.058364`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.014274`, as_primary `0`, as_primary_hit `None`, avg `-0.001194`, median `0.001884`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.018961`, as_primary `0`, as_primary_hit `None`, avg `-0.000571`, median `0.002095`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.031807`, as_primary `0`, as_primary_hit `None`, avg `-0.000321`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.044908`, as_primary `0`, as_primary_hit `None`, avg `0.016358`, median `0.019949`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.073218`, as_primary `0`, as_primary_hit `None`, avg `0.037739`, median `0.058364`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.020664`, as_primary `80`, as_primary_hit `0.6125`, avg `-0.001194`, median `0.001884`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.02507`, as_primary `80`, as_primary_hit `0.5625`, avg `-0.000571`, median `0.002095`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.027452`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.000321`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.2625`, path_mae `0.056993`, as_primary `80`, as_primary_hit `0.7375`, avg `0.016358`, median `0.019949`
- 60d: sample `80`, direction_hit `0.3375`, path_mae `0.091794`, as_primary `80`, as_primary_hit `0.6625`, avg `0.037739`, median `0.058364`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.014042`, as_primary `0`, as_primary_hit `None`, avg `-0.001194`, median `0.001884`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017044`, as_primary `0`, as_primary_hit `None`, avg `-0.000571`, median `0.002095`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.023464`, as_primary `0`, as_primary_hit `None`, avg `-0.000321`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.03134`, as_primary `0`, as_primary_hit `None`, avg `0.016358`, median `0.019949`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.063951`, as_primary `0`, as_primary_hit `None`, avg `0.037739`, median `0.058364`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.325`, primary_mae `0.020664`, avg `-0.001194`, median `0.001884`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.3625`, primary_mae `0.02507`, avg `-0.000571`, median `0.002095`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.027452`, avg `-0.000321`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.3375`, primary_mae `0.056993`, avg `0.016358`, median `0.019949`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.3875`, primary_mae `0.091794`, avg `0.037739`, median `0.058364`

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
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.015017`, avg `-0.000332`, median `0.00113`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.01594`, avg `0.000841`, median `0.001088`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.029922`, avg `0.002391`, median `0.000926`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.052038`, avg `0.015876`, median `0.017835`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.07126`, avg `0.022949`, median `0.045011`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.35`, primary_closer `0.275`, primary_mae `0.026311`, avg `-0.002057`, median `0.004136`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.225`, primary_mae `0.0342`, avg `-0.001984`, median `0.002729`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.024983`, avg `-0.003033`, median `-0.011477`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.325`, primary_mae `0.061948`, avg `0.01684`, median `0.019949`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.112328`, avg `0.052529`, median `0.089937`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.015017, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.01594, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.024983, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.052038, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.07126, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014042, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020664, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.015017, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017044, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02507, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.01594, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023464, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031807, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.024983, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.475, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031283, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056993, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.052038, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062763, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.091794, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.07126, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.017803`, avg `-0.014894`, median `-0.010699`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.025365`, avg `-0.010839`, median `-0.006116`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.022461`, avg `-0.002733`, median `-0.00918`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.07316`, avg `0.018363`, median `0.024498`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.119623`, avg `0.053794`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.022554`, avg `-0.010542`, median `-0.005846`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.027715`, avg `-0.011586`, median `7.5e-05`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.021932`, avg `-0.004329`, median `-0.007383`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.069467`, avg `0.004974`, median `0.01849`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.104768`, avg `0.029527`, median `0.03596`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.016124`, avg `-0.003674`, median `-0.003808`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.01925`, avg `0.001982`, median `-0.002448`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.033307`, avg `0.009331`, median `0.008455`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.5`, primary_mae `0.029814`, avg `0.031097`, median `0.02289`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.070346`, avg `0.044745`, median `0.057208`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.325`, primary_mae `0.020664`, avg `-0.001194`, median `0.001884`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.3625`, primary_mae `0.02507`, avg `-0.000571`, median `0.002095`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.027452`, avg `-0.000321`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.3375`, primary_mae `0.056993`, avg `0.016358`, median `0.019949`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.3875`, primary_mae `0.091794`, avg `0.037739`, median `0.058364`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.325`, primary_mae `0.020664`, avg `-0.001194`, median `0.001884`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.3625`, primary_mae `0.02507`, avg `-0.000571`, median `0.002095`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.027452`, avg `-0.000321`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.3375`, primary_mae `0.056993`, avg `0.016358`, median `0.019949`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.3875`, primary_mae `0.091794`, avg `0.037739`, median `0.058364`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.35`, primary_closer `0.3167`, primary_mae `0.021228`, avg `-0.001492`, median `0.002204`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.3167`, primary_mae `0.027077`, avg `-0.001703`, median `0.002095`
- 10d: sample `60`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.025265`, avg `-0.004726`, median `-0.011477`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.3`, primary_mae `0.06549`, avg `0.010797`, median `0.01849`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.3833`, primary_mae `0.097139`, avg `0.037956`, median `0.058364`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.015017`, avg `-0.000332`, median `0.00113`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.01594`, avg `0.000841`, median `0.001088`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.029922`, avg `0.002391`, median `0.000926`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.052038`, avg `0.015876`, median `0.017835`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.07126`, avg `0.022949`, median `0.045011`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.325`, primary_mae `0.020664`, avg `-0.001194`, median `0.001884`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.3625`, primary_mae `0.02507`, avg `-0.000571`, median `0.002095`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.4625`, primary_mae `0.027452`, avg `-0.000321`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.3375`, primary_mae `0.056993`, avg `0.016358`, median `0.019949`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.3875`, primary_mae `0.091794`, avg `0.037739`, median `0.058364`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.023864`, avg `-0.001471`, median `0.003063`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.3167`, primary_mae `0.02915`, avg `-0.000381`, median `0.002469`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.027994`, avg `0.002276`, median `-0.003466`
- 20d: sample `60`, primary_hit `0.2`, primary_closer `0.3667`, primary_mae `0.0518`, avg `0.02224`, median `0.024617`
- 60d: sample `60`, primary_hit `0.2833`, primary_closer `0.35`, primary_mae `0.100139`, avg `0.047381`, median `0.069999`

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
