# Historical Replay Benchmark

Generated at: `2026-10-21T01:12:38.961631+00:00`
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
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.019838`
- secondary_mean_absolute_error: `0.01654`
- primary_error_advantage: `-0.003298`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.022535`
- secondary_mean_absolute_error: `0.018444`
- primary_error_advantage: `-0.004091`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.041096`
- secondary_mean_absolute_error: `0.028043`
- primary_error_advantage: `-0.013053`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2625`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.475`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.056427`
- secondary_mean_absolute_error: `0.031634`
- primary_error_advantage: `-0.024793`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.067486`
- secondary_mean_absolute_error: `0.050534`
- primary_error_advantage: `-0.016952`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.017004`, as_primary `0`, as_primary_hit `None`, avg `0.002777`, median `0.006487`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.018995`, as_primary `0`, as_primary_hit `None`, avg `0.00149`, median `0.005717`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.0286`, as_primary `0`, as_primary_hit `None`, avg `0.001404`, median `0.006392`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.033778`, as_primary `0`, as_primary_hit `None`, avg `0.019438`, median `0.026514`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.050769`, as_primary `0`, as_primary_hit `None`, avg `0.066899`, median `0.075447`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.019006`, as_primary `0`, as_primary_hit `None`, avg `0.002777`, median `0.006487`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.021699`, as_primary `0`, as_primary_hit `None`, avg `0.00149`, median `0.005717`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.035599`, as_primary `0`, as_primary_hit `None`, avg `0.001404`, median `0.006392`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.046019`, as_primary `0`, as_primary_hit `None`, avg `0.019438`, median `0.026514`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.056254`, as_primary `0`, as_primary_hit `None`, avg `0.066899`, median `0.075447`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.019838`, as_primary `80`, as_primary_hit `0.5875`, avg `0.002777`, median `0.006487`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.022535`, as_primary `80`, as_primary_hit `0.5625`, avg `0.00149`, median `0.005717`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.041096`, as_primary `80`, as_primary_hit `0.575`, avg `0.001404`, median `0.006392`
- 20d: sample `80`, direction_hit `0.2625`, path_mae `0.056427`, as_primary `80`, as_primary_hit `0.7375`, avg `0.019438`, median `0.026514`
- 60d: sample `80`, direction_hit `0.1875`, path_mae `0.067486`, as_primary `80`, as_primary_hit `0.8125`, avg `0.066899`, median `0.075447`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.016599`, as_primary `0`, as_primary_hit `None`, avg `0.002777`, median `0.006487`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.018216`, as_primary `0`, as_primary_hit `None`, avg `0.00149`, median `0.005717`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.027903`, as_primary `0`, as_primary_hit `None`, avg `0.001404`, median `0.006392`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.031961`, as_primary `0`, as_primary_hit `None`, avg `0.019438`, median `0.026514`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.050516`, as_primary `0`, as_primary_hit `None`, avg `0.066899`, median `0.075447`

## Edge Status Performance

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.025185`, avg `-0.001594`, median `-0.009627`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.02367`, avg `-0.009289`, median `-0.014973`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.075321`, avg `-0.019569`, median `-0.021202`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.08067`, avg `0.007908`, median `0.008529`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.10019`, avg `0.075036`, median `0.089836`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.4167`, primary_mae `0.018055`, avg `0.004233`, median `0.00737`
- 5d: sample `60`, primary_hit `0.3667`, primary_closer `0.45`, primary_mae `0.022157`, avg `0.005083`, median `0.009271`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.3667`, primary_mae `0.029687`, avg `0.008395`, median `0.012931`
- 20d: sample `60`, primary_hit `0.2`, primary_closer `0.2667`, primary_mae `0.048346`, avg `0.023281`, median `0.027686`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.3167`, primary_mae `0.056584`, avg `0.064187`, median `0.065407`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.020958`, avg `-4.8e-05`, median `0.00281`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.021455`, avg `-0.00443`, median `-0.01267`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.04614`, avg `-0.006115`, median `-0.000275`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.055108`, avg `0.012809`, median `0.013482`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.325`, primary_mae `0.088561`, avg `0.069173`, median `0.075447`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.018103`, avg `0.008016`, median `0.016082`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.02011`, avg `0.009719`, median `0.011781`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.026596`, avg `0.014406`, median `0.02208`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.047377`, avg `0.042058`, median `0.040733`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.055965`, avg `0.073464`, median `0.093013`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.019332`, avg `0.003186`, median `0.006729`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.027121`, avg `0.005101`, median `0.010292`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.045506`, avg `0.003441`, median `0.008378`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.068114`, avg `0.010074`, median `0.028966`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.25`, primary_mae `0.036854`, avg `0.055786`, median `0.053187`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.018103, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.02011, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.026596, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.047377, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.036854, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016599, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019838, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.018103, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018216, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022535, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.02011, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027903, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041096, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.026596, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.475, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031961, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056427, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.047377, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050516, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067486, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.036854, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.024393`, avg `0.010505`, median `0.009432`
- 5d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.036859`, avg `0.016698`, median `0.014072`
- 10d: sample `8`, primary_hit `0.125`, primary_closer `0.0`, primary_mae `0.062112`, avg `0.021807`, median `0.022309`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.084315`, avg `0.03102`, median `0.032012`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.050712`, avg `0.079153`, median `0.085113`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.021751`, avg `0.006422`, median `0.009174`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.029307`, avg `0.006822`, median `0.011847`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.1875`, primary_mae `0.049628`, avg `0.007124`, median `0.016167`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.070984`, avg `0.011758`, median `0.028966`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.25`, primary_mae `0.038188`, avg `0.060472`, median `0.053187`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.02889`, avg `0.001018`, median `-0.001588`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.023539`, avg `-0.010677`, median `-0.014973`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.07642`, avg `-0.020952`, median `-0.032707`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.07591`, avg `0.001843`, median `-0.002909`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.096768`, avg `0.067056`, median `0.069259`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.019838`, avg `0.002777`, median `0.006487`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.022535`, avg `0.00149`, median `0.005717`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.041096`, avg `0.001404`, median `0.006392`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.2875`, primary_mae `0.056427`, avg `0.019438`, median `0.026514`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.067486`, avg `0.066899`, median `0.075447`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.019838`, avg `0.002777`, median `0.006487`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.022535`, avg `0.00149`, median `0.005717`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.041096`, avg `0.001404`, median `0.006392`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.2875`, primary_mae `0.056427`, avg `0.019438`, median `0.026514`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.067486`, avg `0.066899`, median `0.075447`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.35`, primary_closer `0.325`, primary_mae `0.018718`, avg `0.005601`, median `0.009174`
- 5d: sample `40`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.023615`, avg `0.00741`, median `0.010656`
- 10d: sample `40`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.036051`, avg `0.008924`, median `0.0183`
- 20d: sample `40`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.057745`, avg `0.026066`, median `0.032209`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.275`, primary_mae `0.04641`, avg `0.064625`, median `0.069623`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.020958`, avg `-4.8e-05`, median `0.00281`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.021455`, avg `-0.00443`, median `-0.01267`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.04614`, avg `-0.006115`, median `-0.000275`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.055108`, avg `0.012809`, median `0.013482`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.325`, primary_mae `0.088561`, avg `0.069173`, median `0.075447`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.019838`, avg `0.002777`, median `0.006487`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.022535`, avg `0.00149`, median `0.005717`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.041096`, avg `0.001404`, median `0.006392`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.2875`, primary_mae `0.056427`, avg `0.019438`, median `0.026514`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.067486`, avg `0.066899`, median `0.075447`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.019838`, avg `0.002777`, median `0.006487`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.022535`, avg `0.00149`, median `0.005717`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.041096`, avg `0.001404`, median `0.006392`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.2875`, primary_mae `0.056427`, avg `0.019438`, median `0.026514`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.067486`, avg `0.066899`, median `0.075447`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
