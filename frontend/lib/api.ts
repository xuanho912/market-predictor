type HorizonForecast = {
  horizon: string;
  up_probability: number;
  down_probability: number;
  sideways_probability: number;
  expected_return: number;
  max_upside_p50: number;
  max_downside_p50: number;
  confidence: number;
};

type TopReason = {
  title: string;
  layer: string;
  direction: string;
  evidence: string;
  contribution: number;
};

type SimilarDay = {
  date: string;
  similarity: number;
  regime: string;
  forward_20d_return: number;
  max_drawdown_20d: number;
};

type RiskSource = {
  source: string;
  score: number;
  contribution: number;
  evidence: string;
};

export type PredictionSnapshot = {
  forecast_timestamp: string;
  symbol: string;
  market_regime: string;
  model_version: string;
  feature_snapshot_version: string;
  horizons: HorizonForecast[];
  pullback_risk_score: number;
  crisis_risk_score: number;
  bounce_probability: number;
  bounce_quality_score: number;
  downside_continuation_probability: number;
  trend_reversal_probability: number;
  dead_cat_bounce_risk: number;
  top_reasons: TopReason[];
  historical_similar_days: SimilarDay[];
  risk_source_breakdown: RiskSource[];
};

export type AlphaV1Status = {
  signal_name: string;
  signal_version: string;
  status: "NO ALPHA" | "RESEARCH ALPHA CANDIDATE" | "FORWARD-VALIDATED ALPHA CANDIDATE";
  live_signal: boolean;
  threshold: number;
  latest_checked_date: string | null;
  latest_bounce_probability_by_symbol: Record<string, number | null>;
  distance_to_threshold_by_symbol: Record<string, number | null>;
  expected_validation_horizons: string[];
  risk_note: string;
  data_source_status?: string | null;
  signal_blocked_reason?: string | null;
  no_signal: string | null;
  validation_period: string;
};

const fallbackPrediction: PredictionSnapshot = {
  forecast_timestamp: new Date().toISOString(),
  symbol: "SPY",
  market_regime: "unknown",
  model_version: "frontend-fallback",
  feature_snapshot_version: "frontend-fallback",
  horizons: ["1d", "3d", "5d", "10d", "20d", "60d"].map((horizon) => ({
    horizon,
    up_probability: 0,
    down_probability: 0,
    sideways_probability: 1,
    expected_return: 0,
    max_upside_p50: 0,
    max_downside_p50: 0,
    confidence: 0,
  })),
  pullback_risk_score: 0,
  crisis_risk_score: 0,
  bounce_probability: 0,
  bounce_quality_score: 0,
  downside_continuation_probability: 0,
  trend_reversal_probability: 0,
  dead_cat_bounce_risk: 0,
  top_reasons: [],
  historical_similar_days: [],
  risk_source_breakdown: [],
};

const fallbackAlphaV1Status: AlphaV1Status = {
  signal_name: "bounce_probability_top_decile_v1",
  signal_version: "alpha_v1",
  status: "RESEARCH ALPHA CANDIDATE",
  live_signal: false,
  threshold: 0.32534311,
  latest_checked_date: null,
  latest_bounce_probability_by_symbol: {},
  distance_to_threshold_by_symbol: {},
  expected_validation_horizons: ["3d", "5d", "10d", "20d", "60d"],
  risk_note: "Research alpha candidate only. Forward-only observation; not paper trading and not live trading.",
  data_source_status: "unknown",
  signal_blocked_reason: null,
  no_signal: "no live signal",
  validation_period: "forward_only",
};

export async function getLatestPrediction(symbol = "SPY"): Promise<PredictionSnapshot> {
  const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";
  try {
    const response = await fetch(`${baseUrl}/api/prediction/latest?symbol=${symbol}`, {
      next: { revalidate: 60 },
    });
    if (!response.ok) {
      return fallbackPrediction;
    }
    return response.json();
  } catch {
    return fallbackPrediction;
  }
}

export async function getAlphaV1Status(): Promise<AlphaV1Status> {
  const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";
  try {
    const response = await fetch(`${baseUrl}/api/alpha/v1/status`, {
      next: { revalidate: 60 },
    });
    if (!response.ok) {
      return fallbackAlphaV1Status;
    }
    return response.json();
  } catch {
    return fallbackAlphaV1Status;
  }
}
