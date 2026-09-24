# High Confidence Edge Report

Generated at: `2026-09-24T17:17:05.141511+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `47`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `47`, gate `early_evidence`
- 5d: completed `47`, gate `early_evidence`
- 10d: completed `47`, gate `early_evidence`
- 20d: completed `47`, gate `early_evidence`
- 60d: completed `47`, gate `early_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.005245`, median `-0.003649`, mae `0.016038`
- 5d: sample `40`, hit `0.45`, avg `-0.010742`, median `-0.001562`, mae `0.017754`
- 10d: sample `40`, hit `0.375`, avg `-0.011225`, median `-0.006389`, mae `0.022639`
- 20d: sample `40`, hit `0.65`, avg `0.002143`, median `0.016027`, mae `0.041381`
- 60d: sample `40`, hit `0.8`, avg `0.024232`, median `0.03308`, mae `0.061846`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.007626`, median `-0.009843`, mae `0.019376`
- 5d: sample `40`, hit `0.4`, avg `-0.010372`, median `-0.013229`, mae `0.02452`
- 10d: sample `40`, hit `0.5`, avg `-0.007551`, median `0.000397`, mae `0.03209`
- 20d: sample `40`, hit `0.6`, avg `0.009876`, median `0.01927`, mae `0.04451`
- 60d: sample `40`, hit `0.825`, avg `0.05854`, median `0.084216`, mae `0.089169`

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
- 3d: sample `8`, hit `0.375`, avg `-0.009846`, median `-0.001658`, mae `0.024079`
- 5d: sample `8`, hit `0.5`, avg `-0.013804`, median `0.005072`, mae `0.022134`
- 10d: sample `8`, hit `0.125`, avg `-0.014418`, median `-0.013832`, mae `0.017175`
- 20d: sample `8`, hit `0.75`, avg `0.013426`, median `0.029166`, mae `0.043553`
- 60d: sample `8`, hit `0.875`, avg `0.052254`, median `0.072696`, mae `0.087536`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.009846`, median `-0.001658`, mae `0.024079`
- 5d: sample `8`, hit `0.5`, avg `-0.013804`, median `0.005072`, mae `0.022134`
- 10d: sample `8`, hit `0.125`, avg `-0.014418`, median `-0.013832`, mae `0.017175`
- 20d: sample `8`, hit `0.75`, avg `0.013426`, median `0.029166`, mae `0.043553`
- 60d: sample `8`, hit `0.875`, avg `0.052254`, median `0.072696`, mae `0.087536`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.005245, 'median_return': -0.003649, 'mean_absolute_return': 0.016038, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.010742, 'median_return': -0.001562, 'mean_absolute_return': 0.017754, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.011225, 'median_return': -0.006389, 'mean_absolute_return': 0.022639, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.036168}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.002143, 'median_return': 0.016027, 'mean_absolute_return': 0.041381, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.024232, 'median_return': 0.03308, 'mean_absolute_return': 0.061846, 'max_adverse_excursion': -0.146095, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.009846, 'median_return': -0.001658, 'mean_absolute_return': 0.024079, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.013804, 'median_return': 0.005072, 'mean_absolute_return': 0.022134, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.010589}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.014418, 'median_return': -0.013832, 'mean_absolute_return': 0.017175, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.011031}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.013426, 'median_return': 0.029166, 'mean_absolute_return': 0.043553, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.052254, 'median_return': 0.072696, 'mean_absolute_return': 0.087536, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.006057, 'median_return': -0.004296, 'mean_absolute_return': 0.016999, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.010196, 'median_return': -0.009444, 'mean_absolute_return': 0.021026, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.008829, 'median_return': -0.004767, 'mean_absolute_return': 0.028496, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.005185, 'median_return': 0.015725, 'mean_absolute_return': 0.042878, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.8056, 'avg_return': 0.040178, 'median_return': 0.05019, 'mean_absolute_return': 0.074171, 'max_adverse_excursion': -0.193228, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.3875}, '20d': {'sample_size': 80, 'hit_rate': 0.425}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.006435, 'median_return': -0.004296, 'mean_absolute_return': 0.017707, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': -0.010557, 'median_return': -0.009444, 'mean_absolute_return': 0.021137, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.009388, 'median_return': -0.006389, 'mean_absolute_return': 0.027364, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.006009, 'median_return': 0.016027, 'mean_absolute_return': 0.042945, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.8125, 'avg_return': 0.041386, 'median_return': 0.050438, 'mean_absolute_return': 0.075508, 'max_adverse_excursion': -0.193228, 'max_favorable_excursion': 0.154804}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4`, avg `-0.006435`, median `-0.004296`, mae `0.017707`
- 5d: sample `80`, hit `0.425`, avg `-0.010557`, median `-0.009444`, mae `0.021137`
- 10d: sample `80`, hit `0.4375`, avg `-0.009388`, median `-0.006389`, mae `0.027364`
- 20d: sample `80`, hit `0.625`, avg `0.006009`, median `0.016027`, mae `0.042945`
- 60d: sample `80`, hit `0.8125`, avg `0.041386`, median `0.050438`, mae `0.075508`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.010292`, median `-0.010094`, mae `0.022162`
- 5d: sample `20`, hit `0.3`, avg `-0.017705`, median `-0.018175`, mae `0.023983`
- 10d: sample `20`, hit `0.15`, avg `-0.021642`, median `-0.013832`, mae `0.026163`
- 20d: sample `20`, hit `0.6`, avg `0.00108`, median `0.020068`, mae `0.047614`
- 60d: sample `20`, hit `0.75`, avg `0.027605`, median `0.046132`, mae `0.077497`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.004869`, median `-0.001658`, mae `0.019587`
- 5d: sample `40`, hit `0.425`, avg `-0.010061`, median `-0.013237`, mae `0.021586`
- 10d: sample `40`, hit `0.35`, avg `-0.014497`, median `-0.010456`, mae `0.02457`
- 20d: sample `40`, hit `0.65`, avg `0.00643`, median `0.01927`, mae `0.038572`
- 60d: sample `40`, hit `0.8`, avg `0.039939`, median `0.053855`, mae `0.07286`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.010292`, median `-0.010094`, mae `0.022162`
- 5d: sample `20`, hit `0.3`, avg `-0.017705`, median `-0.018175`, mae `0.023983`
- 10d: sample `20`, hit `0.15`, avg `-0.021642`, median `-0.013832`, mae `0.026163`
- 20d: sample `20`, hit `0.6`, avg `0.00108`, median `0.020068`, mae `0.047614`
- 60d: sample `20`, hit `0.75`, avg `0.027605`, median `0.046132`, mae `0.077497`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.00515`, median `-0.003676`, mae `0.016222`
- 5d: sample `60`, hit `0.4667`, avg `-0.008174`, median `-0.005632`, mae `0.020189`
- 10d: sample `60`, hit `0.5333`, avg `-0.005303`, median `0.004306`, mae `0.027765`
- 20d: sample `60`, hit `0.6333`, avg `0.007653`, median `0.015725`, mae `0.041389`
- 60d: sample `60`, hit `0.8333`, avg `0.04598`, median `0.057507`, mae `0.074844`

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
- 3d: sample `80`, hit `0.4`, avg `-0.006435`, median `-0.004296`, mae `0.017707`
- 5d: sample `80`, hit `0.425`, avg `-0.010557`, median `-0.009444`, mae `0.021137`
- 10d: sample `80`, hit `0.4375`, avg `-0.009388`, median `-0.006389`, mae `0.027364`
- 20d: sample `80`, hit `0.625`, avg `0.006009`, median `0.016027`, mae `0.042945`
- 60d: sample `80`, hit `0.8125`, avg `0.041386`, median `0.050438`, mae `0.075508`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.010292`, median `-0.010094`, mae `0.022162`
- 5d: sample `20`, hit `0.3`, avg `-0.017705`, median `-0.018175`, mae `0.023983`
- 10d: sample `20`, hit `0.15`, avg `-0.021642`, median `-0.013832`, mae `0.026163`
- 20d: sample `20`, hit `0.6`, avg `0.00108`, median `0.020068`, mae `0.047614`
- 60d: sample `20`, hit `0.75`, avg `0.027605`, median `0.046132`, mae `0.077497`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.005245`, median `-0.003649`, mae `0.016038`
- 5d: sample `40`, hit `0.45`, avg `-0.010742`, median `-0.001562`, mae `0.017754`
- 10d: sample `40`, hit `0.375`, avg `-0.011225`, median `-0.006389`, mae `0.022639`
- 20d: sample `40`, hit `0.65`, avg `0.002143`, median `0.016027`, mae `0.041381`
- 60d: sample `40`, hit `0.8`, avg `0.024232`, median `0.03308`, mae `0.061846`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.010292`, median `-0.010094`, mae `0.022162`
- 5d: sample `20`, hit `0.3`, avg `-0.017705`, median `-0.018175`, mae `0.023983`
- 10d: sample `20`, hit `0.15`, avg `-0.021642`, median `-0.013832`, mae `0.026163`
- 20d: sample `20`, hit `0.6`, avg `0.00108`, median `0.020068`, mae `0.047614`
- 60d: sample `20`, hit `0.75`, avg `0.027605`, median `0.046132`, mae `0.077497`

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
