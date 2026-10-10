# Historical Replay Benchmark

Generated at: `2026-10-10T10:09:33.050308+00:00`
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
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.3625`
- primary_vs_secondary_accuracy_spread: `0.275`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.019821`
- secondary_mean_absolute_error: `0.016697`
- primary_error_advantage: `-0.003124`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.022346`
- secondary_mean_absolute_error: `0.019618`
- primary_error_advantage: `-0.002728`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.575`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.028181`
- secondary_mean_absolute_error: `0.02494`
- primary_error_advantage: `-0.003241`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.062237`
- secondary_mean_absolute_error: `0.043477`
- primary_error_advantage: `-0.01876`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.225`
- secondary_hit_rate: `0.775`
- primary_vs_secondary_accuracy_spread: `-0.55`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.076297`
- secondary_mean_absolute_error: `0.056069`
- primary_error_advantage: `-0.020228`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.016068`, as_primary `0`, as_primary_hit `None`, avg `-0.007103`, median `-0.004922`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.017121`, as_primary `0`, as_primary_hit `None`, avg `-0.011502`, median `-0.013233`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.023148`, as_primary `0`, as_primary_hit `None`, avg `-0.008977`, median `-0.007166`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.036809`, as_primary `0`, as_primary_hit `None`, avg `0.014045`, median `0.015876`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.047597`, as_primary `0`, as_primary_hit `None`, avg `0.039059`, median `0.048222`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.017119`, as_primary `0`, as_primary_hit `None`, avg `-0.007103`, median `-0.004922`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.019542`, as_primary `0`, as_primary_hit `None`, avg `-0.011502`, median `-0.013233`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.02881`, as_primary `0`, as_primary_hit `None`, avg `-0.008977`, median `-0.007166`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.054347`, as_primary `0`, as_primary_hit `None`, avg `0.014045`, median `0.015876`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.059914`, as_primary `0`, as_primary_hit `None`, avg `0.039059`, median `0.048222`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.019821`, as_primary `80`, as_primary_hit `0.3625`, avg `-0.007103`, median `-0.004922`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.022346`, as_primary `80`, as_primary_hit `0.4`, avg `-0.011502`, median `-0.013233`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.028181`, as_primary `80`, as_primary_hit `0.4`, avg `-0.008977`, median `-0.007166`
- 20d: sample `80`, direction_hit `0.4`, path_mae `0.062237`, as_primary `80`, as_primary_hit `0.6`, avg `0.014045`, median `0.015876`
- 60d: sample `80`, direction_hit `0.225`, path_mae `0.076297`, as_primary `80`, as_primary_hit `0.775`, avg `0.039059`, median `0.048222`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.015336`, as_primary `0`, as_primary_hit `None`, avg `-0.007103`, median `-0.004922`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.016548`, as_primary `0`, as_primary_hit `None`, avg `-0.011502`, median `-0.013233`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.022642`, as_primary `0`, as_primary_hit `None`, avg `-0.008977`, median `-0.007166`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.03625`, as_primary `0`, as_primary_hit `None`, avg `0.014045`, median `0.015876`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.049579`, as_primary `0`, as_primary_hit `None`, avg `0.039059`, median `0.048222`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5667`, primary_closer `0.4667`, primary_mae `0.017785`, avg `-0.004951`, median `-0.003662`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.5667`, primary_mae `0.021775`, avg `-0.009254`, median `-0.006789`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.4`, primary_mae `0.023353`, avg `-0.007877`, median `-0.006503`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.4`, primary_mae `0.054152`, avg `0.010623`, median `0.015876`
- 60d: sample `60`, primary_hit `0.25`, primary_closer `0.3333`, primary_mae `0.071632`, avg `0.028294`, median `0.043421`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.02593`, avg `-0.013559`, median `-0.010671`
- 5d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.024057`, avg `-0.018248`, median `-0.021882`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.042665`, avg `-0.012275`, median `-0.029899`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.086492`, avg `0.024309`, median `0.020526`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.090291`, avg `0.071353`, median `0.085768`

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
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.019821`, avg `-0.007103`, median `-0.004922`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.022346`, avg `-0.011502`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.028181`, avg `-0.008977`, median `-0.007166`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.062237`, avg `0.014045`, median `0.015876`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.076297`, avg `0.039059`, median `0.048222`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6375, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.019821, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.022346, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.028181, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.062237, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.076297, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_vs_secondary_accuracy_spread': 0.275, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015336, 'direction_hit_rate': 0.3625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019821, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6375, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.019821, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016548, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022346, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.022346, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022642, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02881, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.028181, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03625, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062237, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.062237, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.225, 'secondary_hit_rate': 0.775, 'primary_vs_secondary_accuracy_spread': -0.55, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.047597, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076297, 'direction_hit_rate': 0.225}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.076297, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.01786`, avg `-0.016807`, median `-0.030767`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.031311`, avg `-0.01718`, median `-0.020293`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.025217`, avg `-0.012488`, median `-0.014252`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.089956`, avg `0.014597`, median `0.027639`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.143914`, avg `0.053341`, median `0.065914`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.020693`, avg `-0.011881`, median `-0.01401`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.029575`, avg `-0.019577`, median `-0.02258`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.030807`, avg `-0.013064`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.079436`, avg `0.008378`, median `0.023936`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.126317`, avg `0.032446`, median `0.054785`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.125`, primary_mae `0.02622`, avg `-0.007314`, median `-0.010058`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.021158`, avg `-0.016326`, median `-0.021882`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.039456`, avg `-0.012589`, median `-0.029899`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.093015`, avg `0.031454`, median `0.042225`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.1875`, primary_mae `0.097691`, avg `0.084365`, median `0.092349`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.019821`, avg `-0.007103`, median `-0.004922`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.022346`, avg `-0.011502`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.028181`, avg `-0.008977`, median `-0.007166`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.062237`, avg `0.014045`, median `0.015876`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.076297`, avg `0.039059`, median `0.048222`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.019821`, avg `-0.007103`, median `-0.004922`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.022346`, avg `-0.011502`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.028181`, avg `-0.008977`, median `-0.007166`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.062237`, avg `0.014045`, median `0.015876`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.076297`, avg `0.039059`, median `0.048222`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.020052`, avg `-0.012605`, median `-0.012389`
- 5d: sample `20`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.029317`, avg `-0.018823`, median `-0.021349`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.028247`, avg `-0.01616`, median `-0.014807`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.076242`, avg `0.007223`, median `0.019252`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.122824`, avg `0.032983`, median `0.054785`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.325`, primary_mae `0.020329`, avg `-0.005121`, median `-0.003848`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.017271`, avg `-0.008875`, median `-0.008187`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.028701`, avg `-0.005328`, median `-0.005578`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.059266`, avg `0.018647`, median `0.01444`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.25`, primary_mae `0.06796`, avg `0.045811`, median `0.043421`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.019821`, avg `-0.007103`, median `-0.004922`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.022346`, avg `-0.011502`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.028181`, avg `-0.008977`, median `-0.007166`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.062237`, avg `0.014045`, median `0.015876`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.076297`, avg `0.039059`, median `0.048222`

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
