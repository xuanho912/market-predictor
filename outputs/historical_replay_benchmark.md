# Historical Replay Benchmark

Generated at: `2026-11-05T20:01:29.544351+00:00`
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
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.029036`
- secondary_mean_absolute_error: `0.023435`
- primary_error_advantage: `-0.005601`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.038903`
- secondary_mean_absolute_error: `0.028926`
- primary_error_advantage: `-0.009977`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.2375`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.069336`
- secondary_mean_absolute_error: `0.050221`
- primary_error_advantage: `-0.019115`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.116523`
- secondary_mean_absolute_error: `0.059636`
- primary_error_advantage: `-0.056887`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.102702`
- secondary_mean_absolute_error: `0.065403`
- primary_error_advantage: `-0.037299`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.021288`, as_primary `0`, as_primary_hit `None`, avg `0.003785`, median `0.010159`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.026973`, as_primary `0`, as_primary_hit `None`, avg `0.007207`, median `0.012755`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.04579`, as_primary `0`, as_primary_hit `None`, avg `0.011867`, median `0.027424`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.053613`, as_primary `0`, as_primary_hit `None`, avg `0.016964`, median `0.040226`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.062028`, as_primary `0`, as_primary_hit `None`, avg `0.03988`, median `0.055256`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.023228`, as_primary `0`, as_primary_hit `None`, avg `0.003785`, median `0.010159`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.030757`, as_primary `0`, as_primary_hit `None`, avg `0.007207`, median `0.012755`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.052042`, as_primary `0`, as_primary_hit `None`, avg `0.011867`, median `0.027424`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.072246`, as_primary `0`, as_primary_hit `None`, avg `0.016964`, median `0.040226`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.072712`, as_primary `0`, as_primary_hit `None`, avg `0.03988`, median `0.055256`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.029036`, as_primary `80`, as_primary_hit `0.625`, avg `0.003785`, median `0.010159`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.038903`, as_primary `80`, as_primary_hit `0.6125`, avg `0.007207`, median `0.012755`
- 10d: sample `80`, direction_hit `0.375`, path_mae `0.069336`, as_primary `80`, as_primary_hit `0.6125`, avg `0.011867`, median `0.027424`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.116523`, as_primary `80`, as_primary_hit `0.675`, avg `0.016964`, median `0.040226`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.102702`, as_primary `80`, as_primary_hit `0.725`, avg `0.03988`, median `0.055256`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.02129`, as_primary `0`, as_primary_hit `None`, avg `0.003785`, median `0.010159`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.026789`, as_primary `0`, as_primary_hit `None`, avg `0.007207`, median `0.012755`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.04561`, as_primary `0`, as_primary_hit `None`, avg `0.011867`, median `0.027424`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.054348`, as_primary `0`, as_primary_hit `None`, avg `0.016964`, median `0.040226`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.062878`, as_primary `0`, as_primary_hit `None`, avg `0.03988`, median `0.055256`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.029036`, avg `0.003785`, median `0.010159`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.35`, primary_mae `0.038903`, avg `0.007207`, median `0.012755`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.069336`, avg `0.011867`, median `0.027424`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.116523`, avg `0.016964`, median `0.040226`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.102702`, avg `0.03988`, median `0.055256`

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
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.029036`, avg `0.003785`, median `0.010159`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.35`, primary_mae `0.038903`, avg `0.007207`, median `0.012755`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.069336`, avg `0.011867`, median `0.027424`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.116523`, avg `0.016964`, median `0.040226`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.102702`, avg `0.03988`, median `0.055256`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.029036, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3875, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.038903, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.069336, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.116523, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.102702, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021288, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029036, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.029036, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026789, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038903, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3875, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.038903, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.2375, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04561, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069336, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.069336, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053613, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.116523, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.116523, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062028, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.102702, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.102702, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.029066`, avg `0.006992`, median `0.011369`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.024606`, avg `0.006574`, median `0.015572`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.054687`, avg `0.011358`, median `0.007589`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.089771`, avg `0.019063`, median `0.021287`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.07346`, avg `0.024882`, median `0.041669`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.030339`, avg `0.003571`, median `0.008712`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.025665`, avg `0.006388`, median `0.011845`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.051795`, avg `0.005021`, median `0.003439`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.097209`, avg `0.005758`, median `0.024327`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.069877`, avg `0.019292`, median `0.039614`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.6875`, primary_mae `0.026769`, avg `0.003884`, median `0.01284`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.028259`, avg `0.023728`, median `0.01808`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.070417`, avg `0.043786`, median `0.058207`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.0625`, primary_mae `0.108473`, avg `0.058392`, median `0.067551`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.117203`, avg `0.063687`, median `0.093613`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.029036`, avg `0.003785`, median `0.010159`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.35`, primary_mae `0.038903`, avg `0.007207`, median `0.012755`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.069336`, avg `0.011867`, median `0.027424`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.116523`, avg `0.016964`, median `0.040226`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.102702`, avg `0.03988`, median `0.055256`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.029036`, avg `0.003785`, median `0.010159`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.35`, primary_mae `0.038903`, avg `0.007207`, median `0.012755`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.069336`, avg `0.011867`, median `0.027424`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.116523`, avg `0.016964`, median `0.040226`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.102702`, avg `0.03988`, median `0.055256`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.3833`, primary_mae `0.030755`, avg `0.003917`, median `0.008997`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.35`, primary_mae `0.042302`, avg `0.003143`, median `0.011845`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.45`, primary_mae `0.070426`, avg `0.003927`, median `0.011637`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.2833`, primary_mae `0.121987`, avg `0.007403`, median `0.028426`
- 60d: sample `60`, primary_hit `0.2833`, primary_closer `0.2667`, primary_mae `0.09997`, avg `0.031401`, median `0.051172`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.6`, primary_mae `0.023879`, avg `0.003392`, median `0.011882`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.028706`, avg `0.019399`, median `0.01808`
- 10d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.066065`, avg `0.035685`, median `0.05436`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.15`, primary_mae `0.10013`, avg `0.045646`, median `0.063528`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.110899`, avg `0.065317`, median `0.093613`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.029036`, avg `0.003785`, median `0.010159`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.35`, primary_mae `0.038903`, avg `0.007207`, median `0.012755`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.069336`, avg `0.011867`, median `0.027424`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.116523`, avg `0.016964`, median `0.040226`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.102702`, avg `0.03988`, median `0.055256`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.029036`, avg `0.003785`, median `0.010159`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.35`, primary_mae `0.038903`, avg `0.007207`, median `0.012755`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.069336`, avg `0.011867`, median `0.027424`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.116523`, avg `0.016964`, median `0.040226`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.102702`, avg `0.03988`, median `0.055256`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.029036`, avg `0.003785`, median `0.010159`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.35`, primary_mae `0.038903`, avg `0.007207`, median `0.012755`
- 10d: sample `80`, primary_hit `0.375`, primary_closer `0.3875`, primary_mae `0.069336`, avg `0.011867`, median `0.027424`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.116523`, avg `0.016964`, median `0.040226`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.102702`, avg `0.03988`, median `0.055256`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
