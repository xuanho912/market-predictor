# Historical Replay Benchmark

Generated at: `2026-06-19T23:43:33.429195+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons', 'forward validation completed samples are below the minimum gate'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.01592`
- secondary_mean_absolute_error: `0.013878`
- primary_error_advantage: `-0.002042`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.019908`
- secondary_mean_absolute_error: `0.016208`
- primary_error_advantage: `-0.0037`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.030689`
- secondary_mean_absolute_error: `0.024493`
- primary_error_advantage: `-0.006196`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.053203`
- secondary_mean_absolute_error: `0.046082`
- primary_error_advantage: `-0.007121`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.058584`
- secondary_mean_absolute_error: `0.053088`
- primary_error_advantage: `-0.005496`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.014348`, as_primary `0`, as_primary_hit `None`, avg `0.005437`, median `0.004555`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.016532`, as_primary `0`, as_primary_hit `None`, avg `0.006523`, median `0.006004`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.022296`, as_primary `0`, as_primary_hit `None`, avg `0.00538`, median `0.005897`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.028433`, as_primary `0`, as_primary_hit `None`, avg `0.003654`, median `0.009462`
- 60d: sample `80`, direction_hit `0.5`, path_mae `0.046593`, as_primary `0`, as_primary_hit `None`, avg `0.010989`, median `0.001124`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.015777`, as_primary `40`, as_primary_hit `0.5`, avg `0.005437`, median `0.004555`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.017933`, as_primary `40`, as_primary_hit `0.625`, avg `0.006523`, median `0.006004`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.027056`, as_primary `40`, as_primary_hit `0.475`, avg `0.00538`, median `0.005897`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.04399`, as_primary `40`, as_primary_hit `0.5`, avg `0.003654`, median `0.009462`
- 60d: sample `80`, direction_hit `0.5`, path_mae `0.059255`, as_primary `40`, as_primary_hit `0.425`, avg `0.010989`, median `0.001124`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.014021`, as_primary `40`, as_primary_hit `0.7`, avg `0.005437`, median `0.004555`
- 5d: sample `80`, direction_hit `0.3`, path_mae `0.018184`, as_primary `40`, as_primary_hit `0.775`, avg `0.006523`, median `0.006004`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.028125`, as_primary `40`, as_primary_hit `0.65`, avg `0.00538`, median `0.005897`
- 20d: sample `80`, direction_hit `0.4125`, path_mae `0.055295`, as_primary `40`, as_primary_hit `0.675`, avg `0.003654`, median `0.009462`
- 60d: sample `80`, direction_hit `0.5`, path_mae `0.052418`, as_primary `40`, as_primary_hit `0.575`, avg `0.010989`, median `0.001124`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.013607`, as_primary `0`, as_primary_hit `None`, avg `0.005437`, median `0.004555`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.015849`, as_primary `0`, as_primary_hit `None`, avg `0.006523`, median `0.006004`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.021615`, as_primary `0`, as_primary_hit `None`, avg `0.00538`, median `0.005897`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.027922`, as_primary `0`, as_primary_hit `None`, avg `0.003654`, median `0.009462`
- 60d: sample `80`, direction_hit `0.5`, path_mae `0.043282`, as_primary `0`, as_primary_hit `None`, avg `0.010989`, median `0.001124`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.3667`, primary_mae `0.017124`, avg `0.005615`, median `0.003213`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.3833`, primary_mae `0.020613`, avg `0.0065`, median `0.005205`
- 10d: sample `60`, primary_hit `0.4167`, primary_closer `0.3833`, primary_mae `0.031769`, avg `0.007311`, median `0.005479`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.048359`, avg `0.008106`, median `0.013848`
- 60d: sample `60`, primary_hit `0.3333`, primary_closer `0.4833`, primary_mae `0.055548`, avg `0.020298`, median `0.028569`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.012309`, avg `0.004904`, median `0.008878`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.017793`, avg `0.00659`, median `0.010885`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.027446`, avg `-0.000412`, median `0.005897`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.067733`, avg `-0.009702`, median `0.002802`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.067694`, avg `-0.016939`, median `-0.011068`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.01624`, avg `0.003245`, median `-0.000261`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.018293`, avg `0.003164`, median `0.00337`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.026269`, avg `0.00284`, median `-0.003297`
- 20d: sample `40`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.045353`, avg `-0.000401`, median `0.000176`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.05994`, avg `0.00065`, median `-0.015624`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.012309`, avg `0.004904`, median `0.008878`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.017793`, avg `0.00659`, median `0.010885`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.027446`, avg `-0.000412`, median `0.005897`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.067733`, avg `-0.009702`, median `0.002802`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.067694`, avg `-0.016939`, median `-0.011068`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.018892`, avg `0.010354`, median `0.018118`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.025255`, avg `0.013172`, median `0.012456`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.042769`, avg `0.016253`, median `0.028201`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.054372`, avg `0.025121`, median `0.030284`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.6`, primary_mae `0.046764`, avg `0.059594`, median `0.062686`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.012309, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.017793, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.026269, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.045353, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.046764, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013607, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015777, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.012309, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015849, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018184, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.017793, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021615, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028125, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.026269, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027922, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055295, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.045353, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043282, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059255, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.046764, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.011616`, avg `0.002698`, median `0.001408`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.012305`, avg `0.003863`, median `0.002404`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.029489`, avg `0.004889`, median `0.004636`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.055817`, avg `-0.021094`, median `-0.017063`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.051624`, avg `0.035988`, median `0.066796`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.014311`, avg `0.004221`, median `0.000638`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.019928`, avg `-0.000595`, median `-0.001663`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.030832`, avg `0.007446`, median `0.001486`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.04213`, avg `-0.001574`, median `0.001452`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.059161`, avg `0.019018`, median `0.015626`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.1875`, primary_closer `0.375`, primary_mae `0.011711`, avg `0.006307`, median `0.008878`
- 5d: sample `16`, primary_hit `0.1875`, primary_closer `0.375`, primary_mae `0.01663`, avg `0.009329`, median `0.010885`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.024791`, avg `-0.000265`, median `0.003601`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.068316`, avg `-0.010914`, median `0.002802`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.067932`, avg `-0.008177`, median `-0.011068`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.01592`, avg `0.005437`, median `0.004555`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.019908`, avg `0.006523`, median `0.006004`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.030689`, avg `0.00538`, median `0.005897`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.053203`, avg `0.003654`, median `0.009462`
- 60d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.058584`, avg `0.010989`, median `0.001124`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.01592`, avg `0.005437`, median `0.004555`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.019908`, avg `0.006523`, median `0.006004`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.030689`, avg `0.00538`, median `0.005897`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.053203`, avg `0.003654`, median `0.009462`
- 60d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.058584`, avg `0.010989`, median `0.001124`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.01624`, avg `0.003245`, median `-0.000261`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.018293`, avg `0.003164`, median `0.00337`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.026269`, avg `0.00284`, median `-0.003297`
- 20d: sample `40`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.045353`, avg `-0.000401`, median `0.000176`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.05994`, avg `0.00065`, median `-0.015624`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.0156`, avg `0.007629`, median `0.012428`
- 5d: sample `40`, primary_hit `0.225`, primary_closer `0.4`, primary_mae `0.021524`, avg `0.009881`, median `0.010885`
- 10d: sample `40`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.035108`, avg `0.007921`, median `0.011745`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.275`, primary_mae `0.061052`, avg `0.00771`, median `0.016405`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.5`, primary_mae `0.057229`, avg `0.021327`, median `0.017569`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.01592`, avg `0.005437`, median `0.004555`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.019908`, avg `0.006523`, median `0.006004`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.030689`, avg `0.00538`, median `0.005897`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.053203`, avg `0.003654`, median `0.009462`
- 60d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.058584`, avg `0.010989`, median `0.001124`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.01592`, avg `0.005437`, median `0.004555`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.019908`, avg `0.006523`, median `0.006004`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.030689`, avg `0.00538`, median `0.005897`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.053203`, avg `0.003654`, median `0.009462`
- 60d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.058584`, avg `0.010989`, median `0.001124`

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
