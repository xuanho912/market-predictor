# High Confidence Edge Report

Generated at: `2026-10-31T01:18:15.642386+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `152`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `152`, gate `stronger_evidence`
- 5d: completed `152`, gate `stronger_evidence`
- 10d: completed `152`, gate `stronger_evidence`
- 20d: completed `152`, gate `stronger_evidence`
- 60d: completed `152`, gate `stronger_evidence`

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
- 3d: sample `40`, hit `0.55`, avg `0.001211`, median `0.005136`, mae `0.016382`
- 5d: sample `40`, hit `0.45`, avg `-0.00245`, median `-0.00891`, mae `0.023655`
- 10d: sample `40`, hit `0.35`, avg `-0.009894`, median `-0.021242`, mae `0.038732`
- 20d: sample `40`, hit `0.325`, avg `-0.017634`, median `-0.02364`, mae `0.044375`
- 60d: sample `40`, hit `0.775`, avg `0.041132`, median `0.044344`, mae `0.05133`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.00592`, median `0.008833`, mae `0.020882`
- 5d: sample `40`, hit `0.575`, avg `0.003862`, median `0.007168`, mae `0.025565`
- 10d: sample `40`, hit `0.525`, avg `-0.004577`, median `0.001411`, mae `0.043814`
- 20d: sample `40`, hit `0.45`, avg `-0.014135`, median `-0.002799`, mae `0.044417`
- 60d: sample `40`, hit `0.875`, avg `0.086899`, median `0.103439`, mae `0.097923`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.001211, 'median_return': 0.005136, 'mean_absolute_return': 0.016382, 'max_adverse_excursion': -0.038555, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.00245, 'median_return': -0.00891, 'mean_absolute_return': 0.023655, 'max_adverse_excursion': -0.041488, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.009894, 'median_return': -0.021242, 'mean_absolute_return': 0.038732, 'max_adverse_excursion': -0.104082, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.017634, 'median_return': -0.02364, 'mean_absolute_return': 0.044375, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.041132, 'median_return': 0.044344, 'mean_absolute_return': 0.05133, 'max_adverse_excursion': -0.039851, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004536, 'median_return': 0.017631, 'mean_absolute_return': 0.01986, 'max_adverse_excursion': -0.026722, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003249, 'median_return': 0.002812, 'mean_absolute_return': 0.027528, 'max_adverse_excursion': -0.039725, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002268, 'median_return': 0.036012, 'mean_absolute_return': 0.043349, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004281, 'median_return': 0.02284, 'mean_absolute_return': 0.038002, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.057759}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.052016, 'median_return': 0.069082, 'mean_absolute_return': 0.054554, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.090399}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.003458, 'median_return': 0.007101, 'mean_absolute_return': 0.018495, 'max_adverse_excursion': -0.058326, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.000423, 'median_return': 0.00246, 'mean_absolute_return': 0.024286, 'max_adverse_excursion': -0.049979, 'max_favorable_excursion': 0.059395}, '10d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.008291, 'median_return': -0.012607, 'mean_absolute_return': 0.041042, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 72, 'hit_rate': 0.375, 'avg_return': -0.017174, 'median_return': -0.021765, 'mean_absolute_return': 0.045106, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.086095}, '60d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.065349, 'median_return': 0.065855, 'mean_absolute_return': 0.076857, 'max_adverse_excursion': -0.057863, 'max_favorable_excursion': 0.188608}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.45}, '5d': {'sample_size': 80, 'hit_rate': 0.4375}, '10d': {'sample_size': 80, 'hit_rate': 0.4125}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.45}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.00315, 'median_return': 0.006321, 'mean_absolute_return': 0.017394, 'max_adverse_excursion': -0.038555, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.000253, 'median_return': -0.00378, 'mean_absolute_return': 0.024213, 'max_adverse_excursion': -0.041734, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.01018, 'median_return': -0.020732, 'mean_absolute_return': 0.041502, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.017365, 'median_return': -0.023277, 'mean_absolute_return': 0.044567, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.047971, 'median_return': 0.052669, 'mean_absolute_return': 0.062119, 'max_adverse_excursion': -0.057863, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.004812, 'median_return': 0.007362, 'mean_absolute_return': 0.022345, 'max_adverse_excursion': -0.058326, 'max_favorable_excursion': 0.044418}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.003584, 'median_return': 0.007257, 'mean_absolute_return': 0.025801, 'max_adverse_excursion': -0.049979, 'max_favorable_excursion': 0.059395}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.001598, 'median_return': 0.009015, 'mean_absolute_return': 0.040586, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.075219}, '20d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.011445, 'median_return': -0.017316, 'mean_absolute_return': 0.043882, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.086095}, '60d': {'sample_size': 20, 'hit_rate': 1.0, 'avg_return': 0.112149, 'median_return': 0.113726, 'mean_absolute_return': 0.112149, 'max_adverse_excursion': 0.01793, 'max_favorable_excursion': 0.188608}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.00315`, median `0.006321`, mae `0.017394`
- 5d: sample `60`, hit `0.4667`, avg `-0.000253`, median `-0.00378`, mae `0.024213`
- 10d: sample `60`, hit `0.3833`, avg `-0.01018`, median `-0.020732`, mae `0.041502`
- 20d: sample `60`, hit `0.3833`, avg `-0.017365`, median `-0.023277`, mae `0.044567`
- 60d: sample `60`, hit `0.7667`, avg `0.047971`, median `0.052669`, mae `0.062119`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.004812`, median `0.007362`, mae `0.022345`
- 5d: sample `20`, hit `0.65`, avg `0.003584`, median `0.007257`, mae `0.025801`
- 10d: sample `20`, hit `0.6`, avg `0.001598`, median `0.009015`, mae `0.040586`
- 20d: sample `20`, hit `0.4`, avg `-0.011445`, median `-0.017316`, mae `0.043882`
- 60d: sample `20`, hit `1.0`, avg `0.112149`, median `0.113726`, mae `0.112149`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001211`, median `0.005136`, mae `0.016382`
- 5d: sample `40`, hit `0.45`, avg `-0.00245`, median `-0.00891`, mae `0.023655`
- 10d: sample `40`, hit `0.35`, avg `-0.009894`, median `-0.021242`, mae `0.038732`
- 20d: sample `40`, hit `0.325`, avg `-0.017634`, median `-0.02364`, mae `0.044375`
- 60d: sample `40`, hit `0.775`, avg `0.041132`, median `0.044344`, mae `0.05133`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001211`, median `0.005136`, mae `0.016382`
- 5d: sample `40`, hit `0.45`, avg `-0.00245`, median `-0.00891`, mae `0.023655`
- 10d: sample `40`, hit `0.35`, avg `-0.009894`, median `-0.021242`, mae `0.038732`
- 20d: sample `40`, hit `0.325`, avg `-0.017634`, median `-0.02364`, mae `0.044375`
- 60d: sample `40`, hit `0.775`, avg `0.041132`, median `0.044344`, mae `0.05133`

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
- 3d: sample `20`, hit `0.65`, avg `0.004812`, median `0.007362`, mae `0.022345`
- 5d: sample `20`, hit `0.65`, avg `0.003584`, median `0.007257`, mae `0.025801`
- 10d: sample `20`, hit `0.6`, avg `0.001598`, median `0.009015`, mae `0.040586`
- 20d: sample `20`, hit `0.4`, avg `-0.011445`, median `-0.017316`, mae `0.043882`
- 60d: sample `20`, hit `1.0`, avg `0.112149`, median `0.113726`, mae `0.112149`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001211`, median `0.005136`, mae `0.016382`
- 5d: sample `40`, hit `0.45`, avg `-0.00245`, median `-0.00891`, mae `0.023655`
- 10d: sample `40`, hit `0.35`, avg `-0.009894`, median `-0.021242`, mae `0.038732`
- 20d: sample `40`, hit `0.325`, avg `-0.017634`, median `-0.02364`, mae `0.044375`
- 60d: sample `40`, hit `0.775`, avg `0.041132`, median `0.044344`, mae `0.05133`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.007027`, median `0.010308`, mae `0.019418`
- 5d: sample `20`, hit `0.5`, avg `0.004141`, median `0.007168`, mae `0.025329`
- 10d: sample `20`, hit `0.45`, avg `-0.010752`, median `-0.008597`, mae `0.047041`
- 20d: sample `20`, hit `0.5`, avg `-0.016826`, median `0.004568`, mae `0.044952`
- 60d: sample `20`, hit `0.75`, avg `0.061649`, median `0.096389`, mae `0.083697`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001211`, median `0.005136`, mae `0.016382`
- 5d: sample `40`, hit `0.45`, avg `-0.00245`, median `-0.00891`, mae `0.023655`
- 10d: sample `40`, hit `0.35`, avg `-0.009894`, median `-0.021242`, mae `0.038732`
- 20d: sample `40`, hit `0.325`, avg `-0.017634`, median `-0.02364`, mae `0.044375`
- 60d: sample `40`, hit `0.775`, avg `0.041132`, median `0.044344`, mae `0.05133`

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
- 3d: sample `60`, hit `0.6333`, avg `0.005134`, median `0.008833`, mae `0.020736`
- 5d: sample `60`, hit `0.5667`, avg `0.003075`, median `0.003699`, mae `0.02571`
- 10d: sample `60`, hit `0.5`, avg `-0.001912`, median `0.000466`, mae `0.042721`
- 20d: sample `60`, hit `0.4667`, avg `-0.01146`, median `-0.002799`, mae `0.046114`
- 60d: sample `60`, hit `0.9`, avg `0.079646`, median `0.090399`, mae `0.087334`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.003566`, median `0.007101`, mae `0.018632`
- 5d: sample `80`, hit `0.5125`, avg `0.000706`, median `0.00246`, mae `0.02461`
- 10d: sample `80`, hit `0.4375`, avg `-0.007235`, median `-0.012607`, mae `0.041273`
- 20d: sample `80`, hit `0.3875`, avg `-0.015885`, median `-0.021765`, mae `0.044396`
- 60d: sample `80`, hit `0.825`, avg `0.064015`, median `0.065855`, mae `0.074627`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.003563`, median `0.012255`, mae `0.020444`
- 5d: sample `20`, hit `0.55`, avg `0.001501`, median `0.002574`, mae `0.026`
- 10d: sample `20`, hit `0.45`, avg `0.003417`, median `-0.004602`, mae `0.040534`
- 20d: sample `20`, hit `0.5`, avg `-0.006109`, median `0.020118`, mae `0.049507`
- 60d: sample `20`, hit `0.95`, avg `0.06514`, median `0.065766`, mae `0.066156`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001211`, median `0.005136`, mae `0.016382`
- 5d: sample `40`, hit `0.45`, avg `-0.00245`, median `-0.00891`, mae `0.023655`
- 10d: sample `40`, hit `0.35`, avg `-0.009894`, median `-0.021242`, mae `0.038732`
- 20d: sample `40`, hit `0.325`, avg `-0.017634`, median `-0.02364`, mae `0.044375`
- 60d: sample `40`, hit `0.775`, avg `0.041132`, median `0.044344`, mae `0.05133`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.00592`, median `0.008833`, mae `0.020882`
- 5d: sample `40`, hit `0.575`, avg `0.003862`, median `0.007168`, mae `0.025565`
- 10d: sample `40`, hit `0.525`, avg `-0.004577`, median `0.001411`, mae `0.043814`
- 20d: sample `40`, hit `0.45`, avg `-0.014135`, median `-0.002799`, mae `0.044417`
- 60d: sample `40`, hit `0.875`, avg `0.086899`, median `0.103439`, mae `0.097923`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
