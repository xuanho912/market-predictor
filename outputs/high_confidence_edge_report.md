# High Confidence Edge Report

Generated at: `2026-08-20T02:34:10.012522+00:00`

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
- 3d: sample `80`, hit `0.5875`, avg `0.003615`, median `0.005458`, mae `0.014385`
- 5d: sample `80`, hit `0.5875`, avg `0.004049`, median `0.004014`, mae `0.018041`
- 10d: sample `80`, hit `0.65`, avg `0.006161`, median `0.010495`, mae `0.02599`
- 20d: sample `80`, hit `0.7125`, avg `0.015394`, median `0.019193`, mae `0.04107`
- 60d: sample `80`, hit `0.6125`, avg `0.026943`, median `0.046132`, mae `0.071512`

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
- 3d: sample `8`, hit `0.625`, avg `0.005624`, median `0.009229`, mae `0.010905`
- 5d: sample `8`, hit `0.75`, avg `0.010667`, median `0.013852`, mae `0.013669`
- 10d: sample `8`, hit `0.875`, avg `0.018814`, median `0.024811`, mae `0.023095`
- 20d: sample `8`, hit `0.75`, avg `0.02311`, median `0.022652`, mae `0.028789`
- 60d: sample `8`, hit `0.25`, avg `-0.000717`, median `-0.020268`, mae `0.0464`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.005624`, median `0.009229`, mae `0.010905`
- 5d: sample `8`, hit `0.75`, avg `0.010667`, median `0.013852`, mae `0.013669`
- 10d: sample `8`, hit `0.875`, avg `0.018814`, median `0.024811`, mae `0.023095`
- 20d: sample `8`, hit `0.75`, avg `0.02311`, median `0.022652`, mae `0.028789`
- 60d: sample `8`, hit `0.25`, avg `-0.000717`, median `-0.020268`, mae `0.0464`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.003615, 'median_return': 0.005458, 'mean_absolute_return': 0.014385, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.004049, 'median_return': 0.004014, 'mean_absolute_return': 0.018041, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.006161, 'median_return': 0.010495, 'mean_absolute_return': 0.02599, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.7125, 'avg_return': 0.015394, 'median_return': 0.019193, 'mean_absolute_return': 0.04107, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.026943, 'median_return': 0.046132, 'mean_absolute_return': 0.071512, 'max_adverse_excursion': -0.253302, 'max_favorable_excursion': 0.171512}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005624, 'median_return': 0.009229, 'mean_absolute_return': 0.010905, 'max_adverse_excursion': -0.012068, 'max_favorable_excursion': 0.022679}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.010667, 'median_return': 0.013852, 'mean_absolute_return': 0.013669, 'max_adverse_excursion': -0.007018, 'max_favorable_excursion': 0.032969}, '10d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.018814, 'median_return': 0.024811, 'mean_absolute_return': 0.023095, 'max_adverse_excursion': -0.017124, 'max_favorable_excursion': 0.04237}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.02311, 'median_return': 0.022652, 'mean_absolute_return': 0.028789, 'max_adverse_excursion': -0.015135, 'max_favorable_excursion': 0.07754}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.000717, 'median_return': -0.020268, 'mean_absolute_return': 0.0464, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.095628}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.003392, 'median_return': 0.005458, 'mean_absolute_return': 0.014771, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.003314, 'median_return': 0.003684, 'mean_absolute_return': 0.018527, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.004755, 'median_return': 0.00794, 'mean_absolute_return': 0.026312, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.014536, 'median_return': 0.019193, 'mean_absolute_return': 0.042434, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.030017, 'median_return': 0.048421, 'mean_absolute_return': 0.074302, 'max_adverse_excursion': -0.253302, 'max_favorable_excursion': 0.171512}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.5875}, '10d': {'sample_size': 80, 'hit_rate': 0.65}, '20d': {'sample_size': 80, 'hit_rate': 0.7125}, '60d': {'sample_size': 80, 'hit_rate': 0.6125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 47, 'both_miss': 33}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 47, 'both_miss': 33}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 52, 'both_miss': 28}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7125, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': 0.0, 'both_hit': 57, 'both_miss': 23}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.004298, 'median_return': 0.006565, 'mean_absolute_return': 0.016466, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.003691, 'median_return': 0.003684, 'mean_absolute_return': 0.020099, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.008065, 'median_return': 0.011168, 'mean_absolute_return': 0.028579, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.021078, 'median_return': 0.024844, 'mean_absolute_return': 0.046296, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.036054, 'median_return': 0.063119, 'mean_absolute_return': 0.078, 'max_adverse_excursion': -0.253302, 'max_favorable_excursion': 0.171512}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.001566, 'median_return': 0.001534, 'mean_absolute_return': 0.008141, 'max_adverse_excursion': -0.014409, 'max_favorable_excursion': 0.019264}, '5d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.005123, 'median_return': 0.006452, 'mean_absolute_return': 0.011868, 'max_adverse_excursion': -0.018642, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.000446, 'median_return': 0.009675, 'mean_absolute_return': 0.018225, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.027042}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': -0.001659, 'median_return': 0.007988, 'mean_absolute_return': 0.025392, 'max_adverse_excursion': -0.092026, 'max_favorable_excursion': 0.035222}, '60d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.00039, 'median_return': -0.01711, 'mean_absolute_return': 0.052048, 'max_adverse_excursion': -0.088557, 'max_favorable_excursion': 0.096597}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.00157`, median `0.001534`, mae `0.011883`
- 5d: sample `40`, hit `0.65`, avg `0.004798`, median `0.005319`, mae `0.014492`
- 10d: sample `40`, hit `0.65`, avg `0.002368`, median `0.010495`, mae `0.022222`
- 20d: sample `40`, hit `0.7`, avg `0.010271`, median `0.013178`, mae `0.031778`
- 60d: sample `40`, hit `0.475`, avg `0.014353`, median `-0.004287`, mae `0.052343`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.003314`, median `0.00558`, mae `0.016323`
- 5d: sample `40`, hit `0.5`, avg `0.002528`, median `0.000863`, mae `0.019697`
- 10d: sample `40`, hit `0.725`, avg `0.010248`, median `0.011426`, mae `0.02839`
- 20d: sample `40`, hit `0.775`, avg `0.029602`, median `0.028499`, mae `0.046427`
- 60d: sample `40`, hit `0.65`, avg `0.04842`, median `0.065495`, mae `0.067657`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.00157`, median `0.001534`, mae `0.011883`
- 5d: sample `40`, hit `0.65`, avg `0.004798`, median `0.005319`, mae `0.014492`
- 10d: sample `40`, hit `0.65`, avg `0.002368`, median `0.010495`, mae `0.022222`
- 20d: sample `40`, hit `0.7`, avg `0.010271`, median `0.013178`, mae `0.031778`
- 60d: sample `40`, hit `0.475`, avg `0.014353`, median `-0.004287`, mae `0.052343`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.003314`, median `0.00558`, mae `0.016323`
- 5d: sample `40`, hit `0.5`, avg `0.002528`, median `0.000863`, mae `0.019697`
- 10d: sample `40`, hit `0.725`, avg `0.010248`, median `0.011426`, mae `0.02839`
- 20d: sample `40`, hit `0.775`, avg `0.029602`, median `0.028499`, mae `0.046427`
- 60d: sample `40`, hit `0.65`, avg `0.04842`, median `0.065495`, mae `0.067657`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.005053`, median `0.00558`, mae `0.017022`
- 5d: sample `20`, hit `0.45`, avg `0.000584`, median `-0.002418`, mae `0.022278`
- 10d: sample `20`, hit `0.75`, avg `0.016206`, median `0.013022`, mae `0.030561`
- 20d: sample `20`, hit `0.8`, avg `0.037002`, median `0.029029`, mae `0.05469`
- 60d: sample `20`, hit `0.8`, avg `0.067743`, median `0.079128`, mae `0.082675`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.00157`, median `0.001534`, mae `0.011883`
- 5d: sample `40`, hit `0.65`, avg `0.004798`, median `0.005319`, mae `0.014492`
- 10d: sample `40`, hit `0.65`, avg `0.002368`, median `0.010495`, mae `0.022222`
- 20d: sample `40`, hit `0.7`, avg `0.010271`, median `0.013178`, mae `0.031778`
- 60d: sample `40`, hit `0.475`, avg `0.014353`, median `-0.004287`, mae `0.052343`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.00566`, median `0.006565`, mae `0.016887`
- 5d: sample `40`, hit `0.525`, avg `0.0033`, median `0.003197`, mae `0.02159`
- 10d: sample `40`, hit `0.65`, avg `0.009953`, median `0.011168`, mae `0.029759`
- 20d: sample `40`, hit `0.725`, avg `0.020516`, median `0.024844`, mae `0.050362`
- 60d: sample `40`, hit `0.75`, avg `0.039533`, median `0.065495`, mae `0.09068`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.00157`, median `0.001534`, mae `0.011883`
- 5d: sample `40`, hit `0.65`, avg `0.004798`, median `0.005319`, mae `0.014492`
- 10d: sample `40`, hit `0.65`, avg `0.002368`, median `0.010495`, mae `0.022222`
- 20d: sample `40`, hit `0.7`, avg `0.010271`, median `0.013178`, mae `0.031778`
- 60d: sample `40`, hit `0.475`, avg `0.014353`, median `-0.004287`, mae `0.052343`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.003615`, median `0.005458`, mae `0.014385`
- 5d: sample `80`, hit `0.5875`, avg `0.004049`, median `0.004014`, mae `0.018041`
- 10d: sample `80`, hit `0.65`, avg `0.006161`, median `0.010495`, mae `0.02599`
- 20d: sample `80`, hit `0.7125`, avg `0.015394`, median `0.019193`, mae `0.04107`
- 60d: sample `80`, hit `0.6125`, avg `0.026943`, median `0.046132`, mae `0.071512`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.003615`, median `0.005458`, mae `0.014385`
- 5d: sample `80`, hit `0.5875`, avg `0.004049`, median `0.004014`, mae `0.018041`
- 10d: sample `80`, hit `0.65`, avg `0.006161`, median `0.010495`, mae `0.02599`
- 20d: sample `80`, hit `0.7125`, avg `0.015394`, median `0.019193`, mae `0.04107`
- 60d: sample `80`, hit `0.6125`, avg `0.026943`, median `0.046132`, mae `0.071512`

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
