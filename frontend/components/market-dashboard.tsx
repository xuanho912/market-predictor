"use client";

import { useEffect, useMemo, useState } from "react";
import type { BreadthStatus, DataQualityReport, HistoricalAnalogCase, PredictionDashboard, SimulatedSymbolPaths } from "../lib/api";

const SYMBOL_ORDER = ["SPY", "QQQ", "IWM", "DIA"];
const HORIZON_ORDER = ["3d", "5d", "10d", "20d", "60d"];

const stateText: Record<string, string> = {
  risk_on: "风险偏好",
  risk_off: "风险偏弱",
  oversold_bounce: "超跌反抽",
  failed_bounce_risk: "反抽失败风险",
  downside_continuation: "下跌延续",
  sideways: "震荡观察",
  recovery: "修复中",
  panic: "恐慌压力",
  no_edge: "暂无优势",
};

const supportText: Record<string, string> = {
  supportive: "支持",
  weak_or_conflicting: "偏弱/冲突",
  weak: "偏弱",
  neutral: "中性",
  low_sample: "样本少",
};

const categoryText: Record<string, string> = {
  price: "价格",
  volatility: "波动率",
  credit: "信用",
  rates: "利率",
  liquidity: "流动性",
  breadth: "市场宽度",
  options: "期权",
  macro: "宏观",
  flow: "资金流",
  market_structure: "市场结构",
};

const predictorText: Record<string, string> = {
  bounce_predictor: "反抽",
  downside_continuation_predictor: "继续下跌",
  trend_reversal_predictor: "修复/反转",
  risk_expansion_predictor: "风险扩散",
};

const factorText: Record<string, string> = {
  bounce_probability: "反抽概率",
  failed_bounce_risk: "失败反抽风险",
  signal_agreement: "信号一致性",
  historical_analog_support: "历史相似支持",
  credit_stability: "信用稳定",
  volatility_reversal: "波动率回落",
  breadth_support: "宽度支持",
  news_risk: "新闻风险",
  macro_event_risk: "宏观事件风险",
  rates_pressure: "利率压力",
  data_completeness: "数据完整度",
};

function pct(value: number | null | undefined, digits = 0) {
  if (value == null || Number.isNaN(value)) return "暂无";
  return `${(value * 100).toFixed(digits)}%`;
}

function price(value: number | null | undefined) {
  if (value == null || Number.isNaN(value)) return "暂无";
  return value.toLocaleString("zh-CN", { maximumFractionDigits: 2 });
}

function displayTimestamp(value: string | null | undefined) {
  if (!value) return "暂无";
  const normalized = value
    .replace("T", " ")
    .replace(/\.\d+/, "")
    .replace(/Z$/, "")
    .replace(/\+00:00$/, "")
    .trim();
  return `${normalized} UTC`;
}

function dashboardGeneratedAt(dashboard: PredictionDashboard) {
  return dashboard.data_quality_report?.generated_at
    ?? dashboard.market_intelligence_v3?.generated_at
    ?? dashboard.market_intelligence_v2?.generated_at
    ?? dashboard.as_of
    ?? "";
}

function publicAssetPath(filename: string) {
  const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? "";
  return `${basePath}/${filename}`;
}

function signedPct(value: number | null | undefined, digits = 1) {
  if (value == null || Number.isNaN(value)) return "暂无";
  const formatted = `${(value * 100).toFixed(digits)}%`;
  return value > 0 ? `+${formatted}` : formatted;
}

function stateCn(value: string | undefined) {
  return stateText[value ?? ""] ?? value ?? "未知";
}

function supportCn(value: string | undefined) {
  return supportText[value ?? ""] ?? value ?? "中性";
}

function confidenceCn(value: string | undefined) {
  if (value === "high") return "高";
  if (value === "medium") return "中";
  if (value === "low") return "低";
  return "未知";
}

function statusCn(value: string | undefined) {
  if (value === "available") return "可用";
  if (value === "partial") return "部分可用";
  if (value === "proxy") return "代理可用";
  if (value === "fallback") return "备用/规则";
  if (value === "missing") return "缺失";
  if (value === "stale") return "过期";
  if (value === "rate_limited") return "限速";
  if (value === "not_available") return "未接入";
  return value ?? "未知";
}

function breadthCoverageText(value: string | undefined, isTrue?: boolean, isProxy?: boolean) {
  if (isTrue) return "true";
  if (isProxy || value === "proxy") return "proxy";
  if (value === "available" || value === "partial" || value === "stale") return "true";
  return "missing";
}

function scorePct(value: number | null | undefined) {
  if (value == null || Number.isNaN(value)) return "暂无";
  return `${value.toFixed(0)}/100`;
}

function breadthImpactText(status: BreadthStatus | undefined, data: SimulatedSymbolPaths | undefined) {
  if (!status || !data) return "暂无 breadth 数据。";
  const item = status.universes?.[data.symbol];
  if (!item) return `${data.symbol} 暂无 breadth 数据。`;
  const confirmation = item.scores?.breadth_confirmation_score ?? 0;
  const conflict = item.scores?.breadth_conflict_score ?? 0;
  const above20 = item.metrics?.percent_above_20d;
  const change20 = item.metrics?.percent_above_20d_change_5d;
  const low20 = item.metrics?.new_lows_20d;
  if (confirmation >= 65 && confirmation >= conflict) {
    return `${data.symbol} 当前主路径获得 breadth 支持：20d 上方比例 ${pct(above20)}，5d 宽度变化 ${signedPct(change20)}，20d 新低 ${low20 ?? "暂无"}。`;
  }
  if (conflict >= 55) {
    return `${data.symbol} 当前存在 breadth 冲突：成分股参与不足或新低扩张，反抽更容易切到失败反抽/震荡路径。`;
  }
  return `${data.symbol} breadth 目前偏中性：可以辅助判断，但不足以单独提高主路径置信度。`;
}

function resonanceCn(value: string | undefined) {
  if (value === "aligned") return "内部共振";
  if (value === "mixed") return "部分共振";
  if (value === "surface_only") return "指数表面强";
  if (value === "weak") return "内部未共振";
  return value ?? "未知";
}

function edgeCn(value: string | undefined) {
  if (value === "NO_EDGE") return "无优势";
  if (value === "WEAK_EDGE") return "弱优势";
  if (value === "MODERATE_EDGE") return "中等优势";
  if (value === "STRONG_EDGE") return "强优势";
  if (value === "RISK_WARNING") return "风险预警";
  return value ?? "未知";
}

function agreementCn(value: string | undefined) {
  if (value === "strong") return "强一致";
  if (value === "mixed") return "有冲突";
  if (value === "weak") return "弱一致";
  return value ?? "未知";
}

function confirmationCn(value: string | undefined) {
  if (value === "strong") return "强确认";
  if (value === "mixed") return "混合确认";
  if (value === "weak") return "弱确认";
  return value ?? "未知";
}

function strongestScenario(symbolData: SimulatedSymbolPaths | undefined) {
  if (!symbolData) return "暂无";
  if (symbolData.scenario_ranking?.primary?.label) return symbolData.scenario_ranking.primary.label;
  const cards = [...symbolData.scenario_cards].sort((left, right) => right.probability_weight - left.probability_weight);
  return cards[0]?.name_cn ?? "暂无";
}

function scenarioRankLabel(rank: number | undefined) {
  if (rank === 1) return "最可能";
  if (rank === 2) return "第二可能";
  if (rank === 3) return "风险路径";
  return "";
}

