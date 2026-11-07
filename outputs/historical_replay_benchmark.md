# Historical Replay Benchmark

Generated at: `2026-11-07T00:12:21.955030+00:00`
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
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.028451`
- secondary_mean_absolute_error: `0.023507`
- primary_error_advantage: `-0.004944`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.034852`
- secondary_mean_absolute_error: `0.02821`
- primary_error_advantage: `-0.006642`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.3375`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.06738`
- secondary_mean_absolute_error: `0.047777`
- primary_error_advantage: `-0.019603`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.225`
- primary_mean_absolute_error: `0.12119`
- secondary_mean_absolute_error: `0.059383`
- primary_error_advantage: `-0.061807`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `-0.6`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.099624`
- secondary_mean_absolute_error: `0.057513`
- primary_error_advantage: `-0.042111`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.02119`, as_primary `0`, as_primary_hit `None`, avg `0.003729`, median `0.008997`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.025678`, as_primary `0`, as_primary_hit `None`, avg `0.009408`, median `0.01341`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.042618`, as_primary `0`, as_primary_hit `None`, avg `0.012481`, median `0.024377`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.053143`, as_primary `0`, as_primary_hit `None`, avg `0.017892`, median `0.044993`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.059375`, as_primary `0`, as_primary_hit `None`, avg `0.050863`, median `0.072628`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.024375`, as_primary `0`, as_primary_hit `None`, avg `0.003729`, median `0.008997`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.030115`, as_primary `0`, as_primary_hit `None`, avg `0.009408`, median `0.01341`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.049789`, as_primary `0`, as_primary_hit `None`, avg `0.012481`, median `0.024377`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.071158`, as_primary `0`, as_primary_hit `None`, avg `0.017892`, median `0.044993`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.06013`, as_primary `0`, as_primary_hit `None`, avg `0.050863`, median `0.072628`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.028451`, as_primary `80`, as_primary_hit `0.625`, avg `0.003729`, median `0.008997`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.034852`, as_primary `80`, as_primary_hit `0.6375`, avg `0.009408`, median `0.01341`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.06738`, as_primary `80`, as_primary_hit `0.6625`, avg `0.012481`, median `0.024377`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.12119`, as_primary `80`, as_primary_hit `0.7`, avg `0.017892`, median `0.044993`
- 60d: sample `80`, direction_hit `0.2`, path_mae `0.099624`, as_primary `80`, as_primary_hit `0.8`, avg `0.050863`, median `0.072628`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.021302`, as_primary `0`, as_primary_hit `None`, avg `0.003729`, median `0.008997`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.025`, as_primary `0`, as_primary_hit `None`, avg `0.009408`, median `0.01341`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.042501`, as_primary `0`, as_primary_hit `None`, avg `0.012481`, median `0.024377`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.053836`, as_primary `0`, as_primary_hit `None`, avg `0.017892`, median `0.044993`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.056552`, as_primary `0`, as_primary_hit `None`, avg `0.050863`, median `0.072628`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.028451`, avg `0.003729`, median `0.008997`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.034852`, avg `0.009408`, median `0.01341`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.06738`, avg `0.012481`, median `0.024377`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.225`, primary_mae `0.12119`, avg `0.017892`, median `0.044993`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.2625`, primary_mae `0.099624`, avg `0.050863`, median `0.072628`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.028451`, avg `0.003729`, median `0.008997`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.034852`, avg `0.009408`, median `0.01341`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.06738`, avg `0.012481`, median `0.024377`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.225`, primary_mae `0.12119`, avg `0.017892`, median `0.044993`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.2625`, primary_mae `0.099624`, avg `0.050863`, median `0.072628`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.028451, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3625, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.034852, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.06738, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.12119, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.2625, 'primary_mean_absolute_error': 0.099624, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02119, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028451, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.028451, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034852, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3625, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.034852, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.3375, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042501, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06738, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.06738, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.225, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053143, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.12119, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.12119, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': -0.6, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056552, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.099624, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.2625, 'primary_mean_absolute_error': 0.099624, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.032004`, avg `0.013863`, median `0.01487`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.023436`, avg `0.017298`, median `0.014042`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.048777`, avg `-0.003558`, median `-0.012245`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.099728`, avg `0.00707`, median `0.026664`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.042006`, avg `0.05666`, median `0.070952`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.028999`, avg `0.012335`, median `0.011421`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.020185`, avg `0.01375`, median `0.01341`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.054692`, avg `0.013506`, median `0.020708`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.095188`, avg `0.021709`, median `0.03064`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.3125`, primary_mae `0.047546`, avg `0.073534`, median `0.070952`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.025076`, avg `0.004258`, median `0.011882`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.025463`, avg `0.024815`, median `0.024793`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.051241`, avg `0.038305`, median `0.058473`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.103184`, avg `0.054332`, median `0.074921`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.096848`, avg `0.077306`, median `0.099746`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.028451`, avg `0.003729`, median `0.008997`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.034852`, avg `0.009408`, median `0.01341`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.06738`, avg `0.012481`, median `0.024377`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.225`, primary_mae `0.12119`, avg `0.017892`, median `0.044993`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.2625`, primary_mae `0.099624`, avg `0.050863`, median `0.072628`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.028451`, avg `0.003729`, median `0.008997`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.034852`, avg `0.009408`, median `0.01341`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.06738`, avg `0.012481`, median `0.024377`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.225`, primary_mae `0.12119`, avg `0.017892`, median `0.044993`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.2625`, primary_mae `0.099624`, avg `0.050863`, median `0.072628`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.030445`, avg `0.003082`, median `0.007407`
- 5d: sample `60`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.038678`, avg `0.003767`, median `0.011845`
- 10d: sample `60`, primary_hit `0.3833`, primary_closer `0.4`, primary_mae `0.073749`, avg `0.003251`, median `0.011637`
- 20d: sample `60`, primary_hit `0.35`, primary_closer `0.2333`, primary_mae `0.129082`, avg `0.006984`, median `0.027803`
- 60d: sample `60`, primary_hit `0.2167`, primary_closer `0.2833`, primary_mae `0.101173`, avg `0.038392`, median `0.06005`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.55`, primary_mae `0.02247`, avg `0.00567`, median `0.011882`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.023376`, avg `0.02633`, median `0.029536`
- 10d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.048272`, avg `0.04017`, median `0.053885`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.2`, primary_mae `0.097513`, avg `0.050618`, median `0.067551`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.2`, primary_mae `0.094977`, avg `0.088274`, median `0.101673`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.028451`, avg `0.003729`, median `0.008997`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.034852`, avg `0.009408`, median `0.01341`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.06738`, avg `0.012481`, median `0.024377`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.225`, primary_mae `0.12119`, avg `0.017892`, median `0.044993`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.2625`, primary_mae `0.099624`, avg `0.050863`, median `0.072628`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.028451`, avg `0.003729`, median `0.008997`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.034852`, avg `0.009408`, median `0.01341`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.06738`, avg `0.012481`, median `0.024377`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.225`, primary_mae `0.12119`, avg `0.017892`, median `0.044993`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.2625`, primary_mae `0.099624`, avg `0.050863`, median `0.072628`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.028451`, avg `0.003729`, median `0.008997`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.034852`, avg `0.009408`, median `0.01341`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3625`, primary_mae `0.06738`, avg `0.012481`, median `0.024377`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.225`, primary_mae `0.12119`, avg `0.017892`, median `0.044993`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.2625`, primary_mae `0.099624`, avg `0.050863`, median `0.072628`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
