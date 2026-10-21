# High Confidence Edge Report

Generated at: `2026-10-21T01:32:18.871420+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `120`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `120`, gate `stronger_evidence`
- 5d: completed `120`, gate `stronger_evidence`
- 10d: completed `120`, gate `stronger_evidence`
- 20d: completed `120`, gate `stronger_evidence`
- 60d: completed `120`, gate `stronger_evidence`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001975`, median `0.001199`, mae `0.012709`
- 5d: sample `40`, hit `0.575`, avg `-0.002855`, median `0.003005`, mae `0.015067`
- 10d: sample `40`, hit `0.45`, avg `1.4e-05`, median `-0.000231`, mae `0.017085`
- 20d: sample `40`, hit `0.725`, avg `0.017104`, median `0.021759`, mae `0.029605`
- 60d: sample `40`, hit `0.6`, avg `0.013832`, median `0.032628`, mae `0.074274`

### NO_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.0`, median `0.006632`, mae `0.017858`
- 5d: sample `20`, hit `0.5`, avg `0.001017`, median `0.001573`, mae `0.022799`
- 10d: sample `20`, hit `0.65`, avg `0.00778`, median `0.009854`, mae `0.027477`
- 20d: sample `20`, hit `0.7`, avg `0.024637`, median `0.014522`, mae `0.032658`
- 60d: sample `20`, hit `0.8`, avg `0.060023`, median `0.055167`, mae `0.077284`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `4.2e-05`, median `0.000496`, mae `0.014328`
- 5d: sample `20`, hit `0.45`, avg `-0.005327`, median `-0.011925`, mae `0.019651`
- 10d: sample `20`, hit `0.3`, avg `-0.016779`, median `-0.021171`, mae `0.034295`
- 20d: sample `20`, hit `0.45`, avg `-0.001306`, median `-0.00018`, mae `0.03334`
- 60d: sample `20`, hit `0.75`, avg `0.050935`, median `0.064934`, mae `0.07579`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.00592`, median `0.00745`, mae `0.009339`
- 5d: sample `8`, hit `0.75`, avg `0.006419`, median `0.011724`, mae `0.009148`
- 10d: sample `8`, hit `0.75`, avg `0.008099`, median `0.011`, mae `0.009445`
- 20d: sample `8`, hit `0.875`, avg `0.017643`, median `0.023636`, mae `0.019868`
- 60d: sample `8`, hit `0.625`, avg `-0.009263`, median `0.046273`, mae `0.083915`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.011091`, median `-0.010033`, mae `0.014744`
- 5d: sample `8`, hit `0.375`, avg `-0.015262`, median `-0.022295`, mae `0.020634`
- 10d: sample `8`, hit `0.125`, avg `-0.010057`, median `-0.006017`, mae `0.012815`
- 20d: sample `8`, hit `0.75`, avg `0.029025`, median `0.043456`, mae `0.037455`
- 60d: sample `8`, hit `0.75`, avg `0.064406`, median `0.099838`, mae `0.086125`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.011091, 'median_return': -0.010033, 'mean_absolute_return': 0.014744, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.012272}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.015262, 'median_return': -0.022295, 'mean_absolute_return': 0.020634, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.010057, 'median_return': -0.006017, 'mean_absolute_return': 0.012815, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.011031}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.029025, 'median_return': 0.043456, 'mean_absolute_return': 0.037455, 'max_adverse_excursion': -0.02149, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.064406, 'median_return': 0.099838, 'mean_absolute_return': 0.086125, 'max_adverse_excursion': -0.055789, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.000146, 'median_return': 0.003785, 'mean_absolute_return': 0.014363, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.001088, 'median_return': 0.001695, 'mean_absolute_return': 0.01787, 'max_adverse_excursion': -0.047223, 'max_favorable_excursion': 0.04835}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.001374, 'median_return': 0.00118, 'mean_absolute_return': 0.025227, 'max_adverse_excursion': -0.060434, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.012758, 'median_return': 0.012046, 'mean_absolute_return': 0.030618, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.086756}, '60d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.03135, 'median_return': 0.043741, 'mean_absolute_return': 0.074215, 'max_adverse_excursion': -0.138565, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.5375}, '20d': {'sample_size': 80, 'hit_rate': 0.35}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.001975, 'median_return': 0.001199, 'mean_absolute_return': 0.012709, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.002855, 'median_return': 0.003005, 'mean_absolute_return': 0.015067, 'max_adverse_excursion': -0.04605, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 1.4e-05, 'median_return': -0.000231, 'mean_absolute_return': 0.017085, 'max_adverse_excursion': -0.060333, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.017104, 'median_return': 0.021759, 'mean_absolute_return': 0.029605, 'max_adverse_excursion': -0.062788, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.013832, 'median_return': 0.032628, 'mean_absolute_return': 0.074274, 'max_adverse_excursion': -0.138565, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 2.1e-05, 'median_return': 0.000496, 'mean_absolute_return': 0.016093, 'max_adverse_excursion': -0.034896, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.002155, 'median_return': -0.002776, 'mean_absolute_return': 0.021225, 'max_adverse_excursion': -0.047223, 'max_favorable_excursion': 0.04835}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.0045, 'median_return': -0.010145, 'mean_absolute_return': 0.030886, 'max_adverse_excursion': -0.060434, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.011666, 'median_return': 0.008882, 'mean_absolute_return': 0.032999, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.086756}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.055479, 'median_return': 0.059007, 'mean_absolute_return': 0.076537, 'max_adverse_excursion': -0.111942, 'max_favorable_excursion': 0.21267}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001975`, median `0.001199`, mae `0.012709`
- 5d: sample `40`, hit `0.575`, avg `-0.002855`, median `0.003005`, mae `0.015067`
- 10d: sample `40`, hit `0.45`, avg `1.4e-05`, median `-0.000231`, mae `0.017085`
- 20d: sample `40`, hit `0.725`, avg `0.017104`, median `0.021759`, mae `0.029605`
- 60d: sample `40`, hit `0.6`, avg `0.013832`, median `0.032628`, mae `0.074274`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `2.1e-05`, median `0.000496`, mae `0.016093`
- 5d: sample `40`, hit `0.475`, avg `-0.002155`, median `-0.002776`, mae `0.021225`
- 10d: sample `40`, hit `0.475`, avg `-0.0045`, median `-0.010145`, mae `0.030886`
- 20d: sample `40`, hit `0.575`, avg `0.011666`, median `0.008882`, mae `0.032999`
- 60d: sample `40`, hit `0.775`, avg `0.055479`, median `0.059007`, mae `0.076537`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `2.1e-05`, median `0.000496`, mae `0.016093`
- 5d: sample `40`, hit `0.475`, avg `-0.002155`, median `-0.002776`, mae `0.021225`
- 10d: sample `40`, hit `0.475`, avg `-0.0045`, median `-0.010145`, mae `0.030886`
- 20d: sample `40`, hit `0.575`, avg `0.011666`, median `0.008882`, mae `0.032999`
- 60d: sample `40`, hit `0.775`, avg `0.055479`, median `0.059007`, mae `0.076537`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `-0.000977`, median `0.001149`, mae `0.014401`
- 5d: sample `80`, hit `0.525`, avg `-0.002505`, median `0.001573`, mae `0.018146`
- 10d: sample `80`, hit `0.4625`, avg `-0.002243`, median `-0.0004`, mae `0.023985`
- 20d: sample `80`, hit `0.65`, avg `0.014385`, median `0.012291`, mae `0.031302`
- 60d: sample `80`, hit `0.6875`, avg `0.034655`, median `0.046273`, mae `0.075406`

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
- 3d: sample `80`, hit `0.5125`, avg `-0.000977`, median `0.001149`, mae `0.014401`
- 5d: sample `80`, hit `0.525`, avg `-0.002505`, median `0.001573`, mae `0.018146`
- 10d: sample `80`, hit `0.4625`, avg `-0.002243`, median `-0.0004`, mae `0.023985`
- 20d: sample `80`, hit `0.65`, avg `0.014385`, median `0.012291`, mae `0.031302`
- 60d: sample `80`, hit `0.6875`, avg `0.034655`, median `0.046273`, mae `0.075406`

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
- 3d: sample `80`, hit `0.5125`, avg `-0.000977`, median `0.001149`, mae `0.014401`
- 5d: sample `80`, hit `0.525`, avg `-0.002505`, median `0.001573`, mae `0.018146`
- 10d: sample `80`, hit `0.4625`, avg `-0.002243`, median `-0.0004`, mae `0.023985`
- 20d: sample `80`, hit `0.65`, avg `0.014385`, median `0.012291`, mae `0.031302`
- 60d: sample `80`, hit `0.6875`, avg `0.034655`, median `0.046273`, mae `0.075406`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
