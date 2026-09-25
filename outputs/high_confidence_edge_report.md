# High Confidence Edge Report

Generated at: `2026-09-25T01:34:22.881954+00:00`

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
- 3d: sample `40`, hit `0.575`, avg `0.00258`, median `0.003898`, mae `0.012089`
- 5d: sample `40`, hit `0.625`, avg `0.002249`, median `0.004651`, mae `0.014766`
- 10d: sample `40`, hit `0.675`, avg `0.006365`, median `0.009775`, mae `0.021409`
- 20d: sample `40`, hit `0.75`, avg `0.019224`, median `0.024743`, mae `0.037094`
- 60d: sample `40`, hit `0.925`, avg `0.060095`, median `0.060702`, mae `0.072763`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.007259`, median `-0.009843`, mae `0.019083`
- 5d: sample `40`, hit `0.425`, avg `-0.008156`, median `-0.00693`, mae `0.022334`
- 10d: sample `40`, hit `0.525`, avg `-0.006195`, median `0.003815`, mae `0.035396`
- 20d: sample `40`, hit `0.6`, avg `0.011181`, median `0.01927`, mae `0.047269`
- 60d: sample `40`, hit `0.825`, avg `0.063898`, median `0.088768`, mae `0.088647`

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
- 3d: sample `8`, hit `0.75`, avg `0.005815`, median `0.012272`, mae `0.014511`
- 5d: sample `8`, hit `0.625`, avg `0.006695`, median `0.009709`, mae `0.016592`
- 10d: sample `8`, hit `0.75`, avg `0.009347`, median `0.013069`, mae `0.017068`
- 20d: sample `8`, hit `0.625`, avg `0.026788`, median `0.043456`, mae `0.034274`
- 60d: sample `8`, hit `1.0`, avg `0.114868`, median `0.119272`, mae `0.114868`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.005815`, median `0.012272`, mae `0.014511`
- 5d: sample `8`, hit `0.625`, avg `0.006695`, median `0.009709`, mae `0.016592`
- 10d: sample `8`, hit `0.75`, avg `0.009347`, median `0.013069`, mae `0.017068`
- 20d: sample `8`, hit `0.625`, avg `0.026788`, median `0.043456`, mae `0.034274`
- 60d: sample `8`, hit `1.0`, avg `0.114868`, median `0.119272`, mae `0.114868`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.00258, 'median_return': 0.003898, 'mean_absolute_return': 0.012089, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.031839}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.002249, 'median_return': 0.004651, 'mean_absolute_return': 0.014766, 'max_adverse_excursion': -0.03581, 'max_favorable_excursion': 0.041233}, '10d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.006365, 'median_return': 0.009775, 'mean_absolute_return': 0.021409, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.019224, 'median_return': 0.024743, 'mean_absolute_return': 0.037094, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.089661}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.060095, 'median_return': 0.060702, 'mean_absolute_return': 0.072763, 'max_adverse_excursion': -0.146095, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005815, 'median_return': 0.012272, 'mean_absolute_return': 0.014511, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006695, 'median_return': 0.009709, 'mean_absolute_return': 0.016592, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.009347, 'median_return': 0.013069, 'mean_absolute_return': 0.017068, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026788, 'median_return': 0.043456, 'mean_absolute_return': 0.034274, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.114868, 'median_return': 0.119272, 'mean_absolute_return': 0.114868, 'max_adverse_excursion': 0.099512, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.003246, 'median_return': -0.001591, 'mean_absolute_return': 0.015706, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.004025, 'median_return': 0.000863, 'mean_absolute_return': 0.018768, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.041233}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': -0.000944, 'median_return': 0.005691, 'mean_absolute_return': 0.029662, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.013915, 'median_return': 0.020886, 'mean_absolute_return': 0.04306, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.8611, 'avg_return': 0.056122, 'median_return': 0.063683, 'mean_absolute_return': 0.076909, 'max_adverse_excursion': -0.177096, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.525}, '20d': {'sample_size': 80, 'hit_rate': 0.475}, '60d': {'sample_size': 80, 'hit_rate': 0.375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.1, 'both_hit': 13, 'both_miss': 7}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': 0.025, 'both_hit': 13, 'both_miss': 7}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.075, 'both_hit': 15, 'both_miss': 5}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.2, 'both_hit': 16, 'both_miss': 4}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.875, 'primary_minus_secondary': -0.5, 'both_hit': 20, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': -0.00234, 'median_return': -0.001058, 'mean_absolute_return': 0.015586, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': -0.002953, 'median_return': 0.000935, 'mean_absolute_return': 0.01855, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.041233}, '10d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 8.5e-05, 'median_return': 0.006604, 'mean_absolute_return': 0.028402, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.015202, 'median_return': 0.020886, 'mean_absolute_return': 0.042182, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.875, 'avg_return': 0.061996, 'median_return': 0.082251, 'mean_absolute_return': 0.080705, 'max_adverse_excursion': -0.177096, 'max_favorable_excursion': 0.154804}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.4875`, avg `-0.00234`, median `-0.001058`, mae `0.015586`
- 5d: sample `80`, hit `0.525`, avg `-0.002953`, median `0.000935`, mae `0.01855`
- 10d: sample `80`, hit `0.6`, avg `8.5e-05`, median `0.006604`, mae `0.028402`
- 20d: sample `80`, hit `0.675`, avg `0.015202`, median `0.020886`, mae `0.042182`
- 60d: sample `80`, hit `0.875`, avg `0.061996`, median `0.082251`, mae `0.080705`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005357`, median `0.009206`, mae `0.014266`
- 5d: sample `20`, hit `0.65`, avg `0.008277`, median `0.010241`, mae `0.018008`
- 10d: sample `20`, hit `0.75`, avg `0.013538`, median `0.020334`, mae `0.023704`
- 20d: sample `20`, hit `0.8`, avg `0.035241`, median `0.03801`, mae `0.03904`
- 60d: sample `20`, hit `1.0`, avg `0.09933`, median `0.109494`, mae `0.09933`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005357`, median `0.009206`, mae `0.014266`
- 5d: sample `20`, hit `0.65`, avg `0.008277`, median `0.010241`, mae `0.018008`
- 10d: sample `20`, hit `0.75`, avg `0.013538`, median `0.020334`, mae `0.023704`
- 20d: sample `20`, hit `0.8`, avg `0.035241`, median `0.03801`, mae `0.03904`
- 60d: sample `20`, hit `1.0`, avg `0.09933`, median `0.109494`, mae `0.09933`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.004905`, median `-0.003649`, mae `0.016026`
- 5d: sample `60`, hit `0.4833`, avg `-0.006697`, median `-0.001562`, mae `0.018731`
- 10d: sample `60`, hit `0.55`, avg `-0.004399`, median `0.005535`, mae `0.029969`
- 20d: sample `60`, hit `0.6333`, avg `0.008522`, median `0.015725`, mae `0.043229`
- 60d: sample `60`, hit `0.8333`, avg `0.049552`, median `0.057507`, mae `0.074497`

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
- 3d: sample `80`, hit `0.4875`, avg `-0.00234`, median `-0.001058`, mae `0.015586`
- 5d: sample `80`, hit `0.525`, avg `-0.002953`, median `0.000935`, mae `0.01855`
- 10d: sample `80`, hit `0.6`, avg `8.5e-05`, median `0.006604`, mae `0.028402`
- 20d: sample `80`, hit `0.675`, avg `0.015202`, median `0.020886`, mae `0.042182`
- 60d: sample `80`, hit `0.875`, avg `0.061996`, median `0.082251`, mae `0.080705`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005357`, median `0.009206`, mae `0.014266`
- 5d: sample `20`, hit `0.65`, avg `0.008277`, median `0.010241`, mae `0.018008`
- 10d: sample `20`, hit `0.75`, avg `0.013538`, median `0.020334`, mae `0.023704`
- 20d: sample `20`, hit `0.8`, avg `0.035241`, median `0.03801`, mae `0.03904`
- 60d: sample `20`, hit `1.0`, avg `0.09933`, median `0.109494`, mae `0.09933`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4875`, avg `-0.00234`, median `-0.001058`, mae `0.015586`
- 5d: sample `80`, hit `0.525`, avg `-0.002953`, median `0.000935`, mae `0.01855`
- 10d: sample `80`, hit `0.6`, avg `8.5e-05`, median `0.006604`, mae `0.028402`
- 20d: sample `80`, hit `0.675`, avg `0.015202`, median `0.020886`, mae `0.042182`
- 60d: sample `80`, hit `0.875`, avg `0.061996`, median `0.082251`, mae `0.080705`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005357`, median `0.009206`, mae `0.014266`
- 5d: sample `20`, hit `0.65`, avg `0.008277`, median `0.010241`, mae `0.018008`
- 10d: sample `20`, hit `0.75`, avg `0.013538`, median `0.020334`, mae `0.023704`
- 20d: sample `20`, hit `0.8`, avg `0.035241`, median `0.03801`, mae `0.03904`
- 60d: sample `20`, hit `1.0`, avg `0.09933`, median `0.109494`, mae `0.09933`

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
