# High Confidence Edge Report

Generated at: `2026-10-21T01:12:27.764260+00:00`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004233`, median `0.00745`, mae `0.015731`
- 5d: sample `60`, hit `0.6333`, avg `0.005083`, median `0.009561`, mae `0.018828`
- 10d: sample `60`, hit `0.65`, avg `0.008395`, median `0.013648`, mae `0.024212`
- 20d: sample `60`, hit `0.8`, avg `0.023281`, median `0.027885`, mae `0.035354`
- 60d: sample `60`, hit `0.8`, avg `0.064187`, median `0.068712`, mae `0.073673`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001594`, median `-0.00952`, mae `0.022596`
- 5d: sample `20`, hit `0.35`, avg `-0.009289`, median `-0.014463`, mae `0.023036`
- 10d: sample `20`, hit `0.35`, avg `-0.019569`, median `-0.018077`, mae `0.048754`
- 20d: sample `20`, hit `0.55`, avg `0.007908`, median `0.016065`, mae `0.049751`
- 60d: sample `20`, hit `0.85`, avg `0.075036`, median `0.092689`, mae `0.095346`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `1.0`, avg `0.010505`, median `0.011414`, mae `0.010505`
- 5d: sample `8`, hit `1.0`, avg `0.016698`, median `0.015191`, mae `0.016698`
- 10d: sample `8`, hit `0.875`, avg `0.021807`, median `0.023034`, mae `0.021861`
- 20d: sample `8`, hit `1.0`, avg `0.03102`, median `0.032954`, mae `0.03102`
- 60d: sample `8`, hit `1.0`, avg `0.079153`, median `0.087238`, mae `0.079153`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `1.0`, avg `0.010505`, median `0.011414`, mae `0.010505`
- 5d: sample `8`, hit `1.0`, avg `0.016698`, median `0.015191`, mae `0.016698`
- 10d: sample `8`, hit `0.875`, avg `0.021807`, median `0.023034`, mae `0.021861`
- 20d: sample `8`, hit `1.0`, avg `0.03102`, median `0.032954`, mae `0.03102`
- 60d: sample `8`, hit `1.0`, avg `0.079153`, median `0.087238`, mae `0.079153`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.010505, 'median_return': 0.011414, 'mean_absolute_return': 0.010505, 'max_adverse_excursion': 0.004542, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.016698, 'median_return': 0.015191, 'mean_absolute_return': 0.016698, 'max_adverse_excursion': 0.00774, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.021807, 'median_return': 0.023034, 'mean_absolute_return': 0.021861, 'max_adverse_excursion': -0.000214, 'max_favorable_excursion': 0.038121}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.03102, 'median_return': 0.032954, 'mean_absolute_return': 0.03102, 'max_adverse_excursion': 0.019193, 'max_favorable_excursion': 0.04151}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.079153, 'median_return': 0.087238, 'mean_absolute_return': 0.079153, 'max_adverse_excursion': 0.043741, 'max_favorable_excursion': 0.10629}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.001918, 'median_return': 0.004815, 'mean_absolute_return': 0.018219, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.0002, 'median_return': 0.001573, 'mean_absolute_return': 0.020234, 'max_adverse_excursion': -0.04784, 'max_favorable_excursion': 0.046426}, '10d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.000863, 'median_return': 0.003921, 'mean_absolute_return': 0.03129, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.080442}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.018151, 'median_return': 0.023636, 'mean_absolute_return': 0.039835, 'max_adverse_excursion': -0.103293, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.065537, 'median_return': 0.068712, 'mean_absolute_return': 0.079085, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.194911}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4125}, '5d': {'sample_size': 80, 'hit_rate': 0.4375}, '10d': {'sample_size': 80, 'hit_rate': 0.425}, '20d': {'sample_size': 80, 'hit_rate': 0.2625}, '60d': {'sample_size': 80, 'hit_rate': 0.1875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.475, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_minus_secondary': -0.625, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.005601, 'median_return': 0.010897, 'mean_absolute_return': 0.01474, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.00741, 'median_return': 0.011604, 'mean_absolute_return': 0.018442, 'max_adverse_excursion': -0.029469, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.008924, 'median_return': 0.019171, 'mean_absolute_return': 0.027132, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.05207}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.026066, 'median_return': 0.032954, 'mean_absolute_return': 0.041576, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.064625, 'median_return': 0.077143, 'mean_absolute_return': 0.0711, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -4.8e-05, 'median_return': 0.003921, 'mean_absolute_return': 0.020155, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.00443, 'median_return': -0.012276, 'mean_absolute_return': 0.021318, 'max_adverse_excursion': -0.04784, 'max_favorable_excursion': 0.046426}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.006115, 'median_return': 9.9e-05, 'mean_absolute_return': 0.033563, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.080442}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.012809, 'median_return': 0.014918, 'mean_absolute_return': 0.03633, 'max_adverse_excursion': -0.103293, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.069173, 'median_return': 0.0765, 'mean_absolute_return': 0.087083, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.194911}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.005601`, median `0.010897`, mae `0.01474`
- 5d: sample `40`, hit `0.65`, avg `0.00741`, median `0.011604`, mae `0.018442`
- 10d: sample `40`, hit `0.65`, avg `0.008924`, median `0.019171`, mae `0.027132`
- 20d: sample `40`, hit `0.8`, avg `0.026066`, median `0.032954`, mae `0.041576`
- 60d: sample `40`, hit `0.875`, avg `0.064625`, median `0.077143`, mae `0.0711`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-4.8e-05`, median `0.003921`, mae `0.020155`
- 5d: sample `40`, hit `0.475`, avg `-0.00443`, median `-0.012276`, mae `0.021318`
- 10d: sample `40`, hit `0.5`, avg `-0.006115`, median `9.9e-05`, mae `0.033563`
- 20d: sample `40`, hit `0.675`, avg `0.012809`, median `0.014918`, mae `0.03633`
- 60d: sample `40`, hit `0.75`, avg `0.069173`, median `0.0765`, mae `0.087083`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.005601`, median `0.010897`, mae `0.01474`
- 5d: sample `40`, hit `0.65`, avg `0.00741`, median `0.011604`, mae `0.018442`
- 10d: sample `40`, hit `0.65`, avg `0.008924`, median `0.019171`, mae `0.027132`
- 20d: sample `40`, hit `0.8`, avg `0.026066`, median `0.032954`, mae `0.041576`
- 60d: sample `40`, hit `0.875`, avg `0.064625`, median `0.077143`, mae `0.0711`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.005601`, median `0.010897`, mae `0.01474`
- 5d: sample `40`, hit `0.65`, avg `0.00741`, median `0.011604`, mae `0.018442`
- 10d: sample `40`, hit `0.65`, avg `0.008924`, median `0.019171`, mae `0.027132`
- 20d: sample `40`, hit `0.8`, avg `0.026066`, median `0.032954`, mae `0.041576`
- 60d: sample `40`, hit `0.875`, avg `0.064625`, median `0.077143`, mae `0.0711`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-4.8e-05`, median `0.003921`, mae `0.020155`
- 5d: sample `40`, hit `0.475`, avg `-0.00443`, median `-0.012276`, mae `0.021318`
- 10d: sample `40`, hit `0.5`, avg `-0.006115`, median `9.9e-05`, mae `0.033563`
- 20d: sample `40`, hit `0.675`, avg `0.012809`, median `0.014918`, mae `0.03633`
- 60d: sample `40`, hit `0.75`, avg `0.069173`, median `0.0765`, mae `0.087083`

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
- 3d: sample `80`, hit `0.5875`, avg `0.002777`, median `0.006632`, mae `0.017448`
- 5d: sample `80`, hit `0.5625`, avg `0.00149`, median `0.006047`, mae `0.01988`
- 10d: sample `80`, hit `0.575`, avg `0.001404`, median `0.008243`, mae `0.030348`
- 20d: sample `80`, hit `0.7375`, avg `0.019438`, median `0.027488`, mae `0.038953`
- 60d: sample `80`, hit `0.8125`, avg `0.066899`, median `0.0765`, mae `0.079091`

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
- 3d: sample `80`, hit `0.5875`, avg `0.002777`, median `0.006632`, mae `0.017448`
- 5d: sample `80`, hit `0.5625`, avg `0.00149`, median `0.006047`, mae `0.01988`
- 10d: sample `80`, hit `0.575`, avg `0.001404`, median `0.008243`, mae `0.030348`
- 20d: sample `80`, hit `0.7375`, avg `0.019438`, median `0.027488`, mae `0.038953`
- 60d: sample `80`, hit `0.8125`, avg `0.066899`, median `0.0765`, mae `0.079091`

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
- 3d: sample `80`, hit `0.5875`, avg `0.002777`, median `0.006632`, mae `0.017448`
- 5d: sample `80`, hit `0.5625`, avg `0.00149`, median `0.006047`, mae `0.01988`
- 10d: sample `80`, hit `0.575`, avg `0.001404`, median `0.008243`, mae `0.030348`
- 20d: sample `80`, hit `0.7375`, avg `0.019438`, median `0.027488`, mae `0.038953`
- 60d: sample `80`, hit `0.8125`, avg `0.066899`, median `0.0765`, mae `0.079091`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