function scenarioRankingFor(data: SimulatedSymbolPaths, scenario: string) {
  const ranking = data.scenario_ranking;
  const items = ranking?.all_scenarios ?? [ranking?.primary, ranking?.secondary, ranking?.tertiary].filter(Boolean);
  const index = items.findIndex((item) => item?.scenario === scenario);
  const item = index >= 0 ? items[index] : undefined;
  return item ? { item, rank: index + 1 } : { item: undefined, rank: undefined };
}

function scenarioProbability(data: SimulatedSymbolPaths, scenario: string) {
  const ranked = scenarioRankingFor(data, scenario).item;
  if (ranked?.probability != null) return ranked.probability;
  const weights = data.scenario_weights ?? {};
  if (scenario === "expected_path") return data.base_path_weight ?? data.path_weight_model?.base_path_weight ?? weights.base_scenario;
  if (scenario === "bounce_path") return data.bounce_path_weight ?? data.path_weight_model?.bounce_path_weight ?? weights.bounce_scenario;
  if (scenario === "bearish_path") return data.bearish_path_weight ?? data.path_weight_model?.bearish_path_weight ?? weights.bearish_scenario;
  if (scenario === "analog_average_path") return data.analog_path_weight ?? data.path_weight_model?.analog_path_weight ?? weights.historical_analog_average;
  return undefined;
}

function scenarioDisplayLabel(data: SimulatedSymbolPaths, scenario: string, fallback: string) {
  const { item, rank } = scenarioRankingFor(data, scenario);
  const rankLabel = scenarioRankLabel(rank);
  const probability = scenarioProbability(data, scenario);
  const label = item?.label ?? fallback;
  return `${label}${rankLabel ? `｜${rankLabel}` : ""}${probability != null ? ` ${pct(probability)}` : ""}`;
}

function scenarioStrokeWidth(data: SimulatedSymbolPaths, scenario: string) {
  const { rank } = scenarioRankingFor(data, scenario);
  if (data.scenario_ranking?.close_call) {
    if (rank === 1 || rank === 2) return 2.8;
    if (rank === 3) return 2.1;
    return 1.8;
  }
  if (rank === 1) return 3.8;
  if (rank === 2) return 2.8;
  if (rank === 3) return 2;
  return 1.6;
}

function scenarioGapText(data: SimulatedSymbolPaths) {
  const gap = data.scenario_ranking?.primary_secondary_gap;
  if (gap == null) return "暂无";
  const level = gap < 0.08 ? "路径分歧" : gap < 0.16 ? "中等优势" : "优势较明显";
  return `${(gap * 100).toFixed(0)} 个百分点，${level}`;
}

function primarySwitchText(data: SimulatedSymbolPaths) {
  return data.scenario_ranking?.primary_to_secondary_switch_conditions?.slice(0, 4).join(" / ") || data.risk_invalidation_conditions.slice(0, 4).join(" / ") || "暂无";
}

function strongestPredictor(data: SimulatedSymbolPaths | undefined) {
  const entries = Object.entries(data?.predictors_v4 ?? data?.predictors ?? {});
  if (!entries.length) return null;
  return entries.sort(([, left], [, right]) => right.probability - left.probability)[0];
}

function strongestPredictorText(data: SimulatedSymbolPaths | undefined) {
  const winner = strongestPredictor(data);
  if (!winner) return "暂无";
  return `${predictorText[winner[0]] ?? winner[0]} ${pct(winner[1].probability)}`;
}

function plainAction(data: SimulatedSymbolPaths) {
  const edge = data.market_edge_status?.market_edge_status;
  const winner = strongestPredictor(data)?.[0];
  if (edge === "NO_EDGE" || edge === "WEAK_EDGE") return "先等，不要强行下结论";
  if (winner === "bounce_predictor") return "重点观察反抽是否延续";
  if (winner === "downside_continuation_predictor") return "防继续下跌，别急着抄底";
  if (winner === "trend_reversal_predictor") return "观察修复能否站稳";
  if (winner === "risk_expansion_predictor") return "先防风险扩散";
  return "观察信号是否继续同向";
}

function plainDecision(data: SimulatedSymbolPaths) {
  const state = stateCn(data.market_state);
  const edge = edgeCn(data.market_edge_status?.market_edge_status);
  const strongest = strongestPredictorText(data);
  const fiveDay = data.prediction_horizons?.["5d"];
  const twentyDay = data.prediction_horizons?.["20d"];
  const fiveText = fiveDay ? `${fiveDay.expected_direction}，区间 ${signedPct(fiveDay.expected_return_range?.[0])} 到 ${signedPct(fiveDay.expected_return_range?.[1])}` : "暂无";
  const twentyText = twentyDay ? `${twentyDay.expected_direction}，区间 ${signedPct(twentyDay.expected_return_range?.[0])} 到 ${signedPct(twentyDay.expected_return_range?.[1])}` : "暂无";
  const action = plainAction(data);
  const primary = data.scenario_ranking?.primary;
  const secondary = data.scenario_ranking?.secondary;
  const scenarioText = primary && secondary
    ? `当前最大概率路径是“${primary.label}”，概率 ${pct(primary.probability)}；第二可能是“${secondary.label}”，概率 ${pct(secondary.probability)}；两者差距 ${scenarioGapText(data)}。如果 ${primarySwitchText(data)}，主路径可能失效并切换到风险路径。`
    : "";
  const confirmation = data.signal_confirmation ? `多源确认 ${data.signal_confirmation.confirmation_score}/100（${confirmationCn(data.signal_confirmation.confirmation_level)}）。` : "";
  const noEdge = data.market_edge_status?.no_edge_note ? `${data.market_edge_status.no_edge_note} ` : "";
  return `${data.symbol} 现在是“${state}”，今天的可用预测优势是“${edge}”。${noEdge}${scenarioText} ${confirmation}最强方向是 ${strongest}。5日看法：${fiveText}；20日看法：${twentyText}。大白话：${action}。这不是确定走势，也不是交易指令。`;
}

function plainSummary(symbolData: SimulatedSymbolPaths | undefined) {
  if (!symbolData) return "当前没有可用数据。";
  if (symbolData.current_integrated_judgment) return symbolData.current_integrated_judgment;
  const state = stateCn(symbolData.market_state);
  const scenario = strongestScenario(symbolData);
  return `${symbolData.symbol} 当前状态偏向“${state}”，最强情景是“${scenario}”。这是概率情景，不是确定预测。`;
}

function svgPath(values: Array<number | null>, minY: number, maxY: number, width: number, height: number, pad: number) {
  const step = (width - pad * 2) / Math.max(values.length - 1, 1);
  const scaleY = (value: number) => height - pad - ((value - minY) / Math.max(maxY - minY, 1)) * (height - pad * 2);
  let path = "";
  values.forEach((value, index) => {
    if (value == null) return;
    const x = pad + index * step;
    const y = scaleY(value);
    path += path ? ` L ${x.toFixed(2)} ${y.toFixed(2)}` : `M ${x.toFixed(2)} ${y.toFixed(2)}`;
  });
  return path;
}

function xForIndex(index: number, total: number, width: number, pad: number) {
  const step = (width - pad * 2) / Math.max(total - 1, 1);
  return pad + index * step;
}

function valueAt(values: Array<number | null>, index: number | null) {
  if (index == null) return null;
  const value = values[index];
  return typeof value === "number" && Number.isFinite(value) ? value : null;
}

