# Historical Replay Benchmark

Generated at: `2026-08-26T13:20:49.943720+00:00`
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
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.017498`
- secondary_mean_absolute_error: `0.016621`
- primary_error_advantage: `-0.000877`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.021737`
- secondary_mean_absolute_error: `0.019388`
- primary_error_advantage: `-0.002349`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.038338`
- secondary_mean_absolute_error: `0.034962`
- primary_error_advantage: `-0.003376`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.06037`
- secondary_mean_absolute_error: `0.06003`
- primary_error_advantage: `-0.00034`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.064642`
- secondary_mean_absolute_error: `0.073658`
- primary_error_advantage: `0.009016`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014449`, as_primary `0`, as_primary_hit `None`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.018048`, as_primary `0`, as_primary_hit `None`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.025525`, as_primary `0`, as_primary_hit `None`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.036707`, as_primary `0`, as_primary_hit `None`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.060878`, as_primary `0`, as_primary_hit `None`, avg `0.01801`, median `0.028684`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014548`, as_primary `40`, as_primary_hit `0.575`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.019895`, as_primary `40`, as_primary_hit `0.575`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.037186`, as_primary `40`, as_primary_hit `0.575`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.049712`, as_primary `40`, as_primary_hit `0.675`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.074744`, as_primary `40`, as_primary_hit `0.6`, avg `0.01801`, median `0.028684`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.019536`, as_primary `40`, as_primary_hit `0.6`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.021759`, as_primary `40`, as_primary_hit `0.55`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.040702`, as_primary `40`, as_primary_hit `0.4`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.074468`, as_primary `40`, as_primary_hit `0.55`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, direction_hit `0.4`, path_mae `0.074851`, as_primary `40`, as_primary_hit `0.6`, avg `0.01801`, median `0.028684`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014185`, as_primary `0`, as_primary_hit `None`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017744`, as_primary `0`, as_primary_hit `None`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.025014`, as_primary `0`, as_primary_hit `None`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.037453`, as_primary `0`, as_primary_hit `None`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.056717`, as_primary `0`, as_primary_hit `None`, avg `0.01801`, median `0.028684`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.017498`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.021737`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.038338`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.4875`, primary_mae `0.06037`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.064642`, avg `0.01801`, median `0.028684`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.015724`, avg `0.004973`, median `0.005259`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.023743`, avg `0.007089`, median `0.006399`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.043659`, avg `0.004836`, median `0.008604`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.75`, primary_mae `0.049235`, avg `-4.7e-05`, median `0.016578`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.7`, primary_mae `0.049351`, avg `0.000455`, median `0.007994`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.014978`, avg `-0.001171`, median `-0.000413`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.013065`, avg `-0.002599`, median `0.000781`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.023815`, avg `-0.01227`, median `-0.016966`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.066036`, avg `-0.020576`, median `-0.011784`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.072856`, avg `-0.003977`, median `-0.018485`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.019646`, avg `0.001509`, median `0.005007`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.025071`, avg `-2e-06`, median `-0.002011`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.042939`, avg `0.006066`, median `0.006195`
- 20d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.063104`, avg `0.012049`, median `0.02729`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.068182`, avg `0.03778`, median `0.039151`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014978, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013065, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.023815, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.049235, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.049351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014185, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019536, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014978, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017744, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021759, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013065, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025014, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040702, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.023815, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036707, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074468, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.049235, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056717, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074851, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.049351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016107`, avg `-0.008017`, median `0.001949`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.024323`, avg `-0.008603`, median `-0.006309`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.029901`, avg `-0.001747`, median `-0.00518`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.05324`, avg `-0.000917`, median `0.006586`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.081364`, avg `0.002785`, median `0.004851`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.625`, primary_mae `0.01456`, avg `-0.002252`, median `0.001949`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.019308`, avg `-0.002461`, median `0.00171`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.026133`, avg `0.006015`, median `0.013177`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.043274`, avg `0.01168`, median `0.023299`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.071627`, avg `0.021661`, median `0.029874`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.016348`, avg `0.000141`, median `0.000684`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.012923`, avg `-0.00307`, median `0.000633`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.024496`, avg `-0.011944`, median `-0.016467`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.067051`, avg `-0.020369`, median `-0.011784`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.075705`, avg `-0.003036`, median `-0.018485`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.017498`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.021737`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.038338`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.4875`, primary_mae `0.06037`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.064642`, avg `0.01801`, median `0.028684`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.017498`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.021737`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.038338`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.4875`, primary_mae `0.06037`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.064642`, avg `0.01801`, median `0.028684`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.014992`, avg `-0.00385`, median `-0.000127`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.019661`, avg `-0.004014`, median `-0.002011`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.024422`, avg `0.007073`, median `0.010282`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.65`, primary_mae `0.039228`, avg `0.0152`, median `0.027848`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.070691`, avg `0.022341`, median `0.031374`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.019639`, avg `0.002849`, median `0.003955`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.021773`, avg `0.000706`, median `0.000781`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.042636`, avg `-0.003605`, median `-0.007787`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.275`, primary_mae `0.076508`, avg `-0.005839`, median `0.009671`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.069264`, avg `0.024621`, median `0.030984`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.017498`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.021737`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.038338`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.4875`, primary_mae `0.06037`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.064642`, avg `0.01801`, median `0.028684`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.017498`, avg `0.001705`, median `0.002957`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.45`, primary_mae `0.021737`, avg `0.001122`, median `0.001271`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.038338`, avg `0.001174`, median `-0.001839`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.4875`, primary_mae `0.06037`, avg `0.000869`, median `0.016995`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.575`, primary_mae `0.064642`, avg `0.01801`, median `0.028684`

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
