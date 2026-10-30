# High Confidence Edge Report

Generated at: `2026-10-30T01:27:41.417261+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `148`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `148`, gate `stronger_evidence`
- 5d: completed `148`, gate `stronger_evidence`
- 10d: completed `148`, gate `stronger_evidence`
- 20d: completed `148`, gate `stronger_evidence`
- 60d: completed `148`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004674`, median `0.008833`, mae `0.016902`
- 5d: sample `60`, hit `0.55`, avg `0.002404`, median `0.002812`, mae `0.022975`
- 10d: sample `60`, hit `0.5`, avg `-0.003602`, median `9.9e-05`, mae `0.03857`
- 20d: sample `60`, hit `0.5`, avg `-0.007306`, median `0.000994`, mae `0.046778`
- 60d: sample `60`, hit `0.8167`, avg `0.053269`, median `0.059488`, mae `0.064654`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001616`, median `0.007291`, mae `0.02269`
- 5d: sample `20`, hit `0.6`, avg `-0.003017`, median `0.009561`, mae `0.026981`
- 10d: sample `20`, hit `0.65`, avg `0.004255`, median `0.010251`, mae `0.027023`
- 20d: sample `20`, hit `0.55`, avg `0.003742`, median `0.001939`, mae `0.027065`
- 60d: sample `20`, hit `1.0`, avg `0.110559`, median `0.109805`, mae `0.110559`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.004674, 'median_return': 0.008833, 'mean_absolute_return': 0.016902, 'max_adverse_excursion': -0.038555, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.002404, 'median_return': 0.002812, 'mean_absolute_return': 0.022975, 'max_adverse_excursion': -0.041734, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.003602, 'median_return': 9.9e-05, 'mean_absolute_return': 0.03857, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.069999}, '20d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.007306, 'median_return': 0.000994, 'mean_absolute_return': 0.046778, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.053269, 'median_return': 0.059488, 'mean_absolute_return': 0.064654, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.140645}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.011129, 'median_return': 0.020188, 'mean_absolute_return': 0.019772, 'max_adverse_excursion': -0.018946, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.008236, 'median_return': 0.030736, 'mean_absolute_return': 0.032516, 'max_adverse_excursion': -0.039725, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003698, 'median_return': 0.036012, 'mean_absolute_return': 0.044778, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003955, 'median_return': 0.02284, 'mean_absolute_return': 0.038328, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.060367}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.055409, 'median_return': 0.069082, 'mean_absolute_return': 0.057947, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.117089}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.00221, 'median_return': 0.00745, 'mean_absolute_return': 0.018191, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.00025, 'median_return': 0.005387, 'mean_absolute_return': 0.023028, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.002231, 'median_return': 0.001598, 'mean_absolute_return': 0.034673, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.069999}, '20d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.004609, 'median_return': 0.000994, 'mean_absolute_return': 0.042241, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 72, 'hit_rate': 0.8611, 'avg_return': 0.068945, 'median_return': 0.072453, 'mean_absolute_return': 0.078151, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.188608}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.4625}, '20d': {'sample_size': 80, 'hit_rate': 0.4875}, '60d': {'sample_size': 80, 'hit_rate': 0.6125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.1, 'both_hit': 13, 'both_miss': 7}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.05, 'both_hit': 13, 'both_miss': 7}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.1, 'both_hit': 11, 'both_miss': 9}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 10, 'both_miss': 10}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 19, 'both_miss': 1}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.006511, 'median_return': 0.010308, 'mean_absolute_return': 0.016854, 'max_adverse_excursion': -0.028791, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.001822, 'median_return': 0.000548, 'mean_absolute_return': 0.023454, 'max_adverse_excursion': -0.041734, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.002246, 'median_return': 0.001411, 'mean_absolute_return': 0.039143, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.067422}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': -0.000477, 'median_return': 0.019563, 'mean_absolute_return': 0.047282, 'max_adverse_excursion': -0.103697, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.066767, 'median_return': 0.096389, 'mean_absolute_return': 0.083029, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.140645}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.001965, 'median_return': 0.00745, 'mean_absolute_return': 0.018847, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.04128}, '5d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.00079, 'median_return': 0.006018, 'mean_absolute_return': 0.024151, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.001435, 'median_return': 0.008188, 'mean_absolute_return': 0.03453, 'max_adverse_excursion': -0.104082, 'max_favorable_excursion': 0.069999}, '20d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.005899, 'median_return': -0.007733, 'mean_absolute_return': 0.040039, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.07754}, '60d': {'sample_size': 60, 'hit_rate': 0.8833, 'avg_return': 0.067866, 'median_return': 0.069082, 'mean_absolute_return': 0.073831, 'max_adverse_excursion': -0.039851, 'max_favorable_excursion': 0.188608}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004674`, median `0.008833`, mae `0.016902`
- 5d: sample `60`, hit `0.55`, avg `0.002404`, median `0.002812`, mae `0.022975`
- 10d: sample `60`, hit `0.5`, avg `-0.003602`, median `9.9e-05`, mae `0.03857`
- 20d: sample `60`, hit `0.5`, avg `-0.007306`, median `0.000994`, mae `0.046778`
- 60d: sample `60`, hit `0.8167`, avg `0.053269`, median `0.059488`, mae `0.064654`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001616`, median `0.007291`, mae `0.02269`
- 5d: sample `20`, hit `0.6`, avg `-0.003017`, median `0.009561`, mae `0.026981`
- 10d: sample `20`, hit `0.65`, avg `0.004255`, median `0.010251`, mae `0.027023`
- 20d: sample `20`, hit `0.55`, avg `0.003742`, median `0.001939`, mae `0.027065`
- 60d: sample `20`, hit `1.0`, avg `0.110559`, median `0.109805`, mae `0.110559`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004674`, median `0.008833`, mae `0.016902`
- 5d: sample `60`, hit `0.55`, avg `0.002404`, median `0.002812`, mae `0.022975`
- 10d: sample `60`, hit `0.5`, avg `-0.003602`, median `9.9e-05`, mae `0.03857`
- 20d: sample `60`, hit `0.5`, avg `-0.007306`, median `0.000994`, mae `0.046778`
- 60d: sample `60`, hit `0.8167`, avg `0.053269`, median `0.059488`, mae `0.064654`

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
- 3d: sample `60`, hit `0.6333`, avg `0.004674`, median `0.008833`, mae `0.016902`
- 5d: sample `60`, hit `0.55`, avg `0.002404`, median `0.002812`, mae `0.022975`
- 10d: sample `60`, hit `0.5`, avg `-0.003602`, median `9.9e-05`, mae `0.03857`
- 20d: sample `60`, hit `0.5`, avg `-0.007306`, median `0.000994`, mae `0.046778`
- 60d: sample `60`, hit `0.8167`, avg `0.053269`, median `0.059488`, mae `0.064654`

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
- 3d: sample `20`, hit `0.55`, avg `-0.001616`, median `0.007291`, mae `0.02269`
- 5d: sample `20`, hit `0.6`, avg `-0.003017`, median `0.009561`, mae `0.026981`
- 10d: sample `20`, hit `0.65`, avg `0.004255`, median `0.010251`, mae `0.027023`
- 20d: sample `20`, hit `0.55`, avg `0.003742`, median `0.001939`, mae `0.027065`
- 60d: sample `20`, hit `1.0`, avg `0.110559`, median `0.109805`, mae `0.110559`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.003755`, median `0.008174`, mae `0.016925`
- 5d: sample `40`, hit `0.575`, avg `0.002694`, median `0.005387`, mae `0.022736`
- 10d: sample `40`, hit `0.475`, avg `-0.00428`, median `-0.004602`, mae `0.038284`
- 20d: sample `40`, hit `0.425`, avg `-0.01072`, median `-0.021765`, mae `0.046527`
- 60d: sample `40`, hit `0.825`, avg `0.046519`, median `0.055986`, mae `0.055467`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006511`, median `0.010308`, mae `0.016854`
- 5d: sample `20`, hit `0.5`, avg `0.001822`, median `0.000548`, mae `0.023454`
- 10d: sample `20`, hit `0.55`, avg `-0.002246`, median `0.001411`, mae `0.039143`
- 20d: sample `20`, hit `0.65`, avg `-0.000477`, median `0.019563`, mae `0.047282`
- 60d: sample `20`, hit `0.8`, avg `0.066767`, median `0.096389`, mae `0.083029`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001616`, median `0.007291`, mae `0.02269`
- 5d: sample `20`, hit `0.6`, avg `-0.003017`, median `0.009561`, mae `0.026981`
- 10d: sample `20`, hit `0.65`, avg `0.004255`, median `0.010251`, mae `0.027023`
- 20d: sample `20`, hit `0.55`, avg `0.003742`, median `0.001939`, mae `0.027065`
- 60d: sample `20`, hit `1.0`, avg `0.110559`, median `0.109805`, mae `0.110559`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.003755`, median `0.008174`, mae `0.016925`
- 5d: sample `40`, hit `0.575`, avg `0.002694`, median `0.005387`, mae `0.022736`
- 10d: sample `40`, hit `0.475`, avg `-0.00428`, median `-0.004602`, mae `0.038284`
- 20d: sample `40`, hit `0.425`, avg `-0.01072`, median `-0.021765`, mae `0.046527`
- 60d: sample `40`, hit `0.825`, avg `0.046519`, median `0.055986`, mae `0.055467`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.00351`, median `0.009859`, mae `0.020352`
- 5d: sample `60`, hit `0.5833`, avg `0.001138`, median `0.005387`, mae `0.025457`
- 10d: sample `60`, hit `0.5833`, avg `0.002904`, median `0.010251`, mae `0.035412`
- 20d: sample `60`, hit `0.5667`, avg `5.9e-05`, median `0.004568`, mae `0.042291`
- 60d: sample `60`, hit `0.9167`, avg `0.079692`, median `0.086722`, mae `0.085452`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.003102`, median `0.008174`, mae `0.018349`
- 5d: sample `80`, hit `0.5625`, avg `0.001048`, median `0.005387`, mae `0.023976`
- 10d: sample `80`, hit `0.5375`, avg `-0.001638`, median `0.001598`, mae `0.035683`
- 20d: sample `80`, hit `0.5125`, avg `-0.004544`, median `0.000994`, mae `0.04185`
- 60d: sample `80`, hit `0.8625`, avg `0.067591`, median `0.06911`, mae `0.076131`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.006073`, median `0.012066`, mae `0.019183`
- 5d: sample `40`, hit `0.575`, avg `0.003215`, median `0.002812`, mae `0.024696`
- 10d: sample `40`, hit `0.55`, avg `0.002229`, median `0.016142`, mae `0.039607`
- 20d: sample `40`, hit `0.575`, avg `-0.001783`, median `0.019563`, mae `0.049904`
- 60d: sample `40`, hit `0.875`, avg `0.064259`, median `0.069082`, mae `0.072898`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004674`, median `0.008833`, mae `0.016902`
- 5d: sample `60`, hit `0.55`, avg `0.002404`, median `0.002812`, mae `0.022975`
- 10d: sample `60`, hit `0.5`, avg `-0.003602`, median `9.9e-05`, mae `0.03857`
- 20d: sample `60`, hit `0.5`, avg `-0.007306`, median `0.000994`, mae `0.046778`
- 60d: sample `60`, hit `0.8167`, avg `0.053269`, median `0.059488`, mae `0.064654`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001616`, median `0.007291`, mae `0.02269`
- 5d: sample `20`, hit `0.6`, avg `-0.003017`, median `0.009561`, mae `0.026981`
- 10d: sample `20`, hit `0.65`, avg `0.004255`, median `0.010251`, mae `0.027023`
- 20d: sample `20`, hit `0.55`, avg `0.003742`, median `0.001939`, mae `0.027065`
- 60d: sample `20`, hit `1.0`, avg `0.110559`, median `0.109805`, mae `0.110559`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
