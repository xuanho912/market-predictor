# Historical Replay Benchmark

Generated at: `2026-09-03T23:35:53.474180+00:00`
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
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.015919`
- secondary_mean_absolute_error: `0.013802`
- primary_error_advantage: `-0.002117`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.019754`
- secondary_mean_absolute_error: `0.01598`
- primary_error_advantage: `-0.003774`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.026134`
- secondary_mean_absolute_error: `0.028256`
- primary_error_advantage: `0.002122`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.053172`
- secondary_mean_absolute_error: `0.040428`
- primary_error_advantage: `-0.012744`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.079923`
- secondary_mean_absolute_error: `0.065031`
- primary_error_advantage: `-0.014892`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3333`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.013915`, as_primary `0`, as_primary_hit `None`, avg `-0.000515`, median `0.000737`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.016329`, as_primary `0`, as_primary_hit `None`, avg `0.000868`, median `0.001056`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.021725`, as_primary `0`, as_primary_hit `None`, avg `-0.001961`, median `-0.008909`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.030336`, as_primary `0`, as_primary_hit `None`, avg `0.003052`, median `0.010265`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.05442`, as_primary `0`, as_primary_hit `None`, avg `0.023052`, median `0.037497`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.014408`, as_primary `0`, as_primary_hit `None`, avg `-0.000515`, median `0.000737`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.016731`, as_primary `0`, as_primary_hit `None`, avg `0.000868`, median `0.001056`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.029863`, as_primary `0`, as_primary_hit `None`, avg `-0.001961`, median `-0.008909`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.044642`, as_primary `0`, as_primary_hit `None`, avg `0.003052`, median `0.010265`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.068828`, as_primary `0`, as_primary_hit `None`, avg `0.023052`, median `0.037497`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.015919`, as_primary `80`, as_primary_hit `0.55`, avg `-0.000515`, median `0.000737`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.019754`, as_primary `80`, as_primary_hit `0.5625`, avg `0.000868`, median `0.001056`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.026134`, as_primary `80`, as_primary_hit `0.4`, avg `-0.001961`, median `-0.008909`
- 20d: sample `80`, direction_hit `0.4125`, path_mae `0.053172`, as_primary `80`, as_primary_hit `0.5875`, avg `0.003052`, median `0.010265`
- 60d: sample `80`, direction_hit `0.35`, path_mae `0.079923`, as_primary `80`, as_primary_hit `0.65`, avg `0.023052`, median `0.037497`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.013471`, as_primary `0`, as_primary_hit `None`, avg `-0.000515`, median `0.000737`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.015782`, as_primary `0`, as_primary_hit `None`, avg `0.000868`, median `0.001056`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.020517`, as_primary `0`, as_primary_hit `None`, avg `-0.001961`, median `-0.008909`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.030576`, as_primary `0`, as_primary_hit `None`, avg `0.003052`, median `0.010265`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.054934`, as_primary `0`, as_primary_hit `None`, avg `0.023052`, median `0.037497`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.3833`, primary_mae `0.017654`, avg `0.000367`, median `0.002683`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.4333`, primary_mae `0.02126`, avg `0.001758`, median `0.002104`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.4667`, primary_mae `0.028363`, avg `0.002213`, median `-0.000811`
- 20d: sample `60`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.051292`, avg `0.013393`, median `0.023635`
- 60d: sample `60`, primary_hit `0.2333`, primary_closer `0.3333`, primary_mae `0.086332`, avg `0.036219`, median `0.051777`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.010713`, avg `-0.003162`, median `-0.001535`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.015238`, avg `-0.001804`, median `0.000818`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.6`, primary_mae `0.019444`, avg `-0.014486`, median `-0.01712`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.058812`, avg `-0.027969`, median `-0.020035`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.060696`, avg `-0.016448`, median `-0.028583`

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
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.010713`, avg `-0.003162`, median `-0.001535`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.015238`, avg `-0.001804`, median `0.000818`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.6`, primary_mae `0.019444`, avg `-0.014486`, median `-0.01712`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.058812`, avg `-0.027969`, median `-0.020035`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.060696`, avg `-0.016448`, median `-0.028583`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.3833`, primary_mae `0.017654`, avg `0.000367`, median `0.002683`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.4333`, primary_mae `0.02126`, avg `0.001758`, median `0.002104`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.4667`, primary_mae `0.028363`, avg `0.002213`, median `-0.000811`
- 20d: sample `60`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.051292`, avg `0.013393`, median `0.023635`
- 60d: sample `60`, primary_hit `0.2333`, primary_closer `0.3333`, primary_mae `0.086332`, avg `0.036219`, median `0.051777`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.010713, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.015238, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.019444, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.051292, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.060696, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013471, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015919, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.010713, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015782, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019754, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.015238, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020517, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029863, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.019444, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030336, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053172, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.051292, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05442, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.079923, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.060696, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.016261`, avg `-0.007591`, median `0.001949`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.01733`, avg `-0.01205`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.025282`, avg `0.000185`, median `0.000295`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.052572`, avg `0.012354`, median `0.023299`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.080442`, avg `0.03306`, median `0.037982`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.01534`, avg `-0.003131`, median `-5e-05`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.014547`, avg `-0.005899`, median `-0.002115`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.026855`, avg `0.002803`, median `-0.000811`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.056786`, avg `0.017566`, median `0.030181`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.098054`, avg `0.043976`, median `0.062395`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.011099`, avg `-0.00288`, median `-0.000614`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.015265`, avg `-0.002594`, median `0.000818`
- 10d: sample `16`, primary_hit `0.875`, primary_closer `0.5625`, primary_mae `0.01833`, avg `-0.015427`, median `-0.016051`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.063004`, avg `-0.024574`, median `-0.015662`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.064339`, avg `-0.014024`, median `-0.019635`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.015919`, avg `-0.000515`, median `0.000737`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.019754`, avg `0.000868`, median `0.001056`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.026134`, avg `-0.001961`, median `-0.008909`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.375`, primary_mae `0.053172`, avg `0.003052`, median `0.010265`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.079923`, avg `0.023052`, median `0.037497`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.015919`, avg `-0.000515`, median `0.000737`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.019754`, avg `0.000868`, median `0.001056`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.026134`, avg `-0.001961`, median `-0.008909`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.375`, primary_mae `0.053172`, avg `0.003052`, median `0.010265`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.079923`, avg `0.023052`, median `0.037497`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.4333`, primary_mae `0.014557`, avg `-0.000794`, median `0.000402`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.4167`, primary_mae `0.016931`, avg `-0.000848`, median `0.000552`
- 10d: sample `60`, primary_hit `0.6333`, primary_closer `0.45`, primary_mae `0.025812`, avg `-0.002292`, median `-0.008909`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.3667`, primary_mae `0.050057`, avg `0.002962`, median `0.009981`
- 60d: sample `60`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.072277`, avg `0.028256`, median `0.047922`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.015919`, avg `-0.000515`, median `0.000737`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4`, primary_mae `0.019754`, avg `0.000868`, median `0.001056`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.026134`, avg `-0.001961`, median `-0.008909`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.375`, primary_mae `0.053172`, avg `0.003052`, median `0.010265`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.079923`, avg `0.023052`, median `0.037497`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.013065`, avg `-0.003422`, median `-0.001535`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.014878`, avg `-0.004249`, median `0.000552`
- 10d: sample `40`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.021125`, avg `-0.008127`, median `-0.013778`
- 20d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.057631`, avg `-0.004967`, median `-0.000495`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.081234`, avg `0.015224`, median `0.020962`

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
