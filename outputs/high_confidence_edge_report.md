# High Confidence Edge Report

Generated at: `2026-10-27T18:04:04.165540+00:00`

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
- 3d: sample `60`, hit `0.6`, avg `0.004571`, median `0.004886`, mae `0.013641`
- 5d: sample `60`, hit `0.6`, avg `0.007391`, median `0.006832`, mae `0.018635`
- 10d: sample `60`, hit `0.6667`, avg `0.011658`, median `0.009373`, mae `0.026105`
- 20d: sample `60`, hit `0.75`, avg `0.019847`, median `0.025541`, mae `0.035263`
- 60d: sample `60`, hit `0.7667`, avg `0.032941`, median `0.049084`, mae `0.0629`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002112`, median `0.006264`, mae `0.017936`
- 5d: sample `20`, hit `0.6`, avg `0.005731`, median `0.009192`, mae `0.01976`
- 10d: sample `20`, hit `0.6`, avg `0.00639`, median `0.009015`, mae `0.025877`
- 20d: sample `20`, hit `0.55`, avg `0.007631`, median `0.001802`, mae `0.033368`
- 60d: sample `20`, hit `0.75`, avg `0.036613`, median `0.033062`, mae `0.068582`

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
- 3d: sample `8`, hit `0.875`, avg `0.010674`, median `0.01711`, mae `0.01175`
- 5d: sample `8`, hit `0.625`, avg `0.008099`, median `0.015228`, mae `0.019632`
- 10d: sample `8`, hit `0.625`, avg `0.001235`, median `0.012215`, mae `0.032603`
- 20d: sample `8`, hit `0.625`, avg `0.016613`, median `0.015404`, mae `0.024061`
- 60d: sample `8`, hit `0.75`, avg `0.017036`, median `0.038268`, mae `0.053807`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.004571, 'median_return': 0.004886, 'mean_absolute_return': 0.013641, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.033003}, '5d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.007391, 'median_return': 0.006832, 'mean_absolute_return': 0.018635, 'max_adverse_excursion': -0.036194, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.011658, 'median_return': 0.009373, 'mean_absolute_return': 0.026105, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.019847, 'median_return': 0.025541, 'mean_absolute_return': 0.035263, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.032941, 'median_return': 0.049084, 'mean_absolute_return': 0.0629, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.139935}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.010674, 'median_return': 0.01711, 'mean_absolute_return': 0.01175, 'max_adverse_excursion': -0.004305, 'max_favorable_excursion': 0.022499}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.008099, 'median_return': 0.015228, 'mean_absolute_return': 0.019632, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.03068}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.001235, 'median_return': 0.012215, 'mean_absolute_return': 0.032603, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.059334}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.016613, 'median_return': 0.015404, 'mean_absolute_return': 0.024061, 'max_adverse_excursion': -0.020103, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.017036, 'median_return': 0.038268, 'mean_absolute_return': 0.053807, 'max_adverse_excursion': -0.077263, 'max_favorable_excursion': 0.099148}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.00321, 'median_return': 0.004391, 'mean_absolute_return': 0.015044, 'max_adverse_excursion': -0.033574, 'max_favorable_excursion': 0.038776}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.006851, 'median_return': 0.006712, 'mean_absolute_return': 0.018837, 'max_adverse_excursion': -0.037279, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.011353, 'median_return': 0.009031, 'mean_absolute_return': 0.02532, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.016813, 'median_return': 0.024811, 'mean_absolute_return': 0.035981, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.035729, 'median_return': 0.049084, 'mean_absolute_return': 0.065488, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.188184}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.6375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.025, 'both_hit': 36, 'both_miss': 24}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.05, 'both_hit': 36, 'both_miss': 24}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.05, 'both_hit': 40, 'both_miss': 20}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.025, 'both_hit': 45, 'both_miss': 15}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.7625, 'primary_minus_secondary': -0.125, 'both_hit': 46, 'both_miss': 14}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.006162, 'median_return': 0.005785, 'mean_absolute_return': 0.015142, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.033003}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.010362, 'median_return': 0.013109, 'mean_absolute_return': 0.021381, 'max_adverse_excursion': -0.036194, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.017928, 'median_return': 0.019956, 'mean_absolute_return': 0.028453, 'max_adverse_excursion': -0.058968, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.023263, 'median_return': 0.031196, 'mean_absolute_return': 0.040913, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.045266, 'median_return': 0.066636, 'mean_absolute_return': 0.072618, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.139935}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.001751, 'median_return': 0.003865, 'mean_absolute_return': 0.014288, 'max_adverse_excursion': -0.033574, 'max_favorable_excursion': 0.038776}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.00359, 'median_return': 0.003714, 'mean_absolute_return': 0.016451, 'max_adverse_excursion': -0.037279, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.002753, 'median_return': 0.007467, 'mean_absolute_return': 0.023643, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.010323, 'median_return': 0.011728, 'mean_absolute_return': 0.028666, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.022453, 'median_return': 0.029982, 'mean_absolute_return': 0.056023, 'max_adverse_excursion': -0.113937, 'max_favorable_excursion': 0.188184}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.004571`, median `0.004886`, mae `0.013641`
- 5d: sample `60`, hit `0.6`, avg `0.007391`, median `0.006832`, mae `0.018635`
- 10d: sample `60`, hit `0.6667`, avg `0.011658`, median `0.009373`, mae `0.026105`
- 20d: sample `60`, hit `0.75`, avg `0.019847`, median `0.025541`, mae `0.035263`
- 60d: sample `60`, hit `0.7667`, avg `0.032941`, median `0.049084`, mae `0.0629`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002112`, median `0.006264`, mae `0.017936`
- 5d: sample `20`, hit `0.6`, avg `0.005731`, median `0.009192`, mae `0.01976`
- 10d: sample `20`, hit `0.6`, avg `0.00639`, median `0.009015`, mae `0.025877`
- 20d: sample `20`, hit `0.55`, avg `0.007631`, median `0.001802`, mae `0.033368`
- 60d: sample `20`, hit `0.75`, avg `0.036613`, median `0.033062`, mae `0.068582`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.004571`, median `0.004886`, mae `0.013641`
- 5d: sample `60`, hit `0.6`, avg `0.007391`, median `0.006832`, mae `0.018635`
- 10d: sample `60`, hit `0.6667`, avg `0.011658`, median `0.009373`, mae `0.026105`
- 20d: sample `60`, hit `0.75`, avg `0.019847`, median `0.025541`, mae `0.035263`
- 60d: sample `60`, hit `0.7667`, avg `0.032941`, median `0.049084`, mae `0.0629`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.004571`, median `0.004886`, mae `0.013641`
- 5d: sample `60`, hit `0.6`, avg `0.007391`, median `0.006832`, mae `0.018635`
- 10d: sample `60`, hit `0.6667`, avg `0.011658`, median `0.009373`, mae `0.026105`
- 20d: sample `60`, hit `0.75`, avg `0.019847`, median `0.025541`, mae `0.035263`
- 60d: sample `60`, hit `0.7667`, avg `0.032941`, median `0.049084`, mae `0.0629`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.004571`, median `0.004886`, mae `0.013641`
- 5d: sample `60`, hit `0.6`, avg `0.007391`, median `0.006832`, mae `0.018635`
- 10d: sample `60`, hit `0.6667`, avg `0.011658`, median `0.009373`, mae `0.026105`
- 20d: sample `60`, hit `0.75`, avg `0.019847`, median `0.025541`, mae `0.035263`
- 60d: sample `60`, hit `0.7667`, avg `0.032941`, median `0.049084`, mae `0.0629`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.004571`, median `0.004886`, mae `0.013641`
- 5d: sample `60`, hit `0.6`, avg `0.007391`, median `0.006832`, mae `0.018635`
- 10d: sample `60`, hit `0.6667`, avg `0.011658`, median `0.009373`, mae `0.026105`
- 20d: sample `60`, hit `0.75`, avg `0.019847`, median `0.025541`, mae `0.035263`
- 60d: sample `60`, hit `0.7667`, avg `0.032941`, median `0.049084`, mae `0.0629`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002112`, median `0.006264`, mae `0.017936`
- 5d: sample `20`, hit `0.6`, avg `0.005731`, median `0.009192`, mae `0.01976`
- 10d: sample `20`, hit `0.6`, avg `0.00639`, median `0.009015`, mae `0.025877`
- 20d: sample `20`, hit `0.55`, avg `0.007631`, median `0.001802`, mae `0.033368`
- 60d: sample `20`, hit `0.75`, avg `0.036613`, median `0.033062`, mae `0.068582`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001391`, median `0.003072`, mae `0.010639`
- 5d: sample `20`, hit `0.55`, avg `0.00145`, median `0.003402`, mae `0.013142`
- 10d: sample `20`, hit `0.55`, avg `-0.000883`, median `0.006378`, mae `0.02141`
- 20d: sample `20`, hit `0.75`, avg `0.013014`, median `0.015404`, mae `0.023963`
- 60d: sample `20`, hit `0.65`, avg `0.008293`, median `0.014662`, mae `0.043464`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.005644`, median `0.004243`, mae `0.016353`
- 5d: sample `20`, hit `0.45`, avg `0.004662`, median `-0.003328`, mae `0.019579`
- 10d: sample `20`, hit `0.6`, avg `0.014596`, median `0.0076`, mae `0.025537`
- 20d: sample `20`, hit `0.9`, avg `0.031208`, median `0.028791`, mae `0.035232`
- 60d: sample `20`, hit `0.9`, avg `0.066753`, median `0.074922`, mae `0.0726`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002112`, median `0.006264`, mae `0.017936`
- 5d: sample `20`, hit `0.6`, avg `0.005731`, median `0.009192`, mae `0.01976`
- 10d: sample `20`, hit `0.6`, avg `0.00639`, median `0.009015`, mae `0.025877`
- 20d: sample `20`, hit `0.55`, avg `0.007631`, median `0.001802`, mae `0.033368`
- 60d: sample `20`, hit `0.75`, avg `0.036613`, median `0.033062`, mae `0.068582`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001391`, median `0.003072`, mae `0.010639`
- 5d: sample `20`, hit `0.55`, avg `0.00145`, median `0.003402`, mae `0.013142`
- 10d: sample `20`, hit `0.55`, avg `-0.000883`, median `0.006378`, mae `0.02141`
- 20d: sample `20`, hit `0.75`, avg `0.013014`, median `0.015404`, mae `0.023963`
- 60d: sample `20`, hit `0.65`, avg `0.008293`, median `0.014662`, mae `0.043464`

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
- 3d: sample `80`, hit `0.5875`, avg `0.003957`, median `0.004886`, mae `0.014715`
- 5d: sample `80`, hit `0.6`, avg `0.006976`, median `0.006832`, mae `0.018916`
- 10d: sample `80`, hit `0.65`, avg `0.010341`, median `0.009031`, mae `0.026048`
- 20d: sample `80`, hit `0.7`, avg `0.016793`, median `0.020066`, mae `0.034789`
- 60d: sample `80`, hit `0.7625`, avg `0.033859`, median `0.045822`, mae `0.06432`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.004571`, median `0.004886`, mae `0.013641`
- 5d: sample `60`, hit `0.6`, avg `0.007391`, median `0.006832`, mae `0.018635`
- 10d: sample `60`, hit `0.6667`, avg `0.011658`, median `0.009373`, mae `0.026105`
- 20d: sample `60`, hit `0.75`, avg `0.019847`, median `0.025541`, mae `0.035263`
- 60d: sample `60`, hit `0.7667`, avg `0.032941`, median `0.049084`, mae `0.0629`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002112`, median `0.006264`, mae `0.017936`
- 5d: sample `20`, hit `0.6`, avg `0.005731`, median `0.009192`, mae `0.01976`
- 10d: sample `20`, hit `0.6`, avg `0.00639`, median `0.009015`, mae `0.025877`
- 20d: sample `20`, hit `0.55`, avg `0.007631`, median `0.001802`, mae `0.033368`
- 60d: sample `20`, hit `0.75`, avg `0.036613`, median `0.033062`, mae `0.068582`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
