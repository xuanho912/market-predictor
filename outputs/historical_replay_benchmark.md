# Historical Replay Benchmark

Generated at: `2026-11-13T02:18:04.925241+00:00`
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
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.019578`
- secondary_mean_absolute_error: `0.01651`
- primary_error_advantage: `-0.003068`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.02653`
- secondary_mean_absolute_error: `0.021863`
- primary_error_advantage: `-0.004667`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.054001`
- secondary_mean_absolute_error: `0.034816`
- primary_error_advantage: `-0.019185`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.875`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.052638`
- secondary_mean_absolute_error: `0.039532`
- primary_error_advantage: `-0.013106`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.75`
- secondary_hit_rate: `0.925`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.053828`
- secondary_mean_absolute_error: `0.041975`
- primary_error_advantage: `-0.011853`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.75`, path_mae `0.015899`, as_primary `0`, as_primary_hit `None`, avg `0.011477`, median `0.012652`
- 5d: sample `80`, direction_hit `0.7375`, path_mae `0.022109`, as_primary `0`, as_primary_hit `None`, avg `0.015433`, median `0.017855`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.035135`, as_primary `0`, as_primary_hit `None`, avg `0.020585`, median `0.026366`
- 20d: sample `80`, direction_hit `0.875`, path_mae `0.040537`, as_primary `0`, as_primary_hit `None`, avg `0.042289`, median `0.03796`
- 60d: sample `80`, direction_hit `0.925`, path_mae `0.043449`, as_primary `0`, as_primary_hit `None`, avg `0.098521`, median `0.098004`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.75`, path_mae `0.017197`, as_primary `60`, as_primary_hit `0.7167`, avg `0.011477`, median `0.012652`
- 5d: sample `80`, direction_hit `0.7375`, path_mae `0.024983`, as_primary `60`, as_primary_hit `0.7`, avg `0.015433`, median `0.017855`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.045721`, as_primary `60`, as_primary_hit `0.7167`, avg `0.020585`, median `0.026366`
- 20d: sample `80`, direction_hit `0.875`, path_mae `0.053718`, as_primary `60`, as_primary_hit `0.8667`, avg `0.042289`, median `0.03796`
- 60d: sample `80`, direction_hit `0.925`, path_mae `0.056143`, as_primary `60`, as_primary_hit `0.95`, avg `0.098521`, median `0.098004`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.25`, path_mae `0.023352`, as_primary `20`, as_primary_hit `0.85`, avg `0.011477`, median `0.012652`
- 5d: sample `80`, direction_hit `0.2625`, path_mae `0.028987`, as_primary `20`, as_primary_hit `0.85`, avg `0.015433`, median `0.017855`
- 10d: sample `80`, direction_hit `0.2875`, path_mae `0.061003`, as_primary `20`, as_primary_hit `0.7`, avg `0.020585`, median `0.026366`
- 20d: sample `80`, direction_hit `0.125`, path_mae `0.075098`, as_primary `20`, as_primary_hit `0.9`, avg `0.042289`, median `0.03796`
- 60d: sample `80`, direction_hit `0.075`, path_mae `0.067326`, as_primary `20`, as_primary_hit `0.85`, avg `0.098521`, median `0.098004`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.75`, path_mae `0.01651`, as_primary `0`, as_primary_hit `None`, avg `0.011477`, median `0.012652`
- 5d: sample `80`, direction_hit `0.7375`, path_mae `0.021863`, as_primary `0`, as_primary_hit `None`, avg `0.015433`, median `0.017855`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.034816`, as_primary `0`, as_primary_hit `None`, avg `0.020585`, median `0.026366`
- 20d: sample `80`, direction_hit `0.875`, path_mae `0.039532`, as_primary `0`, as_primary_hit `None`, avg `0.042289`, median `0.03796`
- 60d: sample `80`, direction_hit `0.925`, path_mae `0.041975`, as_primary `0`, as_primary_hit `None`, avg `0.098521`, median `0.098004`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4125`, primary_mae `0.019578`, avg `0.011477`, median `0.012652`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3875`, primary_mae `0.02653`, avg `0.015433`, median `0.017855`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3375`, primary_mae `0.054001`, avg `0.020585`, median `0.026366`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4125`, primary_mae `0.052638`, avg `0.042289`, median `0.03796`
- 60d: sample `80`, primary_hit `0.75`, primary_closer `0.3625`, primary_mae `0.053828`, avg `0.098521`, median `0.098004`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.5`, primary_mae `0.015354`, avg `0.007578`, median `0.011685`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.425`, primary_mae `0.022312`, avg `0.009251`, median `0.011847`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.035871`, avg `0.009156`, median `0.014094`
- 20d: sample `40`, primary_hit `0.85`, primary_closer `0.5`, primary_mae `0.032818`, avg `0.031436`, median `0.035199`
- 60d: sample `40`, primary_hit `0.95`, primary_closer `0.45`, primary_mae `0.028209`, avg `0.081703`, median `0.087171`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.15`, primary_closer `0.15`, primary_mae `0.027777`, avg `0.015645`, median `0.016121`
- 5d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.038326`, avg `0.022195`, median `0.021135`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.1`, primary_mae `0.101642`, avg `0.024965`, median `0.030699`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.25`, primary_mae `0.095115`, avg `0.050125`, median `0.031305`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.09497`, avg `0.118317`, median `0.105065`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.8`, primary_closer `0.5`, primary_mae `0.019825`, avg `0.015108`, median `0.021826`
- 5d: sample `20`, primary_hit `0.8`, primary_closer `0.45`, primary_mae `0.02317`, avg `0.021034`, median `0.0241`
- 10d: sample `20`, primary_hit `0.95`, primary_closer `0.35`, primary_mae `0.04262`, avg `0.039061`, median `0.042218`
- 20d: sample `20`, primary_hit `0.9`, primary_closer `0.4`, primary_mae `0.049802`, avg `0.056159`, median `0.073748`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.25`, primary_mae `0.063923`, avg `0.112362`, median `0.122259`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.015354, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.022312, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.035871, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.032818, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.028209, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015899, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023352, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.015354, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021863, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028987, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.022312, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034816, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061003, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.035871, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.875, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039532, 'direction_hit_rate': 0.875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075098, 'direction_hit_rate': 0.125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.032818, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.925, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041975, 'direction_hit_rate': 0.925}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067326, 'direction_hit_rate': 0.075}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.028209, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.017288`, avg `0.011259`, median `0.02164`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.021608`, avg `0.015354`, median `0.020154`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.032506`, avg `0.022958`, median `0.028693`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.375`, primary_mae `0.030581`, avg `0.056495`, median `0.060676`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.020452`, avg `0.110147`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.012728`, avg `0.013469`, median `0.020444`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.5625`, primary_mae `0.01969`, avg `0.018669`, median `0.028596`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.032697`, avg `0.020639`, median `0.034294`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.4375`, primary_mae `0.034826`, avg `0.051819`, median `0.060676`
- 60d: sample `16`, primary_hit `1.0`, primary_closer `0.375`, primary_mae `0.023923`, avg `0.102179`, median `0.098383`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.028482`, avg `0.015203`, median `0.016121`
- 5d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.037036`, avg `0.019089`, median `0.021135`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.125`, primary_mae `0.100743`, avg `0.020177`, median `0.030699`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.09747`, avg `0.049727`, median `0.038523`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.100162`, avg `0.118371`, median `0.111654`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4125`, primary_mae `0.019578`, avg `0.011477`, median `0.012652`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3875`, primary_mae `0.02653`, avg `0.015433`, median `0.017855`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3375`, primary_mae `0.054001`, avg `0.020585`, median `0.026366`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4125`, primary_mae `0.052638`, avg `0.042289`, median `0.03796`
- 60d: sample `80`, primary_hit `0.75`, primary_closer `0.3625`, primary_mae `0.053828`, avg `0.098521`, median `0.098004`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4125`, primary_mae `0.019578`, avg `0.011477`, median `0.012652`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3875`, primary_mae `0.02653`, avg `0.015433`, median `0.017855`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3375`, primary_mae `0.054001`, avg `0.020585`, median `0.026366`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4125`, primary_mae `0.052638`, avg `0.042289`, median `0.03796`
- 60d: sample `80`, primary_hit `0.75`, primary_closer `0.3625`, primary_mae `0.053828`, avg `0.098521`, median `0.098004`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.7167`, primary_closer `0.5`, primary_mae `0.016845`, avg `0.010088`, median `0.012387`
- 5d: sample `60`, primary_hit `0.7`, primary_closer `0.4333`, primary_mae `0.022598`, avg `0.013178`, median `0.016224`
- 10d: sample `60`, primary_hit `0.7167`, primary_closer `0.4167`, primary_mae `0.038121`, avg `0.019125`, median `0.02525`
- 20d: sample `60`, primary_hit `0.8667`, primary_closer `0.4667`, primary_mae `0.03848`, avg `0.039677`, median `0.038653`
- 60d: sample `60`, primary_hit `0.95`, primary_closer `0.3833`, primary_mae `0.040114`, avg `0.091923`, median `0.096112`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.15`, primary_closer `0.15`, primary_mae `0.027777`, avg `0.015645`, median `0.016121`
- 5d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.038326`, avg `0.022195`, median `0.021135`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.1`, primary_mae `0.101642`, avg `0.024965`, median `0.030699`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.25`, primary_mae `0.095115`, avg `0.050125`, median `0.031305`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.09497`, avg `0.118317`, median `0.105065`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4125`, primary_mae `0.019578`, avg `0.011477`, median `0.012652`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3875`, primary_mae `0.02653`, avg `0.015433`, median `0.017855`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3375`, primary_mae `0.054001`, avg `0.020585`, median `0.026366`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4125`, primary_mae `0.052638`, avg `0.042289`, median `0.03796`
- 60d: sample `80`, primary_hit `0.75`, primary_closer `0.3625`, primary_mae `0.053828`, avg `0.098521`, median `0.098004`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4125`, primary_mae `0.019578`, avg `0.011477`, median `0.012652`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3875`, primary_mae `0.02653`, avg `0.015433`, median `0.017855`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3375`, primary_mae `0.054001`, avg `0.020585`, median `0.026366`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4125`, primary_mae `0.052638`, avg `0.042289`, median `0.03796`
- 60d: sample `80`, primary_hit `0.75`, primary_closer `0.3625`, primary_mae `0.053828`, avg `0.098521`, median `0.098004`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4125`, primary_mae `0.019578`, avg `0.011477`, median `0.012652`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3875`, primary_mae `0.02653`, avg `0.015433`, median `0.017855`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.3375`, primary_mae `0.054001`, avg `0.020585`, median `0.026366`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.4125`, primary_mae `0.052638`, avg `0.042289`, median `0.03796`
- 60d: sample `80`, primary_hit `0.75`, primary_closer `0.3625`, primary_mae `0.053828`, avg `0.098521`, median `0.098004`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
