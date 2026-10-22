# Historical Replay Benchmark

Generated at: `2026-10-22T17:14:17.032266+00:00`
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
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.017291`
- secondary_mean_absolute_error: `0.014397`
- primary_error_advantage: `-0.002894`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.019472`
- secondary_mean_absolute_error: `0.016991`
- primary_error_advantage: `-0.002481`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.027815`
- secondary_mean_absolute_error: `0.024673`
- primary_error_advantage: `-0.003142`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.041958`
- secondary_mean_absolute_error: `0.027711`
- primary_error_advantage: `-0.014247`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.056296`
- secondary_mean_absolute_error: `0.04459`
- primary_error_advantage: `-0.011706`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014516`, as_primary `0`, as_primary_hit `None`, avg `0.004178`, median `0.004406`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.017832`, as_primary `0`, as_primary_hit `None`, avg `0.003646`, median `0.003762`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.023878`, as_primary `0`, as_primary_hit `None`, avg `0.008265`, median `0.009345`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.02807`, as_primary `0`, as_primary_hit `None`, avg `0.017068`, median `0.017488`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.041974`, as_primary `0`, as_primary_hit `None`, avg `0.037033`, median `0.039074`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014639`, as_primary `20`, as_primary_hit `0.7`, avg `0.004178`, median `0.004406`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.020515`, as_primary `20`, as_primary_hit `0.7`, avg `0.003646`, median `0.003762`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.031474`, as_primary `20`, as_primary_hit `0.7`, avg `0.008265`, median `0.009345`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.043654`, as_primary `20`, as_primary_hit `0.75`, avg `0.017068`, median `0.017488`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.047387`, as_primary `20`, as_primary_hit `0.6`, avg `0.037033`, median `0.039074`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.017302`, as_primary `60`, as_primary_hit `0.55`, avg `0.004178`, median `0.004406`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.018779`, as_primary `60`, as_primary_hit `0.5333`, avg `0.003646`, median `0.003762`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.030005`, as_primary `60`, as_primary_hit `0.6333`, avg `0.008265`, median `0.009345`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.041599`, as_primary `60`, as_primary_hit `0.7167`, avg `0.017068`, median `0.017488`
- 60d: sample `80`, direction_hit `0.25`, path_mae `0.056161`, as_primary `60`, as_primary_hit `0.8`, avg `0.037033`, median `0.039074`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014463`, as_primary `0`, as_primary_hit `None`, avg `0.004178`, median `0.004406`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.017005`, as_primary `0`, as_primary_hit `None`, avg `0.003646`, median `0.003762`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.021588`, as_primary `0`, as_primary_hit `None`, avg `0.008265`, median `0.009345`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.024464`, as_primary `0`, as_primary_hit `None`, avg `0.017068`, median `0.017488`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.041991`, as_primary `0`, as_primary_hit `None`, avg `0.037033`, median `0.039074`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.4125`, primary_mae `0.017291`, avg `0.004178`, median `0.004406`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.019472`, avg `0.003646`, median `0.003762`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.027815`, avg `0.008265`, median `0.009345`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.041958`, avg `0.017068`, median `0.017488`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.056296`, avg `0.037033`, median `0.039074`

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
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.022753`, avg `-0.002687`, median `-0.00922`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.020113`, avg `-0.003785`, median `-0.005339`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.022716`, avg `0.005152`, median `0.008279`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.048005`, avg `0.008499`, median `0.002813`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.35`, primary_mae `0.063115`, avg `0.056195`, median `0.041256`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.008075`, avg `0.004833`, median `0.00547`
- 5d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.017099`, avg `0.006585`, median `0.007532`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.65`, primary_mae `0.023197`, avg `0.006683`, median `0.010945`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.031693`, avg `0.015245`, median `0.014917`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.064966`, avg `0.013374`, median `0.018611`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.019168`, avg `0.007283`, median `0.011073`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.020339`, avg `0.005892`, median `0.010356`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.032674`, avg `0.010613`, median `0.009516`
- 20d: sample `40`, primary_hit `0.225`, primary_closer `0.175`, primary_mae `0.044066`, avg `0.022264`, median `0.026844`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.275`, primary_mae `0.048551`, avg `0.039282`, median `0.051409`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.008075, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.017099, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.022716, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.031693, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.048551, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014463, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017302, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.008075, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017005, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020515, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.017099, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021588, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031474, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.022716, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024464, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043654, 'direction_hit_rate': 0.725}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.031693, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041974, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056161, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.048551, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.005885`, avg `0.007954`, median `0.006991`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.021891`, avg `0.00142`, median `-0.002082`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.030319`, avg `-0.005397`, median `0.009841`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.034329`, avg `0.009106`, median `0.008479`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.076697`, avg `0.00634`, median `0.002733`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.8125`, primary_closer `0.625`, primary_mae `0.007483`, avg `0.00725`, median `0.006991`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.017898`, avg `0.007049`, median `0.007532`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.75`, primary_mae `0.021471`, avg `0.009647`, median `0.019584`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.034756`, avg `0.013058`, median `0.012453`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.071449`, avg `0.010145`, median `0.002733`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.021352`, avg `0.000501`, median `-0.00786`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.022183`, avg `-0.003991`, median `-0.005339`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.023359`, avg `0.009213`, median `0.009495`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.051713`, avg `0.011708`, median `0.011531`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.375`, primary_mae `0.051788`, avg `0.043746`, median `0.031522`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.4125`, primary_mae `0.017291`, avg `0.004178`, median `0.004406`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.019472`, avg `0.003646`, median `0.003762`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.027815`, avg `0.008265`, median `0.009345`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.041958`, avg `0.017068`, median `0.017488`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.056296`, avg `0.037033`, median `0.039074`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.4125`, primary_mae `0.017291`, avg `0.004178`, median `0.004406`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.019472`, avg `0.003646`, median `0.003762`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.027815`, avg `0.008265`, median `0.009345`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.041958`, avg `0.017068`, median `0.017488`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.056296`, avg `0.037033`, median `0.039074`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.4333`, primary_mae `0.01547`, avg `0.006466`, median `0.006547`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.4167`, primary_mae `0.019259`, avg `0.006123`, median `0.008725`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.4667`, primary_mae `0.029515`, avg `0.009303`, median `0.010553`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.2833`, primary_mae `0.039942`, avg `0.019924`, median `0.020026`
- 60d: sample `60`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.054023`, avg `0.030646`, median `0.039074`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.020317`, avg `0.0024`, median `0.001514`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.021556`, avg `0.003309`, median `0.00398`
- 10d: sample `40`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.032466`, avg `0.009083`, median `0.010995`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.275`, primary_mae `0.051578`, avg `0.011575`, median `0.006138`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.051209`, avg `0.032845`, median `0.025896`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.4125`, primary_mae `0.017291`, avg `0.004178`, median `0.004406`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.019472`, avg `0.003646`, median `0.003762`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.027815`, avg `0.008265`, median `0.009345`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.041958`, avg `0.017068`, median `0.017488`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.056296`, avg `0.037033`, median `0.039074`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.4125`, primary_mae `0.017291`, avg `0.004178`, median `0.004406`
- 5d: sample `80`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.019472`, avg `0.003646`, median `0.003762`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.027815`, avg `0.008265`, median `0.009345`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.041958`, avg `0.017068`, median `0.017488`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.056296`, avg `0.037033`, median `0.039074`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
