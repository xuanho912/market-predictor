# Historical Replay Benchmark

Generated at: `2026-08-04T04:36:05.974301+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.016262`
- secondary_mean_absolute_error: `0.015317`
- primary_error_advantage: `-0.000945`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.021516`
- secondary_mean_absolute_error: `0.01983`
- primary_error_advantage: `-0.001686`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.027073`
- secondary_mean_absolute_error: `0.023888`
- primary_error_advantage: `-0.003185`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.037079`
- secondary_mean_absolute_error: `0.031832`
- primary_error_advantage: `-0.005247`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.067631`
- secondary_mean_absolute_error: `0.063093`
- primary_error_advantage: `-0.004538`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.725`, path_mae `0.01457`, as_primary `0`, as_primary_hit `None`, avg `0.008454`, median `0.011156`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.019235`, as_primary `0`, as_primary_hit `None`, avg `0.010593`, median `0.010318`
- 10d: sample `80`, direction_hit `0.8`, path_mae `0.023335`, as_primary `0`, as_primary_hit `None`, avg `0.020115`, median `0.021019`
- 20d: sample `80`, direction_hit `0.8875`, path_mae `0.024975`, as_primary `0`, as_primary_hit `None`, avg `0.034093`, median `0.030926`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.058118`, as_primary `0`, as_primary_hit `None`, avg `0.047153`, median `0.069591`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.725`, path_mae `0.015869`, as_primary `40`, as_primary_hit `0.775`, avg `0.008454`, median `0.011156`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.021227`, as_primary `40`, as_primary_hit `0.775`, avg `0.010593`, median `0.010318`
- 10d: sample `80`, direction_hit `0.8`, path_mae `0.030591`, as_primary `40`, as_primary_hit `0.85`, avg `0.020115`, median `0.021019`
- 20d: sample `80`, direction_hit `0.8875`, path_mae `0.036822`, as_primary `40`, as_primary_hit `0.925`, avg `0.034093`, median `0.030926`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.070729`, as_primary `40`, as_primary_hit `0.95`, avg `0.047153`, median `0.069591`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.275`, path_mae `0.016632`, as_primary `40`, as_primary_hit `0.675`, avg `0.008454`, median `0.011156`
- 5d: sample `80`, direction_hit `0.3125`, path_mae `0.02188`, as_primary `40`, as_primary_hit `0.6`, avg `0.010593`, median `0.010318`
- 10d: sample `80`, direction_hit `0.2`, path_mae `0.025828`, as_primary `40`, as_primary_hit `0.75`, avg `0.020115`, median `0.021019`
- 20d: sample `80`, direction_hit `0.1125`, path_mae `0.038876`, as_primary `40`, as_primary_hit `0.85`, avg `0.034093`, median `0.030926`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.071523`, as_primary `40`, as_primary_hit `0.575`, avg `0.047153`, median `0.069591`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.725`, path_mae `0.014687`, as_primary `0`, as_primary_hit `None`, avg `0.008454`, median `0.011156`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.018805`, as_primary `0`, as_primary_hit `None`, avg `0.010593`, median `0.010318`
- 10d: sample `80`, direction_hit `0.8`, path_mae `0.020521`, as_primary `0`, as_primary_hit `None`, avg `0.020115`, median `0.021019`
- 20d: sample `80`, direction_hit `0.8875`, path_mae `0.023488`, as_primary `0`, as_primary_hit `None`, avg `0.034093`, median `0.030926`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.058074`, as_primary `0`, as_primary_hit `None`, avg `0.047153`, median `0.069591`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6333`, primary_closer `0.5167`, primary_mae `0.01432`, avg `0.007296`, median `0.009174`
- 5d: sample `60`, primary_hit `0.6667`, primary_closer `0.45`, primary_mae `0.021177`, avg `0.009214`, median `0.010922`
- 10d: sample `60`, primary_hit `0.6667`, primary_closer `0.4`, primary_mae `0.026509`, avg `0.01788`, median `0.018762`
- 20d: sample `60`, primary_hit `0.6667`, primary_closer `0.45`, primary_mae `0.034282`, avg `0.031446`, median `0.028861`
- 60d: sample `60`, primary_hit `0.7833`, primary_closer `0.5`, primary_mae `0.052653`, avg `0.056445`, median `0.07206`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.02209`, avg `0.011931`, median `0.01429`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.022535`, avg `0.01473`, median `0.008083`
- 10d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.028767`, avg `0.02682`, median `0.031316`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.045471`, avg `0.042034`, median `0.043617`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.112564`, avg `0.019279`, median `0.064428`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.5`, primary_mae `0.013656`, avg `0.009021`, median `0.013734`
- 5d: sample `20`, primary_hit `0.8`, primary_closer `0.5`, primary_mae `0.017439`, avg `0.014578`, median `0.017715`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.028206`, avg `0.019694`, median `0.018985`
- 20d: sample `20`, primary_hit `0.9`, primary_closer `0.5`, primary_mae `0.03906`, avg `0.045067`, median `0.050926`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.65`, primary_mae `0.034064`, avg `0.089569`, median `0.099615`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.4833`, primary_mae `0.017131`, avg `0.008265`, median `0.007355`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.4667`, primary_mae `0.022875`, avg `0.009264`, median `0.00793`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.3833`, primary_mae `0.026696`, avg `0.020256`, median `0.02156`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.3833`, primary_mae `0.036419`, avg `0.030435`, median `0.03011`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.4167`, primary_mae `0.07882`, avg `0.033015`, median `0.059624`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.013656, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.017439, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.026696, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.036419, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.034064, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01457, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016632, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.013656, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018805, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02188, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.017439, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020521, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030591, 'direction_hit_rate': 0.8}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.026696, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023488, 'direction_hit_rate': 0.8875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038876, 'direction_hit_rate': 0.1125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.036419, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058074, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071523, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.034064, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.020257`, avg `-0.000482`, median `0.005307`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.125`, primary_mae `0.0206`, avg `0.005892`, median `0.008828`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.03778`, avg `0.005166`, median `0.006274`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.039368`, avg `0.043557`, median `0.050926`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.044924`, avg `0.078417`, median `0.093471`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.015267`, avg `0.006854`, median `0.012449`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.018528`, avg `0.012907`, median `0.012047`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.028357`, avg `0.016705`, median `0.017428`
- 20d: sample `16`, primary_hit `1.0`, primary_closer `0.5625`, primary_mae `0.033034`, avg `0.050551`, median `0.058396`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.625`, primary_mae `0.035331`, avg `0.08783`, median `0.098383`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.022519`, avg `0.013642`, median `0.016544`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.022043`, avg `0.014687`, median `0.008083`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.023465`, avg `0.029506`, median `0.031316`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.375`, primary_mae `0.043393`, avg `0.039447`, median `0.047417`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.108264`, avg `0.017291`, median `0.071057`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4875`, primary_mae `0.016262`, avg `0.008454`, median `0.011156`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.021516`, avg `0.010593`, median `0.010318`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.027073`, avg `0.020115`, median `0.021019`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.037079`, avg `0.034093`, median `0.030926`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.475`, primary_mae `0.067631`, avg `0.047153`, median `0.069591`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4875`, primary_mae `0.016262`, avg `0.008454`, median `0.011156`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.021516`, avg `0.010593`, median `0.010318`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.027073`, avg `0.020115`, median `0.021019`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.037079`, avg `0.034093`, median `0.030926`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.475`, primary_mae `0.067631`, avg `0.047153`, median `0.069591`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.775`, primary_closer `0.525`, primary_mae `0.00969`, avg `0.007489`, median `0.009174`
- 5d: sample `40`, primary_hit `0.775`, primary_closer `0.45`, primary_mae `0.014908`, avg `0.011771`, median `0.011847`
- 10d: sample `40`, primary_hit `0.85`, primary_closer `0.4`, primary_mae `0.019742`, avg `0.01729`, median `0.017418`
- 20d: sample `40`, primary_hit `0.925`, primary_closer `0.4`, primary_mae `0.028385`, avg `0.036834`, median `0.032326`
- 60d: sample `40`, primary_hit `0.95`, primary_closer `0.525`, primary_mae `0.031258`, avg `0.073206`, median `0.083793`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.02209`, avg `0.011931`, median `0.01429`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.022535`, avg `0.01473`, median `0.008083`
- 10d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.028767`, avg `0.02682`, median `0.031316`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.045471`, avg `0.042034`, median `0.043617`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.112564`, avg `0.019279`, median `0.064428`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4875`, primary_mae `0.016262`, avg `0.008454`, median `0.011156`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.021516`, avg `0.010593`, median `0.010318`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.027073`, avg `0.020115`, median `0.021019`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.037079`, avg `0.034093`, median `0.030926`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.475`, primary_mae `0.067631`, avg `0.047153`, median `0.069591`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4875`, primary_mae `0.016262`, avg `0.008454`, median `0.011156`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.475`, primary_mae `0.021516`, avg `0.010593`, median `0.010318`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.027073`, avg `0.020115`, median `0.021019`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4125`, primary_mae `0.037079`, avg `0.034093`, median `0.030926`
- 60d: sample `80`, primary_hit `0.6875`, primary_closer `0.475`, primary_mae `0.067631`, avg `0.047153`, median `0.069591`

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
