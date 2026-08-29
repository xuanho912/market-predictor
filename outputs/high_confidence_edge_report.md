# High Confidence Edge Report

Generated at: `2026-08-29T04:11:04.729759+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `0`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `0`, gate `insufficient`
- 5d: completed `0`, gate `insufficient`
- 10d: completed `0`, gate `insufficient`
- 20d: completed `0`, gate `insufficient`
- 60d: completed `0`, gate `insufficient`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.7125`, avg `0.007384`, median `0.012272`, mae `0.019853`
- 5d: sample `80`, hit `0.7`, avg `0.011149`, median `0.014937`, mae `0.024883`
- 10d: sample `80`, hit `0.65`, avg `0.013442`, median `0.021584`, mae `0.03751`
- 20d: sample `80`, hit `0.75`, avg `0.028051`, median `0.03107`, mae `0.047943`
- 60d: sample `80`, hit `0.775`, avg `0.061483`, median `0.0765`, mae `0.08075`

### WEAK_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.012736`, median `0.022579`, mae `0.021432`
- 5d: sample `8`, hit `0.75`, avg `0.01665`, median `0.030736`, mae `0.024452`
- 10d: sample `8`, hit `0.625`, avg `0.020096`, median `0.036012`, mae `0.028883`
- 20d: sample `8`, hit `1.0`, avg `0.05728`, median `0.062955`, mae `0.05728`
- 60d: sample `8`, hit `0.875`, avg `0.0807`, median `0.097048`, mae `0.09219`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.012736`, median `0.022579`, mae `0.021432`
- 5d: sample `8`, hit `0.75`, avg `0.01665`, median `0.030736`, mae `0.024452`
- 10d: sample `8`, hit `0.625`, avg `0.020096`, median `0.036012`, mae `0.028883`
- 20d: sample `8`, hit `1.0`, avg `0.05728`, median `0.062955`, mae `0.05728`
- 60d: sample `8`, hit `0.875`, avg `0.0807`, median `0.097048`, mae `0.09219`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.7125, 'avg_return': 0.007384, 'median_return': 0.012272, 'mean_absolute_return': 0.019853, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.011149, 'median_return': 0.014937, 'mean_absolute_return': 0.024883, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.013442, 'median_return': 0.021584, 'mean_absolute_return': 0.03751, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.028051, 'median_return': 0.03107, 'mean_absolute_return': 0.047943, 'max_adverse_excursion': -0.078831, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.775, 'avg_return': 0.061483, 'median_return': 0.0765, 'mean_absolute_return': 0.08075, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.012736, 'median_return': 0.022579, 'mean_absolute_return': 0.021432, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.01665, 'median_return': 0.030736, 'mean_absolute_return': 0.024452, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.020096, 'median_return': 0.036012, 'mean_absolute_return': 0.028883, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.05728, 'median_return': 0.062955, 'mean_absolute_return': 0.05728, 'max_adverse_excursion': 0.02284, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.0807, 'median_return': 0.097048, 'mean_absolute_return': 0.09219, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.006789, 'median_return': 0.011414, 'mean_absolute_return': 0.019678, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.010538, 'median_return': 0.014937, 'mean_absolute_return': 0.024931, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.012703, 'median_return': 0.021169, 'mean_absolute_return': 0.038469, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.024804, 'median_return': 0.029072, 'mean_absolute_return': 0.046906, 'max_adverse_excursion': -0.078831, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.059348, 'median_return': 0.069306, 'mean_absolute_return': 0.079479, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.7125}, '5d': {'sample_size': 80, 'hit_rate': 0.7}, '10d': {'sample_size': 80, 'hit_rate': 0.65}, '20d': {'sample_size': 80, 'hit_rate': 0.75}, '60d': {'sample_size': 80, 'hit_rate': 0.775}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.7125, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': 0.05, 'both_hit': 45, 'both_miss': 15}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': 0.0, 'both_hit': 46, 'both_miss': 14}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.025, 'both_hit': 43, 'both_miss': 17}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 10}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.775, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': 0.075, 'both_hit': 49, 'both_miss': 11}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.7125, 'avg_return': 0.007384, 'median_return': 0.012272, 'mean_absolute_return': 0.019853, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.011149, 'median_return': 0.014937, 'mean_absolute_return': 0.024883, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.013442, 'median_return': 0.021584, 'mean_absolute_return': 0.03751, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.028051, 'median_return': 0.03107, 'mean_absolute_return': 0.047943, 'max_adverse_excursion': -0.078831, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.775, 'avg_return': 0.061483, 'median_return': 0.0765, 'mean_absolute_return': 0.08075, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.7333`, avg `0.009196`, median `0.012542`, mae `0.018273`
- 5d: sample `60`, hit `0.7333`, avg `0.013689`, median `0.015191`, mae `0.024082`
- 10d: sample `60`, hit `0.6667`, avg `0.015034`, median `0.023034`, mae `0.037148`
- 20d: sample `60`, hit `0.7667`, avg `0.032853`, median `0.032954`, mae `0.050116`
- 60d: sample `60`, hit `0.8`, avg `0.069413`, median `0.082988`, mae `0.079864`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.7333`, avg `0.009196`, median `0.012542`, mae `0.018273`
- 5d: sample `60`, hit `0.7333`, avg `0.013689`, median `0.015191`, mae `0.024082`
- 10d: sample `60`, hit `0.6667`, avg `0.015034`, median `0.023034`, mae `0.037148`
- 20d: sample `60`, hit `0.7667`, avg `0.032853`, median `0.032954`, mae `0.050116`
- 60d: sample `60`, hit `0.8`, avg `0.069413`, median `0.082988`, mae `0.079864`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.85`, avg `0.015719`, median `0.018644`, mae `0.022861`
- 5d: sample `20`, hit `0.9`, avg `0.023075`, median `0.025337`, mae `0.029888`
- 10d: sample `20`, hit `0.8`, avg `0.030329`, median `0.045189`, mae `0.049311`
- 20d: sample `20`, hit `0.85`, avg `0.055633`, median `0.050611`, mae `0.067916`
- 60d: sample `20`, hit `0.85`, avg `0.096616`, median `0.113503`, mae `0.100828`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.7125`, avg `0.007384`, median `0.012272`, mae `0.019853`
- 5d: sample `80`, hit `0.7`, avg `0.011149`, median `0.014937`, mae `0.024883`
- 10d: sample `80`, hit `0.65`, avg `0.013442`, median `0.021584`, mae `0.03751`
- 20d: sample `80`, hit `0.75`, avg `0.028051`, median `0.03107`, mae `0.047943`
- 60d: sample `80`, hit `0.775`, avg `0.061483`, median `0.0765`, mae `0.08075`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Internal Resonance Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

### aligned_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### mixed_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.7125`, avg `0.007384`, median `0.012272`, mae `0.019853`
- 5d: sample `80`, hit `0.7`, avg `0.011149`, median `0.014937`, mae `0.024883`
- 10d: sample `80`, hit `0.65`, avg `0.013442`, median `0.021584`, mae `0.03751`
- 20d: sample `80`, hit `0.75`, avg `0.028051`, median `0.03107`, mae `0.047943`
- 60d: sample `80`, hit `0.775`, avg `0.061483`, median `0.0765`, mae `0.08075`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.7125`, avg `0.007384`, median `0.012272`, mae `0.019853`
- 5d: sample `80`, hit `0.7`, avg `0.011149`, median `0.014937`, mae `0.024883`
- 10d: sample `80`, hit `0.65`, avg `0.013442`, median `0.021584`, mae `0.03751`
- 20d: sample `80`, hit `0.75`, avg `0.028051`, median `0.03107`, mae `0.047943`
- 60d: sample `80`, hit `0.775`, avg `0.061483`, median `0.0765`, mae `0.08075`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.7125`, avg `0.007384`, median `0.012272`, mae `0.019853`
- 5d: sample `80`, hit `0.7`, avg `0.011149`, median `0.014937`, mae `0.024883`
- 10d: sample `80`, hit `0.65`, avg `0.013442`, median `0.021584`, mae `0.03751`
- 20d: sample `80`, hit `0.75`, avg `0.028051`, median `0.03107`, mae `0.047943`
- 60d: sample `80`, hit `0.775`, avg `0.061483`, median `0.0765`, mae `0.08075`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.7125`, avg `0.007384`, median `0.012272`, mae `0.019853`
- 5d: sample `80`, hit `0.7`, avg `0.011149`, median `0.014937`, mae `0.024883`
- 10d: sample `80`, hit `0.65`, avg `0.013442`, median `0.021584`, mae `0.03751`
- 20d: sample `80`, hit `0.75`, avg `0.028051`, median `0.03107`, mae `0.047943`
- 60d: sample `80`, hit `0.775`, avg `0.061483`, median `0.0765`, mae `0.08075`

### bounce_with_flow_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### risk_path_with_flow_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
