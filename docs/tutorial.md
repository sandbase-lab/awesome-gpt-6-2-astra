# GPT-6.2 Astra tutorial: from prompt to video

English · [简体中文](zh-CN/tutorial.md) · [← Back to the collection](../README.md)

From a prompt to an MP4 in four steps. GPT-6.2 Astra writes a web page; you play it and record it.

## 1. Start from a video you like

Open any title in the [collection](../README.md) to reach its page on [SandBase Lab][lab]: the video, the original post and, when the creator shared one, the prompt. Press **Recreate**. Lab opens the text arena with the post loaded and GPT-6.2 Astra selected. Sign in, run it, and you get the HTML back, with a live preview.

No prompt shared? Write one with the [prompt guide](prompt-guide.md). It has a fill-in template.

## 2. Compare models on the same prompt

In the [text arena][arena], add one or two more models next to GPT-6.2 Astra (for example `anthropic/claude-opus-5.5`) and run once. Every model gets the same words, and each result shows its cost and time. It is the quickest way to check a claim from the [comparison page](model-comparison.md) on your own task.

## 3. Or call the API

GPT-6.2 Astra is `openai/gpt-6.2-astra` on SandBase, OpenAI-compatible.

1. Create a key in the [console][keys] and export it: `export SANDBASE_API_KEY=sk-sb-...`
2. Save your prompt as `prompt.txt`.
3. Run:

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

- `max_tokens: 128000`: a long single-file page needs room, and a limit that is too tight gives you a truncated page while you still pay for the tokens.
- `--max-time 900`: one long page can take several minutes.
- `sed '/^```/d'` removes Markdown fences if the model added them.
- `usage` shows the tokens you were billed for. Prices are on the [model page][model].

Open `astra.html` in a browser. If it is blank, open the developer console: the usual causes are a truncated file (raise `max_tokens`) or a CDN that did not load (ask for everything inline). Check the UI as well as the render.

## 4. Turn the page into a video

Most creators screen-record the page. To get the same clip every time, record it headlessly with [`scripts/record.mjs`](../scripts/record.mjs):

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # or use your installed Chrome: export RECORD_CHANNEL=chrome
node scripts/record.mjs astra.html astra.mp4 12 1920 1080   # 12 seconds at 1080p
```

It opens the page at the size you give, records for that many seconds, and converts to H.264 MP4 with ffmpeg. For a clean result, ask in the prompt for an autoplay sequence or a fixed-length loop (see [prompt guide §1](prompt-guide.md#1-give-one-short-task-and-name-the-deliverable)), so nothing depends on a mouse.

The recording is picture only, so add audio in the edit if you want sound. If you record the page yourself, capture the tab audio, not the microphone.

## Run generated code safely

The HTML is code you haven't read. Opening it from disk is usually fine for a single-file page, but it can still load scripts and make network requests. For anything you don't trust, or to run many pages automatically, use a [SandBox][sandbox]: an isolated environment with a time limit and no access to your files or keys.

## Share it

Post your video on X with the prompt and mention GPT-6.2 Astra. To have it added here, [submit it](https://github.com/sandbase-lab/awesome-gpt-6-2-astra/issues/new?template=submit-video.yml); accepted posts go into the Lab collection and show up in this list on the next daily sync.

[lab]: https://www.sandbase.ai/lab/ai-videos/gpt-6-2-astra?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra
[arena]: https://www.sandbase.ai/arena/text?models=openai%2Fgpt-6.2-astra&utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra
[model]: https://www.sandbase.ai/model/openai/gpt-6.2-astra?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-gpt-6-2-astra
