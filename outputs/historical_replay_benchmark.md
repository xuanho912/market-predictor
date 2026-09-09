# Historical Replay Benchmark

Generated at: `2026-09-09T16:42:31.341546+00:00`
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
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.016448`
- secondary_mean_absolute_error: `0.01292`
- primary_error_advantage: `-0.003528`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.018285`
- secondary_mean_absolute_error: `0.014707`
- primary_error_advantage: `-0.003578`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.031641`
- secondary_mean_absolute_error: `0.025764`
- primary_error_advantage: `-0.005877`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.060714`
- secondary_mean_absolute_error: `0.037481`
- primary_error_advantage: `-0.023233`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.097635`
- secondary_mean_absolute_error: `0.062583`
- primary_error_advantage: `-0.035052`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.012239`, as_primary `0`, as_primary_hit `None`, avg `0.002164`, median `0.001813`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.015097`, as_primary `0`, as_primary_hit `None`, avg `0.002586`, median `0.001723`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.024797`, as_primary `0`, as_primary_hit `None`, avg `0.001062`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.037242`, as_primary `0`, as_primary_hit `None`, avg `0.010701`, median `0.020147`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.066965`, as_primary `0`, as_primary_hit `None`, avg `0.040486`, median `0.059722`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.014504`, as_primary `0`, as_primary_hit `None`, avg `0.002164`, median `0.001813`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.018271`, as_primary `0`, as_primary_hit `None`, avg `0.002586`, median `0.001723`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.037318`, as_primary `0`, as_primary_hit `None`, avg `0.001062`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.054873`, as_primary `0`, as_primary_hit `None`, avg `0.010701`, median `0.020147`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.073163`, as_primary `0`, as_primary_hit `None`, avg `0.040486`, median `0.059722`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.016448`, as_primary `80`, as_primary_hit `0.575`, avg `0.002164`, median `0.001813`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.018285`, as_primary `80`, as_primary_hit `0.6`, avg `0.002586`, median `0.001723`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.031641`, as_primary `80`, as_primary_hit `0.4`, avg `0.001062`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.060714`, as_primary `80`, as_primary_hit `0.625`, avg `0.010701`, median `0.020147`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.097635`, as_primary `80`, as_primary_hit `0.725`, avg `0.040486`, median `0.059722`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.012154`, as_primary `0`, as_primary_hit `None`, avg `0.002164`, median `0.001813`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.014826`, as_primary `0`, as_primary_hit `None`, avg `0.002586`, median `0.001723`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.023006`, as_primary `0`, as_primary_hit `None`, avg `0.001062`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.034576`, as_primary `0`, as_primary_hit `None`, avg `0.010701`, median `0.020147`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.062681`, as_primary `0`, as_primary_hit `None`, avg `0.040486`, median `0.059722`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.016448`, avg `0.002164`, median `0.001813`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.018285`, avg `0.002586`, median `0.001723`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.031641`, avg `0.001062`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.275`, primary_mae `0.060714`, avg `0.010701`, median `0.020147`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.097635`, avg `0.040486`, median `0.059722`

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
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.4167`, primary_mae `0.013601`, avg `-0.000101`, median `0.000402`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.3833`, primary_mae `0.014606`, avg `-0.000474`, median `0.001056`
- 10d: sample `60`, primary_hit `0.6667`, primary_closer `0.4833`, primary_mae `0.026988`, avg `-0.005586`, median `-0.010483`
- 20d: sample `60`, primary_hit `0.4667`, primary_closer `0.2667`, primary_mae `0.065096`, avg `0.00032`, median `0.004833`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.3167`, primary_mae `0.106797`, avg `0.027055`, median `0.051878`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.024991`, avg `0.00896`, median `0.010341`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.029321`, avg `0.011765`, median `0.011918`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.045601`, avg `0.021005`, median `0.019602`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.3`, primary_mae `0.047567`, avg `0.041845`, median `0.036414`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.070148`, avg `0.080777`, median `0.077217`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.013601, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.014606, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6667, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.026988, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047567, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.070148, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012154, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016448, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.013601, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014826, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018285, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.014606, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023006, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037318, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6667, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.026988, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034576, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060714, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047567, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062681, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.097635, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.070148, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.020508`, avg `-0.000535`, median `0.001949`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.01655`, avg `-0.005484`, median `-0.002115`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.028602`, avg `0.000352`, median `-0.004116`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.06262`, avg `0.019425`, median `0.024617`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.117204`, avg `0.048845`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.018116`, avg `-0.00447`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.017281`, avg `-0.007925`, median `-0.002115`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.028288`, avg `-0.000413`, median `-0.00362`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.061803`, avg `0.01658`, median `0.030181`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.118314`, avg `0.04566`, median `0.072376`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.013408`, avg `0.005342`, median `0.007138`
- 5d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.01597`, avg `0.011903`, median `0.0116`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.035012`, avg `0.002289`, median `-0.001235`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.074256`, avg `0.006157`, median `-0.003661`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.121977`, avg `0.031606`, median `0.035382`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.016448`, avg `0.002164`, median `0.001813`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.018285`, avg `0.002586`, median `0.001723`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.031641`, avg `0.001062`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.275`, primary_mae `0.060714`, avg `0.010701`, median `0.020147`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.097635`, avg `0.040486`, median `0.059722`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.016448`, avg `0.002164`, median `0.001813`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.018285`, avg `0.002586`, median `0.001723`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.031641`, avg `0.001062`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.275`, primary_mae `0.060714`, avg `0.010701`, median `0.020147`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.097635`, avg `0.040486`, median `0.059722`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.009026`, avg `-0.000663`, median `-0.001535`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.010653`, avg `-0.00226`, median `0.000818`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.022587`, avg `-0.008149`, median `-0.011447`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.065958`, avg `-0.008985`, median `-0.002363`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.083089`, avg `0.019717`, median `0.045303`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.3167`, primary_mae `0.018922`, avg `0.003107`, median `0.004891`
- 5d: sample `60`, primary_hit `0.4`, primary_closer `0.3667`, primary_mae `0.020829`, avg `0.004201`, median `0.00496`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.3833`, primary_mae `0.034659`, avg `0.004132`, median `-0.004843`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.25`, primary_mae `0.058965`, avg `0.017263`, median `0.027235`
- 60d: sample `60`, primary_hit `0.2167`, primary_closer `0.3`, primary_mae `0.102484`, avg `0.047408`, median `0.064699`

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