function PredictionChart({ data }: { data: SimulatedSymbolPaths }) {
  const [hoverIndex, setHoverIndex] = useState<number | null>(null);
  const width = 760;
  const height = 360;
  const pad = 42;
  const paths = data.paths;
  const allValues = [
    ...paths.historical_price,
    ...paths.expected_path,
    ...paths.bounce_path,
    ...paths.bearish_path,
    ...paths.analog_average_path,
    ...paths.confidence_band_upper,
    ...paths.confidence_band_lower,
  ].filter((value): value is number => typeof value === "number" && Number.isFinite(value));
  const minY = Math.min(...allValues) * 0.985;
  const maxY = Math.max(...allValues) * 1.015;
  const splitX = xForIndex(paths.split_index, paths.dates.length, width, pad);
  const yForPrice = (value: number) => height - pad - ((value - minY) / Math.max(maxY - minY, 1)) * (height - pad * 2);
  const historicalValues = paths.historical_price.filter((value): value is number => value != null);
  const currentPrice = data.current_price ?? historicalValues[historicalValues.length - 1] ?? null;
  const priceTicks = [maxY, (maxY + minY) / 2, minY];
  const chartSeries = [
    { key: "history", label: "历史价格", values: paths.historical_price, color: "#14211f" },
    { key: "expected", scenario: "expected_path", label: scenarioDisplayLabel(data, "expected_path", "综合期望"), values: paths.expected_path, color: "#2563eb" },
    { key: "bounce", scenario: "bounce_path", label: scenarioDisplayLabel(data, "bounce_path", "反抽情景"), values: paths.bounce_path, color: "#0f9f7a" },
    { key: "bearish", scenario: "bearish_path", label: scenarioDisplayLabel(data, "bearish_path", "失败反抽"), values: paths.bearish_path, color: "#dc4a4a" },
    { key: "analog", scenario: "analog_average_path", label: scenarioDisplayLabel(data, "analog_average_path", "历史均值"), values: paths.analog_average_path, color: "#f59e0b" },
    { key: "upper", label: "上沿", values: paths.confidence_band_upper, color: "#64748b" },
    { key: "lower", label: "下沿", values: paths.confidence_band_lower, color: "#64748b" },
  ];
  const hoverRows = (hoverIndex == null
    ? []
    : chartSeries
        .map((item) => ({ ...item, value: valueAt(item.values, hoverIndex) }))
        .filter((item) => item.value != null)) as Array<(typeof chartSeries)[number] & { value: number }>;
  const hoverX = hoverIndex == null ? null : xForIndex(hoverIndex, paths.dates.length, width, pad);
  const hoverPrimary = hoverRows[0]?.value ?? null;
  const hoverY = hoverPrimary == null ? null : yForPrice(hoverPrimary);
  const tooltipWidth = 280;
  const tooltipHeight = Math.max(92, 48 + hoverRows.length * 22);
  const tooltipX = hoverX == null ? 0 : Math.min(Math.max(hoverX + 12, pad), width - pad - tooltipWidth);
  const tooltipY = hoverY == null ? pad : Math.min(Math.max(hoverY - tooltipHeight / 2, pad), height - pad - tooltipHeight);
  const hoverDate = hoverIndex == null ? null : paths.dates[hoverIndex];
  const hoverPhase = hoverIndex == null ? "" : hoverIndex <= paths.split_index ? "历史已发生" : "未来情景模拟";
  const horizonIndexes = [3, 5, 10, 20, 60].map((days) => ({
    days,
    index: Math.min(paths.split_index + days, paths.dates.length - 1),
  }));

  return (
    <section className="mt-5 rounded-lg border border-teal bg-white p-4 shadow-sm">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <p className="text-xs uppercase text-teal">核心图表</p>
          <h2 className="mt-1 text-xl font-semibold">过去走势 + 未来概率路径</h2>
          <p className="mt-1 text-xs text-muted">鼠标放到图中任意一天，可以看到当天价格和各条模拟路径价格。</p>
        </div>
        <p className="text-xs text-muted sm:text-right">竖虚线右侧是概率情景，不是保证会发生的预测。</p>
      </div>
      <ScenarioRankingPanel data={data} />
      <div className="mt-3 overflow-x-auto">
        <svg
          viewBox={`0 0 ${width} ${height}`}
          className="h-[360px] min-w-[720px] w-full"
          onMouseLeave={() => setHoverIndex(null)}
        >
          <rect x="0" y="0" width={width} height={height} rx="8" fill="#ffffff" />
          {priceTicks.map((tick) => (
            <g key={tick}>
              <line x1={pad} x2={width - pad} y1={yForPrice(tick)} y2={yForPrice(tick)} stroke="#e5ece9" />
              <text x={8} y={yForPrice(tick) + 4} fontSize="11" fill="#62706b">{price(tick)}</text>
            </g>
          ))}
          {currentPrice != null ? (
            <g>
              <line x1={pad} x2={width - pad} y1={yForPrice(currentPrice)} y2={yForPrice(currentPrice)} stroke="#0f9f7a" strokeDasharray="2 4" />
              <rect x={width - 94} y={yForPrice(currentPrice) - 13} width="86" height="22" rx="5" fill="#0f9f7a" />
              <text x={width - 51} y={yForPrice(currentPrice) + 3} textAnchor="middle" fontSize="11" fill="#ffffff">现价 {price(currentPrice)}</text>
            </g>
          ) : null}
          <line x1={splitX} x2={splitX} y1={pad} y2={height - pad} stroke="#14211f" strokeDasharray="4 4" />
          {horizonIndexes.map(({ days, index }) => {
            const x = xForIndex(index, paths.dates.length, width, pad);
            return (
              <g key={days}>
                <line x1={x} x2={x} y1={pad} y2={height - pad} stroke="#d6dedb" strokeDasharray="3 6" />
                <text x={x} y={height - 12} textAnchor="middle" fontSize="11" fill="#62706b">{days}日</text>
              </g>
            );
          })}
          <path d={svgPath(paths.confidence_band_upper, minY, maxY, width, height, pad)} fill="none" stroke="#94a3b8" strokeWidth="1.2" strokeDasharray="5 5" />
          <path d={svgPath(paths.confidence_band_lower, minY, maxY, width, height, pad)} fill="none" stroke="#94a3b8" strokeWidth="1.2" strokeDasharray="5 5" />
          <path d={svgPath(paths.historical_price, minY, maxY, width, height, pad)} fill="none" stroke="#14211f" strokeWidth="2.4" />
          <path d={svgPath(paths.expected_path, minY, maxY, width, height, pad)} fill="none" stroke="#2563eb" strokeWidth={scenarioStrokeWidth(data, "expected_path")} />
          <path d={svgPath(paths.bounce_path, minY, maxY, width, height, pad)} fill="none" stroke="#0f9f7a" strokeWidth={scenarioStrokeWidth(data, "bounce_path")} />
          <path d={svgPath(paths.bearish_path, minY, maxY, width, height, pad)} fill="none" stroke="#dc4a4a" strokeWidth={scenarioStrokeWidth(data, "bearish_path")} />
          <path d={svgPath(paths.analog_average_path, minY, maxY, width, height, pad)} fill="none" stroke="#f59e0b" strokeWidth={scenarioStrokeWidth(data, "analog_average_path")} />
          <text x={pad} y={22} fontSize="12" fill="#62706b">历史价格</text>
          <text x={splitX + 10} y={22} fontSize="12" fill="#62706b">模拟未来</text>
          {paths.dates.map((date, index) => {
            const x = xForIndex(index, paths.dates.length, width, pad);
            const step = (width - pad * 2) / Math.max(paths.dates.length - 1, 1);
            const titleRows = chartSeries
              .map((item) => {
                const rowValue = valueAt(item.values, index);
                if (rowValue == null) return null;
                const scenario = "scenario" in item ? item.scenario : undefined;
                const ranked = scenario ? scenarioRankingFor(data, scenario) : { item: undefined, rank: undefined };
                const expectedReturn = currentPrice ? `，预期收益 ${signedPct(rowValue / currentPrice - 1)}` : "";
                const rankText = ranked.rank ? `，排名 ${ranked.rank}` : "";
                const reason = ranked.item?.reason ? `，原因：${ranked.item.reason}` : "";
                return `${item.label}: ${price(rowValue)}${expectedReturn}${rankText}${reason}`;
              })
              .filter(Boolean)
              .join("\n");
            return (
              <rect
                key={`${date}-${index}`}
                x={x - step / 2}
                y={pad}
                width={Math.max(step, 4)}
                height={height - pad * 2}
                fill="transparent"
                onMouseEnter={() => setHoverIndex(index)}
                onMouseMove={() => setHoverIndex(index)}
                onTouchStart={() => setHoverIndex(index)}
              >
                <title>{`${date}\n${index <= paths.split_index ? "历史已发生" : "未来情景模拟"}\n${titleRows}`}</title>
              </rect>
            );
          })}
          {hoverIndex != null && hoverX != null ? (
            <g pointerEvents="none">
              <line x1={hoverX} x2={hoverX} y1={pad} y2={height - pad} stroke="#0f766e" strokeWidth="1.2" strokeDasharray="3 3" />
              {hoverRows.map((item) => (
                <circle key={item.key} cx={hoverX} cy={yForPrice(item.value)} r="3.5" fill={item.color} stroke="#ffffff" strokeWidth="1.5" />
              ))}
              <rect x={tooltipX} y={tooltipY} width={tooltipWidth} height={tooltipHeight} rx="8" fill="#14211f" opacity="0.94" />
              <text x={tooltipX + 12} y={tooltipY + 20} fontSize="12" fontWeight="700" fill="#ffffff">{hoverDate}</text>
              <text x={tooltipX + 12} y={tooltipY + 37} fontSize="11" fill="#cbd5d1">{hoverPhase}</text>
              {hoverRows.map((item, rowIndex) => (
                <g key={item.key}>
                  <circle cx={tooltipX + 13} cy={tooltipY + 60 + rowIndex * 22} r="3" fill={item.color} />
                  <text x={tooltipX + 23} y={tooltipY + 64 + rowIndex * 22} fontSize="11" fill="#ffffff">
                    {item.label}: {price(item.value)}{currentPrice ? ` / ${signedPct(item.value / currentPrice - 1)}` : ""}
                  </text>
                </g>
              ))}
            </g>
          ) : null}
        </svg>
      </div>
      <div className="mt-3 grid grid-cols-2 gap-2 text-xs text-muted sm:grid-cols-5">
        <span>黑线：历史价格</span>
        <span className="text-blue-700">蓝线：{scenarioDisplayLabel(data, "expected_path", "综合期望")}</span>
        <span className="text-teal">绿线：{scenarioDisplayLabel(data, "bounce_path", "反抽情景")}</span>
        <span className="text-rose">红线：{scenarioDisplayLabel(data, "bearish_path", "失败反抽")}</span>
        <span className="text-amber">黄线：{scenarioDisplayLabel(data, "analog_average_path", "历史均值")}</span>
      </div>
      <ScenarioWeights data={data} />
      <p className="mt-3 text-xs text-muted">
        模拟路径基于当前信号和历史相似情景生成，是概率情景，不是保证会发生的预测。
      </p>
    </section>
  );
}

