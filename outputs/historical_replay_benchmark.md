# Historical Replay Benchmark

Generated at: `2026-11-17T04:10:44.139402+00:00`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.02731`
- secondary_mean_absolute_error: `0.022689`
- primary_error_advantage: `-0.004621`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.027839`
- secondary_mean_absolute_error: `0.023814`
- primary_error_advantage: `-0.004025`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.0375`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.032332`
- secondary_mean_absolute_error: `0.028975`
- primary_error_advantage: `-0.003357`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.053304`
- secondary_mean_absolute_error: `0.043511`
- primary_error_advantage: `-0.009793`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.084073`
- secondary_mean_absolute_error: `0.071911`
- primary_error_advantage: `-0.012162`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.021827`, as_primary `0`, as_primary_hit `None`, avg `0.00119`, median `0.003038`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.021727`, as_primary `0`, as_primary_hit `None`, avg `-0.000877`, median `0.000448`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.026109`, as_primary `0`, as_primary_hit `None`, avg `0.001941`, median `0.003658`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.033952`, as_primary `0`, as_primary_hit `None`, avg `0.010443`, median `0.022038`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.0681`, as_primary `0`, as_primary_hit `None`, avg `0.045819`, median `0.065617`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.02376`, as_primary `0`, as_primary_hit `None`, avg `0.00119`, median `0.003038`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.024087`, as_primary `0`, as_primary_hit `None`, avg `-0.000877`, median `0.000448`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.031`, as_primary `0`, as_primary_hit `None`, avg `0.001941`, median `0.003658`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.054483`, as_primary `0`, as_primary_hit `None`, avg `0.010443`, median `0.022038`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.077225`, as_primary `0`, as_primary_hit `None`, avg `0.045819`, median `0.065617`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.02731`, as_primary `80`, as_primary_hit `0.525`, avg `0.00119`, median `0.003038`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.027839`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.000877`, median `0.000448`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.032332`, as_primary `80`, as_primary_hit `0.5125`, avg `0.001941`, median `0.003658`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.053304`, as_primary `80`, as_primary_hit `0.625`, avg `0.010443`, median `0.022038`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.084073`, as_primary `80`, as_primary_hit `0.675`, avg `0.045819`, median `0.065617`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.020924`, as_primary `0`, as_primary_hit `None`, avg `0.00119`, median `0.003038`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.021481`, as_primary `0`, as_primary_hit `None`, avg `-0.000877`, median `0.000448`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.025633`, as_primary `0`, as_primary_hit `None`, avg `0.001941`, median `0.003658`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.033517`, as_primary `0`, as_primary_hit `None`, avg `0.010443`, median `0.022038`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.066723`, as_primary `0`, as_primary_hit `None`, avg `0.045819`, median `0.065617`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.02731`, avg `0.00119`, median `0.003038`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4375`, primary_mae `0.027839`, avg `-0.000877`, median `0.000448`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.032332`, avg `0.001941`, median `0.003658`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.053304`, avg `0.010443`, median `0.022038`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.475`, primary_mae `0.084073`, avg `0.045819`, median `0.065617`

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
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.02731`, avg `0.00119`, median `0.003038`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4375`, primary_mae `0.027839`, avg `-0.000877`, median `0.000448`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.032332`, avg `0.001941`, median `0.003658`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.053304`, avg `0.010443`, median `0.022038`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.475`, primary_mae `0.084073`, avg `0.045819`, median `0.065617`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.02731, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4875, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.027839, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.032332, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.053304, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.084073, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020924, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02731, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.02731, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021481, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027839, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4875, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.027839, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.0375, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025633, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032332, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.032332, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033517, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054483, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.053304, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066723, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.084073, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.084073, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.042498`, avg `0.014081`, median `0.021724`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.045734`, avg `0.001344`, median `0.008703`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.060211`, avg `0.018349`, median `0.006008`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.072639`, avg `0.034973`, median `0.037208`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.142681`, avg `0.060364`, median `0.118517`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.035719`, avg `0.004565`, median `0.008482`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.043915`, avg `0.002613`, median `0.012478`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.051588`, avg `0.006667`, median `0.001141`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.069312`, avg `0.032468`, median `0.035916`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.149025`, avg `0.065075`, median `0.115499`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.030308`, avg `0.007774`, median `0.017715`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.033473`, avg `0.009258`, median `0.011083`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.036539`, avg `0.006146`, median `0.010051`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.055522`, avg `-0.032988`, median `-0.048417`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.072783`, avg `0.038414`, median `0.039156`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.02731`, avg `0.00119`, median `0.003038`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4375`, primary_mae `0.027839`, avg `-0.000877`, median `0.000448`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.032332`, avg `0.001941`, median `0.003658`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.053304`, avg `0.010443`, median `0.022038`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.475`, primary_mae `0.084073`, avg `0.045819`, median `0.065617`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.02731`, avg `0.00119`, median `0.003038`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4375`, primary_mae `0.027839`, avg `-0.000877`, median `0.000448`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.032332`, avg `0.001941`, median `0.003658`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.053304`, avg `0.010443`, median `0.022038`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.475`, primary_mae `0.084073`, avg `0.045819`, median `0.065617`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.026808`, avg `0.000805`, median `-0.00013`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.4333`, primary_mae `0.027333`, avg `-0.002988`, median `-7.7e-05`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.5167`, primary_mae `0.030897`, avg `0.001339`, median `-0.001481`
- 20d: sample `60`, primary_hit `0.3`, primary_closer `0.3833`, primary_mae `0.047642`, avg `0.019874`, median `0.029262`
- 60d: sample `60`, primary_hit `0.3333`, primary_closer `0.5`, primary_mae `0.086916`, avg `0.044388`, median `0.070221`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.028815`, avg `0.002344`, median `0.00965`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.029356`, avg `0.005457`, median `0.005361`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.036636`, avg `0.003746`, median `0.010051`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.070291`, avg `-0.017848`, median `-0.023373`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.075542`, avg `0.05011`, median `0.039777`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.02731`, avg `0.00119`, median `0.003038`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4375`, primary_mae `0.027839`, avg `-0.000877`, median `0.000448`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.032332`, avg `0.001941`, median `0.003658`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.053304`, avg `0.010443`, median `0.022038`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.475`, primary_mae `0.084073`, avg `0.045819`, median `0.065617`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.02731`, avg `0.00119`, median `0.003038`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4375`, primary_mae `0.027839`, avg `-0.000877`, median `0.000448`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.032332`, avg `0.001941`, median `0.003658`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.053304`, avg `0.010443`, median `0.022038`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.475`, primary_mae `0.084073`, avg `0.045819`, median `0.065617`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.02731`, avg `0.00119`, median `0.003038`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.4375`, primary_mae `0.027839`, avg `-0.000877`, median `0.000448`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.032332`, avg `0.001941`, median `0.003658`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.053304`, avg `0.010443`, median `0.022038`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.475`, primary_mae `0.084073`, avg `0.045819`, median `0.065617`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
