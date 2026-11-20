# Historical Replay Benchmark

Generated at: `2026-11-20T20:25:34.390156+00:00`
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
- primary_closer_than_secondary_rate: `0.2375`
- primary_mean_absolute_error: `0.049077`
- secondary_mean_absolute_error: `0.030678`
- primary_error_advantage: `-0.018399`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.2125`
- primary_mean_absolute_error: `0.062929`
- secondary_mean_absolute_error: `0.034692`
- primary_error_advantage: `-0.028237`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.086042`
- secondary_mean_absolute_error: `0.049162`
- primary_error_advantage: `-0.03688`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.1625`
- primary_mean_absolute_error: `0.152446`
- secondary_mean_absolute_error: `0.073295`
- primary_error_advantage: `-0.079151`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.157429`
- secondary_mean_absolute_error: `0.105202`
- primary_error_advantage: `-0.052227`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.03239`, as_primary `0`, as_primary_hit `None`, avg `-0.001387`, median `0.010624`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.03696`, as_primary `0`, as_primary_hit `None`, avg `-0.00066`, median `0.012707`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.050354`, as_primary `0`, as_primary_hit `None`, avg `-0.001016`, median `0.014857`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.07267`, as_primary `0`, as_primary_hit `None`, avg `0.00017`, median `0.025541`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.104881`, as_primary `0`, as_primary_hit `None`, avg `0.026128`, median `0.049692`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.029517`, as_primary `0`, as_primary_hit `None`, avg `-0.001387`, median `0.010624`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.036099`, as_primary `0`, as_primary_hit `None`, avg `-0.00066`, median `0.012707`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.059457`, as_primary `0`, as_primary_hit `None`, avg `-0.001016`, median `0.014857`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.098543`, as_primary `0`, as_primary_hit `None`, avg `0.00017`, median `0.025541`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.132165`, as_primary `0`, as_primary_hit `None`, avg `0.026128`, median `0.049692`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.049077`, as_primary `80`, as_primary_hit `0.6125`, avg `-0.001387`, median `0.010624`
- 5d: sample `80`, direction_hit `0.3125`, path_mae `0.062929`, as_primary `80`, as_primary_hit `0.6875`, avg `-0.00066`, median `0.012707`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.086042`, as_primary `80`, as_primary_hit `0.5875`, avg `-0.001016`, median `0.014857`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.152446`, as_primary `80`, as_primary_hit `0.65`, avg `0.00017`, median `0.025541`
- 60d: sample `80`, direction_hit `0.4`, path_mae `0.157429`, as_primary `80`, as_primary_hit `0.6`, avg `0.026128`, median `0.049692`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.030678`, as_primary `0`, as_primary_hit `None`, avg `-0.001387`, median `0.010624`
- 5d: sample `80`, direction_hit `0.6875`, path_mae `0.034692`, as_primary `0`, as_primary_hit `None`, avg `-0.00066`, median `0.012707`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.049162`, as_primary `0`, as_primary_hit `None`, avg `-0.001016`, median `0.014857`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.073295`, as_primary `0`, as_primary_hit `None`, avg `0.00017`, median `0.025541`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.105202`, as_primary `0`, as_primary_hit `None`, avg `0.026128`, median `0.049692`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.2375`, primary_mae `0.049077`, avg `-0.001387`, median `0.010624`
- 5d: sample `80`, primary_hit `0.3125`, primary_closer `0.2125`, primary_mae `0.062929`, avg `-0.00066`, median `0.012707`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.25`, primary_mae `0.086042`, avg `-0.001016`, median `0.014857`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.1625`, primary_mae `0.152446`, avg `0.00017`, median `0.025541`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.157429`, avg `0.026128`, median `0.049692`

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
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.25`, primary_mae `0.054299`, avg `-0.004613`, median `0.0101`
- 5d: sample `60`, primary_hit `0.35`, primary_closer `0.2167`, primary_mae `0.07522`, avg `-0.004859`, median `0.011636`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.25`, primary_mae `0.095321`, avg `-0.00406`, median `0.012327`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.1833`, primary_mae `0.15995`, avg `-0.001908`, median `0.024723`
- 60d: sample `60`, primary_hit `0.4167`, primary_closer `0.3167`, primary_mae `0.191715`, avg `0.027311`, median `0.053364`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.2`, primary_mae `0.033409`, avg `0.008292`, median `0.012203`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.026055`, avg `0.011938`, median `0.013255`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.058205`, avg `0.008117`, median `0.018028`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.1`, primary_mae `0.129935`, avg `0.006403`, median `0.038015`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.054572`, avg `0.022578`, median `0.02645`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.033409, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.026055, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.058205, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.1, 'primary_mean_absolute_error': 0.129935, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.054572, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.2375, 'best_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029517, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049077, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.033409, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.2125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034692, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062929, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.026055, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049162, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.086042, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.058205, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.1625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07267, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.152446, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.1, 'primary_mean_absolute_error': 0.129935, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.104881, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.157429, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.054572, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.024442`, avg `-0.004738`, median `-0.003756`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.0178`, avg `-0.002973`, median `0.001059`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.050442`, avg `-0.018604`, median `-0.012935`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.113141`, avg `-0.046429`, median `-0.016283`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.058448`, avg `0.017696`, median `0.022528`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.1875`, primary_mae `0.030781`, avg `0.005474`, median `0.007815`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.026796`, avg `0.010912`, median `0.012731`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.055786`, avg `0.000535`, median `0.001876`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.124472`, avg `-0.007375`, median `0.024723`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.065431`, avg `0.032362`, median `0.059939`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.069709`, avg `-0.013577`, median `0.003156`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.1875`, primary_mae `0.111786`, avg `-0.016802`, median `0.001324`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.1875`, primary_mae `0.117107`, avg `0.000217`, median `0.019008`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.153497`, avg `0.02467`, median `0.04586`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.214124`, avg `0.036513`, median `0.095049`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.2375`, primary_mae `0.049077`, avg `-0.001387`, median `0.010624`
- 5d: sample `80`, primary_hit `0.3125`, primary_closer `0.2125`, primary_mae `0.062929`, avg `-0.00066`, median `0.012707`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.25`, primary_mae `0.086042`, avg `-0.001016`, median `0.014857`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.1625`, primary_mae `0.152446`, avg `0.00017`, median `0.025541`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.157429`, avg `0.026128`, median `0.049692`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.2375`, primary_mae `0.049077`, avg `-0.001387`, median `0.010624`
- 5d: sample `80`, primary_hit `0.3125`, primary_closer `0.2125`, primary_mae `0.062929`, avg `-0.00066`, median `0.012707`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.25`, primary_mae `0.086042`, avg `-0.001016`, median `0.014857`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.1625`, primary_mae `0.152446`, avg `0.00017`, median `0.025541`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.157429`, avg `0.026128`, median `0.049692`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.2`, primary_mae `0.030462`, avg `0.005151`, median `0.008011`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.024574`, avg `0.009668`, median `0.011636`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.049855`, avg `-0.002291`, median `-0.01006`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.1`, primary_mae `0.126354`, avg `5.1e-05`, median `0.024723`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.068787`, avg `0.030526`, median `0.059903`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.2333`, primary_mae `0.045109`, avg `0.000451`, median `0.010624`
- 5d: sample `60`, primary_hit `0.3`, primary_closer `0.2167`, primary_mae `0.054639`, avg `0.001444`, median `0.011636`
- 10d: sample `60`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.07619`, avg `0.000342`, median `0.014857`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.1333`, primary_mae `0.133919`, avg `0.006425`, median `0.028101`
- 60d: sample `60`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.111067`, avg `0.027034`, median `0.051113`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.2375`, primary_mae `0.049077`, avg `-0.001387`, median `0.010624`
- 5d: sample `80`, primary_hit `0.3125`, primary_closer `0.2125`, primary_mae `0.062929`, avg `-0.00066`, median `0.012707`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.25`, primary_mae `0.086042`, avg `-0.001016`, median `0.014857`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.1625`, primary_mae `0.152446`, avg `0.00017`, median `0.025541`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.157429`, avg `0.026128`, median `0.049692`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.2375`, primary_mae `0.049077`, avg `-0.001387`, median `0.010624`
- 5d: sample `80`, primary_hit `0.3125`, primary_closer `0.2125`, primary_mae `0.062929`, avg `-0.00066`, median `0.012707`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.25`, primary_mae `0.086042`, avg `-0.001016`, median `0.014857`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.1625`, primary_mae `0.152446`, avg `0.00017`, median `0.025541`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.157429`, avg `0.026128`, median `0.049692`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
