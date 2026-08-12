# Historical Replay Benchmark

Generated at: `2026-08-12T22:23:42.644340+00:00`
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
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.015725`
- secondary_mean_absolute_error: `0.012948`
- primary_error_advantage: `-0.002777`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.024177`
- secondary_mean_absolute_error: `0.015639`
- primary_error_advantage: `-0.008538`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.036049`
- secondary_mean_absolute_error: `0.022199`
- primary_error_advantage: `-0.01385`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.225`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.064354`
- secondary_mean_absolute_error: `0.035683`
- primary_error_advantage: `-0.028671`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.175`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.092896`
- secondary_mean_absolute_error: `0.065208`
- primary_error_advantage: `-0.027688`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.2`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013231`, as_primary `0`, as_primary_hit `None`, avg `0.002932`, median `0.004273`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.018096`, as_primary `0`, as_primary_hit `None`, avg `0.003803`, median `0.004935`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.025256`, as_primary `0`, as_primary_hit `None`, avg `0.007499`, median `0.00771`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.040041`, as_primary `0`, as_primary_hit `None`, avg `0.012945`, median `0.012723`
- 60d: sample `80`, direction_hit `0.575`, path_mae `0.069429`, as_primary `0`, as_primary_hit `None`, avg `0.019791`, median `0.026711`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.015725`, as_primary `80`, as_primary_hit `0.6125`, avg `0.002932`, median `0.004273`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.024177`, as_primary `80`, as_primary_hit `0.6875`, avg `0.003803`, median `0.004935`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.036049`, as_primary `80`, as_primary_hit `0.6125`, avg `0.007499`, median `0.00771`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.064354`, as_primary `80`, as_primary_hit `0.675`, avg `0.012945`, median `0.012723`
- 60d: sample `80`, direction_hit `0.575`, path_mae `0.092896`, as_primary `80`, as_primary_hit `0.575`, avg `0.019791`, median `0.026711`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.014705`, as_primary `0`, as_primary_hit `None`, avg `0.002932`, median `0.004273`
- 5d: sample `80`, direction_hit `0.3125`, path_mae `0.0178`, as_primary `0`, as_primary_hit `None`, avg `0.003803`, median `0.004935`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.02983`, as_primary `0`, as_primary_hit `None`, avg `0.007499`, median `0.00771`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.067943`, as_primary `0`, as_primary_hit `None`, avg `0.012945`, median `0.012723`
- 60d: sample `80`, direction_hit `0.425`, path_mae `0.083819`, as_primary `0`, as_primary_hit `None`, avg `0.019791`, median `0.026711`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.012948`, as_primary `0`, as_primary_hit `None`, avg `0.002932`, median `0.004273`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.015639`, as_primary `0`, as_primary_hit `None`, avg `0.003803`, median `0.004935`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.022199`, as_primary `0`, as_primary_hit `None`, avg `0.007499`, median `0.00771`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.035683`, as_primary `0`, as_primary_hit `None`, avg `0.012945`, median `0.012723`
- 60d: sample `80`, direction_hit `0.575`, path_mae `0.065208`, as_primary `0`, as_primary_hit `None`, avg `0.019791`, median `0.026711`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.013539`, avg `0.001474`, median `0.001352`
- 5d: sample `40`, primary_hit `0.725`, primary_closer `0.3`, primary_mae `0.025579`, avg `0.002571`, median `0.004719`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.037759`, avg `0.0051`, median `0.006069`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.275`, primary_mae `0.065015`, avg `0.011211`, median `0.011923`
- 60d: sample `40`, primary_hit `0.55`, primary_closer `0.275`, primary_mae `0.086283`, avg `0.017045`, median `0.017574`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.017911`, avg `0.00439`, median `0.006579`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.022775`, avg `0.005036`, median `0.005421`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.034339`, avg `0.009898`, median `0.011059`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.225`, primary_mae `0.063694`, avg `0.014678`, median `0.022248`
- 60d: sample `40`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.09951`, avg `0.022538`, median `0.045588`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5667`, primary_closer `0.4167`, primary_mae `0.016867`, avg `0.00107`, median `0.001774`
- 5d: sample `60`, primary_hit `0.6833`, primary_closer `0.2833`, primary_mae `0.026146`, avg `0.003135`, median `0.004629`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.3333`, primary_mae `0.036361`, avg `0.004866`, median `0.006069`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.2667`, primary_mae `0.062788`, avg `0.012621`, median `0.012222`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.3167`, primary_mae `0.084362`, avg `0.017024`, median `0.017574`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.0123`, avg `0.008518`, median `0.006631`
- 5d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.018271`, avg `0.005809`, median `0.007427`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.035114`, avg `0.015397`, median `0.017553`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.2`, primary_mae `0.069055`, avg `0.013915`, median `0.019252`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.2`, primary_mae `0.118499`, avg `0.028095`, median `0.054594`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.0123, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.018271, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.035114, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.062788, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.084362, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012948, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015725, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.0123, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015639, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024177, 'direction_hit_rate': 0.6875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.018271, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022199, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036049, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.035114, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035683, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067943, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.062788, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065208, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.092896, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.084362, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.02186`, avg `0.001218`, median `0.005338`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.028582`, avg `0.000746`, median `0.004667`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.028141`, avg `0.006792`, median `0.007806`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.125`, primary_mae `0.052035`, avg `0.019195`, median `0.023697`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.077329`, avg `0.01915`, median `0.007661`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.023028`, avg `0.000933`, median `0.005338`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.026597`, avg `0.005497`, median `0.004667`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.028526`, avg `0.010194`, median `0.011059`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.050821`, avg `0.023589`, median `0.026122`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.070641`, avg `0.026314`, median `0.038342`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.023028`, avg `0.000933`, median `0.005338`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.026597`, avg `0.005497`, median `0.004667`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.028526`, avg `0.010194`, median `0.011059`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.050821`, avg `0.023589`, median `0.026122`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.070641`, avg `0.026314`, median `0.038342`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.015725`, avg `0.002932`, median `0.004273`
- 5d: sample `80`, primary_hit `0.6875`, primary_closer `0.3`, primary_mae `0.024177`, avg `0.003803`, median `0.004935`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3125`, primary_mae `0.036049`, avg `0.007499`, median `0.00771`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.25`, primary_mae `0.064354`, avg `0.012945`, median `0.012723`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.2875`, primary_mae `0.092896`, avg `0.019791`, median `0.026711`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.015725`, avg `0.002932`, median `0.004273`
- 5d: sample `80`, primary_hit `0.6875`, primary_closer `0.3`, primary_mae `0.024177`, avg `0.003803`, median `0.004935`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3125`, primary_mae `0.036049`, avg `0.007499`, median `0.00771`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.25`, primary_mae `0.064354`, avg `0.012945`, median `0.012723`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.2875`, primary_mae `0.092896`, avg `0.019791`, median `0.026711`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.014634`, avg `0.002335`, median `0.003446`
- 5d: sample `60`, primary_hit `0.7`, primary_closer `0.3167`, primary_mae `0.018117`, avg `0.004677`, median `0.005202`
- 10d: sample `60`, primary_hit `0.6167`, primary_closer `0.35`, primary_mae `0.027082`, avg `0.007783`, median `0.008249`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.2833`, primary_mae `0.05076`, avg `0.011231`, median `0.017926`
- 60d: sample `60`, primary_hit `0.5167`, primary_closer `0.3167`, primary_mae `0.089404`, avg `0.010639`, median `0.015082`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.018998`, avg `0.004722`, median `0.008884`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.042357`, avg `0.001184`, median `0.004719`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.06295`, avg `0.006646`, median `0.007278`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.15`, primary_mae `0.105137`, avg `0.018086`, median `0.01147`
- 60d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.103372`, avg `0.047247`, median `0.028352`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.015725`, avg `0.002932`, median `0.004273`
- 5d: sample `80`, primary_hit `0.6875`, primary_closer `0.3`, primary_mae `0.024177`, avg `0.003803`, median `0.004935`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3125`, primary_mae `0.036049`, avg `0.007499`, median `0.00771`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.25`, primary_mae `0.064354`, avg `0.012945`, median `0.012723`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.2875`, primary_mae `0.092896`, avg `0.019791`, median `0.026711`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.015725`, avg `0.002932`, median `0.004273`
- 5d: sample `80`, primary_hit `0.6875`, primary_closer `0.3`, primary_mae `0.024177`, avg `0.003803`, median `0.004935`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3125`, primary_mae `0.036049`, avg `0.007499`, median `0.00771`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.25`, primary_mae `0.064354`, avg `0.012945`, median `0.012723`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.2875`, primary_mae `0.092896`, avg `0.019791`, median `0.026711`

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