function ScenarioRankingPanel({ data }: { data: SimulatedSymbolPaths }) {
  const ranking = data.scenario_ranking;
  if (!ranking) return null;
  const items = [
    ["第一可能", ranking.primary],
    ["第二可能", ranking.secondary],
    ["第三可能", ranking.tertiary],
  ] as const;
  return (
    <div className="mt-4 rounded-lg border border-line bg-panel p-4">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <p className="text-xs uppercase text-muted">Scenario Probability Ranking</p>
          <h3 className="mt-1 text-base font-semibold">最可能路径排序</h3>
          <p className="mt-1 text-sm text-muted">
            当前主路径：<b className="text-ink">{ranking.primary.label} {pct(ranking.primary.probability)}</b>
            {" "}；第二路径：<b className="text-ink">{ranking.secondary.label} {pct(ranking.secondary.probability)}</b>
          </p>
        </div>
        <div className="rounded-md bg-white px-3 py-2 text-sm">
          <p className="text-muted">路径差距</p>
          <p className="font-semibold">{scenarioGapText(data)}</p>
          {ranking.close_call ? <p className="mt-1 text-xs text-rose">路径分歧较大，不宜过度押注单一路径</p> : null}
        </div>
      </div>
      <div className="mt-4 grid gap-3 md:grid-cols-3">
        {items.map(([rankLabel, item]) => (
          <div key={rankLabel} className="rounded-md border border-line bg-white p-3">
            <div className="flex items-center justify-between gap-2">
              <p className="text-xs text-muted">{rankLabel}</p>
              <p className="text-sm font-semibold">{pct(item.probability)}</p>
            </div>
            <p className="mt-1 font-semibold text-ink">{item.label}</p>
            <p className="mt-2 text-xs leading-5 text-muted">{item.reason}</p>
            <p className="mt-2 text-xs text-muted">预期周期：{item.expected_horizon}；可靠度：{confidenceCn(item.confidence)}</p>
          </div>
        ))}
      </div>
      <div className="mt-3 rounded-md bg-white p-3 text-xs">
        <p className="font-medium text-ink">主路径切换条件</p>
        <p className="mt-1 text-muted">{primarySwitchText(data)}</p>
      </div>
      {ranking.ranking_note ? <p className="mt-3 text-xs text-muted">{ranking.ranking_note}</p> : null}
    </div>
  );
}

function ScenarioWeights({ data }: { data: SimulatedSymbolPaths }) {
  const pathModel = data.path_weight_model;
  const scenarioWeights = data.scenario_weights ?? {};
  const items = [
    ["基准", data.base_path_weight ?? pathModel?.base_path_weight ?? scenarioWeights.base_scenario],
    ["反抽", data.bounce_path_weight ?? pathModel?.bounce_path_weight ?? scenarioWeights.bounce_scenario],
    ["偏空", data.bearish_path_weight ?? pathModel?.bearish_path_weight ?? scenarioWeights.bearish_scenario],
    ["历史均值", data.analog_path_weight ?? pathModel?.analog_path_weight ?? scenarioWeights.historical_analog_average],
  ] as const;
  const factors = pathModel?.weight_factors ?? {};
  return (
    <div className="mt-3 rounded-md bg-white p-3">
      <div className="flex flex-wrap items-center gap-3 text-xs">
        <span className="font-medium text-ink">路径权重</span>
        {items.map(([label, value]) => (
          <span key={label} className="text-muted">{label}: <b className="text-ink">{pct(value, 0)}</b></span>
        ))}
        <span className="text-muted">路径可信度: <b className="text-ink">{confidenceCn(data.path_confidence)}</b></span>
        {data.low_confidence_simulation ? <span className="font-medium text-rose">低可信模拟</span> : null}
      </div>
      {Object.keys(factors).length ? (
        <div className="mt-3 grid gap-2 text-xs sm:grid-cols-4">
          {Object.entries(factors).map(([key, value]) => (
            <span key={key} className="rounded bg-panel px-2 py-1 text-muted">{factorText[key] ?? key}: <b className="text-ink">{pct(value, 0)}</b></span>
          ))}
        </div>
      ) : null}
    </div>
  );
}

function edgeRank(value: string | undefined) {
  if (value === "STRONG_EDGE") return 4;
  if (value === "MODERATE_EDGE") return 3;
  if (value === "WEAK_EDGE") return 2;
  return 1;
}

