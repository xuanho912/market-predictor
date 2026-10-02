# High Confidence Edge Report

Generated at: `2026-10-02T01:37:23.613088+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `68`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `68`, gate `moderate_evidence`
- 5d: completed `68`, gate `moderate_evidence`
- 10d: completed `68`, gate `moderate_evidence`
- 20d: completed `68`, gate `moderate_evidence`
- 60d: completed `68`, gate `moderate_evidence`

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
- 3d: sample `60`, hit `0.5`, avg `3.2e-05`, median `0.000239`, mae `0.015703`
- 5d: sample `60`, hit `0.4833`, avg `0.000569`, median `-0.001129`, mae `0.017717`
- 10d: sample `60`, hit `0.65`, avg `0.006477`, median `0.008676`, mae `0.020272`
- 20d: sample `60`, hit `0.8333`, avg `0.035835`, median `0.0344`, mae `0.039367`
- 60d: sample `60`, hit `0.9`, avg `0.086536`, median `0.10344`, mae `0.093401`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.004632`, median `-0.002952`, mae `0.017324`
- 5d: sample `20`, hit `0.35`, avg `-0.004042`, median `-0.005632`, mae `0.018384`
- 10d: sample `20`, hit `0.45`, avg `-0.00253`, median `-0.001818`, mae `0.032969`
- 20d: sample `20`, hit `0.5`, avg `0.002391`, median `0.017648`, mae `0.049902`
- 60d: sample `20`, hit `0.95`, avg `0.118903`, median `0.129489`, mae `0.119343`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005815, 'median_return': 0.012272, 'mean_absolute_return': 0.014511, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006695, 'median_return': 0.009709, 'mean_absolute_return': 0.016592, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.009347, 'median_return': 0.013069, 'mean_absolute_return': 0.017068, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026788, 'median_return': 0.043456, 'mean_absolute_return': 0.034274, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.114868, 'median_return': 0.119272, 'mean_absolute_return': 0.114868, 'max_adverse_excursion': 0.099512, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.001906, 'median_return': -0.001591, 'mean_absolute_return': 0.016286, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.001392, 'median_return': -0.004348, 'mean_absolute_return': 0.018027, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.003656, 'median_return': 0.005356, 'mean_absolute_return': 0.024155, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.02755, 'median_return': 0.033704, 'mean_absolute_return': 0.042859, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.9028, 'avg_return': 0.092379, 'median_return': 0.112881, 'mean_absolute_return': 0.098222, 'max_adverse_excursion': -0.078345, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.4}, '20d': {'sample_size': 80, 'hit_rate': 0.25}, '60d': {'sample_size': 80, 'hit_rate': 0.0875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': -0.5, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.0875, 'secondary_hit_rate': 0.9125, 'primary_minus_secondary': -0.825, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.001705, 'median_return': 0.002957, 'mean_absolute_return': 0.012886, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.025934}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.001352, 'median_return': 0.00438, 'mean_absolute_return': 0.015122, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.030717}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.006959, 'median_return': 0.011031, 'mean_absolute_return': 0.019126, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.039009}, '20d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.036092, 'median_return': 0.03801, 'mean_absolute_return': 0.04016, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.092742}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.094175, 'median_return': 0.112881, 'mean_absolute_return': 0.099272, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.156899}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.003974, 'median_return': -0.003676, 'mean_absolute_return': 0.019331, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.00252, 'median_return': -0.005796, 'mean_absolute_return': 0.020646, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.001492, 'median_return': -0.001818, 'mean_absolute_return': 0.027767, 'max_adverse_excursion': -0.053986, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.018856, 'median_return': 0.027885, 'mean_absolute_return': 0.043841, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 40, 'hit_rate': 0.9, 'avg_return': 0.095081, 'median_return': 0.114377, 'mean_absolute_return': 0.1005, 'max_adverse_excursion': -0.078345, 'max_favorable_excursion': 0.192595}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.475`, avg `-0.001134`, median `-0.001227`, mae `0.016108`
- 5d: sample `80`, hit `0.45`, avg `-0.000584`, median `-0.003262`, mae `0.017884`
- 10d: sample `80`, hit `0.6`, avg `0.004225`, median `0.007751`, mae `0.023447`
- 20d: sample `80`, hit `0.75`, avg `0.027474`, median `0.033704`, mae `0.042001`
- 60d: sample `80`, hit `0.9125`, avg `0.094628`, median `0.113428`, mae `0.099886`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002282`, median `0.003757`, mae `0.014244`
- 5d: sample `20`, hit `0.5`, avg `0.002521`, median `0.004597`, mae `0.016682`
- 10d: sample `20`, hit `0.65`, avg `0.007543`, median `0.015799`, mae `0.022392`
- 20d: sample `20`, hit `0.8`, avg `0.036148`, median `0.035951`, mae `0.039946`
- 60d: sample `20`, hit `0.9`, avg `0.091283`, median `0.113428`, mae `0.099395`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.475`, avg `-0.001134`, median `-0.001227`, mae `0.016108`
- 5d: sample `80`, hit `0.45`, avg `-0.000584`, median `-0.003262`, mae `0.017884`
- 10d: sample `80`, hit `0.6`, avg `0.004225`, median `0.007751`, mae `0.023447`
- 20d: sample `80`, hit `0.75`, avg `0.027474`, median `0.033704`, mae `0.042001`
- 60d: sample `80`, hit `0.9125`, avg `0.094628`, median `0.113428`, mae `0.099886`

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
- 3d: sample `80`, hit `0.475`, avg `-0.001134`, median `-0.001227`, mae `0.016108`
- 5d: sample `80`, hit `0.45`, avg `-0.000584`, median `-0.003262`, mae `0.017884`
- 10d: sample `80`, hit `0.6`, avg `0.004225`, median `0.007751`, mae `0.023447`
- 20d: sample `80`, hit `0.75`, avg `0.027474`, median `0.033704`, mae `0.042001`
- 60d: sample `80`, hit `0.9125`, avg `0.094628`, median `0.113428`, mae `0.099886`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.475`, avg `-0.001134`, median `-0.001227`, mae `0.016108`
- 5d: sample `80`, hit `0.45`, avg `-0.000584`, median `-0.003262`, mae `0.017884`
- 10d: sample `80`, hit `0.6`, avg `0.004225`, median `0.007751`, mae `0.023447`
- 20d: sample `80`, hit `0.75`, avg `0.027474`, median `0.033704`, mae `0.042001`
- 60d: sample `80`, hit `0.9125`, avg `0.094628`, median `0.113428`, mae `0.099886`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
