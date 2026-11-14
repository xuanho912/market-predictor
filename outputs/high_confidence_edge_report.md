# High Confidence Edge Report

Generated at: `2026-11-14T00:58:22.472709+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `192`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `historical_proxy_supports_higher_confidence_but_forward_validation_required`

## Forward Sample Gates

- 3d: completed `192`, gate `stronger_evidence`
- 5d: completed `192`, gate `stronger_evidence`
- 10d: completed `192`, gate `stronger_evidence`
- 20d: completed `192`, gate `stronger_evidence`
- 60d: completed `192`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.00151`, median `-0.004565`, mae `0.019559`
- 5d: sample `40`, hit `0.475`, avg `0.000847`, median `-0.002525`, mae `0.020109`
- 10d: sample `40`, hit `0.375`, avg `0.003915`, median `-0.007011`, mae `0.02647`
- 20d: sample `40`, hit `0.6`, avg `0.010933`, median `0.016745`, mae `0.042643`
- 60d: sample `40`, hit `0.5`, avg `0.011857`, median `0.012092`, mae `0.080139`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.005179`, median `0.003486`, mae `0.019738`
- 5d: sample `40`, hit `0.625`, avg `0.007122`, median `0.004606`, mae `0.022113`
- 10d: sample `40`, hit `0.45`, avg `0.005907`, median `-0.004918`, mae `0.030695`
- 20d: sample `40`, hit `0.625`, avg `0.020608`, median `0.01927`, mae `0.049056`
- 60d: sample `40`, hit `0.55`, avg `0.028545`, median `0.00464`, mae `0.077106`

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
- 3d: sample `8`, hit `0.125`, avg `-0.014139`, median `-0.010094`, mae `0.019142`
- 5d: sample `8`, hit `0.25`, avg `-0.017817`, median `-0.022295`, mae `0.019189`
- 10d: sample `8`, hit `0.0`, avg `-0.015109`, median `-0.011432`, mae `0.015109`
- 20d: sample `8`, hit `0.375`, avg `0.004121`, median `-0.001666`, mae `0.033108`
- 60d: sample `8`, hit `0.5`, avg `0.010735`, median `0.037425`, mae `0.07112`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.125`, avg `-0.014139`, median `-0.010094`, mae `0.019142`
- 5d: sample `8`, hit `0.25`, avg `-0.017817`, median `-0.022295`, mae `0.019189`
- 10d: sample `8`, hit `0.0`, avg `-0.015109`, median `-0.011432`, mae `0.015109`
- 20d: sample `8`, hit `0.375`, avg `0.004121`, median `-0.001666`, mae `0.033108`
- 60d: sample `8`, hit `0.5`, avg `0.010735`, median `0.037425`, mae `0.07112`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.00151, 'median_return': -0.004565, 'mean_absolute_return': 0.019559, 'max_adverse_excursion': -0.040531, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.000847, 'median_return': -0.002525, 'mean_absolute_return': 0.020109, 'max_adverse_excursion': -0.050569, 'max_favorable_excursion': 0.062512}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': 0.003915, 'median_return': -0.007011, 'mean_absolute_return': 0.02647, 'max_adverse_excursion': -0.05959, 'max_favorable_excursion': 0.099025}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.010933, 'median_return': 0.016745, 'mean_absolute_return': 0.042643, 'max_adverse_excursion': -0.120224, 'max_favorable_excursion': 0.117235}, '60d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.011857, 'median_return': 0.012092, 'mean_absolute_return': 0.080139, 'max_adverse_excursion': -0.182805, 'max_favorable_excursion': 0.195631}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.005179, 'median_return': 0.003486, 'mean_absolute_return': 0.019738, 'max_adverse_excursion': -0.035222, 'max_favorable_excursion': 0.047314}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.007122, 'median_return': 0.004606, 'mean_absolute_return': 0.022113, 'max_adverse_excursion': -0.033868, 'max_favorable_excursion': 0.067976}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.005907, 'median_return': -0.004918, 'mean_absolute_return': 0.030695, 'max_adverse_excursion': -0.065085, 'max_favorable_excursion': 0.109183}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.020608, 'median_return': 0.01927, 'mean_absolute_return': 0.049056, 'max_adverse_excursion': -0.093242, 'max_favorable_excursion': 0.158039}, '60d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.028545, 'median_return': 0.00464, 'mean_absolute_return': 0.077106, 'max_adverse_excursion': -0.168571, 'max_favorable_excursion': 0.258847}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.014139, 'median_return': -0.010094, 'mean_absolute_return': 0.019142, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.017817, 'median_return': -0.022295, 'mean_absolute_return': 0.019189, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.005072}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.015109, 'median_return': -0.011432, 'mean_absolute_return': 0.015109, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': -0.005891}, '20d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.004121, 'median_return': -0.001666, 'mean_absolute_return': 0.033108, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.010735, 'median_return': 0.037425, 'mean_absolute_return': 0.07112, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.003609, 'median_return': 0.001558, 'mean_absolute_return': 0.019705, 'max_adverse_excursion': -0.040531, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.006407, 'median_return': 0.003888, 'mean_absolute_return': 0.021324, 'max_adverse_excursion': -0.050569, 'max_favorable_excursion': 0.067976}, '10d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': 0.007135, 'median_return': -0.004918, 'mean_absolute_return': 0.03008, 'max_adverse_excursion': -0.065085, 'max_favorable_excursion': 0.109183}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.017065, 'median_return': 0.01927, 'mean_absolute_return': 0.047266, 'max_adverse_excursion': -0.120224, 'max_favorable_excursion': 0.158039}, '60d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.021253, 'median_return': 0.00464, 'mean_absolute_return': 0.079456, 'max_adverse_excursion': -0.182805, 'max_favorable_excursion': 0.258847}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.3375}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.3875}, '20d': {'sample_size': 80, 'hit_rate': 0.5125}, '60d': {'sample_size': 80, 'hit_rate': 0.4}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.25, 'both_hit': 17, 'both_miss': 23}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.075, 'both_hit': 19, 'both_miss': 21}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': -0.1, 'both_hit': 15, 'both_miss': 25}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.075, 'both_hit': 24, 'both_miss': 16}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 20, 'both_miss': 20}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.016456, 'median_return': 0.022992, 'mean_absolute_return': 0.025701, 'max_adverse_excursion': -0.035222, 'max_favorable_excursion': 0.047314}, '5d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.017091, 'median_return': 0.024027, 'mean_absolute_return': 0.031051, 'max_adverse_excursion': -0.032427, 'max_favorable_excursion': 0.067976}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.016716, 'median_return': 0.021743, 'mean_absolute_return': 0.045917, 'max_adverse_excursion': -0.065085, 'max_favorable_excursion': 0.109183}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.03743, 'median_return': 0.036446, 'mean_absolute_return': 0.070265, 'max_adverse_excursion': -0.093242, 'max_favorable_excursion': 0.158039}, '60d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.070873, 'median_return': 0.055167, 'mean_absolute_return': 0.104436, 'max_adverse_excursion': -0.168571, 'max_favorable_excursion': 0.258847}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.3667, 'avg_return': -0.003039, 'median_return': -0.007357, 'mean_absolute_return': 0.017631, 'max_adverse_excursion': -0.040531, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.000384, 'median_return': 0.000415, 'mean_absolute_return': 0.017797, 'max_adverse_excursion': -0.050569, 'max_favorable_excursion': 0.062512}, '10d': {'sample_size': 60, 'hit_rate': 0.3667, 'avg_return': 0.000976, 'median_return': -0.00923, 'mean_absolute_return': 0.022805, 'max_adverse_excursion': -0.05959, 'max_favorable_excursion': 0.099025}, '20d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.008551, 'median_return': 0.013823, 'mean_absolute_return': 0.037711, 'max_adverse_excursion': -0.120224, 'max_favorable_excursion': 0.117235}, '60d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': 0.00331, 'median_return': -0.006198, 'mean_absolute_return': 0.070018, 'max_adverse_excursion': -0.182805, 'max_favorable_excursion': 0.195631}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.3667`, avg `-0.003039`, median `-0.007357`, mae `0.017631`
- 5d: sample `60`, hit `0.5`, avg `-0.000384`, median `0.000415`, mae `0.017797`
- 10d: sample `60`, hit `0.3667`, avg `0.000976`, median `-0.00923`, mae `0.022805`
- 20d: sample `60`, hit `0.5833`, avg `0.008551`, median `0.013823`, mae `0.037711`
- 60d: sample `60`, hit `0.45`, avg `0.00331`, median `-0.006198`, mae `0.070018`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.016456`, median `0.022992`, mae `0.025701`
- 5d: sample `20`, hit `0.7`, avg `0.017091`, median `0.024027`, mae `0.031051`
- 10d: sample `20`, hit `0.55`, avg `0.016716`, median `0.021743`, mae `0.045917`
- 20d: sample `20`, hit `0.7`, avg `0.03743`, median `0.036446`, mae `0.070265`
- 60d: sample `20`, hit `0.75`, avg `0.070873`, median `0.055167`, mae `0.104436`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.3667`, avg `-0.003039`, median `-0.007357`, mae `0.017631`
- 5d: sample `60`, hit `0.5`, avg `-0.000384`, median `0.000415`, mae `0.017797`
- 10d: sample `60`, hit `0.3667`, avg `0.000976`, median `-0.00923`, mae `0.022805`
- 20d: sample `60`, hit `0.5833`, avg `0.008551`, median `0.013823`, mae `0.037711`
- 60d: sample `60`, hit `0.45`, avg `0.00331`, median `-0.006198`, mae `0.070018`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.3667`, avg `-0.003039`, median `-0.007357`, mae `0.017631`
- 5d: sample `60`, hit `0.5`, avg `-0.000384`, median `0.000415`, mae `0.017797`
- 10d: sample `60`, hit `0.3667`, avg `0.000976`, median `-0.00923`, mae `0.022805`
- 20d: sample `60`, hit `0.5833`, avg `0.008551`, median `0.013823`, mae `0.037711`
- 60d: sample `60`, hit `0.45`, avg `0.00331`, median `-0.006198`, mae `0.070018`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.016456`, median `0.022992`, mae `0.025701`
- 5d: sample `20`, hit `0.7`, avg `0.017091`, median `0.024027`, mae `0.031051`
- 10d: sample `20`, hit `0.55`, avg `0.016716`, median `0.021743`, mae `0.045917`
- 20d: sample `20`, hit `0.7`, avg `0.03743`, median `0.036446`, mae `0.070265`
- 60d: sample `20`, hit `0.75`, avg `0.070873`, median `0.055167`, mae `0.104436`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.006703`, median `-0.009383`, mae `0.016301`
- 5d: sample `40`, hit `0.45`, avg `-0.005379`, median `-0.001796`, mae `0.015186`
- 10d: sample `40`, hit `0.275`, avg `-0.005043`, median `-0.01051`, mae `0.017161`
- 20d: sample `40`, hit `0.575`, avg `0.008611`, median `0.016745`, mae `0.030726`
- 60d: sample `40`, hit `0.45`, avg `0.002402`, median `-0.005523`, mae `0.057678`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.004288`, median `0.001999`, mae `0.02029`
- 5d: sample `20`, hit `0.6`, avg `0.009607`, median `0.009706`, mae `0.023018`
- 10d: sample `20`, hit `0.55`, avg `0.013013`, median `0.001447`, mae `0.034091`
- 20d: sample `20`, hit `0.6`, avg `0.00843`, median `0.013823`, mae `0.051683`
- 60d: sample `20`, hit `0.45`, avg `0.005126`, median `-0.029513`, mae `0.0947`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.016456`, median `0.022992`, mae `0.025701`
- 5d: sample `20`, hit `0.7`, avg `0.017091`, median `0.024027`, mae `0.031051`
- 10d: sample `20`, hit `0.55`, avg `0.016716`, median `0.021743`, mae `0.045917`
- 20d: sample `20`, hit `0.7`, avg `0.03743`, median `0.036446`, mae `0.070265`
- 60d: sample `20`, hit `0.75`, avg `0.070873`, median `0.055167`, mae `0.104436`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.006703`, median `-0.009383`, mae `0.016301`
- 5d: sample `40`, hit `0.45`, avg `-0.005379`, median `-0.001796`, mae `0.015186`
- 10d: sample `40`, hit `0.275`, avg `-0.005043`, median `-0.01051`, mae `0.017161`
- 20d: sample `40`, hit `0.575`, avg `0.008611`, median `0.016745`, mae `0.030726`
- 60d: sample `40`, hit `0.45`, avg `0.002402`, median `-0.005523`, mae `0.057678`

### bounce_surface_only
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `0.001834`, median `-0.001347`, mae `0.019648`
- 5d: sample `80`, hit `0.55`, avg `0.003985`, median `0.003026`, mae `0.021111`
- 10d: sample `80`, hit `0.4125`, avg `0.004911`, median `-0.007011`, mae `0.028583`
- 20d: sample `80`, hit `0.6125`, avg `0.015771`, median `0.017416`, mae `0.04585`
- 60d: sample `80`, hit `0.525`, avg `0.020201`, median `0.00464`, mae `0.078623`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `0.001834`, median `-0.001347`, mae `0.019648`
- 5d: sample `80`, hit `0.55`, avg `0.003985`, median `0.003026`, mae `0.021111`
- 10d: sample `80`, hit `0.4125`, avg `0.004911`, median `-0.007011`, mae `0.028583`
- 20d: sample `80`, hit `0.6125`, avg `0.015771`, median `0.017416`, mae `0.04585`
- 60d: sample `80`, hit `0.525`, avg `0.020201`, median `0.00464`, mae `0.078623`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.3667`, avg `-0.003039`, median `-0.007357`, mae `0.017631`
- 5d: sample `60`, hit `0.5`, avg `-0.000384`, median `0.000415`, mae `0.017797`
- 10d: sample `60`, hit `0.3667`, avg `0.000976`, median `-0.00923`, mae `0.022805`
- 20d: sample `60`, hit `0.5833`, avg `0.008551`, median `0.013823`, mae `0.037711`
- 60d: sample `60`, hit `0.45`, avg `0.00331`, median `-0.006198`, mae `0.070018`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.3667`, avg `-0.003039`, median `-0.007357`, mae `0.017631`
- 5d: sample `60`, hit `0.5`, avg `-0.000384`, median `0.000415`, mae `0.017797`
- 10d: sample `60`, hit `0.3667`, avg `0.000976`, median `-0.00923`, mae `0.022805`
- 20d: sample `60`, hit `0.5833`, avg `0.008551`, median `0.013823`, mae `0.037711`
- 60d: sample `60`, hit `0.45`, avg `0.00331`, median `-0.006198`, mae `0.070018`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.016456`, median `0.022992`, mae `0.025701`
- 5d: sample `20`, hit `0.7`, avg `0.017091`, median `0.024027`, mae `0.031051`
- 10d: sample `20`, hit `0.55`, avg `0.016716`, median `0.021743`, mae `0.045917`
- 20d: sample `20`, hit `0.7`, avg `0.03743`, median `0.036446`, mae `0.070265`
- 60d: sample `20`, hit `0.75`, avg `0.070873`, median `0.055167`, mae `0.104436`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
