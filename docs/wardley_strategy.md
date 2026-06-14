# Wardley Strategy For Market Predictor

核心原则：

> 值得独一无二的，自己做；可以平平无奇的，外包给世界。

这个项目不是为了自研基础设施，不是为了折腾部署，也不是为了做 Trading Bot。项目目标是打造一个能直接预测和解释大盘下一步概率路径的 Market Prediction Dashboard。

## 最终用户

最终用户：我本人。

核心需求：

- 打开网页即可看到大盘接下来更可能反抽、继续跌、震荡还是趋势修复。
- 直接看到 SPY / QQQ / IWM / DIA 的未来模拟路径、信号强弱、历史相似情景、失效条件和风险解释。
- 不需要提问，不需要手动运行脚本，不需要理解底层工程细节。
- 第一屏必须回答：今天有没有预测优势，最大概率路径是什么，第二可能路径是什么，主次路径差距多少，预测可信度多少，哪些数据支持，哪些数据冲突，什么情况会让主路径失效。

## 核心阿尔法优势

项目的核心优势不是部署、图表、API key、数据搬运、登录系统、云平台或框架选择。

真正值得自研和长期打磨的是：

- Market State Engine
- Signal Agreement / Signal Confirmation
- Historical Analog Engine
- Edge / No Edge 判断
- 反抽 / 下跌延续 / 趋势反转 / 风险扩散预测器
- Scenario Probability Ranking
- 模拟未来路径权重
- 高置信预测验证
- 风险失效条件解释
- Daily Market Brief 的判断质量

这些模块离用户需求最近，也最直接决定预测质量和解释质量。

## Build Vs Buy Map

| 类别 | 模块 | 策略 |
| --- | --- | --- |
| Genesis / Custom | 市场状态判断 | 自研重点 |
| Genesis / Custom | Edge / No Edge | 自研重点 |
| Genesis / Custom | Historical Analog 解释 | 自研重点 |
| Genesis / Custom | Signal Agreement / Confirmation | 自研重点 |
| Genesis / Custom | Confidence Score | 自研重点 |
| Genesis / Custom | Simulated Path Weighting | 自研重点 |
| Genesis / Custom | Predictor Ensemble | 自研重点 |
| Genesis / Custom | Invalidation Conditions | 自研重点 |
| Genesis / Custom | Daily Market Brief | 自研重点 |
| Product / Rental | Finnhub API | 直接接入 |
| Product / Rental | FRED API | 直接接入 |
| Product / Rental | Yahoo / Stooq fallback | 直接接入 |
| Product / Rental | CBOE / options data if available | 直接接入 |
| Product / Rental | Cloudflare Pages / GitHub Actions | 使用现成服务 |
| Commodity / Utility | hosting | 不浪费时间 |
| Commodity / Utility | deployment | 不浪费时间 |
| Commodity / Utility | chart library | 使用成熟库 |
| Commodity / Utility | CI/CD | 使用 GitHub Actions |
| Commodity / Utility | frontend framework | 使用成熟框架 |
| Commodity / Utility | data caching infrastructure | 只做必要缓存，不把它当核心 |
| Commodity / Utility | authentication if not necessary | 不做 |

## Do Not Build

不要自研：

- 通用数据平台
- 通用图表系统
- 登录系统
- 云平台
- 券商接入系统
- 自动执行系统
- 订单模拟工作流
- 仓位管理规则
- 模拟组合核算或下单模拟
- 为部署体验牺牲预测质量的工程架构

如果某个模块已经是成熟市场服务，就优先购买、接 API、用现成库或用托管平台。

## 项目战略优先级

最高优先级：

1. 数据质量
2. Market State Engine
3. Signal Confirmation
4. Historical Analog
5. Predictor 分层
6. Edge / No Edge
7. Confidence Calibration
8. High-confidence Forecast Validation
9. Scenario Probability Ranking
10. Daily Market Brief

低优先级：

- UI 美化
- 部署平台切换
- 自建数据抓取框架
- 非必要 backend 重构
- 复杂工程架构
- 登录、权限、账号体系，除非未来明确需要

## 数据源原则

Finnhub / FRED / CBOE / Yahoo 都是右侧供应商，不是项目护城河。

接入它们的目的不是展示“我们有很多数据”，而是服务左侧判断层：

- 提高 data completeness
- 提高 model confidence
- 支持 signal confirmation
- 支持 macro event risk
- 支持 simulated path weighting
- 支持 risk invalidation explanation

如果某个数据源缺失，必须明确显示 `missing`、`not_available`、`fallback`、`stale_data` 或 `data_source_failed`，不能假装成可用。

## 预测而非交易

这个项目只做预测和解释，不做交易。

允许：

- forecast signal
- forecast start date
- forecast horizon
- scenario validation
- forward return tracking
- prediction accuracy
- primary scenario hit rate
- invalidation condition
- risk condition

不允许作为产品方向：

- order-simulation workflow
- execution-oriented signal
- position-management rule
- simulated portfolio accounting
- execution strategy
- execution recommendation
- actionable order recommendation

Alpha v1 只能叫 forecast signal / bounce scenario input。它不是执行输入，也不是下单依据。

## 私有化和成果保护

核心代码、Alpha 逻辑、Market Intelligence Engine、Historical Analog Engine、Signal Agreement、模拟路径权重逻辑都应该保留在 private repo。

API Key 只能放在 GitHub Secrets：

- 不写进代码
- 不写进 README
- 不提交 `.env`
- 不输出到日志
- 不放进 `frontend/public`
- 不用 `NEXT_PUBLIC_*` 暴露给前端

公开网页只展示结果，不暴露 key，不暴露完整算法细节。

## 最终页面目标

用户打开页面后，不需要提问，不需要运行脚本，第一屏直接回答：

1. 今天有没有预测优势？
2. 当前最大概率路径是什么？
3. 第二可能路径是什么？
4. 主路径概率是多少？
5. 主路径和次路径差距是多少？
6. 当前预测可信度是多少？
7. 哪些数据支持这个判断？
8. 哪些数据冲突？
9. 什么情况会让主路径失效？
10. 未来几个周期需要观察什么？

## Codex 工作规则

以后每次新增功能前，必须先判断：

1. 这个功能离用户是否近？
2. 这个功能是否决定预测质量？
3. 市面上是否已有成熟服务？
4. 它是 Genesis / Custom，还是 Product / Rental，还是 Commodity / Utility？

如果是右侧商品化模块，优先接 API、买服务、用现成库，不允许过度自研。

如果是左侧核心判断模块，并且能提高预测质量、解释质量或验证质量，才值得深化。
