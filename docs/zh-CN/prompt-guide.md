# GPT-6.2 Astra 提示词写法：如何为视频提示 GPT-6.2 Astra

[English](../prompt-guide.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

GPT-6.2 Astra 不直接输出视频。它写代码，作者再把它写出的页面录下来。本指南来自作者随视频公开的提示词。合集还年轻，目前只有两条写法，随着更多作者公开提示词，指南会继续扩充。每个例子都链接到它来自的帖子。

## 1. 给出一个简短任务，并说明交付物

任务清楚、交付物明确时，一行话就够了。两位作者把同一句话发给了几款模型：

- "Generate an SVG of a pelican riding a bicycle."（生成一张骑自行车的鹈鹕 SVG）（[@Its_lakshya_ai](https://x.com/Its_lakshya_ai/status/2117955030506709468)）：GPT-6.2 Astra 和 Fable 5.5 Max 拿到同一个任务，作者把两者的输出合成一段并排对比的视频。
- "Make me a video of 2 stickman fighting, anime style."（给我做一段两个火柴人打斗的视频，动漫风格）（[@leohuanfang](https://x.com/leohuanfang/status/2117973639333298513)）：同一句话分别交给 Claude Code 中的 Fable 5.5、不使用工具的 Opus 5.5，以及 GPT-6.2 Astra。

第二条帖子提醒了交付物的重要性：不使用工具的 Opus 5.5 说它无法渲染视频，于是改写了一个 Python 脚本。所以要在提示词里写明你要的输出，比如一个独立的 HTML 页面，这样得到的结果才能录制。

## 2. 对比时保持提示词不变

做对比时只换模型，别改文字。上面两条帖子都让所有模型拿到同样的措辞，花费和耗时才有可比性。作者报告的花费见[模型对比](model-comparison.md)。

## 可以直接用的提示词

```text
把 [主题] 做成一个从磁盘直接打开就能跑的独立 HTML 文件。

画面：[风格，例如 low-poly / 电影感 / 动漫 / 霓虹]，[氛围、光照、配色]。
运动：[什么在动、怎么动]。加载后自动播放 [10] 秒的序列，然后循环。
交互：[拖拽 = …，滚轮 = …，点击 = …，按键 = …]。
规则：[场景必须遵守的数字或约束]。

技术：
- 不要外部图片、字体、音频或模型，需要的内容用代码生成。
- 铺满视口，不出现滚动条。
- 完成前自检：页面加载零 console 错误，每个操作都可用。
- 只返回完整的 HTML，从 <!DOCTYPE html> 到 </html>，不要省略。
```

可以到 [Lab 文本竞技场](https://www.sandbase.ai/arena/text?models=openai%2Fgpt-6.2-astra&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra) 里，把这段同时跑在 GPT-6.2 Astra 和其他模型上对比；用 API 的方式见[教程](tutorial.md)。

---

引文均为短摘录并注明作者，完整提示词和视频请点链接。
