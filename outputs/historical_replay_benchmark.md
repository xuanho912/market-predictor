# Historical Replay Benchmark

Generated at: `2026-09-18T01:16:41.104911+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'low', 'reasons': [], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.016254`
- secondary_mean_absolute_error: `0.016569`
- primary_error_advantage: `0.000315`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.020753`
- secondary_mean_absolute_error: `0.021678`
- primary_error_advantage: `0.000925`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.026991`
- secondary_mean_absolute_error: `0.029628`
- primary_error_advantage: `0.002637`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6333`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.048527`
- secondary_mean_absolute_error: `0.047941`
- primary_error_advantage: `-0.000586`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `-0.6`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.067632`
- secondary_mean_absolute_error: `0.060721`
- primary_error_advantage: `-0.006911`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.015613`, as_primary `0`, as_primary_hit `None`, avg `0.002328`, median `0.005428`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.019676`, as_primary `0`, as_primary_hit `None`, avg `0.003238`, median `0.00651`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.024587`, as_primary `0`, as_primary_hit `None`, avg `0.010177`, median `0.009599`
- 20d: sample `80`, direction_hit `0.8125`, path_mae `0.033611`, as_primary `0`, as_primary_hit `None`, avg `0.032109`, median `0.034552`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.055623`, as_primary `0`, as_primary_hit `None`, avg `0.069723`, median `0.089556`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.016569`, as_primary `0`, as_primary_hit `None`, avg `0.002328`, median `0.005428`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.021678`, as_primary `0`, as_primary_hit `None`, avg `0.003238`, median `0.00651`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.029628`, as_primary `0`, as_primary_hit `None`, avg `0.010177`, median `0.009599`
- 20d: sample `80`, direction_hit `0.8125`, path_mae `0.047941`, as_primary `0`, as_primary_hit `None`, avg `0.032109`, median `0.034552`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.060721`, as_primary `0`, as_primary_hit `None`, avg `0.069723`, median `0.089556`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.016254`, as_primary `80`, as_primary_hit `0.5875`, avg `0.002328`, median `0.005428`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.020753`, as_primary `80`, as_primary_hit `0.5625`, avg `0.003238`, median `0.00651`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.026991`, as_primary `80`, as_primary_hit `0.6625`, avg `0.010177`, median `0.009599`
- 20d: sample `80`, direction_hit `0.1875`, path_mae `0.048527`, as_primary `80`, as_primary_hit `0.8125`, avg `0.032109`, median `0.034552`
- 60d: sample `80`, direction_hit `0.2`, path_mae `0.067632`, as_primary `80`, as_primary_hit `0.8`, avg `0.069723`, median `0.089556`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.015363`, as_primary `0`, as_primary_hit `None`, avg `0.002328`, median `0.005428`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.019061`, as_primary `0`, as_primary_hit `None`, avg `0.003238`, median `0.00651`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.023284`, as_primary `0`, as_primary_hit `None`, avg `0.010177`, median `0.009599`
- 20d: sample `80`, direction_hit `0.8125`, path_mae `0.031415`, as_primary `0`, as_primary_hit `None`, avg `0.032109`, median `0.034552`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.054803`, as_primary `0`, as_primary_hit `None`, avg `0.069723`, median `0.089556`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.35`, primary_closer `0.5833`, primary_mae `0.013798`, avg `0.005752`, median `0.008122`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.5333`, primary_mae `0.018626`, avg `0.007268`, median `0.009885`
- 10d: sample `60`, primary_hit `0.3`, primary_closer `0.6333`, primary_mae `0.021008`, avg `0.013729`, median `0.011325`
- 20d: sample `60`, primary_hit `0.1333`, primary_closer `0.4833`, primary_mae `0.04183`, avg `0.037694`, median `0.034552`
- 60d: sample `60`, primary_hit `0.1667`, primary_closer `0.4167`, primary_mae `0.052927`, avg `0.079898`, median `0.091366`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.023623`, avg `-0.007944`, median `-0.005289`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.027133`, avg `-0.008851`, median `-0.009536`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.044939`, avg `-0.000479`, median `0.002203`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.068618`, avg `0.015353`, median `0.032716`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.111746`, avg `0.039197`, median `0.078066`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.01112`, avg `0.001893`, median `0.002973`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.014462`, avg `0.001753`, median `0.004536`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.6`, primary_mae `0.011221`, avg `0.003662`, median `0.006274`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.35`, primary_mae `0.035732`, avg `0.031684`, median `0.036446`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.3`, primary_mae `0.047306`, avg `0.075863`, median `0.077578`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.023623`, avg `-0.007944`, median `-0.005289`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.027133`, avg `-0.008851`, median `-0.009536`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.044939`, avg `-0.000479`, median `0.002203`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.068618`, avg `0.015353`, median `0.032716`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.111746`, avg `0.039197`, median `0.078066`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.325`, primary_closer `0.575`, primary_mae `0.015137`, avg `0.007681`, median `0.012428`
- 5d: sample `40`, primary_hit `0.35`, primary_closer `0.575`, primary_mae `0.020708`, avg `0.010026`, median `0.012686`
- 10d: sample `40`, primary_hit `0.325`, primary_closer `0.65`, primary_mae `0.025902`, avg `0.018763`, median `0.019373`
- 20d: sample `40`, primary_hit `0.15`, primary_closer `0.55`, primary_mae `0.044878`, avg `0.040699`, median `0.034552`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.475`, primary_mae `0.055738`, avg `0.081916`, median `0.099615`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.01112, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014462, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.011221, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.035732, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047306, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015363, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016569, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.01112, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019061, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021678, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.014462, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023284, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029628, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.011221, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031415, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048527, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.035732, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': -0.6, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054803, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067632, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047306, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.015208`, avg `0.009676`, median `0.010967`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.025502`, avg `0.004274`, median `0.012817`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.032103`, avg `0.018545`, median `0.003835`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.75`, primary_mae `0.031509`, avg `0.030206`, median `0.015844`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.060033`, avg `0.058792`, median `0.023533`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.625`, primary_mae `0.016103`, avg `0.00778`, median `0.013091`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.023426`, avg `0.011396`, median `0.012817`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.034161`, avg `0.023393`, median `0.024578`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.5625`, primary_mae `0.050204`, avg `0.049219`, median `0.034279`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.078568`, avg `0.082198`, median `0.091536`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.022694`, avg `-0.006539`, median `-0.005289`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.025747`, avg `-0.008232`, median `-0.009536`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.042846`, avg `-0.001877`, median `-0.00147`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.062886`, avg `0.009019`, median `0.021827`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.109623`, avg `0.040604`, median `0.078066`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.5375`, primary_mae `0.016254`, avg `0.002328`, median `0.005428`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.525`, primary_mae `0.020753`, avg `0.003238`, median `0.00651`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.575`, primary_mae `0.026991`, avg `0.010177`, median `0.009599`
- 20d: sample `80`, primary_hit `0.1875`, primary_closer `0.4625`, primary_mae `0.048527`, avg `0.032109`, median `0.034552`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.067632`, avg `0.069723`, median `0.089556`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.5375`, primary_mae `0.016254`, avg `0.002328`, median `0.005428`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.525`, primary_mae `0.020753`, avg `0.003238`, median `0.00651`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.575`, primary_mae `0.026991`, avg `0.010177`, median `0.009599`
- 20d: sample `80`, primary_hit `0.1875`, primary_closer `0.4625`, primary_mae `0.048527`, avg `0.032109`, median `0.034552`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.067632`, avg `0.069723`, median `0.089556`

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
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.5375`, primary_mae `0.016254`, avg `0.002328`, median `0.005428`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.525`, primary_mae `0.020753`, avg `0.003238`, median `0.00651`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.575`, primary_mae `0.026991`, avg `0.010177`, median `0.009599`
- 20d: sample `80`, primary_hit `0.1875`, primary_closer `0.4625`, primary_mae `0.048527`, avg `0.032109`, median `0.034552`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.067632`, avg `0.069723`, median `0.089556`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.5375`, primary_mae `0.016254`, avg `0.002328`, median `0.005428`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.525`, primary_mae `0.020753`, avg `0.003238`, median `0.00651`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.575`, primary_mae `0.026991`, avg `0.010177`, median `0.009599`
- 20d: sample `80`, primary_hit `0.1875`, primary_closer `0.4625`, primary_mae `0.048527`, avg `0.032109`, median `0.034552`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.067632`, avg `0.069723`, median `0.089556`

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
