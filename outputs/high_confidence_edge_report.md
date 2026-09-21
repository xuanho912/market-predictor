# High Confidence Edge Report

Generated at: `2026-09-21T18:15:54.904592+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `36`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `36`, gate `early_evidence`
- 5d: completed `36`, gate `early_evidence`
- 10d: completed `36`, gate `early_evidence`
- 20d: completed `36`, gate `early_evidence`
- 60d: completed `36`, gate `early_evidence`

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
- 3d: sample `60`, hit `0.4333`, avg `-0.004237`, median `-0.003649`, mae `0.016414`
- 5d: sample `60`, hit `0.4833`, avg `-0.006795`, median `-0.001562`, mae `0.018008`
- 10d: sample `60`, hit `0.3833`, avg `-0.002526`, median `-0.007019`, mae `0.019209`
- 20d: sample `60`, hit `0.6`, avg `0.013906`, median `0.016027`, mae `0.03452`
- 60d: sample `60`, hit `0.7167`, avg `0.03134`, median `0.037425`, mae `0.063438`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.005826`, median `-0.003823`, mae `0.011432`
- 5d: sample `20`, hit `0.15`, avg `-0.015981`, median `-0.012239`, mae `0.020916`
- 10d: sample `20`, hit `0.15`, avg `-0.029747`, median `-0.032485`, mae `0.034125`
- 20d: sample `20`, hit `0.35`, avg `-0.012529`, median `-0.027406`, mae `0.051663`
- 60d: sample `20`, hit `0.65`, avg `0.010433`, median `0.038708`, mae `0.082982`

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
- 3d: sample `8`, hit `0.0`, avg `-0.018856`, median `-0.010094`, mae `0.018856`
- 5d: sample `8`, hit `0.25`, avg `-0.01519`, median `-0.022295`, mae `0.017721`
- 10d: sample `8`, hit `0.0`, avg `-0.015127`, median `-0.015123`, mae `0.015127`
- 20d: sample `8`, hit `0.625`, avg `0.017035`, median `0.029166`, mae `0.040233`
- 60d: sample `8`, hit `0.625`, avg `0.034259`, median `0.072696`, mae `0.086871`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.0`, avg `-0.018856`, median `-0.010094`, mae `0.018856`
- 5d: sample `8`, hit `0.25`, avg `-0.01519`, median `-0.022295`, mae `0.017721`
- 10d: sample `8`, hit `0.0`, avg `-0.015127`, median `-0.015123`, mae `0.015127`
- 20d: sample `8`, hit `0.625`, avg `0.017035`, median `0.029166`, mae `0.040233`
- 60d: sample `8`, hit `0.625`, avg `0.034259`, median `0.072696`, mae `0.086871`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.004237, 'median_return': -0.003649, 'mean_absolute_return': 0.016414, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.006795, 'median_return': -0.001562, 'mean_absolute_return': 0.018008, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.002526, 'median_return': -0.007019, 'mean_absolute_return': 0.019209, 'max_adverse_excursion': -0.060333, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.013906, 'median_return': 0.016027, 'mean_absolute_return': 0.03452, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.03134, 'median_return': 0.037425, 'mean_absolute_return': 0.063438, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.018856, 'median_return': -0.010094, 'mean_absolute_return': 0.018856, 'max_adverse_excursion': -0.033992, 'max_favorable_excursion': -0.001658}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.01519, 'median_return': -0.022295, 'mean_absolute_return': 0.017721, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.015127, 'median_return': -0.015123, 'mean_absolute_return': 0.015127, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.017035, 'median_return': 0.029166, 'mean_absolute_return': 0.040233, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.034259, 'median_return': 0.072696, 'mean_absolute_return': 0.086871, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.003054, 'median_return': -0.001651, 'mean_absolute_return': 0.014759, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.008414, 'median_return': -0.006464, 'mean_absolute_return': 0.018847, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 72, 'hit_rate': 0.3611, 'avg_return': -0.008687, 'median_return': -0.009882, 'mean_absolute_return': 0.023806, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.006215, 'median_return': 0.009364, 'mean_absolute_return': 0.038647, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.025208, 'median_return': 0.032982, 'mean_absolute_return': 0.066263, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.6125}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.05, 'both_hit': 12, 'both_miss': 8}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.075, 'both_hit': 13, 'both_miss': 7}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.05, 'both_hit': 12, 'both_miss': 8}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.15, 'both_hit': 13, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': 0.1, 'both_hit': 16, 'both_miss': 4}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.004237, 'median_return': -0.003649, 'mean_absolute_return': 0.016414, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.006795, 'median_return': -0.001562, 'mean_absolute_return': 0.018008, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.002526, 'median_return': -0.007019, 'mean_absolute_return': 0.019209, 'max_adverse_excursion': -0.060333, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.013906, 'median_return': 0.016027, 'mean_absolute_return': 0.03452, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.03134, 'median_return': 0.037425, 'mean_absolute_return': 0.063438, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.005826, 'median_return': -0.003823, 'mean_absolute_return': 0.011432, 'max_adverse_excursion': -0.029185, 'max_favorable_excursion': 0.020866}, '5d': {'sample_size': 20, 'hit_rate': 0.15, 'avg_return': -0.015981, 'median_return': -0.012239, 'mean_absolute_return': 0.020916, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.022754}, '10d': {'sample_size': 20, 'hit_rate': 0.15, 'avg_return': -0.029747, 'median_return': -0.032485, 'mean_absolute_return': 0.034125, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.023905}, '20d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.012529, 'median_return': -0.027406, 'mean_absolute_return': 0.051663, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.086975}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.010433, 'median_return': 0.038708, 'mean_absolute_return': 0.082982, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.147189}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.00612`, median `-0.007923`, mae `0.014817`
- 5d: sample `20`, hit `0.45`, avg `-0.008182`, median `-0.006464`, mae `0.014597`
- 10d: sample `20`, hit `0.35`, avg `-0.005703`, median `-0.007491`, mae `0.016544`
- 20d: sample `20`, hit `0.6`, avg `0.014509`, median `0.01927`, mae `0.023828`
- 60d: sample `20`, hit `0.75`, avg `0.036506`, median `0.059948`, mae `0.05389`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4`, avg `-0.004634`, median `-0.003676`, mae `0.015168`
- 5d: sample `80`, hit `0.4`, avg `-0.009092`, median `-0.00863`, mae `0.018735`
- 10d: sample `80`, hit `0.325`, avg `-0.009331`, median `-0.01051`, mae `0.022938`
- 20d: sample `80`, hit `0.5375`, avg `0.007297`, median `0.010824`, mae `0.038806`
- 60d: sample `80`, hit `0.7`, avg `0.026113`, median `0.037425`, mae `0.068324`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.00612`, median `-0.007923`, mae `0.014817`
- 5d: sample `20`, hit `0.45`, avg `-0.008182`, median `-0.006464`, mae `0.014597`
- 10d: sample `20`, hit `0.35`, avg `-0.005703`, median `-0.007491`, mae `0.016544`
- 20d: sample `20`, hit `0.6`, avg `0.014509`, median `0.01927`, mae `0.023828`
- 60d: sample `20`, hit `0.75`, avg `0.036506`, median `0.059948`, mae `0.05389`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.004237`, median `-0.003649`, mae `0.016414`
- 5d: sample `60`, hit `0.4833`, avg `-0.006795`, median `-0.001562`, mae `0.018008`
- 10d: sample `60`, hit `0.3833`, avg `-0.002526`, median `-0.007019`, mae `0.019209`
- 20d: sample `60`, hit `0.6`, avg `0.013906`, median `0.016027`, mae `0.03452`
- 60d: sample `60`, hit `0.7167`, avg `0.03134`, median `0.037425`, mae `0.063438`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.013634`, median `-0.010094`, mae `0.020216`
- 5d: sample `20`, hit `0.35`, avg `-0.017453`, median `-0.016421`, mae `0.023096`
- 10d: sample `20`, hit `0.2`, avg `-0.012218`, median `-0.011432`, mae `0.018663`
- 20d: sample `20`, hit `0.55`, avg `0.003755`, median `0.020068`, mae `0.039956`
- 60d: sample `20`, hit `0.6`, avg `0.020763`, median `0.046132`, mae `0.080189`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.00612`, median `-0.007923`, mae `0.014817`
- 5d: sample `20`, hit `0.45`, avg `-0.008182`, median `-0.006464`, mae `0.014597`
- 10d: sample `20`, hit `0.35`, avg `-0.005703`, median `-0.007491`, mae `0.016544`
- 20d: sample `20`, hit `0.6`, avg `0.014509`, median `0.01927`, mae `0.023828`
- 60d: sample `20`, hit `0.75`, avg `0.036506`, median `0.059948`, mae `0.05389`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003296`, median `-0.001658`, mae `0.017212`
- 5d: sample `40`, hit `0.5`, avg `-0.006102`, median `0.000415`, mae `0.019713`
- 10d: sample `40`, hit `0.4`, avg `-0.000938`, median `-0.006017`, mae `0.020541`
- 20d: sample `40`, hit `0.6`, avg `0.013604`, median `0.016027`, mae `0.039866`
- 60d: sample `40`, hit `0.7`, avg `0.028757`, median `0.031273`, mae `0.068211`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.005826`, median `-0.003823`, mae `0.011432`
- 5d: sample `20`, hit `0.15`, avg `-0.015981`, median `-0.012239`, mae `0.020916`
- 10d: sample `20`, hit `0.15`, avg `-0.029747`, median `-0.032485`, mae `0.034125`
- 20d: sample `20`, hit `0.35`, avg `-0.012529`, median `-0.027406`, mae `0.051663`
- 60d: sample `20`, hit `0.65`, avg `0.010433`, median `0.038708`, mae `0.082982`

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
- 3d: sample `80`, hit `0.4`, avg `-0.004634`, median `-0.003676`, mae `0.015168`
- 5d: sample `80`, hit `0.4`, avg `-0.009092`, median `-0.00863`, mae `0.018735`
- 10d: sample `80`, hit `0.325`, avg `-0.009331`, median `-0.01051`, mae `0.022938`
- 20d: sample `80`, hit `0.5375`, avg `0.007297`, median `0.010824`, mae `0.038806`
- 60d: sample `80`, hit `0.7`, avg `0.026113`, median `0.037425`, mae `0.068324`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.004237`, median `-0.003649`, mae `0.016414`
- 5d: sample `60`, hit `0.4833`, avg `-0.006795`, median `-0.001562`, mae `0.018008`
- 10d: sample `60`, hit `0.3833`, avg `-0.002526`, median `-0.007019`, mae `0.019209`
- 20d: sample `60`, hit `0.6`, avg `0.013906`, median `0.016027`, mae `0.03452`
- 60d: sample `60`, hit `0.7167`, avg `0.03134`, median `0.037425`, mae `0.063438`

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
