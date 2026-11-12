# Historical Replay Benchmark

Generated at: `2026-11-12T02:35:36.422772+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.021795`
- secondary_mean_absolute_error: `0.019771`
- primary_error_advantage: `-0.002024`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.029078`
- secondary_mean_absolute_error: `0.024394`
- primary_error_advantage: `-0.004684`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.046435`
- secondary_mean_absolute_error: `0.033606`
- primary_error_advantage: `-0.012829`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.060687`
- secondary_mean_absolute_error: `0.046924`
- primary_error_advantage: `-0.013763`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.775`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.049895`
- secondary_mean_absolute_error: `0.044181`
- primary_error_advantage: `-0.005714`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.018936`, as_primary `0`, as_primary_hit `None`, avg `0.003728`, median `0.010083`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.024256`, as_primary `0`, as_primary_hit `None`, avg `0.004033`, median `0.007499`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.033049`, as_primary `0`, as_primary_hit `None`, avg `0.003268`, median `0.010815`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.04145`, as_primary `0`, as_primary_hit `None`, avg `0.00309`, median `0.009388`
- 60d: sample `80`, direction_hit `0.875`, path_mae `0.043861`, as_primary `0`, as_primary_hit `None`, avg `0.069582`, median `0.078309`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.020657`, as_primary `60`, as_primary_hit `0.6333`, avg `0.003728`, median `0.010083`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.026644`, as_primary `60`, as_primary_hit `0.5667`, avg `0.004033`, median `0.007499`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.042023`, as_primary `60`, as_primary_hit `0.5333`, avg `0.003268`, median `0.010815`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.058883`, as_primary `60`, as_primary_hit `0.5833`, avg `0.00309`, median `0.009388`
- 60d: sample `80`, direction_hit `0.875`, path_mae `0.048565`, as_primary `60`, as_primary_hit `0.8333`, avg `0.069582`, median `0.078309`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.35`, path_mae `0.024858`, as_primary `20`, as_primary_hit `0.7`, avg `0.003728`, median `0.010083`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.031583`, as_primary `20`, as_primary_hit `0.7`, avg `0.004033`, median `0.007499`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.052253`, as_primary `20`, as_primary_hit `0.7`, avg `0.003268`, median `0.010815`
- 20d: sample `80`, direction_hit `0.425`, path_mae `0.069481`, as_primary `20`, as_primary_hit `0.55`, avg `0.00309`, median `0.009388`
- 60d: sample `80`, direction_hit `0.125`, path_mae `0.064941`, as_primary `20`, as_primary_hit `1.0`, avg `0.069582`, median `0.078309`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.019421`, as_primary `0`, as_primary_hit `None`, avg `0.003728`, median `0.010083`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.02388`, as_primary `0`, as_primary_hit `None`, avg `0.004033`, median `0.007499`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.033067`, as_primary `0`, as_primary_hit `None`, avg `0.003268`, median `0.010815`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.041323`, as_primary `0`, as_primary_hit `None`, avg `0.00309`, median `0.009388`
- 60d: sample `80`, direction_hit `0.875`, path_mae `0.044104`, as_primary `0`, as_primary_hit `None`, avg `0.069582`, median `0.078309`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.020529`, avg `0.00392`, median `0.01054`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.4667`, primary_mae `0.027724`, avg `0.003718`, median `0.004762`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.45`, primary_mae `0.041755`, avg `0.002422`, median `0.014178`
- 20d: sample `60`, primary_hit `0.5833`, primary_closer `0.35`, primary_mae `0.0605`, avg `0.004848`, median `0.018545`
- 60d: sample `60`, primary_hit `0.8333`, primary_closer `0.4667`, primary_mae `0.050346`, avg `0.054317`, median `0.065936`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.025593`, avg `0.00315`, median `0.009216`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.033141`, avg `0.004979`, median `0.010244`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.15`, primary_mae `0.060473`, avg `0.005805`, median `0.010405`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.2`, primary_mae `0.061248`, avg `-0.002183`, median `0.001267`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.35`, primary_mae `0.048544`, avg `0.115376`, median `0.105065`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.525`, primary_mae `0.017279`, avg `0.003814`, median `0.007812`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.027411`, avg `0.001327`, median `0.001372`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.04417`, avg `-0.005531`, median `-0.010049`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.062483`, avg `-0.006174`, median `-0.021284`
- 60d: sample `40`, primary_hit `0.825`, primary_closer `0.45`, primary_mae `0.043318`, avg `0.049068`, median `0.056969`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.025593`, avg `0.00315`, median `0.009216`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.033141`, avg `0.004979`, median `0.010244`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.15`, primary_mae `0.060473`, avg `0.005805`, median `0.010405`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.2`, primary_mae `0.061248`, avg `-0.002183`, median `0.001267`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.35`, primary_mae `0.048544`, avg `0.115376`, median `0.105065`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.027031`, avg `0.004132`, median `0.011428`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.028349`, avg `0.0085`, median `0.019826`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.45`, primary_mae `0.036926`, avg `0.018327`, median `0.023734`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.056533`, avg `0.026892`, median `0.021998`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.5`, primary_mae `0.064401`, avg `0.064816`, median `0.091555`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.017279, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.027411, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.036926, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.056533, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.825, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.043318, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018936, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024858, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.017279, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02388, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031583, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.027411, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033049, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052253, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.036926, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041323, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069481, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.056533, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.775, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043861, 'direction_hit_rate': 0.875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064941, 'direction_hit_rate': 0.125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.825, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.043318, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.02022`, avg `0.004176`, median `0.008001`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.034733`, avg `0.000383`, median `-0.00914`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.048613`, avg `-0.005346`, median `-0.024095`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.0`, primary_mae `0.10251`, avg `-0.026833`, median `-0.02913`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.125`, primary_mae `0.059555`, avg `0.045151`, median `0.050394`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.021115`, avg `0.001653`, median `0.010214`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.031209`, avg `-0.001018`, median `0.001372`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.043947`, avg `-0.002354`, median `-0.008604`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.1875`, primary_mae `0.092097`, avg `-0.01642`, median `-0.02913`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.25`, primary_mae `0.051924`, avg `0.054329`, median `0.057737`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.021558`, avg `0.010269`, median `0.009216`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.03235`, avg `0.013027`, median `0.012355`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.125`, primary_mae `0.068605`, avg `0.01158`, median `0.01485`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.125`, primary_mae `0.067595`, avg `0.005016`, median `0.005465`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.3125`, primary_mae `0.047853`, avg `0.121496`, median `0.111654`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.021795`, avg `0.003728`, median `0.010083`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4125`, primary_mae `0.029078`, avg `0.004033`, median `0.007499`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.046435`, avg `0.003268`, median `0.010815`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.3125`, primary_mae `0.060687`, avg `0.00309`, median `0.009388`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.049895`, avg `0.069582`, median `0.078309`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.021795`, avg `0.003728`, median `0.010083`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4125`, primary_mae `0.029078`, avg `0.004033`, median `0.007499`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.046435`, avg `0.003268`, median `0.010815`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.3125`, primary_mae `0.060687`, avg `0.00309`, median `0.009388`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.049895`, avg `0.069582`, median `0.078309`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.020529`, avg `0.00392`, median `0.01054`
- 5d: sample `60`, primary_hit `0.5667`, primary_closer `0.4667`, primary_mae `0.027724`, avg `0.003718`, median `0.004762`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.45`, primary_mae `0.041755`, avg `0.002422`, median `0.014178`
- 20d: sample `60`, primary_hit `0.5833`, primary_closer `0.35`, primary_mae `0.0605`, avg `0.004848`, median `0.018545`
- 60d: sample `60`, primary_hit `0.8333`, primary_closer `0.4667`, primary_mae `0.050346`, avg `0.054317`, median `0.065936`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.025593`, avg `0.00315`, median `0.009216`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.033141`, avg `0.004979`, median `0.010244`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.15`, primary_mae `0.060473`, avg `0.005805`, median `0.010405`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.2`, primary_mae `0.061248`, avg `-0.002183`, median `0.001267`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.35`, primary_mae `0.048544`, avg `0.115376`, median `0.105065`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.021795`, avg `0.003728`, median `0.010083`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4125`, primary_mae `0.029078`, avg `0.004033`, median `0.007499`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.046435`, avg `0.003268`, median `0.010815`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.3125`, primary_mae `0.060687`, avg `0.00309`, median `0.009388`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.049895`, avg `0.069582`, median `0.078309`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.021795`, avg `0.003728`, median `0.010083`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4125`, primary_mae `0.029078`, avg `0.004033`, median `0.007499`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.046435`, avg `0.003268`, median `0.010815`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.3125`, primary_mae `0.060687`, avg `0.00309`, median `0.009388`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.049895`, avg `0.069582`, median `0.078309`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
