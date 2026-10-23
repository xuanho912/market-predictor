# High Confidence Edge Report

Generated at: `2026-10-23T01:16:45.162090+00:00`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001857`, median `0.005136`, mae `0.012766`
- 5d: sample `20`, hit `0.5`, avg `-2e-05`, median `0.006712`, mae `0.020356`
- 10d: sample `20`, hit `0.4`, avg `-0.011059`, median `-0.029809`, mae `0.035942`
- 20d: sample `20`, hit `0.4`, avg `-0.012072`, median `-0.021765`, mae `0.037542`
- 60d: sample `20`, hit `0.7`, avg `0.036782`, median `0.047238`, mae `0.053663`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.002403`, median `0.008574`, mae `0.022329`
- 5d: sample `60`, hit `0.5667`, avg `0.000829`, median `0.005387`, mae `0.02754`
- 10d: sample `60`, hit `0.55`, avg `0.00152`, median `0.009015`, mae `0.041321`
- 20d: sample `60`, hit `0.5167`, avg `-0.004539`, median `0.003343`, mae `0.042244`
- 60d: sample `60`, hit `0.8667`, avg `0.074531`, median `0.077579`, mae `0.084934`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.004536`, median `0.017631`, mae `0.01986`
- 5d: sample `8`, hit `0.625`, avg `0.003249`, median `0.002812`, mae `0.027528`
- 10d: sample `8`, hit `0.5`, avg `0.002268`, median `0.036012`, mae `0.043349`
- 20d: sample `8`, hit `0.5`, avg `-0.004281`, median `0.02284`, mae `0.038002`
- 60d: sample `8`, hit `0.875`, avg `0.052016`, median `0.069082`, mae `0.054554`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.004536`, median `0.017631`, mae `0.01986`
- 5d: sample `8`, hit `0.625`, avg `0.003249`, median `0.002812`, mae `0.027528`
- 10d: sample `8`, hit `0.5`, avg `0.002268`, median `0.036012`, mae `0.043349`
- 20d: sample `8`, hit `0.5`, avg `-0.004281`, median `0.02284`, mae `0.038002`
- 60d: sample `8`, hit `0.875`, avg `0.052016`, median `0.069082`, mae `0.054554`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004536, 'median_return': 0.017631, 'mean_absolute_return': 0.01986, 'max_adverse_excursion': -0.026722, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003249, 'median_return': 0.002812, 'mean_absolute_return': 0.027528, 'max_adverse_excursion': -0.039725, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002268, 'median_return': 0.036012, 'mean_absolute_return': 0.043349, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004281, 'median_return': 0.02284, 'mean_absolute_return': 0.038002, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.057759}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.052016, 'median_return': 0.069082, 'mean_absolute_return': 0.054554, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.090399}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.002015, 'median_return': 0.007291, 'mean_absolute_return': 0.019947, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.000325, 'median_return': 0.006018, 'mean_absolute_return': 0.025546, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.059395}, '10d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.002058, 'median_return': 0.001411, 'mean_absolute_return': 0.039601, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.00666, 'median_return': -0.002558, 'mean_absolute_return': 0.041409, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.066547, 'median_return': 0.06911, 'mean_absolute_return': 0.079623, 'max_adverse_excursion': -0.057863, 'max_favorable_excursion': 0.188608}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.425}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.5125}, '60d': {'sample_size': 80, 'hit_rate': 0.175}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.175, 'secondary_hit_rate': 0.825, 'primary_minus_secondary': -0.65, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.001857, 'median_return': 0.005136, 'mean_absolute_return': 0.012766, 'max_adverse_excursion': -0.021194, 'max_favorable_excursion': 0.030754}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -2e-05, 'median_return': 0.006712, 'mean_absolute_return': 0.020356, 'max_adverse_excursion': -0.029469, 'max_favorable_excursion': 0.038957}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.011059, 'median_return': -0.029809, 'mean_absolute_return': 0.035942, 'max_adverse_excursion': -0.054516, 'max_favorable_excursion': 0.048125}, '20d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.012072, 'median_return': -0.021765, 'mean_absolute_return': 0.037542, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.036798}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.036782, 'median_return': 0.047238, 'mean_absolute_return': 0.053663, 'max_adverse_excursion': -0.039851, 'max_favorable_excursion': 0.099148}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.002403, 'median_return': 0.008574, 'mean_absolute_return': 0.022329, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.000829, 'median_return': 0.005387, 'mean_absolute_return': 0.02754, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.059395}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.00152, 'median_return': 0.009015, 'mean_absolute_return': 0.041321, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.004539, 'median_return': 0.003343, 'mean_absolute_return': 0.042244, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 60, 'hit_rate': 0.8667, 'avg_return': 0.074531, 'median_return': 0.077579, 'mean_absolute_return': 0.084934, 'max_adverse_excursion': -0.057863, 'max_favorable_excursion': 0.188608}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.003524`, median `0.00745`, mae `0.018411`
- 5d: sample `60`, hit `0.5333`, avg `0.001442`, median `0.002812`, mae `0.023746`
- 10d: sample `60`, hit `0.45`, avg `-0.006299`, median `-0.012607`, mae `0.041779`
- 20d: sample `60`, hit `0.4667`, avg `-0.010876`, median `-0.007733`, mae `0.043672`
- 60d: sample `60`, hit `0.7667`, avg `0.049566`, median `0.059488`, mae `0.065595`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001506`, median `0.007291`, mae `0.02452`
- 5d: sample `20`, hit `0.6`, avg `-0.001858`, median `0.009561`, mae `0.03174`
- 10d: sample `20`, hit `0.7`, avg `0.012395`, median `0.010559`, mae `0.034567`
- 20d: sample `20`, hit `0.55`, avg `0.00694`, median `0.003343`, mae `0.033257`
- 60d: sample `20`, hit `1.0`, avg `0.111679`, median `0.113503`, mae `0.111679`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001506`, median `0.007291`, mae `0.02452`
- 5d: sample `20`, hit `0.6`, avg `-0.001858`, median `0.009561`, mae `0.03174`
- 10d: sample `20`, hit `0.7`, avg `0.012395`, median `0.010559`, mae `0.034567`
- 20d: sample `20`, hit `0.55`, avg `0.00694`, median `0.003343`, mae `0.033257`
- 60d: sample `20`, hit `1.0`, avg `0.111679`, median `0.113503`, mae `0.111679`

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
- 3d: sample `20`, hit `0.55`, avg `0.001857`, median `0.005136`, mae `0.012766`
- 5d: sample `20`, hit `0.5`, avg `-2e-05`, median `0.006712`, mae `0.020356`
- 10d: sample `20`, hit `0.4`, avg `-0.011059`, median `-0.029809`, mae `0.035942`
- 20d: sample `20`, hit `0.4`, avg `-0.012072`, median `-0.021765`, mae `0.037542`
- 60d: sample `20`, hit `0.7`, avg `0.036782`, median `0.047238`, mae `0.053663`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.575`, avg `0.002267`, median `0.007291`, mae `0.019938`
- 5d: sample `80`, hit `0.55`, avg `0.000617`, median `0.005387`, mae `0.025744`
- 10d: sample `80`, hit `0.5125`, avg `-0.001625`, median `0.001411`, mae `0.039976`
- 20d: sample `80`, hit `0.4875`, avg `-0.006422`, median `-0.002558`, mae `0.041068`
- 60d: sample `80`, hit `0.825`, avg `0.065094`, median `0.069082`, mae `0.077116`

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
- 3d: sample `80`, hit `0.575`, avg `0.002267`, median `0.007291`, mae `0.019938`
- 5d: sample `80`, hit `0.55`, avg `0.000617`, median `0.005387`, mae `0.025744`
- 10d: sample `80`, hit `0.5125`, avg `-0.001625`, median `0.001411`, mae `0.039976`
- 20d: sample `80`, hit `0.4875`, avg `-0.006422`, median `-0.002558`, mae `0.041068`
- 60d: sample `80`, hit `0.825`, avg `0.065094`, median `0.069082`, mae `0.077116`

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
- 3d: sample `80`, hit `0.575`, avg `0.002267`, median `0.007291`, mae `0.019938`
- 5d: sample `80`, hit `0.55`, avg `0.000617`, median `0.005387`, mae `0.025744`
- 10d: sample `80`, hit `0.5125`, avg `-0.001625`, median `0.001411`, mae `0.039976`
- 20d: sample `80`, hit `0.4875`, avg `-0.006422`, median `-0.002558`, mae `0.041068`
- 60d: sample `80`, hit `0.825`, avg `0.065094`, median `0.069082`, mae `0.077116`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
