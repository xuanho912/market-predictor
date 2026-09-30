# Historical Replay Benchmark

Generated at: `2026-09-30T10:02:46.130602+00:00`
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
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.01777`
- secondary_mean_absolute_error: `0.014775`
- primary_error_advantage: `-0.002995`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.023806`
- secondary_mean_absolute_error: `0.018713`
- primary_error_advantage: `-0.005093`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.03596`
- secondary_mean_absolute_error: `0.026015`
- primary_error_advantage: `-0.009945`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.071338`
- secondary_mean_absolute_error: `0.048366`
- primary_error_advantage: `-0.022972`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.15`
- secondary_hit_rate: `0.85`
- primary_vs_secondary_accuracy_spread: `-0.7`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.089182`
- secondary_mean_absolute_error: `0.058601`
- primary_error_advantage: `-0.030581`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.015357`, as_primary `0`, as_primary_hit `None`, avg `-0.003963`, median `-0.003098`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.018257`, as_primary `0`, as_primary_hit `None`, avg `-0.008273`, median `-0.004447`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.025576`, as_primary `0`, as_primary_hit `None`, avg `-0.003842`, median `0.001002`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.040232`, as_primary `0`, as_primary_hit `None`, avg `0.010828`, median `0.016235`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.055062`, as_primary `0`, as_primary_hit `None`, avg `0.057016`, median `0.073912`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.014886`, as_primary `0`, as_primary_hit `None`, avg `-0.003963`, median `-0.003098`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.020144`, as_primary `0`, as_primary_hit `None`, avg `-0.008273`, median `-0.004447`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.030515`, as_primary `0`, as_primary_hit `None`, avg `-0.003842`, median `0.001002`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.060401`, as_primary `0`, as_primary_hit `None`, avg `0.010828`, median `0.016235`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.06281`, as_primary `0`, as_primary_hit `None`, avg `0.057016`, median `0.073912`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.01777`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.003963`, median `-0.003098`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.023806`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.008273`, median `-0.004447`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.03596`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.003842`, median `0.001002`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.071338`, as_primary `80`, as_primary_hit `0.6125`, avg `0.010828`, median `0.016235`
- 60d: sample `80`, direction_hit `0.15`, path_mae `0.089182`, as_primary `80`, as_primary_hit `0.85`, avg `0.057016`, median `0.073912`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.014883`, as_primary `0`, as_primary_hit `None`, avg `-0.003963`, median `-0.003098`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.017882`, as_primary `0`, as_primary_hit `None`, avg `-0.008273`, median `-0.004447`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.025098`, as_primary `0`, as_primary_hit `None`, avg `-0.003842`, median `0.001002`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.040022`, as_primary `0`, as_primary_hit `None`, avg `0.010828`, median `0.016235`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.056648`, as_primary `0`, as_primary_hit `None`, avg `0.057016`, median `0.073912`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.01777`, avg `-0.003963`, median `-0.003098`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.023806`, avg `-0.008273`, median `-0.004447`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.35`, primary_mae `0.03596`, avg `-0.003842`, median `0.001002`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.071338`, avg `0.010828`, median `0.016235`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.275`, primary_mae `0.089182`, avg `0.057016`, median `0.073912`

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
- 3d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.016415`, avg `-0.012655`, median `-0.010989`
- 5d: sample `20`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.020675`, avg `-0.016044`, median `-0.015571`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.039819`, avg `-0.002773`, median `-0.003925`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.082029`, avg `0.009823`, median `-0.003631`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.3`, primary_mae `0.063194`, avg `0.087142`, median `0.115176`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.45`, primary_mae `0.018222`, avg `-0.001066`, median `0.001753`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.3833`, primary_mae `0.024849`, avg `-0.005683`, median `0.000695`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.3167`, primary_mae `0.034674`, avg `-0.004199`, median `0.002711`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.3`, primary_mae `0.067775`, avg `0.011164`, median `0.018008`
- 60d: sample `60`, primary_hit `0.1667`, primary_closer `0.2667`, primary_mae `0.097845`, avg `0.046974`, median `0.058305`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.016415, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.020675, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.034674, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.067775, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.063194, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014883, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01777, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.016415, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017882, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023806, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.020675, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025098, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03596, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.034674, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040022, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071338, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.067775, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.15, 'secondary_hit_rate': 0.85, 'primary_vs_secondary_accuracy_spread': -0.7, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055062, 'direction_hit_rate': 0.85}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.089182, 'direction_hit_rate': 0.15}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.063194, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.027999`, avg `-0.003446`, median `0.005307`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.038725`, avg `-0.006543`, median `0.00651`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.046158`, avg `-0.008101`, median `-0.012632`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.105682`, avg `0.018437`, median `0.032607`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.160215`, avg `0.062084`, median `0.086267`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.023286`, avg `-0.008468`, median `-0.005846`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.032371`, avg `-0.014095`, median `-0.013247`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.046103`, avg `-0.010183`, median `-0.008724`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.090409`, avg `0.007705`, median `0.019252`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.151867`, avg `0.051698`, median `0.086104`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.016379`, avg `-0.013495`, median `-0.012143`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.022682`, avg `-0.014876`, median `-0.013338`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.046092`, avg `0.001197`, median `0.012828`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.095355`, avg `0.022728`, median `0.039587`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.066375`, avg `0.08268`, median `0.115176`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.01777`, avg `-0.003963`, median `-0.003098`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.023806`, avg `-0.008273`, median `-0.004447`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.35`, primary_mae `0.03596`, avg `-0.003842`, median `0.001002`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.071338`, avg `0.010828`, median `0.016235`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.275`, primary_mae `0.089182`, avg `0.057016`, median `0.073912`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.01777`, avg `-0.003963`, median `-0.003098`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.023806`, avg `-0.008273`, median `-0.004447`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.35`, primary_mae `0.03596`, avg `-0.003842`, median `0.001002`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.071338`, avg `0.010828`, median `0.016235`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.275`, primary_mae `0.089182`, avg `0.057016`, median `0.073912`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.021229`, avg `-0.001186`, median `0.002181`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.029763`, avg `-0.006329`, median `-0.002346`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.3`, primary_mae `0.039701`, avg `-0.008901`, median `-0.000315`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.065913`, avg `0.006182`, median `0.015082`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.325`, primary_mae `0.099984`, avg `0.050801`, median `0.062563`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.01431`, avg `-0.006741`, median `-0.007522`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.017848`, avg `-0.010218`, median `-0.006281`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.03222`, avg `0.001217`, median `0.006069`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.2`, primary_mae `0.076764`, avg `0.015475`, median `0.028292`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.225`, primary_mae `0.078379`, avg `0.063231`, median `0.075566`

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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4`, primary_mae `0.017757`, avg `-0.006228`, median `-0.005572`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.3667`, primary_mae `0.023181`, avg `-0.010573`, median `-0.007462`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.3667`, primary_mae `0.035944`, avg `-0.003546`, median `-0.000315`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.2333`, primary_mae `0.079185`, avg `0.011157`, median `0.019252`
- 60d: sample `60`, primary_hit `0.15`, primary_closer `0.2167`, primary_mae `0.10102`, avg `0.058622`, median `0.075566`

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