function MarketCard({
  symbol,
  selected,
  data,
  onSelect,
}: {
  symbol: string;
  selected: boolean;
  data: SimulatedSymbolPaths;
  onSelect: () => void;
}) {
  const support = data.historical_support_by_horizon;
  return (
    <button
      type="button"
      onClick={onSelect}
      title={`${symbol} 最近收盘价：${price(data.current_price)}；状态：${stateCn(data.market_state)}；反抽概率：${pct(data.bounce_probability)}`}
      className={`rounded-lg border p-3 text-left transition hover:border-teal hover:shadow-sm ${selected ? "border-teal bg-panel shadow-sm" : "border-line bg-white"}`}
    >
      <div className="flex items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <span className="flex h-10 w-10 items-center justify-center rounded-full bg-ink text-sm font-semibold text-white">{symbol}</span>
          <div>
            <p className="font-semibold">{symbol}</p>
            <p className="text-xs text-muted">{data.name}</p>
          </div>
        </div>
        <span className={data.live_signal ? "text-xs font-semibold text-teal" : "text-xs text-muted"}>{data.live_signal ? "有信号" : "无信号"}</span>
      </div>
      <div className="mt-3 grid grid-cols-2 gap-2 text-xs">
        <Metric label="收盘价" value={price(data.current_price)} />
        <Metric label="状态" value={stateCn(data.market_state)} />
        <Metric label="预测优势" value={edgeCn(data.market_edge_status?.market_edge_status)} />
        <Metric label="信号一致性" value={`${data.signal_agreement?.signal_agreement_score ?? "暂无"}`} />
        <Metric label="反抽概率" value={pct(data.bounce_probability)} />
        <Metric label="下跌延续" value={pct(data.downside_continuation_probability)} />
        <Metric label="趋势反转" value={pct(data.trend_reversal_probability)} />
        <Metric label="20d历史支持" value={supportCn(support?.by_horizon?.["20d"]?.support ?? data.historical_support)} />
      </div>
    </button>
  );
}

function Metric({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <p className="text-muted">{label}</p>
      <p className="mt-1 font-medium">{value}</p>
    </div>
  );
}

function DataQualityPanel({ report }: { report?: DataQualityReport }) {
  if (!report) return null;
  const summary = report.summary;
  return (
    <section className="mt-5 rounded-lg border border-line bg-white p-4">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <p className="text-xs uppercase text-muted">Data Quality Panel</p>
          <h2 className="mt-1 text-base font-semibold">数据质量审计</h2>
          <p className="mt-1 text-xs text-muted">最新交易日：{summary.latest_date ?? report.as_of ?? "暂无"}</p>
          <p className="mt-1 text-xs text-muted">页面生成：{displayTimestamp(report.generated_at)}</p>
          <p className="mt-1 text-xs text-teal">自动更新：美股交易日收盘后由 GitHub Actions 刷新，页面每 5 分钟检查新结果</p>
        </div>
        <div className="rounded-md bg-panel px-4 py-2 text-right">
          <p className="text-xs text-muted">数据完整度</p>
          <p className="text-2xl font-semibold">{summary.data_completeness_score}<span className="text-sm text-muted">/100</span></p>
        </div>
      </div>
      <div className="mt-4 grid gap-2 sm:grid-cols-2 lg:grid-cols-5">
        {Object.entries(report.coverage_categories).map(([key, item]) => (
          <div key={key} className="rounded-md border border-line bg-panel p-3">
            <div className="flex items-center justify-between gap-2">
              <p className="text-sm font-medium">{categoryText[key] ?? key}</p>
              <span className={`text-xs ${item.status === "available" ? "text-teal" : item.status === "partial" ? "text-amber" : "text-rose"}`}>{statusCn(item.status)}</span>
            </div>
            <p className="mt-2 text-xs text-muted">{item.detail}</p>
          </div>
        ))}
      </div>
      <p className="mt-3 text-xs text-muted">
        重要：期权、市场宽度、资金流、宏观如果没有真实接入，会明确显示“未接入”，不会假装参与预测。
      </p>
      {summary.missing_key_sources?.length ? (
        <p className="mt-2 text-xs text-muted">缺失关键源：{summary.missing_key_sources.slice(0, 8).join(" / ")}</p>
      ) : null}
      <p className="mt-2 text-xs text-muted">
        Finnhub：{summary.finnhub_available ? "可用" : summary.finnhub_rate_limited ? "限速/使用缓存或回退" : "未接入或 Secret 未注入"}；
        Yahoo fallback：{summary.yahoo_fallback_used ? "已使用" : "未使用"}；
        仍需真实源：FRED / options / breadth / flow。
      </p>
      {summary.quality_note ? <p className="mt-2 text-xs text-muted">{summary.quality_note}</p> : null}
    </section>
  );
}

