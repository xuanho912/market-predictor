"use client";

import { useMemo, useState } from "react";
import type { DataQualityReport, HistoricalAnalogCase, PredictionDashboard, SimulatedSymbolPaths } from "../lib/api";

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

function pct(value: number | null | undefined, digits = 0) {
  if (value == null || Number.isNaN(value)) return "暂无";
  return `${(value * 100).toFixed(digits)}%`;
}

function price(value: number | null | undefined) {
  if (value == null || Number.isNaN(value)) return "暂无";
  return value.toLocaleString("zh-CN", { maximumFractionDigits: 2 });
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
  if (value === "not_available") return "未接入";
  return value ?? "未知";
}

function edgeCn(value: string | undefined) {
  if (value === "NO_EDGE") return "无优势";
  if (value === "WEAK_EDGE") return "弱优势";
  if (value === "MODERATE_EDGE") return "中等优势";
  if (value === "STRONG_EDGE") return "强优势";
  return value ?? "未知";
}

function agreementCn(value: string | undefined) {
  if (value === "strong") return "强一致";
  if (value === "mixed") return "有冲突";
  if (value === "weak") return "弱一致";
  return value ?? "未知";
}

function strongestScenario(symbolData: SimulatedSymbolPaths | undefined) {
  if (!symbolData) return "暂无";
  const cards = [...symbolData.scenario_cards].sort((left, right) => right.probability_weight - left.probability_weight);
  return cards[0]?.name_cn ?? "暂无";
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

function PredictionChart({ data }: { data: SimulatedSymbolPaths }) {
  const width = 760;
  const height = 320;
  const pad = 36;
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
  const horizonIndexes = [3, 5, 10, 20, 60].map((days) => ({
    days,
    index: Math.min(paths.split_index + days, paths.dates.length - 1),
  }));

  return (
    <section className="mt-5 rounded-lg border border-line bg-panel p-4">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div>
          <p className="text-xs uppercase text-muted">Past + Simulated Future Path</p>
          <h2 className="mt-1 text-base font-semibold">过去走势 + 概率情景路径</h2>
        </div>
        <p className="text-xs text-muted sm:text-right">分界线右侧为模拟路径，低可信路径会被标记为观察。</p>
      </div>
      <div className="mt-3 overflow-x-auto">
        <svg viewBox={`0 0 ${width} ${height}`} className="h-80 min-w-[720px] w-full">
          <rect x="0" y="0" width={width} height={height} rx="8" fill="#ffffff" />
          {[0.2, 0.4, 0.6, 0.8].map((ratio) => (
            <line key={ratio} x1={pad} x2={width - pad} y1={pad + (height - pad * 2) * ratio} y2={pad + (height - pad * 2) * ratio} stroke="#e5ece9" />
          ))}
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
          <path d={svgPath(paths.expected_path, minY, maxY, width, height, pad)} fill="none" stroke="#2563eb" strokeWidth="2.3" />
          <path d={svgPath(paths.bounce_path, minY, maxY, width, height, pad)} fill="none" stroke="#0f9f7a" strokeWidth="2" />
          <path d={svgPath(paths.bearish_path, minY, maxY, width, height, pad)} fill="none" stroke="#dc4a4a" strokeWidth="2" />
          <path d={svgPath(paths.analog_average_path, minY, maxY, width, height, pad)} fill="none" stroke="#f59e0b" strokeWidth="2" />
          <text x={pad} y={22} fontSize="12" fill="#62706b">历史价格</text>
          <text x={splitX + 10} y={22} fontSize="12" fill="#62706b">模拟未来</text>
        </svg>
      </div>
      <div className="mt-3 grid grid-cols-2 gap-2 text-xs text-muted sm:grid-cols-5">
        <span>黑线：历史价格</span>
        <span className="text-blue-700">蓝线：综合期望</span>
        <span className="text-teal">绿线：反抽情景</span>
        <span className="text-rose">红线：失败反抽</span>
        <span className="text-amber">黄线：历史均值</span>
      </div>
      <ScenarioWeights data={data} />
      <p className="mt-3 text-xs text-muted">
        模拟路径基于当前信号和历史相似情景生成，是概率情景，不是保证会发生的预测。
      </p>
    </section>
  );
}

function ScenarioWeights({ data }: { data: SimulatedSymbolPaths }) {
  const weights = data.scenario_weights ?? {};
  const items = [
    ["基准", weights.base_scenario],
    ["反抽", weights.bounce_scenario],
    ["偏空", weights.bearish_scenario],
    ["历史均值", weights.historical_analog_average],
  ] as const;
  return (
    <div className="mt-3 rounded-md bg-white p-3">
      <div className="flex flex-wrap items-center gap-3 text-xs">
        <span className="font-medium text-ink">路径权重</span>
        {items.map(([label, value]) => (
          <span key={label} className="text-muted">{label}: <b className="text-ink">{pct(value, 0)}</b></span>
        ))}
        <span className="text-muted">路径可信度: <b className="text-ink">{confidenceCn(data.path_confidence)}</b></span>
      </div>
    </div>
  );
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
      className={`rounded-lg border p-3 text-left transition ${selected ? "border-teal bg-panel shadow-sm" : "border-line bg-white"}`}
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
          <p className="mt-1 text-xs text-muted">最近更新：{summary.latest_date ?? report.as_of ?? "暂无"}</p>
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
      {summary.quality_note ? <p className="mt-2 text-xs text-muted">{summary.quality_note}</p> : null}
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
  return (
    <section className="rounded-lg border border-teal bg-[#eefaf5] p-4">
      <p className="text-xs uppercase text-teal">大白话预测总结</p>
      <h2 className="mt-1 text-lg font-semibold">{data.symbol} 当前判断</h2>
      <p className="mt-3 text-sm leading-6">{plainSummary(data)}</p>
      <div className="mt-4 grid gap-3 text-sm sm:grid-cols-3">
        <Metric label="今天是否有预测优势" value={edgeCn(data.market_edge_status?.market_edge_status)} />
        <Metric label="当前状态" value={stateCn(data.market_state)} />
        <Metric label="最强情景" value={strongestScenario(data)} />
        <Metric label="5d / 20d / 60d 历史支持" value={`${supportCn(support?.by_horizon?.["5d"]?.support)} / ${supportCn(support?.by_horizon?.["20d"]?.support)} / ${supportCn(support?.by_horizon?.["60d"]?.support)}`} />
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

export function MarketDashboard({ dashboard }: { dashboard: PredictionDashboard }) {
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
      .sort((left, right) => right.bounce_probability - left.bounce_probability)[0];
  }, [availableSymbols, dashboard.simulated_paths.symbols]);

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
            <p className="text-muted">最近更新</p>
            <p className="mt-1 font-medium">{dashboard.data_quality_report?.summary.latest_date ?? dashboard.as_of ?? "暂无"}</p>
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

      <DataQualityPanel report={dashboard.data_quality_report ?? dashboard.market_intelligence_v2?.data_quality_report} />

      <div className="mt-5 grid gap-5 lg:grid-cols-[1.4fr_0.9fr]">
        <CurrentSummary data={selected} />
        <ConfidencePanel data={selected} />
      </div>

      <PredictionChart data={selected} />
      <HorizonTable data={selected} />
      <PredictorPanel data={selected} />
      <MarketStatePanel data={selected} />
      <ScenarioCards data={selected} />
      <HistoricalAnalogs cases={topAnalogs} data={selected} />
      <RiskPanel data={selected} />
    </main>
  );
}
