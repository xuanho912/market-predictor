# Historical Replay Benchmark

Generated at: `2026-11-11T19:38:58.011448+00:00`
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
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.01703`
- secondary_mean_absolute_error: `0.017035`
- primary_error_advantage: `5e-06`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.023311`
- secondary_mean_absolute_error: `0.020878`
- primary_error_advantage: `-0.002433`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.1125`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.03556`
- secondary_mean_absolute_error: `0.029946`
- primary_error_advantage: `-0.005614`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.044724`
- secondary_mean_absolute_error: `0.033349`
- primary_error_advantage: `-0.011375`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.05393`
- secondary_mean_absolute_error: `0.059224`
- primary_error_advantage: `0.005294`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.015609`, as_primary `0`, as_primary_hit `None`, avg `-0.000838`, median `-0.002703`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.019714`, as_primary `0`, as_primary_hit `None`, avg `-0.00145`, median `-0.001825`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.025913`, as_primary `0`, as_primary_hit `None`, avg `0.00621`, median `0.006521`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.025156`, as_primary `0`, as_primary_hit `None`, avg `0.021932`, median `0.027108`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.048633`, as_primary `0`, as_primary_hit `None`, avg `0.043313`, median `0.063656`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.017704`, as_primary `60`, as_primary_hit `0.45`, avg `-0.000838`, median `-0.002703`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.022684`, as_primary `60`, as_primary_hit `0.4667`, avg `-0.00145`, median `-0.001825`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.033854`, as_primary `60`, as_primary_hit `0.55`, avg `0.00621`, median `0.006521`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.038904`, as_primary `60`, as_primary_hit `0.8`, avg `0.021932`, median `0.027108`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.052967`, as_primary `60`, as_primary_hit `0.7333`, avg `0.043313`, median `0.063656`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.017021`, as_primary `20`, as_primary_hit `0.4`, avg `-0.000838`, median `-0.002703`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.021509`, as_primary `20`, as_primary_hit `0.55`, avg `-0.00145`, median `-0.001825`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.034573`, as_primary `20`, as_primary_hit `0.7`, avg `0.00621`, median `0.006521`
- 20d: sample `80`, direction_hit `0.2`, path_mae `0.048273`, as_primary `20`, as_primary_hit `0.8`, avg `0.021932`, median `0.027108`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.0733`, as_primary `20`, as_primary_hit `0.85`, avg `0.043313`, median `0.063656`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.015089`, as_primary `0`, as_primary_hit `None`, avg `-0.000838`, median `-0.002703`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.01892`, as_primary `0`, as_primary_hit `None`, avg `-0.00145`, median `-0.001825`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.024944`, as_primary `0`, as_primary_hit `None`, avg `0.00621`, median `0.006521`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.024218`, as_primary `0`, as_primary_hit `None`, avg `0.021932`, median `0.027108`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.050518`, as_primary `0`, as_primary_hit `None`, avg `0.043313`, median `0.063656`

## Edge Status Performance

### STRONG_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.016859`, avg `-0.000613`, median `-0.001726`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.45`, primary_mae `0.023121`, avg `-0.000729`, median `-0.005558`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.4333`, primary_mae `0.035034`, avg `0.006698`, median `0.006262`
- 20d: sample `60`, primary_hit `0.8`, primary_closer `0.5`, primary_mae `0.038889`, avg `0.021733`, median `0.024827`
- 60d: sample `60`, primary_hit `0.7333`, primary_closer `0.5833`, primary_mae `0.05515`, avg `0.036901`, median `0.056661`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.017544`, avg `-0.001511`, median `-0.009662`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.023879`, avg `-0.003613`, median `0.004066`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.03714`, avg `0.004748`, median `0.008`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.15`, primary_mae `0.06223`, avg `0.022531`, median `0.032742`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.05027`, avg `0.062547`, median `0.069067`

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
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.017544`, avg `-0.001511`, median `-0.009662`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.023879`, avg `-0.003613`, median `0.004066`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.03714`, avg `0.004748`, median `0.008`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.15`, primary_mae `0.06223`, avg `0.022531`, median `0.032742`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.05027`, avg `0.062547`, median `0.069067`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.016859`, avg `-0.000613`, median `-0.001726`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.45`, primary_mae `0.023121`, avg `-0.000729`, median `-0.005558`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.4333`, primary_mae `0.035034`, avg `0.006698`, median `0.006262`
- 20d: sample `60`, primary_hit `0.8`, primary_closer `0.5`, primary_mae `0.038889`, avg `0.021733`, median `0.024827`
- 60d: sample `60`, primary_hit `0.7333`, primary_closer `0.5833`, primary_mae `0.05515`, avg `0.036901`, median `0.056661`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016859, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.023121, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.035034, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.038889, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.05027, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015089, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017704, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016859, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01892, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022684, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.023121, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.1125, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024944, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034573, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.035034, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024218, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048273, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.038889, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048633, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0733, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.05027, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.025615`, avg `-5e-05`, median `-0.004159`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.029809`, avg `0.001194`, median `-0.010753`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.023934`, avg `0.021796`, median `0.022448`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.031455`, avg `0.033882`, median `0.031427`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.875`, primary_mae `0.01981`, avg `0.079187`, median `0.086868`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.023151`, avg `0.000937`, median `0.000401`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.028864`, avg `-0.001823`, median `-0.005558`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.033899`, avg `0.00841`, median `0.003189`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.6875`, primary_mae `0.037033`, avg `0.024938`, median `0.028445`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.6875`, primary_mae `0.046572`, avg `0.050009`, median `0.070816`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.017185`, avg `-0.002304`, median `-0.009662`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.024262`, avg `-0.003134`, median `-0.005094`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.035233`, avg `0.000547`, median `0.008`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.059401`, avg `0.017845`, median `0.028361`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.5`, primary_mae `0.052524`, avg `0.05631`, median `0.058724`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.01703`, avg `-0.000838`, median `-0.002703`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.023311`, avg `-0.00145`, median `-0.001825`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.03556`, avg `0.00621`, median `0.006521`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.044724`, avg `0.021932`, median `0.027108`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5375`, primary_mae `0.05393`, avg `0.043313`, median `0.063656`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.01703`, avg `-0.000838`, median `-0.002703`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.023311`, avg `-0.00145`, median `-0.001825`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.03556`, avg `0.00621`, median `0.006521`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.044724`, avg `0.021932`, median `0.027108`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5375`, primary_mae `0.05393`, avg `0.043313`, median `0.063656`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.016859`, avg `-0.000613`, median `-0.001726`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.45`, primary_mae `0.023121`, avg `-0.000729`, median `-0.005558`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.4333`, primary_mae `0.035034`, avg `0.006698`, median `0.006262`
- 20d: sample `60`, primary_hit `0.8`, primary_closer `0.5`, primary_mae `0.038889`, avg `0.021733`, median `0.024827`
- 60d: sample `60`, primary_hit `0.7333`, primary_closer `0.5833`, primary_mae `0.05515`, avg `0.036901`, median `0.056661`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.017544`, avg `-0.001511`, median `-0.009662`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.023879`, avg `-0.003613`, median `0.004066`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.03714`, avg `0.004748`, median `0.008`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.15`, primary_mae `0.06223`, avg `0.022531`, median `0.032742`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.05027`, avg `0.062547`, median `0.069067`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.01703`, avg `-0.000838`, median `-0.002703`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.023311`, avg `-0.00145`, median `-0.001825`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.03556`, avg `0.00621`, median `0.006521`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.044724`, avg `0.021932`, median `0.027108`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5375`, primary_mae `0.05393`, avg `0.043313`, median `0.063656`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.01703`, avg `-0.000838`, median `-0.002703`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.45`, primary_mae `0.023311`, avg `-0.00145`, median `-0.001825`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.4`, primary_mae `0.03556`, avg `0.00621`, median `0.006521`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.4125`, primary_mae `0.044724`, avg `0.021932`, median `0.027108`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5375`, primary_mae `0.05393`, avg `0.043313`, median `0.063656`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
