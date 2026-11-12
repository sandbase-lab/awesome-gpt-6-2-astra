# GPT-6.2 Astra 对比 Fable 5.5 和 Claude Opus 5.5

[English](../model-comparison.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

两类证据，分开呈现：

1. **我们测到的。** Lab [Evals 榜单](https://www.sandbase.ai/leaderboards?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra) 展示 Artificial Analysis 的数据；Lab [Pelican Test](https://www.sandbase.ai/arena/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra) 用同一份固定提示词跑每个模型并给结果打分。
2. **创作者报告的。** 发在 X 上的同提示词运行，附他们自己的花费和耗时。有参考价值，但我们没有验证。

## 我们测到的

**本列表所依据的实测数据来源中，没有 GPT-6.2 Astra 这一行。** 下面的 Evals 和 Pelican Test 数字只是对手模型的参照，不是 GPT-6.2 Astra 的成绩。最新的行请查看实时榜单。

Evals 榜单，Artificial Analysis 2026-10-19 快照：

| 模型（榜单上的行） | 智能指数 | 单任务成本 |
|---|---|---|
| **GPT-6.2 Astra** | **本快照中没有这一行** | — |
| Claude Opus 5.5 (Max) | 57.6（第 1） | $5.98（第 188） |

Pelican Test，2026-10-20 读取的实时榜单：

| 排名 | 模型 | 结果数 | 得分 | 平均成本 |
|---|---|---|---|---|
| — | **openai/gpt-6.2-astra** | **无** | — | — |
| 1 | openai/gpt-6.1-sol | 6 | 3.79 | $0.026 |
| 2 | google/gemini-4-argon | 4 | 3.75 | $0.150 |
| 4 | anthropic/claude-opus-5.5 | 6 | 3.46 | $0.223 |

这说明：关于 GPT-6.2 Astra 的实测分数，什么也说明不了。对手的行只显示前沿模型之间的成本差距，可以作为下面创作者花费的背景，但不是对 GPT-6.2 Astra 的测量。

## 创作者报告的

发在 X 上的两条同提示词运行。数字按创作者自述：每条提示词各只跑了一次，设置不同，没有独立核实。点进链接可以两边一起看。

| 创作者 | 任务 | GPT-6.2 Astra | 对手 | 创作者说明 |
|---|---|---|---|---|
| [@Its_lakshya_ai](https://x.com/Its_lakshya_ai/status/2117955030506709468) | 骑自行车的鹈鹕 SVG | 与 Fable 5.5 Max 并排展示；未给出花费或耗时 | Fable 5.5 Max | "两个输出都非常惊艳，尤其是细节。" 请观众投票选更好的那个。 |
| [@leohuanfang](https://x.com/leohuanfang/status/2117973639333298513) | "Make me a video of 2 stickman fighting, anime style."（两个火柴人打斗，动漫风格） | $1.65（未给出耗时） | Claude Code 中的 Fable 5.5：66 分钟，$15.71 · 不使用工具的 Opus 5.5：8.5 分钟，$1.11 | 不使用工具的 Opus 说它无法渲染视频，于是写了一个 Python 脚本。 |

仅从这两条帖子能得出的结论：

- **价格。** 在火柴人提示词上，GPT-6.2 Astra 花费 $1.65：约为 Claude Code 中 Fable 5.5 的十分之一，比不使用工具的 Opus 5.5 多 $0.54。这一次运行中 Opus 更便宜，所以成本排名取决于对手是谁。
- **质量。** 鹈鹕那条帖子除了作者的赞扬，没有给出高下判断；火柴人那条也没有质量排名。
- **样本量。** 两条帖子，每个提示词每个模型各一次运行，来自两位作者。依赖结论前请自己重跑一遍。

## 重跑一次再相信对比

设置一变结果就变。把提示词粘到 [Lab 文本竞技场](https://www.sandbase.ai/arena/text?models=openai%2Fgpt-6.2-astra&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra)，选两三个模型；或者按[教程](tutorial.md)用 API。

## 更多实测

- [Lab Evals 榜单](https://www.sandbase.ai/leaderboards?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra)：Artificial Analysis 数据，2026-10-19 快照。
- [Lab Pelican Test](https://www.sandbase.ai/arena/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra)：同一提示词、同一评分方式，画作直接展示。
- [SandBase Lab 上的全部 AI 视频合集](https://www.sandbase.ai/lab/ai-videos?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra)。

---

Lab 数据：[Evals 榜单](https://www.sandbase.ai/leaderboards)（Artificial Analysis，2026-10-19 快照）与 [Pelican Test](https://www.sandbase.ai/arena/pelican-test)（2026-10-20 读取）。创作者数据：他们本人的帖子，已附链接，未经我们独立验证。
