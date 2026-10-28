# High Confidence Edge Report

Generated at: `2026-10-28T18:23:50.109505+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `144`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `144`, gate `stronger_evidence`
- 5d: completed `144`, gate `stronger_evidence`
- 10d: completed `144`, gate `stronger_evidence`
- 20d: completed `144`, gate `stronger_evidence`
- 60d: completed `144`, gate `stronger_evidence`

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
- 3d: sample `60`, hit `0.65`, avg `0.005243`, median `0.005785`, mae `0.012902`
- 5d: sample `60`, hit `0.6333`, avg `0.008275`, median `0.010187`, mae `0.019297`
- 10d: sample `60`, hit `0.7667`, avg `0.015405`, median `0.019466`, mae `0.027521`
- 20d: sample `60`, hit `0.7667`, avg `0.025869`, median `0.028791`, mae `0.033655`
- 60d: sample `60`, hit `0.7333`, avg `0.036147`, median `0.052632`, mae `0.060567`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000162`, median `0.003648`, mae `0.01737`
- 5d: sample `20`, hit `0.5`, avg `0.000536`, median `0.004752`, mae `0.02022`
- 10d: sample `20`, hit `0.6`, avg `0.005691`, median `0.008188`, mae `0.030649`
- 20d: sample `20`, hit `0.6`, avg `0.01363`, median `0.002548`, mae `0.034984`
- 60d: sample `20`, hit `0.7`, avg `0.034032`, median `0.05455`, mae `0.079756`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.005243, 'median_return': 0.005785, 'mean_absolute_return': 0.012902, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.008275, 'median_return': 0.010187, 'mean_absolute_return': 0.019297, 'max_adverse_excursion': -0.036194, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.015405, 'median_return': 0.019466, 'mean_absolute_return': 0.027521, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.025869, 'median_return': 0.028791, 'mean_absolute_return': 0.033655, 'max_adverse_excursion': -0.048763, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.036147, 'median_return': 0.052632, 'mean_absolute_return': 0.060567, 'max_adverse_excursion': -0.154456, 'max_favorable_excursion': 0.139935}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005635, 'median_return': 0.004243, 'mean_absolute_return': 0.016873, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.006385, 'median_return': 0.011002, 'mean_absolute_return': 0.019258, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.015161, 'median_return': 0.020918, 'mean_absolute_return': 0.024249, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.054167}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.033414, 'median_return': 0.031196, 'mean_absolute_return': 0.035796, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.067525, 'median_return': 0.073586, 'mean_absolute_return': 0.067525, 'max_adverse_excursion': 0.025315, 'max_favorable_excursion': 0.101208}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.003698, 'median_return': 0.005726, 'mean_absolute_return': 0.013702, 'max_adverse_excursion': -0.026477, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.006335, 'median_return': 0.009192, 'mean_absolute_return': 0.019557, 'max_adverse_excursion': -0.037279, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.012733, 'median_return': 0.012215, 'mean_absolute_return': 0.028753, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.021631, 'median_return': 0.025541, 'mean_absolute_return': 0.033786, 'max_adverse_excursion': -0.05681, 'max_favorable_excursion': 0.086431}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.032073, 'median_return': 0.045822, 'mean_absolute_return': 0.065124, 'max_adverse_excursion': -0.154456, 'max_favorable_excursion': 0.188184}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6125}, '5d': {'sample_size': 80, 'hit_rate': 0.6}, '10d': {'sample_size': 80, 'hit_rate': 0.675}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 39, 'both_miss': 21}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 38, 'both_miss': 22}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.05, 'both_hit': 46, 'both_miss': 14}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.05, 'both_hit': 46, 'both_miss': 14}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.1, 'both_hit': 44, 'both_miss': 16}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.003817, 'median_return': 0.004886, 'mean_absolute_return': 0.0155, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.006802, 'median_return': 0.00971, 'mean_absolute_return': 0.021241, 'max_adverse_excursion': -0.037279, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.0153, 'median_return': 0.016725, 'mean_absolute_return': 0.030246, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.024308, 'median_return': 0.028791, 'mean_absolute_return': 0.03771, 'max_adverse_excursion': -0.05681, 'max_favorable_excursion': 0.086431}, '60d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.042687, 'median_return': 0.056005, 'mean_absolute_return': 0.071783, 'max_adverse_excursion': -0.154456, 'max_favorable_excursion': 0.188184}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.004116, 'median_return': 0.006274, 'mean_absolute_return': 0.009577, 'max_adverse_excursion': -0.016396, 'max_favorable_excursion': 0.022499}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.004955, 'median_return': 0.006571, 'mean_absolute_return': 0.014385, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.03068}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.006006, 'median_return': 0.009675, 'mean_absolute_return': 0.022474, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.059334}, '20d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.018312, 'median_return': 0.018139, 'mean_absolute_return': 0.022818, 'max_adverse_excursion': -0.020103, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.014412, 'median_return': 0.004698, 'mean_absolute_return': 0.04611, 'max_adverse_excursion': -0.077263, 'max_favorable_excursion': 0.099148}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005243`, median `0.005785`, mae `0.012902`
- 5d: sample `60`, hit `0.6333`, avg `0.008275`, median `0.010187`, mae `0.019297`
- 10d: sample `60`, hit `0.7667`, avg `0.015405`, median `0.019466`, mae `0.027521`
- 20d: sample `60`, hit `0.7667`, avg `0.025869`, median `0.028791`, mae `0.033655`
- 60d: sample `60`, hit `0.7333`, avg `0.036147`, median `0.052632`, mae `0.060567`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000162`, median `0.003648`, mae `0.01737`
- 5d: sample `20`, hit `0.5`, avg `0.000536`, median `0.004752`, mae `0.02022`
- 10d: sample `20`, hit `0.6`, avg `0.005691`, median `0.008188`, mae `0.030649`
- 20d: sample `20`, hit `0.6`, avg `0.01363`, median `0.002548`, mae `0.034984`
- 60d: sample `20`, hit `0.7`, avg `0.034032`, median `0.05455`, mae `0.079756`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005243`, median `0.005785`, mae `0.012902`
- 5d: sample `60`, hit `0.6333`, avg `0.008275`, median `0.010187`, mae `0.019297`
- 10d: sample `60`, hit `0.7667`, avg `0.015405`, median `0.019466`, mae `0.027521`
- 20d: sample `60`, hit `0.7667`, avg `0.025869`, median `0.028791`, mae `0.033655`
- 60d: sample `60`, hit `0.7333`, avg `0.036147`, median `0.052632`, mae `0.060567`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005243`, median `0.005785`, mae `0.012902`
- 5d: sample `60`, hit `0.6333`, avg `0.008275`, median `0.010187`, mae `0.019297`
- 10d: sample `60`, hit `0.7667`, avg `0.015405`, median `0.019466`, mae `0.027521`
- 20d: sample `60`, hit `0.7667`, avg `0.025869`, median `0.028791`, mae `0.033655`
- 60d: sample `60`, hit `0.7333`, avg `0.036147`, median `0.052632`, mae `0.060567`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005243`, median `0.005785`, mae `0.012902`
- 5d: sample `60`, hit `0.6333`, avg `0.008275`, median `0.010187`, mae `0.019297`
- 10d: sample `60`, hit `0.7667`, avg `0.015405`, median `0.019466`, mae `0.027521`
- 20d: sample `60`, hit `0.7667`, avg `0.025869`, median `0.028791`, mae `0.033655`
- 60d: sample `60`, hit `0.7333`, avg `0.036147`, median `0.052632`, mae `0.060567`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005243`, median `0.005785`, mae `0.012902`
- 5d: sample `60`, hit `0.6333`, avg `0.008275`, median `0.010187`, mae `0.019297`
- 10d: sample `60`, hit `0.7667`, avg `0.015405`, median `0.019466`, mae `0.027521`
- 20d: sample `60`, hit `0.7667`, avg `0.025869`, median `0.028791`, mae `0.033655`
- 60d: sample `60`, hit `0.7333`, avg `0.036147`, median `0.052632`, mae `0.060567`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000162`, median `0.003648`, mae `0.01737`
- 5d: sample `20`, hit `0.5`, avg `0.000536`, median `0.004752`, mae `0.02022`
- 10d: sample `20`, hit `0.6`, avg `0.005691`, median `0.008188`, mae `0.030649`
- 20d: sample `20`, hit `0.6`, avg `0.01363`, median `0.002548`, mae `0.034984`
- 60d: sample `20`, hit `0.7`, avg `0.034032`, median `0.05455`, mae `0.079756`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.004116`, median `0.006274`, mae `0.009577`
- 5d: sample `20`, hit `0.65`, avg `0.004955`, median `0.006571`, mae `0.014385`
- 10d: sample `20`, hit `0.7`, avg `0.006006`, median `0.009675`, mae `0.022474`
- 20d: sample `20`, hit `0.8`, avg `0.018312`, median `0.018139`, mae `0.022818`
- 60d: sample `20`, hit `0.6`, avg `0.014412`, median `0.004698`, mae `0.04611`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.005807`, median `0.005785`, mae `0.014565`
- 5d: sample `40`, hit `0.625`, avg `0.009935`, median `0.013109`, mae `0.021752`
- 10d: sample `40`, hit `0.8`, avg `0.020104`, median `0.021778`, mae `0.030044`
- 20d: sample `40`, hit `0.75`, avg `0.029647`, median `0.031658`, mae `0.039073`
- 60d: sample `40`, hit `0.8`, avg `0.047015`, median `0.066636`, mae `0.067796`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.004116`, median `0.006274`, mae `0.009577`
- 5d: sample `20`, hit `0.65`, avg `0.004955`, median `0.006571`, mae `0.014385`
- 10d: sample `20`, hit `0.7`, avg `0.006006`, median `0.009675`, mae `0.022474`
- 20d: sample `20`, hit `0.8`, avg `0.018312`, median `0.018139`, mae `0.022818`
- 60d: sample `20`, hit `0.6`, avg `0.014412`, median `0.004698`, mae `0.04611`

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
- 3d: sample `80`, hit `0.6125`, avg `0.003892`, median `0.004886`, mae `0.014019`
- 5d: sample `80`, hit `0.6`, avg `0.00634`, median `0.009192`, mae `0.019527`
- 10d: sample `80`, hit `0.725`, avg `0.012976`, median `0.012215`, mae `0.028303`
- 20d: sample `80`, hit `0.725`, avg `0.022809`, median `0.028264`, mae `0.033987`
- 60d: sample `80`, hit `0.725`, avg `0.035618`, median `0.052632`, mae `0.065364`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005243`, median `0.005785`, mae `0.012902`
- 5d: sample `60`, hit `0.6333`, avg `0.008275`, median `0.010187`, mae `0.019297`
- 10d: sample `60`, hit `0.7667`, avg `0.015405`, median `0.019466`, mae `0.027521`
- 20d: sample `60`, hit `0.7667`, avg `0.025869`, median `0.028791`, mae `0.033655`
- 60d: sample `60`, hit `0.7333`, avg `0.036147`, median `0.052632`, mae `0.060567`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000162`, median `0.003648`, mae `0.01737`
- 5d: sample `20`, hit `0.5`, avg `0.000536`, median `0.004752`, mae `0.02022`
- 10d: sample `20`, hit `0.6`, avg `0.005691`, median `0.008188`, mae `0.030649`
- 20d: sample `20`, hit `0.6`, avg `0.01363`, median `0.002548`, mae `0.034984`
- 60d: sample `20`, hit `0.7`, avg `0.034032`, median `0.05455`, mae `0.079756`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