function BreadthPanel({ status, selected }: { status?: BreadthStatus; selected?: SimulatedSymbolPaths }) {
  if (!status) return null;
  const summary = status.summary;
  return (
    <section className="mt-5 rounded-lg border border-line bg-white p-4">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <p className="text-xs uppercase text-muted">Data / Breadth</p>
          <h2 className="mt-1 text-base font-semibold">市场宽度：内部参与度</h2>
          <p className="mt-1 text-xs text-muted">判断反抽/修复是不是多数股票参与，而不是少数大票撑指数。</p>
        </div>
        <div className="rounded-md bg-panel px-4 py-2 text-right">
          <p className="text-xs text-muted">平均质量</p>
          <p className="text-2xl font-semibold">{scorePct(summary.average_breadth_quality_score)}</p>
          <p className="text-xs text-muted">{summary.true_breadth_available ? "true breadth" : "partial / proxy"}</p>
        </div>
      </div>
      <div className="mt-3 grid gap-2 text-xs sm:grid-cols-4">
        <Metric label="Breadth Coverage" value={summary.true_breadth_available ? "true" : summary.provider_available ? "partial" : "missing"} />
        <Metric label="真实宽度" value={summary.true_breadth_symbols?.join(" / ") || "暂无"} />
        <Metric label="Proxy" value={summary.breadth_proxy_only_symbols?.join(" / ") || "无"} />
        <Metric label="Stale warning" value={summary.stale_data ? `有：${summary.stale_symbols?.join(" / ")}` : "无"} />
      </div>
      {selected?.internal_resonance ? (
        <div className="mt-3 grid gap-2 text-xs sm:grid-cols-4">
          <Metric label="内部共振状态" value={resonanceCn(selected.internal_resonance.resonance_state)} />
          <Metric label="内部共振分数" value={scorePct(selected.internal_resonance.resonance_score)} />
          <Metric label="广泛参与" value={selected.internal_resonance.broad_participation ? "是" : "否"} />
          <Metric label="表面强风险" value={selected.internal_resonance.surface_strength_without_participation ? "有" : "无"} />
        </div>
      ) : null}
      <div className="mt-4 overflow-x-auto">
        <table className="w-full min-w-[860px] text-left text-xs">
          <thead className="border-b border-line text-muted">
            <tr>
              <th className="py-2">Universe</th>
              <th>Coverage</th>
              <th>有效 / 应有</th>
              <th>缺失样本</th>
              <th>Above 20/50/200d</th>
              <th>Advance / Decline</th>
              <th>New High / Low</th>
              <th>Confirmation</th>
              <th>Conflict</th>
            </tr>
          </thead>
          <tbody>
            {SYMBOL_ORDER.map((symbol) => {
              const item = status.universes?.[symbol];
              if (!item) return null;
              const missing = item.failed_tickers_sample?.length ? item.failed_tickers_sample.slice(0, 5).join(" / ") : "无";
              return (
                <tr key={symbol} className="border-b border-line last:border-0">
                  <td className="py-2 font-semibold">{symbol}</td>
                  <td>{breadthCoverageText(item.status, item.is_true_breadth, item.is_proxy)}</td>
                  <td>{item.constituents_used ?? "proxy"} / {item.constituents_expected ?? "proxy"}</td>
                  <td>{missing}</td>
                  <td>{pct(item.metrics.percent_above_20d)} / {pct(item.metrics.percent_above_50d)} / {pct(item.metrics.percent_above_200d)}</td>
                  <td>{item.metrics.advancers ?? "暂无"} / {item.metrics.decliners ?? "暂无"}</td>
                  <td>{item.metrics.new_highs_20d ?? "暂无"} / {item.metrics.new_lows_20d ?? "暂无"}</td>
                  <td className="font-medium text-teal">{scorePct(item.scores.breadth_confirmation_score)}</td>
                  <td className="font-medium text-rose">{scorePct(item.scores.breadth_conflict_score)}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
      <div className="mt-3 rounded-md bg-panel p-3 text-sm">
        <p className="font-medium text-ink">Breadth 对当前判断的影响</p>
        <p className="mt-1 text-muted">{breadthImpactText(status, selected)}</p>
      </div>
    </section>
  );
}

function ConfidencePanel({ data }: { data: SimulatedSymbolPaths }) {
  const confidence = data.model_confidence;
  if (!confidence) return null;
  return (
    <section className="rounded-lg border border-line bg-white p-4">
      <div className="flex items-start justify-between gap-3">
        <div>
          <p className="text-xs uppercase text-muted">Model Confidence</p>
          <h2 className="mt-1 text-base font-semibold">模型可信度评分</h2>
        </div>
        <div className="text-right">
          <p className="text-2xl font-semibold">{confidence.confidence_score}<span className="text-sm text-muted">/100</span></p>
          <p className="text-xs text-muted">{confidenceCn(confidence.confidence_level)}</p>
        </div>
      </div>
      <ul className="mt-3 space-y-1 text-xs text-muted">
        {confidence.why_confidence_is_limited.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
      {data.signal_agreement ? (
        <div className="mt-3 rounded-md bg-panel p-3 text-xs">
          <p className="font-medium text-ink">信号一致性：{data.signal_agreement.signal_agreement_score}/100，{agreementCn(data.signal_agreement.agreement_level)}</p>
          <p className="mt-1 text-muted">冲突信号：{data.signal_agreement.conflicting_signals.map((item) => item.name).join(" / ") || "暂无明显冲突"}</p>
        </div>
      ) : null}
    </section>
  );
}

function CurrentSummary({ data }: { data: SimulatedSymbolPaths }) {
  const support = data.historical_support_by_horizon;
  const ranking = data.scenario_ranking;
  return (
    <section className="rounded-lg border border-teal bg-[#eefaf5] p-5 shadow-sm">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <p className="text-xs uppercase text-teal">大白话预测总结</p>
          <h2 className="mt-1 text-2xl font-semibold">{data.symbol} 当前判断</h2>
        </div>
        <div className="rounded-md bg-white px-3 py-2 text-sm">
          <p className="text-muted">下一步</p>
          <p className="font-semibold text-ink">{plainAction(data)}</p>
        </div>
      </div>
      <p className="mt-4 text-base leading-7">{plainDecision(data)}</p>
      <p className="mt-3 text-sm leading-6 text-muted">{plainSummary(data)}</p>
      <div className="mt-5 grid gap-3 text-sm sm:grid-cols-4">
        <Metric label="今天是否有预测优势" value={edgeCn(data.market_edge_status?.market_edge_status)} />
        <Metric label="多源确认" value={data.signal_confirmation ? `${data.signal_confirmation.confirmation_score}/100 / ${confirmationCn(data.signal_confirmation.confirmation_level)}` : "暂无"} />
        <Metric label="当前状态" value={stateCn(data.market_state)} />
        <Metric label="最强方向" value={strongestPredictorText(data)} />
        <Metric label="最大概率路径" value={ranking?.primary ? `${ranking.primary.label} ${pct(ranking.primary.probability)}` : strongestScenario(data)} />
        <Metric label="第二可能路径" value={ranking?.secondary ? `${ranking.secondary.label} ${pct(ranking.secondary.probability)}` : "暂无"} />
        <Metric label="路径差距" value={scenarioGapText(data)} />
        <Metric label="主路径失效条件" value={primarySwitchText(data)} />
        <Metric label="5d / 20d / 60d 历史支持" value={`${supportCn(support?.by_horizon?.["5d"]?.support)} / ${supportCn(support?.by_horizon?.["20d"]?.support)} / ${supportCn(support?.by_horizon?.["60d"]?.support)}`} />
      </div>
    </section>
  );
}

function FirstScreenDecisionPanel({
  selected,
  strongest,
}: {
  selected: SimulatedSymbolPaths;
  strongest?: SimulatedSymbolPaths;
}) {
  const supporting = selected.signal_confirmation?.supporting_evidence ?? selected.signal_agreement?.supporting_signals ?? [];
  const conflicts = selected.signal_confirmation?.conflicting_evidence ?? selected.signal_agreement?.conflicting_signals ?? [];
  const missing = selected.signal_confirmation?.missing_evidence ?? [];
  return (
    <section className="mt-5 rounded-lg border border-line bg-white p-4">
      <div className="grid gap-4 lg:grid-cols-[1.15fr_0.85fr]">
        <div>
          <p className="text-xs uppercase text-muted">Today&apos;s Prediction Edge</p>
          <h2 className="mt-1 text-xl font-semibold">今天是否有可用预测优势：{edgeCn(selected.market_edge_status?.market_edge_status)}</h2>
          <p className="mt-2 text-sm leading-6 text-muted">{selected.market_edge_status?.summary ?? "当前优势状态未知。"}</p>
          <div className="mt-4 grid gap-3 text-sm sm:grid-cols-4">
            <Metric label="最强预测方向" value={strongestPredictorText(selected)} />
            <Metric label="当前状态" value={stateCn(selected.market_state)} />
            <Metric label="最强指数信号" value={strongest ? `${strongest.symbol} / ${edgeCn(strongest.market_edge_status?.market_edge_status)}` : "暂无"} />
            <Metric label="预测可信度" value={`${selected.model_confidence?.confidence_score ?? "暂无"}/100`} />
            <Metric label="多源确认" value={selected.signal_confirmation ? `${selected.signal_confirmation.confirmation_score}/100 / ${confirmationCn(selected.signal_confirmation.confirmation_level)}` : "暂无"} />
            <Metric label="主路径" value={selected.scenario_ranking?.primary ? `${selected.scenario_ranking.primary.label} ${pct(selected.scenario_ranking.primary.probability)}` : "暂无"} />
            <Metric label="第二路径" value={selected.scenario_ranking?.secondary ? `${selected.scenario_ranking.secondary.label} ${pct(selected.scenario_ranking.secondary.probability)}` : "暂无"} />
            <Metric label="路径差距" value={scenarioGapText(selected)} />
          </div>
        </div>
        <div className="grid gap-3 text-xs sm:grid-cols-3 lg:grid-cols-1">
          <div className="rounded-md bg-panel p-3">
            <p className="font-medium text-ink">支持信号</p>
            <p className="mt-1 text-muted">{supporting.slice(0, 4).map((item) => item.name).join(" / ") || "暂无明显支持"}</p>
          </div>
          <div className="rounded-md bg-panel p-3">
            <p className="font-medium text-ink">冲突信号</p>
            <p className="mt-1 text-muted">{conflicts.slice(0, 4).map((item) => item.name).join(" / ") || "暂无明显冲突"}</p>
          </div>
          <div className="rounded-md bg-panel p-3">
            <p className="font-medium text-ink">缺失证据</p>
            <p className="mt-1 text-muted">{missing.slice(0, 4).map((item) => item.name).join(" / ") || "暂无关键缺失"}</p>
          </div>
          <div className="rounded-md bg-panel p-3">
            <p className="font-medium text-ink">失效条件</p>
            <p className="mt-1 text-muted">{selected.risk_invalidation_conditions.slice(0, 3).join(" / ")}</p>
          </div>
        </div>
      </div>
    </section>
  );
}

function PredictorPanel({ data }: { data: SimulatedSymbolPaths }) {
  const predictors = data.predictors;
  if (!predictors) return null;
  const labels: Record<string, string> = {
    bounce_predictor: "反抽预测器",
    downside_continuation_predictor: "下跌延续预测器",
    trend_reversal_predictor: "趋势修复/反转预测器",
    risk_expansion_predictor: "风险扩散预测器",
  };
  return (
    <section className="mt-5 rounded-lg border border-line bg-white p-4">
      <p className="text-xs uppercase text-muted">Predictor Stack</p>
      <h2 className="mt-1 text-base font-semibold">四个独立预测器</h2>
      <div className="mt-3 grid gap-3 md:grid-cols-4">
        {Object.entries(predictors).map(([key, predictor]) => (
          <div key={key} className="rounded-md bg-panel p-3">
            <div className="flex items-center justify-between gap-2">
              <p className="text-sm font-medium">{labels[key] ?? key}</p>
              <p className="text-sm font-semibold">{pct(predictor.probability)}</p>
            </div>
            <p className="mt-1 text-xs text-muted">可信度：{pct(predictor.confidence)}，最佳周期：{predictor.best_horizon}</p>
            <ul className="mt-2 space-y-1 text-xs text-muted">
              {predictor.main_drivers.slice(0, 3).map((item) => <li key={item}>{item}</li>)}
            </ul>
          </div>
        ))}
      </div>
      <p className="mt-3 text-xs text-muted">四个预测器分开看，避免一个综合模型强行解释所有市场状态。</p>
    </section>
  );
}

function HorizonTable({ data }: { data: SimulatedSymbolPaths }) {
  const predictions = data.prediction_horizons ?? {};
  return (
    <section className="mt-5 rounded-lg border border-line bg-white p-4">
      <div>
        <p className="text-xs uppercase text-muted">Period Forecast</p>
        <h2 className="mt-1 text-base font-semibold">分周期预测</h2>
      </div>
      <div className="mt-3 overflow-x-auto">
        <table className="w-full min-w-[760px] text-left text-sm">
          <thead className="border-b border-line text-xs text-muted">
            <tr>
              <th className="py-2">周期</th>
              <th>方向判断</th>
              <th>预期区间</th>
              <th>上涨概率</th>
              <th>下跌概率</th>
              <th>反抽概率</th>
              <th>失败反抽风险</th>
              <th>可信度</th>
              <th>历史支持</th>
            </tr>
          </thead>
          <tbody>
            {HORIZON_ORDER.map((key) => {
              const row = predictions[key];
              if (!row) return null;
              return (
                <tr key={key} className="border-b border-line last:border-0">
                  <td className="py-2 font-medium">{key}</td>
                  <td>{row.expected_direction}</td>
                  <td>{signedPct(row.expected_return_range?.[0])} 到 {signedPct(row.expected_return_range?.[1])}</td>
                  <td>{pct(row.up_probability)}</td>
                  <td>{pct(row.down_probability)}</td>
                  <td>{pct(row.bounce_probability)}</td>
                  <td>{pct(row.failed_bounce_risk)}</td>
                  <td>{pct(row.confidence)}</td>
                  <td>{supportCn(row.historical_support)}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </section>
  );
}

function MarketStatePanel({ data }: { data: SimulatedSymbolPaths }) {
  const states = data.market_state_v2?.states;
  if (!states) return null;
  const topStates = Object.entries(states).sort(([, left], [, right]) => right.probability - left.probability).slice(0, 5);
  const selectedState = states[data.market_state as keyof typeof states];
  return (
    <section className="mt-5 rounded-lg border border-line bg-white p-4">
      <p className="text-xs uppercase text-muted">Market State Engine v2</p>
      <h2 className="mt-1 text-base font-semibold">综合市场状态</h2>
      <div className="mt-3 grid gap-3 md:grid-cols-5">
        {topStates.map(([state, payload]) => (
          <div key={state} className="rounded-md bg-panel p-3">
            <div className="flex items-center justify-between gap-2">
              <p className="text-sm font-medium">{stateCn(state)}</p>
              <p className="text-sm font-semibold">{pct(payload.probability)}</p>
            </div>
            <p className="mt-2 text-xs text-muted">{payload.reason}</p>
          </div>
        ))}
      </div>
      <div className="mt-4 grid gap-3 md:grid-cols-2">
        <div className="rounded-md border border-line p-3">
          <p className="text-sm font-medium">支持特征</p>
          <ul className="mt-2 space-y-1 text-xs text-muted">
            {selectedState?.supporting_features?.map((item) => <li key={item}>{item}</li>)}
          </ul>
        </div>
        <div className="rounded-md border border-line p-3">
          <p className="text-sm font-medium">冲突特征</p>
          <ul className="mt-2 space-y-1 text-xs text-muted">
            {selectedState?.conflicting_features?.map((item) => <li key={item}>{item}</li>)}
          </ul>
        </div>
      </div>
    </section>
  );
}

function ScenarioCards({ data }: { data: SimulatedSymbolPaths }) {
  return (
    <section className="mt-5 grid gap-3 md:grid-cols-4">
      {data.scenario_cards.map((card) => (
        <div key={card.name} className="rounded-lg border border-line bg-white p-4">
          <p className="text-sm font-semibold">{card.name_cn}</p>
          <p className="mt-2 text-xs leading-5 text-muted">{card.summary_cn}</p>
          <div className="mt-3 flex items-center justify-between text-xs">
            <span className="text-muted">20d收益</span>
            <span className={card.return_20d >= 0 ? "font-medium text-teal" : "font-medium text-rose"}>{signedPct(card.return_20d)}</span>
          </div>
          <div className="mt-1 flex items-center justify-between text-xs">
            <span className="text-muted">权重</span>
            <span className="font-medium">{pct(card.probability_weight)}</span>
          </div>
        </div>
      ))}
    </section>
  );
}

function HistoricalAnalogs({
  cases,
  data,
}: {
  cases: HistoricalAnalogCase[];
  data: SimulatedSymbolPaths;
}) {
  const support = data.historical_support_by_horizon;
  return (
    <section className="mt-5 rounded-lg border border-line bg-white p-4">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <p className="text-xs uppercase text-muted">Historical Analogs</p>
          <h2 className="mt-1 text-base font-semibold">历史相似情景</h2>
        </div>
        <div className="text-xs text-muted sm:text-right">
          <p>样本质量：{support?.analog_sample_quality ? confidenceCn(support.analog_sample_quality) : "未知"}</p>
          <p>最坏路径风险：{support?.worst_path_risk ?? "未知"}</p>
        </div>
      </div>
      <div className="mt-3 grid gap-2 sm:grid-cols-5">
        {["3d", "5d", "10d", "20d", "60d"].map((key) => {
          const item = support?.by_horizon?.[key];
          return (
            <div key={key} className="rounded-md bg-panel p-3 text-xs">
              <p className="font-medium">{key}</p>
              <p className="mt-1 text-muted">支持：{supportCn(item?.support)}</p>
              <p className="text-muted">均值：{signedPct(item?.avg_return)}</p>
              <p className="text-muted">胜率：{pct(item?.hit_rate)}</p>
            </div>
          );
        })}
      </div>
      <div className="mt-4 grid gap-3 lg:grid-cols-5">
        {cases.map((item) => (
          <div key={item.date} className="rounded-md border border-line p-3">
            <div className="flex items-center justify-between gap-2">
              <p className="font-medium">{item.date}</p>
              <p className="text-xs text-muted">{pct(item.similarity_score)}</p>
            </div>
            <p className="mt-2 text-xs text-muted">状态：{item.regime}</p>
            <p className="mt-1 text-xs text-muted">5d：{signedPct(item.forward_return_5d)}</p>
            <p className="text-xs text-muted">20d：{signedPct(item.forward_return_20d)}</p>
            <p className="text-xs text-muted">60d：{signedPct(item.forward_return_60d)}</p>
            <p className="mt-2 text-xs text-rose">最差路径：{signedPct(item.max_adverse_excursion)}</p>
          </div>
        ))}
      </div>
      <p className="mt-3 text-xs text-muted">历史相似不等于未来必然重复，只用于解释、条件分布和前向观察。</p>
    </section>
  );
}

function RiskPanel({ data }: { data: SimulatedSymbolPaths }) {
  return (
    <section className="mt-5 rounded-lg border border-line bg-white p-4">
      <p className="text-xs uppercase text-muted">Risk / Invalidation</p>
      <h2 className="mt-1 text-base font-semibold">预测失效条件</h2>
      <div className="mt-3 grid gap-2 md:grid-cols-2">
        {data.risk_invalidation_conditions.map((item) => (
          <div key={item} className="rounded-md bg-panel p-3 text-sm text-muted">{item}</div>
        ))}
      </div>
    </section>
  );
}

export function MarketDashboard({ dashboard: initialDashboard }: { dashboard: PredictionDashboard }) {
  const [dashboard, setDashboard] = useState(initialDashboard);
  const availableSymbols = SYMBOL_ORDER.filter((symbol) => dashboard.simulated_paths.symbols[symbol]);
  const defaultSymbol = availableSymbols.includes(dashboard.overview.strongest_symbol)
    ? dashboard.overview.strongest_symbol
    : availableSymbols[0] ?? "SPY";
  const [selectedSymbol, setSelectedSymbol] = useState(defaultSymbol);
  const selected = dashboard.simulated_paths.symbols[selectedSymbol];
  const analog = dashboard.analogs[selectedSymbol];
  const topAnalogs = (analog?.top_similar_cases ?? []).slice(0, 5);
  const strongest = useMemo(() => {
    return availableSymbols
      .map((symbol) => dashboard.simulated_paths.symbols[symbol])
      .sort((left, right) => {
        const edgeDelta = edgeRank(right.market_edge_status?.market_edge_status) - edgeRank(left.market_edge_status?.market_edge_status);
        if (edgeDelta !== 0) return edgeDelta;
        const agreementDelta = (right.signal_agreement?.signal_agreement_score ?? 0) - (left.signal_agreement?.signal_agreement_score ?? 0);
        if (agreementDelta !== 0) return agreementDelta;
        return right.bounce_probability - left.bounce_probability;
      })[0];
  }, [availableSymbols, dashboard.simulated_paths.symbols]);

  useEffect(() => {
    setDashboard(initialDashboard);
  }, [initialDashboard]);

  useEffect(() => {
    const refreshDashboard = async () => {
      try {
        const response = await fetch(`${publicAssetPath("prediction-dashboard.json")}?ts=${Date.now()}`, {
          cache: "no-store",
        });
        if (!response.ok) return;
        const nextDashboard = (await response.json()) as PredictionDashboard;
        if (!nextDashboard?.overview?.symbols) return;
        setDashboard((currentDashboard) => (
          dashboardGeneratedAt(nextDashboard) !== dashboardGeneratedAt(currentDashboard)
            ? nextDashboard
            : currentDashboard
        ));
      } catch {
        // Keep the last rendered dashboard when the static file is temporarily unavailable.
      }
    };
    const interval = window.setInterval(refreshDashboard, 5 * 60 * 1000);
    return () => window.clearInterval(interval);
  }, []);

  useEffect(() => {
    if (availableSymbols.length && !availableSymbols.includes(selectedSymbol)) {
      setSelectedSymbol(defaultSymbol);
    }
  }, [availableSymbols, defaultSymbol, selectedSymbol]);

  if (!selected) {
    return (
      <main className="mx-auto min-h-screen w-full max-w-5xl px-4 py-5">
        <h1 className="text-2xl font-semibold">市场预测终端</h1>
        <p className="mt-3 text-muted">暂无可用数据。请先运行 GitHub Actions 的 Forward Alpha v1 Observation。</p>
      </main>
    );
  }

  return (
    <main className="mx-auto min-h-screen w-full max-w-6xl px-4 py-5">
      <header className="border-b border-line pb-5">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <p className="text-xs uppercase tracking-[0.18em] text-muted">Market Prediction Dashboard</p>
            <h1 className="mt-2 text-3xl font-semibold tracking-normal">市场预测终端</h1>
            <p className="mt-2 max-w-3xl text-sm leading-6 text-muted">
              页面直接展示大盘状态、概率路径、历史相似情景和数据质量。Alpha v1 仍是 RESEARCH ALPHA CANDIDATE，不是实盘交易信号。
            </p>
          </div>
          <div className="rounded-lg border border-line bg-white p-3 text-sm">
            <p className="text-muted">最新交易日</p>
            <p className="mt-1 font-medium">{dashboard.data_quality_report?.summary.latest_date ?? dashboard.as_of ?? "暂无"}</p>
            <p className="mt-2 text-muted">页面生成</p>
            <p className="mt-1 font-medium">{displayTimestamp(dashboard.data_quality_report?.generated_at ?? dashboard.market_intelligence_v3?.generated_at ?? dashboard.market_intelligence_v2?.generated_at)}</p>
            <p className="mt-2 text-xs text-teal">自动：收盘后更新，页面每 5 分钟检查</p>
          </div>
        </div>
      </header>

      <section className="mt-5">
        <div className="flex items-center justify-between gap-3">
          <div>
            <p className="text-xs uppercase text-muted">Market Overview</p>
            <h2 className="mt-1 text-base font-semibold">主要大盘指数 / ETF</h2>
          </div>
          {strongest && (
            <p className="text-right text-xs text-muted">当前反抽概率最高：<b className="text-ink">{strongest.symbol}</b></p>
          )}
        </div>
        <div className="mt-3 grid gap-3 md:grid-cols-4">
          {availableSymbols.map((symbol) => (
            <MarketCard
              key={symbol}
              symbol={symbol}
              selected={selectedSymbol === symbol}
              data={dashboard.simulated_paths.symbols[symbol]}
              onSelect={() => setSelectedSymbol(symbol)}
            />
          ))}
        </div>
      </section>

      <div className="mt-5 grid gap-5 lg:grid-cols-[1.4fr_0.9fr]">
        <CurrentSummary data={selected} />
        <ConfidencePanel data={selected} />
      </div>

      <PredictionChart data={selected} />
      <FirstScreenDecisionPanel selected={selected} strongest={strongest} />
      <HorizonTable data={selected} />
      <PredictorPanel data={selected} />
      <MarketStatePanel data={selected} />
      <ScenarioCards data={selected} />
      <HistoricalAnalogs cases={topAnalogs} data={selected} />
      <RiskPanel data={selected} />
      <DataQualityPanel report={dashboard.data_quality_report ?? dashboard.market_intelligence_v2?.data_quality_report} />
      <BreadthPanel status={dashboard.breadth_status} selected={selected} />
    </main>
  );
}
