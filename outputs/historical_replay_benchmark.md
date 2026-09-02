# Historical Replay Benchmark

Generated at: `2026-09-02T23:33:40.374291+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
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
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.014997`
- secondary_mean_absolute_error: `0.013787`
- primary_error_advantage: `-0.00121`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.019645`
- secondary_mean_absolute_error: `0.016219`
- primary_error_advantage: `-0.003426`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.031149`
- secondary_mean_absolute_error: `0.028467`
- primary_error_advantage: `-0.002682`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.55`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.065472`
- secondary_mean_absolute_error: `0.043423`
- primary_error_advantage: `-0.022049`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.110793`
- secondary_mean_absolute_error: `0.076911`
- primary_error_advantage: `-0.033882`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.013372`, as_primary `0`, as_primary_hit `None`, avg `-6e-06`, median `0.000662`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.016242`, as_primary `0`, as_primary_hit `None`, avg `0.000143`, median `0.000818`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.02435`, as_primary `0`, as_primary_hit `None`, avg `0.000504`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.034633`, as_primary `0`, as_primary_hit `None`, avg `0.009612`, median `0.020147`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.069583`, as_primary `0`, as_primary_hit `None`, avg `0.026935`, median `0.049098`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.014638`, as_primary `0`, as_primary_hit `None`, avg `-6e-06`, median `0.000662`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.017067`, as_primary `0`, as_primary_hit `None`, avg `0.000143`, median `0.000818`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.030785`, as_primary `0`, as_primary_hit `None`, avg `0.000504`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.047356`, as_primary `0`, as_primary_hit `None`, avg `0.009612`, median `0.020147`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.077621`, as_primary `0`, as_primary_hit `None`, avg `0.026935`, median `0.049098`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.014997`, as_primary `80`, as_primary_hit `0.5375`, avg `-6e-06`, median `0.000662`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.019645`, as_primary `80`, as_primary_hit `0.55`, avg `0.000143`, median `0.000818`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.031149`, as_primary `80`, as_primary_hit `0.425`, avg `0.000504`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.065472`, as_primary `80`, as_primary_hit `0.6625`, avg `0.009612`, median `0.020147`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.110793`, as_primary `80`, as_primary_hit `0.675`, avg `0.026935`, median `0.049098`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.013082`, as_primary `0`, as_primary_hit `None`, avg `-6e-06`, median `0.000662`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.015984`, as_primary `0`, as_primary_hit `None`, avg `0.000143`, median `0.000818`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.023216`, as_primary `0`, as_primary_hit `None`, avg `0.000504`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.034548`, as_primary `0`, as_primary_hit `None`, avg `0.009612`, median `0.020147`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.069872`, as_primary `0`, as_primary_hit `None`, avg `0.026935`, median `0.049098`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.019469`, avg `-0.006736`, median `-0.005597`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.019233`, avg `-0.012013`, median `-0.012995`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.018233`, avg `-0.002862`, median `-0.006514`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.053462`, avg `0.016067`, median `0.024617`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.104828`, avg `0.041198`, median `0.052814`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.4`, primary_mae `0.013506`, avg `0.002238`, median `0.000755`
- 5d: sample `60`, primary_hit `0.4`, primary_closer `0.3833`, primary_mae `0.019782`, avg `0.004194`, median `0.002241`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.5`, primary_mae `0.035455`, avg `0.001626`, median `-0.007304`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.3167`, primary_mae `0.069476`, avg `0.007461`, median `0.019748`
- 60d: sample `60`, primary_hit `0.3333`, primary_closer `0.3833`, primary_mae `0.112782`, avg `0.02218`, median `0.049098`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.008687`, avg `-0.00386`, median `-0.004974`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.011411`, avg `-0.005064`, median `0.000725`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.02052`, avg `-0.00763`, median `-0.011447`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.061822`, avg `-0.00318`, median `0.0029`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.079568`, avg `0.022115`, median `0.031073`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.012638`, avg `0.003137`, median `0.002008`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.024257`, avg `0.008647`, median `0.009715`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.048337`, avg `-0.002534`, median `-0.009971`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.106591`, avg `0.00037`, median `0.027145`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.193711`, avg `-0.006737`, median `0.030627`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.019332`, avg `0.00035`, median `0.001949`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.021456`, avg `-0.001507`, median `-0.002115`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.02787`, avg `0.00609`, median `-0.000811`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.046738`, avg `0.020629`, median `0.027123`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.375`, primary_mae `0.084948`, avg `0.04618`, median `0.0618`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.008687, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.011411, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.02052, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.046738, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.079568, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013082, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014997, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.008687, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015984, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019645, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.011411, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023216, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031149, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.02052, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034548, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065472, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.046738, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069583, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.110793, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.079568, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.019373`, avg `-0.007732`, median `-5e-05`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.020571`, avg `-0.012817`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.023512`, avg `0.001642`, median `0.0036`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.060069`, avg `0.020806`, median `0.030181`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.124076`, avg `0.064394`, median `0.076071`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.017752`, avg `-0.007301`, median `-0.005597`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.018191`, avg `-0.012901`, median `-0.014548`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.020928`, avg `-0.000331`, median `-0.005954`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.057853`, avg `0.021263`, median `0.030181`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.112716`, avg `0.053034`, median `0.076071`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.011585`, avg `0.002381`, median `0.002008`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.023894`, avg `0.00947`, median `0.009715`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.049146`, avg `0.000419`, median `-0.00166`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.106731`, avg `0.001427`, median `0.023026`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.200203`, avg `-0.000736`, median `0.059521`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3875`, primary_mae `0.014997`, avg `-6e-06`, median `0.000662`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.019645`, avg `0.000143`, median `0.000818`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.031149`, avg `0.000504`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.35`, primary_mae `0.065472`, avg `0.009612`, median `0.020147`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.110793`, avg `0.026935`, median `0.049098`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3875`, primary_mae `0.014997`, avg `-6e-06`, median `0.000662`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.019645`, avg `0.000143`, median `0.000818`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.031149`, avg `0.000504`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.35`, primary_mae `0.065472`, avg `0.009612`, median `0.020147`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.110793`, avg `0.026935`, median `0.049098`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.014078`, avg `-0.005298`, median `-0.005059`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.015322`, avg `-0.008538`, median `-0.003439`
- 10d: sample `40`, primary_hit `0.7`, primary_closer `0.65`, primary_mae `0.019376`, avg `-0.005246`, median `-0.009483`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.057642`, avg `0.006443`, median `0.012243`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.425`, primary_mae `0.092198`, avg `0.031657`, median `0.041779`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.35`, primary_mae `0.0171`, avg `0.001279`, median `0.001949`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.4167`, primary_mae `0.022389`, avg `0.001878`, median `0.002122`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4667`, primary_mae `0.034693`, avg `0.003216`, median `-0.002446`
- 20d: sample `60`, primary_hit `0.2833`, primary_closer `0.35`, primary_mae `0.066689`, avg `0.013876`, median `0.027123`
- 60d: sample `60`, primary_hit `0.2833`, primary_closer `0.3667`, primary_mae `0.121202`, avg `0.028541`, median `0.054604`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4625`, primary_closer `0.3875`, primary_mae `0.014997`, avg `-6e-06`, median `0.000662`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.019645`, avg `0.000143`, median `0.000818`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.031149`, avg `0.000504`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.35`, primary_mae `0.065472`, avg `0.009612`, median `0.020147`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.110793`, avg `0.026935`, median `0.049098`

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
