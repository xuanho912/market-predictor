# Historical Replay Benchmark

Generated at: `2026-08-29T04:11:17.518643+00:00`
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
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.019219`
- secondary_mean_absolute_error: `0.016858`
- primary_error_advantage: `-0.002361`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.7`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.024039`
- secondary_mean_absolute_error: `0.021098`
- primary_error_advantage: `-0.002941`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.038997`
- secondary_mean_absolute_error: `0.033598`
- primary_error_advantage: `-0.005399`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.75`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.060703`
- secondary_mean_absolute_error: `0.038315`
- primary_error_advantage: `-0.022388`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3375`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.7`
- secondary_hit_rate: `0.775`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.055008`
- secondary_mean_absolute_error: `0.053158`
- primary_error_advantage: `-0.00185`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.525`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7125`, path_mae `0.016282`, as_primary `0`, as_primary_hit `None`, avg `0.007384`, median `0.012177`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.020318`, as_primary `0`, as_primary_hit `None`, avg `0.011149`, median `0.014525`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.031819`, as_primary `0`, as_primary_hit `None`, avg `0.013442`, median `0.021377`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.039942`, as_primary `0`, as_primary_hit `None`, avg `0.028051`, median `0.030996`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.052383`, as_primary `0`, as_primary_hit `None`, avg `0.061483`, median `0.075373`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7125`, path_mae `0.018377`, as_primary `60`, as_primary_hit `0.75`, avg `0.007384`, median `0.012177`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.023907`, as_primary `60`, as_primary_hit `0.7667`, avg `0.011149`, median `0.014525`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.039328`, as_primary `60`, as_primary_hit `0.7167`, avg `0.013442`, median `0.021377`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.05605`, as_primary `60`, as_primary_hit `0.8333`, avg `0.028051`, median `0.030996`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.054914`, as_primary `60`, as_primary_hit `0.8167`, avg `0.061483`, median `0.075373`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.2875`, path_mae `0.023494`, as_primary `20`, as_primary_hit `0.6`, avg `0.007384`, median `0.012177`
- 5d: sample `80`, direction_hit `0.3`, path_mae `0.028766`, as_primary `20`, as_primary_hit `0.5`, avg `0.011149`, median `0.014525`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.050116`, as_primary `20`, as_primary_hit `0.45`, avg `0.013442`, median `0.021377`
- 20d: sample `80`, direction_hit `0.25`, path_mae `0.062781`, as_primary `20`, as_primary_hit `0.5`, avg `0.028051`, median `0.030996`
- 60d: sample `80`, direction_hit `0.225`, path_mae `0.070758`, as_primary `20`, as_primary_hit `0.65`, avg `0.061483`, median `0.075373`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7125`, path_mae `0.016454`, as_primary `0`, as_primary_hit `None`, avg `0.007384`, median `0.012177`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.020197`, as_primary `0`, as_primary_hit `None`, avg `0.011149`, median `0.014525`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.032139`, as_primary `0`, as_primary_hit `None`, avg `0.013442`, median `0.021377`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.037084`, as_primary `0`, as_primary_hit `None`, avg `0.028051`, median `0.030996`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.053122`, as_primary `0`, as_primary_hit `None`, avg `0.061483`, median `0.075373`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.019219`, avg `0.007384`, median `0.012177`
- 5d: sample `80`, primary_hit `0.7`, primary_closer `0.4375`, primary_mae `0.024039`, avg `0.011149`, median `0.014525`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.4375`, primary_mae `0.038997`, avg `0.013442`, median `0.021377`
- 20d: sample `80`, primary_hit `0.75`, primary_closer `0.3375`, primary_mae `0.060703`, avg `0.028051`, median `0.030996`
- 60d: sample `80`, primary_hit `0.7`, primary_closer `0.525`, primary_mae `0.055008`, avg `0.061483`, median `0.075373`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6`, primary_closer `0.4667`, primary_mae `0.019358`, avg `0.004606`, median `0.010603`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.4833`, primary_mae `0.023289`, avg `0.007174`, median `0.009981`
- 10d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.037051`, avg `0.007813`, median `0.017431`
- 20d: sample `60`, primary_hit `0.7167`, primary_closer `0.3667`, primary_mae `0.049785`, avg `0.018858`, median `0.028173`
- 60d: sample `60`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.04759`, avg `0.049773`, median `0.069194`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.85`, primary_closer `0.4`, primary_mae `0.018799`, avg `0.015719`, median `0.018551`
- 5d: sample `20`, primary_hit `0.9`, primary_closer `0.3`, primary_mae `0.026288`, avg `0.023075`, median `0.02518`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.044832`, avg `0.030329`, median `0.043572`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.25`, primary_mae `0.093456`, avg `0.055633`, median `0.04979`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.45`, primary_mae `0.077263`, avg `0.096616`, median `0.110038`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018799, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.023289, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.037051, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7167, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.049785, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.04759, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016282, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023494, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018799, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020197, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028766, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.023289, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031819, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050116, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.037051, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037084, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062781, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7167, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.049785, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.775, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052383, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070758, 'direction_hit_rate': 0.225}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.04759, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.013521`, avg `0.012736`, median `0.021989`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.018562`, avg `0.01665`, median `0.022294`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.022735`, avg `0.020096`, median `0.030411`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.375`, primary_mae `0.024263`, avg `0.05728`, median `0.060676`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.031922`, avg `0.0807`, median `0.096338`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.01302`, avg `0.0114`, median `0.017216`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.5`, primary_mae `0.018627`, avg `0.017882`, median `0.020142`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.02601`, avg `0.019728`, median `0.024318`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.25`, primary_mae `0.038837`, avg `0.042698`, median `0.03746`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.4375`, primary_mae `0.040618`, avg `0.07335`, median `0.088751`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.018282`, avg `0.001006`, median `0.005901`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.024386`, avg `0.003252`, median `0.00873`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.038585`, avg `-0.002431`, median `0.002362`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.06218`, avg `0.001055`, median `0.0272`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.045893`, avg `0.037052`, median `0.04549`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.019219`, avg `0.007384`, median `0.012177`
- 5d: sample `80`, primary_hit `0.7`, primary_closer `0.4375`, primary_mae `0.024039`, avg `0.011149`, median `0.014525`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.4375`, primary_mae `0.038997`, avg `0.013442`, median `0.021377`
- 20d: sample `80`, primary_hit `0.75`, primary_closer `0.3375`, primary_mae `0.060703`, avg `0.028051`, median `0.030996`
- 60d: sample `80`, primary_hit `0.7`, primary_closer `0.525`, primary_mae `0.055008`, avg `0.061483`, median `0.075373`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.019219`, avg `0.007384`, median `0.012177`
- 5d: sample `80`, primary_hit `0.7`, primary_closer `0.4375`, primary_mae `0.024039`, avg `0.011149`, median `0.014525`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.4375`, primary_mae `0.038997`, avg `0.013442`, median `0.021377`
- 20d: sample `80`, primary_hit `0.75`, primary_closer `0.3375`, primary_mae `0.060703`, avg `0.028051`, median `0.030996`
- 60d: sample `80`, primary_hit `0.7`, primary_closer `0.525`, primary_mae `0.055008`, avg `0.061483`, median `0.075373`

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
- 3d: sample `60`, primary_hit `0.6667`, primary_closer `0.4833`, primary_mae `0.016202`, avg `0.009196`, median `0.012522`
- 5d: sample `60`, primary_hit `0.7333`, primary_closer `0.4333`, primary_mae `0.022134`, avg `0.013689`, median `0.015064`
- 10d: sample `60`, primary_hit `0.7`, primary_closer `0.4667`, primary_mae `0.034434`, avg `0.015034`, median `0.022309`
- 20d: sample `60`, primary_hit `0.7667`, primary_closer `0.3333`, primary_mae `0.062019`, avg `0.032853`, median `0.032209`
- 60d: sample `60`, primary_hit `0.7`, primary_closer `0.4833`, primary_mae `0.052981`, avg `0.069413`, median `0.082215`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.019219`, avg `0.007384`, median `0.012177`
- 5d: sample `80`, primary_hit `0.7`, primary_closer `0.4375`, primary_mae `0.024039`, avg `0.011149`, median `0.014525`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.4375`, primary_mae `0.038997`, avg `0.013442`, median `0.021377`
- 20d: sample `80`, primary_hit `0.75`, primary_closer `0.3375`, primary_mae `0.060703`, avg `0.028051`, median `0.030996`
- 60d: sample `80`, primary_hit `0.7`, primary_closer `0.525`, primary_mae `0.055008`, avg `0.061483`, median `0.075373`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.45`, primary_mae `0.019219`, avg `0.007384`, median `0.012177`
- 5d: sample `80`, primary_hit `0.7`, primary_closer `0.4375`, primary_mae `0.024039`, avg `0.011149`, median `0.014525`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.4375`, primary_mae `0.038997`, avg `0.013442`, median `0.021377`
- 20d: sample `80`, primary_hit `0.75`, primary_closer `0.3375`, primary_mae `0.060703`, avg `0.028051`, median `0.030996`
- 60d: sample `80`, primary_hit `0.7`, primary_closer `0.525`, primary_mae `0.055008`, avg `0.061483`, median `0.075373`

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
