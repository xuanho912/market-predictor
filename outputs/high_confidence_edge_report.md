# High Confidence Edge Report

Generated at: `2026-10-16T16:42:32.869786+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `112`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `112`, gate `stronger_evidence`
- 5d: completed `112`, gate `stronger_evidence`
- 10d: completed `112`, gate `stronger_evidence`
- 20d: completed `112`, gate `stronger_evidence`
- 60d: completed `112`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.003971`, median `0.001405`, mae `0.011248`
- 5d: sample `20`, hit `0.55`, avg `-0.003412`, median `0.001303`, mae `0.013672`
- 10d: sample `20`, hit `0.55`, avg `-0.000366`, median `0.000397`, mae `0.01658`
- 20d: sample `20`, hit `0.55`, avg `0.010308`, median `0.010653`, mae `0.022522`
- 60d: sample `20`, hit `0.55`, avg `0.007545`, median `0.029164`, mae `0.056329`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `60`
- 3d: sample `60`, hit `0.3667`, avg `-0.006561`, median `-0.007083`, mae `0.016177`
- 5d: sample `60`, hit `0.4167`, avg `-0.007549`, median `-0.011925`, mae `0.020672`
- 10d: sample `60`, hit `0.3833`, avg `-0.007359`, median `-0.010456`, mae `0.027959`
- 20d: sample `60`, hit `0.6`, avg `0.016794`, median `0.017149`, mae `0.035897`
- 60d: sample `60`, hit `0.8`, avg `0.062821`, median `0.0765`, mae `0.085214`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.002903`, median `0.001405`, mae `0.009668`
- 5d: sample `8`, hit `0.5`, avg `-0.006121`, median `0.000688`, mae `0.014627`
- 10d: sample `8`, hit `0.5`, avg `-0.006253`, median `0.000197`, mae `0.012124`
- 20d: sample `8`, hit `0.5`, avg `0.014079`, median `0.01927`, mae `0.023566`
- 60d: sample `8`, hit `0.625`, avg `0.021077`, median `0.053855`, mae `0.043847`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.002903`, median `0.001405`, mae `0.009668`
- 5d: sample `8`, hit `0.5`, avg `-0.006121`, median `0.000688`, mae `0.014627`
- 10d: sample `8`, hit `0.5`, avg `-0.006253`, median `0.000197`, mae `0.012124`
- 20d: sample `8`, hit `0.5`, avg `0.014079`, median `0.01927`, mae `0.023566`
- 60d: sample `8`, hit `0.625`, avg `0.021077`, median `0.053855`, mae `0.043847`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.002903, 'median_return': 0.001405, 'mean_absolute_return': 0.009668, 'max_adverse_excursion': -0.029438, 'max_favorable_excursion': 0.010897}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006121, 'median_return': 0.000688, 'mean_absolute_return': 0.014627, 'max_adverse_excursion': -0.033868, 'max_favorable_excursion': 0.018625}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006253, 'median_return': 0.000197, 'mean_absolute_return': 0.012124, 'max_adverse_excursion': -0.025298, 'max_favorable_excursion': 0.017201}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.014079, 'median_return': 0.01927, 'mean_absolute_return': 0.023566, 'max_adverse_excursion': -0.016058, 'max_favorable_excursion': 0.046563}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.021077, 'median_return': 0.053855, 'mean_absolute_return': 0.043847, 'max_adverse_excursion': -0.046594, 'max_favorable_excursion': 0.059948}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.006248, 'median_return': -0.006508, 'mean_absolute_return': 0.015531, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.006559, 'median_return': -0.010337, 'mean_absolute_return': 0.0194, 'max_adverse_excursion': -0.04605, 'max_favorable_excursion': 0.04835}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.005539, 'median_return': -0.009464, 'mean_absolute_return': 0.026557, 'max_adverse_excursion': -0.060434, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.015294, 'median_return': 0.015416, 'mean_absolute_return': 0.033552, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.110633}, '60d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.052104, 'median_return': 0.068712, 'mean_absolute_return': 0.081787, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.575}, '20d': {'sample_size': 80, 'hit_rate': 0.4125}, '60d': {'sample_size': 80, 'hit_rate': 0.2625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.475, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.003971, 'median_return': 0.001405, 'mean_absolute_return': 0.011248, 'max_adverse_excursion': -0.03413, 'max_favorable_excursion': 0.015419}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.003412, 'median_return': 0.001303, 'mean_absolute_return': 0.013672, 'max_adverse_excursion': -0.033868, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.000366, 'median_return': 0.000397, 'mean_absolute_return': 0.01658, 'max_adverse_excursion': -0.03706, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.010308, 'median_return': 0.010653, 'mean_absolute_return': 0.022522, 'max_adverse_excursion': -0.042211, 'max_favorable_excursion': 0.053054}, '60d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.007545, 'median_return': 0.029164, 'mean_absolute_return': 0.056329, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.098228}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.3667, 'avg_return': -0.006561, 'median_return': -0.007083, 'mean_absolute_return': 0.016177, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.007549, 'median_return': -0.011925, 'mean_absolute_return': 0.020672, 'max_adverse_excursion': -0.04605, 'max_favorable_excursion': 0.04835}, '10d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.007359, 'median_return': -0.010456, 'mean_absolute_return': 0.027959, 'max_adverse_excursion': -0.060434, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.016794, 'median_return': 0.017149, 'mean_absolute_return': 0.035897, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.110633}, '60d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.062821, 'median_return': 0.0765, 'mean_absolute_return': 0.085214, 'max_adverse_excursion': -0.111942, 'max_favorable_excursion': 0.21267}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.005464`, median `0.000603`, mae `0.014109`
- 5d: sample `40`, hit `0.525`, avg `-0.006479`, median `0.001087`, mae `0.0166`
- 10d: sample `40`, hit `0.45`, avg `-0.002737`, median `-0.005891`, mae `0.019386`
- 20d: sample `40`, hit `0.6`, avg `0.014311`, median `0.015416`, mae `0.02785`
- 60d: sample `40`, hit `0.6`, avg `0.023778`, median `0.046132`, mae `0.068117`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.006363`, median `-0.008838`, mae `0.01578`
- 5d: sample `40`, hit `0.375`, avg `-0.006551`, median `-0.011925`, mae `0.021245`
- 10d: sample `40`, hit `0.4`, avg `-0.008484`, median `-0.01314`, mae `0.030842`
- 20d: sample `40`, hit `0.575`, avg `0.016034`, median `0.015713`, mae `0.037256`
- 60d: sample `40`, hit `0.875`, avg `0.074225`, median `0.079528`, mae `0.087869`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.003971`, median `0.001405`, mae `0.011248`
- 5d: sample `20`, hit `0.55`, avg `-0.003412`, median `0.001303`, mae `0.013672`
- 10d: sample `20`, hit `0.55`, avg `-0.000366`, median `0.000397`, mae `0.01658`
- 20d: sample `20`, hit `0.55`, avg `0.010308`, median `0.010653`, mae `0.022522`
- 60d: sample `20`, hit `0.55`, avg `0.007545`, median `0.029164`, mae `0.056329`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.003971`, median `0.001405`, mae `0.011248`
- 5d: sample `20`, hit `0.55`, avg `-0.003412`, median `0.001303`, mae `0.013672`
- 10d: sample `20`, hit `0.55`, avg `-0.000366`, median `0.000397`, mae `0.01658`
- 20d: sample `20`, hit `0.55`, avg `0.010308`, median `0.010653`, mae `0.022522`
- 60d: sample `20`, hit `0.55`, avg `0.007545`, median `0.029164`, mae `0.056329`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.006363`, median `-0.008838`, mae `0.01578`
- 5d: sample `40`, hit `0.375`, avg `-0.006551`, median `-0.011925`, mae `0.021245`
- 10d: sample `40`, hit `0.4`, avg `-0.008484`, median `-0.01314`, mae `0.030842`
- 20d: sample `40`, hit `0.575`, avg `0.016034`, median `0.015713`, mae `0.037256`
- 60d: sample `40`, hit `0.875`, avg `0.074225`, median `0.079528`, mae `0.087869`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.003971`, median `0.001405`, mae `0.011248`
- 5d: sample `20`, hit `0.55`, avg `-0.003412`, median `0.001303`, mae `0.013672`
- 10d: sample `20`, hit `0.55`, avg `-0.000366`, median `0.000397`, mae `0.01658`
- 20d: sample `20`, hit `0.55`, avg `0.010308`, median `0.010653`, mae `0.022522`
- 60d: sample `20`, hit `0.55`, avg `0.007545`, median `0.029164`, mae `0.056329`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.425`, avg `-0.005914`, median `-0.006202`, mae `0.014945`
- 5d: sample `80`, hit `0.45`, avg `-0.006515`, median `-0.009879`, mae `0.018922`
- 10d: sample `80`, hit `0.425`, avg `-0.005611`, median `-0.007491`, mae `0.025114`
- 20d: sample `80`, hit `0.5875`, avg `0.015172`, median `0.015416`, mae `0.032553`
- 60d: sample `80`, hit `0.7375`, avg `0.049002`, median `0.059495`, mae `0.077993`

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

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.425`, avg `-0.005914`, median `-0.006202`, mae `0.014945`
- 5d: sample `80`, hit `0.45`, avg `-0.006515`, median `-0.009879`, mae `0.018922`
- 10d: sample `80`, hit `0.425`, avg `-0.005611`, median `-0.007491`, mae `0.025114`
- 20d: sample `80`, hit `0.5875`, avg `0.015172`, median `0.015416`, mae `0.032553`
- 60d: sample `80`, hit `0.7375`, avg `0.049002`, median `0.059495`, mae `0.077993`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### risk_path_with_flow_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.425`, avg `-0.005914`, median `-0.006202`, mae `0.014945`
- 5d: sample `80`, hit `0.45`, avg `-0.006515`, median `-0.009879`, mae `0.018922`
- 10d: sample `80`, hit `0.425`, avg `-0.005611`, median `-0.007491`, mae `0.025114`
- 20d: sample `80`, hit `0.5875`, avg `0.015172`, median `0.015416`, mae `0.032553`
- 60d: sample `80`, hit `0.7375`, avg `0.049002`, median `0.059495`, mae `0.077993`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
