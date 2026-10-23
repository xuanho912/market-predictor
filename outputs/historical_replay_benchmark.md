# Historical Replay Benchmark

Generated at: `2026-10-23T08:52:55.562393+00:00`
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
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.016787`
- secondary_mean_absolute_error: `0.015101`
- primary_error_advantage: `-0.001686`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.01896`
- secondary_mean_absolute_error: `0.020145`
- primary_error_advantage: `0.001185`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.027233`
- secondary_mean_absolute_error: `0.027428`
- primary_error_advantage: `0.000195`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.575`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.043608`
- secondary_mean_absolute_error: `0.035963`
- primary_error_advantage: `-0.007645`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.425`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.05507`
- secondary_mean_absolute_error: `0.0457`
- primary_error_advantage: `-0.00937`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.014476`, as_primary `0`, as_primary_hit `None`, avg `0.004512`, median `0.004406`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.017844`, as_primary `0`, as_primary_hit `None`, avg `0.0035`, median `0.003762`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.023554`, as_primary `0`, as_primary_hit `None`, avg `0.009019`, median `0.010267`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.028849`, as_primary `0`, as_primary_hit `None`, avg `0.017976`, median `0.019215`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.042809`, as_primary `0`, as_primary_hit `None`, avg `0.037263`, median `0.048358`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.015028`, as_primary `20`, as_primary_hit `0.75`, avg `0.004512`, median `0.004406`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.020793`, as_primary `20`, as_primary_hit `0.75`, avg `0.0035`, median `0.003762`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.030896`, as_primary `20`, as_primary_hit `0.75`, avg `0.009019`, median `0.010267`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.044586`, as_primary `20`, as_primary_hit `0.75`, avg `0.017976`, median `0.019215`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.046563`, as_primary `20`, as_primary_hit `0.6`, avg `0.037263`, median `0.048358`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016804`, as_primary `60`, as_primary_hit `0.55`, avg `0.004512`, median `0.004406`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.018383`, as_primary `60`, as_primary_hit `0.5167`, avg `0.0035`, median `0.003762`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.030457`, as_primary `60`, as_primary_hit `0.6333`, avg `0.009019`, median `0.010267`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.042507`, as_primary `60`, as_primary_hit `0.7`, avg `0.017976`, median `0.019215`
- 60d: sample `80`, direction_hit `0.2625`, path_mae `0.056709`, as_primary `60`, as_primary_hit `0.7833`, avg `0.037263`, median `0.048358`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.014284`, as_primary `0`, as_primary_hit `None`, avg `0.004512`, median `0.004406`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.017019`, as_primary `0`, as_primary_hit `None`, avg `0.0035`, median `0.003762`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.02164`, as_primary `0`, as_primary_hit `None`, avg `0.009019`, median `0.010267`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.02555`, as_primary `0`, as_primary_hit `None`, avg `0.017976`, median `0.019215`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.042043`, as_primary `0`, as_primary_hit `None`, avg `0.037263`, median `0.048358`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.008197`, avg `0.00638`, median `0.006991`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.016513`, avg `0.008271`, median `0.009916`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.021448`, avg `0.009135`, median `0.01584`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.036856`, avg `0.01744`, median `0.014917`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.059127`, avg `0.014627`, median `0.021483`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.015963`, avg `0.006391`, median `0.008477`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.021697`, avg `0.007971`, median `0.015204`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.042021`, avg `0.010664`, median `0.017986`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.054633`, avg `0.014134`, median `0.010237`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.037686`, avg `0.006608`, median `0.008337`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.021494`, avg `0.002639`, median `0.00105`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.018815`, avg `-0.001122`, median `-0.005339`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.525`, primary_mae `0.022731`, avg `0.008139`, median `0.006889`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.425`, primary_mae `0.041471`, avg `0.020164`, median `0.028024`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.275`, primary_mae `0.061734`, avg `0.063908`, median `0.067799`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.008197`, avg `0.00638`, median `0.006991`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.016513`, avg `0.008271`, median `0.009916`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.021448`, avg `0.009135`, median `0.01584`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.036856`, avg `0.01744`, median `0.014917`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.059127`, avg `0.014627`, median `0.021483`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.25`, primary_mae `0.024375`, avg `-0.001802`, median `-0.00786`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.019952`, avg `-0.003624`, median `-0.005339`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.022328`, avg `0.008066`, median `0.009495`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.049959`, avg `0.010453`, median `0.004843`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.065668`, avg `0.058748`, median `0.052`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.018613`, avg `0.007079`, median `0.00758`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.017679`, avg `0.001381`, median `-0.005063`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.65`, primary_mae `0.023134`, avg `0.008212`, median `0.002415`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.5`, primary_mae `0.032983`, avg `0.029876`, median `0.029544`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.25`, primary_mae `0.057799`, avg `0.069068`, median `0.077573`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.015963`, avg `0.006391`, median `0.008477`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.021697`, avg `0.007971`, median `0.015204`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.042021`, avg `0.010664`, median `0.017986`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.054633`, avg `0.014134`, median `0.010237`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.037686`, avg `0.006608`, median `0.008337`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.008197, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016513, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.021448, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.032983, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.037686, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014284, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016804, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.008197, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017019, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020793, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016513, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02164, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030896, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.021448, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02555, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044586, 'direction_hit_rate': 0.7125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.032983, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.425, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042043, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056709, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.037686, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.005708`, avg `0.007954`, median `0.006991`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.02326`, avg `0.00142`, median `-0.002082`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.031131`, avg `-0.005397`, median `0.009841`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.0`, primary_mae `0.041094`, avg `0.009106`, median `0.008479`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.074319`, avg `0.00634`, median `0.002733`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.007587`, avg `0.005912`, median `0.005645`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.018686`, avg `0.006385`, median `0.007532`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.5`, primary_mae `0.021088`, avg `0.006337`, median `0.01584`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.0625`, primary_mae `0.041145`, avg `0.009056`, median `0.012453`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.069085`, avg `0.008943`, median `0.002733`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.023458`, avg `0.000501`, median `-0.00786`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.022183`, avg `-0.003991`, median `-0.005339`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.023359`, avg `0.009213`, median `0.009495`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.051713`, avg `0.011708`, median `0.011531`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.375`, primary_mae `0.051788`, avg `0.043746`, median `0.031522`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.016787`, avg `0.004512`, median `0.004406`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.01896`, avg `0.0035`, median `0.003762`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.027233`, avg `0.009019`, median `0.010267`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.043608`, avg `0.017976`, median `0.019215`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.4125`, primary_mae `0.05507`, avg `0.037263`, median `0.048358`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.016787`, avg `0.004512`, median `0.004406`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.01896`, avg `0.0035`, median `0.003762`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.027233`, avg `0.009019`, median `0.010267`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.043608`, avg `0.017976`, median `0.019215`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.4125`, primary_mae `0.05507`, avg `0.037263`, median `0.048358`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.5`, primary_mae `0.014258`, avg `0.006617`, median `0.006991`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.5`, primary_mae `0.01863`, avg `0.005874`, median `0.008725`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.5`, primary_mae `0.028868`, avg `0.009337`, median `0.011579`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.4167`, primary_mae `0.041491`, avg `0.020483`, median `0.022399`
- 60d: sample `60`, primary_hit `0.3667`, primary_closer `0.45`, primary_mae `0.051538`, avg `0.030101`, median `0.043282`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.25`, primary_mae `0.024375`, avg `-0.001802`, median `-0.00786`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.019952`, avg `-0.003624`, median `-0.005339`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.022328`, avg `0.008066`, median `0.009495`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.049959`, avg `0.010453`, median `0.004843`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.065668`, avg `0.058748`, median `0.052`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.016787`, avg `0.004512`, median `0.004406`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.01896`, avg `0.0035`, median `0.003762`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.027233`, avg `0.009019`, median `0.010267`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.043608`, avg `0.017976`, median `0.019215`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.4125`, primary_mae `0.05507`, avg `0.037263`, median `0.048358`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.016787`, avg `0.004512`, median `0.004406`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.01896`, avg `0.0035`, median `0.003762`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.027233`, avg `0.009019`, median `0.010267`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.043608`, avg `0.017976`, median `0.019215`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.4125`, primary_mae `0.05507`, avg `0.037263`, median `0.048358`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.016787`, avg `0.004512`, median `0.004406`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.01896`, avg `0.0035`, median `0.003762`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.027233`, avg `0.009019`, median `0.010267`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.043608`, avg `0.017976`, median `0.019215`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.4125`, primary_mae `0.05507`, avg `0.037263`, median `0.048358`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.4375`, primary_mae `0.016787`, avg `0.004512`, median `0.004406`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.01896`, avg `0.0035`, median `0.003762`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.475`, primary_mae `0.027233`, avg `0.009019`, median `0.010267`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.043608`, avg `0.017976`, median `0.019215`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.4125`, primary_mae `0.05507`, avg `0.037263`, median `0.048358`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
