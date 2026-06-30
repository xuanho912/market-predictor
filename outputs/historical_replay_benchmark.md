# Historical Replay Benchmark

Generated at: `2026-06-30T23:48:13.222940+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'low', 'reasons': [], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.011812`
- secondary_mean_absolute_error: `0.011371`
- primary_error_advantage: `-0.000441`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.6`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.017595`
- secondary_mean_absolute_error: `0.01544`
- primary_error_advantage: `-0.002155`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.022266`
- secondary_mean_absolute_error: `0.020986`
- primary_error_advantage: `-0.00128`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.050249`
- secondary_mean_absolute_error: `0.050223`
- primary_error_advantage: `-2.6e-05`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.575`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.07793`
- secondary_mean_absolute_error: `0.068076`
- primary_error_advantage: `-0.009854`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.010651`, as_primary `0`, as_primary_hit `None`, avg `-0.003088`, median `-0.00397`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.015141`, as_primary `0`, as_primary_hit `None`, avg `-0.003942`, median `-0.003063`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.01837`, as_primary `0`, as_primary_hit `None`, avg `-0.000677`, median `-0.003425`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.032103`, as_primary `0`, as_primary_hit `None`, avg `0.003524`, median `0.00995`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.057468`, as_primary `0`, as_primary_hit `None`, avg `0.009056`, median `-0.00576`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.011909`, as_primary `60`, as_primary_hit `0.4333`, avg `-0.003088`, median `-0.00397`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.01783`, as_primary `60`, as_primary_hit `0.4167`, avg `-0.003942`, median `-0.003063`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.022118`, as_primary `60`, as_primary_hit `0.4667`, avg `-0.000677`, median `-0.003425`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.045971`, as_primary `60`, as_primary_hit `0.6167`, avg `0.003524`, median `0.00995`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.08279`, as_primary `60`, as_primary_hit `0.55`, avg `0.009056`, median `-0.00576`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.011891`, as_primary `20`, as_primary_hit `0.25`, avg `-0.003088`, median `-0.00397`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.015283`, as_primary `20`, as_primary_hit `0.6`, avg `-0.003942`, median `-0.003063`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.021516`, as_primary `20`, as_primary_hit `0.45`, avg `-0.000677`, median `-0.003425`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.060134`, as_primary `20`, as_primary_hit `0.6`, avg `0.003524`, median `0.00995`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.075255`, as_primary `20`, as_primary_hit `0.2`, avg `0.009056`, median `-0.00576`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.010482`, as_primary `0`, as_primary_hit `None`, avg `-0.003088`, median `-0.00397`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.014423`, as_primary `0`, as_primary_hit `None`, avg `-0.003942`, median `-0.003063`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.018411`, as_primary `0`, as_primary_hit `None`, avg `-0.000677`, median `-0.003425`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.030696`, as_primary `0`, as_primary_hit `None`, avg `0.003524`, median `0.00995`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.053861`, as_primary `0`, as_primary_hit `None`, avg `0.009056`, median `-0.00576`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.5333`, primary_mae `0.013465`, avg `-0.002349`, median `-0.001981`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.4833`, primary_mae `0.020004`, avg `-0.004943`, median `-0.005416`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.025331`, avg `-0.000542`, median `-0.003912`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.4667`, primary_mae `0.049832`, avg `0.004846`, median `0.00995`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.4667`, primary_mae `0.092148`, avg `0.024327`, median `0.021052`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.6`, primary_mae `0.006855`, avg `-0.005303`, median `-0.007329`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.010368`, avg `-0.00094`, median `0.002906`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.013072`, avg `-0.001082`, median `-0.003297`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.051499`, avg `-0.000442`, median `0.009366`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.7`, primary_mae `0.035276`, avg `-0.036757`, median `-0.042342`

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
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.6`, primary_mae `0.006855`, avg `-0.005303`, median `-0.007329`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.010368`, avg `-0.00094`, median `0.002906`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.013072`, avg `-0.001082`, median `-0.003297`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.051499`, avg `-0.000442`, median `0.009366`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.7`, primary_mae `0.035276`, avg `-0.036757`, median `-0.042342`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.5333`, primary_mae `0.013465`, avg `-0.002349`, median `-0.001981`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.4833`, primary_mae `0.020004`, avg `-0.004943`, median `-0.005416`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.025331`, avg `-0.000542`, median `-0.003912`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.4667`, primary_mae `0.049832`, avg `0.004846`, median `0.00995`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.4667`, primary_mae `0.092148`, avg `0.024327`, median `0.021052`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.006855, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.010368, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.013072, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.049832, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.035276, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.010482, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011909, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.006855, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014423, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01783, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.010368, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01837, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022118, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.013072, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030696, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060134, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.049832, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053861, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.08279, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.035276, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.014743`, avg `-0.013613`, median `-0.013259`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.021694`, avg `-0.019931`, median `-0.024559`
- 10d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.012856`, avg `-0.006621`, median `-0.006325`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.038921`, avg `0.022237`, median `0.030181`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.071759`, avg `0.052494`, median `0.073193`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.014516`, avg `-0.009342`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.018938`, avg `-0.013389`, median `-0.017664`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.013674`, avg `-0.003376`, median `-0.005954`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.038293`, avg `0.02577`, median `0.028979`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.063815`, avg `0.063794`, median `0.076894`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.00712`, avg `-0.004836`, median `-0.006076`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.012387`, avg `-0.0022`, median `0.000615`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.013669`, avg `5.1e-05`, median `-0.000739`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.058939`, avg `0.006136`, median `0.013848`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.039277`, avg `-0.035706`, median `-0.041472`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.55`, primary_mae `0.011812`, avg `-0.003088`, median `-0.00397`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.5125`, primary_mae `0.017595`, avg `-0.003942`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.022266`, avg `-0.000677`, median `-0.003425`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.050249`, avg `0.003524`, median `0.00995`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.07793`, avg `0.009056`, median `-0.00576`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.55`, primary_mae `0.011812`, avg `-0.003088`, median `-0.00397`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.5125`, primary_mae `0.017595`, avg `-0.003942`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.022266`, avg `-0.000677`, median `-0.003425`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.050249`, avg `0.003524`, median `0.00995`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.07793`, avg `0.009056`, median `-0.00576`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.5333`, primary_mae `0.013465`, avg `-0.002349`, median `-0.001981`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.4833`, primary_mae `0.020004`, avg `-0.004943`, median `-0.005416`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.025331`, avg `-0.000542`, median `-0.003912`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.4667`, primary_mae `0.049832`, avg `0.004846`, median `0.00995`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.4667`, primary_mae `0.092148`, avg `0.024327`, median `0.021052`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.6`, primary_mae `0.006855`, avg `-0.005303`, median `-0.007329`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.010368`, avg `-0.00094`, median `0.002906`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.013072`, avg `-0.001082`, median `-0.003297`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.051499`, avg `-0.000442`, median `0.009366`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.7`, primary_mae `0.035276`, avg `-0.036757`, median `-0.042342`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.55`, primary_mae `0.011812`, avg `-0.003088`, median `-0.00397`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.5125`, primary_mae `0.017595`, avg `-0.003942`, median `-0.003063`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.022266`, avg `-0.000677`, median `-0.003425`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.050249`, avg `0.003524`, median `0.00995`
- 60d: sample `80`, primary_hit `0.6125`, primary_closer `0.525`, primary_mae `0.07793`, avg `0.009056`, median `-0.00576`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.5333`, primary_mae `0.013465`, avg `-0.002349`, median `-0.001981`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.4833`, primary_mae `0.020004`, avg `-0.004943`, median `-0.005416`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.025331`, avg `-0.000542`, median `-0.003912`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.4667`, primary_mae `0.049832`, avg `0.004846`, median `0.00995`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.4667`, primary_mae `0.092148`, avg `0.024327`, median `0.021052`

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
