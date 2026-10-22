# High Confidence Edge Report

Generated at: `2026-10-22T17:14:05.180232+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `128`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `128`, gate `stronger_evidence`
- 5d: completed `128`, gate `stronger_evidence`
- 10d: completed `128`, gate `stronger_evidence`
- 20d: completed `128`, gate `stronger_evidence`
- 60d: completed `128`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.004833`, median `0.006372`, mae `0.009393`
- 5d: sample `20`, hit `0.7`, avg `0.006585`, median `0.00774`, mae `0.015986`
- 10d: sample `20`, hit `0.7`, avg `0.006683`, median `0.012215`, mae `0.021938`
- 20d: sample `20`, hit `0.75`, avg `0.015245`, median `0.015404`, mae `0.021905`
- 60d: sample `20`, hit `0.6`, avg `0.013374`, median `0.032524`, mae `0.054577`

### WEAK_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### NO_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002687`, median `-0.007917`, mae `0.017928`
- 5d: sample `20`, hit `0.4`, avg `-0.003785`, median `-0.005024`, mae `0.017785`
- 10d: sample `20`, hit `0.65`, avg `0.005152`, median `0.009015`, mae `0.022267`
- 20d: sample `20`, hit `0.6`, avg `0.008499`, median `0.003824`, mae `0.031486`
- 60d: sample `20`, hit `0.85`, avg `0.056195`, median `0.04945`, mae `0.061413`

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.007283`, median `0.011229`, mae `0.017112`
- 5d: sample `40`, hit `0.6`, avg `0.005892`, median `0.011002`, mae `0.019977`
- 10d: sample `40`, hit `0.625`, avg `0.010613`, median `0.011431`, mae `0.024536`
- 20d: sample `40`, hit `0.775`, avg `0.022264`, median `0.028264`, mae `0.033883`
- 60d: sample `40`, hit `0.775`, avg `0.039282`, median `0.054522`, mae `0.056492`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.007954`, median `0.007259`, mae `0.008245`
- 5d: sample `8`, hit `0.5`, avg `0.00142`, median `0.00774`, mae `0.017534`
- 10d: sample `8`, hit `0.625`, avg `-0.005397`, median `0.012215`, mae `0.025972`
- 20d: sample `8`, hit `0.625`, avg `0.009106`, median `0.015404`, mae `0.016554`
- 60d: sample `8`, hit `0.625`, avg `0.00634`, median `0.004698`, mae `0.061732`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.007954`, median `0.007259`, mae `0.008245`
- 5d: sample `8`, hit `0.5`, avg `0.00142`, median `0.00774`, mae `0.017534`
- 10d: sample `8`, hit `0.625`, avg `-0.005397`, median `0.012215`, mae `0.025972`
- 20d: sample `8`, hit `0.625`, avg `0.009106`, median `0.015404`, mae `0.016554`
- 60d: sample `8`, hit `0.625`, avg `0.00634`, median `0.004698`, mae `0.061732`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.004833, 'median_return': 0.006372, 'mean_absolute_return': 0.009393, 'max_adverse_excursion': -0.013293, 'max_favorable_excursion': 0.022499}, '5d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.006585, 'median_return': 0.00774, 'mean_absolute_return': 0.015986, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.006683, 'median_return': 0.012215, 'mean_absolute_return': 0.021938, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.059334}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.015245, 'median_return': 0.015404, 'mean_absolute_return': 0.021905, 'max_adverse_excursion': -0.021537, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.013374, 'median_return': 0.032524, 'mean_absolute_return': 0.054577, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.099148}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.007954, 'median_return': 0.007259, 'mean_absolute_return': 0.008245, 'max_adverse_excursion': -0.001166, 'max_favorable_excursion': 0.020779}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.00142, 'median_return': 0.00774, 'mean_absolute_return': 0.017534, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.03068}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.005397, 'median_return': 0.012215, 'mean_absolute_return': 0.025972, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.023034}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.009106, 'median_return': 0.015404, 'mean_absolute_return': 0.016554, 'max_adverse_excursion': -0.020103, 'max_favorable_excursion': 0.03107}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.00634, 'median_return': 0.004698, 'mean_absolute_return': 0.061732, 'max_adverse_excursion': -0.077263, 'max_favorable_excursion': 0.096597}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.003758, 'median_return': 0.004243, 'mean_absolute_return': 0.016179, 'max_adverse_excursion': -0.035175, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.003893, 'median_return': 0.00381, 'mean_absolute_return': 0.018531, 'max_adverse_excursion': -0.054326, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.009783, 'median_return': 0.009675, 'mean_absolute_return': 0.023025, 'max_adverse_excursion': -0.071498, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.017953, 'median_return': 0.019238, 'mean_absolute_return': 0.031816, 'max_adverse_excursion': -0.064325, 'max_favorable_excursion': 0.093998}, '60d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.040443, 'median_return': 0.040914, 'mean_absolute_return': 0.056745, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.174756}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.525}, '10d': {'sample_size': 80, 'hit_rate': 0.45}, '20d': {'sample_size': 80, 'hit_rate': 0.4}, '60d': {'sample_size': 80, 'hit_rate': 0.3}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.075, 'both_hit': 14, 'both_miss': 6}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.05, 'both_hit': 14, 'both_miss': 6}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.2, 'both_hit': 14, 'both_miss': 6}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.325, 'both_hit': 15, 'both_miss': 5}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': -0.45, 'both_hit': 12, 'both_miss': 8}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.006466, 'median_return': 0.006722, 'mean_absolute_return': 0.014539, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.006123, 'median_return': 0.00971, 'mean_absolute_return': 0.018647, 'max_adverse_excursion': -0.054326, 'max_favorable_excursion': 0.044543}, '10d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.009303, 'median_return': 0.011431, 'mean_absolute_return': 0.02367, 'max_adverse_excursion': -0.071498, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.019924, 'median_return': 0.020066, 'mean_absolute_return': 0.029891, 'max_adverse_excursion': -0.064325, 'max_favorable_excursion': 0.093998}, '60d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.030646, 'median_return': 0.039879, 'mean_absolute_return': 0.055853, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.117712}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.002687, 'median_return': -0.007917, 'mean_absolute_return': 0.017928, 'max_adverse_excursion': -0.035175, 'max_favorable_excursion': 0.038776}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.003785, 'median_return': -0.005024, 'mean_absolute_return': 0.017785, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.005152, 'median_return': 0.009015, 'mean_absolute_return': 0.022267, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.008499, 'median_return': 0.003824, 'mean_absolute_return': 0.031486, 'max_adverse_excursion': -0.055489, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.056195, 'median_return': 0.04945, 'mean_absolute_return': 0.061413, 'max_adverse_excursion': -0.037128, 'max_favorable_excursion': 0.174756}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.006466`, median `0.006722`, mae `0.014539`
- 5d: sample `60`, hit `0.6333`, avg `0.006123`, median `0.00971`, mae `0.018647`
- 10d: sample `60`, hit `0.65`, avg `0.009303`, median `0.011431`, mae `0.02367`
- 20d: sample `60`, hit `0.7667`, avg `0.019924`, median `0.020066`, mae `0.029891`
- 60d: sample `60`, hit `0.7167`, avg `0.030646`, median `0.039879`, mae `0.055853`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.0024`, median `0.002296`, mae `0.017505`
- 5d: sample `40`, hit `0.575`, avg `0.003309`, median `0.004149`, mae `0.019864`
- 10d: sample `40`, hit `0.7`, avg `0.009083`, median `0.011431`, mae `0.025465`
- 20d: sample `40`, hit `0.625`, avg `0.011575`, median `0.006413`, mae `0.032677`
- 60d: sample `40`, hit `0.75`, avg `0.032845`, median `0.029229`, mae `0.049741`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.004833`, median `0.006372`, mae `0.009393`
- 5d: sample `20`, hit `0.7`, avg `0.006585`, median `0.00774`, mae `0.015986`
- 10d: sample `20`, hit `0.7`, avg `0.006683`, median `0.012215`, mae `0.021938`
- 20d: sample `20`, hit `0.75`, avg `0.015245`, median `0.015404`, mae `0.021905`
- 60d: sample `20`, hit `0.6`, avg `0.013374`, median `0.032524`, mae `0.054577`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.005956`, median `0.006372`, mae `0.013267`
- 5d: sample `40`, hit `0.575`, avg `0.003983`, median `0.003714`, mae `0.016999`
- 10d: sample `40`, hit `0.6`, avg `0.007447`, median `0.007467`, mae `0.021174`
- 20d: sample `40`, hit `0.825`, avg `0.022561`, median `0.025541`, mae `0.027902`
- 60d: sample `40`, hit `0.75`, avg `0.041221`, median `0.065295`, mae `0.064746`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.004833`, median `0.006372`, mae `0.009393`
- 5d: sample `20`, hit `0.7`, avg `0.006585`, median `0.00774`, mae `0.015986`
- 10d: sample `20`, hit `0.7`, avg `0.006683`, median `0.012215`, mae `0.021938`
- 20d: sample `20`, hit `0.75`, avg `0.015245`, median `0.015404`, mae `0.021905`
- 60d: sample `20`, hit `0.6`, avg `0.013374`, median `0.032524`, mae `0.054577`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.005956`, median `0.006372`, mae `0.013267`
- 5d: sample `40`, hit `0.575`, avg `0.003983`, median `0.003714`, mae `0.016999`
- 10d: sample `40`, hit `0.6`, avg `0.007447`, median `0.007467`, mae `0.021174`
- 20d: sample `40`, hit `0.825`, avg `0.022561`, median `0.025541`, mae `0.027902`
- 60d: sample `40`, hit `0.75`, avg `0.041221`, median `0.065295`, mae `0.064746`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.0024`, median `0.002296`, mae `0.017505`
- 5d: sample `40`, hit `0.575`, avg `0.003309`, median `0.004149`, mae `0.019864`
- 10d: sample `40`, hit `0.7`, avg `0.009083`, median `0.011431`, mae `0.025465`
- 20d: sample `40`, hit `0.625`, avg `0.011575`, median `0.006413`, mae `0.032677`
- 60d: sample `40`, hit `0.75`, avg `0.032845`, median `0.029229`, mae `0.049741`

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
- 3d: sample `20`, hit `0.7`, avg `0.004833`, median `0.006372`, mae `0.009393`
- 5d: sample `20`, hit `0.7`, avg `0.006585`, median `0.00774`, mae `0.015986`
- 10d: sample `20`, hit `0.7`, avg `0.006683`, median `0.012215`, mae `0.021938`
- 20d: sample `20`, hit `0.75`, avg `0.015245`, median `0.015404`, mae `0.021905`
- 60d: sample `20`, hit `0.6`, avg `0.013374`, median `0.032524`, mae `0.054577`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.004178`, median `0.004569`, mae `0.015386`
- 5d: sample `80`, hit `0.575`, avg `0.003646`, median `0.00381`, mae `0.018431`
- 10d: sample `80`, hit `0.65`, avg `0.008265`, median `0.009675`, mae `0.023319`
- 20d: sample `80`, hit `0.725`, avg `0.017068`, median `0.018139`, mae `0.03029`
- 60d: sample `80`, hit `0.75`, avg `0.037033`, median `0.039879`, mae `0.057243`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.004833`, median `0.006372`, mae `0.009393`
- 5d: sample `20`, hit `0.7`, avg `0.006585`, median `0.00774`, mae `0.015986`
- 10d: sample `20`, hit `0.7`, avg `0.006683`, median `0.012215`, mae `0.021938`
- 20d: sample `20`, hit `0.75`, avg `0.015245`, median `0.015404`, mae `0.021905`
- 60d: sample `20`, hit `0.6`, avg `0.013374`, median `0.032524`, mae `0.054577`

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
- 3d: sample `80`, hit `0.5875`, avg `0.004178`, median `0.004569`, mae `0.015386`
- 5d: sample `80`, hit `0.575`, avg `0.003646`, median `0.00381`, mae `0.018431`
- 10d: sample `80`, hit `0.65`, avg `0.008265`, median `0.009675`, mae `0.023319`
- 20d: sample `80`, hit `0.725`, avg `0.017068`, median `0.018139`, mae `0.03029`
- 60d: sample `80`, hit `0.75`, avg `0.037033`, median `0.039879`, mae `0.057243`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.004833`, median `0.006372`, mae `0.009393`
- 5d: sample `20`, hit `0.7`, avg `0.006585`, median `0.00774`, mae `0.015986`
- 10d: sample `20`, hit `0.7`, avg `0.006683`, median `0.012215`, mae `0.021938`
- 20d: sample `20`, hit `0.75`, avg `0.015245`, median `0.015404`, mae `0.021905`
- 60d: sample `20`, hit `0.6`, avg `0.013374`, median `0.032524`, mae `0.054577`

### risk_path_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.00396`, median `0.004243`, mae `0.017384`
- 5d: sample `60`, hit `0.5333`, avg `0.002666`, median `0.001023`, mae `0.019246`
- 10d: sample `60`, hit `0.6333`, avg `0.008793`, median `0.009015`, mae `0.02378`
- 20d: sample `60`, hit `0.7167`, avg `0.017675`, median `0.019987`, mae `0.033084`
- 60d: sample `60`, hit `0.8`, avg `0.044919`, median `0.04945`, mae `0.058132`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
