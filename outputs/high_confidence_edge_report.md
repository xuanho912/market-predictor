# High Confidence Edge Report

Generated at: `2026-10-29T00:24:22.751329+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `144`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `historical_proxy_supports_higher_confidence_but_forward_validation_required`

## Forward Sample Gates

- 3d: completed `144`, gate `stronger_evidence`
- 5d: completed `144`, gate `stronger_evidence`
- 10d: completed `144`, gate `stronger_evidence`
- 20d: completed `144`, gate `stronger_evidence`
- 60d: completed `144`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.006328`, median `0.012083`, mae `0.019438`
- 5d: sample `40`, hit `0.575`, avg `0.003431`, median `0.002812`, mae `0.024832`
- 10d: sample `40`, hit `0.55`, avg `0.000319`, median `0.016142`, mae `0.040555`
- 20d: sample `40`, hit `0.575`, avg `-0.000694`, median `0.019563`, mae `0.050338`
- 60d: sample `40`, hit `0.875`, avg `0.064306`, median `0.069082`, mae `0.072945`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.001909`, median `0.007291`, mae `0.018169`
- 5d: sample `40`, hit `0.575`, avg `0.001984`, median `0.00774`, mae `0.022126`
- 10d: sample `40`, hit `0.55`, avg `-0.00384`, median `0.008188`, mae `0.032596`
- 20d: sample `40`, hit `0.45`, avg `-0.006209`, median `-0.011521`, mae `0.033997`
- 60d: sample `40`, hit `0.85`, avg `0.073039`, median `0.077579`, mae `0.081479`

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
- 3d: sample `8`, hit `0.625`, avg `0.011129`, median `0.020188`, mae `0.019772`
- 5d: sample `8`, hit `0.625`, avg `0.008236`, median `0.030736`, mae `0.032516`
- 10d: sample `8`, hit `0.5`, avg `0.003698`, median `0.036012`, mae `0.044778`
- 20d: sample `8`, hit `0.5`, avg `-0.003955`, median `0.02284`, mae `0.038328`
- 60d: sample `8`, hit `0.875`, avg `0.055409`, median `0.069082`, mae `0.057947`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.011129`, median `0.020188`, mae `0.019772`
- 5d: sample `8`, hit `0.625`, avg `0.008236`, median `0.030736`, mae `0.032516`
- 10d: sample `8`, hit `0.5`, avg `0.003698`, median `0.036012`, mae `0.044778`
- 20d: sample `8`, hit `0.5`, avg `-0.003955`, median `0.02284`, mae `0.038328`
- 60d: sample `8`, hit `0.875`, avg `0.055409`, median `0.069082`, mae `0.057947`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.006328, 'median_return': 0.012083, 'mean_absolute_return': 0.019438, 'max_adverse_excursion': -0.038555, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.003431, 'median_return': 0.002812, 'mean_absolute_return': 0.024832, 'max_adverse_excursion': -0.041734, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.000319, 'median_return': 0.016142, 'mean_absolute_return': 0.040555, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.067422}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.000694, 'median_return': 0.019563, 'mean_absolute_return': 0.050338, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.064306, 'median_return': 0.069082, 'mean_absolute_return': 0.072945, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.140645}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.011129, 'median_return': 0.020188, 'mean_absolute_return': 0.019772, 'max_adverse_excursion': -0.018946, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.008236, 'median_return': 0.030736, 'mean_absolute_return': 0.032516, 'max_adverse_excursion': -0.039725, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003698, 'median_return': 0.036012, 'mean_absolute_return': 0.044778, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003955, 'median_return': 0.02284, 'mean_absolute_return': 0.038328, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.060367}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.055409, 'median_return': 0.069082, 'mean_absolute_return': 0.057947, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.117089}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.003339, 'median_return': 0.008574, 'mean_absolute_return': 0.018695, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.002093, 'median_return': 0.006018, 'mean_absolute_return': 0.022475, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -0.002367, 'median_return': 0.008188, 'mean_absolute_return': 0.035664, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.067422}, '20d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.003396, 'median_return': 0.000994, 'mean_absolute_return': 0.042594, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 72, 'hit_rate': 0.8611, 'avg_return': 0.070146, 'median_return': 0.077579, 'mean_absolute_return': 0.079352, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.188608}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.425}, '20d': {'sample_size': 80, 'hit_rate': 0.4875}, '60d': {'sample_size': 80, 'hit_rate': 0.6125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': 0.025, 'both_hit': 13, 'both_miss': 7}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 10, 'both_miss': 10}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.175, 'both_hit': 11, 'both_miss': 9}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.1, 'both_hit': 13, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.075, 'both_hit': 16, 'both_miss': 4}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.003456, 'median_return': 0.00745, 'mean_absolute_return': 0.017744, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.001956, 'median_return': 0.006712, 'mean_absolute_return': 0.022542, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.004262, 'median_return': 0.001785, 'mean_absolute_return': 0.035731, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.067422}, '20d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.00408, 'median_return': 0.000994, 'mean_absolute_return': 0.038207, 'max_adverse_excursion': -0.103293, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 60, 'hit_rate': 0.8333, 'avg_return': 0.071209, 'median_return': 0.082988, 'mean_absolute_return': 0.082256, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.188608}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.006103, 'median_return': 0.018606, 'mean_absolute_return': 0.02198, 'max_adverse_excursion': -0.038555, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.004961, 'median_return': 0.005387, 'mean_absolute_return': 0.02629, 'max_adverse_excursion': -0.041488, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.005743, 'median_return': 0.024811, 'mean_absolute_return': 0.039109, 'max_adverse_excursion': -0.104082, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.001566, 'median_return': 0.02284, 'mean_absolute_return': 0.054049, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 20, 'hit_rate': 0.95, 'avg_return': 0.061063, 'median_return': 0.065766, 'mean_absolute_return': 0.062078, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.117089}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.004733`, median `0.008833`, mae `0.01711`
- 5d: sample `60`, hit `0.5333`, avg `0.001869`, median `0.002574`, mae `0.023246`
- 10d: sample `60`, hit `0.4833`, avg `-0.005555`, median `-0.00304`, mae `0.039828`
- 20d: sample `60`, hit `0.5`, avg `-0.006546`, median `0.000994`, mae `0.047033`
- 60d: sample `60`, hit `0.8167`, avg `0.053984`, median `0.059606`, mae `0.06537`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.002272`, median `0.009859`, mae `0.023883`
- 5d: sample `20`, hit `0.7`, avg `0.005224`, median `0.011107`, mae `0.024178`
- 10d: sample `20`, hit `0.75`, avg `0.009622`, median `0.010559`, mae `0.026818`
- 20d: sample `20`, hit `0.55`, avg `0.00583`, median `0.001939`, mae `0.027572`
- 60d: sample `20`, hit `1.0`, avg `0.112737`, median `0.113503`, mae `0.112737`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.004733`, median `0.008833`, mae `0.01711`
- 5d: sample `60`, hit `0.5333`, avg `0.001869`, median `0.002574`, mae `0.023246`
- 10d: sample `60`, hit `0.4833`, avg `-0.005555`, median `-0.00304`, mae `0.039828`
- 20d: sample `60`, hit `0.5`, avg `-0.006546`, median `0.000994`, mae `0.047033`
- 60d: sample `60`, hit `0.8167`, avg `0.053984`, median `0.059606`, mae `0.06537`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006552`, median `0.010308`, mae `0.016895`
- 5d: sample `20`, hit `0.5`, avg `0.001902`, median `0.000548`, mae `0.023374`
- 10d: sample `20`, hit `0.55`, avg `-0.005105`, median `0.001411`, mae `0.042002`
- 20d: sample `20`, hit `0.65`, avg `0.000177`, median `0.019563`, mae `0.046628`
- 60d: sample `20`, hit `0.8`, avg `0.067549`, median `0.096389`, mae `0.083811`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.004733`, median `0.008833`, mae `0.01711`
- 5d: sample `60`, hit `0.5333`, avg `0.001869`, median `0.002574`, mae `0.023246`
- 10d: sample `60`, hit `0.4833`, avg `-0.005555`, median `-0.00304`, mae `0.039828`
- 20d: sample `60`, hit `0.5`, avg `-0.006546`, median `0.000994`, mae `0.047033`
- 60d: sample `60`, hit `0.8167`, avg `0.053984`, median `0.059606`, mae `0.06537`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006552`, median `0.010308`, mae `0.016895`
- 5d: sample `20`, hit `0.5`, avg `0.001902`, median `0.000548`, mae `0.023374`
- 10d: sample `20`, hit `0.55`, avg `-0.005105`, median `0.001411`, mae `0.042002`
- 20d: sample `20`, hit `0.65`, avg `0.000177`, median `0.019563`, mae `0.046628`
- 60d: sample `20`, hit `0.8`, avg `0.067549`, median `0.096389`, mae `0.083811`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.002272`, median `0.009859`, mae `0.023883`
- 5d: sample `20`, hit `0.7`, avg `0.005224`, median `0.011107`, mae `0.024178`
- 10d: sample `20`, hit `0.75`, avg `0.009622`, median `0.010559`, mae `0.026818`
- 20d: sample `20`, hit `0.55`, avg `0.00583`, median `0.001939`, mae `0.027572`
- 60d: sample `20`, hit `1.0`, avg `0.112737`, median `0.113503`, mae `0.112737`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006103`, median `0.018606`, mae `0.02198`
- 5d: sample `20`, hit `0.65`, avg `0.004961`, median `0.005387`, mae `0.02629`
- 10d: sample `20`, hit `0.55`, avg `0.005743`, median `0.024811`, mae `0.039109`
- 20d: sample `20`, hit `0.5`, avg `-0.001566`, median `0.02284`, mae `0.054049`
- 60d: sample `20`, hit `0.95`, avg `0.061063`, median `0.065766`, mae `0.062078`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.004048`, median `0.007259`, mae `0.014674`
- 5d: sample `40`, hit `0.475`, avg `0.000323`, median `-0.002194`, mae `0.021724`
- 10d: sample `40`, hit `0.45`, avg `-0.011204`, median `-0.008597`, mae `0.040187`
- 20d: sample `40`, hit `0.5`, avg `-0.009035`, median `0.000994`, mae `0.043525`
- 60d: sample `40`, hit `0.75`, avg `0.050445`, median `0.058598`, mae `0.067016`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.002272`, median `0.009859`, mae `0.023883`
- 5d: sample `20`, hit `0.7`, avg `0.005224`, median `0.011107`, mae `0.024178`
- 10d: sample `20`, hit `0.75`, avg `0.009622`, median `0.010559`, mae `0.026818`
- 20d: sample `20`, hit `0.55`, avg `0.00583`, median `0.001939`, mae `0.027572`
- 60d: sample `20`, hit `1.0`, avg `0.112737`, median `0.113503`, mae `0.112737`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006103`, median `0.018606`, mae `0.02198`
- 5d: sample `20`, hit `0.65`, avg `0.004961`, median `0.005387`, mae `0.02629`
- 10d: sample `20`, hit `0.55`, avg `0.005743`, median `0.024811`, mae `0.039109`
- 20d: sample `20`, hit `0.5`, avg `-0.001566`, median `0.02284`, mae `0.054049`
- 60d: sample `20`, hit `0.95`, avg `0.061063`, median `0.065766`, mae `0.062078`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.004412`, median `0.009859`, mae `0.020389`
- 5d: sample `40`, hit `0.6`, avg `0.003563`, median `0.009561`, mae `0.023776`
- 10d: sample `40`, hit `0.65`, avg `0.002259`, median `0.010251`, mae `0.03441`
- 20d: sample `40`, hit `0.6`, avg `0.003004`, median `0.004568`, mae `0.0371`
- 60d: sample `40`, hit `0.9`, avg `0.090143`, median `0.103439`, mae `0.098274`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.004118`, median `0.008833`, mae `0.018803`
- 5d: sample `80`, hit `0.575`, avg `0.002707`, median `0.006018`, mae `0.023479`
- 10d: sample `80`, hit `0.55`, avg `-0.001761`, median `0.008188`, mae `0.036576`
- 20d: sample `80`, hit `0.5125`, avg `-0.003452`, median `0.000994`, mae `0.042168`
- 60d: sample `80`, hit `0.8625`, avg `0.068673`, median `0.072453`, mae `0.077212`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006552`, median `0.010308`, mae `0.016895`
- 5d: sample `20`, hit `0.5`, avg `0.001902`, median `0.000548`, mae `0.023374`
- 10d: sample `20`, hit `0.55`, avg `-0.005105`, median `0.001411`, mae `0.042002`
- 20d: sample `20`, hit `0.65`, avg `0.000177`, median `0.019563`, mae `0.046628`
- 60d: sample `20`, hit `0.8`, avg `0.067549`, median `0.096389`, mae `0.083811`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.004733`, median `0.008833`, mae `0.01711`
- 5d: sample `60`, hit `0.5333`, avg `0.001869`, median `0.002574`, mae `0.023246`
- 10d: sample `60`, hit `0.4833`, avg `-0.005555`, median `-0.00304`, mae `0.039828`
- 20d: sample `60`, hit `0.5`, avg `-0.006546`, median `0.000994`, mae `0.047033`
- 60d: sample `60`, hit `0.8167`, avg `0.053984`, median `0.059606`, mae `0.06537`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.002272`, median `0.009859`, mae `0.023883`
- 5d: sample `20`, hit `0.7`, avg `0.005224`, median `0.011107`, mae `0.024178`
- 10d: sample `20`, hit `0.75`, avg `0.009622`, median `0.010559`, mae `0.026818`
- 20d: sample `20`, hit `0.55`, avg `0.00583`, median `0.001939`, mae `0.027572`
- 60d: sample `20`, hit `1.0`, avg `0.112737`, median `0.113503`, mae `0.112737`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
