# High Confidence Edge Report

Generated at: `2026-11-12T02:35:24.162926+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `184`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `184`, gate `stronger_evidence`
- 5d: completed `184`, gate `stronger_evidence`
- 10d: completed `184`, gate `stronger_evidence`
- 20d: completed `184`, gate `stronger_evidence`
- 60d: completed `184`, gate `stronger_evidence`

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
- 3d: sample `60`, hit `0.6333`, avg `0.00392`, median `0.010773`, mae `0.019335`
- 5d: sample `60`, hit `0.5667`, avg `0.003718`, median `0.006712`, mae `0.024644`
- 10d: sample `60`, hit `0.5333`, avg `0.002422`, median `0.016142`, mae `0.037602`
- 20d: sample `60`, hit `0.5833`, avg `0.004848`, median `0.020431`, mae `0.0476`
- 60d: sample `60`, hit `0.8333`, avg `0.054317`, median `0.066018`, mae `0.07261`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.00315`, median `0.009859`, mae `0.023428`
- 5d: sample `20`, hit `0.7`, avg `0.004979`, median `0.010926`, mae `0.025176`
- 10d: sample `20`, hit `0.7`, avg `0.005805`, median `0.010559`, mae `0.032041`
- 20d: sample `20`, hit `0.55`, avg `-0.002183`, median `0.001939`, mae `0.031423`
- 60d: sample `20`, hit `1.0`, avg `0.115376`, median `0.109805`, mae `0.115376`

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
- 3d: sample `8`, hit `0.5`, avg `0.004176`, median `0.017631`, mae `0.02022`
- 5d: sample `8`, hit `0.5`, avg `0.000383`, median `0.002812`, mae `0.030353`
- 10d: sample `8`, hit `0.375`, avg `-0.005346`, median `-0.020732`, mae `0.040918`
- 20d: sample `8`, hit `0.375`, avg `-0.026833`, median `-0.027546`, mae `0.046114`
- 60d: sample `8`, hit `0.875`, avg `0.045151`, median `0.065766`, mae `0.047689`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.004176`, median `0.017631`, mae `0.02022`
- 5d: sample `8`, hit `0.5`, avg `0.000383`, median `0.002812`, mae `0.030353`
- 10d: sample `8`, hit `0.375`, avg `-0.005346`, median `-0.020732`, mae `0.040918`
- 20d: sample `8`, hit `0.375`, avg `-0.026833`, median `-0.027546`, mae `0.046114`
- 60d: sample `8`, hit `0.875`, avg `0.045151`, median `0.065766`, mae `0.047689`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.00392, 'median_return': 0.010773, 'mean_absolute_return': 0.019335, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.003718, 'median_return': 0.006712, 'mean_absolute_return': 0.024644, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.055415}, '10d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.002422, 'median_return': 0.016142, 'mean_absolute_return': 0.037602, 'max_adverse_excursion': -0.104082, 'max_favorable_excursion': 0.067422}, '20d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.004848, 'median_return': 0.020431, 'mean_absolute_return': 0.0476, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 60, 'hit_rate': 0.8333, 'avg_return': 0.054317, 'median_return': 0.066018, 'mean_absolute_return': 0.07261, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004176, 'median_return': 0.017631, 'mean_absolute_return': 0.02022, 'max_adverse_excursion': -0.029605, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.000383, 'median_return': 0.002812, 'mean_absolute_return': 0.030353, 'max_adverse_excursion': -0.039725, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.005346, 'median_return': -0.020732, 'mean_absolute_return': 0.040918, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.026833, 'median_return': -0.027546, 'mean_absolute_return': 0.046114, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.029103}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.045151, 'median_return': 0.065766, 'mean_absolute_return': 0.047689, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.090399}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.003678, 'median_return': 0.010308, 'mean_absolute_return': 0.020373, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.004439, 'median_return': 0.008121, 'mean_absolute_return': 0.024158, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.055415}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.004225, 'median_return': 0.012215, 'mean_absolute_return': 0.035689, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.067422}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.006415, 'median_return': 0.009812, 'mean_absolute_return': 0.043272, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 72, 'hit_rate': 0.875, 'avg_return': 0.072297, 'median_return': 0.083723, 'mean_absolute_return': 0.087259, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.188608}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.475}, '20d': {'sample_size': 80, 'hit_rate': 0.55}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.05, 'both_hit': 26, 'both_miss': 14}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.125, 'both_hit': 25, 'both_miss': 15}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.175, 'both_hit': 25, 'both_miss': 15}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.075, 'both_hit': 27, 'both_miss': 13}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.775, 'primary_minus_secondary': -0.15, 'both_hit': 36, 'both_miss': 4}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.003641, 'median_return': 0.010773, 'mean_absolute_return': 0.023723, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.006739, 'median_return': 0.011107, 'mean_absolute_return': 0.026919, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.055415}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.012066, 'median_return': 0.019314, 'mean_absolute_return': 0.03425, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.067422}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.012355, 'median_return': 0.009812, 'mean_absolute_return': 0.037943, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.090096, 'median_return': 0.100324, 'mean_absolute_return': 0.108782, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.188608}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.003814, 'median_return': 0.008174, 'mean_absolute_return': 0.016993, 'max_adverse_excursion': -0.038555, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.001327, 'median_return': 0.002574, 'mean_absolute_return': 0.022636, 'max_adverse_excursion': -0.041488, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.005531, 'median_return': -0.007491, 'mean_absolute_return': 0.038175, 'max_adverse_excursion': -0.104082, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.006174, 'median_return': -0.020804, 'mean_absolute_return': 0.049169, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.049068, 'median_return': 0.057953, 'mean_absolute_return': 0.057822, 'max_adverse_excursion': -0.039851, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.00392`, median `0.010773`, mae `0.019335`
- 5d: sample `60`, hit `0.5667`, avg `0.003718`, median `0.006712`, mae `0.024644`
- 10d: sample `60`, hit `0.5333`, avg `0.002422`, median `0.016142`, mae `0.037602`
- 20d: sample `60`, hit `0.5833`, avg `0.004848`, median `0.020431`, mae `0.0476`
- 60d: sample `60`, hit `0.8333`, avg `0.054317`, median `0.066018`, mae `0.07261`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.00315`, median `0.009859`, mae `0.023428`
- 5d: sample `20`, hit `0.7`, avg `0.004979`, median `0.010926`, mae `0.025176`
- 10d: sample `20`, hit `0.7`, avg `0.005805`, median `0.010559`, mae `0.032041`
- 20d: sample `20`, hit `0.55`, avg `-0.002183`, median `0.001939`, mae `0.031423`
- 60d: sample `20`, hit `1.0`, avg `0.115376`, median `0.109805`, mae `0.115376`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.00392`, median `0.010773`, mae `0.019335`
- 5d: sample `60`, hit `0.5667`, avg `0.003718`, median `0.006712`, mae `0.024644`
- 10d: sample `60`, hit `0.5333`, avg `0.002422`, median `0.016142`, mae `0.037602`
- 20d: sample `60`, hit `0.5833`, avg `0.004848`, median `0.020431`, mae `0.0476`
- 60d: sample `60`, hit `0.8333`, avg `0.054317`, median `0.066018`, mae `0.07261`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.004132`, median `0.012083`, mae `0.024019`
- 5d: sample `20`, hit `0.65`, avg `0.0085`, median `0.021374`, mae `0.028662`
- 10d: sample `20`, hit `0.75`, avg `0.018327`, median `0.02569`, mae `0.036458`
- 20d: sample `20`, hit `0.8`, avg `0.026892`, median `0.023565`, mae `0.044463`
- 60d: sample `20`, hit `0.85`, avg `0.064816`, median `0.096389`, mae `0.102187`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.00392`, median `0.010773`, mae `0.019335`
- 5d: sample `60`, hit `0.5667`, avg `0.003718`, median `0.006712`, mae `0.024644`
- 10d: sample `60`, hit `0.5333`, avg `0.002422`, median `0.016142`, mae `0.037602`
- 20d: sample `60`, hit `0.5833`, avg `0.004848`, median `0.020431`, mae `0.0476`
- 60d: sample `60`, hit `0.8333`, avg `0.054317`, median `0.066018`, mae `0.07261`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.004132`, median `0.012083`, mae `0.024019`
- 5d: sample `20`, hit `0.65`, avg `0.0085`, median `0.021374`, mae `0.028662`
- 10d: sample `20`, hit `0.75`, avg `0.018327`, median `0.02569`, mae `0.036458`
- 20d: sample `20`, hit `0.8`, avg `0.026892`, median `0.023565`, mae `0.044463`
- 60d: sample `20`, hit `0.85`, avg `0.064816`, median `0.096389`, mae `0.102187`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.00315`, median `0.009859`, mae `0.023428`
- 5d: sample `20`, hit `0.7`, avg `0.004979`, median `0.010926`, mae `0.025176`
- 10d: sample `20`, hit `0.7`, avg `0.005805`, median `0.010559`, mae `0.032041`
- 20d: sample `20`, hit `0.55`, avg `-0.002183`, median `0.001939`, mae `0.031423`
- 60d: sample `20`, hit `1.0`, avg `0.115376`, median `0.109805`, mae `0.115376`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003814`, median `0.008174`, mae `0.016993`
- 5d: sample `40`, hit `0.525`, avg `0.001327`, median `0.002574`, mae `0.022636`
- 10d: sample `40`, hit `0.425`, avg `-0.005531`, median `-0.007491`, mae `0.038175`
- 20d: sample `40`, hit `0.475`, avg `-0.006174`, median `-0.020804`, mae `0.049169`
- 60d: sample `40`, hit `0.825`, avg `0.049068`, median `0.057953`, mae `0.057822`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.004132`, median `0.012083`, mae `0.024019`
- 5d: sample `20`, hit `0.65`, avg `0.0085`, median `0.021374`, mae `0.028662`
- 10d: sample `20`, hit `0.75`, avg `0.018327`, median `0.02569`, mae `0.036458`
- 20d: sample `20`, hit `0.8`, avg `0.026892`, median `0.023565`, mae `0.044463`
- 60d: sample `20`, hit `0.85`, avg `0.064816`, median `0.096389`, mae `0.102187`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003814`, median `0.008174`, mae `0.016993`
- 5d: sample `40`, hit `0.525`, avg `0.001327`, median `0.002574`, mae `0.022636`
- 10d: sample `40`, hit `0.425`, avg `-0.005531`, median `-0.007491`, mae `0.038175`
- 20d: sample `40`, hit `0.475`, avg `-0.006174`, median `-0.020804`, mae `0.049169`
- 60d: sample `40`, hit `0.825`, avg `0.049068`, median `0.057953`, mae `0.057822`

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
- 3d: sample `80`, hit `0.65`, avg `0.003728`, median `0.010308`, mae `0.020358`
- 5d: sample `80`, hit `0.6`, avg `0.004033`, median `0.00774`, mae `0.024777`
- 10d: sample `80`, hit `0.575`, avg `0.003268`, median `0.011071`, mae `0.036212`
- 20d: sample `80`, hit `0.575`, avg `0.00309`, median `0.009784`, mae `0.043556`
- 60d: sample `80`, hit `0.875`, avg `0.069582`, median `0.079039`, mae `0.083302`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.65`, avg `0.003728`, median `0.010308`, mae `0.020358`
- 5d: sample `80`, hit `0.6`, avg `0.004033`, median `0.00774`, mae `0.024777`
- 10d: sample `80`, hit `0.575`, avg `0.003268`, median `0.011071`, mae `0.036212`
- 20d: sample `80`, hit `0.575`, avg `0.00309`, median `0.009784`, mae `0.043556`
- 60d: sample `80`, hit `0.875`, avg `0.069582`, median `0.079039`, mae `0.083302`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.00392`, median `0.010773`, mae `0.019335`
- 5d: sample `60`, hit `0.5667`, avg `0.003718`, median `0.006712`, mae `0.024644`
- 10d: sample `60`, hit `0.5333`, avg `0.002422`, median `0.016142`, mae `0.037602`
- 20d: sample `60`, hit `0.5833`, avg `0.004848`, median `0.020431`, mae `0.0476`
- 60d: sample `60`, hit `0.8333`, avg `0.054317`, median `0.066018`, mae `0.07261`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.00392`, median `0.010773`, mae `0.019335`
- 5d: sample `60`, hit `0.5667`, avg `0.003718`, median `0.006712`, mae `0.024644`
- 10d: sample `60`, hit `0.5333`, avg `0.002422`, median `0.016142`, mae `0.037602`
- 20d: sample `60`, hit `0.5833`, avg `0.004848`, median `0.020431`, mae `0.0476`
- 60d: sample `60`, hit `0.8333`, avg `0.054317`, median `0.066018`, mae `0.07261`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.00315`, median `0.009859`, mae `0.023428`
- 5d: sample `20`, hit `0.7`, avg `0.004979`, median `0.010926`, mae `0.025176`
- 10d: sample `20`, hit `0.7`, avg `0.005805`, median `0.010559`, mae `0.032041`
- 20d: sample `20`, hit `0.55`, avg `-0.002183`, median `0.001939`, mae `0.031423`
- 60d: sample `20`, hit `1.0`, avg `0.115376`, median `0.109805`, mae `0.115376`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
