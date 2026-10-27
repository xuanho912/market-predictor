# Historical Replay Benchmark

Generated at: `2026-10-27T06:21:37.848199+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
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
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.017891`
- secondary_mean_absolute_error: `0.015895`
- primary_error_advantage: `-0.001996`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.017482`
- secondary_mean_absolute_error: `0.019162`
- primary_error_advantage: `0.00168`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.02666`
- secondary_mean_absolute_error: `0.025194`
- primary_error_advantage: `-0.001466`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.045469`
- secondary_mean_absolute_error: `0.036672`
- primary_error_advantage: `-0.008797`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.15`
- secondary_hit_rate: `0.85`
- primary_vs_secondary_accuracy_spread: `-0.7`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.047842`
- secondary_mean_absolute_error: `0.037388`
- primary_error_advantage: `-0.010454`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.01554`, as_primary `0`, as_primary_hit `None`, avg `0.004195`, median `0.005755`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017212`, as_primary `0`, as_primary_hit `None`, avg `0.004834`, median `0.006642`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.021928`, as_primary `0`, as_primary_hit `None`, avg `0.012354`, median `0.010879`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.03126`, as_primary `0`, as_primary_hit `None`, avg `0.019908`, median `0.022438`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.037367`, as_primary `0`, as_primary_hit `None`, avg `0.043178`, median `0.048873`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.015709`, as_primary `0`, as_primary_hit `None`, avg `0.004195`, median `0.005755`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.019226`, as_primary `0`, as_primary_hit `None`, avg `0.004834`, median `0.006642`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.02919`, as_primary `0`, as_primary_hit `None`, avg `0.012354`, median `0.010879`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.046471`, as_primary `0`, as_primary_hit `None`, avg `0.019908`, median `0.022438`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.039647`, as_primary `0`, as_primary_hit `None`, avg `0.043178`, median `0.048873`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.017891`, as_primary `80`, as_primary_hit `0.575`, avg `0.004195`, median `0.005755`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.017482`, as_primary `80`, as_primary_hit `0.5625`, avg `0.004834`, median `0.006642`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.02666`, as_primary `80`, as_primary_hit `0.675`, avg `0.012354`, median `0.010879`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.045469`, as_primary `80`, as_primary_hit `0.725`, avg `0.019908`, median `0.022438`
- 60d: sample `80`, direction_hit `0.15`, path_mae `0.047842`, as_primary `80`, as_primary_hit `0.85`, avg `0.043178`, median `0.048873`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.01534`, as_primary `0`, as_primary_hit `None`, avg `0.004195`, median `0.005755`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.016629`, as_primary `0`, as_primary_hit `None`, avg `0.004834`, median `0.006642`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.020075`, as_primary `0`, as_primary_hit `None`, avg `0.012354`, median `0.010879`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.02827`, as_primary `0`, as_primary_hit `None`, avg `0.019908`, median `0.022438`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.03654`, as_primary `0`, as_primary_hit `None`, avg `0.043178`, median `0.048873`

