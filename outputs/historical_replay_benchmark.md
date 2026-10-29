# Historical Replay Benchmark

Generated at: `2026-10-29T18:31:42.554070+00:00`
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
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.017142`
- secondary_mean_absolute_error: `0.015615`
- primary_error_advantage: `-0.001527`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.024216`
- secondary_mean_absolute_error: `0.019676`
- primary_error_advantage: `-0.00454`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.031323`
- secondary_mean_absolute_error: `0.030398`
- primary_error_advantage: `-0.000925`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.041309`
- secondary_mean_absolute_error: `0.032146`
- primary_error_advantage: `-0.009163`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.04784`
- secondary_mean_absolute_error: `0.044515`
- primary_error_advantage: `-0.003325`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.016839`, as_primary `0`, as_primary_hit `None`, avg `0.004251`, median `0.006251`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.021693`, as_primary `0`, as_primary_hit `None`, avg `0.004669`, median `0.005385`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.026617`, as_primary `0`, as_primary_hit `None`, avg `0.015708`, median `0.014536`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.027901`, as_primary `0`, as_primary_hit `None`, avg `0.025688`, median `0.028743`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.045567`, as_primary `0`, as_primary_hit `None`, avg `0.050207`, median `0.055668`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.018325`, as_primary `60`, as_primary_hit `0.6667`, avg `0.004251`, median `0.006251`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.024137`, as_primary `60`, as_primary_hit `0.5667`, avg `0.004669`, median `0.005385`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.033786`, as_primary `60`, as_primary_hit `0.7333`, avg `0.015708`, median `0.014536`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.040903`, as_primary `60`, as_primary_hit `0.8`, avg `0.025688`, median `0.028743`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.048166`, as_primary `60`, as_primary_hit `0.7667`, avg `0.050207`, median `0.055668`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.017637`, as_primary `20`, as_primary_hit `0.45`, avg `0.004251`, median `0.006251`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.021747`, as_primary `20`, as_primary_hit `0.55`, avg `0.004669`, median `0.005385`
- 10d: sample `80`, direction_hit `0.2875`, path_mae `0.037673`, as_primary `20`, as_primary_hit `0.65`, avg `0.015708`, median `0.014536`
- 20d: sample `80`, direction_hit `0.2125`, path_mae `0.050163`, as_primary `20`, as_primary_hit `0.75`, avg `0.025688`, median `0.028743`
- 60d: sample `80`, direction_hit `0.1875`, path_mae `0.058272`, as_primary `20`, as_primary_hit `0.95`, avg `0.050207`, median `0.055668`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.015648`, as_primary `0`, as_primary_hit `None`, avg `0.004251`, median `0.006251`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.019676`, as_primary `0`, as_primary_hit `None`, avg `0.004669`, median `0.005385`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.025105`, as_primary `0`, as_primary_hit `None`, avg `0.015708`, median `0.014536`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.026851`, as_primary `0`, as_primary_hit `None`, avg `0.025688`, median `0.028743`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.044074`, as_primary `0`, as_primary_hit `None`, avg `0.050207`, median `0.055668`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6667`, primary_closer `0.4`, primary_mae `0.014804`, avg `0.005792`, median `0.006323`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.3833`, primary_mae `0.023589`, avg `0.006677`, median `0.006642`
- 10d: sample `60`, primary_hit `0.7333`, primary_closer `0.5167`, primary_mae `0.031618`, avg `0.015895`, median `0.016465`
- 20d: sample `60`, primary_hit `0.8`, primary_closer `0.3833`, primary_mae `0.037667`, avg `0.025893`, median `0.028743`
- 60d: sample `60`, primary_hit `0.7667`, primary_closer `0.4667`, primary_mae `0.048171`, avg `0.043497`, median `0.055351`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.024155`, avg `-0.000372`, median `-0.007516`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.026099`, avg `-0.001354`, median `0.004066`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.030437`, avg `0.015147`, median `0.009373`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.052235`, avg `0.025074`, median `0.023666`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.35`, primary_mae `0.046848`, avg `0.070339`, median `0.059139`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.019167`, avg `0.008251`, median `0.008204`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.030929`, avg `0.004834`, median `-0.000258`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.039619`, avg `0.017251`, median `0.015525`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.041561`, avg `0.029679`, median `0.028445`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.45`, primary_mae `0.042301`, avg `0.053025`, median `0.066906`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.024155`, avg `-0.000372`, median `-0.007516`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.026099`, avg `-0.001354`, median `0.004066`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.030437`, avg `0.015147`, median `0.009373`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.052235`, avg `0.025074`, median `0.023666`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.35`, primary_mae `0.046848`, avg `0.070339`, median `0.059139`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.012622`, avg `0.004562`, median `0.006323`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.019919`, avg `0.007598`, median `0.008893`
- 10d: sample `40`, primary_hit `0.775`, primary_closer `0.625`, primary_mae `0.027618`, avg `0.015217`, median `0.017155`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.45`, primary_mae `0.035719`, avg `0.024`, median `0.029059`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.475`, primary_mae `0.051105`, avg `0.038733`, median `0.050858`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.012622, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.019919, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.027618, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.035719, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.042301, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015648, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018325, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.012622, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019676, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024137, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.019919, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025105, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037673, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.027618, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026851, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050163, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.035719, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044074, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058272, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.042301, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.023912`, avg `0.003864`, median `0.002901`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.028854`, avg `0.008008`, median `0.00228`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.036719`, avg `0.019334`, median `0.022448`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.038308`, avg `0.033152`, median `0.02973`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.032095`, avg `0.061844`, median `0.070816`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.02129`, avg `0.005813`, median `0.005236`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.031907`, avg `0.00377`, median `-0.000258`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.04284`, avg `0.014235`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.043904`, avg `0.027515`, median `0.028445`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.4375`, primary_mae `0.039326`, avg `0.053366`, median `0.066906`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.026595`, avg `-0.000592`, median `-0.007516`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.027417`, avg `-0.000573`, median `0.005385`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.032041`, avg `0.017204`, median `0.018098`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.059071`, avg `0.031268`, median `0.042586`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.3125`, primary_mae `0.049799`, avg `0.063473`, median `0.052482`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.017142`, avg `0.004251`, median `0.006251`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.024216`, avg `0.004669`, median `0.005385`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5`, primary_mae `0.031323`, avg `0.015708`, median `0.014536`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.35`, primary_mae `0.041309`, avg `0.025688`, median `0.028743`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4375`, primary_mae `0.04784`, avg `0.050207`, median `0.055668`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.017142`, avg `0.004251`, median `0.006251`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.024216`, avg `0.004669`, median `0.005385`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5`, primary_mae `0.031323`, avg `0.015708`, median `0.014536`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.35`, primary_mae `0.041309`, avg `0.025688`, median `0.028743`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4375`, primary_mae `0.04784`, avg `0.050207`, median `0.055668`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6667`, primary_closer `0.4`, primary_mae `0.014804`, avg `0.005792`, median `0.006323`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.3833`, primary_mae `0.023589`, avg `0.006677`, median `0.006642`
- 10d: sample `60`, primary_hit `0.7333`, primary_closer `0.5167`, primary_mae `0.031618`, avg `0.015895`, median `0.016465`
- 20d: sample `60`, primary_hit `0.8`, primary_closer `0.3833`, primary_mae `0.037667`, avg `0.025893`, median `0.028743`
- 60d: sample `60`, primary_hit `0.7667`, primary_closer `0.4667`, primary_mae `0.048171`, avg `0.043497`, median `0.055351`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.024155`, avg `-0.000372`, median `-0.007516`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.026099`, avg `-0.001354`, median `0.004066`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.030437`, avg `0.015147`, median `0.009373`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.052235`, avg `0.025074`, median `0.023666`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.35`, primary_mae `0.046848`, avg `0.070339`, median `0.059139`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.017142`, avg `0.004251`, median `0.006251`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.024216`, avg `0.004669`, median `0.005385`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5`, primary_mae `0.031323`, avg `0.015708`, median `0.014536`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.35`, primary_mae `0.041309`, avg `0.025688`, median `0.028743`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4375`, primary_mae `0.04784`, avg `0.050207`, median `0.055668`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.019468`, avg `0.005271`, median `0.00948`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.3667`, primary_mae `0.026614`, avg `0.006846`, median `0.011038`
- 10d: sample `60`, primary_hit `0.6167`, primary_closer `0.4333`, primary_mae `0.031398`, avg `0.020325`, median `0.022878`
- 20d: sample `60`, primary_hit `0.6333`, primary_closer `0.2833`, primary_mae `0.043031`, avg `0.030005`, median `0.03148`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.4333`, primary_mae `0.04572`, avg `0.05977`, median `0.06498`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.4125`, primary_mae `0.017142`, avg `0.004251`, median `0.006251`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.024216`, avg `0.004669`, median `0.005385`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5`, primary_mae `0.031323`, avg `0.015708`, median `0.014536`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.35`, primary_mae `0.041309`, avg `0.025688`, median `0.028743`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4375`, primary_mae `0.04784`, avg `0.050207`, median `0.055668`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
