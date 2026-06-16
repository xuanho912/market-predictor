# Historical Replay Benchmark

Generated at: `2026-06-16T15:33:57.568043+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'high', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay', 'forward validation completed samples are below the minimum gate'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.014012`
- secondary_mean_absolute_error: `0.013551`
- primary_error_advantage: `-0.000461`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.019592`
- secondary_mean_absolute_error: `0.017391`
- primary_error_advantage: `-0.002201`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.028676`
- secondary_mean_absolute_error: `0.027355`
- primary_error_advantage: `-0.001321`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.7125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.04789`
- secondary_mean_absolute_error: `0.043813`
- primary_error_advantage: `-0.004077`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.069694`
- secondary_mean_absolute_error: `0.059851`
- primary_error_advantage: `-0.009843`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.013177`, as_primary `0`, as_primary_hit `None`, avg `0.00492`, median `0.005843`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.016903`, as_primary `0`, as_primary_hit `None`, avg `0.007156`, median `0.006206`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.022699`, as_primary `0`, as_primary_hit `None`, avg `0.007918`, median `0.009352`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.033242`, as_primary `0`, as_primary_hit `None`, avg `0.010482`, median `0.018375`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.05408`, as_primary `0`, as_primary_hit `None`, avg `0.027871`, median `0.032906`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.014012`, as_primary `80`, as_primary_hit `0.625`, avg `0.00492`, median `0.005843`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.019592`, as_primary `80`, as_primary_hit `0.6375`, avg `0.007156`, median `0.006206`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.028676`, as_primary `80`, as_primary_hit `0.6125`, avg `0.007918`, median `0.009352`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.04789`, as_primary `80`, as_primary_hit `0.7125`, avg `0.010482`, median `0.018375`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.069694`, as_primary `80`, as_primary_hit `0.625`, avg `0.027871`, median `0.032906`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.014175`, as_primary `0`, as_primary_hit `None`, avg `0.00492`, median `0.005843`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.018386`, as_primary `0`, as_primary_hit `None`, avg `0.007156`, median `0.006206`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.030814`, as_primary `0`, as_primary_hit `None`, avg `0.007918`, median `0.009352`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.062278`, as_primary `0`, as_primary_hit `None`, avg `0.010482`, median `0.018375`
- 60d: sample `80`, direction_hit `0.375`, path_mae `0.070841`, as_primary `0`, as_primary_hit `None`, avg `0.027871`, median `0.032906`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.012637`, as_primary `0`, as_primary_hit `None`, avg `0.00492`, median `0.005843`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.016106`, as_primary `0`, as_primary_hit `None`, avg `0.007156`, median `0.006206`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.02203`, as_primary `0`, as_primary_hit `None`, avg `0.007918`, median `0.009352`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.03111`, as_primary `0`, as_primary_hit `None`, avg `0.010482`, median `0.018375`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.052147`, as_primary `0`, as_primary_hit `None`, avg `0.027871`, median `0.032906`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.014012`, avg `0.00492`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3875`, primary_mae `0.019592`, avg `0.007156`, median `0.006206`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.028676`, avg `0.007918`, median `0.009352`
- 20d: sample `80`, primary_hit `0.7125`, primary_closer `0.3875`, primary_mae `0.04789`, avg `0.010482`, median `0.018375`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.069694`, avg `0.027871`, median `0.032906`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.425`, primary_mae `0.014261`, avg `0.007557`, median `0.006716`
- 5d: sample `40`, primary_hit `0.775`, primary_closer `0.375`, primary_mae `0.020893`, avg `0.011016`, median `0.011262`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.55`, primary_mae `0.029748`, avg `0.005219`, median `0.008571`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.052647`, avg `0.000489`, median `0.01201`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.071171`, avg `0.007272`, median `0.000394`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.013763`, avg `0.002283`, median `0.003745`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.018291`, avg `0.003295`, median `-0.000454`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.027604`, avg `0.010617`, median `0.010966`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.275`, primary_mae `0.043132`, avg `0.020475`, median `0.022746`
- 60d: sample `40`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.068216`, avg `0.048471`, median `0.06003`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.013763, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018291, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.027604, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.043132, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.068216, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012637, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014175, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.013763, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016106, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019592, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018291, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02203, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030814, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.027604, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03111, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062278, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.043132, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052147, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070841, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.068216, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.013881`, avg `-0.007791`, median `-0.007158`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.015631`, avg `-0.011833`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.012386`, avg `0.008706`, median `0.006918`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.125`, primary_mae `0.015756`, avg `0.028852`, median `0.030181`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.032369`, avg `0.054535`, median `0.055714`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.015196`, avg `-0.004727`, median `-0.006094`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.016676`, avg `-0.007672`, median `-0.010372`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.014885`, avg `0.007218`, median `0.006918`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.125`, primary_mae `0.026742`, avg `0.019289`, median `0.024685`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.05497`, avg `0.035914`, median `0.055714`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.015196`, avg `-0.004727`, median `-0.006094`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.016676`, avg `-0.007672`, median `-0.010372`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.014885`, avg `0.007218`, median `0.006918`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.125`, primary_mae `0.026742`, avg `0.019289`, median `0.024685`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.05497`, avg `0.035914`, median `0.055714`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.014012`, avg `0.00492`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3875`, primary_mae `0.019592`, avg `0.007156`, median `0.006206`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.028676`, avg `0.007918`, median `0.009352`
- 20d: sample `80`, primary_hit `0.7125`, primary_closer `0.3875`, primary_mae `0.04789`, avg `0.010482`, median `0.018375`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.069694`, avg `0.027871`, median `0.032906`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.014012`, avg `0.00492`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3875`, primary_mae `0.019592`, avg `0.007156`, median `0.006206`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.028676`, avg `0.007918`, median `0.009352`
- 20d: sample `80`, primary_hit `0.7125`, primary_closer `0.3875`, primary_mae `0.04789`, avg `0.010482`, median `0.018375`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.069694`, avg `0.027871`, median `0.032906`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.014012`, avg `0.00492`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3875`, primary_mae `0.019592`, avg `0.007156`, median `0.006206`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.028676`, avg `0.007918`, median `0.009352`
- 20d: sample `80`, primary_hit `0.7125`, primary_closer `0.3875`, primary_mae `0.04789`, avg `0.010482`, median `0.018375`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.069694`, avg `0.027871`, median `0.032906`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.014012`, avg `0.00492`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3875`, primary_mae `0.019592`, avg `0.007156`, median `0.006206`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.028676`, avg `0.007918`, median `0.009352`
- 20d: sample `80`, primary_hit `0.7125`, primary_closer `0.3875`, primary_mae `0.04789`, avg `0.010482`, median `0.018375`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.069694`, avg `0.027871`, median `0.032906`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.014012`, avg `0.00492`, median `0.005843`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.3875`, primary_mae `0.019592`, avg `0.007156`, median `0.006206`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.028676`, avg `0.007918`, median `0.009352`
- 20d: sample `80`, primary_hit `0.7125`, primary_closer `0.3875`, primary_mae `0.04789`, avg `0.010482`, median `0.018375`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.069694`, avg `0.027871`, median `0.032906`

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
