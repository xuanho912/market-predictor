# High Confidence Edge Report

Generated at: `2026-10-28T06:55:29.646866+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `140`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `140`, gate `stronger_evidence`
- 5d: completed `140`, gate `stronger_evidence`
- 10d: completed `140`, gate `stronger_evidence`
- 20d: completed `140`, gate `stronger_evidence`
- 60d: completed `140`, gate `stronger_evidence`

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
- 3d: sample `60`, hit `0.65`, avg `0.006058`, median `0.006274`, mae `0.01358`
- 5d: sample `60`, hit `0.6667`, avg `0.009745`, median `0.011002`, mae `0.01933`
- 10d: sample `60`, hit `0.7333`, avg `0.014975`, median `0.016016`, mae `0.026691`
- 20d: sample `60`, hit `0.7667`, avg `0.022037`, median `0.028626`, mae `0.036563`
- 60d: sample `60`, hit `0.75`, avg `0.032402`, median `0.052632`, mae `0.063904`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.004608`, median `0.007291`, mae `0.018752`
- 5d: sample `20`, hit `0.6`, avg `0.005896`, median `0.009561`, mae `0.022971`
- 10d: sample `20`, hit `0.55`, avg `0.003721`, median `0.008188`, mae `0.029145`
- 20d: sample `20`, hit `0.55`, avg `0.00999`, median `0.001802`, mae `0.034108`
- 60d: sample `20`, hit `0.75`, avg `0.03823`, median `0.033062`, mae `0.0668`

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
- 3d: sample `8`, hit `0.625`, avg `0.005635`, median `0.004243`, mae `0.016873`
- 5d: sample `8`, hit `0.5`, avg `0.006385`, median `0.011002`, mae `0.019258`
- 10d: sample `8`, hit `0.625`, avg `0.015161`, median `0.020918`, mae `0.024249`
- 20d: sample `8`, hit `0.875`, avg `0.033414`, median `0.031196`, mae `0.035796`
- 60d: sample `8`, hit `1.0`, avg `0.067525`, median `0.073586`, mae `0.067525`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.005635`, median `0.004243`, mae `0.016873`
- 5d: sample `8`, hit `0.5`, avg `0.006385`, median `0.011002`, mae `0.019258`
- 10d: sample `8`, hit `0.625`, avg `0.015161`, median `0.020918`, mae `0.024249`
- 20d: sample `8`, hit `0.875`, avg `0.033414`, median `0.031196`, mae `0.035796`
- 60d: sample `8`, hit `1.0`, avg `0.067525`, median `0.073586`, mae `0.067525`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.006058, 'median_return': 0.006274, 'mean_absolute_return': 0.01358, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.033003}, '5d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.009745, 'median_return': 0.011002, 'mean_absolute_return': 0.01933, 'max_adverse_excursion': -0.036194, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.014975, 'median_return': 0.016016, 'mean_absolute_return': 0.026691, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.022037, 'median_return': 0.028626, 'mean_absolute_return': 0.036563, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.032402, 'median_return': 0.052632, 'mean_absolute_return': 0.063904, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.139935}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005635, 'median_return': 0.004243, 'mean_absolute_return': 0.016873, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.006385, 'median_return': 0.011002, 'mean_absolute_return': 0.019258, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.015161, 'median_return': 0.020918, 'mean_absolute_return': 0.024249, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.054167}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.033414, 'median_return': 0.031196, 'mean_absolute_return': 0.035796, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.067525, 'median_return': 0.073586, 'mean_absolute_return': 0.067525, 'max_adverse_excursion': 0.025315, 'max_favorable_excursion': 0.101208}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.005703, 'median_return': 0.006372, 'mean_absolute_return': 0.01465, 'max_adverse_excursion': -0.026477, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.009049, 'median_return': 0.010187, 'mean_absolute_return': 0.02035, 'max_adverse_excursion': -0.037279, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.011828, 'median_return': 0.010559, 'mean_absolute_return': 0.027644, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.017427, 'median_return': 0.024811, 'mean_absolute_return': 0.035967, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.086431}, '60d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.030118, 'median_return': 0.044733, 'mean_absolute_return': 0.064306, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.188184}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6}, '5d': {'sample_size': 80, 'hit_rate': 0.6}, '10d': {'sample_size': 80, 'hit_rate': 0.6625}, '20d': {'sample_size': 80, 'hit_rate': 0.6875}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.025, 'both_hit': 39, 'both_miss': 21}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.05, 'both_hit': 40, 'both_miss': 20}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.025, 'both_hit': 44, 'both_miss': 16}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.025, 'both_hit': 46, 'both_miss': 14}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': -0.125, 'both_hit': 45, 'both_miss': 15}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.006274, 'median_return': 0.007291, 'mean_absolute_return': 0.016509, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.010351, 'median_return': 0.013109, 'mean_absolute_return': 0.022485, 'max_adverse_excursion': -0.037279, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.015417, 'median_return': 0.016725, 'mean_absolute_return': 0.028937, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.020946, 'median_return': 0.028791, 'mean_absolute_return': 0.039728, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.086431}, '60d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.042735, 'median_return': 0.060303, 'mean_absolute_return': 0.070826, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.188184}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.003961, 'median_return': 0.006274, 'mean_absolute_return': 0.009963, 'max_adverse_excursion': -0.016396, 'max_favorable_excursion': 0.022499}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.004077, 'median_return': 0.006571, 'mean_absolute_return': 0.013506, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.03068}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.002393, 'median_return': 0.009031, 'mean_absolute_return': 0.022407, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.059334}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.013263, 'median_return': 0.015404, 'mean_absolute_return': 0.024615, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.007229, 'median_return': 0.004698, 'mean_absolute_return': 0.046035, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.099148}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.006058`, median `0.006274`, mae `0.01358`
- 5d: sample `60`, hit `0.6667`, avg `0.009745`, median `0.011002`, mae `0.01933`
- 10d: sample `60`, hit `0.7333`, avg `0.014975`, median `0.016016`, mae `0.026691`
- 20d: sample `60`, hit `0.7667`, avg `0.022037`, median `0.028626`, mae `0.036563`
- 60d: sample `60`, hit `0.75`, avg `0.032402`, median `0.052632`, mae `0.063904`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.004608`, median `0.007291`, mae `0.018752`
- 5d: sample `20`, hit `0.6`, avg `0.005896`, median `0.009561`, mae `0.022971`
- 10d: sample `20`, hit `0.55`, avg `0.003721`, median `0.008188`, mae `0.029145`
- 20d: sample `20`, hit `0.55`, avg `0.00999`, median `0.001802`, mae `0.034108`
- 60d: sample `20`, hit `0.75`, avg `0.03823`, median `0.033062`, mae `0.0668`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.006058`, median `0.006274`, mae `0.01358`
- 5d: sample `60`, hit `0.6667`, avg `0.009745`, median `0.011002`, mae `0.01933`
- 10d: sample `60`, hit `0.7333`, avg `0.014975`, median `0.016016`, mae `0.026691`
- 20d: sample `60`, hit `0.7667`, avg `0.022037`, median `0.028626`, mae `0.036563`
- 60d: sample `60`, hit `0.75`, avg `0.032402`, median `0.052632`, mae `0.063904`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.007107`, median `0.008854`, mae `0.015388`
- 5d: sample `40`, hit `0.675`, avg `0.012579`, median `0.017768`, mae `0.022242`
- 10d: sample `40`, hit `0.775`, avg `0.021266`, median `0.021778`, mae `0.028833`
- 20d: sample `40`, hit `0.775`, avg `0.026424`, median `0.031658`, mae `0.042538`
- 60d: sample `40`, hit `0.825`, avg `0.044988`, median `0.066636`, mae `0.072839`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.006058`, median `0.006274`, mae `0.01358`
- 5d: sample `60`, hit `0.6667`, avg `0.009745`, median `0.011002`, mae `0.01933`
- 10d: sample `60`, hit `0.7333`, avg `0.014975`, median `0.016016`, mae `0.026691`
- 20d: sample `60`, hit `0.7667`, avg `0.022037`, median `0.028626`, mae `0.036563`
- 60d: sample `60`, hit `0.75`, avg `0.032402`, median `0.052632`, mae `0.063904`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.007107`, median `0.008854`, mae `0.015388`
- 5d: sample `40`, hit `0.675`, avg `0.012579`, median `0.017768`, mae `0.022242`
- 10d: sample `40`, hit `0.775`, avg `0.021266`, median `0.021778`, mae `0.028833`
- 20d: sample `40`, hit `0.775`, avg `0.026424`, median `0.031658`, mae `0.042538`
- 60d: sample `40`, hit `0.825`, avg `0.044988`, median `0.066636`, mae `0.072839`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.004608`, median `0.007291`, mae `0.018752`
- 5d: sample `20`, hit `0.6`, avg `0.005896`, median `0.009561`, mae `0.022971`
- 10d: sample `20`, hit `0.55`, avg `0.003721`, median `0.008188`, mae `0.029145`
- 20d: sample `20`, hit `0.55`, avg `0.00999`, median `0.001802`, mae `0.034108`
- 60d: sample `20`, hit `0.75`, avg `0.03823`, median `0.033062`, mae `0.0668`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.003961`, median `0.006274`, mae `0.009963`
- 5d: sample `20`, hit `0.65`, avg `0.004077`, median `0.006571`, mae `0.013506`
- 10d: sample `20`, hit `0.65`, avg `0.002393`, median `0.009031`, mae `0.022407`
- 20d: sample `20`, hit `0.75`, avg `0.013263`, median `0.015404`, mae `0.024615`
- 60d: sample `20`, hit `0.6`, avg `0.007229`, median `0.004698`, mae `0.046035`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.007107`, median `0.008854`, mae `0.015388`
- 5d: sample `40`, hit `0.675`, avg `0.012579`, median `0.017768`, mae `0.022242`
- 10d: sample `40`, hit `0.775`, avg `0.021266`, median `0.021778`, mae `0.028833`
- 20d: sample `40`, hit `0.775`, avg `0.026424`, median `0.031658`, mae `0.042538`
- 60d: sample `40`, hit `0.825`, avg `0.044988`, median `0.066636`, mae `0.072839`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.004608`, median `0.007291`, mae `0.018752`
- 5d: sample `20`, hit `0.6`, avg `0.005896`, median `0.009561`, mae `0.022971`
- 10d: sample `20`, hit `0.55`, avg `0.003721`, median `0.008188`, mae `0.029145`
- 20d: sample `20`, hit `0.55`, avg `0.00999`, median `0.001802`, mae `0.034108`
- 60d: sample `20`, hit `0.75`, avg `0.03823`, median `0.033062`, mae `0.0668`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.003961`, median `0.006274`, mae `0.009963`
- 5d: sample `20`, hit `0.65`, avg `0.004077`, median `0.006571`, mae `0.013506`
- 10d: sample `20`, hit `0.65`, avg `0.002393`, median `0.009031`, mae `0.022407`
- 20d: sample `20`, hit `0.75`, avg `0.013263`, median `0.015404`, mae `0.024615`
- 60d: sample `20`, hit `0.6`, avg `0.007229`, median `0.004698`, mae `0.046035`

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
- 3d: sample `80`, hit `0.625`, avg `0.005696`, median `0.006274`, mae `0.014873`
- 5d: sample `80`, hit `0.65`, avg `0.008783`, median `0.010187`, mae `0.02024`
- 10d: sample `80`, hit `0.6875`, avg `0.012161`, median `0.010559`, mae `0.027305`
- 20d: sample `80`, hit `0.7125`, avg `0.019025`, median `0.026531`, mae `0.035949`
- 60d: sample `80`, hit `0.75`, avg `0.033859`, median `0.049084`, mae `0.064628`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.006058`, median `0.006274`, mae `0.01358`
- 5d: sample `60`, hit `0.6667`, avg `0.009745`, median `0.011002`, mae `0.01933`
- 10d: sample `60`, hit `0.7333`, avg `0.014975`, median `0.016016`, mae `0.026691`
- 20d: sample `60`, hit `0.7667`, avg `0.022037`, median `0.028626`, mae `0.036563`
- 60d: sample `60`, hit `0.75`, avg `0.032402`, median `0.052632`, mae `0.063904`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.004608`, median `0.007291`, mae `0.018752`
- 5d: sample `20`, hit `0.6`, avg `0.005896`, median `0.009561`, mae `0.022971`
- 10d: sample `20`, hit `0.55`, avg `0.003721`, median `0.008188`, mae `0.029145`
- 20d: sample `20`, hit `0.55`, avg `0.00999`, median `0.001802`, mae `0.034108`
- 60d: sample `20`, hit `0.75`, avg `0.03823`, median `0.033062`, mae `0.0668`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
