# Historical Replay Benchmark

Generated at: `2026-09-30T18:04:14.499687+00:00`
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
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.016599`
- secondary_mean_absolute_error: `0.015637`
- primary_error_advantage: `-0.000962`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.026722`
- secondary_mean_absolute_error: `0.020311`
- primary_error_advantage: `-0.006411`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.040298`
- secondary_mean_absolute_error: `0.029418`
- primary_error_advantage: `-0.01088`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.074525`
- secondary_mean_absolute_error: `0.050761`
- primary_error_advantage: `-0.023764`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2375`
- secondary_hit_rate: `0.7625`
- primary_vs_secondary_accuracy_spread: `-0.525`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.097073`
- secondary_mean_absolute_error: `0.074614`
- primary_error_advantage: `-0.022459`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.0151`, as_primary `0`, as_primary_hit `None`, avg `-0.005194`, median `-0.003446`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.019092`, as_primary `0`, as_primary_hit `None`, avg `-0.008838`, median `-0.005714`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.027686`, as_primary `0`, as_primary_hit `None`, avg `-0.005192`, median `-0.002583`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.041287`, as_primary `0`, as_primary_hit `None`, avg `0.007179`, median `0.016386`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.063447`, as_primary `0`, as_primary_hit `None`, avg `0.033783`, median `0.045479`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.015596`, as_primary `0`, as_primary_hit `None`, avg `-0.005194`, median `-0.003446`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.020294`, as_primary `0`, as_primary_hit `None`, avg `-0.008838`, median `-0.005714`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.034536`, as_primary `0`, as_primary_hit `None`, avg `-0.005192`, median `-0.002583`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.061601`, as_primary `0`, as_primary_hit `None`, avg `0.007179`, median `0.016386`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.069968`, as_primary `0`, as_primary_hit `None`, avg `0.033783`, median `0.045479`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.016599`, as_primary `80`, as_primary_hit `0.425`, avg `-0.005194`, median `-0.003446`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.026722`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.008838`, median `-0.005714`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.040298`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.005192`, median `-0.002583`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.074525`, as_primary `80`, as_primary_hit `0.6375`, avg `0.007179`, median `0.016386`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.097073`, as_primary `80`, as_primary_hit `0.7625`, avg `0.033783`, median `0.045479`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.015168`, as_primary `0`, as_primary_hit `None`, avg `-0.005194`, median `-0.003446`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.01935`, as_primary `0`, as_primary_hit `None`, avg `-0.008838`, median `-0.005714`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.027831`, as_primary `0`, as_primary_hit `None`, avg `-0.005192`, median `-0.002583`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.042136`, as_primary `0`, as_primary_hit `None`, avg `0.007179`, median `0.016386`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.06597`, as_primary `0`, as_primary_hit `None`, avg `0.033783`, median `0.045479`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.015748`, avg `0.00283`, median `0.005108`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.025679`, avg `-0.001374`, median `0.005583`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.036009`, avg `-0.00473`, median `0.004006`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.0478`, avg `0.009844`, median `0.010261`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.45`, primary_mae `0.053668`, avg `0.052197`, median `0.056479`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.016882`, avg `-0.007869`, median `-0.004922`
- 5d: sample `60`, primary_hit `0.5833`, primary_closer `0.35`, primary_mae `0.02707`, avg `-0.011327`, median `-0.007022`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.3667`, primary_mae `0.041727`, avg `-0.005347`, median `-0.006203`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.2833`, primary_mae `0.083433`, avg `0.00629`, median `0.018406`
- 60d: sample `60`, primary_hit `0.2667`, primary_closer `0.2833`, primary_mae `0.111541`, avg `0.027645`, median `0.043377`

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
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.013311`, avg `-0.006436`, median `-0.003986`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.02295`, avg `-0.008517`, median `-0.004042`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.045258`, avg `0.001567`, median `0.008886`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.084687`, avg `0.009988`, median `0.025964`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.101997`, avg `0.032605`, median `0.043377`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.019886`, avg `-0.003952`, median `-0.002206`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.030495`, avg `-0.00916`, median `-0.007554`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.035337`, avg `-0.011952`, median `-0.008446`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.425`, primary_mae `0.064363`, avg `0.004369`, median `0.015719`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.4`, primary_mae `0.09215`, avg `0.034961`, median `0.04627`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.013311, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.02295, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.035337, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.064363, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.09215, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0151, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016599, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.013311, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019092, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026722, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.02295, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027686, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040298, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.035337, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041287, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074525, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.064363, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_vs_secondary_accuracy_spread': -0.525, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.063447, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.097073, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.09215, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.01683`, avg `0.000512`, median `0.00311`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.022636`, avg `-0.001319`, median `0.005583`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.029491`, avg `-0.003463`, median `-0.004743`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.053584`, avg `0.019551`, median `0.017343`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.5`, primary_mae `0.033753`, avg `0.044293`, median `0.041509`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.015956`, avg `0.001926`, median `0.005108`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.026606`, avg `-0.000119`, median `0.006826`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.037036`, avg `-0.004031`, median `0.004006`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.051`, avg `0.013159`, median `0.017343`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.4375`, primary_mae `0.053146`, avg `0.049989`, median `0.056479`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.015207`, avg `-0.017511`, median `-0.014095`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.02765`, avg `-0.016353`, median `-0.010188`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.052953`, avg `0.001066`, median `0.012828`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.095569`, avg `0.017925`, median `0.039587`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.143281`, avg `0.071239`, median `0.114142`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.016599`, avg `-0.005194`, median `-0.003446`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3625`, primary_mae `0.026722`, avg `-0.008838`, median `-0.005714`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.35`, primary_mae `0.040298`, avg `-0.005192`, median `-0.002583`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3375`, primary_mae `0.074525`, avg `0.007179`, median `0.016386`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.325`, primary_mae `0.097073`, avg `0.033783`, median `0.045479`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.016599`, avg `-0.005194`, median `-0.003446`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3625`, primary_mae `0.026722`, avg `-0.008838`, median `-0.005714`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.35`, primary_mae `0.040298`, avg `-0.005192`, median `-0.002583`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3375`, primary_mae `0.074525`, avg `0.007179`, median `0.016386`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.325`, primary_mae `0.097073`, avg `0.033783`, median `0.045479`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.019886`, avg `-0.003952`, median `-0.002206`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.030495`, avg `-0.00916`, median `-0.007554`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.035337`, avg `-0.011952`, median `-0.008446`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.425`, primary_mae `0.064363`, avg `0.004369`, median `0.015719`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.4`, primary_mae `0.09215`, avg `0.034961`, median `0.04627`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.013311`, avg `-0.006436`, median `-0.003986`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.02295`, avg `-0.008517`, median `-0.004042`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.045258`, avg `0.001567`, median `0.008886`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.084687`, avg `0.009988`, median `0.025964`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.101997`, avg `0.032605`, median `0.043377`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.016599`, avg `-0.005194`, median `-0.003446`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3625`, primary_mae `0.026722`, avg `-0.008838`, median `-0.005714`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.35`, primary_mae `0.040298`, avg `-0.005192`, median `-0.002583`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3375`, primary_mae `0.074525`, avg `0.007179`, median `0.016386`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.325`, primary_mae `0.097073`, avg `0.033783`, median `0.045479`

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
