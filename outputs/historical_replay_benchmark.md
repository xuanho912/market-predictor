# Historical Replay Benchmark

Generated at: `2026-09-26T00:21:45.637506+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.015823`
- secondary_mean_absolute_error: `0.014918`
- primary_error_advantage: `-0.000905`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.019037`
- secondary_mean_absolute_error: `0.016879`
- primary_error_advantage: `-0.002158`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.021501`
- secondary_mean_absolute_error: `0.021441`
- primary_error_advantage: `-6e-05`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.55`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.425`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.047668`
- secondary_mean_absolute_error: `0.035003`
- primary_error_advantage: `-0.012665`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1125`
- secondary_hit_rate: `0.8875`
- primary_vs_secondary_accuracy_spread: `-0.775`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.05031`
- secondary_mean_absolute_error: `0.041667`
- primary_error_advantage: `-0.008643`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015173`, as_primary `0`, as_primary_hit `None`, avg `-0.000534`, median `1.9e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.017475`, as_primary `0`, as_primary_hit `None`, avg `0.002032`, median `0.00331`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.022505`, as_primary `0`, as_primary_hit `None`, avg `0.006455`, median `0.008213`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.034241`, as_primary `0`, as_primary_hit `None`, avg `0.021227`, median `0.026945`
- 60d: sample `80`, direction_hit `0.8875`, path_mae `0.042523`, as_primary `0`, as_primary_hit `None`, avg `0.081548`, median `0.098227`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015693`, as_primary `0`, as_primary_hit `None`, avg `-0.000534`, median `1.9e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.018207`, as_primary `0`, as_primary_hit `None`, avg `0.002032`, median `0.00331`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.026449`, as_primary `0`, as_primary_hit `None`, avg `0.006455`, median `0.008213`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.04823`, as_primary `0`, as_primary_hit `None`, avg `0.021227`, median `0.026945`
- 60d: sample `80`, direction_hit `0.8875`, path_mae `0.048166`, as_primary `0`, as_primary_hit `None`, avg `0.081548`, median `0.098227`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015823`, as_primary `80`, as_primary_hit `0.5`, avg `-0.000534`, median `1.9e-05`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.019037`, as_primary `80`, as_primary_hit `0.5125`, avg `0.002032`, median `0.00331`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.021501`, as_primary `80`, as_primary_hit `0.625`, avg `0.006455`, median `0.008213`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.047668`, as_primary `80`, as_primary_hit `0.7125`, avg `0.021227`, median `0.026945`
- 60d: sample `80`, direction_hit `0.1125`, path_mae `0.05031`, as_primary `80`, as_primary_hit `0.8875`, avg `0.081548`, median `0.098227`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015012`, as_primary `0`, as_primary_hit `None`, avg `-0.000534`, median `1.9e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.016891`, as_primary `0`, as_primary_hit `None`, avg `0.002032`, median `0.00331`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.02109`, as_primary `0`, as_primary_hit `None`, avg `0.006455`, median `0.008213`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.03146`, as_primary `0`, as_primary_hit `None`, avg `0.021227`, median `0.026945`
- 60d: sample `80`, direction_hit `0.8875`, path_mae `0.042114`, as_primary `0`, as_primary_hit `None`, avg `0.081548`, median `0.098227`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.016431`, avg `0.002031`, median `0.005195`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.019595`, avg `0.004511`, median `0.005185`
- 10d: sample `40`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.021168`, avg `0.010534`, median `0.013359`
- 20d: sample `40`, primary_hit `0.2`, primary_closer `0.425`, primary_mae `0.040626`, avg `0.032976`, median `0.029674`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.5`, primary_mae `0.058967`, avg `0.069993`, median `0.085041`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.425`, primary_mae `0.015215`, avg `-0.003099`, median `-0.003098`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.01848`, avg `-0.000446`, median `-0.000293`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.021834`, avg `0.002376`, median `0.005365`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.05471`, avg `0.009479`, median `0.025303`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.4`, primary_mae `0.041653`, avg `0.093103`, median `0.103255`

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
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.018009`, avg `-0.006757`, median `-0.010089`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.022626`, avg `-0.002723`, median `-0.004042`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.033309`, avg `-0.000555`, median `-0.003925`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.068096`, avg `-0.005393`, median `0.003968`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.4`, primary_mae `0.045496`, avg `0.104861`, median `0.114142`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.4667`, primary_mae `0.015094`, avg `0.00154`, median `0.003357`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.017841`, avg `0.003618`, median `0.005185`
- 10d: sample `60`, primary_hit `0.3167`, primary_closer `0.55`, primary_mae `0.017565`, avg `0.008792`, median `0.009969`
- 20d: sample `60`, primary_hit `0.2167`, primary_closer `0.3833`, primary_mae `0.040859`, avg `0.030101`, median `0.030406`
- 60d: sample `60`, primary_hit `0.1167`, primary_closer `0.4667`, primary_mae `0.051914`, avg `0.073777`, median `0.084258`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.015094, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017841, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.017565, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.040859, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.045496, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015012, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015823, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.015094, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016891, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019037, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017841, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02109, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026449, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.017565, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.425, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03146, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04823, 'direction_hit_rate': 0.7125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.040859, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1125, 'secondary_hit_rate': 0.8875, 'primary_vs_secondary_accuracy_spread': -0.775, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042114, 'direction_hit_rate': 0.8875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05031, 'direction_hit_rate': 0.1125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.045496, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.013124`, avg `0.005815`, median `0.008014`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.015499`, avg `0.006695`, median `0.008828`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.75`, primary_mae `0.014721`, avg `0.009347`, median `0.01205`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.035436`, avg `0.026788`, median `0.029102`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.5`, primary_mae `0.0093`, avg `0.114868`, median `0.11635`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.014156`, avg `0.004328`, median `0.006481`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.016249`, avg `0.006465`, median `0.008828`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.018544`, avg `0.010055`, median `0.016702`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.5625`, primary_mae `0.036625`, avg `0.029553`, median `0.026175`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.625`, primary_mae `0.036703`, avg `0.088342`, median `0.104666`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.019257`, avg `-0.007032`, median `-0.006398`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.025316`, avg `-0.00041`, median `-0.001376`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.035614`, avg `0.001215`, median `-0.001779`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.074145`, avg `0.000315`, median `0.021827`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.3125`, primary_mae `0.049134`, avg `0.098416`, median `0.113344`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.015823`, avg `-0.000534`, median `1.9e-05`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.019037`, avg `0.002032`, median `0.00331`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.5125`, primary_mae `0.021501`, avg `0.006455`, median `0.008213`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.375`, primary_mae `0.047668`, avg `0.021227`, median `0.026945`
- 60d: sample `80`, primary_hit `0.1125`, primary_closer `0.45`, primary_mae `0.05031`, avg `0.081548`, median `0.098227`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.015823`, avg `-0.000534`, median `1.9e-05`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.019037`, avg `0.002032`, median `0.00331`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.5125`, primary_mae `0.021501`, avg `0.006455`, median `0.008213`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.375`, primary_mae `0.047668`, avg `0.021227`, median `0.026945`
- 60d: sample `80`, primary_hit `0.1125`, primary_closer `0.45`, primary_mae `0.05031`, avg `0.081548`, median `0.098227`

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
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.015823`, avg `-0.000534`, median `1.9e-05`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.019037`, avg `0.002032`, median `0.00331`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.5125`, primary_mae `0.021501`, avg `0.006455`, median `0.008213`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.375`, primary_mae `0.047668`, avg `0.021227`, median `0.026945`
- 60d: sample `80`, primary_hit `0.1125`, primary_closer `0.45`, primary_mae `0.05031`, avg `0.081548`, median `0.098227`

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
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.015823`, avg `-0.000534`, median `1.9e-05`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.425`, primary_mae `0.019037`, avg `0.002032`, median `0.00331`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.5125`, primary_mae `0.021501`, avg `0.006455`, median `0.008213`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.375`, primary_mae `0.047668`, avg `0.021227`, median `0.026945`
- 60d: sample `80`, primary_hit `0.1125`, primary_closer `0.45`, primary_mae `0.05031`, avg `0.081548`, median `0.098227`

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