## Edge Status Performance

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.015841`, avg `0.007633`, median `0.009718`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.013379`, avg `0.013617`, median `0.016839`
- 10d: sample `20`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.020676`, avg `0.021166`, median `0.020528`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.052674`, avg `0.022436`, median `0.021004`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.5`, primary_mae `0.031924`, avg `0.026839`, median `0.023762`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.4333`, primary_mae `0.018574`, avg `0.003049`, median `0.003658`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.01885`, avg `0.001906`, median `-0.001153`
- 10d: sample `60`, primary_hit `0.3833`, primary_closer `0.4333`, primary_mae `0.028655`, avg `0.009417`, median `0.008601`
- 20d: sample `60`, primary_hit `0.25`, primary_closer `0.4667`, primary_mae `0.043067`, avg `0.019065`, median `0.022438`
- 60d: sample `60`, primary_hit `0.15`, primary_closer `0.3833`, primary_mae `0.053148`, avg `0.048624`, median `0.054536`

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
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.024843`, avg `0.001136`, median `-0.007516`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.021268`, avg `-0.001162`, median `-0.001784`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.02457`, avg `0.006086`, median `0.009495`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.047793`, avg `0.007945`, median `0.001221`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.080418`, avg `0.045545`, median `0.041256`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.018394`, avg `0.005974`, median `0.002901`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.020362`, avg `0.004551`, median `-0.003772`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.024871`, avg `0.017933`, median `0.014259`
- 20d: sample `20`, primary_hit `0.05`, primary_closer `0.65`, primary_mae `0.030262`, avg `0.03352`, median `0.028709`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.5`, primary_mae `0.030966`, avg `0.072656`, median `0.078007`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.014164`, avg `0.004835`, median `0.006323`
- 5d: sample `40`, primary_hit `0.35`, primary_closer `0.525`, primary_mae `0.014149`, avg `0.007973`, median `0.009272`
- 10d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.028599`, avg `0.012698`, median `0.011971`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.05191`, avg `0.019082`, median `0.019102`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.425`, primary_mae `0.039993`, avg `0.027255`, median `0.031432`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014164, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.014149, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.02457, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.030262, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.030966, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01534, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017891, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014164, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016629, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019226, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.014149, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020075, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02919, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.02457, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02827, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.046471, 'direction_hit_rate': 0.725}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.030262, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.15, 'secondary_hit_rate': 0.85, 'primary_vs_secondary_accuracy_spread': -0.7, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03654, 'direction_hit_rate': 0.85}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.047842, 'direction_hit_rate': 0.15}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.030966, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.013527`, avg `0.002738`, median `0.006323`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.015098`, avg `0.003635`, median `0.004986`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.043618`, avg `0.008584`, median `0.014419`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.054556`, avg `0.02459`, median `0.023499`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.04363`, avg `0.026024`, median `0.037084`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.012875`, avg `0.005612`, median `0.006547`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.015747`, avg `0.004939`, median `0.006642`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.038222`, avg `0.005282`, median `0.007954`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.051516`, avg `0.01674`, median `0.019102`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.375`, primary_mae `0.044426`, avg `0.027644`, median `0.039614`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.023709`, avg `0.003351`, median `-0.000483`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.019292`, avg `0.00347`, median `0.002887`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.026889`, avg `0.007115`, median `0.009787`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.044258`, avg `0.003933`, median `-0.004493`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.083583`, avg `0.055727`, median `0.041256`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.017891`, avg `0.004195`, median `0.005755`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.017482`, avg `0.004834`, median `0.006642`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.02666`, avg `0.012354`, median `0.010879`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.4375`, primary_mae `0.045469`, avg `0.019908`, median `0.022438`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.4125`, primary_mae `0.047842`, avg `0.043178`, median `0.048873`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.017891`, avg `0.004195`, median `0.005755`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.017482`, avg `0.004834`, median `0.006642`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.02666`, avg `0.012354`, median `0.010879`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.4375`, primary_mae `0.045469`, avg `0.019908`, median `0.022438`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.4125`, primary_mae `0.047842`, avg `0.043178`, median `0.048873`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.45`, primary_mae `0.015574`, avg `0.005215`, median `0.006029`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.5333`, primary_mae `0.01622`, avg `0.006832`, median `0.007155`
- 10d: sample `60`, primary_hit `0.3167`, primary_closer `0.4333`, primary_mae `0.027357`, avg `0.014443`, median `0.011971`
- 20d: sample `60`, primary_hit `0.2167`, primary_closer `0.45`, primary_mae `0.044694`, avg `0.023895`, median `0.026442`
- 60d: sample `60`, primary_hit `0.1333`, primary_closer `0.45`, primary_mae `0.036984`, avg `0.042389`, median `0.050464`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.024843`, avg `0.001136`, median `-0.007516`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.021268`, avg `-0.001162`, median `-0.001784`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.02457`, avg `0.006086`, median `0.009495`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.047793`, avg `0.007945`, median `0.001221`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.080418`, avg `0.045545`, median `0.041256`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.017891`, avg `0.004195`, median `0.005755`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.017482`, avg `0.004834`, median `0.006642`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.02666`, avg `0.012354`, median `0.010879`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.4375`, primary_mae `0.045469`, avg `0.019908`, median `0.022438`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.4125`, primary_mae `0.047842`, avg `0.043178`, median `0.048873`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.017891`, avg `0.004195`, median `0.005755`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.017482`, avg `0.004834`, median `0.006642`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.4125`, primary_mae `0.02666`, avg `0.012354`, median `0.010879`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.4375`, primary_mae `0.045469`, avg `0.019908`, median `0.022438`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.4125`, primary_mae `0.047842`, avg `0.043178`, median `0.048873`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
