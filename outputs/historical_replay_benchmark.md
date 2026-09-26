# Historical Replay Benchmark

Generated at: `2026-09-26T16:27:30.902774+00:00`
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
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.018028`
- secondary_mean_absolute_error: `0.015653`
- primary_error_advantage: `-0.002375`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.025356`
- secondary_mean_absolute_error: `0.019849`
- primary_error_advantage: `-0.005507`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.036556`
- secondary_mean_absolute_error: `0.027889`
- primary_error_advantage: `-0.008667`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.073452`
- secondary_mean_absolute_error: `0.045339`
- primary_error_advantage: `-0.028113`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.2`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2125`
- secondary_hit_rate: `0.7875`
- primary_vs_secondary_accuracy_spread: `-0.575`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.100761`
- secondary_mean_absolute_error: `0.069714`
- primary_error_advantage: `-0.031047`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.2`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.01519`, as_primary `0`, as_primary_hit `None`, avg `-0.007209`, median `-0.003835`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018721`, as_primary `0`, as_primary_hit `None`, avg `-0.011175`, median `-0.008187`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.026334`, as_primary `0`, as_primary_hit `None`, avg `-0.008763`, median `-0.006203`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.041439`, as_primary `0`, as_primary_hit `None`, avg `0.004228`, median `0.015082`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.06409`, as_primary `0`, as_primary_hit `None`, avg `0.036471`, median `0.052147`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015965`, as_primary `0`, as_primary_hit `None`, avg `-0.007209`, median `-0.003835`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.021018`, as_primary `0`, as_primary_hit `None`, avg `-0.011175`, median `-0.008187`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.034274`, as_primary `0`, as_primary_hit `None`, avg `-0.008763`, median `-0.006203`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.062344`, as_primary `0`, as_primary_hit `None`, avg `0.004228`, median `0.015082`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.069074`, as_primary `0`, as_primary_hit `None`, avg `0.036471`, median `0.052147`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.018028`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.007209`, median `-0.003835`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.025356`, as_primary `80`, as_primary_hit `0.45`, avg `-0.011175`, median `-0.008187`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.036556`, as_primary `80`, as_primary_hit `0.45`, avg `-0.008763`, median `-0.006203`
- 20d: sample `80`, direction_hit `0.4`, path_mae `0.073452`, as_primary `80`, as_primary_hit `0.6`, avg `0.004228`, median `0.015082`
- 60d: sample `80`, direction_hit `0.2125`, path_mae `0.100761`, as_primary `80`, as_primary_hit `0.7875`, avg `0.036471`, median `0.052147`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015035`, as_primary `0`, as_primary_hit `None`, avg `-0.007209`, median `-0.003835`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018819`, as_primary `0`, as_primary_hit `None`, avg `-0.011175`, median `-0.008187`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.026167`, as_primary `0`, as_primary_hit `None`, avg `-0.008763`, median `-0.006203`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.041293`, as_primary `0`, as_primary_hit `None`, avg `0.004228`, median `0.015082`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.065431`, as_primary `0`, as_primary_hit `None`, avg `0.036471`, median `0.052147`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.023659`, avg `-0.011099`, median `-0.015445`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.035274`, avg `-0.016982`, median `-0.017298`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.35`, primary_mae `0.038112`, avg `-0.015639`, median `-0.012632`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.087426`, avg `0.005394`, median `0.018406`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.144411`, avg `0.036176`, median `0.054785`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4`, primary_mae `0.016151`, avg `-0.005912`, median `-0.003662`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.3667`, primary_mae `0.022051`, avg `-0.00924`, median `-0.003597`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.3333`, primary_mae `0.036037`, avg `-0.006472`, median `0.002106`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.2833`, primary_mae `0.068794`, avg `0.003839`, median `0.012135`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.2667`, primary_mae `0.086211`, avg `0.03657`, median `0.052022`

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
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4`, primary_mae `0.016151`, avg `-0.005912`, median `-0.003662`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.3667`, primary_mae `0.022051`, avg `-0.00924`, median `-0.003597`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.3333`, primary_mae `0.036037`, avg `-0.006472`, median `0.002106`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.2833`, primary_mae `0.068794`, avg `0.003839`, median `0.012135`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.2667`, primary_mae `0.086211`, avg `0.03657`, median `0.052022`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.023659`, avg `-0.011099`, median `-0.015445`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.035274`, avg `-0.016982`, median `-0.017298`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.35`, primary_mae `0.038112`, avg `-0.015639`, median `-0.012632`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.087426`, avg `0.005394`, median `0.018406`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.144411`, avg `0.036176`, median `0.054785`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016151, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.022051, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.3333, 'primary_mean_absolute_error': 0.036037, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.2833, 'primary_mean_absolute_error': 0.068794, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.086211, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015035, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018028, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016151, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018721, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025356, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.022051, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026167, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036556, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.3333, 'primary_mean_absolute_error': 0.036037, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041293, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073452, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.2833, 'primary_mean_absolute_error': 0.068794, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2125, 'secondary_hit_rate': 0.7875, 'primary_vs_secondary_accuracy_spread': -0.575, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06409, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.100761, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.086211, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

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
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.021302`, avg `-0.014012`, median `-0.022443`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.033913`, avg `-0.019182`, median `-0.020235`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.375`, primary_mae `0.035586`, avg `-0.019007`, median `-0.015452`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.087093`, avg `0.003896`, median `0.023936`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.139382`, avg `0.029088`, median `0.054785`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.02212`, avg `-0.013895`, median `-0.012143`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.028457`, avg `-0.017284`, median `-0.017304`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.054714`, avg `-0.001897`, median `-0.01146`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.101264`, avg `0.009202`, median `0.012219`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.142639`, avg `0.05552`, median `0.114142`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.018028`, avg `-0.007209`, median `-0.003835`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.025356`, avg `-0.011175`, median `-0.008187`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.3375`, primary_mae `0.036556`, avg `-0.008763`, median `-0.006203`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.275`, primary_mae `0.073452`, avg `0.004228`, median `0.015082`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.2625`, primary_mae `0.100761`, avg `0.036471`, median `0.052147`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.018028`, avg `-0.007209`, median `-0.003835`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.025356`, avg `-0.011175`, median `-0.008187`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.3375`, primary_mae `0.036556`, avg `-0.008763`, median `-0.006203`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.275`, primary_mae `0.073452`, avg `0.004228`, median `0.015082`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.2625`, primary_mae `0.100761`, avg `0.036471`, median `0.052147`

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
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.425`, primary_mae `0.018028`, avg `-0.007209`, median `-0.003835`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.025356`, avg `-0.011175`, median `-0.008187`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.3375`, primary_mae `0.036556`, avg `-0.008763`, median `-0.006203`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.275`, primary_mae `0.073452`, avg `0.004228`, median `0.015082`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.2625`, primary_mae `0.100761`, avg `0.036471`, median `0.052147`

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
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.45`, primary_mae `0.016943`, avg `-0.002881`, median `0.000983`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.3667`, primary_mae `0.02484`, avg `-0.007073`, median `0.000899`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.3`, primary_mae `0.033543`, avg `-0.0072`, median `-0.002583`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.2333`, primary_mae `0.068551`, avg `0.006947`, median `0.015873`
- 60d: sample `60`, primary_hit `0.1833`, primary_closer `0.25`, primary_mae `0.091241`, avg `0.037135`, median `0.04627`

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
