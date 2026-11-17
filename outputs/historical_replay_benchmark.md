# Historical Replay Benchmark

Generated at: `2026-11-17T20:58:42.533287+00:00`
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
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.02389`
- secondary_mean_absolute_error: `0.020587`
- primary_error_advantage: `-0.003303`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.026005`
- secondary_mean_absolute_error: `0.022073`
- primary_error_advantage: `-0.003932`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.034662`
- secondary_mean_absolute_error: `0.029252`
- primary_error_advantage: `-0.00541`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.056396`
- secondary_mean_absolute_error: `0.03847`
- primary_error_advantage: `-0.017926`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.071647`
- secondary_mean_absolute_error: `0.069414`
- primary_error_advantage: `-0.002233`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.021197`, as_primary `0`, as_primary_hit `None`, avg `0.006423`, median `0.008272`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.022732`, as_primary `0`, as_primary_hit `None`, avg `0.010781`, median `0.010702`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.030023`, as_primary `0`, as_primary_hit `None`, avg `0.021136`, median `0.015054`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.041881`, as_primary `0`, as_primary_hit `None`, avg `0.031709`, median `0.03694`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.072456`, as_primary `0`, as_primary_hit `None`, avg `0.048638`, median `0.053364`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.021358`, as_primary `0`, as_primary_hit `None`, avg `0.006423`, median `0.008272`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.023388`, as_primary `0`, as_primary_hit `None`, avg `0.010781`, median `0.010702`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.03311`, as_primary `0`, as_primary_hit `None`, avg `0.021136`, median `0.015054`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.061279`, as_primary `0`, as_primary_hit `None`, avg `0.031709`, median `0.03694`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.084386`, as_primary `0`, as_primary_hit `None`, avg `0.048638`, median `0.053364`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.02389`, as_primary `80`, as_primary_hit `0.5875`, avg `0.006423`, median `0.008272`
- 5d: sample `80`, direction_hit `0.325`, path_mae `0.026005`, as_primary `80`, as_primary_hit `0.675`, avg `0.010781`, median `0.010702`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.034662`, as_primary `80`, as_primary_hit `0.675`, avg `0.021136`, median `0.015054`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.056396`, as_primary `80`, as_primary_hit `0.725`, avg `0.031709`, median `0.03694`
- 60d: sample `80`, direction_hit `0.3875`, path_mae `0.071647`, as_primary `80`, as_primary_hit `0.6125`, avg `0.048638`, median `0.053364`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.020587`, as_primary `0`, as_primary_hit `None`, avg `0.006423`, median `0.008272`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.022073`, as_primary `0`, as_primary_hit `None`, avg `0.010781`, median `0.010702`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.029252`, as_primary `0`, as_primary_hit `None`, avg `0.021136`, median `0.015054`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.03847`, as_primary `0`, as_primary_hit `None`, avg `0.031709`, median `0.03694`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.069414`, as_primary `0`, as_primary_hit `None`, avg `0.048638`, median `0.053364`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.375`, primary_mae `0.02389`, avg `0.006423`, median `0.008272`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.026005`, avg `0.010781`, median `0.010702`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4375`, primary_mae `0.034662`, avg `0.021136`, median `0.015054`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.056396`, avg `0.031709`, median `0.03694`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.071647`, avg `0.048638`, median `0.053364`

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
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.033083`, avg `-0.001677`, median `0.001708`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.039906`, avg `0.01292`, median `0.017911`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.040119`, avg `0.030027`, median `0.024519`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.08563`, avg `0.017067`, median `0.027635`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.090317`, avg `0.014082`, median `-0.014177`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.3667`, primary_mae `0.020826`, avg `0.009124`, median `0.008928`
- 5d: sample `60`, primary_hit `0.3333`, primary_closer `0.4167`, primary_mae `0.021372`, avg `0.010067`, median `0.00906`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.032843`, avg `0.018173`, median `0.011643`
- 20d: sample `60`, primary_hit `0.2167`, primary_closer `0.35`, primary_mae `0.046651`, avg `0.03659`, median `0.03694`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.4`, primary_mae `0.065424`, avg `0.060156`, median `0.067587`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.020826, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.021372, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.032843, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2167, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.046651, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.065424, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020587, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02389, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.020826, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022073, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026005, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.021372, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029252, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034662, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.032843, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03847, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061279, 'direction_hit_rate': 0.725}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2167, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.046651, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069414, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.084386, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.065424, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.024803`, avg `0.010561`, median `0.016867`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.022117`, avg `0.010055`, median `0.006683`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.030241`, avg `0.007601`, median `0.002148`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.043964`, avg `0.016553`, median `0.018428`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.06413`, avg `0.019755`, median `0.020882`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.020624`, avg `0.005243`, median `0.008011`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.018284`, avg `0.000242`, median `0.000647`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022973`, avg `0.00693`, median `0.002148`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.055906`, avg `0.028901`, median `0.031811`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.084383`, avg `0.046748`, median `0.059903`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.029659`, avg `-0.00333`, median `-0.005955`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.036801`, avg `0.009363`, median `0.016116`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.4375`, primary_mae `0.034467`, avg `0.024527`, median `0.019434`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.069143`, avg `-0.000198`, median `-0.023373`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.082976`, avg `0.010522`, median `-0.014177`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.375`, primary_mae `0.02389`, avg `0.006423`, median `0.008272`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.026005`, avg `0.010781`, median `0.010702`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4375`, primary_mae `0.034662`, avg `0.021136`, median `0.015054`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.056396`, avg `0.031709`, median `0.03694`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.071647`, avg `0.048638`, median `0.053364`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.375`, primary_mae `0.02389`, avg `0.006423`, median `0.008272`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.026005`, avg `0.010781`, median `0.010702`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4375`, primary_mae `0.034662`, avg `0.021136`, median `0.015054`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.056396`, avg `0.031709`, median `0.03694`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.071647`, avg `0.048638`, median `0.053364`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.3667`, primary_mae `0.020826`, avg `0.009124`, median `0.008928`
- 5d: sample `60`, primary_hit `0.3333`, primary_closer `0.4167`, primary_mae `0.021372`, avg `0.010067`, median `0.00906`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.032843`, avg `0.018173`, median `0.011643`
- 20d: sample `60`, primary_hit `0.2167`, primary_closer `0.35`, primary_mae `0.046651`, avg `0.03659`, median `0.03694`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.4`, primary_mae `0.065424`, avg `0.060156`, median `0.067587`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.033083`, avg `-0.001677`, median `0.001708`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.039906`, avg `0.01292`, median `0.017911`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.040119`, avg `0.030027`, median `0.024519`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.08563`, avg `0.017067`, median `0.027635`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.090317`, avg `0.014082`, median `-0.014177`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.375`, primary_mae `0.02389`, avg `0.006423`, median `0.008272`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.026005`, avg `0.010781`, median `0.010702`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4375`, primary_mae `0.034662`, avg `0.021136`, median `0.015054`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.056396`, avg `0.031709`, median `0.03694`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.071647`, avg `0.048638`, median `0.053364`

### flow_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.018972`, avg `0.004351`, median `0.007093`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.017857`, avg `0.00163`, median `0.001655`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.023609`, avg `0.004505`, median `-0.002297`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.051414`, avg `0.024782`, median `0.030451`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.079564`, avg `0.035468`, median `0.050609`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.375`, primary_mae `0.02389`, avg `0.006423`, median `0.008272`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.3875`, primary_mae `0.026005`, avg `0.010781`, median `0.010702`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4375`, primary_mae `0.034662`, avg `0.021136`, median `0.015054`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.056396`, avg `0.031709`, median `0.03694`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.071647`, avg `0.048638`, median `0.053364`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
