# High Confidence Edge Report

Generated at: `2026-11-11T01:32:27.773629+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `180`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `180`, gate `stronger_evidence`
- 5d: completed `180`, gate `stronger_evidence`
- 10d: completed `180`, gate `stronger_evidence`
- 20d: completed `180`, gate `stronger_evidence`
- 60d: completed `180`, gate `stronger_evidence`

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
- 3d: sample `20`, hit `0.65`, avg `0.005781`, median `0.010308`, mae `0.01762`
- 5d: sample `20`, hit `0.45`, avg `0.001372`, median `-0.002194`, mae `0.023849`
- 10d: sample `20`, hit `0.5`, avg `-0.007073`, median `0.001411`, mae `0.04396`
- 20d: sample `20`, hit `0.55`, avg `-0.007699`, median `0.009784`, mae `0.049401`
- 60d: sample `20`, hit `0.8`, avg `0.070133`, median `0.103439`, mae `0.086395`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.003566`, median `0.006321`, mae `0.018584`
- 5d: sample `60`, hit `0.5333`, avg `0.001199`, median `0.002574`, mae `0.025695`
- 10d: sample `60`, hit `0.4`, avg `-0.006063`, median `-0.013567`, mae `0.039842`
- 20d: sample `60`, hit `0.35`, avg `-0.017533`, median `-0.02364`, mae `0.044602`
- 60d: sample `60`, hit `0.85`, avg `0.062179`, median `0.060319`, mae `0.068978`

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
- 3d: sample `8`, hit `0.625`, avg `0.002882`, median `0.008833`, mae `0.016375`
- 5d: sample `8`, hit `0.5`, avg `0.005307`, median `0.02186`, mae `0.029342`
- 10d: sample `8`, hit `0.625`, avg `-0.006788`, median `0.021778`, mae `0.052413`
- 20d: sample `8`, hit `0.625`, avg `-0.004139`, median `0.020431`, mae `0.046287`
- 60d: sample `8`, hit `0.75`, avg `0.063584`, median `0.096389`, mae `0.081986`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.002882`, median `0.008833`, mae `0.016375`
- 5d: sample `8`, hit `0.5`, avg `0.005307`, median `0.02186`, mae `0.029342`
- 10d: sample `8`, hit `0.625`, avg `-0.006788`, median `0.021778`, mae `0.052413`
- 20d: sample `8`, hit `0.625`, avg `-0.004139`, median `0.020431`, mae `0.046287`
- 60d: sample `8`, hit `0.75`, avg `0.063584`, median `0.096389`, mae `0.081986`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.005781, 'median_return': 0.010308, 'mean_absolute_return': 0.01762, 'max_adverse_excursion': -0.028791, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': 0.001372, 'median_return': -0.002194, 'mean_absolute_return': 0.023849, 'max_adverse_excursion': -0.041734, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.007073, 'median_return': 0.001411, 'mean_absolute_return': 0.04396, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.067422}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.007699, 'median_return': 0.009784, 'mean_absolute_return': 0.049401, 'max_adverse_excursion': -0.103697, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.070133, 'median_return': 0.103439, 'mean_absolute_return': 0.086395, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.140645}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.002882, 'median_return': 0.008833, 'mean_absolute_return': 0.016375, 'max_adverse_excursion': -0.026477, 'max_favorable_excursion': 0.041595}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.005307, 'median_return': 0.02186, 'mean_absolute_return': 0.029342, 'max_adverse_excursion': -0.034454, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.006788, 'median_return': 0.021778, 'mean_absolute_return': 0.052413, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.067422}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.004139, 'median_return': 0.020431, 'mean_absolute_return': 0.046287, 'max_adverse_excursion': -0.103293, 'max_favorable_excursion': 0.071064}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.063584, 'median_return': 0.096389, 'mean_absolute_return': 0.081986, 'max_adverse_excursion': -0.040542, 'max_favorable_excursion': 0.139575}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.004257, 'median_return': 0.007362, 'mean_absolute_return': 0.018562, 'max_adverse_excursion': -0.058326, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.000791, 'median_return': 0.00246, 'mean_absolute_return': 0.024777, 'max_adverse_excursion': -0.049979, 'max_favorable_excursion': 0.059395}, '10d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.006263, 'median_return': -0.013567, 'mean_absolute_return': 0.039589, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 72, 'hit_rate': 0.375, 'avg_return': -0.01629, 'median_return': -0.023277, 'mean_absolute_return': 0.045748, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 72, 'hit_rate': 0.8472, 'avg_return': 0.064232, 'median_return': 0.065855, 'mean_absolute_return': 0.07237, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.188608}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.4625}, '10d': {'sample_size': 80, 'hit_rate': 0.575}, '20d': {'sample_size': 80, 'hit_rate': 0.625}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_minus_secondary': 0.25, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.004421, 'median_return': 0.010308, 'mean_absolute_return': 0.018928, 'max_adverse_excursion': -0.038555, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.001977, 'median_return': 0.002574, 'mean_absolute_return': 0.024995, 'max_adverse_excursion': -0.041734, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.001383, 'median_return': -0.004602, 'mean_absolute_return': 0.041802, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.008642, 'median_return': 0.004568, 'mean_absolute_return': 0.050186, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.066399, 'median_return': 0.069082, 'mean_absolute_return': 0.075037, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.003819, 'median_return': 0.005136, 'mean_absolute_return': 0.017759, 'max_adverse_excursion': -0.058326, 'max_favorable_excursion': 0.044418}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.000508, 'median_return': 0.00246, 'mean_absolute_return': 0.025472, 'max_adverse_excursion': -0.049979, 'max_favorable_excursion': 0.059395}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.011248, 'median_return': -0.022349, 'mean_absolute_return': 0.039941, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.075219}, '20d': {'sample_size': 40, 'hit_rate': 0.3, 'avg_return': -0.021507, 'median_return': -0.02364, 'mean_absolute_return': 0.041418, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.086095}, '60d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.061936, 'median_return': 0.065855, 'mean_absolute_return': 0.071627, 'max_adverse_excursion': -0.039851, 'max_favorable_excursion': 0.188608}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5667`, avg `0.002731`, median `0.005136`, mae `0.016888`
- 5d: sample `60`, hit `0.4667`, avg `-0.000934`, median `-0.00378`, mae `0.023648`
- 10d: sample `60`, hit `0.4`, avg `-0.008144`, median `-0.013682`, mae `0.040691`
- 20d: sample `60`, hit `0.4`, avg `-0.014419`, median `-0.021765`, mae `0.046575`
- 60d: sample `60`, hit `0.7833`, avg `0.050701`, median `0.057953`, mae `0.06292`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.008287`, median `0.013019`, mae `0.022708`
- 5d: sample `20`, hit `0.65`, avg `0.007773`, median `0.010926`, mae `0.02999`
- 10d: sample `20`, hit `0.5`, avg `-0.00083`, median `0.000466`, mae `0.041415`
- 20d: sample `20`, hit `0.4`, avg `-0.017041`, median `-0.022298`, mae `0.043483`
- 60d: sample `20`, hit `1.0`, avg `0.104567`, median `0.102823`, mae `0.104567`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005781`, median `0.010308`, mae `0.01762`
- 5d: sample `20`, hit `0.45`, avg `0.001372`, median `-0.002194`, mae `0.023849`
- 10d: sample `20`, hit `0.5`, avg `-0.007073`, median `0.001411`, mae `0.04396`
- 20d: sample `20`, hit `0.55`, avg `-0.007699`, median `0.009784`, mae `0.049401`
- 60d: sample `20`, hit `0.8`, avg `0.070133`, median `0.103439`, mae `0.086395`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005781`, median `0.010308`, mae `0.01762`
- 5d: sample `20`, hit `0.45`, avg `0.001372`, median `-0.002194`, mae `0.023849`
- 10d: sample `20`, hit `0.5`, avg `-0.007073`, median `0.001411`, mae `0.04396`
- 20d: sample `20`, hit `0.55`, avg `-0.007699`, median `0.009784`, mae `0.049401`
- 60d: sample `20`, hit `0.8`, avg `0.070133`, median `0.103439`, mae `0.086395`

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
- 3d: sample `20`, hit `0.7`, avg `0.008287`, median `0.013019`, mae `0.022708`
- 5d: sample `20`, hit `0.65`, avg `0.007773`, median `0.010926`, mae `0.02999`
- 10d: sample `20`, hit `0.5`, avg `-0.00083`, median `0.000466`, mae `0.041415`
- 20d: sample `20`, hit `0.4`, avg `-0.017041`, median `-0.022298`, mae `0.043483`
- 60d: sample `20`, hit `1.0`, avg `0.104567`, median `0.102823`, mae `0.104567`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.004421`, median `0.010308`, mae `0.018928`
- 5d: sample `40`, hit `0.525`, avg `0.001977`, median `0.002574`, mae `0.024995`
- 10d: sample `40`, hit `0.475`, avg `-0.001383`, median `-0.004602`, mae `0.041802`
- 20d: sample `40`, hit `0.5`, avg `-0.008642`, median `0.004568`, mae `0.050186`
- 60d: sample `40`, hit `0.875`, avg `0.066399`, median `0.069082`, mae `0.075037`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000649`, median `0.000438`, mae `0.01281`
- 5d: sample `20`, hit `0.35`, avg `-0.006758`, median `-0.009532`, mae `0.020954`
- 10d: sample `20`, hit `0.25`, avg `-0.021666`, median `-0.030112`, mae `0.038468`
- 20d: sample `20`, hit `0.2`, avg `-0.025973`, median `-0.02364`, mae `0.039352`
- 60d: sample `20`, hit `0.6`, avg `0.019305`, median `0.024785`, mae `0.038687`

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
- 3d: sample `80`, hit `0.6`, avg `0.00412`, median `0.007362`, mae `0.018343`
- 5d: sample `80`, hit `0.5125`, avg `0.001242`, median `0.00246`, mae `0.025234`
- 10d: sample `80`, hit `0.425`, avg `-0.006316`, median `-0.012607`, mae `0.040872`
- 20d: sample `80`, hit `0.4`, avg `-0.015075`, median `-0.022298`, mae `0.045802`
- 60d: sample `80`, hit `0.8375`, avg `0.064167`, median `0.066018`, mae `0.073332`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.00412`, median `0.007362`, mae `0.018343`
- 5d: sample `80`, hit `0.5125`, avg `0.001242`, median `0.00246`, mae `0.025234`
- 10d: sample `80`, hit `0.425`, avg `-0.006316`, median `-0.012607`, mae `0.040872`
- 20d: sample `80`, hit `0.4`, avg `-0.015075`, median `-0.022298`, mae `0.045802`
- 60d: sample `80`, hit `0.8375`, avg `0.064167`, median `0.066018`, mae `0.073332`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005781`, median `0.010308`, mae `0.01762`
- 5d: sample `20`, hit `0.45`, avg `0.001372`, median `-0.002194`, mae `0.023849`
- 10d: sample `20`, hit `0.5`, avg `-0.007073`, median `0.001411`, mae `0.04396`
- 20d: sample `20`, hit `0.55`, avg `-0.007699`, median `0.009784`, mae `0.049401`
- 60d: sample `20`, hit `0.8`, avg `0.070133`, median `0.103439`, mae `0.086395`

### bounce_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005781`, median `0.010308`, mae `0.01762`
- 5d: sample `20`, hit `0.45`, avg `0.001372`, median `-0.002194`, mae `0.023849`
- 10d: sample `20`, hit `0.5`, avg `-0.007073`, median `0.001411`, mae `0.04396`
- 20d: sample `20`, hit `0.55`, avg `-0.007699`, median `0.009784`, mae `0.049401`
- 60d: sample `20`, hit `0.8`, avg `0.070133`, median `0.103439`, mae `0.086395`

### risk_path_with_flow_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.00412`, median `0.007362`, mae `0.018343`
- 5d: sample `80`, hit `0.5125`, avg `0.001242`, median `0.00246`, mae `0.025234`
- 10d: sample `80`, hit `0.425`, avg `-0.006316`, median `-0.012607`, mae `0.040872`
- 20d: sample `80`, hit `0.4`, avg `-0.015075`, median `-0.022298`, mae `0.045802`
- 60d: sample `80`, hit `0.8375`, avg `0.064167`, median `0.066018`, mae `0.073332`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
