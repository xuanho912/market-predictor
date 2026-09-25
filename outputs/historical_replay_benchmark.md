# Historical Replay Benchmark

Generated at: `2026-09-25T17:15:46.858141+00:00`
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
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.018553`
- secondary_mean_absolute_error: `0.015887`
- primary_error_advantage: `-0.002666`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.025811`
- secondary_mean_absolute_error: `0.020047`
- primary_error_advantage: `-0.005764`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.038961`
- secondary_mean_absolute_error: `0.028889`
- primary_error_advantage: `-0.010072`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.0735`
- secondary_mean_absolute_error: `0.047568`
- primary_error_advantage: `-0.025932`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2125`
- secondary_hit_rate: `0.7875`
- primary_vs_secondary_accuracy_spread: `-0.575`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.102003`
- secondary_mean_absolute_error: `0.069911`
- primary_error_advantage: `-0.032092`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015499`, as_primary `0`, as_primary_hit `None`, avg `-0.006056`, median `-0.003835`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.018813`, as_primary `0`, as_primary_hit `None`, avg `-0.010608`, median `-0.007554`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.026956`, as_primary `0`, as_primary_hit `None`, avg `-0.008503`, median `-0.005392`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.043243`, as_primary `0`, as_primary_hit `None`, avg `0.002903`, median `0.013951`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.064479`, as_primary `0`, as_primary_hit `None`, avg `0.03742`, median `0.052147`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015888`, as_primary `0`, as_primary_hit `None`, avg `-0.006056`, median `-0.003835`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.021`, as_primary `0`, as_primary_hit `None`, avg `-0.010608`, median `-0.007554`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.034013`, as_primary `0`, as_primary_hit `None`, avg `-0.008503`, median `-0.005392`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.063668`, as_primary `0`, as_primary_hit `None`, avg `0.002903`, median `0.013951`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.068605`, as_primary `0`, as_primary_hit `None`, avg `0.03742`, median `0.052147`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.018553`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.006056`, median `-0.003835`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.025811`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.010608`, median `-0.007554`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.038961`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.008503`, median `-0.005392`
- 20d: sample `80`, direction_hit `0.4125`, path_mae `0.0735`, as_primary `80`, as_primary_hit `0.5875`, avg `0.002903`, median `0.013951`
- 60d: sample `80`, direction_hit `0.2125`, path_mae `0.102003`, as_primary `80`, as_primary_hit `0.7875`, avg `0.03742`, median `0.052147`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015302`, as_primary `0`, as_primary_hit `None`, avg `-0.006056`, median `-0.003835`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.018974`, as_primary `0`, as_primary_hit `None`, avg `-0.010608`, median `-0.007554`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.026966`, as_primary `0`, as_primary_hit `None`, avg `-0.008503`, median `-0.005392`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.043023`, as_primary `0`, as_primary_hit `None`, avg `0.002903`, median `0.013951`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.065726`, as_primary `0`, as_primary_hit `None`, avg `0.03742`, median `0.052147`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.026028`, avg `-0.00873`, median `-0.010508`
- 5d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.03673`, avg `-0.015526`, median `-0.013247`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.036178`, avg `-0.017661`, median `-0.015452`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.082086`, avg `5.5e-05`, median `0.015746`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.145601`, avg `0.037365`, median `0.054785`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.3833`, primary_mae `0.016061`, avg `-0.005165`, median `-0.003662`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.3833`, primary_mae `0.022171`, avg `-0.008969`, median `-0.003597`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.3333`, primary_mae `0.039889`, avg `-0.00545`, median `0.004006`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.2833`, primary_mae `0.070638`, avg `0.003853`, median `0.012654`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.2667`, primary_mae `0.087471`, avg `0.037438`, median `0.052022`

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
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.3833`, primary_mae `0.016061`, avg `-0.005165`, median `-0.003662`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.3833`, primary_mae `0.022171`, avg `-0.008969`, median `-0.003597`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.3333`, primary_mae `0.039889`, avg `-0.00545`, median `0.004006`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.2833`, primary_mae `0.070638`, avg `0.003853`, median `0.012654`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.2667`, primary_mae `0.087471`, avg `0.037438`, median `0.052022`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.026028`, avg `-0.00873`, median `-0.010508`
- 5d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.03673`, avg `-0.015526`, median `-0.013247`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.036178`, avg `-0.017661`, median `-0.015452`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.082086`, avg `5.5e-05`, median `0.015746`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.145601`, avg `0.037365`, median `0.054785`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.016061, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.022171, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.036178, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.2833, 'primary_mean_absolute_error': 0.070638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.087471, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015302, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018553, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.016061, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018813, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025811, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.022171, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026956, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038961, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.036178, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043023, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0735, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.2833, 'primary_mean_absolute_error': 0.070638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2125, 'secondary_hit_rate': 0.7875, 'primary_vs_secondary_accuracy_spread': -0.575, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064479, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.102003, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.087471, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.030755`, avg `-0.003118`, median `0.005307`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.044885`, avg `-0.007215`, median `0.00651`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.125`, primary_mae `0.043846`, avg `-0.006535`, median `-0.012632`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.104389`, avg `0.016651`, median `0.025462`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.165653`, avg `0.055371`, median `0.061567`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.022706`, avg `-0.012608`, median `-0.022443`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.035351`, avg `-0.017744`, median `-0.020235`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.035885`, avg `-0.018709`, median `-0.015452`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.08481`, avg `0.001613`, median `0.019252`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.141576`, avg `0.031282`, median `0.054785`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.022002`, avg `-0.016439`, median `-0.012143`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.031727`, avg `-0.015468`, median `-0.012686`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.057198`, avg `0.002944`, median `0.013888`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.105122`, avg `0.016793`, median `0.034922`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.136012`, avg `0.067054`, median `0.114142`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.018553`, avg `-0.006056`, median `-0.003835`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.025811`, avg `-0.010608`, median `-0.007554`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.35`, primary_mae `0.038961`, avg `-0.008503`, median `-0.005392`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.3`, primary_mae `0.0735`, avg `0.002903`, median `0.013951`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.2625`, primary_mae `0.102003`, avg `0.03742`, median `0.052147`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.018553`, avg `-0.006056`, median `-0.003835`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.025811`, avg `-0.010608`, median `-0.007554`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.35`, primary_mae `0.038961`, avg `-0.008503`, median `-0.005392`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.3`, primary_mae `0.0735`, avg `0.002903`, median `0.013951`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.2625`, primary_mae `0.102003`, avg `0.03742`, median `0.052147`

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
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.4`, primary_mae `0.018553`, avg `-0.006056`, median `-0.003835`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.025811`, avg `-0.010608`, median `-0.007554`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.35`, primary_mae `0.038961`, avg `-0.008503`, median `-0.005392`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.3`, primary_mae `0.0735`, avg `0.002903`, median `0.013951`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.2625`, primary_mae `0.102003`, avg `0.03742`, median `0.052147`

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
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.4333`, primary_mae `0.017317`, avg `-0.00167`, median `0.001302`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.3667`, primary_mae `0.024928`, avg `-0.006834`, median `-0.000371`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.3`, primary_mae `0.035399`, avg `-0.008309`, median `-0.002583`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.2667`, primary_mae `0.068012`, avg `0.004579`, median `0.015082`
- 60d: sample `60`, primary_hit `0.1833`, primary_closer `0.25`, primary_mae `0.092548`, avg `0.03805`, median `0.04627`

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
