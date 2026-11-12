# GPT-6.2 Astra 教程：从提示词到视频

[English](../tutorial.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

四步把提示词变成 MP4。GPT-6.2 Astra 写网页，你来播放并录制。

## 1. 从喜欢的视频开始

在[合集](../../README.zh-CN.md)里点任意标题，进入它在 [SandBase Lab][lab] 的页面：视频、原帖，以及作者公开的提示词（如果有）。点 **复刻**，Lab 会打开文本竞技场，自动填好帖子内容并选中 GPT-6.2 Astra。登录后运行，就能拿到 HTML，并带实时预览。

作者没有公开提示词？照[提示词写法](prompt-guide.md)自己写一条，里面有填空模板。

## 2. 用同一个提示词对比模型

在[文本竞技场][arena]里，在 GPT-6.2 Astra 旁边再加一两个模型（例如 `anthropic/claude-opus-5.5`），跑一次。所有模型拿到同样的文字，每个结果都显示花费和耗时。这是在你自己的任务上验证[对比页](model-comparison.md)结论的最快方式。

## 3. 或者直接调用 API

GPT-6.2 Astra 在 SandBase 上的模型 ID 是 `openai/gpt-6.2-astra`，兼容 OpenAI。

1. 在[控制台][keys]创建 Key 并导出：`export SANDBASE_API_KEY=sk-sb-...`
2. 把提示词保存为 `prompt.txt`。
3. 运行：

```bash
jq -n --rawfile prompt prompt.txt '{
  model: "openai/gpt-6.2-astra",
  max_tokens: 128000,
  messages: [{role: "user", content: $prompt}]
}' |
curl -sS --max-time 900 https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- > response.json

jq -r '.choices[0].message.content' response.json | sed '/^```/d' > astra.html
jq '.usage' response.json
```

- `max_tokens: 128000`：单文件的长页面需要足够的空间。额度给小了，你会拿到被截断的页面，而且照样为这些 token 付费。
- `--max-time 900`：一个长页面可能要跑好几分钟。
- `sed '/^```/d'` 去掉模型可能加上的 Markdown 代码围栏。
- `usage` 显示计费的 token。价格见[模型页][model]。

用浏览器打开 `astra.html`。如果一片空白，打开开发者工具：常见原因是被截断的文件（加大 `max_tokens`）或 CDN 没加载（要求所有资源内联）。除了画面，也检查一下 UI。

## 4. 把页面录成视频

大多数作者是直接录屏。想每次得到一样的片段，可以用 [`scripts/record.mjs`](../../scripts/record.mjs) 无头录制：

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # 或使用本机 Chrome：export RECORD_CHANNEL=chrome
node scripts/record.mjs astra.html astra.mp4 12 1920 1080   # 12 秒，1080p
```

它按你给的尺寸打开页面，录指定秒数，再用 ffmpeg 转成 H.264 MP4。想要干净的效果，就在提示词里要求自动播放的序列或定长循环（见[提示词写法](prompt-guide.md)），让整个画面不依赖鼠标。

录制本身只有画面，想要声音就在剪辑里加。如果你自己录页面，记得捕获标签页音频，而不是麦克风。

## 安全运行生成的代码

这段 HTML 是你没读过的代码。单文件页面从本地打开通常没问题，但它仍然可以加载脚本、发起网络请求。对于不完全信任的内容，或者要批量运行很多页面，请使用 [SandBox][sandbox]：一个有时限、接触不到你的文件和 Key 的隔离环境。

## 分享

把视频发到 X，附上提示词并 @ GPT-6.2 Astra。想被收录，就[提交给我们](https://github.com/sandbase-lab/awesome-gpt-6-2-astra/issues/new?template=submit-video.yml)；通过后会先进入 Lab 合集，下一次每日同步时出现在本列表。

[lab]: https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra
[arena]: https://www.sandbase.ai/arena/text?models=openai%2Fgpt-6.2-astra&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra
[model]: https://www.sandbase.ai/model/openai/gpt-6.2-astra?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra
